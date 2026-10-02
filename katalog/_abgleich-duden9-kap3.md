> Lehrerentscheid 02.10.2026: Empfehlungen der Gruppe „Katalog“ übernehmen; zusätzlich aufnehmen (statt „nicht aufnehmen“): Ungleichungen und Ungleichungssysteme, Kathetensatz und Höhensatz, negativer Streckfaktor, Intervallschachtelung, Beweise – mit Marke (Gymnasium/Vorrat) nach ziel.md § 1 („Klasse und Schulform filtern nicht; sie ordnen“). Satz von Vieta offen. Umsetzung in Katalog und Bank steht aus.

# Abgleich: Duden „Wissen – Üben – Testen, Mathematik 9“ (2017), Kapitel 3, gegen katalog/quadratische-funktionen.md

Messversuch 2 „Lehrbuch als Quelle für Katalog und Aufgabenbank“,
2026-10-02. Gelesen: PDF-Seiten 27–37 (11 Seiten, als Bild mit 85 dpi;
keine Seite musste mit 110 dpi nachgerendert werden). Die Klassenarbeiten
(S. 38–43) sind bewusst nicht gelesen. Katalogstand: Klon mathe-nachhilfe
(flach, letzter Commit); Bank: Klon aufgabenbank,
bank/quadratische-funktionen (Stand 26.09., Katalog-Commit c8c16ef).
Kein Wortlaut und keine Zahl aus dem Buch in den Bankzeilen; vom Buch
stammen nur Typ und Stufung.

## Kurzfassung

Das Buch bestätigt die Einheiten 1 bis 3 des Katalogs im Kern; einem
Blatt aus der Bank fehlen nach dem Buch vor allem die Sonderfälle der
Scheitelpunktform (Scheitel auf einer Achse, Dezimal- und Bruchzahlen),
mehrere Parabeln in einem Bild und – weil die Bank älter ist als vier
Katalogsprossen – die Nullstellenaufgaben mit genau einer oder keiner
Nullstelle. Neu für den Katalog bringt das Buch zwei Dinge für alle
(die Verschiebung nach oben oder unten an der Wertetabelle entdecken;
beschreiben, wo die Parabel fällt und wo sie steigt) und zwei als Vorrat
fürs Gymnasium (quadratische Ergänzung ohne Graph; größtes Rechteck bei
festem Zaun). Umgekehrt fehlen dem Buch fast alle prüfungsnahen Formen
des Katalogs: Verschieben und Spiegeln als Auftrag, Normalform
nachweisen, Schnittpunkte Gerade–Parabel, Fehler finden, Begründen. Ein
Drittel der Buchaufgaben (7 von 21: Wurzel- und Umkehrfunktion,
allgemeine Form, Rekonstruktion) liegt bewusst außerhalb des Eintrags.

## A „Im Buch, nicht im Katalog“

Gruppe „Bank“: nur zusätzliche Aufgaben an einer Sprosse, die im
Katalog schon steht – geht ohne Einzelbestätigung in die Bank. Gruppe
„Katalog“: ändert den Katalog (neue Sprosse, neuer Typ, Reihenfolge,
Streichung aus „Nicht aufgenommen“) – Entscheidung des Lehrers je Zeile;
die Spalte „Was der Schüler ohne sie nicht übt“ ist für diese Zeilen
so geschrieben, dass ohne Datei geurteilt werden kann. „Bankzeilen“
nennt die Zahl der Entwürfe in `neu-quadratische-funktionen-duden9.jsonl`.
Sprossennummern nach der heutigen Bank.

