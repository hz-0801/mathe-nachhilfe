Modell: Opus (Unteragent aus dem Chat verbessereBlaetter, 28.09.2026)

# Bericht – Katalog-Nachzug aus den Urteilen vom 28.09.2026

Auftrag: archiv/auftrag-katalog-nachzug-2026-09-29.md (gestartet
2026-09-28 23:32, Abschluss 2026-09-29). Umgebung: Linux-Klon statt
PowerShell, Push durch den Unteragenten (Vorgabe des Chats). Standdatei:
archiv/stand-katalog-nachzug-2026-09-29.md.

Prüfung vor und nach jedem Teil: `_pruef_katalog.py` über alle 72
Einträge und `_pruef_struktur.py`; Ausgabe vorher aufgehoben und
verglichen. Ergebnis nach Teil 1, 2 und 5: keine neuen Treffer. Ein
Zwischentreffer nach Teil 1 (Kennzahl 8: Verweis „bank.md“ in der
Änderungszeile von rationale-zahlen.md las sich als Katalogverweis)
ist im Text behoben, nicht im Skript. Die übrigen Unterschiede der
Ausgabe sind nur die Reihenfolge gleicher Zahlen in der Mengenausgabe
(„0,6“/„0,60“), nicht der Inhalt.

## Teil 1 – Katalog Sek I (Commit cebfd50)

Geänderte Dateien: katalog/lineare-gleichungen.md,
binomische-formeln.md, brueche-dezimalzahlen.md, prozentrechnung.md,
terme.md, rationale-zahlen.md, bruchrechnung.md, pythagoras.md; dazu
auftrag-katalog-nachzug.md und stand-katalog-nachzug.md angelegt.
Je Eintrag eine Zeile „- Änderungen 2026-09-28 (Urteile vom 28.09.):
…“ als letzte Zeile unter „Offene Punkte des Eintrags“ (dort steht die
einzige frühere Änderungszeile dieser Art, prozentrechnung.md; im Kopf
steht nur die Status-Zeile).

Eingefügt – 13 Sprossen/Vorstufen, dazu Vorstufenfrage und Umbenennung
binomische-formeln:

| Eintrag | eingefügt | Zahl |
|---|---|---|
| lineare-gleichungen | E2 Sprosse „x steht hinter dem Minus“; Erkennungsschritt „Was ist als Nächstes dran?“ vor Einheit 3 | 2 |
| binomische-formeln | E3 dritte Frage der Vorstufe „Welche davon können gar kein Binom sein?“; „kein Binom erkennen und begründen“ → „kein Binom begründen“ | 0 (+Frage, +Umbenennung) |
| brueche-dezimalzahlen | E5 neue Vorstufe „Wo entscheidet es sich?“, „Nullen anhängen“ von der Vorstufe zur Sprosse vor „verschieden viele Stellen“; E4 Sprosse „Stellen einzeln gegeben → Dezimalzahl“ | 2 |
| prozentrechnung | E2 „Überschlag über einen einfachen Bruch“; E3 „ein Prozent einer Einheit“ (Vorform); E4 „derselbe Teil, verschiedene Sätze“ | 3 |
| terme | E4 Vorstufe „Faktor vorgegeben, nur die Klammer füllen“; E3 „Minusklammer mit Zahlen auf zwei Wegen“ | 2 |
| rationale-zahlen | E2 „nur das Vorzeichen“ | 1 |
| bruchrechnung | E3 „Kontrolle: Ergebnis mal Teiler“; E1 „Hauptnenner und beide Erweiterungszahlen anschreiben“ | 2 |
| pythagoras | Erkennungsschritt „Satz oder Umkehrung?“ vor Einheit 2 | 1 |
| winkel-dreiecke | nichts (keine Kette Umkehrung dort) | 0 |

Abweichung von der Zählung des Auftrags: 13 statt 12. Die 12 der
Prüfliste zählen Teil A; die Vorstufe pythagoras aus Teil B kommt
dazu. „Überschläge beurteilen“ ist nach dem Urteil keine Sprosse und
hat keine Katalogzeile.

