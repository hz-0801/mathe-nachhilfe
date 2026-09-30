# Vorschläge 30.09.2026 – Katalogbefunde der Bank-Nachzüge vom 29.09.

Stand 30.09.2026: Katalog auf Commit 6ae89f9 (mathe-nachhilfe),
Bank auf 11d6a36 (aufgabenbank). Zeilennummern „Z.“ der Einträge
beziehen sich auf diesen Stand; Zeilennummern der stand.md-Dateien
auf `bank/<eintrag>/stand.md` in 11d6a36.

Zweck: Vorschlag für das Urteil im Chat. Stoff sind die Zeilen mit
„Katalog:“ oder „Katalog,“ unter „Befunde“ in den stand.md-Dateien
der 24 Einträge, die am 29.09. auf den Katalog nachgezogen wurden
(Liste aus bericht-katalog-nachzug.md: lineare-gleichungen,
binomische-formeln, brueche-dezimalzahlen, prozentrechnung, terme,
rationale-zahlen, bruchrechnung, pythagoras; kurvenuntersuchung,
extremalprobleme, geraden, abstaende, flaecheninhalt-durch-
integration, binomialverteilung, ableitungsregeln, funktionsklassen-
und-eigenschaften, skalarprodukt-und-winkel, stammfunktion-und-
hauptsatz, tangente-normale-schnittwinkel, lagebeziehungen,
vektoren-und-rechenoperationen, zufallsexperimente-und-pfadregeln,
ableitung-und-aenderungsrate, ebenen). Dazu die Katalogzeilen von
flaecheninhalt-und-volumen-im-raum, nur als Prüfstein der Regel am
Ende (nicht unter den 24). **Nichts ist in die Einträge
übernommen**; kein Eintrag, keine Belegdatei, nichts in
aufgabenbank ist geändert.

Zählung: 66 Katalogzeilen in den 24 stand.md-Dateien, nach Art:
(a) Verweis oder Zeile falsch oder widersprüchlich 13 ·
(b) Kennungen oder Originale ohne Mappeneintrag oder umgekehrt 11 ·
(c) Typzeile unvollständig 4 · (d) Erkennungsschritt wiederholt
eine Vorstufe 21 · (e) Sonstiges 6 · (f) Bank- oder Skriptfrage 11.
Vorgeschlagene Katalogzeilen: 25 (in 24 Vorschlägen), davon 7 ohne
Beleg. Dazu ein Skriptvorschlag zu (b) und die Regelfassung für
bank.md am Ende.

Lesart: Eine „vorgeschlagene Zeile“ ist eine Zeile im Format des
Eintrags (Typzeile, Sprossenkette, Erkennungsschritt,
Fertigkeitszeile, Fehlerzeile), die eine bestehende ersetzt oder
neu dazukommt; sie steht im Codeblock als ganze Zeile, darunter
der Einfügeort und „Beleg:“. Beleg ist eine Prüfungs-id (msa/,
fhr/, abitur/), eine Lehrwerksstelle aus katalog/_klassen-belege.md
oder eine Rahmenlehrplanstelle; wo nur die Form oder die
Rechenprobe trägt, steht „kein Beleg gefunden“ und der Vorschlag
bleibt stehen. Sprossen sind außerhalb der Belegklammern
ziffernfrei geschrieben; Ziffern in unveränderten Teilen bleiben.
Befunde der Art (d) haben keinen eigenen Abschnitt: sie sind die
Prüfsteine des Regelabschnitts am Ende; wo einer eine Katalogzeile
ändert (Bereich eines Erkennungsschritts), steht der Vorschlag beim
Eintrag. Befunde der Art (f) sind nur genannt (Abschnitt F).

Probe: Alle 25 Zeilen wurden in eine Kopie des Katalogs auf 6ae89f9
eingesetzt (Hilfsskript `_probe/` im Klon, nichts im Repo);
`_pruef_katalog.py` meldet für die 16 berührten Einträge dieselben
Treffer wie vorher (vier Treffer, alle Bestand: lineare-gleichungen
„12 : (−3)“ und „3 · 4 − 5“, terme „3 − 7“ und „3 · (−4)“ in Blatt-0-
Fertigkeiten); `_pruef_struktur.py` gibt dieselbe Ausgabe
(Strukturprüfung ok, Kennzahl 5 = 28, Kennzahl 8 = 3 Verweise,
Kennzahl 9 = 24). Einzige Abweichung im ersten Lauf: ein Verweis
„unterrichtsblatt.md 2.2“ in Vorschlag 7.2 zählte als Verweis auf
eine fehlende Datei (Kennzahl 8: 4 statt 3); der Vorschlag nennt
jetzt „Unterrichtsblatt-Prompt, Abschnitt 2.2“ – danach gleich.
Die übrigen Unterschiede sind nur die Reihenfolge gleicher Zahlen
in der Mengenausgabe („0,05“/„0,050“).

## 1 lineare-gleichungen.md

**Befund** (stand.md Z. 84–85, Art a): „Katalog: Die Vorstufe der
Kette Umformen heißt „Blatt 0", steht aber als Vorstufe der
Einheit; hier in e2 geführt.“ – Stand heute: trifft zu.

**Befund** (stand.md Z. 82–83, Art a): „Katalog: Kette Umformen
führt keine Klammer, alle drei e2-Originale haben eine (Klammer als
Block gelöst).“ – Stand heute: trifft zu.

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 78: „… einschrittige Gleichung mit leerem Strich (Vorstufe,
  Blatt 0) → …“ gegen Z. 31: „Erkennungsschritte (Vorstufe der
  Einheit, vor der sie stehen, nicht auf Blatt 0 …)“ und Z. 20:
  „Umformung anschreiben (Vorstufe, s. Voraussetzungen)“. Die
  Vorstufe ist Sprosse 0 der Kette (bank.md), nicht Blatt 0.
- Z. 78 endet: „… → Umkehrung: Gleichung zu gegebener Lösung →
  Prüfungshöhe: zweischrittig mit negativer Lösung und Probe.“ –
  keine Klammer. Z. 83: „„Lineare Gleichung lösen" dreimal als
  Basisaufgabe, jedes Mal mit Klammer – 2020-OS-B1e (2(x − 4) = 6),
  2023-OS-B1e (3 · (x − 8) + 2 = 2) und 2024-OS-B1d
  (2 · (x − 6,5) = 0 …)“; Z. 84: „Einheit 2 – eine zweischrittige
  Gleichung mit Klammer in Prüfungsform lösen“. Das Auflösen der
  Klammer ist Einheit 3 (Z. 21, Z. 29 „Klammern auflösen – nur
  Einheit 3“); die drei Originale gehen ohne Auflösen, wenn die
  Klammer als Block behandelt wird (erst teilen, dann die Klammer
  weglassen) – so hat die Bank sie gelöst.

**Vorschlag 1.1 – Kette Umformen ohne „Blatt 0“ (ersetzt Z. 78)**

```
- Umformen (Einheit 2): Umformung nur anschreiben: „Schreibe hinter den Strich, was x allein stellt“, einschrittige Gleichung mit leerem Strich (Vorstufe) → einschrittig plus/minus (4×) → einschrittig mal/geteilt → negative Lösung → zweischrittig erst Strich dann Punkt (4×, mit Probe [INKL]) → x steht hinter dem Minus (zwanzig minus x gleich dreizehn) → negative Vorzahl → Vorzahl als Bruch → Umkehrung: Gleichung zu gegebener Lösung → Prüfungshöhe: zweischrittig mit negativer Lösung und Probe.
```

Nur „(Vorstufe, Blatt 0)“ → „(Vorstufe)“; sonst wortgleich.

Beleg: kein Beleg gefunden (Formfrage: Z. 31 des Eintrags,
bank.md „sprosse 0 = Vorstufe“, katalog/_vorlage.md führt Blatt 0
nur für Fertigkeiten, Erkennungsschritte, Grundvorstellung).

**Vorschlag 1.2 – Klammer als Block in der Kette Umformen (ersetzt
Z. 78; mit 1.1 zusammen in einer Zeile)**

```
- Umformen (Einheit 2): Umformung nur anschreiben: „Schreibe hinter den Strich, was x allein stellt“, einschrittige Gleichung mit leerem Strich (Vorstufe) → einschrittig plus/minus (4×) → einschrittig mal/geteilt → negative Lösung → zweischrittig erst Strich dann Punkt (4×, mit Probe [INKL]) → x steht hinter dem Minus (zwanzig minus x gleich dreizehn) → negative Vorzahl → Vorzahl als Bruch → Klammer als Block: Zahl mal Klammer gleich Zahl, erst durch die Zahl teilen, dann die Klammer weglassen, nicht auflösen (P10-Form 2020-OS-B1e, 2024-OS-B1d) → Umkehrung: Gleichung zu gegebener Lösung → Prüfungshöhe: zweischrittig mit negativer Lösung und Probe; in P10-Form mit der Klammer als Block und einer Zahl außerhalb der Klammer (2023-OS-B1e, Niveau I).
```

Neu ist eine Sprosse vor der Umkehrung und der Nachsatz der
Prüfungshöhe; die Typzeile Z. 20 braucht dann den Typ „Klammer als
Block (Zahl mal Klammer gleich Zahl)“ vor „Umformung anschreiben“ –
hier nicht als Zeile ausgeführt, weil die Typklammern von
marken-bau.py kommen.

Beleg: [Prüfung] msa 2020-OS-B1e (2(x − 4) = 6), 2023-OS-B1e
(3 · (x − 8) + 2 = 2: erst die Zahl außerhalb, dann durch drei),
2024-OS-B1d (2 · (x − 6,5) = 0), alle Basis, Niveau I (Z. 83–85);
[RLP] E „Lösen linearer Gleichungen … durch
Äquivalenzumformungen“, F „Lösen von linearen Gleichungen (auch
mit Klammern)“ (Z. 5) – die Blockform bleibt auf E, das Auflösen
ist F und Einheit 3.

## 2 binomische-formeln.md

**Befund** (stand.md Z. 81–85, Art d): „Katalog: Die
Erkennungsschritte „Was ist a, was ist b?“ und „Welche Formel?“
(Zeilen 34, 35) wiederholen den Handgriff der e2-Vorstufe „Formel
erkennen und a, b einkreisen“ und entfallen; …“ – Stand heute:
trifft zu (Prüfstein 1 am Ende). Katalogfolge: Z. 34 nennt „Vor
Einheit 2 und 3“, der Schritt fragt aber nach Plus- und
Minusklammern eines Produkts – in Einheit 3 (Faktorisieren) liegt
ein dreigliedriger Term vor, dort passt die Frage nicht, und die
Vorstufe der Einheit 3 (Z. 85: Quadrate erkennen, Mittelglied
unterstreichen, kein Binom streichen) ist ein anderer Handgriff.

**Befund** (stand.md Z. 86–88, Art a): „Katalog: Die Prüfungshöhe
e2 verweist auf quadratische-gleichungen.md Einheit 2, die
e3-Sprosse „Anwendung“ auf Einheit 3 – einer der Verweise ist
falsch.“ – Stand heute: trifft nicht zu. quadratische-gleichungen.md
hat Einheit 2 „Normalform und p-q-Formel“ und Einheit 3 „Satz vom
Nullprodukt – Produktform (x − a)·(x − b) = 0“. Z. 84 verweist für
das Gleichsetzen mit einer Geraden (2022-OS-K3c, danach p-q-Formel)
richtig auf Einheit 2, Z. 85 für „Produktform gleich null“ richtig
auf Einheit 3. Kein Vorschlag.

**Befund** (stand.md Z. 89–90, Art e): „Katalog: Vorrat mitten in
der Kette (e2 s3, s6 vor den P10-tragenden s7–s9); ein Blatt für den
Mindeststoff überspringt.“ – Stand heute: trifft zu.

**Befund** (stand.md Z. 93–94, Art c): „Katalog: Kein Typ trägt
Sachanwendung oder Darstellungswechsel; anwendung und darstellung
fehlen im ganzen Eintrag.“ – Stand heute: halb. Die Anwendung ist
da, nur nicht so benannt: Z. 20 „Klammer mit Formel auflösen und
mit dem Rest zusammenfassen (Scheitelpunktform → Normalform)“,
Z. 21 „Anwendung: Produktform gleich null“ – für anwendung kein
Vorschlag. Ein Darstellungswechsel fehlt in allen drei Typzeilen,
obwohl die Grundvorstellung (Z. 81) und beide Begründen-Typen
(Z. 19, 20 „Flächenbild“) ihn brauchen.

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 34: „„Welche Formel?“ – zu Termen ankreuzen: Plus in der
  Klammer und Quadrat → erste, Minus und Quadrat → zweite,
  Plus-Klammer mal Minus-Klammer → dritte, sonst keine; nichts
  rechnen. Vor Einheit 2 und 3.“