| Nr. | Gruppe | Typ | Buchstelle | Was der Schüler ohne ihn nicht übt | Vorschlag | Bankzeilen |
|---|---|---|---|---|---|---|
| A1 | Bank | Quadratische Funktion an ungeordnetem Term erkennen (x² steht hinten, mit Minus; zwei x-Glieder ohne Quadrat) | S. 28 Nr. 1 | Er erkennt die Parabel nur, wenn x² vorne steht. | e1 Kette 1, Vorstufe „Gerade oder Parabel ankreuzen“, Varianten 5–6. | 2 |
| A2 | Katalog | Parameter a, b, c der allgemeinen Form ablesen; Nicht-Parabeln 1/x² und x³ ausschließen | S. 28 Nr. 1 | Er liest a, b, c nicht aus einer beliebig geordneten allgemeinen Form ab und grenzt die Parabel nicht gegen Kehrwert und Kubik ab. | Nicht aufnehmen: allgemeine Form ist H und steht als Vorrat-Typ ohne Sprosse (Einheit 3); Kehrwert und Kubik gehören zu potenz-exponentialfunktionen.md. GYM. | 0 |
| A3 | Katalog | Wertetabelle zu x² + e neben der zu x² ausfüllen; jeder Wert um e verschoben, Scheitel (0 \| e) | S. 28 Nr. 2 | Er lernt „+ e schiebt nach oben“ als Ableseregel, sieht aber nie in Zahlen, dass jeder Funktionswert um genau e wächst – die Regel bleibt auswendig gelernt. | Aufnehmen, Einheit 1, neue Sprosse nach „Funktionswert und Punktprobe mit negativem x“ (NEU-tabelle-verschoben); für alle. Stützt sich auf LISUM-PH erster Block („Werte über Wertetabelle … Einfluss des Summanden e als Verschiebung in y-Richtung“). | 2 |
| A4 | Bank | Wertetabelle zu x² mit halben x-Werten (−2,5 … 2,5) | S. 28 Nr. 2 | Er quadriert in der Tabelle nur ganze Zahlen. | e1 Kette 1, Grundfall, Variante 6. | 1 |
| A5 | Bank | Zwei Parabeln in einem Bild, beide Gleichungen aufstellen (Scheitel auf der y-Achse; eine nach unten geöffnet) | S. 28 Nr. 3; S. 32 Nr. 9 | Er stellt Gleichungen nur an einer einzelnen Parabel auf und muss nie zuordnen, welcher Bogen welcher ist. | e2 Kette 1, Sprosse 6 „Gleichung aus dem Graphen aufstellen“, Varianten 4–5. | 2 |
| A6 | Bank | Scheitel ablesen, wenn e = 0 oder d = 0 ist, mit Dezimalzahl | S. 31 Nr. 4 | Bei (x + 3,5)² oder x² − 4,5 fehlt ihm ein Teil, und er setzt eine Zahl falsch ein. | e2 Kette 1, Sprosse 2 „d oder e negativ“, Varianten 4–5. | 2 |
| A7 | Bank | Gleichung zum Scheitel auf einer Achse, mit Dezimal- oder Bruchzahl | S. 31 Nr. 5 | Er stellt Gleichungen nur zu ganzzahligen Scheiteln abseits der Achsen auf. | e2 Kette 1, Sprosse 5 „Gleichung aus dem Scheitel aufstellen“, Varianten 4–5. | 2 |
| A8 | Bank | Parabel mit halbzahligem Scheitel skizzieren | S. 31 Nr. 8 (auch Nr. 4) | Er setzt den Scheitel nur auf Gitterpunkte. | e2 Kette 1, Sprosse 4 „Parabel aus der Gleichung skizzieren“, Variante 4. | 1 |
| A9 | Bank | Öffnung und Breite an a ankreuzen, a als Bruch | S. 31 Nr. 7 | Er entscheidet „breiter/schmaler“ nur an Dezimalzahlen. | e1 Kette 1, Sprosse 6, Varianten 4–5. | 2 |
| A10 | Bank | Merkmale gestreckter Parabel, Scheitel auf der y-Achse oder a als Bruch | S. 33 Nr. 11; S. 31 Nr. 6b | Die Bank hat dort nur ganzzahlige Faktoren und immer eine Klammer. | e2 Kette 1, Sprosse 12, Varianten 4–5. | 2 |
| A11 | Katalog | Term erst umformen, bis der Scheitel ablesbar ist: Produkt (x − a)(x + a), Faktor vor der Klammer, Bruchstrich | S. 31 Nr. 6 | Er erkennt eine Parabel in Produktform nicht als verschobene Normalparabel. | Nicht aufnehmen: Produktform ist Linearfaktorform (H, „Nicht aufgenommen“ [→GOST]); der Teil a·x² + e steckt in A10. GYM. | 0 |
| A12 | Katalog | Steigen und Fallen: angeben, für welche x die Parabel fällt und für welche sie steigt (Monotonie) | S. 32 Nr. 10; S. 33 Nr. 11 | Er sieht den Scheitel nur als Punkt, nicht als Stelle, an der die Parabel vom Fallen ins Steigen umschlägt – genau das braucht er bei jeder Wurfbahn („steigt bis …“). | Aufnehmen, Einheit 2, neue Sprosse nach „Parabel aus der Gleichung skizzieren“ (NEU-steigen-fallen); für alle mit „steigend/fallend“ (beide LISUM-Reihen nennen die Begriffe), „streng monoton“ nur GYM als Wort. | 3 |
| A13 | Bank | Nullstellen mit der p-q-Formel, wenn unter der Wurzel null oder eine negative Zahl steht, mit Gegenprobe am Scheitel | S. 33 Nr. 12b, c; Wissen S. 33 | Die Katalogsprossen stehen seit dem 29.09. im Katalog, die Bank (26.09.) hat sie nicht: Er rechnet nur Fälle mit zwei Nullstellen. | Leere Katalogsprossen füllen: e4 Kette 1 „Wert unter der Wurzel null: …“ und „… negativ: …“, je drei Zeilen, nach Sprosse 3 (alte 4–15 rücken um zwei). Nr. 12c mit Vorzahl ist durch Sprosse „vorher durch den Streckfaktor teilen“ gedeckt. | 6 |
| A14 | Katalog | Normalform ohne Graph in die Scheitelpunktform: vollständiges Quadrat erkennen, sonst quadratisch ergänzen | S. 34 Nr. 14; Wissen S. 30 | Er kommt von x² + px + q nur dann zum Scheitel, wenn ein Graph daneben steht; ohne Bild ist er hilflos. | Aufnehmen als Vorrat-Sprosse (H, GYM 9) am Ende der Kette Einheit 3, vor der Prüfungshöhe (NEU-quadr-ergaenzung). Der Katalog führt die Ergänzung schon als Vorrat-Typ und „nur Vorrat-Sprosse“, hat die Sprosse aber nicht in der Kette. Allgemeine Form mit a ≠ 1 (Beispiel 2, Nr. 14b, c) bleibt draußen. | 3 |
| A15 | Katalog | Allgemein zeigen, dass ax² + bx + c = a(x − d)² + e mit d = −b/(2a) | S. 33 Nr. 13 | Er leitet die Scheitelformel nicht allgemein her. | Nicht aufnehmen: allgemeine Form und Ergänzung als Verfahren sind H [→GOST]. GYM. | 0 |
| A16 | Katalog | Extremwertaufgabe: Rechteck mit festem Zaun, Flächenterm aufstellen, Scheitel als größter Wert | S. 34 Nr. 15; Wissen S. 34 | Er sieht den Scheitel nur an fertig gegebenen Bahnkurven als höchsten Punkt, nie als größten Wert einer Größe, deren Term er selbst aufgestellt hat. | Aufnehmen als Vorrat-Sprosse GYM 9 in Einheit 4 vor der Prüfungshöhe (NEU-extremwert). Lösungsweg ohne Ergänzung: Nullstellen von x(k − x) ablesen, Scheitel in der Mitte – damit auch für OS tragfähig. Sek-II-Fortsetzung mit Ableitung: extremalprobleme.md. | 2 |
| A17 | Katalog | a, b, c der allgemeinen Form aus drei Punkten | S. 34 Nr. 16 | Er rekonstruiert keine Parabel aus Punkten. | Nicht aufnehmen: „Rekonstruktion aus drei Punkten (H)“ steht unter „Nicht aufgenommen“, Ort rekonstruktion-von-funktionsgleichungen.md. GYM. | 0 |
| A18 | Katalog | Wurzelfunktion: maximale Definitionsmenge, Wertetabelle und Graph verschobener Wurzelfunktionen, Verschiebung/Spiegelung von √x erkennen, √x, ∛x, ∜x vergleichen | S. 36 Nr. 17–19; S. 37 Nr. 21 | Er lernt die Wurzelfunktion nicht als eigenen Funktionstyp kennen. | Nicht hier: LISUM-Reihe „Potenz- und Wurzelfunktionen“ (Kl. 10, nur Gymnasium, H); in potenz-exponentialfunktionen.md als offener Punkt „bleibt ungeführt“ vermerkt. Das Buch ist ein Beleg für diesen offenen Punkt. GYM. | 0 |
| A19 | Katalog | Umkehrfunktion: Spiegeln an y = x, Gleichung der Umkehrfunktion; x² nur für x ≥ 0 umkehrbar | S. 37 Nr. 20; Wissen S. 35–36 | Er bildet keine Umkehrfunktion. | Nicht hier, gleicher Ort wie A18. GYM. | 0 |

