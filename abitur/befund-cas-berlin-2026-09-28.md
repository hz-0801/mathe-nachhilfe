# Befund: Berliner CAS-Hefte 2017/2018 gegen die WTR-Fassung

Stand 28.09.2026 (Auftrag Nacht 2026-09-28, Teil 3). Gemessen, nicht erfasst:
kein Katalogeintrag. Frage aus abi.md § 9: Die Berliner CAS-Hefte sind
durchgehend eigene Fassungen ohne „CAS:"-Präfix; welche Teilaufgaben bekommen
beim Nachtrag eine eigene Zeile? Das Urteil fällt im Chat; hier stehen nur die
Messung und die Art jeder Abweichung.

## Verfahren

- Hefte unter hefte/abi/ (Dateinamen nach abi-quellen.md § 8, lokal): 2017-be-gk
  und -cas, 2017-be-lk und -cas, 2018-be-gk und -cas, 2018-be-lk und -cas; Text
  mit `pdftotext -layout`. Werkzeug: `werkzeuge/cas-vergleich.py` (v0.1, neu in
  diesem Auftrag); Aufruf je Heft, für die LK-Hefte mit dem Brandenburger
  CAS-Heft desselben Jahres als drittem Heft.
- Normierung wie beim Pool-Abgleich (iqb-quellen.py): nur Buchstaben und
  Ziffern, ohne Seitenköpfe, Fußzeilen und die Wörter CAS/WTR. Je Teilaufgabe
  der CAS-Fassung wird die WTR-Teilaufgabe derselben Aufgabe mit dem
  ähnlichsten Text gesucht; die Zuordnung ist von Hand nachgelesen und dort
  berichtigt, wo ein Zwischenstamm (Text zwischen zwei Teilaufgaben) die
  Ähnlichkeit verzerrt. Eine Abweichung im Zwischenstamm gehört zur folgenden
  Teilaufgabe. Wo nur ein Formelbild anders gesetzt ist, entschied das
  Seitenbild (2018-be-lk 1.1, 2.1).
- **wortgleich** heißt: Text gleich (rein redaktionelle Änderungen ohne Folge für
  Zahlen, Auftrag und BE eingeschlossen, jeweils vermerkt) **und** gleiche BE –
  wie „uebernommen" im Nachtragsmodus von abi-bau.py (abi.md § 7). Alles andere
  ist **abweichend**.