- Z. 84: „… → zweite Formel, Minus im Mittelglied → dritte Formel,
  Mittelglied fällt weg (Vorrat: kein P10-Original) → gemischt:
  Formel wählen, auch „keine“ → Vorzahl vor x (Vorzahl mit
  quadrieren) → zwei Variablen (Vorrat) → Vorfaktor vor der Klammer
  … → Klammer auflösen und mit dem Rest zusammenfassen →
  Prüfungshöhe: …“ gegen Z. 91: „dritte Formel, zwei Variablen und
  Kopfrechnen sind Vorrat und in der Kette so markiert“ und Z. 80
  (Mindeststoff der Prüfungsvorbereitung: erste und zweite Formel,
  Minus vor der Klammer, Klammer auflösen).
- Z. 20 (Typen Einheit 2): kein Typ „Darstellung“.

**Vorschlag 2.1 – Bereich des Erkennungsschritts (ersetzt Z. 34)**

```
- „Welche Formel?“ – zu Termen ankreuzen: Plus in der Klammer und Quadrat → erste, Minus und Quadrat → zweite, Plus-Klammer mal Minus-Klammer → dritte, sonst keine; nichts rechnen. Vor Einheit 2. [Serlo 1499 Entscheidungsbaum]
```

Beleg: der Schritt selbst (Vorlage sind Produkte, nicht
dreigliedrige Terme); [Lehrwerk] _klassen-belege.md Z. 3518 „LS
Kl. 8: „Kapitel II Terme mit mehreren Variablen“ › „4 Binomische
Formeln““ – das Faktorisieren steht dort in derselben Lerneinheit
rückwärts (Z. 15 des Eintrags), mit eigenem Entscheidungsbaum
(Serlo 1499, Z. 103).

**Vorschlag 2.2 – Typ Darstellung Einheit 2 (ersetzt Z. 20)**

```
Einheit 2: gleiche Klammer zweimal erkennen ((a + b)² ist (a + b)·(a + b)) · erste binomische Formel mit x und Zahl [OS 8] · zweite Formel (Minus im Mittelglied) [OS 8] · dritte Formel (Mittelglied fällt weg) [OS 8] · Formel zuordnen (welche der drei, oder keine) · mit Vorzahl vor x (a ist die ganze Vorzahl mit x) · mit zwei Variablen · Vorfaktor vor der Klammer · Minus vor der Klammer · Klammer mit Formel auflösen und mit dem Rest zusammenfassen (Scheitelpunktform → Normalform) · Nachweis „Normalform stimmt“ (P10-Form) · Kopfrechnen mit der Formel (Vorrat) · Darstellung: Term ↔ Flächenbild, das Quadrat mit der Seite a plus b in zwei Quadrate und zwei Rechtecke zerlegen und die vier Teilflächen als Glieder der ersten Formel lesen · Fehler finden (Mittelglied fehlt; Vorzeichen des Mittelglieds; Vorzahl nicht quadriert; Minus vor der Klammer nur aufs erste Glied) · Begründen (warum (a + b)² nicht a² + b² ist – Zahlenprobe, Flächenbild).
```

Neu ist der Typ „Darstellung: …“ vor „Fehler finden“; die
Typklammer bleibt Sache von marken-bau.py.

Beleg: [Lehrwerk] _klassen-belege.md Z. 3516 „Schnittpunkt Kl. 8,
S. 15: „EXTRA: Binomische Formeln geometrisch beweisen““, Z. 3509
„Sekundo Kl. 8, S. 182: „LVL: Herleitung der Binomischen
Formeln““; [RLP] F/G in Z. 81 des Eintrags (Grundvorstellung mit
Flächenbild); [Prüfung] Fehlerquelle „Mittelglied fehlt“ 2017-OS-K5d,
2022-OS-K3c (Z. 33) – das Flächenbild zeigt das Mittelglied.

**Vorschlag 2.3 – Vorrat ans Ende der Kette (ersetzt Z. 84)**

```
- Binomische Formeln (Einheit 2): Formel erkennen und a, b einkreisen (Vorstufe) → erste Formel mit x und Zahl (4×) → zweite Formel, Minus im Mittelglied → gemischt: Formel wählen, auch „keine“ → Vorzahl vor x (Vorzahl mit quadrieren) → Vorfaktor vor der Klammer (erst Formel, dann Vorfaktor auf alle drei Glieder) → Minus vor der Klammer (alle drei Vorzeichen drehen) → Klammer auflösen und mit dem Rest zusammenfassen → dritte Formel, Mittelglied fällt weg (Vorrat: kein P10-Original) → zwei Variablen (Vorrat) → Prüfungshöhe: Scheitelpunktform einer verschobenen Normalparabel als vorgegebene Normalform nachweisen (P10-Form 2017-OS-K5d, Stern); Scheitelpunktform vor dem Gleichsetzen mit einer Geraden ausmultiplizieren (2022-OS-K3c, Stern; Verfahren quadratische-gleichungen.md Einheit 2).
```

Die beiden Vorrat-Sprossen wandern hinter „Klammer auflösen und
mit dem Rest zusammenfassen“; sonst wortgleich. Abwägung: „gemischt:
Formel wählen, auch „keine““ steht dann vor der dritten Formel; die
Auswahl läuft dort zwischen erster, zweiter und keiner Formel – die
dritte kommt als Vorrat dazu. Die Alternative (Vorrat an Ort und
Stelle, Blatt überspringt nach Marke) bräuchte eine Regel im
Zusammenbau, die es nicht gibt.

Beleg: [Prüfung] msa 2017-OS-K5d, 2022-OS-K3c (erste und zweite
Formel; Z. 88, 91); Z. 91 „dritte Formel, zwei Variablen und
Kopfrechnen sind Vorrat“; [Lehrwerk] _klassen-belege.md Z. 3511–3513
(Mathematik 2023 Kl. 8, S. 18–20: erste, zweite, dritte Formel in
dieser Folge – die dritte zuletzt).

## 3 brueche-dezimalzahlen.md

**Befund** (stand.md Z. 104–105, Art a): „Katalog Z. 106: Drei
Originale der e1-Prüfungshöhe verlangen Prozent, das der Eintrag
erst für e5 voraussetzt (Z. 36).“ – Stand heute: trifft zu.

**Befund** (stand.md Z. 106–107, Art a): „Katalog Z. 110, 111:
2015-OS-B1c und 2014-OS-B1h verlangen Wurzeln und negative Zahlen
(Vorrat, Z. 103).“ – Stand heute: trifft zu.

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 36: „Prozent als Hundertstel (45 % = 0,45) – Einheit 5. Thema
  Prozentrechnung (prozentrechnung.md), Einheit 1. [RLP E]“ gegen
  Z. 106 (Prüfungshöhe Einheit 1): „… der Anteil einer
  Kästchenfigur als Bruch und als Prozentsatz (2014-OS-B1i), das
  Markieren eines Prozentanteils in einer Kästchenfigur
  (2022-OS-B1a, 2023-OS-B1d) …“.
- Z. 103: „Vorrat: … Vergleichen … mit Wurzeln (G), negative Zahlen
  (E, rationale-zahlen.md) …“ und Z. 27: „mit negativen Zahlen
  (Vorrat, rationale-zahlen.md Einheit 1) · mit Wurzeln über
  Näherungswert (Vorrat, potenzen-wurzeln.md)“ gegen Z. 111
  (Prüfungshöhe Einheit 5): „daneben die aufsteigende Reihe aus
  negativem Bruch, negativer Dezimalzahl, Dezimalzahl und Wurzel
  (2014-OS-B1h), die wahre von drei Ungleichungen mit Bruch,
  Dezimalzahl und Wurzel ankreuzen (2015-OS-B1c)“ – ohne
  Vorrat-Marke. Z. 110 (Einheit 4) nennt 2015-OS-B1c als
  Prüfungshöhe fürs Umwandeln; das Umwandeln dort (3/2 = 1,5) ist
  ohne Wurzel machbar, die Zeile bleibt.

**Vorschlag 3.1 – Fertigkeit Prozent auch für Einheit 1 (ersetzt
Z. 36)**

```
- Prozent als Hundertstel (45 % = 0,45) – Einheit 1 in der P10-Form (Anteil einer Kästchenfigur auch als Prozentsatz, Prozentanteil einer Figur markieren) und Einheit 5. Thema Prozentrechnung (prozentrechnung.md), Einheit 1. [RLP E; P10 2014-OS-B1i, 2022-OS-B1a, 2023-OS-B1d]
```

Beleg: [Prüfung] msa 2014-OS-B1i (9 von 15 = 3/5 = 60 %),
2022-OS-B1a (20 % von 15 Kästchen markieren), 2023-OS-B1d (25 %
von 24 Kästchen), alle Niveau I (Z. 114); [RLP] E (Z. 36).

**Vorschlag 3.2 – Vorrat-Marke in der Prüfungshöhe Einheit 5
(ersetzt Z. 111)**

```
- Vergleichen und Ordnen (Einheit 5): „Wo entscheidet es sich?“ – zu zwei Dezimalzahlen mit gleich vielen Stellen nur die Stelle nennen, an der sie sich zuerst unterscheiden; kein Zeichen setzen (Vorstufe) → zwei Dezimalzahlen mit gleich vielen Stellen (4×) → Nullen anhängen: Dezimalzahlen auf gleich viele Stellen bringen, ohne zu vergleichen [MSK D2B; LS-AA Kl. 6 II 2] → verschieden viele Stellen → vier Zahlen ordnen → runden → Mitte zweier Zahlen → Bruch gegen Dezimalzahl → Prozent gegen Dezimalzahl → Potenz einer Dezimalzahl → Prüfungshöhe: aus vier Zahlen in vier verschiedenen Darstellungen – Dezimalzahl, Dezimalzahl, Quadrat einer Dezimalzahl und Prozentangabe – die kleinste bestimmen (P10-Form 2023-OS-B1f, Niveau I); daneben, als Vorrat (negative Zahlen rationale-zahlen.md Einheit 1, Wurzel über den Näherungswert potenzen-wurzeln.md Einheit 3), die aufsteigende Reihe aus negativem Bruch, negativer Dezimalzahl, Dezimalzahl und Wurzel (2014-OS-B1h) und die wahre von drei Ungleichungen mit Bruch, Dezimalzahl und Wurzel ankreuzen (2015-OS-B1c); ohne Vorrat das Vergleichszeichen zwischen Prozentangabe und Dezimalzahl setzen (2018-OS-B1d) und die Mitte zweier negativer Dezimalzahlen (2020-OS-B1f), alle Niveau I; die drei Originale mit Potenzen und Zehnerpotenzen (2017-OS-B1e, 2019-OS-B1d, 2022-OS-B1j) führt potenzen-wurzeln.md.
```

Nur die Prüfungshöhe ist umgestellt (Vorrat-Klammer, Verweise);
Sprossen wortgleich. 2020-OS-B1f (Mitte von −0,6 und −0,5) bleibt
ohne Vorrat-Marke: der Eintrag führt es als Hauptoriginal des Typs
„Mitte zweier Zahlen bestimmen“ (Z. 114, 117) und rationale-
zahlen.md Z. 91 nennt es als angrenzend – ob die Mitte negativer
Zahlen Vorrat ist, entscheidet der Chat.

Beleg: [Prüfung] msa 2014-OS-B1h (−1/2; 1,4; −0,512; √2),
2015-OS-B1c (√2 > 3/2), Z. 114; [RLP] Stufen aus Z. 103 („mit
Wurzeln (G), negative Zahlen (E, rationale-zahlen.md)“);
potenzen-wurzeln.md Einheit 3 „Wurzel abschätzen“ (Z. 115 des
Eintrags).

## 4 prozentrechnung.md