Zählung: Gruppe Bank 9 Zeilen (A1, A4–A10, A13) mit 20 Bankzeilen;
Gruppe Katalog 10 Zeilen (A2, A3, A11, A12, A14–A19), davon 4 mit
Empfehlung „aufnehmen“ (A3, A12, A14, A16; 10 Bankzeilen) und 6 mit
Empfehlung „nicht aufnehmen“; dazu B1 als Reihenfolge-Vorschlag.

### Platzhalter in der jsonl

| Platzhalter | Bedeutung | Ziel-Bankdatei | vorgeschlagene Stelle |
|---|---|---|---|
| NEU-tabelle-verschoben | A3 | e1.jsonl, Kette 1 | nach Sprosse 4 „Funktionswert und Punktprobe mit negativem x“; alte 5–11 rücken um eins |
| NEU-steigen-fallen | A12 | e2.jsonl, Kette 1 | nach Sprosse 4 „Parabel aus der Gleichung skizzieren“; alte 5–15 rücken um eins |
| NEU-quadr-ergaenzung | A14 | e3.jsonl, Kette 1 | nach Sprosse 8 „Aussagen … wahr oder falsch“, vor der Prüfungshöhe; alte 9–10 rücken um eins |
| NEU-extremwert | A16 | e4.jsonl, Kette 1 | nach Sprosse 12 „Schnittpunkte zweier Parabeln“, vor der Prüfungshöhe |