- **Art der Abweichung:** *Zahl* – nur Zahlenwerte der Angabe oder des Ereignisses
  anders, Auftrag gleich; *Werkzeug* – eine Rechenhilfe fällt weg oder kommt
  dazu (Kontrollangabe, vorgegebene Ableitung, Stammfunktion, Ebenengleichung
  oder Lösung, Hinweis auf die hinreichende Bedingung, „rechnerisch"), der
  Auftrag bleibt; *Auftrag* – bei gleichem Gegenstand ist ein Auftrag geändert,
  ergänzt oder gestrichen; *Zuschnitt* – die Aufträge zweier WTR-Teilaufgaben
  neu verteilt; *ganze Aufgabe* – Teilaufgabe ohne WTR-Gegenstück oder mit
  anderer Frage; *nur BE* – Text wortgleich, BE anders. Mehrere Arten mit „+".

## Übersicht

| Heft | Seiten (Soll abi-pruefungen.md § 2) | Teilaufgaben der CAS-Fassung | wortgleich | abweichend | davon nur BE | davon schon als Zeile eines BB-CAS-Hefts | abweichend ohne Katalogzeile |
|---|---|---|---|---|---|---|---|
| 2017-be-gk-cas | 8 (8) | 34 | 18 | **16** | 5 | 0 | 16 |
| 2017-be-lk-cas | 9 (9) | 36 | 17 | **19** | 9 | 9 (2017-bb-ea-cas 2.2, 3.1, 4.2) | 10 |
| 2018-be-gk-cas | 10 (10) | 37 | 21 | **16** | 2 | 0 | 16 |
| 2018-be-lk-cas | 9 (9) | 43 | 27 | **16** | 7 | 13 (2018-bb-ea-cas 2.1, 2.2, 3.1) | 3 |

Die BE-Summe jeder Aufgabe ist in beiden Fassungen gleich (40/20 im Grundkurs,
50/25 im Leistungskurs). Die WTR-Hefte 2017-be-gk und 2018-be-gk sind erfasst;
von 2017-be-lk und 2018-be-lk sind nur die mit bb-ea gleichlautenden Aufgaben
erfasst (abi-pruefungen.md § 2), die eigenen Aufgaben (2017: 1.1, 2.1, 3.1;
2018: 2.2, 3.1) haben auch in der WTR-Fassung keine Zeile.

## 2017-be-gk-cas (WTR: 2017-be-gk)

| Teilaufgabe CAS | WTR | BE WTR/CAS | Urteil | Art | Unterschied |
|---|---|---|---|---|---|
| 1.1 Einleitung | Einl. | – | wortgleich | – | redaktionell: „des Brückenteils" statt „des Bauelements" |
| 1.1 a | a | 9/8 | abweichend | Werkzeug | Kontrollangabe f′(x) entfällt, A und B bleiben |
| 1.1 b | b | 6/4 | abweichend | nur BE | – |
| 1.1 c | c | 6/5 | abweichend | nur BE | – |
| 1.1 d | e | 5/5 | wortgleich | – | Buchstabe verschoben (Schnittwinkel der Tangenten) |
| 1.1 e | – | –/10 | abweichend | ganze Aufgabe | neu: Graph liegt zwischen den Geraden g_u und g_o; Stelle und Wert des kleinsten vertikalen Abstands |
| 1.1 f | d | 5/8 | abweichend | Auftrag | Volumen des grau dargestellten Brückenteils samt Stütze am rechten Rand statt des Brückenteils allein |
| (WTR 1.1 f) | f | 9/– | – | – | entfällt: Rekonstruktion g(x) = ax³ + bx² + c |
| 1.2 a | a, b | 11 + 3/5 | abweichend | Zuschnitt | Schnittpunkte mit den Achsen (aus WTR a) und Graph zeichnen (WTR b) |
| 1.2 b | a | –/9 | abweichend | Zuschnitt + Auftrag + Werkzeug | Ableitung bilden und Ableitungsregeln angeben (Kontrollangabe f′ entfällt), Extrempunkte (aus WTR a), dazu die zwei Wendepunkte |
| 1.2 c | c | 5/5 | wortgleich | – | redaktionell (Tippfehler „an die maximale") |
| 1.2 d | d | 5/3 | abweichend | Werkzeug | Nachweis der vorgegebenen Stammfunktion F entfällt, F nicht mehr angegeben |
| 1.2 e | e | 9/7 | abweichend | nur BE | – |
| 1.2 f | – | –/4 | abweichend | ganze Aufgabe | neu: Punkt Q mit 45° Gefälle |
| 1.2 g | f | 7/7 | wortgleich | – | Buchstabe verschoben |
| 2.1 a–d | a–d | 7, 5, 4, 4 | wortgleich | – | – |
| 2.2 a, b, e | a, b, e | 2, 4, 5 | wortgleich | – | – |
| 2.2 c | c | 5/6 | abweichend | Auftrag | Winkel der Seitenwand ABFE mit der Deckelfläche EFS statt mit der Grundfläche |
| 2.2 d | d | 4/3 | abweichend | nur BE | – |
| 3.1 a–d, f | a–d, f | 2, 3, 2, 3, 4 | wortgleich | – | – |
| 3.1 e | e | 2/2 | abweichend | Zahl + Auftrag | 250 statt 20 Geräte; gefragt die wahrscheinlichste Anzahl fehlerhafter statt P(keines fehlerhaft) |
| 3.1 g | g | 4/4 | abweichend | Zahl + Auftrag | 90 % statt 95 %; mindestens 500 fehlerfreie statt mindestens ein fehlerhaftes Gerät |
| 3.2 a, b, e | a, b, e | 5, 3, 4 | wortgleich | – | – |
| 3.2 c | c | 5/4 | abweichend | nur BE | – |
| 3.2 d | d | 3/4 | abweichend | Auftrag | Wahrscheinlichkeit für genau i Eintritte (i = 0 … 30), Behauptung „genau fünf Werte über 10 %" statt „Hälfte der Fälle unter 5 %" |

Poolbezug: 3.1 ist wortgleich mit der CAS-Poolfassung 2017MgrundlegendBStochastikCAS
(e = 2 c, g = 2 e); der CAS-Zweig 2017-ga-B ist nicht erfasst (Reserve), die
WTR-Fassung 3.1 zeigt auf 2017MgrundlegendBStochastikWTR1.

## 2017-be-lk-cas (WTR: 2017-be-lk)

| Teilaufgabe CAS | WTR | BE WTR/CAS | Urteil | Art | Unterschied |
|---|---|---|---|---|---|
| 1.1 a | a | 12/13 | abweichend | Werkzeug + Auftrag | f″ nicht mehr vorgegeben („ohne Nachweis dürfen Sie … verwenden" entfällt); dazu „Weisen Sie nach, dass f keine Wendestellen besitzen kann" |
| 1.1 b | b | 6/5 | abweichend | nur BE | – |
| 1.1 c | c | 9/7 | abweichend | nur BE | redaktionell: „Länge der schiefen Ebene" statt „Entfernung" |
| 1.1 d | d | 8/8 | wortgleich | – | – |
| 1.1 e | – | –/6 | abweichend | ganze Aufgabe | neu: Modell g(x) = 5a/(x² − a) + b bei gleicher Höhe und Breite, sichtbare Fläche unter y = 9 |
| 1.1 f | e | 6/3 | abweichend | nur BE | Rotationsvolumen |
| 1.1 g | f | 9/8 | abweichend | nur BE | Modell g(x) = ax⁴ + bx² + c |
| 1.2 a, c, e, f | a, c, d, e | 6, 9, 6, 10 | wortgleich | – | c: Satz „1 LE = 150 m" steht hinter der neuen d; f: Verweis „Teilaufgabe e)" statt „d)" – redaktionell |
| 1.2 b | b | 10/9 | abweichend | nur BE | = 2017-bb-ea-cas-B2.2b |
| 1.2 d | – | –/5 | abweichend | ganze Aufgabe | neu: identische Graphen der Schar zu a₁, a₂ durch R(2 \| 4) = 2017-bb-ea-cas-B2.2d |
| 1.2 g | f | 9/5 | abweichend | nur BE | = 2017-bb-ea-cas-B2.2g |
| 2.1 a, d, e, f | a, d, e, f | 6, 5, 4, 3 | wortgleich | – | – |
| 2.1 b | b | 4/3 | abweichend | nur BE | – |
| 2.1 c | c | 3/4 | abweichend | Auftrag | dazu: Abstand des Befestigungspunkts von einer seitlichen Kante |
| 2.2 a, b, d | a, b, d | 5, 4, 3 | wortgleich | – | – |
| 2.2 c | c | 5/4 | abweichend | nur BE | = 2017-bb-ea-cas-B3.1c |
| 2.2 e | e | 3/4 | abweichend | Werkzeug | zum Nachweis der Vordachlänge die y-Koordinate 5,98 der Kante selbst bestimmen (WTR gibt sie in f vor) = 2017-bb-ea-cas-B3.1e |
| 2.2 f | f | 5/5 | abweichend | Werkzeug | Vorgabe „y-Koordinate 5,98" entfällt = 2017-bb-ea-cas-B3.1f |
| 3.1 a, d, e | a, d, e | 3, 3, 5 | wortgleich | – | – |
| 3.1 b | b | 10/9 | abweichend | nur BE | – |
| 3.1 c | c | 4/5 | abweichend | Zahl | Ereignis D: höchstens 2 statt höchstens ein Kleinwagen |
| 3.2 a | a | 8/8 | abweichend | Zahl | Ereignis C: unter 100 mehr als 78 und weniger als 92 statt unter 20 mehr als 18 = 2017-bb-ea-cas-B4.2a |
| 3.2 b | b | 4/4 | abweichend | Auftrag | Frage umgekehrt: höchstens auswählen, damit unter 98 % = 2017-bb-ea-cas-B4.2b |
| 3.2 c, e | c, e | 5, 4 | wortgleich | – | – |
| 3.2 d | d | 4/4 | abweichend | Zahl | im Zwischenstamm 6 % statt 5 % Stornierungen = 2017-bb-ea-cas-B4.2d |

1.2 Straßenverlauf, 2.2 Zelt und 3.2 Freizeit sind in allen Teilaufgaben
wortgleich mit 2017-bb-ea-cas 2.2, 3.1 und 4.2 (Text; die Fußzeilen der
Brandenburger Fassung abgezogen); die neun abweichenden Teilaufgaben sind dort
schon Zeilen. 2.2 Zelt ist die CAS-Poolfassung 2017MerhoehtBAGLAA2CAS2.

## 2018-be-gk-cas (WTR: 2018-be-gk)

| Teilaufgabe CAS | WTR | BE WTR/CAS | Urteil | Art | Unterschied |
|---|---|---|---|---|---|
| 1.1 a | a | 3/3 | wortgleich | – | – |
| 1.1 b | b | 5/4 | abweichend | nur BE | – |
| 1.1 c | c | 6/7 | abweichend | Werkzeug + Auftrag | Kontrollergebnis g′(x) entfällt; dazu mittlere Steigung des Aufsprunghangs zwischen C und U |
| 1.1 d | d | 4/3 | abweichend | nur BE | – |
| 1.1 e | – | –/4 | abweichend | ganze Aufgabe | neu: knickfreie geradlinige Fortsetzung des Aufsprunghangs in P(110 \| g(110)) |
| 1.1 f | e, f | 6 + 10/11 | abweichend | Zuschnitt + Auftrag | Flugbahn bestimmen (WTR e) und Landepunkt L (WTR f) in einer Teilaufgabe, Skizze der Flugbahn entfällt, dazu der Winkel zwischen Flugbahn und Hang in L |
| 1.1 g | g | 6/8 | abweichend | Auftrag + Werkzeug | dazu das Intervall, in dem der Abstand mindestens 5 m beträgt; Hinweis zur hinreichenden Bedingung entfällt |
| 1.2 Einleitung | Einl. | – | abweichend | Werkzeug | Hinweis „Die Graphen … sind in der Anlage dargestellt" entfällt (keine Anlage) |
| 1.2 a | a | 2/4 | abweichend | Auftrag | Verhalten auch für x → −∞ |
| 1.2 b | b | 7/6 | abweichend | Werkzeug + Auftrag | S(0 \| 1) nicht mehr vorgegeben, dazu der zweite Schnittpunkt T; Kontrollangabe f′ entfällt; Winkel in S wie WTR |
| 1.2 c | c | 9/4 | abweichend | Werkzeug + Auftrag | Stammfunktion F nicht mehr vorgegeben, Nachweis der gemeinsamen Nullstelle entfällt; statt „A berechnen" „ist A größer als 1/10?" |
| 1.2 d | d | 4/4 | abweichend | Werkzeug | Hinweis „hinreichende Bedingung nicht erforderlich" entfällt |
| 1.2 e | (f) | 5/4 | abweichend | ganze Aufgabe | kleinste Steigung und größtes Intervall mit f′(x) ≤ −0,2 anstelle von WTR f („Stelle mit Steigung kleiner als −0,222 nachweisen") |
| 1.2 f | e | 4/4 | abweichend | Werkzeug | Kontrollangabe s(x) = −0,19x + 1,48 kommt dazu |
| 1.2 g | – | –/5 | abweichend | ganze Aufgabe | neu: größter vertikaler Abstand zwischen s und f in [2; 6] |
| 1.2 h | g | 9/9 | abweichend | Auftrag | dazu: genau eine positive Stelle gleicher Steigung von f und h_W nachweisen, Steigung angeben |
| 2.1 a–e | a–e | 4, 3, 6, 2, 5 | wortgleich | – | – |
| 2.2 a–e | a–e | 3, 3, 3, 6, 5 | wortgleich | – | – |
| 3.1 a, c–e | a, c–e | 2, 5, 2, 6 | wortgleich | – | – |
| 3.1 b | b | 5/5 | abweichend | Zahl | Ereignis B: von den übrigen 9 mindestens vier statt höchstens eins |
| 3.2 a | a | 4/4 | abweichend | Zahl | Ereignis B mit 200 Bildschirmen, mehr als 30 und weniger als 50 statt 50, mehr als 10 und weniger als 15 |
| 3.2 b–g | b–g | 2, 3, 4, 3, 2, 2 | wortgleich | – | – |

Poolbezug: die Poolaufgaben von 2018-be-gk (2.2, 3.2) sind in der CAS-Fassung
wortgleich mit dem WTR-Heft bis auf 3.2 a; die CAS-Poolfassungen 2018
grundlegend enthalten die Aufgabe Bildschirme nicht (Anfangszeilen der
fünf 2018MgrundlegendB…CAS-Dateien gelesen).

## 2018-be-lk-cas (WTR: 2018-be-lk)

| Teilaufgabe CAS | WTR | BE WTR/CAS | Urteil | Art | Unterschied |
|---|---|---|---|---|---|
| 1.1 a, b | a, b | 8, 3 | wortgleich | – | – |
| 1.1 c | c | 4/3 | abweichend | nur BE | = 2018-bb-ea-cas-B2.1c |
| 1.1 d | d | 5/5 | abweichend | Werkzeug | Kontrollangabe f_a′(x) entfällt = 2018-bb-ea-cas-B2.1d |
| 1.1 e | e | 8/7 | abweichend | nur BE | = 2018-bb-ea-cas-B2.1e |
| 1.1 f | f | 6/5 | abweichend | nur BE | = 2018-bb-ea-cas-B2.1f |
| 1.1 g | g | 7/5 | abweichend | Werkzeug | „Ermitteln Sie diese beiden Stellen rechnerisch" statt „Bestimmen Sie …" = 2018-bb-ea-cas-B2.1g |
| 1.1 h | – | –/5 | abweichend | ganze Aufgabe | neu: Fassungsvermögen bei 10 % Materialanteil = 2018-bb-ea-cas-B2.1h |
| 1.1 i, j | h, i | 2, 7 | wortgleich | – | i: nur das Formelbild anders gesetzt (Seitenbild) |
| 1.2 a, c, h | a, c, h | 6, 2, 6 | wortgleich | – | – |
| 1.2 b | b | 7/5 | abweichend | nur BE | = 2018-bb-ea-cas-B2.2b |
| 1.2 d | d | 6/6 | abweichend | Auftrag | Koordinaten zweier Punkte mit Tangentenanstieg 1,5 ermitteln statt „zeigen, dass es genau zwei gibt" = 2018-bb-ea-cas-B2.2d |
| 1.2 e | e | 9/8 | abweichend | nur BE | redaktionell „durch die Graphen" statt „durch Teile der Graphen" = 2018-bb-ea-cas-B2.2e |
| 1.2 f | f | 9/9 | abweichend | Werkzeug | Schnittpunkte von G₂ und K selbst ermitteln statt P₁, P₂ nachweisen; Plane wie WTR = 2018-bb-ea-cas-B2.2f |
| 1.2 g | g | 5/3 | abweichend | nur BE | = 2018-bb-ea-cas-B2.2g |
| 1.2 i | – | –/5 | abweichend | ganze Aufgabe | neu: kleinster Abstand der betonierten Fläche zum Teichrand = 2018-bb-ea-cas-B2.2i |
| 2.1 a–e | a–e | 4, 3, 5, 4, 3 | wortgleich | – | – |
| 2.1 f | f | 6/6 | abweichend | Werkzeug | Ebenengleichung von EFG nicht mehr vorgegeben (Seitenbild) = 2018-bb-ea-cas-B3.1f |
| 2.2 a, b, d–f | a, b, d–f | 3, 3, 3, 5, 4 | wortgleich | – | – |
| 2.2 c | c | 5/3 | abweichend | nur BE | – |
| 2.2 g | g | 2/4 | abweichend | Werkzeug + Auftrag | Lösung t = ±2√2 nicht mehr angegeben, dazu „Geben Sie alle Lösungen der Gleichung an" |
| 3.1 a | a | 6/6 | abweichend | Auftrag | zusätzliches Ereignis A3 (genau einer oder genau drei) |
| 3.1 b–e | b–e | 5, 5, 4, 5 | wortgleich | – | – |
| 3.2 a–f | a–f | 4, 5, 5, 2, 3, 6 | wortgleich | – | Brillenträger: die Berliner CAS-Fassung ist die WTR-Fassung; 2018-bb-ea-cas 4.2 weicht davon ab (d, e andere Aufgaben, a/b mit 5/4 statt 4/5 BE) |

1.1 Vase, 1.2 Gartenteich und 2.1 Museum sind in allen Teilaufgaben wortgleich
mit 2018-bb-ea-cas 2.1, 2.2 und 3.1; die dreizehn abweichenden Teilaufgaben
sind dort schon Zeilen. 2.1 Museum ist die CAS-Poolfassung 2018MerhoehtBAGLAA2CAS1.

## Was die Messung zeigt (ohne Urteil)

- Abweichende Teilaufgaben je Heft: 16, 19, 16, 16 von 34, 36, 37, 43.
- Ganz wortgleiche Aufgaben: 2017-be-gk 2.1; 2018-be-gk 2.1, 2.2; 2018-be-lk 3.2.
- Die Arten über alle vier Hefte (Mehrfachnennungen; je Heft gk17, lk17, gk18,
  lk18): nur BE 23 (5, 9, 2, 7), Werkzeug allein oder mit anderem 17 (3, 3, 6,
  5), Auftrag allein oder mit anderem 19 (6, 3, 7, 3), Zahl allein oder mit
  anderem 7 (2, 3, 2, 0), ganze Aufgabe 9 (2, 2, 3, 2), Zuschnitt 3 (2, 0, 1, 0).
- Ohne schon vorhandene Zeile blieben 16 + 10 + 16 + 3 = 45 Teilaufgaben; von
  den 35 abweichenden der beiden LK-Hefte sind 22 schon Zeilen der
  Brandenburger CAS-Hefte.