**Befund** (stand.md Z. 85–86, Art c): „Katalog: e5 hat keinen Typ
Darstellung; pflicht darstellung fehlt dort (9 Pflichtzeilen).“ –
Stand heute: trifft zu.

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 27 (Typen Einheit 5): „„um“ und „auf“ unterscheiden · neuer
  Wert über Prozentwert (dazu, weg) · … · Steigung in Prozent deuten
  und berechnen [OS 10] · Fehler finden (…) · Begründen (…)“ – kein
  Darstellungstyp, während die Kette Z. 102 jede Sprosse am
  Streifen führt: „Faktor 1,2 und 0,8, dargestellt am Streifen, der
  über hundert Prozent hinaus verlängert oder unter hundert Prozent
  verkürzt wird → Veränderung in Prozent aus zwei Werten, beide als
  Streifen untereinander, der alte ist hundert Prozent → …“.

**Vorschlag 4.1 – Typ Darstellung Einheit 5 (ersetzt Z. 27)**

```
Einheit 5: „um“ und „auf“ unterscheiden · neuer Wert über Prozentwert (dazu, weg) · neuer Wert über Faktor (1,2; 0,8) [OS 9] · Veränderung in Prozent aus zwei Werten (Differenz : Ausgangswert) · alter Wert aus neuem Wert und Prozentsatz · Brutto/Netto (19 %, 7 %) [OS 7] · Prozentpunkte gegen Prozent [GYM 7] · Steigung in Prozent deuten und berechnen [OS 10] · Veränderung am Prozentstreifen darstellen und ablesen (der alte Wert ist hundert Prozent, der Streifen wird über hundert Prozent verlängert oder verkürzt) · Fehler finden (Differenz auf den neuen Wert bezogen) · Begründen (welcher Wert ist 100 %).
```

Beleg: [RLP] E „Prozentstreifen, auch Dreisatz“ (Z. 95 des
Eintrags, Mindeststoff); [Lehrwerk] _klassen-belege.md Z. 632
„Schnittpunkt Kl. 7, S. 184: „EXTRA: Prozentband““, Z. 630
„mathe.delta Kl. 7, S. 70: „2.5 Prozente darstellen““ (beide
Typzeilen der Einheit 1 – für Einheit 5 keine eigene
Lehrwerksstelle gefunden); [MSK P B 5] (Z. 41); Kette Z. 102.

## 5 terme.md

**Befund** (stand.md Z. 80–81, Art c): „Katalog: e1 trägt weiter
keinen Typ Begründen, e3 keine Anwendung; die Pflichtmengen fehlen
dort nach den Typen.“ – Stand heute: trifft zu.

**Befund** (stand.md Z. 82–83, Art e): „Katalog, Erkennungsschritte:
keiner wiederholt eine Vorstufe derselben Einheit; e4 hat keinen
Erkennungsschritt.“ – Stand heute: trifft zu; Einheit 4 hat zwei
Vorstufen mit vorgegebenem Faktor (Z. 76), aber keinen Schritt, der
den Faktor finden lässt.

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 21: „Einheit 1: Termwert berechnen (auch negative Einsetzung)
  · Term zu Sachtext angeben (Doppeltes, vermindert um) · Term zu
  Figur angeben (Umfang, Fläche aus Rechtecken) [OS 6] · Situation
  zu Term angeben.“ – ohne „Fehler finden“ und „Begründen“, gegen
  _vorlage.md („Fehler finden · Begründen am Ende“) und die drei
  anderen Typzeilen des Eintrags.
- Z. 23: „Einheit 3: Plusklammer weglassen · … · Klammer auflösen
  und zusammenfassen · Fehler finden · Begründen (Gleichwertigkeit).“
  – kein Sachterm.
- Z. 32–36 (Erkennungsschritte): vor Einheit 2 drei, vor Einheit 3
  einer, vor Einheit 4 keiner.

**Vorschlag 5.1 – Fehler finden und Begründen Einheit 1 (ersetzt
Z. 21)**

```
Einheit 1: Termwert berechnen (auch negative Einsetzung) · Term zu Sachtext angeben (Doppeltes, vermindert um) · Term zu Figur angeben (Umfang, Fläche aus Rechtecken) [OS 6] · Situation zu Term angeben · Fehler finden (Reihenfolge bei „vermindert um“ vertauscht: vier minus x statt x minus vier; Klammer beim Doppelten einer Summe vergessen) · Begründen (warum das Doppelte von x plus zwei eine Klammer braucht – Zahlenprobe auf zwei Wegen).
```

Beleg: [Prüfung] msa 2023-OS-B1h (Term zu drei Anweisungen
ankreuzen, die Klammer entscheidet; Z. 75), 2016-OS-B1b,
2021-OS-B1e (Distraktoren „um 4 vermindert“ als 4 − x, „das
Dreifache von x + 2“ ohne Klammer – lineare-gleichungen.md Z. 70,
83); [RLP] D/E Terme aufstellen (Z. 9 des Eintrags).

**Vorschlag 5.2 – Sachterm mit Klammer Einheit 3 (ersetzt Z. 23)**

```
Einheit 3: Plusklammer weglassen · Minusklammer (alle Vorzeichen drehen) [GYM 8] · Zahl mal Klammer [OS 7–8, GYM 8] · negative Zahl mal Klammer · Klammer auflösen und zusammenfassen · Sachterm mit Klammer auflösen (Preis mal (Anzahl plus x); Umfang eines Rechtecks als zwei mal (a plus b)) · Fehler finden · Begründen (Gleichwertigkeit).
```

Beleg: [Prüfung] msa 2020-OS-K2e (12 · (520 + x) = 7920, Stern,
Niveau II – die Klammer trägt die Aufgabe; lineare-gleichungen.md
Z. 83–84); [LISUM-PH Jg. 8] geometrische Kontexte, „aus Umfang und
Flächeninhalt auf Seitenlängen schließen“ (lineare-gleichungen.md
Z. 6); [RLP] F „Lösen von linearen Gleichungen (auch mit
Klammern)“.

**Vorschlag 5.3 – Erkennungsschritt vor Einheit 4 (neue Zeile nach
Z. 36)**

```
- „Was steckt in jedem Glied?“ – zu Termen den Faktor einkreisen, der in jedem Glied steckt (Zahl, Variable oder beides); nichts ausklammern. Vor Einheit 4.
```

Nach der Regelfassung am Ende ist das kein Doppel der Vorstufen
Z. 76 („Zerlegen mit vorgegebenem Faktor“, „Faktor vorgegeben, nur
die Klammer füllen“): dort ist der Faktor gegeben, hier wird er
gesucht – eine andere Entscheidung.

Beleg: [Lehrwerk] _klassen-belege.md Z. 564 „Fundamente Kl. 7,
S. 104: „3.9 Ausmultiplizieren und Ausklammern““, Z. 401
„Fundamente Kl. 6, S. 129: „4.9 Ausmultiplizieren und
Ausklammern““; [LS-AA Kl. 7 IV 3] (binomische-formeln.md Z. 27);
Typische Fehler binomische-formeln.md Z. 76 „Gemeinsamer Faktor
übersehen oder nur aus einem Glied gezogen“.

## 6 rationale-zahlen.md

**Befund** (stand.md Z. 85–87, Art a): „Katalog Z. 85: Die Sprosse
„nur das Vorzeichen“ steht vor „negative Zahl addieren mit
Klammer“, verlangt aber schon das Betragsdenken der Typ-Zeile
„Beträge“ (k4, Typ ohne Kette).“ – Stand heute: trifft zu.

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 85: „… → positive Zahl dazu oder weg, Start negativ (4×) → nur
  das Vorzeichen: ist die Summe größer oder kleiner als null?
  ankreuzen und mit den Beträgen begründen, nicht ausrechnen →
  negative Zahl addieren mit Klammer → …“ gegen Z. 22: „Beträge:
  gleiche Vorzeichen addieren, verschiedene subtrahieren“ – ein Typ
  ohne Sprosse in der Kette; die Betragsregel kommt im Lehrgang
  nach dem Zahlengeradenmodell (Z. 82 Grundvorstellung: Änderung
  als Pfeil).

**Vorschlag 6.1 – Begründung am Pfeilbild statt mit Beträgen
(ersetzt Z. 85)**

```
- Addieren/Subtrahieren (Einheit 2): Pfeil an der Zahlengeraden – nur den Pfeil vom Startwert aus zeichnen („Zeichne den Pfeil von minus eins um sieben nach rechts“); nicht rechnen [RLP E „Änderung eines Zustandes“] (Vorstufe) → positive Zahl dazu oder weg, Start negativ (4×) → nur das Vorzeichen: ist die Summe größer oder kleiner als null? ankreuzen und am Pfeilbild begründen (reicht der Pfeil über die Null hinaus?), nicht ausrechnen → negative Zahl addieren mit Klammer → negative Zahl subtrahieren → Zeichen zusammenfassen gemischt (4×) → Unterschied zweier Zahlen → Dezimalzahlen → mehrere Summanden → Prüfungshöhe: die Rechnung in der Klammer eines Termwert-Originals – Summe zweier Zahlen mit verschiedenen Vorzeichen, Differenz mit negativem Ergebnis (erster Schritt von 2016-OS-B1i, 2021-OS-B1g und 2026-FOR-B1g, alle Niveau I). Einheit 2 trägt keinen eigenen P10-Typ; die Vorzeichenrechnung dahinter liegt in Einheit 3.
```

Nur „mit den Beträgen begründen“ → „am Pfeilbild begründen (reicht
der Pfeil über die Null hinaus?)“. Alternative B, nicht als Zeile
ausgeführt: die Sprosse hinter „Zeichen zusammenfassen gemischt
(4×)“ setzen und davor eine Sprosse „Beträge: gleiche Vorzeichen
addieren, verschiedene subtrahieren“ aufnehmen – dann bliebe das
Urteil vom 28.09. (Sprosse gleich nach dem Grundfall) nicht
erhalten.

Beleg: [RLP] E „Änderung eines Zustandes“ (Z. 85, Vorstufe);
Grundvorstellung Z. 82 („Starte bei einer negativen Zahl und gehe
nach rechts, wo landest du?“); [LS-AA Kl. 7 I 3] (Z. 34).

## 7 bruchrechnung.md

**Befund** (stand.md Z. 95–97, Art a): „Katalog Z. 87 (Z. 25):
„Zähler geteilt statt Nenner mal“, das Beispiel 3/4 : 2 = 3/2 zeigt
den Nenner geteilt; die Bank folgt dem Beispiel (unverändert seit
27.09.).“ – Stand heute: trifft zu. Dazu: den Zähler zu teilen ist
kein Fehler, sondern ein richtiger Weg, wenn es aufgeht (drei
Viertel geteilt durch drei ist ein Viertel); der Fehler des
Beispiels ist der geteilte Nenner.

**Befund** (stand.md Z. 98–100, Art a): „Katalog Z. 35
„Schriftliches Rechnen“ gegen unterrichtsblatt 2.2 „Schriftliche
Multiplikation ist keine Fertigkeit der Zone“ (unverändert).“ –
Stand heute: trifft zu (unterrichtsblatt.md 2.2, wortgleich in
mappen/bruchrechnung.md Z. 487–488: „Schriftliche Multiplikation
ist keine Fertigkeit der Zone, sondern ein eigenes Thema.“); die
Zone des Blatts ist der Abschnitt „Fertigkeiten“ dieses Eintrags.

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 87: „Bruch geteilt durch Zahl: Zähler geteilt statt Nenner mal
  (3/4 : 2 = 3/2). [FD]“ – 3/2 entsteht aus 4 : 2 im Nenner.
- Z. 25: „… Fehler finden (Kehrbruch beim Multiplizieren; beim
  Teilen den Zähler geteilt) …“.
- Z. 35: „Schriftliches Rechnen mit natürlichen Zahlen, Einmaleins
  – Einheit 2 und 4. [RLP D]“.

**Vorschlag 7.1a – Fehlerzeile (ersetzt Z. 87)**

```
- Bruch geteilt durch Zahl: Nenner geteilt statt Nenner mal (3/4 : 2 = 3/2). [FD]
```

**Vorschlag 7.1b – Typzeile Einheit 3 (ersetzt Z. 25)**

```
Einheit 3: Bruch mal natürliche Zahl (vervielfachen) [OS 6, GYM 6] · Bruch geteilt durch natürliche Zahl (teilen) [OS 6, GYM 6] · Bruch von Bruch (Zähler mal Zähler, Nenner mal Nenner; Bruchteil einer Zahl oder Größe → brueche-dezimalzahlen.md Einheit 1) · vor dem Rechnen kürzen · gemischte Zahl mal Bruch (erst in unechten Bruch) · Zahl geteilt durch Bruch, Bruch geteilt durch Bruch (Kehrbruch) [OS 6, GYM 6] · Sachaufgabe (Rezept, Flaschen füllen) · Fehler finden (Kehrbruch beim Multiplizieren; beim Teilen durch eine Zahl den Nenner geteilt statt malgenommen) · Begründen (warum durch ein Halb mal zwei).
```