Abweichungen vom Wortlaut der Vorschlagsdatei, mit Grund:
- Ziffernfreiheit: „20 − x = 13“ → „zwanzig minus x gleich dreizehn“;
  „3 Einer, 0 Zehntel, 8 Hundertstel“ → in Worten; „60 € sind 10 %,
  20 %, 30 %“ → in Worten; „1 % von 1 m, 1 kg, 1 l“ → „ein Prozent von
  einem Meter, einem Kilogramm, einem Liter“; „6x + 15 = 3 · (__ + __)“
  → „zu sechs x plus fünfzehn ist der Faktor drei vor der Klammer
  vorgegeben, die beiden Glieder in der Klammer ergänzen“;
  „20 − (7 + 3)“ → „zwanzig minus (sieben plus drei)“, der zweite Weg
  „20 − 7 − 3“ nur als „dann Glied für Glied“; das Beispiel der
  Kontrolle bruchrechnung (3/20 · 4 = 3/5) entfällt.
- Kettenform lineare-gleichungen: Die Vorschlagsdatei setzt die Sprosse
  „nach negative Lösung, vor negative Vorzahl“; dazwischen steht
  „zweischrittig erst Strich dann Punkt (4×, mit Probe)“ – schon am
  Stand 808fd7c. Beides zugleich geht nicht; die Sprosse steht direkt
  vor „negative Vorzahl“ (nach „zweischrittig“), weil ihr Merkmal
  (Zeichen bei x) dorthin gehört.
- binomische-formeln: Die Vorschlagsdatei nennt drei Aussonder-Merkmale
  („Mittelglied fehlt, zwei Quadrate addiert, ein Glied kein
  Quadrat“). „Mittelglied fehlt“ allein ist falsch (x² − 9 ist die
  dritte Formel); die Frage streicht deshalb Terme, „bei denen zwei
  Quadrate ohne Mittelglied addiert sind oder ein äußeres Glied kein
  Quadrat ist“.
- brueche-dezimalzahlen E5: Die neue Vorstufe sagt „zu zwei
  Dezimalzahlen mit gleich vielen Stellen“, damit sie zum Grundfall
  passt; die Quellenklammer [MSK D2B; LS-AA Kl. 6 II 2] wandert mit
  „Nullen anhängen“ zur Sprosse.
- prozentrechnung E3: Das Urteil nennt „1 % einer Einheit“ Vorstufe;
  sie steht aber nach dem Grundfall (4×) und nach den Zehn-Prozent-
  Schritten. Sie trägt deshalb die Form des Nachbarn „… als Vorform“,
  nicht „(Vorstufe)“ – eine Vorstufe hinter dem Grundfall widerspräche
  „Grundfall zuerst“ und sprosse 0 = Vorstufe in bank.md. E2: die
  Taschenrechner-Sprosse bekommt „mit dem Überschlag verglichen“ (wie
  die Vorschlagsdatei).
- pythagoras: Die Datei hat keine Kette „Umkehrung“; die Umkehrung ist
  der Schluss der Kette Kathete (Einheit 2). Eine „(Vorstufe)“ mitten
  in der Kette ginge gegen die Form, deshalb steht die Vorstufe als
  Erkennungsschritt vor Einheit 2, neben „Welche Seite ist die
  längste?“ (dort steht schon „Vor Einheit 2 (Umkehrung)“). Zusatz im
  Schritt: „dann den Satz des Pythagoras und seine Umkehrung als
  Wenn-dann-Sätze nebeneinander schreiben“ – ohne ihn bliebe der
  Schritt beim Quadrat stehen. winkel-dreiecke.md Z. 125 ist ein
  offener Punkt, keine Kette; dort nichts eingefügt.

## Teil 2 – Katalog Sek II (Commit 2a296e5, Nachtrag im Abschluss)

Geänderte Dateien (16): kurvenuntersuchung, extremalprobleme, geraden,
abstaende, flaecheninhalt-durch-integration, binomialverteilung,
ableitungsregeln, funktionsklassen-und-eigenschaften,
skalarprodukt-und-winkel, stammfunktion-und-hauptsatz,
tangente-normale-schnittwinkel, lagebeziehungen,
vektoren-und-rechenoperationen, zufallsexperimente-und-pfadregeln,
ableitung-und-aenderungsrate, ebenen. Je Eintrag eine Änderungszeile
(Datum 2026-09-29) unter „Offene Punkte“.