Ohne Platzhalter, aber an neuer Stelle der Bankdatei: die sechs Zeilen
zu A13 tragen sprosse 4 und 5 und den sprosse_text wortgleich aus
Katalogzeile 104; in der Bank rücken die alten Sprossen 4–15 um zwei
(der Mischlauf hat das so nummeriert).

## B „Reihenfolge weicht ab“

| Nr. | Gruppe | Buch | Katalog | Urteil |
|---|---|---|---|---|
| B1 | Katalog | Erst verschieben (3.1 x² + c; 3.2 (x − d)², dann (x − d)² + e), danach strecken und stauchen (a·x²), Spiegeln über a < 0. | Einheit 1 Normalparabel **und** Streckfaktor a·x² (fünf Sprossen), erst Einheit 2 Scheitelpunktform. | Buch und LISUM-PH (Block „y = (x + d)² + e“ vor Block „y = a·(x + d)² + e“) stehen gegen LS-AA, dem der Katalog folgt. Zwei Wege: (a) bleibt – Einheit 1 hat mit a·x² ein Merkmal am Scheitel im Ursprung, die Prüfungshöhe von Einheit 1 (Wertetabelle zu y = 3x², Fallschirm −3t²) braucht a, Einheit 2 bleibt bei 15 Sprossen; (b) die a·x²-Sprossen (5–9) wandern an den Anfang des Streckfaktor-Teils in Einheit 2 – die Leiter folgt LISUM und der P10-Gewichtung (Normalparabel verschieben ist Basis, Streckfaktor nur Erkennen), aber Einheit 1 verliert ihre Prüfungshöhe und Einheit 2 wächst auf rund 20 Sprossen, die Bank zieht in zwei Dateien um. Empfehlung (a); die Grundlage ist zwei Lehrwerke gegen eines plus LISUM, also dünn. |
| B2 | – | Verschiebung in y-Richtung und in x-Richtung getrennt, je mit Sonderform (x² + c, (x − d)²), erst dann beides. | Scheitel ablesen gleich an (x − d)² + e (Sprosse 1 „d und e positiv“), Verschieben als Auftrag „erst oben/unten, dann rechts/links, dann beides“. | Katalog genügt: Ablesen an der vollen Form ist ein Merkmal; die Sonderformen fehlen nur in der Bank und kommen über A6/A7. |
| B3 | – | Nullstellen (3.2 Nr. 12) vor dem Kapitel quadratische Gleichungen, mit Vorgriff auf Kap. 4.2. | Einheit 4 nach quadratische-gleichungen.md. | Katalog besser: das Verfahren ist dann gelernt. |
| B4 | – | Normalform → Scheitelpunktform gleich per quadratischer Ergänzung (S. 30); Ausmultiplizieren nur im Wissen, ohne Übung. | Erst Scheitelpunktform ausmultiplizieren und Normalform nachweisen (P10 2017-OS-K5d), Rückweg über den Graphen; Ergänzung Vorrat. | Katalog besser für OS und P10 (Ergänzung nie verlangt); für GYM siehe A14. |
| B5 | – | Monotonie nach dem Zeichnen der Scheitelpunktform (Nr. 10 nach Nr. 8–9). | Kein Typ. | Ort für A12 nach dem Buch gewählt (nach dem Skizzieren). |