Beleg (7.1a und 7.1b): kein Beleg gefunden – Rechenprobe (drei
Viertel geteilt durch zwei ist drei Achtel, der Nenner wird
verdoppelt); die Fehlerzeile trägt nur [FD].

**Vorschlag 7.2 – Fertigkeitszeile ohne schriftliche Verfahren
(ersetzt Z. 35)**

```
- Einmaleins und Kopfrechnen mit natürlichen Zahlen (Vervielfachen, Teilen ohne Rest) – Einheit 2 und 4; die schriftlichen Verfahren sind kein Blatt-0-Stoff, sondern ein eigenes Thema (Unterrichtsblatt-Prompt, Abschnitt 2.2), die Zahlen der Sprossen bleiben im Kopf rechenbar. [RLP D]
```

Ein Katalogeintrag für die schriftlichen Verfahren gibt es nicht
(kein Eintrag mit „schriftlich“ außer diesem und brueche-
dezimalzahlen.md Z. 35 „Schriftlich oder mit Taschenrechner
dividieren“ – dort steht der Taschenrechner daneben, kein
Vorschlag).

Beleg: unterrichtsblatt.md 2.2 (blattbau; Wortlaut oben); [RLP] D
(Z. 35). Der Verweis steht ohne „.md“, weil verweis-pruef.py sonst
eine fehlende Datei zählt (Probe im Kopf).

## 8 kurvenuntersuchung.md

**Befund** (stand.md Z. 114–116, Art a): „Katalog: Die Sprosse
„Ändert sich die Monotonie …“ enthält „→“, das zugleich die
Sprossen der Kette trennt; wer die Kette an „→“ teilt, zerschneidet
sie in drei Stücke.“ – Stand heute: trifft zu.

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 126: „… → „Ändert sich die Monotonie, ändert sich die
  Krümmung?“ – an Graphen ankreuzen: Monotonie ändert sich →
  Extrempunkt; Monotonie bleibt und Krümmung ändert sich →
  Sattelpunkt; nichts rechnen → Sattelstelle ausschließen …“. Das
  Muster der Datei sonst: Doppelpunkt oder Komma innerhalb einer
  Sprosse (Z. 125 „Art über das Vorzeichen von f'' entscheiden und
  …“); Pfeile in Klammern kommen nur in Erkennungsschritten vor
  (Z. 41, ableitung-und-aenderungsrate.md Z. 39), die keine Kette
  sind.

**Vorschlag 8.1 – Sprosse ohne Pfeil (ersetzt Z. 126)**

```
- Extrempunkte nachweisen (Einheit 2): „gegeben oder gesucht“ ankreuzen (Vorstufe) → für eine genannte Stelle f' bilden und f' an der Stelle gleich null zeigen (Grundfall, viermal) → f'' an der Stelle auswerten und die Art benennen → den Funktionswert des vorgegebenen Punktes bestätigen (abi 2021-be-gk-B2.1c) → den Vorzeichenwechsel von f' statt f'' als Nachweis führen (iqb 2020MgrundlegendAAnalysis11-a, abi 2022-bebb-gk-B2.1a) → mit der gegebenen Angabe „f'' ungleich null“ die hinreichende Bedingung schließen (abi 2025-bebb-lk-A1.1a, iqb 2025MerhoehtAAnalysis12-a) → „Ändert sich die Monotonie, ändert sich die Krümmung?“ – an Graphen ankreuzen: Monotonie ändert sich: Extrempunkt; Monotonie bleibt und Krümmung ändert sich: Sattelpunkt; nichts rechnen → Sattelstelle ausschließen oder nachweisen: doppelte Nullstelle von f' ohne Vorzeichenwechsel, f''' ungleich null (abi 2022-bebb-lk-B2.1g, fhr 2021-B-2c) → „genau einen“ Tiefpunkt über die streng monotone Ableitung begründen (LK; abi 2022-bebb-lk-B2.1b) → Extremstelle ohne Rechnung in ein Intervall einschließen über die Vorzeichen von f' an den Intervallenden (abi 2019-be-gk-A1.1b) → Prüfungshöhe: Extremstelle einer Logarithmusfunktion über die Ableitung oder die Symmetrie begründen (LK; abi 2023-bebb-lk-A1.2b) und Aussagen zu Stellen mit waagerechter Tangente allgemein beurteilen (fhr 2020-C-1c, 2019-A-1c, Niveau III).
```

Nur die beiden Pfeile in der Sprosse sind Doppelpunkte; sonst
wortgleich.

Beleg: kein Beleg gefunden (Formfrage; bank.md „sprosse_text
wortgleich aus dem Katalog“, die Kette wird am Pfeil geteilt).

## 9 extremalprobleme.md

**Befund** (stand.md Z. 95–97, Art a): „Katalog: 2023-A-1f,
2022-bebb-gk-B2.1h und 2020MerhoehtAAnalysis11-a stehen an zwei
Sprossen, einmal davon auf einer Prüfungshöhe (wie 27.09.).“ –
Stand heute: trifft zu, in zwei verschiedenen Lagen.

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 80 (Kette Einheit 3): „… → mit Substitution lösen und Lösungen
  außerhalb des Intervalls verwerfen (fhr 2023-A-1f) → … →
  Prüfungshöhe: … fhr-Zielmarke: Maximum mit Substitution und
  Intervallprüfung (fhr 2023-A-1f, Niveau III).“ – dieselbe
  Kennung zweimal in derselben Kette; nach bank.md („je
  Verfahrenskette genau eine Prüfungssprosse … je Original zwei
  Zeilen“) bekäme das Original in einer Kette zweimal Zeilen.
- 2022-bebb-gk-B2.1h: Z. 79 (Einheit 2) „den Ansatz an einer Figur
  zwischen Ursprung und Graphenpunkt aufstellen (abi
  2022-bebb-gk-B2.1h als Ansatz)“ und Z. 80 (Einheit 3) „das
  achsenparallele Rechteck maximaler Fläche über die Zielfunktion
  aus Stelle mal Funktionswert (abi 2022-bebb-gk-B2.1h)“;
  2020MerhoehtAAnalysis11-a: Z. 78 (Einheit 1) „den Flächenterm
  eines Dreiecks unter dem Graphen begründen (iqb
  2020MerhoehtAAnalysis11-a, Teil A)“ und Z. 79 (Einheit 2,
  Prüfungshöhe) „den Flächenterm an einer Schar mit e-Funktion
  begründen (iqb 2020MerhoehtAAnalysis11-a, Teil A, Niveau I bis
  II)“. Diese beiden sind Teilaufgaben, die zwei Einheiten
  durchlaufen (Ansatz, dann Maximum; Figur, dann Zielfunktion); der
  Katalog nennt sie an beiden Stellen mit Absicht („als Ansatz“).
  Das ist kein Katalogfehler, sondern eine Bankfrage (Abschnitt F:
  wo das Original seine zwei Zeilen bekommt).

**Vorschlag 9.1 – Kennung nur an der Prüfungshöhe (ersetzt Z. 80)**

```
- Maximum bestimmen (Einheit 3): „Stelle, Seiten oder Inhalt?“ – ankreuzen, was verlangt ist (die Stelle, die Maße, der Extremwert) und ob Art und Randwerte zu prüfen sind; nichts rechnen (Vorstufe) → die Zielfunktion ableiten, null setzen und die Lösung im Definitionsbereich wählen (Grundfall, viermal) → die Art über die zweite Ableitung bestätigen und alle gefragten Größen mit Einheit angeben (fhr 2025-A-2f, 2020-C-2e) → mit Substitution lösen und Lösungen außerhalb des Intervalls verwerfen → Randmaximum: die Zielfunktion hat im Innern nur ein Minimum; das gesuchte Maximum über die Randwerte des Definitionsbereichs bestimmen (Vorrat: kein Abitur-GK-Beleg im Katalog) → das achsenparallele Rechteck maximaler Fläche über die Zielfunktion aus Stelle mal Funktionswert (abi 2022-bebb-gk-B2.1h) → den maximalen vertikalen Abstand zweier Graphen über die Differenzfunktion nachweisen (abi 2018-be-gk-B1.1g, 2020-be-gk-B2.1g, 2021-be-gk-B2.2i, 2024-bebb-gk-B2.2g) → den Parameter für den größten Flächeninhalt bestimmen (iqb 2020MerhoehtAAnalysis11-b, 2019MgrundlegendBAnalysisWTR2-1i) → eine Stelle als Maximalstelle über die notwendige Bedingung ausschließen (abi 2021-be-gk-A1.3b, Teil A) → Prüfungshöhe: zu vorgelegten Lösungsschritten die Extremwertaufgabe formulieren und die Schritte erläutern (iqb 2024MerhoehtBAnalysisWTR3-2f, Niveau III); fhr-Zielmarke: Maximum mit Substitution und Intervallprüfung (fhr 2023-A-1f, Niveau III).
```

Nur „(fhr 2023-A-1f)“ an der Sprosse „mit Substitution lösen“ ist
gestrichen; das Original bleibt Prüfungshöhe.

Beleg: kein Beleg gefunden – Formfrage nach bank.md (eine
Prüfungssprosse je Kette mit allen Originalen); das Original selbst
(fhr 2023-A-1f, Substitution mit Intervall) bleibt die fhr-Zielmarke
(Z. 87).

## 10 flaecheninhalt-durch-integration.md

**Befund** (stand.md Z. 100–103, Art e): „Katalog: Z. 105 nennt die
Vorstufe von e4 in der Klammer („Vorstufe: ist der Inhalt gegeben
oder gesucht?“), die übrigen Vorstufen enden auf „nichts rechnen“;
der Sprossentext bleibt dort unverändert.“ – Stand heute: trifft
zu.

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 105: „- Flächenbedingungen (Einheit 4): „Vorwärts oder
  rückwärts?“ als Startfrage (Vorstufe: ist der Inhalt gegeben oder
  gesucht?) → den Parameter einer Geraden …“ gegen die Form der
  übrigen Ketten, Z. 102–104, 106: „„Wo liegt die Fläche?“ – an
  Graphen ankreuzen, …; nichts rechnen (Vorstufe, Grundvorstellung)
  →“.

**Vorschlag 10.1 – Vorstufe in der Form der Nachbarketten (ersetzt
Z. 105)**

```
- Flächenbedingungen (Einheit 4): „Vorwärts oder rückwärts?“ – zu Aufgaben ankreuzen, ob der Flächeninhalt gegeben ist und ein Parameter oder eine Grenze gesucht wird, oder ob der Inhalt gesucht ist; nichts rechnen (Vorstufe) → den Parameter einer Geraden aus dem Flächeninhalt bestimmen (Grundfall, viermal; abi 2022-bebb-gk-A1.3a; iqb 2022MgrundlegendAAnalysis2, 2018MerhoehtAAnalysis11-b) → den Achsenschnittpunkt über Rechteck und Dreieck (iqb 2017MerhoehtAAnalysis2-b) → Flächen halbieren: senkrechte Gerade über den Flächenterm, parallele Gerade und Nullstellengerade über das Achsendreieck, Verschiebung über das Integral null (abi 2026-bb-gk-B2.2e; iqb 2026MgrundlegendBAnalysisWTR2-1e, 2024MerhoehtBAnalysisWTR3-2e, 2026MgrundlegendBAnalysisMMS1-2c, 2025MgrundlegendAAnalysis21-b) → die Parametergleichung aus einem markierten Scharflächenstück ansetzen (iqb 2020MgrundlegendBAnalysisWTR2-2c) → Existenz und Eindeutigkeit begründen: monoton wachsender Flächenterm, Flächenausgleich, Stetigkeit (abi 2022-bebb-gk-B2.1i; iqb 2024MgrundlegendBAnalysisWTR1-1c, 2020MgrundlegendBAnalysisWTR2-1g, 2019MgrundlegendBAnalysisWTR1-2f, 2026MerhoehtBAnalysisWTR3-1c, 2025MerhoehtBAnalysisWTR1-1e) → Prüfungshöhe: die Lösung über Punktsymmetrie und Rechteck ohne Rechnung (iqb 2025MgrundlegendBAnalysisWTR1-1d, Niveau II bis III), die Dreiecksnäherung als parameterunabhängig (iqb 2026MerhoehtBAnalysisMMS2-2e, Niveau III) und die eindeutige Lösung über die Monotonie (iqb 2026MerhoehtBAnalysisWTR3-1c, Niveau II); fhr-Zielmarke: keine – der fhr-Katalog stellt keine Flächenbedingungen.
```