| Eintrag | eingefügt | Zahl |
|---|---|---|
| kurvenuntersuchung | E2 Vorstufe „Stelle, Wert oder Punkt?“; E2 „Ändert sich die Monotonie, ändert sich die Krümmung?“; E4 „aus einer ausgefüllten Übersichtstabelle skizzieren (GK)“ | 3 |
| extremalprobleme | E2 „feste Nebenbedingung ohne Figur“; E3 „Randmaximum“ (Vorrat) | 2 |
| geraden | E1 Vorstufen „Wertetafel“ und „Gleichung am Quader lesen“; E3 Vorstufe „Lagen am Quader“; Merkkasten E3 Vier-Fall-Tafel | 3 (+Kastenform) |
| abstaende | E2 Vorstufe „Abstand des Ursprungs“; Kontrollzeile Lotfußpunkt | 1 (+1 Kontrolle) |
| flaecheninhalt-durch-integration | E5 Integralwert und Flächeninhalt nebeneinander | 1 |
| binomialverteilung | E2 ganze Verteilung für kleines n, Kontrolle Summe eins | 1 |
| ableitungsregeln | E2 innere und äußere Funktion hinschreiben (Vorstufe) | 1 |
| funktionsklassen-und-eigenschaften | E5 im Argument ausklammern (Vorstufe); E2 Koeffizient rückwärts | 2 |
| skalarprodukt-und-winkel | E1 aus Längen und Winkel ohne Koordinaten (Vorstufe) | 1 |
| stammfunktion-und-hauptsatz | E1 drei Stammfunktionen zeichnen | 1 |
| tangente-normale-schnittwinkel | E4 Vorstufe „Welcher Winkel?“ | 1 |
| lagebeziehungen | E1 Seite gegen den Ursprung; Kontrollzeile Schnittpunkt E3 | 1 (+1 Kontrolle) |
| vektoren-und-rechenoperationen | E2 derselbe Vektor auf zwei Kantenwegen | 1 |
| zufallsexperimente-und-pfadregeln | E3 Lückenterm | 1 |
| ableitung-und-aenderungsrate | E3 Tangente mit dem Lineal (Grafik) | 1 |
| ebenen | E2 Punkt der Ebene finden, Probe | 1 |

Summe: 22 Sprossen/Vorstufen, 2 Kontrollzeilen als Schluss bestehender
Sprossen, 1 Kastenform – wie die Prüfliste. Die Prüfliste zählt 3
Kontrollzeilen; die dritte ist nach dem Urteil die Kontrolle der
binomialverteilung („Summe eins“), die als Teil der neuen Sprosse
steht, nicht als Schlusszeile.

Abweichungen und Entscheidungen ohne Regel:
- Vorstufe vor dem Grundfall: Wo ein Fund zwischen Vorstufe und
  Grundfall steht (geraden E1 zweimal, abstaende E2, skalarprodukt E1,
  ableitungsregeln E2, funktionsklassen E5) oder vor der ersten
  Vorstufe (geraden E3), trägt er „(Vorstufe)“ – „Grundfall zuerst“
  (Prüfliste der Einträge) lässt vor dem Grundfall nur Vorstufen zu.
  Bei ableitungsregeln und funktionsklassen fehlte die Marke im
  Commit 2a296e5 und ist im Abschluss nachgetragen (ebenso die
  Änderungszeile). Folge für die Bank: Acht Ketten haben jetzt zwei
  bis drei Vorstufen (kurvenuntersuchung E2, geraden E1 und E3,
  abstaende E2, skalarprodukt E1, tangente E4, ableitungsregeln E2,
  funktionsklassen E5); bank.md kennt nur „sprosse 0 = Vorstufe“.
  Wie mehrere Vorstufen nummeriert werden (0, 1, … mit hoehe
  vorstufe; bank-pruef.py erlaubt den Start bei 0 und die Folge
  vorstufe vor grundfall), sollte der Chat vor dem ersten Bank-Auftrag
  festlegen.