## C „Im Katalog, im Buch nicht“

- Vorstufen „Minus und Quadrat“, „Nach oben oder nach unten?“ (nur
  nahe S. 31 Nr. 7), „Wo steht der Scheitel?“, „Was wird gleichgesetzt?“ –
  Einstieg
- Grundvorstellung: Zuwächse in der Wertetabelle, Lineal oder Bogen –
  Blatt 0
- Funktionswert und Punktprobe an der Parabel (Einheit 1 und 3) – P10
- Wertetabelle zu a·x² ausfüllen und unter mehreren zuordnen
  (2026-FOR-B1e) – P10
- Parabel zu a·x² über verdoppelte oder halbierte Werte zeichnen (Buch:
  nur Bild im Wissen S. 29) – Kern
- Parabelgleichung zum Graphen über Öffnung und Startwert ankreuzen
  (2015-OS-K4b) – P10
- Verschieben als Auftrag, neue Gleichung angeben (2015-OS-B1i,
  2017-OS-K5e) – P10
- An der x-Achse und an der y-Achse spiegeln als Auftrag (2020-OS-K3d) –
  P10
- Parabel zu Eigenschaften angeben (2018-OS-K5d), Lage zweier Parabeln
  begründen (2026-FOR-K5d) – P10
- Aussagen zur Parabel wahr/falsch (2018-OS-K5a) – P10
- y-Achsenabschnitt q ablesen (Buch: nur Wissen S. 30) – Kern
- Scheitelpunktform ausmultiplizieren, Normalform nachweisen
  (2017-OS-K5d; Buch nur Wissen) – P10
- Scheitel einer Normalform-Parabel am Graphen ablesen und
  Scheitelpunktform aufstellen (2025-OS-K5b) – P10
- Nullstellen aus der Scheitelpunktform durch Wurzelziehen; Zahl der
  Nullstellen am Scheitel begründen (Buch nur über D) – Kern
- Nullstellen mit Wurzel und Näherungswert (2025-OS-K5c) – P10
- Argument zu gegebenem Funktionswert (2023-OS-K4c) – P10
- Schnittpunkte Gerade–Parabel, Berührpunkt, kein gemeinsamer Punkt,
  Punktprobe als Nachweis, Gerade ohne gemeinsamen Punkt angeben,
  Schnittpunkte zweier Parabeln – P10 und LISUM G
- Fehler finden (alle Einheiten) – Pflicht
- Begründen (alle Einheiten; S. 33 Nr. 13 ist ein Nachweis auf H) –
  Pflicht
- Modellieren mit Wurfparabel und Bauwerk (Buch: nur das Rechteck der
  Extremwertaufgabe) – Pflicht

## Befunde außerhalb der Tabellen

1. Vier Katalogsprossen der Einheit 4 sind in der Bank leer: „Wert
   unter der Wurzel null/negativ“ bei den Nullstellen und bei den
   Schnittpunkten (Katalogzeile 104; vermutlich mit
   `_vorschlaege-2026-09-29.md` nach dem Bankstand 26.09. in den Katalog
   gekommen). Das Buch füllt die beiden Nullstellen-Sprossen (A13); die
   beiden Schnittpunkt-Sprossen („die Gerade berührt die Parabel“, „kein
   gemeinsamer Punkt“) bleiben leer – das Kapitel hat keine
   Gerade-Parabel-Aufgabe.
2. Das Prüfskript meldet im unveränderten Bestand vier Abweichungen:
   e4-k2-s2-v1 bis v3 „sprosse_text nicht wortgleich in Zeile 25“ (der
   Begründen-Text der Katalogzeile 25 ist jünger als die Bank) und
   „weg.jsonl: Dateiname“. Nicht von diesem Versuch.
3. Mengen: Die Bank-Gruppe schiebt sechs Sprossen über die Sollmenge
   (Vorstufe 6 statt 4, Grundfall 6 statt 5, Sprosse 4–5 statt 3) –
   das Prüfskript warnt. Wenn die Bank-Gruppe ohne Einzelbestätigung
   eingeht, sollte die Regel sagen, ob Zusatzvarianten über die Menge
   hinaus erlaubt sind oder eine ältere Variante ersetzen.
4. Schreibweise: Das Buch schreibt f(x) = (x − d)² + e mit S(d | e) und
   „Normalform“ für x² + px + q – wie der Katalog nach P10, gegen die
   LISUM-Pluszeichenform. Ein weiterer Beleg für die Katalogwahl.