Nur die Vorstufe ist neu gefasst; ab „→ den Parameter einer
Geraden“ wortgleich.

Beleg: kein Beleg gefunden (Formfrage); Inhalt aus dem Grundfall
(abi 2022-bebb-gk-A1.3a, iqb 2022MgrundlegendAAnalysis2 – Parameter
aus dem Flächeninhalt) und Einheit 1 bis 3 (Inhalt gesucht).

## 11 binomialverteilung.md

**Befund** (stand.md Z. 99–100, Art e): „Katalog: „Genau, höchstens
oder mindestens?“ ist weiter Vorstufe von zwei Ketten (e2 und
e3).“ – Stand heute: trifft zu, wortgleich (Z. 125, 126); der
Grundfall der Einheit 3 („den Wortlaut in P(X ≤ k) übersetzen“) tut
dasselbe noch einmal mit Rechnung.

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 125 und Z. 126 beginnen beide: „„Genau, höchstens oder
  mindestens?“ – zu Ereignissen die Grenze ankreuzen: genau k als
  Einzelwahrscheinlichkeit; höchstens, weniger als, mindestens, mehr
  als kumuliert, mit der richtigen ganzen Zahl k und mit oder ohne
  Gegenereignis; nichts rechnen (Vorstufe)“. Die Frage entscheidet
  zwischen Einheit 2 (genau) und Einheit 3 (kumuliert) und gehört
  deshalb vor Einheit 2; Einheit 3 braucht eine Vorstufe, die
  innerhalb des Kumulierten unterscheidet.

**Vorschlag 11.1 – eigene Vorstufe für Einheit 3 (ersetzt Z. 126)**

```
- Kumulierte Wahrscheinlichkeiten (Einheit 3): „Mit oder ohne Gegenereignis?“ – zu Ereignissen ankreuzen, ob P(X ≤ k) unmittelbar aus der Tabelle kommt (höchstens, weniger als) oder über eins minus P(X ≤ k) (mindestens, mehr als), und welches ganzzahlige k gilt; nichts rechnen (Vorstufe) → den Wortlaut in P(X ≤ k) übersetzen: höchstens, weniger als, mindestens, mehr als (Grundfall, viermal) → den Wert mit der Rechnerfunktion oder aus der Tabelle holen (abi 2026-bb-gk-B4b, iqb 2026MgrundlegendBStochastikWTR1-1b) → das Gegenereignis für „mindestens“ und „mehr als“ (iqb 2020MgrundlegendBStochastikWTR1-1a, abi 2022-bebb-lk-B4k) → das Intervall als Differenz zweier kumulierter Werte mit richtig gesetzter unterer Grenze (abi 2018-be-gk-B3.2a, iqb 2024MerhoehtBStochastikWTR2-1c) → Anteile in Anzahlen umrechnen: „mehr als die Hälfte“, „höchstens siebzig Prozent“ (abi 2023-bebb-lk-B4a, iqb 2024MgrundlegendBStochastikWTR2-2a, 2025MerhoehtBStochastikWTR1-1c) → eine Verhältnis- oder Summenbedingung in eine Ungleichung für X übersetzen (abi 2023-bebb-gk-B4.1d, iqb 2018MgrundlegendBStochastikWTR3-2b) → die Abweichung vom Erwartungswert als Intervall oder als einseitige Schranke (iqb 2019MgrundlegendBStochastikWTR1-1a, abi 2025-bebb-lk-B4b) → einen Summenterm in eine Sachaussage übersetzen: Grenzen, p, Gegenereignis (abi 2023-bebb-gk-B4.1e, iqb 2026MgrundlegendBStochastikWTR2-1d, 2021MgrundlegendBStochastikWTR3-1d) → Prüfungshöhe: zwei Binomialmodelle verketten – die Fehlerwahrscheinlichkeit einer Einheit als p der zweiten Verteilung, ein zweistufiger Prüfplan, eine in Abschnitte geteilte Kette (abi 2021-be-gk-B4d, 2022-bebb-lk-B4m; iqb 2023MerhoehtBStochastikWTR3-1c, 2023MgrundlegendBStochastikWTR1-2a, Niveau II bis III) und eine Ungleichung mit Binomialsumme als Sachaussage formulieren (iqb 2024MgrundlegendAStochastik21-b, 2020MgrundlegendAStochastik2-b, Niveau III).
```

Nur die Vorstufe ist neu; ab „→ den Wortlaut“ wortgleich.

Beleg: [Prüfung] iqb 2020MgrundlegendBStochastikWTR1-1a, abi
2022-bebb-lk-B4k (Gegenereignis für „mindestens“, Sprosse 3 der
Kette), abi 2026-bb-gk-B4b (Tabellenwert, Sprosse 2); [GOST] Q2 L5
(Lerneinheit 3, Z. 15: „Gegenereignis 1 − P(X ≤ k − 1)“);
Rohdatei-Fehlerquelle „Erfolg und Misserfolg vertauscht“ (Z. 43).

## 12 skalarprodukt-und-winkel.md

**Befund** (stand.md Z. 102–103, Art a): „Katalog: 2017-bb-ea-B3.1b
ist Prüfungshöhe in e2 und e3; in e2 verlangt es Ebenen-Normalen,
die erst e3 einführt.“ – Stand heute: trifft zu; der Eintrag weiß
es selbst (Z. 107, Punkt 11: „Die Sprossen der Einheiten 2 und 3
nennen 2017-bb-ea-B3.1b weiter als stumpfen Zeltwinkel – beim
Gegenlesen auf Einheit 3 allein ziehen.“).

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 95 (Prüfungshöhe Einheit 2): „… und den stumpfen Innenwinkel
  des Zelts über den Nebenwinkel der Normalenrechnung (abi
  2017-bb-ea-B3.1b, Niveau II).“; Z. 96 (Prüfungshöhe Einheit 3):
  „… und den stumpfen Zeltwinkel vollständig führen (abi
  2017-bb-ea-B3.1b, Niveau II).“; Z. 104 (Zielmarke): „Einheit 2 –
  abi: der Winkel der Zeltkanten (2026-bb-ea-B3b, Niveau II) und
  der Trapezwinkel (2019-be-gk-B3.2c, Niveau …)“ – die Zielmarke
  nennt für Einheit 2 schon andere Originale.

**Vorschlag 12.1 – Prüfungshöhe Einheit 2 ohne Zeltwinkel (ersetzt
Z. 95)**

```
- Winkel zwischen Vektoren, Kanten und Geraden (Einheit 2): „Welche zwei Richtungen bilden den Winkel?“ ankreuzen (Vorstufe) → den Winkel zweier Kanten vom Scheitel aus berechnen (Grundfall, viermal; abi 2026-bb-gk-B3b, 2026-bb-ea-B3b; iqb 2026MgrundlegendBAGLAA2WTR2-1b, 2026MerhoehtBAGLAA2WTR2-1b, 2026MgrundlegendBAGLAA2MMS2-1c) → den Innenwinkel eines Trapezes an der richtigen Ecke ansetzen (abi 2019-be-gk-B3.2c, iqb 2019MgrundlegendBAGLAA2WTR1-1c) → den Innenwinkel eines Dreiecks am Körper (abi 2018-bb-ea-B3.1c) → den rechten Winkel über das Skalarprodukt null nachweisen (abi 2024-bebb-gk-B3b; iqb 2022MerhoehtBAGLAA1WTR-1a) → den spitzen Winkel zwischen zwei Geraden mit Betrag im Zähler (iqb 2021MgrundlegendBAGLAA2WTR2-1d) → Prüfungshöhe: die Innenwinkel über die Gleichseitigkeit statt dreier Einzelrechnungen bestimmen (iqb 2023MerhoehtBAGLAA1WTR-2a, Niveau II) und den Innenwinkel eines Trapezes aus zwei Kantenvektoren vom Scheitel aus (abi 2019-be-gk-B3.2c, Niveau II); der stumpfe Zeltwinkel über Normalenvektoren (abi 2017-bb-ea-B3.1b) liegt in Einheit 3.
```

Nur die Prüfungshöhe ist geändert; das Trapez-Original steht damit
an Sprosse 2 und an der Prüfungshöhe (Sprosse als Ansatz,
Prüfungshöhe als ganze Rechnung) – dieselbe Doppellage wie in
Abschnitt 9; wer das nicht will, nimmt für die abi-Prüfungshöhe
2018-bb-ea-B3.1c (Dreieck am Körper) und streicht es an Sprosse 3.

Beleg: [Prüfung] abi 2019-be-gk-B3.2c (Zielmarke Einheit 2,
Z. 104), abi 2017-bb-ea-B3.1b (abi-katalog.csv: „Stumpfen Winkel
zwischen zwei benachbarten Seitenflächen eines Körpers über die
Normalenvektoren berechnen“, Ebene E: −39y + 25z = 0 – das ist
Einheit 3, Z. 96 und Z. 107 Punkt 11).

## 13 stammfunktion-und-hauptsatz.md

**Befund** (stand.md Z. 106–108, Art a): „Katalog: Die Vorstufe e2
nennt 2025-bebb-lk-B2.2b, das Original steht aber als Gegenstück an
Sprosse 3 (Ableitung); die Vorstufe trägt die beiden
iqb-Originale.“ – Stand heute: trifft zu; die Kennung steht
zweimal in der Kette. Zu beachten: Z. 117 „Änderungen 2026-09-29b
(Chat, Lehrer): … als Vorstufe vor den Grundfall gezogen, Belege
bleiben (bank.md: original an jeder Höhe)“ – die Kennung an der
Vorstufe ist Entscheidung des Chats; offen ist nur das Doppel an
Sprosse 3.

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 95: „mit vorgegebener Stammfunktion nur einsetzen: F(b) − F(a),
  auch mit negativem F(a) (Vorstufe; abi 2025-bebb-lk-B2.2b; iqb …)
  → … → das Integral über die Ableitung als Differenz von
  Funktionswerten (abi 2025-bebb-lk-B2.2b als Gegenstück,
  2025-bebb-lk-B2.2c als Vorbereitung) → …“. Das Original
  (abi-katalog.csv: gesucht „∫_0^2 f_0'(x) dx“, Verfahren
  „Hauptsatz mit f_0 als Stammfunktion“) ist genau die Vorstufe
  (F vorgegeben, nur einsetzen).

**Vorschlag 13.1 – Kennung nur an der Vorstufe (ersetzt Z. 95)**

```
- Hauptsatz (Einheit 2): mit vorgegebener Stammfunktion nur einsetzen: F(b) − F(a), auch mit negativem F(a) (Vorstufe; abi 2025-bebb-lk-B2.2b; iqb 2026MerhoehtBAnalysisWTR3-1b, 2025MerhoehtBAnalysisWTR3-2c) → das bestimmte Integral einer ganzrationalen Funktion mit selbst gebildeter Stammfunktion (Grundfall, viermal; iqb 2018MgrundlegendBAnalysisWTR-1d, 2023MgrundlegendAAnalysis13-a, 2026MgrundlegendAAnalysis13-a; abi 2026-bb-gk-A1.1a) → über eine volle Periode: der trigonometrische Anteil liefert null (iqb 2021MgrundlegendAAnalysis13-a) → das Integral über die Ableitung als Differenz von Funktionswerten (abi 2025-bebb-lk-B2.2c als Vorbereitung; das Gegenstück 2025-bebb-lk-B2.2b trägt die Vorstufe) → Prüfungshöhe: exakter Wert und prozentuale Abweichung eines Näherungswerts (abi 2025-bebb-gk-B2.2d; iqb 2025MgrundlegendBAnalysisWTR2-1d, 2022MgrundlegendBAnalysisWTR1-1f, Niveau II).
```

Beleg: [Prüfung] abi 2025-bebb-lk-B2.2b (abi-katalog.csv, Spalten
gesucht und verfahren, oben); Z. 117 des Eintrags (Entscheidung
29.09.b).

## 14 tangente-normale-schnittwinkel.md

**Befund** (stand.md Z. 121–123, Art e): „Katalog: Die Vorstufe s−1
von e1 und e4 („Was ist gegeben?“) ist wortgleich dieselbe; die
Ankreuzzeilen sind verschieden, aber der Handgriff ist derselbe.“ –
Stand heute: trifft zu (Z. 117, 120).