- Ziffernfreiheit: P(X = 0) → „von k gleich null bis k gleich n“,
  „Summe ist 1“ → „eins“; Winkel „0° bis 180°“, „90°“ → in Worten;
  „1 − (…)^…“ → „eins minus (…) hoch (…)“; „|d|“ → „den Betrag der
  rechten Seite“. Formeln mit Buchstaben (b · (x + c/b), z = v(x),
  u(z), (x₀ | f(x₀))) bleiben.
- abstaende: Die Vorschlagsdatei nennt „Lotfußpunkt über die
  Lotgerade, Probe …“; in Einheit 2 heißt die Sprosse nur „die
  Lotgerade durch einen Punkt angeben“. Ergänzt: „…, ihr Schnitt mit
  der Ebene ist der Lotfußpunkt; Probe: der Lotfußpunkt erfüllt die
  Ebenengleichung“. Einheit 3 (Lotfußpunkt Punkt–Gerade) hat keine
  Ebenengleichung und bleibt unberührt.
- lagebeziehungen: „Schlusszeile des Grundfalls und der Sprossen mit
  Schnittpunkt“ – der Grundfall der Einheit 3 („liegt in der Ebene“)
  hat keinen Schnittpunkt; nur die Prüfungshöhe (parameterabhängiger
  Schnittpunkt) hat einen. Die Kontrollzeile steht nur dort. Die
  Schnittpunktrechnung selbst liegt in schnittmengen.md (dort steht
  schon „Kontrollwert nutzen“).
- geraden Merkkasten: Die Tafel steht als erste Zeile des Kastens
  Einheit 3, als Leerzeichen-Tafel (die Kästen sind eingerückter
  Text). Der Satz „Gemeinsamer Punkt und verschiedene Richtungen →
  schneidend …; gleiche Richtung und Stützpunkt außerhalb → echt
  parallel“ aus „Identisch?“ ist in die Tafel aufgegangen und
  gestrichen; sonst nichts am Kasten geändert.
- extremalprobleme Randmaximum: Klammer „(Vorrat: kein Abitur-GK-Beleg
  im Katalog)“, Grund aus dem Urteil (Offen 3).
- kurvenuntersuchung E4: die Übersichtstabelle steht vor „Graphen von f
  und f' aus berechneten Punkten“ (nach dem Grundfall), Marke „(GK)“.
- Keine Kollision mit einer seit 808fd7c geänderten Stelle; alle
  Ankerstellen wurden über den Sprossentext gefunden.

## Teil 3 – Prüfungskatalog (Commit 25dd6ea)

msa/msa-katalog-gym.csv, Zeile 2025-GYM-K5d: typ_neben „Mantellinie
Kegel bestimmen“ → „Pythagoras Hypotenuse“ (msa-typen.csv Z. 60).
Gegenprobe: 249 Zeilen vorher und nachher; git diff: genau eine
geänderte Zeile (1 Einfügung, 1 Löschung); Ersetzung byteweise im
Feld, Anführungszeichen und Trennzeichen unverändert. Der Posten
„2025-GYM-K5d Nebentyp-Etikett prüfen“ ist aus faellig.md § 2
gestrichen und in § 4 vermerkt.

## Teil 4 – Regeldateien der Aufgabenbank (aufgabenbank 64d2c06)

- bank.md, „Mengen je Kette“: neuer Absatz „drei fehler-Zeilen
  verschiedene Formen (Schülerrechnung mit Fehler; fehlerfreie
  Vorlage P2; Serie P1 oder Prüfzahl P3) – drei begruenden-Zeilen
  ebenso (Begründe, warum; Aussagenserie P4; Personenaussage P6)“.
- bank.md, „Regeln für den Inhalt“: P1–P8 je ein Punkt im Wortlaut der
  Vorschlagsdatei; die Form „vier Rechnungen, eine falsch“ steht
  einmal, als Mehrzahlform in P2 (Überschneidung 2); P5 zusätzlich im
  Feld loesung (dort wirkt es). Urteilsfragen: etwa gleich viele Ja/
  Nein, Urteil als erstes Wort, eine der drei begruenden ohne
  Rechnung. rationale-zahlen: Antwortgerüst nur in den ersten zwei
  Varianten von e2 „Zeichen zusammenfassen gemischt“ und e3 „plus mal
  minus“.