5. Die beiden Extremwert-Zeilen haben keine Skizze; nach unterrichtsblatt
   3.5 (Sachaufgabe mit Figur) gehört beim Einbau ein Rechteck mit
   Beschriftung dazu.
6. `quelle`: alle Zeilen tragen die Zeilen 101–104 des heutigen
   Katalogs; das Prüfskript bestätigt den sprosse_text an diesen Zeilen
   für alle Zeilen an bestehenden Sprossen.

## Anhang: Aufgabenliste des Kapitels

Schwierigkeit nach dem Läufersymbol des Buchs und dem Inhalt; die
Graustufen der Symbole sind bei 85 dpi nicht sicher zu trennen, die
Angabe ist eine Einschätzung.

### 3.1 Die quadratische Funktion (S. 27–28), 3 Übungen
| S. | Nr. | Typ | Schw. | Form |
|---|---|---|---|---|
| 28 | 1 | Quadratische Funktionen unter sechs Gleichungen erkennen (auch 1/x², x³, ungeordnet), a, b, c angeben | leicht | Ankreuzen + Ablesen |
| 28 | 2 | Wertetabelle zu x² + c und x² − c mit halben x, Graphen zeichnen | leicht | Tabelle + Zeichnen |
| 28 | 3 | Drei nach oben/unten verschobene Normalparabeln: Scheitel und Term | leicht | Ablesen (Lücke) |

### 3.2 Eigenschaften und Graphen (S. 29–34), 13 Übungen
| S. | Nr. | Typ | Schw. | Form |
|---|---|---|---|---|
| 31 | 4 | Scheitel von (x − d)² (auch Dezimal-d), mit Schablone zeichnen | leicht | Lücke + Zeichnen |
| 31 | 5 | Gleichung zum Scheitel, Scheitel auf einer Achse, Dezimal/Bruch | leicht | Rechnen (Umkehrung) |
| 31 | 6 | Term umformen, bis der Scheitel ablesbar ist (Produkt, Faktor, Bruchstrich) | mittel | Umformen |
| 31 | 7 | Öffnung und gestreckt/gestaucht zu a·x² (negativ, periodisch, Bruch) | leicht | Ankreuzen (Tabelle) |
| 31 | 8 | Graph zur Scheitelpunktform zeichnen, auch Dezimal-Scheitel | mittel | Zeichnen |
| 32 | 9 | Gleichungen von sechs verschobenen/gespiegelten Normalparabeln aus zwei Bildern | mittel | Ablesen, Aufstellen |
| 32 | 10 | Monotonieverhalten nach Skizze | mittel | Skizzieren + Beschreiben |
| 33 | 11 | Eigenschaften gestreckter Parabeln: Scheitel, Monotonie (Dezimal, Bruch) | mittel | Beschreiben |
| 33 | 12 | Nullstellen: zwei, keine, eine (einmal mit Vorzahl) | mittel | Rechnen |
| 33 | 13 | Allgemeine Form in allgemeine Scheitelpunktform (d = −b/2a) | schwer | Nachweis |
| 34 | 14 | Normalform oder allgemeine Form erkennen, in Scheitelpunktform umformen, Scheitel, zeichnen | schwer | Zuordnen + Umformen + Zeichnen |
| 34 | 15 | Rechteckiger Stall mit festem Zaun, größte Fläche | schwer | Sachaufgabe (Extremwert) |
| 34 | 16 | a, b, c aus drei Punkten | schwer | Rechnen (LGS) |

### 3.3 Wurzelfunktionen als Umkehrfunktionen (S. 35–37), 5 Übungen
| S. | Nr. | Typ | Schw. | Form |
|---|---|---|---|---|
| 36 | 17 | Maximale Definitionsmenge von Wurzeltermen | mittel | Lücke (Mengenschreibweise) |
| 36 | 18 | Wertetabelle zu drei verschobenen Wurzelfunktionen, runden, zeichnen | mittel | Tabelle + Zeichnen |
| 36 | 19 | Verschiebung/Spiegelung von √x an zwei Graphen beschreiben | mittel | Beschreiben |
| 37 | 20 | Graph von √(x − c) an y = x spiegeln, Umkehrfunktion angeben | schwer | Zeichnen + Umkehrung |
| 37 | 21 | √x, ∛x, ∜x zeichnen und vergleichen, Wirkung des Exponenten | schwer | Zeichnen + Begründen |