**Befund** (stand.md Z. 124–126, Art e): „Katalog: e2 bis e5
bleiben bei einer Vorstufe; nur e1 hat die Anstiegsvorstufe, obwohl
e3 (Normale) denselben Schritt f'(x₀) vor dem negativen Kehrwert
braucht.“ – Stand heute: trifft zu; der Grundfall der Einheit 3
startet bei einer gegebenen Tangentensteigung, der fehlende
Handgriff ist der negative Kehrwert allein.

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 117 und Z. 120 beginnen beide: „„Was ist gegeben?“ ankreuzen:
  Punkt gegeben (ableiten und einsetzen), Steigung gegeben
  (f'(x) = m lösen) oder Winkel gegeben oder gesucht (erst über den
  Tangens in eine Steigung übersetzen); nichts rechnen (Vorstufe
  …)“; Z. 120 hat dahinter eine zweite Vorstufe „„Welcher Winkel?“
  …“ (eingefügt 29.09.).
- Z. 117: „… → nur den Anstieg: zu Funktion und Stelle f'(x₀)
  ausrechnen, Antwortgerüst m = (Lücke), keine Gerade aufstellen
  (Vorstufe) → …“; Z. 119: „„Tangente oder Normale?“ – … nichts
  rechnen (Vorstufe) → aus einer Tangentensteigung den negativen
  Kehrwert bilden und die Gerade durch den Punkt aufstellen
  (Grundfall, viermal) → …“ – kein Zwischenschritt.

**Vorschlag 14.1 – Einheit 4 nur mit „Welcher Winkel?“ (ersetzt
Z. 120)**

```
- Winkel (Einheit 4): „Welcher Winkel?“ – ankreuzen, ob der Steigungswinkel gegen die positive x-Richtung (null bis hundertachtzig Grad) oder der Schnittwinkel (höchstens neunzig Grad) gefragt ist; nichts rechnen (Vorstufe) → aus einer Steigung den Winkel über den Arkustangens, aus einem Winkel die Steigung über den Tangens (Grundfall, viermal) → den Steigungswinkel des Graphen in einem Punkt und den Auftreffwinkel an der Nullstelle (iqb 2020MgrundlegendBAnalysisWTR2-1d, 2018MerhoehtBAnalysisWTR2-1f) → Tangentengleichung und Schnittwinkel mit der x-Achse nebeneinander (abi 2020-be-gk-B2.1f; iqb 2026MgrundlegendBAnalysisWTR1-1c) → den Winkel gegen eine senkrechte Kante als Ergänzung (iqb 2026MerhoehtBAnalysisWTR2-2c, 2023MerhoehtBAnalysisWTR2-1d) → Steigungswinkel und Nebenwinkel einzeichnen und deuten (iqb 2025MerhoehtBAnalysisMMS2-2b) → den Schnittwinkel zweier Graphen über beide Tangentensteigungen (abi 2018-be-gk-B1.2b, 2022-bebb-gk-B2.1e, 2023-bebb-gk-B2.1j) → den senkrechten Schnitt über das Produkt der Steigungen (abi 2026-bb-ea-A1.2b; iqb 2026MerhoehtAAnalysis11-b, Teil A) → die Wendetangente mit Steigungswinkel und y-Achsenabschnitt (abi 2022-bebb-gk-B2.2e) → den Bereich mit Mindeststeigungswinkel über die Ungleichung (abi 2022-bebb-gk-B2.2f) → Prüfungshöhe: die Winkelhalbierende über den halben Steigungswinkel (abi 2026-bb-ea-B2.1d, Niveau III), den Öffnungswinkel als doppelten Steigungswinkel (abi 2024-bebb-gk-B2.1i, Niveau III), Scharparameter aus Winkelbedingungen (abi 2024-bebb-lk-B2.1h, 2025-bebb-gk-B2.1d) und vorgelegte Rechenschritte berichtigen (abi 2021-be-gk-B2.2k, Niveau III); fhr-Zielmarke: keine – der RLP FOS kennt keine Winkel an Tangenten.
```

Die erste Vorstufe entfällt; sie bleibt in Einheit 1 (Z. 117), wo
sie die Grundvorstellung trägt. Nach der Regelfassung am Ende wäre
das auch ohne Katalogänderung die Bankfolge (Zeilen einmal, bei der
ersten Kette); der Katalog liest sich ohne das Doppel klarer.

Beleg: kein Beleg gefunden (Formfrage; die Vorstufe in Z. 117
trägt ihre Belege dort).

**Vorschlag 14.2 – Vorstufe „nur die Normalensteigung“ Einheit 3
(ersetzt Z. 119)**

```
- Normale (Einheit 3): „Tangente oder Normale?“ – ankreuzen, welche Gerade gebraucht wird und welche Steigung sie hat: die Tangente den Ableitungswert, die Normale den negativen Kehrwert; nichts rechnen (Vorstufe) → nur die Normalensteigung: zu einer gegebenen Tangentensteigung den negativen Kehrwert bilden, Antwortgerüst m gleich (Lücke), keine Gerade aufstellen (Vorstufe) → aus einer Tangentensteigung den negativen Kehrwert bilden und die Gerade durch den Punkt aufstellen (Grundfall, viermal) → die Normalengleichung nach Funktionswert und Anstieg (fhr 2025-A-1h, 2023-A-1c, 2022-B-1f) → die Gerade senkrecht zu einer gegebenen Tangente durch einen Punkt (iqb 2025MerhoehtBAnalysisWTR2-1b) → die Länge der Normalen bis zur x-Achse (iqb 2024MerhoehtBAnalysisWTR3-1d) → Lotgerade, Lotfußpunkt und Abstand (iqb 2023MgrundlegendAAnalysis11-b) → den Mittelpunkt eines berührenden Kreises auf der Normalen (abi 2026-bb-ea-B2.2e; iqb 2026MerhoehtBAnalysisWTR1-1e, 2026MgrundlegendBAnalysisWTR1-1f) → Prüfungshöhe: eine vorgelegte Abstandsrechnung über die Normalenbedingung deuten (iqb 2023MerhoehtBAnalysisWTR2-2d, 2026MerhoehtBAnalysisWTR2-2d, Niveau II bis III) und den Lösungsweg für eine gemeinsame Normale zweier Kurven erläutern (abi 2022-bebb-gk-B2.2j, Niveau III); fhr-Zielmarke: Normalengleichung mit Funktionswert und Anstieg (fhr 2022-B-1f, 2025-A-1h, Niveau II).
```

Neu ist die zweite Vorstufe nach dem Muster von Z. 117 („nur den
Anstieg … Antwortgerüst … keine Gerade aufstellen“); sonst
wortgleich. Die Kette hat dann zwei Vorstufen (0 und −1), wie
Einheit 1.

Beleg: [Prüfung] fhr 2025-A-1h, 2023-A-1c, 2022-B-1f
(Normalengleichung nach Funktionswert und Anstieg – der Kehrwert
ist dort der Fehlerschritt); Vorbild Z. 117 (Vorstufe „nur den
Anstieg“, Urteil vom 28.09.).

## 15 lagebeziehungen.md

**Befund** (stand.md Z. 107–108, Art d mit Katalogfolge): „Katalog:
„Wer und wogegen?“ steht als Erkennungsschritt vor e1 und e3 und
zugleich als Vorstufe von e2 (Befund vom 27.09.).“ – Stand heute:
trifft zu (Z. 38 „Vor Einheit 1 und 3.“, Z. 94 „Parameter aus der
Lagebedingung (Einheit 2): „Wer und wogegen?“ ankreuzen (Vorstufe)
→ …“). Der Bereich lässt die Einheit aus, in der der Schritt als
Vorstufe steht; Prüfstein 14 am Ende.

**Vorschlag 15.1 – Bereich des Erkennungsschritts (ersetzt Z. 38)**

```
- „Wer und wogegen?“ – zu Aufgabentexten ankreuzen, welche Objekte beteiligt sind (Punkt gegen Ebene, Gerade gegen Ebene) und welche Gleichung die Prüfregel ist; nichts rechnen. Vor Einheit 1 bis 3. [GOST Q3 L3 „Lagebeziehungen zwischen: …“; Rohdatei: Klassen Punkt und Ebene, Gerade und Ebene]
```

Beleg: Z. 94 des Eintrags (Vorstufe der Einheit 2, Urteil vom
27./28.09.); [GOST Q3 L3] (Z. 38).

## 16 ableitung-und-aenderungsrate.md

**Befund** (stand.md Z. 119–120, Art a): „Katalog: „Mittel oder
Moment?“ (Z. 39: „Vor Einheit 1 und 2“) ist Vorstufe von E1 und E3
(Z. 110, 112), nicht von E2.“ – Stand heute: trifft zu (Z. 111,
Einheit 2, hat „Wie hoch, wie steil?“).

**Vorschlag 16.1 – Bereich des Erkennungsschritts (ersetzt Z. 39)**

```
- „Mittel oder Moment?“ – zu Aufgabentexten ankreuzen, ob ein Zeitraum genannt ist („in den ersten sieben Tagen“, „von acht bis zehn Uhr“, „durchschnittlich pro Stunde“ → Differenzenquotient, Sekante) oder ein Zeitpunkt („zum Zeitpunkt“, „nach genau“, „momentan“, „Geschwindigkeit bei“ → Ableitung, Tangente); nichts rechnen. Vor Einheit 1 und 3. [GOST Q1 L2 „mittlere und lokale Änderungsrate“; Rohdatei-Fehlerquellen „h'(7) statt des Differenzenquotienten“ (2019-be-gk-B2.2d), „Term als momentane Änderungsrate deuten“ (2025-bebb-lk-B2.2h); iqb 2026MgrundlegendBAnalysisWTR1-2c]
```

Nur „Vor Einheit 1 und 2“ → „Vor Einheit 1 und 3“. Nach der
Regelfassung am Ende entfällt der Schritt dann in der Bank ganz
(beide Einheiten des Bereichs haben ihn als Vorstufe); mit dem
alten Bereich hätte die neue Regel ihn in Einheit 2 angelegt, wo
er nicht hingehört.

Beleg: Z. 110, 112 des Eintrags (Vorstufen); [GOST Q1 L2] (Z. 39);
Lerneinheit 3 (Z. 15: „die Tangente als Grenzlage der Sekanten“ –
Sekante und Tangente sind dort das Thema).

## 17 Art (b) – Kennungen ohne Mappeneintrag (elf Befunde)

Einträge: kurvenuntersuchung, extremalprobleme, geraden,
flaecheninhalt-durch-integration, binomialverteilung,
funktionsklassen-und-eigenschaften, lagebeziehungen,
zufallsexperimente-und-pfadregeln, ableitung-und-aenderungsrate,
ebenen.

**Befunde** (elf, Art b): kurvenuntersuchung stand.md Z. 117–118
(„Die Prüfungshöhe von „Extrempunkte nachweisen“ nennt nur
Kennungen, die nicht in Abschnitt 2 der Mappe stehen“);
extremalprobleme Z. 92–94 („die Sprossen nennen 2020-C-2d,
2020-C-2e, 2025-A-2f, 2019MgrundlegendBAnalysisWTR2-1g und
2020MerhoehtAAnalysis11-b; die Mappe führt sie nicht in Abschnitt
2“); geraden Z. 102–104 („2019-be-gk-B3.1c und
2018MgrundlegendBAGLAA2WTR2-1e“); flaecheninhalt-durch-integration
Z. 94–99 („Neun Kennungen der Prüfungssprossen fehlen in Abschnitt
2“); binomialverteilung Z. 101–103 („2024-bebb-lk-A1.9a,
2021-be-gk-B4d, 2023MgrundlegendBStochastikWTR1-2a und weitere“);
funktionsklassen-und-eigenschaften Z. 104–106 („etwa
2023MerhoehtBAnalysisWTR2-2c“) und Z. 107–108 („30 Originale in
Abschnitt 2 (CAS-Nachtrag 2017/2018) stehen an keiner Sprosse“);
lagebeziehungen Z. 109–110 („2026MerhoehtBAGLAA2MMS2-1d“);
zufallsexperimente-und-pfadregeln Z. 108–111
(„2023MgrundlegendBStochastikWTR1-2d, 2019MgrundlegendBStochastik
WTR2-3a, 2026MerhoehtAStochastik21-a und -b“);
ableitung-und-aenderungsrate Z. 114–118 (sieben Kennungen); ebenen
Z. 110–112 („2024MerhoehtBAGLAA2WTR1-1c,
2026MgrundlegendBAGLAA2WTR1-1c und 2026MerhoehtBAGLAA2MMS2-1b“).