- bank.md, Feld loesung: Sachaufgabe mit Antwortsatz mit Einheit;
  Begründen nennt die Regel beim Namen; Urteil zuerst.
- bank.md: Päckchen-Punkt ohne den Satz „was in Sek II gleich bleibt,
  klärt der erste Sek-II-Bank-Auftrag“; neuer Punkt „Analytische
  Geometrie: derselbe Körper mit festen Eckpunkten, je Variante ein
  Körper“.
- bank/tangente-normale-schnittwinkel/stand.md, „Offene Punkte“: eine
  Zeile e4 Grundfall (fester Punkt, Winkel aus allen Lagen, 90° als
  „keine Steigung“).
- bau/sprachlauf/regeln.md: Regel 6 vier Satzformen (Prüfen einer
  fremden Rechnung, Aussagen beurteilen, Ergebnisse prüfen,
  Falschergebnis erklären); Regel 7 Alltagsquantoren; Regel 12
  Bedingungsform Sek II („Nebenbedingung:“, „Bedingung f''(x) = 0:“,
  „Nullstelle:“, Urteil in der Zeile der Einsetzung); neue Regel 13
  (Frage nennt genau, was gesucht ist; Maßstab schwacher GK-Schüler).
  Entscheidung ohne Regel: Regel 10 („geändert wird nur, was gegen
  Regel 1–7 verstößt“) nennt jetzt „1–7 und 13“, sonst liefe der
  Sprachlauf Sek II an Regel 13 vorbei.
- bau/layout-befunde.md: Nr. 56 Tafel-Merkkasten (Ergänzung zu 54),
  57 Aussagenserie, 58 Denkaufgabe je Fertigkeit, 59 Formelgestalt
  beim Faktorisieren als Zwischenzeile der Lösung.
- werkzeuge/ nicht berührt; kein Bankordner geändert außer der einen
  stand.md-Zeile. bank-pruef.py tangente-normale-schnittwinkel: 0
  Abweichungen, 4 Warnungen (wie vorher).

## Teil 5 – Abschluss

- urteil-einbindung-2026-09-28.md: Zeile „umgesetzt am 2026-09-29,
  Commits …; nicht umgesetzt: Teil D/E – Chat“ unter der Kopfzeile.
- faellig.md: Posten „Katalog terme: Fertigkeit ‚Term durch Zahl
  teilen‘ (K5)“ geprüft – terme.md hat nach diesem Auftrag keine
  solche Sprosse oder Fertigkeit; der Posten bleibt stehen. Neuer
  Posten in § 2 (Bank-Aufträge je geändertem Eintrag, Prüfstein
  lineare-gleichungen, Auslöser „Abrechnung gemessen“, bei Chat). Der
  Posten „README: neue Dateien in quellen/ eintragen“ ist erledigt
  und nach § 4 verschoben, ebenso 2025-GYM-K5d (Teil 3). Der ältere
  Posten „Bank auffüllen nach dem Katalog-Nachzug … Prüfstein zuerst
  (terme)“ steht noch in § 2 und widerspricht dem neuen Posten im
  Prüfstein (terme gegen lineare-gleichungen) – nicht angefasst, der
  Chat entscheidet, welcher gilt.
- README.md: urteil-einbindung-2026-09-28.md und
  bericht-katalog-nachzug.md unter „Wo fange ich an“ (Standdatei im
  Satz dort, sie liegt jetzt in archiv/); unter quellen/ die sieben
  fehlenden Dateien (register-fundliste, altlehrwerke-fundliste,
  -formen, -pflichtformen, -formen-sek2, blattarten-literatur,
  nachhilfe-situationen) und eine Gruppenzeile für die 173
  Textfassungen `quelle-fremd-*` (Bayern, HH/SH, NI/BW, NRW ZP10, IQB
  VERA-8), die bisher ebenfalls fehlten. Gegenprobe: jede Datei unter
  quellen/ steht jetzt mit Namen oder Muster in README.md.
- Auftrag und Standdatei nach archiv/ verschoben (git mv).

## Befunde für den Chat

1. Mehrere Vorstufen je Kette (Teil 2, erster Punkt): bank.md regelt
   sie nicht; vor den Bank-Aufträgen festlegen.