**Prüfung:** Alle 41 in den stand.md-Dateien einzeln genannten
Kennungen stehen in den Prüfungskatalogen (fhr-katalog.csv,
abi-katalog.csv, iqb-katalog.csv; grep nach `^"<id>";`); keine ist
falsch geschrieben. Die Ursache ist eine Regel des Skripts:
werkzeuge/mappe.py (aufgabenbank) nimmt in Abschnitt 2 nur
Kennungen aus dem Abschnitt „Prüfungsform“ und aus Zeilen, die mit
„Zielmarke“ beginnen (Funktion `originale`: `pf = abschnitt(…,
"Prüfungsform")`, `ziel = … z.startswith("Zielmarke")`); Kennungen
in den Sprossenketten („Für schwache Schüler“) meldet es als „Nur
außerhalb von „Prüfungsform“ genannt, nicht aufgenommen“. Die
Sek-II-Einträge führen ihre Originale aber in den Ketten, die
Prüfungsform nennt Typen mit Zeilenzahl und nur die Zielmarke
einzelne Kennungen. Zahl der so ausgelassenen Kennungen je Mappe
(Zeile „Nur außerhalb …“): kurvenuntersuchung 90 (Abschnitt 2: 84),
flaecheninhalt-durch-integration 45 (104), binomialverteilung 115
(72), funktionsklassen-und-eigenschaften 145 (87),
zufallsexperimente-und-pfadregeln 122 (140), tangente-normale-
schnittwinkel 71 (78), stammfunktion-und-hauptsatz 9 (50),
ableitung-und-aenderungsrate 7 (61), extremalprobleme 5 (22),
ebenen 4 (51), geraden 2 (45), ableitungsregeln 2 (30),
lagebeziehungen 1 (42); abstaende, skalarprodukt-und-winkel,
vektoren-und-rechenoperationen 0. Die Prüfliste der Einträge
(„Jedes Original … mit seiner id in der Prüfungsform“, Regel 10j)
ist in Sek II nicht so gebaut; Kennzahl 5 zählt jede Nennung, auch
in der Kette.

**Vorschlag B.1 – Skript statt Katalogzeilen (werkzeuge/mappe.py,
Funktion `originale`, nicht Teil dieser Datei, weil aufgabenbank
nicht berührt wird):** die Quelle der Kennungen um den Abschnitt
„Für schwache Schüler“ erweitern.

```
    pf = abschnitt(eintrag_text, "Prüfungsform")
    ketten = abschnitt(eintrag_text, "Für schwache Schüler")
    ziel = "\n".join(z for z in eintrag_text.split("\n")
                     if z.startswith("Zielmarke"))
    quelle = pf + "\n" + ketten + "\n" + ziel
```

Wirkung: Abschnitt 2 wächst um die genannten Zahlen (bei
funktionsklassen von 87 auf 232 Originale); die Mappe wird länger,
Lesen ist der Kostentreiber – der Chat entscheidet, ob die Mappe
statt dessen je Kette nur die Kennungen der Prüfungshöhen
aufnimmt (dann: nur Kennungen hinter „Prüfungshöhe:“ aus dem
Abschnitt). Ohne Skriptänderung wäre die Katalogseite: je Eintrag
eine Zeile „Originale der Ketten: …“ unter „Prüfungsform“ mit bis
zu 145 Kennungen – nicht ausgeführt, weil das die Prüfungsform
verdoppelt und beim nächsten Kettenumbau veraltet.

Beleg: werkzeuge/mappe.py Z. 199–204 (Funktion `originale`);
mappen/<eintrag>.md, Zeile „Nur außerhalb von „Prüfungsform“
genannt“; Zählung oben.

**Gegenrichtung (funktionsklassen-und-eigenschaften, 30 Originale
ohne Sprosse):** geprüft – 30 der 87 Kennungen aus Abschnitt 2 der
Mappe kommen im Abschnitt „Für schwache Schüler“ des Eintrags nicht
vor (2017-be-gk-B1.2a, 2017-be-gk-cas-B1.2a, 2017-bb-ea-cas-B2.1a,
2018-bb-ea-B2.2a, 2017MgrundlegendBAnalysisWTR-1a/-1b/-2a/-2b,
2017MerhoehtBAnalysisWTR1-1a/-1e, WTR2-1b/-1c/-1h/-2a,
WTR3-1b/-2a/-2b/-2c, CAS1-2a/-2f/-2g, CAS2-1c,
2017MgrundlegendBAnalysisCAS-1a, 2018MerhoehtBAnalysisCAS1-2a/-2b/
-2c, CAS2-1b/-2a/-2g, 2017MgrundlegendAAnalysis12-a). Das sind die
Zeilen des CAS-Nachtrags 2017/2018 und des Hefts 2017-be-gk, die
am 28./29.09. in die Prüfungsform, nicht in die Ketten
nachgezogen wurden. Kein Zeilenvorschlag: je Original ist eine
Sprosse zu wählen (Urteil), das gehört in einen Katalogauftrag
„Ketten um den CAS-Nachtrag“ mit denselben Regeln wie der Nachzug
vom 29.09. (Beleg: abi-katalog.csv, iqb-katalog.csv, die Kennungen
oben).

## 18 Art (c) ohne Vorschlag – zufallsexperimente-und-pfadregeln

**Befund** (stand.md Z. 106–107, Art c): „Katalog: Die Typen-Zeilen
32–39 nennen keinen Anwendungs- und keinen Darstellungstyp.“ –
Stand heute: trifft dem Wort nach zu, in der Sache nicht. Die
Typzeilen sind die Haupttypen der Rohdatei in der Folge
„Berechnung — Nachweis — Deutung“; die Deutungstypen sind
Darstellung und Anwendung: Einheit 4 „Baumdiagramm mehrstufig ohne
Zurücklegen darstellen (10; fhr)“, Einheit 6 „Baumdiagramm zu einer
zweistufigen Situation erstellen (15)“, Einheit 1 „Term und
Ereignis: Schnittwahrscheinlichkeit zweier Ereignisse im
Sachzusammenhang deuten (3)“, Einheit 7 „Ereignis zu einem
gegebenen Wahrscheinlichkeitsterm beschreiben (23)“. Kein
Vorschlag; für die Bank (bank.md „anwendung 3, darstellung 3, wo
die Typen der Einheit sie tragen“) heißt das: in Sek II tragen die
Deutungstypen die Pflichtelemente, die Wörter „Anwendung“ und
„Darstellung“ kommen in den Typzeilen nicht vor. Das gehört als
Satz in bank.md, nicht in den Katalog (Abschnitt F).

## F Bank- und Skriptfragen (Art f, nur genannt)

- lineare-gleichungen Z. 80–81: „Umkehroperation benennen“ (Z. 32)
  „vor Einheit 1 und 2“, nach bank.md nur in e1 – Bankregel, der
  Katalog ist stimmig.
- brueche-dezimalzahlen Z. 110–111, prozentrechnung Z. 88–90:
  `bank-pruef.py --katalog` erwartet eine Katalogdatei, die Sitzung
  hat nur die Mappe – Skriptfrage (Mappe Abschnitt 1 als Katalog
  lesen).
- rationale-zahlen Z. 91–93: „die ersten zwei Varianten“ mit
  Antwortgerüst beim Päckchen – bank.md.
- extremalprobleme Z. 89–91: Vorstufentexte enden mit „(Vorstufe)“
  bzw. „(Vorstufe, Grundvorstellung)“, sprosse_text endet vor der
  Klammer – Bankkonvention, kein Katalogbefund; ebenso
  ableitungsregeln Z. 85–87 („(Vorstufe) →“ trennt zwei Vorstufen).
- extremalprobleme (Abschnitt 9): ein Original, das zwei Einheiten
  durchläuft (Ansatz in E2, Maximum in E3), steht an zwei Sprossen
  – wo es seine zwei Prüfungszeilen bekommt, regelt bank.md nicht.
- geraden Z. 105–107: „dieselben Körper durch die ganze Kette“
  gegen Übernahme wortgleicher Zeilen – bank.md.
- abstaende Z. 110–111, funktionsklassen Z. 109–110: Ketten nennen
  den Grundfall „viermal“ bzw. „(4×)“ (Form aus _vorlage.md:
  „Grundfall (4×)“ – Blattzahl), bank.md fünf Zeilen (Bankzahl) –
  zwei Zahlen mit zwei Bedeutungen; ein Satz in bank.md („(4×) im
  Katalog ist die Zahl auf dem Blatt, die Bank hält fünf“) würde
  die Frage schließen. Kein Katalogvorschlag.
- vektoren-und-rechenoperationen Z. 95–96: 2018-bb-ea-B3.2c „trägt
  keine eigene Sprosse“ – der Katalog nennt es an e2 s2 neben dem
  iqb-Original (Z. 82) und als abi-Zielmarke (Z. 90); die Bank hat
  die Sprosse mit dem iqb-Original belegt (Dublettenregel). Kein
  Katalogbefund.
- ableitung-und-aenderungsrate Z. 121–123: Prüfungssprossen fassen
  zwei Originale in einem Satz, sprosse_text über 250 Zeichen –
  Folge der Regel „alle Originale an einer Prüfungssprosse“
  (bank.md 29.09.); Bankfrage (Kürzung des sprosse_text auf den
  Teil vor der Klammer).
- zufallsexperimente (Abschnitt 18): Pflichtelemente aus
  Deutungstypen – bank.md.

## R Regel zu Erkennungsschritten und Vorstufen (bank.md)

**Anlass.** Die Regel in bank.md (11d6a36) Z. 164–171 lautet:

> Erkennungsschritt 4 Zeilen: eigene Kette, nur Sprosse 0; er
> steht einmal, in der ersten Einheit seines Bereichs
> (unterrichtsblatt 2.3 a).
>
> Verlangt ein Erkennungsschritt denselben Handgriff wie die
> Vorstufe einer Kette derselben Einheit, entfällt der
> Erkennungsschritt; die Vorstufe bleibt. stand.md nennt den Fall
> unter „Befunde" als Katalogbefund (der Katalog führt beide).

Sie lässt vier Dinge offen, und die Agenten haben sie verschieden
gelesen: (1) Was „derselbe Handgriff“ ist – wortgleich (kurven-
untersuchung, ebenen) oder dieselbe Entscheidung (abstaende,
pythagoras, vektoren „nah beieinander“). (2) Was gilt, wenn der
Schritt in der ersten Einheit seines Bereichs als Vorstufe steht,
in einer späteren Einheit des Bereichs aber nicht: ebenen hat ihn
ganz gestrichen („steht auch vor e4 nicht“), skalarprodukt und
abstaende haben ihn in die nächste Einheit ohne solche Vorstufe
gesetzt, binomialverteilung ihn in e3 als eigene Kette behalten.
(3) Was gilt, wenn die Vorstufe in einer Einheit außerhalb des
Bereichs steht (lagebeziehungen: Schritt vor e1 und e3, Vorstufe
von e2). (4) Zwei Ketten mit derselben Vorstufe (tangente e1/e4,
binomialverteilung e2/e3, ebenen e2 k1/k2, kurvenuntersuchung e2
k1/k2) – dazu sagt die Regel nichts.

**Vorschlag R.1 – ersetzt bank.md Z. 164–171 (zwei Absätze durch
einen):**

```
Erkennungsschritt 4 Zeilen: eigene Kette, nur Sprosse 0
(unterrichtsblatt 2.3 a). Er wird einmal angelegt, in der ersten
Einheit seines Bereichs („Vor Einheit …“ im Katalog), in der keine
Kette eine Vorstufe mit demselben Handgriff hat; hat jede Einheit
des Bereichs eine solche Vorstufe, entfällt er. Derselbe Handgriff
heißt: dieselbe Entscheidung an derselben Art Vorlage (ankreuzen,
ob eine Stelle gegeben oder gesucht ist; „von“ im Text markieren),
gleich, wie die Frage heißt und ob die Ankreuzzeilen anders lauten.
Eine andere Entscheidung oder eine andere Vorlage ist ein anderer
Handgriff (Länge wählen gegen Dreieck finden; was fehlt gegen was
gemeint ist), auch wenn beide nach Zahl oder Richtung fragen. Zwei
Ketten mit Vorstufen desselben Handgriffs, auch in verschiedenen
Einheiten: die Zeilen stehen einmal, bei der ersten Kette in der
Reihenfolge der Datei; die zweite Kette beginnt mit dem Grundfall.
Jeder dieser Fälle steht in stand.md unter „Befunde“ als
Katalogbefund mit beiden Stellen (Erkennungsschritt oder erste
Vorstufe; zweite Vorstufe); der Katalog bleibt unverändert.
```