2. Bankzeilen, deren sprosse_text nicht mehr wortgleich im Katalog
   steht: binomische-formeln e3 (3 Zeilen „kein Binom erkennen und
   begründen“) und brueche-dezimalzahlen e5 („Nullen anhängen“ ist
   jetzt Sprosse statt Vorstufe; die Bankzeilen tragen hoehe vorstufe,
   sprosse 0). Das gehört in die Bank-Aufträge dieser Einträge.
   bank-pruef.py --katalog meldet für diese Einträge schon vorher
   über hundert Abweichungen (Zeilennummern im Feld quelle), die Zahl
   hat sich durch den Nachzug nicht verändert – das Feld quelle
   veraltet mit jeder Katalogänderung.
3. faellig.md § 2: zwei Posten zur Bank nach dem Katalog-Nachzug mit
   verschiedenem Prüfstein (terme, lineare-gleichungen).

## Einträge, die einen Bank-Auftrag brauchen (neue Sprosse oder Form)

Sek I (8): lineare-gleichungen, binomische-formeln (Umbenennung,
Vorstufenfrage, Formelgestalt in der Lösung), brueche-dezimalzahlen,
prozentrechnung, terme, rationale-zahlen (dazu Antwortgerüst e2/e3
und Teilprodukt e3), bruchrechnung, pythagoras.

Sek II (16): kurvenuntersuchung, extremalprobleme, geraden, abstaende,
flaecheninhalt-durch-integration, binomialverteilung,
ableitungsregeln, funktionsklassen-und-eigenschaften,
skalarprodukt-und-winkel, stammfunktion-und-hauptsatz,
tangente-normale-schnittwinkel (dazu e4 Grundfall, stand.md),
lagebeziehungen, vektoren-und-rechenoperationen,
zufallsexperimente-und-pfadregeln, ableitung-und-aenderungsrate
(Grafik), ebenen.

## Pflichtformen P1–P8 – eigener Posten, alle 72 Einträge der Bank

ableitung-und-aenderungsrate, ableitungsregeln, abstaende,
bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung,
binomische-formeln, bruchrechnung, brueche-dezimalzahlen, daten,
ebenen, einheiten, extremalprobleme, flaechen,
flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum,
funktionsklassen-und-eigenschaften, funktionsscharen-und-ortskurven,
geraden, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen,
hypergeometrische-verteilung, hypothesentests, integrationsregeln,
kenngroessen-von-verteilungen, koerper, kombinatorik,
konfidenzintervalle, kreis, kurvenuntersuchung, lagebeziehungen,
lineare-funktionen, lineare-gleichungen, lineare-gleichungssysteme,
linearkombination-und-lineare-abhaengigkeit,
matrizen-und-uebergangsprozesse, normalverteilung-und-sigma-regeln,
orthogonalitaet, potenz-exponentialfunktionen, potenzen-wurzeln,
prozentrechnung, punkte-und-strecken-im-koordinatensystem,
pyramide-kegel-kugel, pythagoras, quadratische-funktionen,
quadratische-gleichungen, rationale-zahlen, reelle-zahlen,
rekonstruktion-von-bestaenden, rekonstruktion-von-funktionsgleichungen,
rotationsvolumen, scharen-von-geraden-und-ebenen, schnittmengen,
skalarprodukt-und-winkel, spiegelung, stammfunktion-und-hauptsatz,
strahlensaetze, symmetrie-abbildungen, tangente-normale-schnittwinkel,
terme, trigonometrie, trigonometrische-funktionen, umkehrfunktion,
unabhaengigkeit, uneigentliche-integrale, vektoren-und-rechenoperationen,
vierfeldertafel, wahrscheinlichkeit, winkel-dreiecke, zinsrechnung,
zufallsexperimente-und-pfadregeln, zufallsgroessen-und-verteilungen,
zuordnungen. (72 Ordner unter bank/; der 73. Katalogeintrag
ableitungsgraph-und-funktionsgraph hat keinen Bankordner.)

Push origin drücken (mathe-nachhilfe und aufgabenbank) – in diesem
Lauf vom Unteragenten selbst gepusht.