Was die Fassung nicht regelt, mit Absicht: ob das Blatt der
zweiten Einheit die Vorstufe der ersten Kette zeigt – das ist eine
Frage des Zusammenbaus, nicht der Bank.

**Prüfsteine** (je Fall: Erkennungsschritt, Vorstufe, was der
Agent tat, was die Regel neu ergäbe):

1. binomische-formeln – „Was ist a, was ist b?“ (Z. 35, vor E2),
   „Welche Formel?“ (Z. 34, vor E2 und 3) / e2-Vorstufe „Formel
   erkennen und a, b einkreisen“ (Z. 84). Agent: beide entfallen.
   Neu: derselbe Handgriff (Formel wählen und a, b markieren an
   Produkten) → in E2 entfallen; „Welche Formel?“ hätte nach dem
   Bereich in E3 angelegt werden müssen (E3-Vorstufe: Quadrate
   erkennen, anderer Handgriff), passt dort aber nicht auf die
   Vorlage – Katalogfolge Vorschlag 2.1 (Bereich „Vor Einheit 2“),
   danach: entfällt ganz.
2. brueche-dezimalzahlen – „Sind alle Teile gleich groß?“ (Z. 39,
   vor E1) / e1 k1 „gleich große Teile prüfen (Vorstufe)“ (Z. 106).
   Agent: entfällt. Neu: gleich (entfällt).
3. bruchrechnung – „Von heißt mal“ (Z. 40, vor E3) / e3 „„von“
   markieren (Vorstufe)“ (Z. 101). Agent: entfällt. Neu: gleich.
4. rationale-zahlen – die drei früheren Schritte stehen nur noch
   als Vorstufen (Z. 85–87); Z. 34 „Vorzeichen oder Rechenzeichen?“
   und Z. 35 „Zeichen zusammenfassen“ (beide vor E2) haben keine
   Vorstufe desselben Handgriffs (e2-Vorstufe: Pfeil zeichnen).
   Agent: beide angelegt. Neu: gleich.
5. pythagoras – „Ganz oder halb?“ (Z. 38) / e3-Vorstufe
   „Teildreieck nachfahren“. Agent: beide bleiben. Neu: andere
   Entscheidung (Länge wählen gegen Dreieck finden) → beide
   bleiben.
6. lineare-gleichungen – „Umkehroperation benennen“ (Z. 32, vor E1
   und 2) / keine Vorstufe desselben Handgriffs (e1: Tabelle,
   Kandidaten; e2: Umformung anschreiben). Agent: in e1. Neu:
   gleich. prozentrechnung „um oder auf?“ (Z. 41, vor E5) / e5
   „„um oder auf“ (Vorstufe)“ (Z. 102) – Agent: „steht nicht
   doppelt“ (als Vorstufe geführt). Neu: entfällt als
   Erkennungsschritt, die Vorstufe bleibt – gleiches Ergebnis.
   terme: keiner der vier Schritte (Z. 33–36) hat eine Vorstufe
   desselben Handgriffs; alle angelegt, neu gleich.
7. kurvenuntersuchung – „Gegeben oder gesucht?“ (Z. 41, vor E2 und
   3) / e2 k1 „„gegeben oder gesucht“ und „welcher Nachweis“
   ankreuzen (Vorstufe)“, e2 k2 „„gegeben oder gesucht“ ankreuzen
   (Vorstufe)“ (Z. 125, 126); e3-Vorstufe „„welcher Nachweis“ –
   ankreuzen …“ (Z. 127). Agent: entfällt. Neu: in E2 entfällt
   (beide Ketten haben den Handgriff), in E3 fehlt er
   (Wendepunkte: „Bestimmen Sie“ gegen „Zeigen Sie, dass bei …“)
   → angelegt in E3. Dazu e2 k1 gegen k2: k1 fragt zusätzlich nach
   dem Nachweis – andere Entscheidung dazu, beide Vorstufen
   bleiben.
8. abstaende – „Abstand wovon zu was?“ (Z. 38, vor allen
   Einheiten) / e1 „„Abstand wovon zu was?“ ankreuzen (Vorstufe)“
   (Z. 103); „Hin oder zurück?“ (Z. 39, vor E1 und 2) / e2 „„Hin
   oder zurück?“ ankreuzen (Vorstufe)“ (Z. 104). Agent: der erste
   entfällt in e1 (und ist damit weg), der zweite steht in e1. Neu:
   der erste wird in E2 angelegt (E2-Vorstufen sind „Hin oder
   zurück?“ und „Abstand des Ursprungs“, andere Handgriffe); der
   zweite in E1 wie bisher.
9. flaecheninhalt-und-volumen-im-raum (nicht unter den 24) – „Höhe
   oder Kante?“ (Z. 39, vor E1 bis 3) / e1-Vorstufe (Z. 101); „Ein
   Drittel oder nicht?“ (Z. 40, vor E3 und 4) / e3-Vorstufe
   (Z. 103); „Welche Figur, welche Formel?“ (Z. 38, vor allen) /
   e2-Vorstufe (Z. 102). Agent: die ersten beiden entfallen, der
   dritte in e1. Neu: „Höhe oder Kante?“ angelegt in E2
   (E2-Vorstufe ist „Welche Figur, welche Formel?“); „Ein Drittel
   oder nicht?“ angelegt in E4 (E4-Vorstufe „Ganz, Summe oder
   Differenz?“); „Welche Figur, welche Formel?“ in E1 wie bisher.
   Die stand.md nennt „Ganz, Summe oder Differenz?“ als
   Erkennungsschritt; der Katalog führt ihn nur als Vorstufe
   (Z. 38–40 hat drei Schritte).
10. binomialverteilung – „Treffer oder Niete gezählt?“ (Z. 43, vor
    E3 und 5) / e5-Vorstufe (Z. 128); e3-Vorstufe „Genau, höchstens
    oder mindestens?“. Agent: eigene Kette in e3. Neu: gleich
    (E3 hat keine Vorstufe desselben Handgriffs; mit Vorschlag 11.1
    ebenso). Dazu e2 gegen e3 (wortgleiche Vorstufen, Z. 125,
    126): Zeilen einmal bei e2, e3 beginnt mit dem Grundfall – oder
    Vorschlag 11.1.
11. ableitungsregeln – „Welche Regel?“ (Z. 36, vor E1 bis 3) / e1
    „„Welche Regel?“ ankreuzen (Vorstufe, Grundvorstellung)“
    (Z. 96), e3 „„Welche Regel?“ und „Innen und außen?“ ankreuzen
    (Vorstufe)“ (Z. 98), e2 „Innen und außen?“ (Z. 97). Agent:
    „Welche Regel?“ entfällt, „Innen und außen?“ (kein
    Erkennungsschritt mehr im Katalog, nur Vorstufe) entfällt.
    Neu: E1 und E3 haben den Handgriff, E2 nicht (dort nur „Innen
    und außen?“ – für eine Verkettung ist die Regel die Kettenregel,
    die Frage „Welche Regel?“ stellt sich dort nicht) → angelegt in
    E2? Das wäre wörtlich die Folge; der Schritt gehört aber nicht
    vor die Kettenregel-Einheit. Ermessen des Chats: Bereich im
    Katalog auf „Vor Einheit 1 und 3“ ziehen, dann entfällt er
    ganz. „Zahl oder Variable?“ (Z. 37, vor E1 und 3) / keine
    Vorstufe desselben Handgriffs → in E1, wie der Agent.
12. skalarprodukt-und-winkel – „Welche zwei Richtungen bilden den
    Winkel?“ (Z. 38, vor E2 bis 4) / e2-Vorstufe (Z. 95); „Der
    Formelwinkel oder sein Nachbar?“ (Z. 39, vor E2 und 3) / in der
    e3-Vorstufe (Z. 96: „„Kosinus oder Sinus?“ … dazu „Der
    Formelwinkel oder sein Nachbar?“ ankreuzen“). Agent: der erste
    entfällt, der zweite steht in e2. Neu: der erste angelegt in E3
    (E3-Vorstufe „Kosinus oder Sinus?“ mit Formelwinkel – andere
    Entscheidung), der zweite in E2 wie bisher.
13. stammfunktion-und-hauptsatz, flaecheninhalt-durch-integration –
    keine Erkennungsschritte (seit 27.09. gestrichen, Z. 36 bzw.
    40). Nichts.
14. lagebeziehungen – „Wer und wogegen?“ (Z. 38, vor E1 und 3) /
    e2-Vorstufe (Z. 94). Agent: in e1, Befund. Neu: E1-Vorstufe
    „Erfüllt, größer oder kleiner?“ ist ein anderer Handgriff → in
    E1; die Vorstufe in E2 liegt außerhalb des Bereichs –
    Katalogfolge Vorschlag 15.1.
15. geraden – „Gerade oder Strecke?“ (Z. 39, vor E1 und 4) /
    e4-Vorstufe (Z. 107). Agent: in e1. Neu: gleich (E1-Vorstufe
    „Punkt, Richtung, Parameter?“ ist anders).
16. ebenen – „Was legt die Ebene fest?“ (Z. 39, vor E1 und 4) /
    e1-Vorstufe (Z. 114); e4-Vorstufe „Parallel, identisch oder
    schneidend?“ (Z. 118). Agent: entfällt ganz. Neu: angelegt in
    E4. Dazu e2 k1 gegen k2: „Welche Form, welcher Weg?“ wortgleich
    (Z. 115, 116) → Zeilen einmal bei k1, k2 beginnt mit dem
    Grundfall.
17. zufallsexperimente-und-pfadregeln – „Anteil aller oder Anteil
    unter …?“ (Z. 54, vor E6 und 8) / e6-Vorstufe (Z. 160);
    e8-Vorstufe „Vorwärts oder rückwärts?“ (Z. 162). Agent:
    entfällt. Neu: angelegt in E8.
18. vektoren-und-rechenoperationen – „Faktor gesucht oder Richtung
    gesucht?“ (Z. 35, vor E1 und 2) / e1- und e3-Vorstufe „Zahl
    oder Pfeil?“ (Z. 81, 83). Agent: beide bleiben („nah
    beieinander“). Neu: andere Entscheidung (was fehlt gegen was
    gemeint ist) → beide bleiben, in E1 angelegt; dass ein Schüler
    zweimal Zahl gegen Richtung ankreuzt, bleibt ein Katalogbefund
    ohne Vorschlag (die Fragen sind verschieden, der Chat kann eine
    streichen).
19. ableitung-und-aenderungsrate – „Mittel oder Moment?“ (Z. 39,
    vor E1 und 2) / e1- und e3-Vorstufe (Z. 110, 112); e2-Vorstufe
    „Wie hoch, wie steil?“. Agent: entfällt. Neu mit altem Bereich:
    angelegt in E2 (falsch, siehe Abschnitt 16); mit Vorschlag
    16.1 (Bereich E1 und 3): entfällt ganz.
20. tangente-normale-schnittwinkel – keine Erkennungsschritte
    betroffen; e1- und e4-Vorstufe wortgleich (Z. 117, 120): Zeilen
    einmal bei e1, e4 beginnt bei „Welcher Winkel?“ – oder
    Vorschlag 14.1.
21. pythagoras, prozentrechnung, terme, lineare-gleichungen,
    geraden, stammfunktion, flaecheninhalt-durch-integration: die
    Agenten fanden keinen Doppel; die neue Fassung ändert dort
    nichts.

Änderungen gegenüber dem Vorgehen der Agenten: fünf Schritte
würden neu angelegt (kurvenuntersuchung E3, abstaende E2,
skalarprodukt E3, ebenen E4, zufallsexperimente E8; dazu
flaecheninhalt-und-volumen E2 und E4 außerhalb der 24), einer
hängt an einer Katalogkorrektur (ableitungsregeln), zwei
Vorstufen-Doppel bekommen eine Regel (ebenen e2, kurvenuntersuchung
e2 bleibt). Das ist ein Bank-Auftrag von etwa sieben mal vier
Zeilen, wenn der Chat die Fassung annimmt.
