# Vorschlag Einbindung – 2026-09-28

Einbindungslauf K1/K2 aus uebergabe.md § 5 (Chat verbessereBlaetter,
28.09. abends). Fünf Quellen der letzten Tage gegen die Dateien
gehalten, in denen sie wirken müssten; je Fund Ort, Wortlaut der
Quelle (Zeile), Befund, Vorschlag. Konkordanzen (katalog/_fremd-*)
nicht dabei – zweiter Lauf nach dem Katalog-Nachzug. Urteil im Chat,
Umsetzung danach durch Claude Code (Katalog, bank.md, regeln.md,
layout-befunde.md) und im Chat (ziel.md, Prompts).

Lauf: fünf Leser (Opus) parallel, je Quelle einer; zusammen
1 011 734 Token, 109 Werkzeugaufrufe, 8 Minuten. Zählungen in den
Berichten stammen aus den Klonen vom 28.09. 18:44 (808fd7c).

## Zielkategorien (Schnitt nach Zieldatei)

- K1 Stoff und Folge → katalog/ (Sprosse, Vorstufe, Reihenfolge,
  Kontrolle)
- K2 Aufgabenformen → aufgabenbank bank.md, auftrag-eintrag.md, Bank
- K3 Sprache → aufgabenbank bau/sprachlauf/regeln.md
- K4 Seite → aufgabenbank bau/layout-befunde.md, zusammenbau
- K5 Blatt und Bestellung → ziel.md, blattbau (unterrichtsblatt.md,
  pruefungsblatt.md)

Zählung: K1 39 Funde (Sek I 14, Sek II 23, Pflichtformen 2), K2 12,
K3 8, K4 5, K5 20 (Blattarten 12, Situationen 8), dazu die
Pflichtelemente P1–P10 (8 aufnehmen, 2 nicht).

## Überschneidungen und Widersprüche (vom Chat)

1. Kontrolle als Schluss steht dreimal: als Lösungszeile (Teil A
   quer), als Sprosse (Teil C lagebeziehungen, binomialverteilung,
   Teil A bruchrechnung) und als „nicht als Pflichtelement“ (Teil B
   P10). Das passt zusammen: Kontrolle ist Sprosse und Lösungszeile,
   kein viertes Pflichtelement.
2. Fehler finden: Teil B P1/P2 (Serie, fehlerfreie Vorlage) und
   Teil A brueche-dezimalzahlen („vier Rechnungen beurteilen“)
   meinen dieselbe Form; bei der Umsetzung einmal in bank.md.
3. Päckchen mit einem festen Wert (Teil A quer) und die Anweisung
   über dem Päckchen (Teil A K3 Nr. 11) gehören zusammen und setzen
   die Sprossenzeile der Bank voraus; das ist die größte Änderung an
   bank.md.
4. Teil D Befund 4 („Ein Blatt trägt einen Teil, 1–3 Fertigkeiten“)
   und Teil E Befund 5 („zu Hause allein weiter“) ändern beide § 1
   von ziel.md; Befund 5 steht gegen das Erfolgskriterium „nicht
   allein“. Entscheidung des Lehrers.
5. Teil D „Nicht eingebunden“: MAKOS-Reihenfolge „zuerst Grund- und
   Umkehraufgabe“ widerspricht ziel.md § 1 („oben … Umkehrung“).
   Kein Vorschlag, aber offen.
6. Teil E Befund 1: pruefungsblatt.md 1.1 macht aus „klassenarbeit“
   eine Probeprüfung, ziel.md § 3 sagt „kein eigenes Format“. Das ist
   ein Widerspruch im Bestand, unabhängig von der Literatur.
7. Beide Prompts: pruefungsblatt.md v0.15 führt noch die Heftsorte
   „Vorbereitung“ und „Nie geschnitten“ (Teil D, E) – beim nächsten
   Umbau fällig.

---

## Teil A – Altlehrwerke Sek I (quellen/altlehrwerke-formen.md)

### quer
- K2 · Ort: aufgabenbank bank.md, „Regeln für den Inhalt“, erster Punkt (Z. 157–160) · Quelle: altlehrwerke-formen.md Z. 643–648, 267–270 · Befund: bank.md lässt die Varianten einer Sprosse in Zahlen und Kontext frei wandern. Deshalb ändern sich im Grundfall zwei Werte zugleich (prozentrechnung e3: 80 €/50 %, 60 kg/25 %, 300 m/10 %). Die Quelle führt dagegen durchgehend Päckchen mit einem festen Wert (ein G, vier p); unterrichtsblatt.md Z. 868–869 verlangt dasselbe.
  Vorschlag: „- Die fünf Grundfall-Zeilen einer Kette sind ein Päckchen: ein Wert bleibt in allen fünf gleich (dasselbe Ganze, derselbe Nenner, derselbe Teiler), genau ein Wert wandert, der Kontext bleibt. Ab der zweiten Sprosse unterscheiden sich Varianten in Zahlen und Kontext, nicht im Merkmal.“
- K3 · Ort: aufgabenbank bau/sprachlauf/regeln.md, „Regeln“, neue Nr. 11 · Quelle: Z. 643–648, 146–148, 309–315 · Befund: Die Regeln kennen nur den Satz der einzelnen Aufgabe. Eine Anweisung über dem Päckchen, die das neue Merkmal nennt, fehlt; die Reihe um 1960 schreibt sie vor jede Nummer.
  Vorschlag: „11. Gilt eine Aufforderung für ein ganzes Päckchen, steht sie einmal darüber und sagt in einem Satz, was an diesen Aufgaben neu ist: „Bei diesen Aufgaben kürzt du vor dem Malnehmen.“, „Hier steht x hinter dem Minus.“ Der Satz kommt aus dem Feld merkmal der Sprosse, in Schülerworten.“
- K2 · Ort: aufgabenbank bank.md, „Felder je Aufgabe“, Feld loesung (Z. 66–72) · Quelle: Z. 660–662, 547–551, 117–119, 473 · Befund: Eine Kontrolle steht in der Bank uneinheitlich oder gar nicht. In lineare-gleichungen e2 steht die Probe in einer Zeile („Probe: 3 · 7 + 5 = 26 (wA)“), ohne linke und rechte Seite. bruchrechnung e3 hat 0 Kontrollzeilen, prozentrechnung e2 hat 0 Überschläge.
  Vorschlag: „Verlangt die Sprosse Probe, Kontrolle oder Überschlag, trägt loesung sie als eigene, beschriftete Zeile: Gleichung „Probe: linke Seite … = …, rechte Seite …, beide gleich“; Teilen „Kontrolle: Ergebnis mal Teiler = …“; Ausklammern „Probe: ausmultipliziert …“; Prozentsatz „Überschlag: … ≈ …“ vor der Rechnung.“
- K3 · Ort: aufgabenbank bau/sprachlauf/regeln.md, „Regeln“, neue Nr. 12 · Quelle: Z. 654–659, 433–441, 466–469 · Befund: Die Regeln gelten nur für das Feld aufgabe. Wie eine Musterlösung ihre Schritte benennt, regeln sie nicht; beide Reihen beschriften jede Zeile mit dem Schritt.
  Vorschlag: „12. Die Lösung (Feld loesung) und das Beispiel im Merkkasten tragen je Rechenzeile den Schritt in Schülerworten: „Klammer auflösen“, „ordnen“, „zusammenfassen“, „x allein stellen“, „Überschlag“, „Probe“. Dieselben Wörter wie in den Anweisungen der Kette.“
- K4 · Ort: aufgabenbank bau/layout-befunde.md, neue Nr. 55 · Quelle: Z. 433–439, 466–467, 543–546 · Befund: Die Sammlung regelt, wie Aufgaben angeordnet werden, aber nicht, wie eine vorgerechnete Lösung angeordnet wird. Die Quelle setzt jedes „=“ untereinander und den Schrittnamen an den Rand.
  Vorschlag: „55. Vorgerechnetes Beispiel und Lösungsblatt: je Umformung eine Zeile, Gleichheitszeichen untereinander, der Schrittname klein links vor der Zeile (nicht rechts daneben, vgl. 38), das Ergebnis zuletzt und abgesetzt.“

### lineare-gleichungen
Sprossen im Katalog: 33 in 5 Ketten. Die Quelle schlägt 5 Punkte vor, davon sind 2 eingebunden (die Probe steht unter quer).
- K1 · Ort: katalog/lineare-gleichungen.md Z. 77 (Kette Umformen) · Quelle: Z. 538–540, 555–557 · Befund: Die Kette hat die negative Vorzahl (−4x = 20), aber nicht x als Subtrahend (a − x = b). Auch bank e2 hat keine Zeile dieser Form.
  Vorschlag: „… → negative Lösung → x steht hinter dem Minus (20 − x = 13) → negative Vorzahl → …“
- K1 · Ort: katalog/lineare-gleichungen.md, Erkennungsschritte (Z. 31–34), neue Zeile · Quelle: Z. 514–525 · Befund: Vor Einheit 3 wird nur „Auf welcher Seite steht weniger x?“ geübt. Die übrigen Entscheidungen (Klammer, zusammenfassen, x allein) werden nicht benannt, bevor gerechnet wird.
  Vorschlag: „- „Was ist als Nächstes dran?“ – zu einer Gleichung ankreuzen: Klammer auflösen, zusammenfassen, x auf eine Seite bringen, x allein stellen; nichts rechnen. Vor Einheit 3.“

### binomische-formeln
Sprossen im Katalog: 35 in 3 Ketten. Die Quelle schlägt 4 Punkte vor, davon sind 2 eingebunden.
- K1 · Ort: katalog/binomische-formeln.md Z. 85 (Kette Faktorisieren) · Quelle: Z. 583–586, 602–605 · Befund: „Kein Binom erkennen“ steht erst nach dem Ausklammern, also nach allen Rückwärts-Sprossen. Die Quelle sondert zuerst aus, was sicher kein Quadrat ist, und prüft erst dann das Mittelglied; das ist eine vertauschte Reihenfolge.
  Vorschlag: „… → dritte Formel rückwärts, x² minus Quadratzahl (4×) → sicher kein Quadrat aussondern: aus einer Liste die Terme streichen, bei denen ein Mittelglied fehlt, zwei Quadrate addiert sind oder ein Glied kein Quadrat ist; nichts faktorisieren → Mittelglied prüfen: … → …“ (die spätere Sprosse heißt dann nur noch „kein Binom begründen“)
- K1 · Ort: katalog/binomische-formeln.md Z. 85 · Quelle: Z. 627–629, 634–637 · Befund: Die Kette bildet das doppelte Produkt, schreibt den Term aber nie in Formelgestalt hin, bevor die Klammer entsteht.
  Vorschlag: „… → Mittelglied prüfen: … → Term in Formelgestalt schreiben: 4x² + 12x + 9 als (2x)² + 2 · 2x · 3 + 3², noch nicht zusammenfassen → erste Formel rückwärts mit geprüftem Mittelglied → …“

### brueche-dezimalzahlen
Sprossen im Katalog: 51 in 6 Ketten. Die Quelle schlägt 6 Punkte vor, davon sind 3 eingebunden.
- K1 · Ort: katalog/brueche-dezimalzahlen.md Z. 111 (Kette Vergleichen und Ordnen) · Quelle: Z. 199–201, 214–217 · Befund: Die Vorstufe „Nullen anhängen“ gehört zum Fall mit verschieden vielen Stellen, steht aber vor dem Grundfall mit gleich vielen Stellen. Für diesen Grundfall fehlt eine Vorstufe.
  Vorschlag: „Vergleichen und Ordnen (Einheit 5): „Wo entscheidet es sich?“ – zu zwei Dezimalzahlen nur die Stelle nennen, an der sie sich zuerst unterscheiden; kein Zeichen setzen (Vorstufe) → zwei Dezimalzahlen mit gleich vielen Stellen (4×) → Nullen anhängen, ohne zu vergleichen → verschieden viele Stellen → …“
- K1 · Ort: katalog/brueche-dezimalzahlen.md Z. 110 (Kette Umwandeln) · Quelle: Z. 232–233, 242, 248–251 · Befund: Die Stellenwerttafel steht unter den Typen (Z. 26), aber nicht in der Kette. Keine Sprosse lässt eine Dezimalzahl aus einzeln genannten Stellen bauen, auch nicht mit einer Null-Stelle.
  Vorschlag: „… → Zehnerbruch ↔ Dezimalzahl (4×) → Stellen einzeln gegeben → Dezimalzahl (3 Einer, 0 Zehntel, 8 Hundertstel) → mit Nullen (Hundertstel, Tausendstel) → …“
- K2 · Ort: aufgabenbank bank.md, „Regeln für den Inhalt“, Punkt Fehler-finden-Aufgaben (Z. 181–183) · Quelle: Z. 195–196, 219 · Befund: In der Bank ist jede Fehler-finden-Aufgabe eine einzige falsche Rechnung. Die Form „vier Rechnungen beurteilen“ fehlt: Dort muss der Schüler auch die richtigen Rechnungen als richtig erkennen.
  Vorschlag: „Von den drei Fehler-finden-Zeilen einer Einheit darf eine vier Rechnungen untereinander zeigen, genau eine davon mit dem Muster aus „Typische Fehler“; gefragt ist, welche falsch ist und wie sie richtig heißt.“

### prozentrechnung
Sprossen im Katalog: 39 in 5 Ketten. Die Quelle schlägt 5 Punkte vor, davon sind 3 eingebunden (das Päckchen mit festem G steht unter quer).
- K1 · Ort: katalog/prozentrechnung.md Z. 99 (Kette Prozentsatz) · Quelle: Z. 312–323, 328–332 · Befund: Die Kette überschlägt nur am Streifen, nicht mit Zahlen. Vor dem Taschenrechner fehlt ein Überschlag, gegen den das Ergebnis geprüft wird; bank e2 hat 0 Zeilen mit Überschlag.
  Vorschlag: „… → Teil von 50, 25, 20, 10 → Überschlag über einen einfachen Bruch: Teil und Ganzes so runden, dass ein Halb, Viertel, Fünftel, Zehntel oder Zwanzigstel entsteht, und den Prozentsatz ungefähr angeben; nicht genau rechnen → Teil : Ganzes als Dezimalzahl mit Taschenrechner, mit dem Überschlag verglichen → …“
- K1 · Ort: katalog/prozentrechnung.md Z. 101 (Kette Grundwert) · Quelle: Z. 276–277, 294–296 · Befund: Keine Sprosse hält den Teil fest und lässt den Prozentsatz wandern. Gerade daran sieht man, dass das Ganze bei doppeltem Satz halb so groß ist; das ist die Gegenprobe zum Fehler „Grundwert und Prozentwert vertauscht“ (Z. 81).
  Vorschlag: „… → Ein-Prozent-Weg → derselbe Teil, verschiedene Sätze: 60 € sind 10 %, 20 %, 30 % – wie groß ist jeweils das Ganze? → beliebiger Satz mit Taschenrechner → …“
- K1 · Ort: katalog/prozentrechnung.md Z. 100 (Kette Prozentwert) · Quelle: Z. 272–273, 296 · Befund: Der Ein-Prozent-Weg beginnt gleich mit Zahlen. Eine Vorstufe, die 1 % einer Einheitsgröße in der kleineren Einheit zeigt, fehlt.
  Vorschlag: „… → Zehn-Prozent-Schritte … → 1 % einer Einheit: 1 % von 1 m, 1 kg, 1 l in der kleineren Einheit angeben → Ein-Prozent-Weg mit glatten Zahlen → …“

### terme
Sprossen im Katalog: 42 in 5 Ketten. Die Quelle schlägt 5 Punkte vor, davon sind 2 eingebunden.
- K1 · Ort: katalog/terme.md Z. 76 (Kette Ausklammern) · Quelle: Z. 426–427, 446–447 · Befund: Die Kette hat keine Vorstufe (bank e4: 0 Vorstufenzeilen). Sie verlangt vom ersten Posten an, den Faktor selbst zu finden.
  Vorschlag: „Ausklammern (Einheit 4): Faktor ist vorgegeben, nur die Klammer füllen: 6x + 15 = 3 · (__ + __) (Vorstufe) → gemeinsamen Zahlfaktor bei zwei Gliedern (4×) → …“
- K1 · Ort: katalog/terme.md Z. 74 (Kette Klammern) · Quelle: Z. 470–472, 478–481 · Befund: Die Minusklammer kommt als Regel mit Variablen, ohne Zahlenfall. In der Quelle kommt zuerst derselbe Zahlterm auf zwei Wegen, und erst dieser Vergleich begründet die Zeichenregel.
  Vorschlag: „… → Zahl · Klammer (4×, …) → Minusklammer mit Zahlen auf zwei Wegen: 20 − (7 + 3) erst mit der Klammer, dann Glied für Glied 20 − 7 − 3; beide Ergebnisse vergleichen → Minusklammer zwei Glieder → …“

### rationale-zahlen
Sprossen im Katalog: 31 in 4 Ketten. Die Quelle schlägt 4 Punkte vor, davon sind 3 eingebunden.
- K1 · Ort: katalog/rationale-zahlen.md Z. 85 (Kette Addieren/Subtrahieren) · Quelle: Z. 350–351, 369–371 · Befund: Die Kette trennt nie das Vorzeichen des Ergebnisses vom Betrag. Den Fehler −2 − 3 = −1 (Z. 69) trifft genau diese Lücke.
  Vorschlag: „… → positive Zahl dazu oder weg, Start negativ (4×) → nur das Vorzeichen: ist die Summe größer oder kleiner als null? ankreuzen und mit den Beträgen begründen, nicht ausrechnen → negative Zahl addieren mit Klammer → …“
- K2 · Ort: aufgabenbank bank/rationale-zahlen, e2 (Sprosse „Zeichen zusammenfassen gemischt (4×)“) und e3 (Grundfall „plus mal minus“), Feld antwort · Quelle: Z. 359–363 · Befund: Die Bank gibt nur das Ergebnis vor. Das Gerüst aus Vorzeichen, Betrag und Ergebnis, das den Zweischritt auf dem Blatt erzwingt, fehlt.
  Vorschlag: „antwort": "Vorzeichen: __ \\ Betrag: __ \\ Ergebnis: __"
- K2 · Ort: aufgabenbank bank/rationale-zahlen/e3.jsonl, Sprosse „drei Faktoren“, Feld loesung · Quelle: Z. 391–395, 401–402 · Befund: Die Lösung nennt nur die Endzahl („$30$“). Ohne Teilprodukt findet der Schüler nicht, wo sein Vorzeichen kippt.
  Vorschlag: „loesung": "$(-2) \\cdot 3 \\cdot (-5) = (-6) \\cdot (-5) = 30$"

### bruchrechnung
Sprossen im Katalog: 40 in 6 Ketten. Die Quelle schlägt 4 Punkte vor, davon sind 2 eingebunden.
- K1 · Ort: katalog/bruchrechnung.md Z. 100 (Kette Dividieren) · Quelle: Z. 109, 117–119, 125–127 · Befund: Die Kette hat keine Kontrolle. Der Fehler „Zähler geteilt statt Nenner mal“ (Z. 85) bleibt so unbemerkt; bank e3 hat 0 Kontrollzeilen.
  Vorschlag: „Dividieren (Einheit 3): Bruch geteilt durch Zahl (4×) → Kontrolle: Ergebnis mal Teiler gibt wieder die Ausgangszahl (3/20 · 4 = 3/5) → Zahl geteilt durch Stammbruch … → …“
- K1 · Ort: katalog/bruchrechnung.md Z. 97 (Kette Addieren/Subtrahieren) · Quelle: Z. 154–160, 168–171 · Befund: Von „ein Nenner Vielfaches des anderen“ springt die Kette direkt zu „beide erweitern“. Eine Sprosse, die nur den Hauptnenner und beide Erweiterungszahlen verlangt, fehlt. Der Erkennungsschritt Z. 39 deckt nur einen Bruch ab.
  Vorschlag: „… → ein Nenner Vielfaches des anderen (4×) → Hauptnenner und beide Erweiterungszahlen anschreiben: zu zwei Nennern nur den Hauptnenner und die beiden Faktoren angeben, nichts addieren → beide erweitern (Hauptnenner) → …“

K1: geprüft, 14 Funde · K2: 5 · K3: 2 · K4: 1

### Nicht eingebunden, mit Grund (Teil A)
- Dichte (Z. 663–666): nach Beschluss verworfen. Der Anteil von einem Drittel für Begründen und Urteilen ist durch die Pflichtelemente schon gedeckt.
- bruchrechnung, Mischfall Bruch plus Dezimalbruch (Z. 125–130): verlangt kein Original, liegt außerhalb des Mindeststoffs und ändert das Blatt nicht.
- bruchrechnung, Teilung in Kopfrechnen und schriftlich (Z. 171–173): Aufwandsmerkmal, kein Strukturmerkmal (unterrichtsblatt.md Z. 701–702).
- brueche-dezimalzahlen, Kreuztabelle Brüche × Erweiterungszahlen (Z. 186–188): Dichteform. Dass ein Merkmal wandert, leistet der Päckchen-Vorschlag (quer).
- brueche-dezimalzahlen, Antwortsatz „Wegen … gilt …“ (Z. 207–209): Die Bank begründet in e5 schon über die entscheidende Stelle.
- brueche-dezimalzahlen, Dreischritt Größe = Zehnerbruch = Dezimalzahl (Z. 243, 252–253): gehört zu einheiten.md; lag außerhalb der Prüfung.
- prozentrechnung, Prozentsatz über 100 als eigenes Päckchen (Z. 311, 333): Einheit 3 hat ihn schon; in Einheit 2 wäre er Vorrat ohne Original.
- prozentrechnung, „18 % sind 70 M – wie viel sind 9 %, 36 %?“ (Z. 275–276): Dreisatz aus bekanntem Paar, steht in der Grundvorstellung (Katalog Z. 96).
- rationale-zahlen, Klammerform (+a) + (−b) als Sprosse (Z. 399–401): Erkennungsschritte decken sie ab.
- terme, Koeffizienten und Glieder nennen (Z. 444–446): liegt als Erkennungsschritte vor.
- terme, Unterklammern gleichartiger Glieder (Z. 467, 481–482): vorhanden.
- terme, Lückenterm mit Kästchen (Z. 422–424, 448): bräuchte eigenen Katalogtyp; „Faktor vorgegeben“ leistet dasselbe.
- lineare-gleichungen, Tabelle „Struktur | Umformung“ als Merkkasten (Z. 514–519): Kastenform beschlossen (layout-befunde Nr. 54).
- lineare-gleichungen, Langform ohne Strich (Z. 507–513, 559–561): bestätigt die Vorstufe „Umformung nur anschreiben“.
- lineare-gleichungen, x rechts isolieren (3 = x): wirkt auf kein Blatt.
- binomische-formeln, Formel darüberschreiben, a, b mit Pfeilen (Z. 588–592, 600–602): Zutatenzeile (Nr. 44) und Erkennungsschritt decken es.
- binomische-formeln, Folge Vorzahlen → Brüche → Dezimalzahlen (Z. 616–618, 637–639): Aufwandsmerkmale, Vorrat.
- quer, Beispiel vor der Regel (Z. 166–167, 247, 553–554): gilt schon (Merkkasten am Ende des Zweigs).

---

## Teil B – Pflichtformen (quellen/altlehrwerke-pflichtformen.md)

Gezählt in 14 618 Bankzeilen (346 Dateien e*.jsonl und zone.jsonl). Pflichtzeilen: fehler 885, begruenden 807, anwendung 567, darstellung 375.

### Pflichtelemente 1–10
- P1 Serie „können nicht stimmen“ · in der Bank: 0 („Welche … nicht stimmen/falsch“), 0 fehler mit form ankreuzen · Empfehlung: aufnehmen. Die Bank prüft Fehler nur an einer einzelnen fremden Rechnung, nie am Überschlag über mehrere Ergebnisse.
  Vorschlag: „fehler: Trägt die Kette ein Kennzeichen (Endziffer, Kommastelle, Vorzeichen, Überschlag), ist eine der drei eine Serie mit 3–4 fertigen Ergebnissen: ‚Welche Ergebnisse können nicht stimmen? Begründe, ohne genau zu rechnen.‘; loesung je falschem Ergebnis das Kennzeichen in einem Halbsatz; pruef "".“
- P2 fehlerfreie Vorlage · in der Bank: 0 („richtig gerechnet“); 0 fehlerfreie Vorlagen unter 885 fehler-Zeilen; 860 von 885 fragen „Finde den Fehler“ · Empfehlung: aufnehmen. Heute lernt der Schüler, dass immer ein Fehler da ist.
  Vorschlag: „fehler: Je Einheit ist eine der drei Vorlagen fehlerfrei (‚Prüfe, ob <Name> richtig gerechnet hat.‘); loesung ‚Richtig.‘ und die Regel des entscheidenden Schritts in einem Satz.“
- P3 Prüfzahl vor der Fehlersuche · in der Bank: 7 von 885 fehler-Zeilen mit „Setze/Probe/einsetzen“ in der aufgabe, 29 mit einer Regel in der loesung · Empfehlung: aufnehmen, nur für Umformungsketten.
  Vorschlag: „fehler bei Gleichungen und Ungleichungen: eine der drei nennt eine Prüfzahl (‚Setze 0 ein. In welcher Zeile stimmt es nicht mehr?‘); loesung in zwei Sätzen: der Fehler mit der verletzten Regel, dann die richtige Zeile.“
- P4 Aussagenserie wahr/falsch · in der Bank: 0 begruenden-Zeilen mit „wahr“; „wahr oder falsch“ 10 insgesamt (nur Prüfungshöhe; Vorbild P10 2021 OS) · Empfehlung: aufnehmen. Urteilen ist in den Büchern die häufigste Art (55 von 163 Nummern).
  Vorschlag: „begruenden: eine der drei ist eine Aussagenserie mit 3 Aussagen, mindestens eine wahr und eine falsch, mit Alltagsquantoren (immer, jede, nie, es gibt); ‚Entscheide bei jeder Aussage, ob sie wahr oder falsch ist. Begründe.‘; form text; loesung je Aussage ‚wahr, denn …‘ bzw. ‚falsch, z. B. …‘ mit Gegenbeispiel; pruef "".“
- P5 „Begründe, dass …“ mit Regelname · in der Bank: 9 „Begründe, dass“ und 454 „Begründe/Erkläre, warum“; 39 von 807 Lösungen nennen Regel, Satz oder Gesetz · Empfehlung: aufnehmen, nur den Regelnamen.
  Vorschlag (bank.md, Feld loesung): „Begründen: Kern in einem Satz, der die Regel beim Namen nennt (‚gleiche Stufenwinkel‘, ‚Division durch eine negative Zahl dreht das Zeichen um‘)“
- P6 Personenaussage „hat sie recht?“ · in der Bank: 42 begruenden mit „sagt:/behauptet/meint“, in 21 von 72 Einträgen · Empfehlung: aufnehmen. Die Satzform steht in regeln.md Nr. 6, als Pflicht fehlt sie in 51 Einträgen.
  Vorschlag: „begruenden: eine der drei ist eine Personenaussage zum häufigsten Fallstrick der Zone (‚<Name> sagt: „…“ Begründe, ob <Name> recht hat.‘); ‚Das kann man nicht entscheiden, weil …‘ ist eine zugelassene loesung.“
- P7 darstellung, Richtung im Operator · in der Bank: 375 Zeilen in 125 Einheiten; 17 „Beschreibe“, 1 „ohne … zu zeichnen“ · Empfehlung: aufnehmen. unterrichtsblatt 2.3 c verlangt beide Richtungen, bank.md sagt es nicht.
  Vorschlag: „darstellung: der Operator nennt die Zieldarstellung (‚Schreibe als Gleichung.‘, ‚Beschreibe den Graphen in Worten, ohne ihn zu zeichnen.‘); die drei Aufgaben je Einheit decken mindestens zwei Richtungen, davon eine rückwärts.“
- P8 anwendung als Entscheidungsfrage · in der Bank: 83 von 567 anwendung-Zeilen, in 65 von 189 Einheiten · Empfehlung: aufnehmen.
  Vorschlag: „anwendung: eine der drei endet mit einer Entscheidung an einem Grenzwert (‚Reicht das Geld?‘, ‚Darf der Wagen über die Brücke?‘); loesung: Urteil zuerst, dann die Rechnung.“
- P9 Aufgaben selbst bilden · in der Bank: 61 „Gib ein … an, das …“, 6 „Zahlenrätsel“, 7 „Denke dir/Erfinde“ · Empfehlung: nicht aufnehmen. Der Katalog trägt die Form als Sprosse (lineare-gleichungen Z. 77). Einen unerfüllbaren Teil löst ein schwacher Schüler ohne Lehrer nicht.
- P10 Prüfen ohne Pflichtelement · in der Bank: 22 von 2 451 Grundfall-Lösungen mit „Probe/Kontrolle“, 39 Grundfall-Aufgaben mit „Probe/Kontrolle/Prüfe“ · Empfehlung: nicht aufnehmen, wie die Quelle vorschlägt. Kandidatenform und Probe stehen im Katalog als Sprosse.

### Weitere Funde (Teil B)
- K2 · Ort: bank.md, „Mengen je Kette“ · Quelle: Z. 400–409 · Befund: „fehler 3, begruenden 3“ sagt nicht, welche Formen die drei tragen, deshalb entsteht dreimal dieselbe Form (860/885 „Finde den Fehler“).
  Vorschlag: „Die drei fehler-Zeilen einer Einheit tragen verschiedene Formen: Schülerrechnung mit Fehler, fehlerfreie Vorlage, Serie oder Prüfzahl. Die drei begruenden-Zeilen: Begründe, warum …; Aussagenserie; Personenaussage.“
- K2 · Ort: bank.md, „Regeln für den Inhalt“ · Quelle: Z. 116–118 · Befund: Von 101 Fragen „Hat … recht?“ endet die loesung 17-mal mit ja und 41-mal mit nein (43 ohne Urteil am Anfang); Prompt 2.4 b will etwa halbe-halbe.
  Vorschlag: „Urteilsfragen (recht, wahr, stimmt, reicht) einer Einheit haben etwa gleich viele Ja- und Nein-Lösungen.“
- K2 · Ort: bank.md, Feld loesung · Quelle: Z. 65–68, 259–261 · Befund: In den Büchern steht das Urteil als erstes Wort. In der Bank beginnen 43 von 101 recht-Lösungen mit einer Rechnung.
  Vorschlag: „Urteilen (recht, wahr, möglich, reicht): Urteil als erstes Wort (‚Ja;‘, ‚Nein;‘, ‚falsch;‘), dann der Grund als Halbsatz oder Rechnung.“
- K2 · Ort: bank.md, „Regeln für den Inhalt“ · Quelle: Z. 262–264 · Befund: „ohne zu rechnen“ steht in 43 von 807 begruenden-Zeilen; unterrichtsblatt 2.3 c fordert es, bank.md nicht.
  Vorschlag: „begruenden: mindestens eine der drei lässt sich ohne Rechnung entscheiden und sagt es (‚Begründe, ohne genau zu rechnen.‘).“
- K3 · Ort: bau/sprachlauf/regeln.md, Regel 6 · Quelle: Z. 116–118, 403 · Befund: „Finde den Fehler und rechne richtig“ unterstellt einen Fehler; die fehlerfreie Vorlage (P2) braucht eine eigene Form.
  Vorschlag: „- Prüfen einer fremden Rechnung: „<Name> soll … Er rechnet so: <Rechnung> Prüfe, ob <Name> richtig gerechnet hat. Wenn nicht, rechne richtig.““
- K3 · Ort: regeln.md, Regel 6 · Quelle: Z. 243–247 · Befund: Für die Aussagenserie (P4) fehlt eine Satzform.
  Vorschlag: „- Aussagen beurteilen: „Entscheide bei jeder Aussage, ob sie wahr oder falsch ist. Begründe.“ Darunter die Aussagen als a), b), c).“
- K3 · Ort: regeln.md, Regel 6 · Quelle: Z. 104–107 · Befund: Für die Serie (P1) fehlt eine Satzform; „ohne auszurechnen“ ist für schwache Schüler unklar.
  Vorschlag: „- Ergebnisse prüfen: „<Lage>. Welche Ergebnisse können nicht stimmen? Begründe, ohne genau zu rechnen.““
- K3 · Ort: regeln.md, Regel 7 · Quelle: Z. 246–247 · Befund: Die Bücher nehmen „stets, niemals, gewiss“; keine Alltagswörter, tragen aber die Falle.
  Vorschlag: „Quantoren in Alltagswörtern: immer, jede, nie, es gibt, sicher – nicht stets, sämtliche, niemals, gewiss.“
- K1 · Ort: katalog/prozentrechnung.md, Sprossenkette (Überschlag) · Quelle: Z. 97, 281 · Befund: Der Kopf nennt Überschlag (RLP F), eine Sprosse „Überschlag beurteilen“ fehlt; 9 Überschlagszeilen in der Bank, alle in bruchrechnung e2. (Deckt sich mit Teil A prozentrechnung.)
  Vorschlag: „Sprosse nach dem Grundfall: Überschläge beurteilen – ‚48 % von 610 € sind etwa 600 €‘ → falsch, etwa 300 €; Urteil plus berichtigter Überschlag.“
- K1 · Ort: katalog/pythagoras.md, Kette Umkehrung (und winkel-dreiecke.md Z. 125) · Quelle: Z. 212, 216, 234, 236, 252 · Befund: Die Bank wendet die Umkehrung an (3 Zeilen), lässt sie aber nie bilden und prüfen.
  Vorschlag: „Vorstufe der Kette Umkehrung: Satz und Umkehrung unterscheiden – den Wenn-dann-Satz umdrehen und entscheiden, ob er wahr ist (Beispiel mit falscher Umkehrung: Quadrat/vier rechte Winkel).“
- K4 · Ort: layout-befunde.md, „Auswahl im Heft“ · Quelle: Z. 73–76 · Befund: In den Büchern rund drei Denkaufgaben je Seite, verteilt ans Ende jedes Blocks. Beim kleinen Zuschnitt fehlt die Regel, dass jeder Teil eine hat.
  Vorschlag: „Jeder Teil endet mit mindestens einer Aufgabe aus fehler oder begruenden zu seinen Fertigkeiten, nicht gesammelt am Blattende.“
- K4 · Ort: layout-befunde.md, „Aufgabenform“ (zu Nr. 9 und 38) · Quelle: Z. 243, 259–261 · Befund: Die Aussagenserie braucht je Aussage eine Antwortstelle; Ankreuzen und Begründen nicht in einer Nummer (unterrichtsblatt 2.3 c).
  Vorschlag: „Aussagenserie: je Aussage eine Teilaufgabe a), b), c) mit einer Schreibzeile, kein Kästchen; das Urteil schreibt der Schüler als erstes Wort.“

K1: 2 · K2: 4 · K3: 4 · K4: 2

### Nicht eingebunden, mit Grund (Teil B)
- Fehler finden und Prüfen als ●-Auftrag vor der Regel (Z. 55–61): widerspricht der Reihenfolge in unterrichtsblatt 2.3 d. Nur als Exemplar in einem Testlauf prüfen.
- Darstellungskette in einer Nummer (Z. 351–356): widerspricht „eine Hauptnummer, eine Fertigkeit“.
- Unerfüllbarer Teil bei „selbst bilden“ (Z. 247–249, 391–394): überfordert schwache Schüler ohne Lehrer.
- Personen mit Vornamen, Kennzeichnung nur am Operator, sinnvoll runden, Kandidatenform: vorhanden.
- Zweiteilige Probe bei Ungleichungen (Z. 303): nur Lösungsdatei weniger Einheiten.
- Siezen in Klasse 9 (Z. 81–82): Die Bank duzt durchgehend.
- Teilbarkeit (Z. 131–133, 201–207): Der Katalog führt sie nicht; ob die P10 sie prüft, nicht geprüft.
- Lösungsanhang nur für (L)-Teile (Z. 62–72): Lösungsdatei, nicht Blatt.
- Hinweis: Die Suchmuster zählen die Form, nicht, ob sie richtig umgesetzt ist.

---

## Teil C – Altlehrwerke Sek II (quellen/altlehrwerke-formen-sek2.md)

### kurvenuntersuchung
- K1 · Ort: katalog/kurvenuntersuchung.md, Sprossen Einheit 4 (Z. 128), vor „Graphen von f und f' aus berechneten Punkten einzeichnen" · Quelle: Z. 106–111, 941–944 · Befund: Das Skizzieren aus Vorgaben gibt es nur als LK-Sprosse. Im GK fehlt eine Stufe, auf der aus fertigen Eigenschaften gezeichnet wird, ohne zu rechnen.
  Vorschlag: „→ aus einer ausgefüllten Übersichtstabelle (Nullstellen, Extrempunkte, Monotonie, Verhalten im Unendlichen, Schnittpunkt mit der y-Achse) den Graphen skizzieren, nichts rechnen (GK)"
- K1 · Ort: kurvenuntersuchung.md, Sprossen Einheit 2, Kette „Extrempunkte berechnen" (Z. 125), Vorstufe · Quelle: Z. 134–138, 142–146 · Befund: Der Fehler „Extremstelle statt Extremwert" ist belegt (Z. 26). Keine Sprosse übt, Stelle, Wert und Punkt zu unterscheiden.
  Vorschlag: „„Stelle, Wert oder Punkt?" – zu Fragen und Antworten ankreuzen, ob die Stelle x₀, der Wert f(x₀) oder der Punkt (x₀ | f(x₀)) verlangt oder gegeben ist; nichts rechnen (Vorstufe)"
- K1 · Ort: kurvenuntersuchung.md, Sprossen Einheit 2, Kette „Extrempunkte nachweisen" (Z. 126), vor „Sattelstelle ausschließen oder nachweisen" · Quelle: Z. 139–141, 146–148 · Befund: Es fehlt eine Denkstufe ohne Rechnung.
  Vorschlag: „→ „Ändert sich die Monotonie, ändert sich die Krümmung?" – an Graphen ankreuzen: Monotonie ändert sich → Extrempunkt, Monotonie bleibt und Krümmung ändert sich → Sattelpunkt; nichts rechnen"

### extremalprobleme
- K1 · Ort: katalog/extremalprobleme.md, Sprossen Einheit 2 (Z. 79), nach dem Grundfall · Quelle: Z. 376–381, 397–400, 944–948 · Befund: Die Kette übt das Aufstellen der Zielfunktion nur an Figuren. Eine Stufe ohne Figur, die Haupt- und Nebenbedingung trennt, fehlt.
  Vorschlag: „→ eine feste Nebenbedingung, wechselnde Zielfunktion ohne Figur: eine Zahl in zwei Summanden zerlegen, einmal das Produkt, einmal die Summe der Quadrate als Zielfunktion aufstellen und ausmultiplizieren"
- K1 · Ort: extremalprobleme.md, Sprossen Einheit 3 (Z. 80), nach „mit Substitution lösen …" · Quelle: Z. 388–392, 401–403 · Befund: Randwerte stehen im Merkkasten, aber keine Sprosse hat das Gesuchte am Rand.
  Vorschlag: „→ Randmaximum: die Zielfunktion hat im Innern nur ein Minimum; das gesuchte Maximum über die Randwerte des Definitionsbereichs bestimmen"

### geraden
- K1 · Ort: katalog/geraden.md, Sprossen Einheit 1 (Z. 100), direkt nach der Vorstufe · Quelle: Z. 606–617, 948–951 · Befund: „Der Parameter läuft" wird nur angekreuzt. Es fehlt die Stufe, die zu gegebenem t den Punkt ausrechnet – Vorstufe der Punktprobe.
  Vorschlag: „→ Wertetafel: zu fünf Parameterwerten (auch negativ und gebrochen) die Punkte ausrechnen und eintragen"
- K1 · Ort: geraden.md, Sprossen Einheit 1 (Z. 100), vor „die Gleichung durch zwei Punkte aufstellen" · Quelle: Z. 577–581, 591–594, 948–951 · Befund: Es fehlt, eine fertige Gleichung an einem bekannten Körper zu lesen.
  Vorschlag: „→ eine Gleichung lesen: zu welcher Kante oder Diagonale eines Quaders mit gegebenen Eckpunkten gehört sie?"
- K1 · Ort: geraden.md, Merkkasten Einheit 3 (Z. 65–70) und Vorstufe Einheit 3 (Z. 102) · Quelle: Z. 695–699, 711–719, 949–951 · Befund: Die vier Lagefälle stehen als Sätze; die Quelle fasst sie in eine Tafel und zeigt sie vorher am Quader.
  Vorschlag: „Merkkasten Einheit 3 als Vier-Fall-Tafel: Richtungsvektoren parallel? ja/nein × gemeinsamer Punkt? ja/nein → identisch, echt parallel, schneidend, windschief. Vorstufe ergänzen: „am Quader zu einer Kante je eine schneidende, parallele und windschiefe Kante zeigen, ohne Rechnung""

### abstaende
- K1 · Ort: katalog/abstaende.md, Sprossen Einheit 2 (Z. 104), zwischen Vorstufe und Grundfall; Schlusszeile beim Lotfußpunkt · Quelle: Z. 752–765, 951–953 · Befund: Im Grundfall wird in einem Schritt normiert und eingesetzt. Beide Bände üben vorher den Abstand des Ursprungs; am Ende die Probe des Lotfußpunkts.
  Vorschlag: „→ Abstand des Ursprungs: nur |d| durch den Betrag des Normalenvektors, noch keinen Punkt einsetzen; … → Lotfußpunkt über die Lotgerade, Probe: der Lotfußpunkt erfüllt die Ebenengleichung"

### flaecheninhalt-durch-integration
- K1 · Ort: katalog/flaecheninhalt-durch-integration.md, Sprossen Einheit 5 (Z. 106), nach „Vorzeichen und Wert null am Graphen begründen" · Quelle: Z. 499–510, 951–954 · Befund: Integralwert und Flächeninhalt werden nur beim Ankreuzen unterschieden, nie zu denselben Grenzen gerechnet.
  Vorschlag: „→ zu denselben Grenzen a) den Wert des Integrals, b) den Inhalt der Fläche rechnen und beide Ergebnisse nebeneinander nennen"

### binomialverteilung
- K1 · Ort: katalog/binomialverteilung.md, Sprossen Einheit 2 (Z. 125), nach „den Term für P(X = k) hinschreiben" · Quelle: Z. 887–906, 954–956 · Befund: Es fehlt die ganze Verteilung für kleines n mit der Summe eins als Kontrolle.
  Vorschlag: „→ die ganze Verteilung für kleines n: P(X = 0) bis P(X = n) der Reihe nach, Kontrolle: die Summe ist 1"

### ableitungsregeln
- K1 · Ort: katalog/ableitungsregeln.md, Sprossen Einheit 2 (Z. 97), nach der Vorstufe „Innen und außen?" · Quelle: Z. 157–171, 174–178, 183–187 · Befund: Es fehlt, u und v hinzuschreiben, auch rückwärts.
  Vorschlag: „→ innere und äußere Funktion hinschreiben, nicht ableiten: z = v(x) und u(z) als zwei Zeilen; rückwärts aus u und v die Verkettung bilden"

### funktionsklassen-und-eigenschaften
- K1 · Ort: katalog/funktionsklassen-und-eigenschaften.md, Sprossen Einheit 5 (Z. 139), nach der Vorstufe „Innen oder außen?" · Quelle: Z. 329–342 · Befund: Der Fehler „Faktor im Argument nicht invertiert" ist belegt; keine Sprosse übt, b auszuklammern.
  Vorschlag: „→ im Argument ausklammern: bx + c als b · (x + c/b) schreiben, die Verschiebung um c/b ablesen, noch nichts zeichnen"
- K1 · Ort: funktionsklassen-und-eigenschaften.md, Sprossen Einheit 2 (Z. 136), nach „eine bekannte Nullstelle durch Einsetzen bestätigen …" · Quelle: Z. 301–311, 314–318 · Befund: Die Einsetzprobe kommt nur vorwärts vor.
  Vorschlag: „→ rückwärts: einen Koeffizienten so bestimmen, dass eine gegebene Zahl Nullstelle ist; Kontrolle durch Faktorisieren"

### skalarprodukt-und-winkel
- K1 · Ort: katalog/skalarprodukt-und-winkel.md, Sprossen Einheit 1 (Z. 94), zwischen Vorstufe und Grundfall · Quelle: Z. 793–799, 807–813, 817–821 · Befund: Die Prüfungshöhe verlangt eine Begründung ohne Koordinaten; die Kette hat dafür keine Vorstufe.
  Vorschlag: „→ Skalarprodukt aus Längen und Winkel an einer Figur mit bekannten Winkeln (gleichseitiges Dreieck, Quader), ohne Koordinaten; das Vorzeichen aus dem Winkel ablesen"

### stammfunktion-und-hauptsatz
- K1 · Ort: katalog/stammfunktion-und-hauptsatz.md, Sprossen Einheit 1 (Z. 94), vor „die Konstante aus einer Wertebedingung bestimmen" · Quelle: Z. 416–420, 434–439 · Befund: Das „+ c" wird berechnet, bevor der Schüler es als Verschiebung gesehen hat.
  Vorschlag: „→ drei verschiedene Stammfunktionen angeben und in ein Koordinatensystem zeichnen; sagen, wie sie auseinander hervorgehen"

### tangente-normale-schnittwinkel
- K1 · Ort: katalog/tangente-normale-schnittwinkel.md, Sprossen Einheit 4 (Z. 120), nach der Vorstufe · Quelle: Z. 260–265, 267–271 · Befund: Steigungswinkel (0°–180°) und Schnittwinkel (bis 90°) werden nicht vor der Rechnung unterschieden.
  Vorschlag: „→ „Welcher Winkel?" – ankreuzen, ob der Steigungswinkel gegen die positive x-Richtung (0° bis 180°) oder der Schnittwinkel (höchstens 90°) gefragt ist; nichts rechnen"

### lagebeziehungen
- K1 · Ort: katalog/lagebeziehungen.md, Sprossen Einheit 3 (Z. 95), Schlusszeile des Grundfalls und der Sprossen mit Schnittpunkt · Quelle: Z. 704–710, 715–717, 931–933 · Befund: Schnittpunkte ohne Kontrolle.
  Vorschlag: „Kontrolle: den Schnittpunkt in die Ebenengleichung einsetzen; sie muss erfüllt sein"
- K1 · Ort: lagebeziehungen.md, Sprossen Einheit 1 (Z. 93), vor „das Seitenargument zwischen zwei parallelen Ebenen" · Quelle: Z. 726–735 · Befund: Davor fehlt der einfachste Vergleichspunkt, der Ursprung.
  Vorschlag: „→ Seite gegen den Ursprung: den Punkt in die nach null umgestellte Gleichung einsetzen und das Vorzeichen mit dem des Ursprungs vergleichen"

### vektoren-und-rechenoperationen
- K1 · Ort: katalog/vektoren-und-rechenoperationen.md, Sprossen Einheit 2 (Z. 82), vor „den Verbindungsvektor zweier Kantenmittelpunkte … als Linearkombination" · Quelle: Z. 530–535, 538–541 · Befund: Nicht geübt wird, dass derselbe Vektor mehrere Wege über die Kanten hat.
  Vorschlag: „→ denselben Verbindungsvektor auf zwei verschiedenen Kantenwegen schreiben und zeigen, dass beide dasselbe ergeben"

### zufallsexperimente-und-pfadregeln
- K1 · Ort: katalog/zufallsexperimente-und-pfadregeln.md, Sprossen Einheit 3 (Z. 157), vor „„mindestens einmal" … über das Gegenereignis" · Quelle: Z. 845–849, 856–857 · Befund: Die Kette springt ohne Zwischenstufe zur Formel 1 − (1 − p)ⁿ.
  Vorschlag: „→ Lückenterm ausfüllen: P(mindestens einmal) = 1 − (…)^… – Basis und Exponent eintragen, noch nicht ausrechnen"

### ableitung-und-aenderungsrate
- K1 · Ort: katalog/ableitung-und-aenderungsrate.md, Sprossen Einheit 3 (Z. 112), nach dem Grundfall · Quelle: Z. 226–237, 239–243 · Befund: Es fehlt eine Stufe, die das Ergebnis am Bild prüft.
  Vorschlag: „→ die Tangente am festen Punkt mit dem Lineal anlegen, die Steigung am Steigungsdreieck messen, dann rechnen und beide Werte vergleichen"

### ebenen
- K1 · Ort: katalog/ebenen.md, Sprossen Einheit 2, Kette „Normalenvektor und Nachweise" (Z. 116), nach dem Grundfall · Quelle: Z. 644–647, 657–662, 665–670 · Befund: Zwei Koordinaten null setzen steht nur als Zeichenhilfe, nicht als Weg zu einem Punkt der Ebene.
  Vorschlag: „→ einen Punkt der Ebene finden: zwei Koordinaten null setzen, die dritte ausrechnen, Probe durch Einsetzen"

### quer (Sek II)
- K2 · Ort: bank.md, „Regeln für den Inhalt" (Z. 157–160) · Quelle: Z. 530–533, 701–702, 927–930 · Befund: Die Bank wechselt bei jeder Variante Zahlen und Kontext; die Quelle rechnet ein ganzes Kapitel am selben Körper.
  Vorschlag: „In den Einträgen der analytischen Geometrie nutzen die Sprossen einer Kette denselben Körper mit festen Eckpunkten (je Variante ein Körper); neu ist je Sprosse nur das Merkmal."
- K2 · Ort: bank.md, Feld loesung (Z. 66–70) · Quelle: Z. 58–60, 384–396, 911–917 · Befund: Bei einer Sachaufgabe endet die Lösung mit dem „Zwischenergebnis"; die Quelle schließt mit einem Antwortsatz mit Einheit.
  Vorschlag: „Sachaufgabe: mit Zwischenergebnis und einem Antwortsatz, der das Gefragte mit Einheit nennt (nicht nur die Stelle)"
- K2 · Ort: bank/tangente-normale-schnittwinkel/e4.jsonl, Grundfall der Kette „Winkel" · Quelle: Z. 277–289 · Befund: Die Quelle hält den Punkt fest und wechselt nur den Winkel, auch 90°.
  Vorschlag: „Grundfall-Varianten: ein fester Punkt, Winkel aus allen Lagen (spitz, stumpf, 90°); die 90°-Variante als Begründung „keine Steigung""
- K3 · Ort: regeln.md, Regel 2 (Z. 19–29) und Maßstab (Z. 9–10) · Quelle: Z. 134–138, 267–271, 499–504 · Befund: Die Sek-II-Bank hatte keinen Sprachlauf; dort hängt die Falle oft am Fragewort.
  Vorschlag: „Sek II: Die Frage nennt genau, was gesucht ist – „die Stelle", „den Funktionswert" oder „den Punkt"; „den Winkel gegen die positive x-Achse" oder „den Schnittwinkel"; „den Wert des Integrals" oder „den Inhalt der Fläche". Maßstab für Sek II: ein schwacher Schüler des Grundkurses."
- K3 · Ort: regeln.md, Regel 6 (Z. 39–46) · Quelle: Z. 838–849, 852–856, 954–956 · Befund: Die Quelle lässt ein falsches Ergebnis erklären („größer als eins kann nicht sein"); Regel 6 kennt nur „Fehler finden".
  Vorschlag: „Falschergebnis erklären: „<Name> rechnet … und erhält …. Erkläre, warum das nicht stimmen kann.""
- K4 · Ort: layout-befunde.md, Nr. 54 Merkkasten (Z. 169–173) · Quelle: Z. 134–141, 329–337, 351–355, 918–926 · Befund: Wo ein Kasten Fälle unterscheidet, steht in der Quelle eine Tafel statt Sätzen.
  Vorschlag: „Merkkasten mit Fällen als Tafel statt Sätzen (Extrempunkt/Sattelpunkt 2×2, Lage zweier Geraden 2×2, Parameterbereich → Strecke/Strahl/Gerade); Neues gegen Bekanntes in zwei Spalten (Zahl | Vektor, Gerade in der Ebene | Ebene im Raum)."
- K4 · Ort: layout-befunde.md, Nr. 44 „Zutatenzeile" (Z. 135–137) · Quelle: Z. 92–95, 127–130, 384–387, 911–917 · Befund: In der Musterlösung trägt jeder Schritt Namen und Bedingung.
  Vorschlag: „Sek II: Die Musterlösung beschriftet jede Zeile mit ihrem Schritt und der Bedingung (Nebenbedingung:, Bedingung f''(x) = 0:, Nullstelle:); das Urteil steht in derselben Zeile wie die Einsetzung."

K1: 23 · K2: 3 · K3: 2 · K4: 2

### Nicht eingebunden, mit Grund (Teil C)
- Stochastik aus DDR-Schulbüchern: kein Kapitel; Baumdiagramme aus heutigen Quellen.
- Normale: in keinem Band eigener Stoff.
- h-Methode in drei Schritten: Katalog führt sie mit Absicht nur als Lesestoff.
- Satz von Rolle, Mittelwertsatz, Beweis der Summenregel: Beweisstoff, nicht GK.
- Hessesche Normalform mit Richtungskosinus, Abstand mit Vorzeichen: nicht GK-Form; das Vorzeichen steckt im Fund „Seite gegen den Ursprung".
- Paare gleicher Schwierigkeit nebeneinander mit ↑: widerspricht layout-befunde Nr. 6.
- Geringe Dichte, 7–34 Posten je Seite: bestätigt Nr. 48.
- Tangentengleichung in drei Zeilen; Stammfunktion „hin und zurück"; ebenen L12-81: schon vorhanden.
- Bruch zerlegen vor dem Aufleiten: negative Exponenten im GK ohne Prüfungsbeleg.
- Wegen der Grenze von 30 weggelassen (kleine Wirkung): sin-Graph getrennt nach a und b; Mittel-/Teilpunkt in zwei Schreibweisen; Netzaufgabe (λ; μ); Päckchenfolge Abstand→gleichschenklig; „Lage bestimmen, dann Schnittwinkel"; Skizze als Teilaufgabe a) und Tabelle f|g|a|b; kumulierte Treppe; Schnittstellen als Nullstellen der Differenz.
- Programmierte Verzweigung (ST-68): ein Blatt hat keine Sprungziele.
- Hinweis: „Stelle, Wert, Punkt" und „welcher Winkel" bewusst zweimal, als Sprosse (K1) und Sprachregel (K3).

---

## Teil D – Blattarten-Literatur (quellen/blattarten-literatur.md) → K5

1. Befund: Vorgerechnete Beispiele heben die Matheleistung, am stärksten bei Anfängern; danach Schritte ausblenden, bis der Schüler selbst löst. Bei Lernschwierigkeiten wirken ausdrückliche Anleitung und Beispielfolgen am stärksten. Quellen: Z. 138 (Barbieri et al. 2023, Metaanalyse, 55 Studien, g = 0,48), Z. 139, 160–162 (Renkl/Atkinson 2003), Z. 141 (Gersten et al. 2009, g = 1,22), Z. 142, 166–168 (IES-Leitfaden). Beleglage: stark.
   ändert in ziel.md § 2 (Option schwach): „der Merkkasten am Ende, nicht am Anfang." → Vorschlag: „vorn am Grundfall ein vorgerechnetes Musterbeispiel, danach ein bis zwei angefangene Lösungen, bei denen der Schüler die letzten Schritte ergänzt; der Merkkasten am Ende, nicht am Anfang." Dazu § 5 streichen: „Beispiel je Typ, Quelle der Merkkasten: am ersten Testlauf."
   Prompt: unterrichtsblatt.md 2.8 – bei schwach gilt „mit beispiel" aus 2.5 von selbst; 2.3 b und 1.1 bleiben für den Regelfall.
2. Befund: Was Anfängern hilft, kann Fortgeschrittenen schaden (Expertise-Umkehr). Z. 140, 163–165 (Kalyuga et al. 2003; Kalyuga 2007). Beleglage: mittel.
   ändert in ziel.md: „Kein Kasten auf dem Blatt; der Merkkasten bleibt im Katalog und ist auf Zuruf zu haben." → Vorschlag: „Kein Kasten und kein vorgerechnetes Beispiel auf dem Blatt; das Beispiel rechnet der Lehrer am Tisch vor. Gedruckt steht es nur bei „schwach" und auf Zuruf, der Merkkasten nur auf Zuruf."
   Prompt: unterrichtsblatt.md 2.3 b bestätigt. pruefungsblatt.md v0.15 führt Beispielzeile (2.2) und Wissensblock (2.3) noch als Standard – beim Umbau angleichen.
3. Befund: Vermischtes Üben schlägt geblocktes im späteren Test deutlich; alle Lehrwerke schließen das Kapitel mit vermischten Aufgaben und Selbsttest. Z. 128, 150–151 (Rohrer et al. 2020, RCT, 787 Schüler Kl. 7, d = 0,83), Z. 129, 130 (Brunmair/Richter 2019, g = 0,34), Z. 193–196, 274. Vorbehalt Z. 174–176: Vermischen mit Verteilen verbunden. Beleglage: stark.
   ändert in ziel.md § 2: „Der Schüler hakt am Ende ab, was er kann." → Vorschlag: „Am Ende steht „Prüfe dich": je Fertigkeit des Teils eine bis zwei Aufgaben, gemischt, ohne Verfahrensüberschrift und ohne Punkte; danach hakt der Schüler ab, was er kann."
   Prompt: unterrichtsblatt.md 2.3 h – vor „Das kann ich" eine Hauptnummer „Ich kann unterscheiden, …"; pruefungsblatt.md unverändert (Probeprüfung ist vermischt).
4. Befund: Mehr gleiche Aufgaben am Stück bringen nichts (neun statt drei: kein Effekt nach 1 und 4 Wochen); bei Hausaufgaben zählen Häufigkeit und Qualität. Z. 134, 152–153 (Rohrer/Taylor 2006), Z. 144–145, 171–172 (Trautwein 2007; Dettmers 2010), Z. 279–290. Beleglage: mittel.
   ändert in ziel.md § 1: „Ein Blatt ist nicht auf eine Stunde bemessen; … Im Zweifel ist ein Blatt voller, nicht kürzer: Der Lehrer streicht am Tisch, der Prompt streicht nicht vorher." → Vorschlag: „Ein Blatt trägt einen Teil des Themas, eine bis drei Fertigkeiten, je Fertigkeit die volle Leiter. Mehr Übung heißt öfter und gemischt, nicht mehr gleiche Aufgaben am Stück. Der Lehrer streicht am Tisch; der Prompt streicht keine Sprosse."
   Prompt: unterrichtsblatt.md § 0 („im Zweifel ist es voller") umformulieren; Kettendichte 2.4 bleibt. „Nie geschnitten" in pruefungsblatt.md § 0 und 2.2 muss beim Umbau fallen.
5. Befund: Verteiltes Üben hilft robust, in kleinem Maß; Wachhalten ist eine eigene Funktion: 5–10 vermischte Aufgaben, höchstens 10 Minuten, regelmäßig, ohne Note. Z. 131 (Murray/Horner/Göbel 2025, g = 0,28), Z. 133, Z. 27–48 (Bruder 2006/2008), Z. 250–253 (Pruzina 2010). Beleglage: stark für die Wirkung, Format ist Didaktik.
   ändert in ziel.md § 1: „Wiederholung ist dasselbe Thema später: …" → anhängen: „Wachhalten ist etwas anderes: kurze gemischte Übung quer durch Themen, die schon gelernt sind, 5–10 Aufgaben, regelmäßig, ohne Note. Das leistet das Basisheft, auf die Themen bis zur Klasse des Schülers gefiltert." Dazu § 4: „das Basisheft (… quer durch die Themen)" → „…; auch zum Wachhalten, in Blöcken zu 5–10".
   Prompt: pruefungsblatt.md 2.4 Zweck ergänzen (Wachhalten, Filter nach gelernten Themen, Block zu zehn = ein Termin). unterrichtsblatt.md hat kein Basisheft; für Kl. 8/9 fehlt die Quelle (katalog-basis führt P10-Stoff).
6. Befund: Lehrwerke und DZLM prüfen Vorwissen mit Selbsteinschätzung und koppeln jede Diagnoseaufgabe an eine Förderstelle. Z. 91–95 (Deutscher/Prediger/Selter 2013), Z. 193–196, 272. Beleglage: mittel.
   ändert in ziel.md § 2: „Hängt der Schüler in dieser Zone, ist die Lücke älter als das Thema – das ist ein Befund, den das Blatt ohne Kennzeichnung sichtbar macht." → Vorschlag: „Hängt der Schüler in dieser Zone, ist die Lücke älter als das Thema. Je Nummer der Zone steht, wo es weitergeht: die Fertigkeit als eigenes Blatt (Fokus) und die Nummer im Lernblatt, die sie braucht."
   Prompt: unterrichtsblatt.md 2.2 Lösungszeile um „hängt → Fokus ‹Fertigkeit›" erweitern (Muster in pruefungsblatt.md 2.2, 2.6). Offen: Verweis auch auf dem Schülerblatt?
7. Befund: Länge der Zone nach Stand, nicht nach Zeit; keine Studie zur Länge. Z. 296–303, 354. Beleglage: schwach.
   ändert in ziel.md § 2: „Wie breit sie ist, bestimmt die Bestellung (§ 3); auf Zuruf entfällt sie oder schrumpft …" → Vorschlag: „Die Zone ist kurz und immer gleich gebaut: je Fertigkeit eine leichte und eine Fallstrick-Aufgabe; wer hängt, bekommt den Verweis (oben), keine längere Zone. Auf Zuruf entfällt sie."
   Prompt: unterrichtsblatt.md 1.1 „wiederholung kurz" und 2.2 fallen zusammen; kurze Form wird Standard.
8. Befund: Förderleitfäden verlangen häufige kumulative Wiederholung, alt und neu gemischt. Z. 142, 166–170 (Gersten 2009; Fuchs 2021), Z. 276. Beleglage: mittel (Grundschule bis Kl. 8).
   ändert in ziel.md § 2 (Option schwach): anhängen: „Bei „schwach" mischt „Prüfe dich" zwei Aufgaben aus der Zone ein, alter und neuer Stoff zusammen."
   Prompt: unterrichtsblatt.md 2.8 ein Punkt dazu.
9. Befund: Einüben am Stück wirkt erst mit einem zweiten, verteilten Termin. Z. 133, 134, 131, 273. Beleglage: mittel.
   ändert in ziel.md § 3: „Fokus: ein Typ, jede Sprosse mehrfach." → Vorschlag: „Fokus: ein Typ, jede Sprosse zwei- bis dreimal. Derselbe Typ kommt einige Tage später gemischt wieder, im Basisheft oder in „Prüfe dich" des nächsten Blatts."
   Prompt: Ausgabeblock nennt den Folgetermin als Zeile; Umfang 15–25 Teilaufgaben nicht erhöhen.
10. Befund: Produktives Üben: Päckchen mit Struktur und Nachdenkfrage. Z. 58–78 (Leuders; PIK AS). Gegenbefund Z. 175–177. Beleglage: schwach. ändert nichts; die Erklärzeile bleibt am Päckchen, nicht am Musterbeispiel.
11. Befund: Lern- und Leistungssituation trennen. Z. 84–90 (Leisen 2013). Beleglage: schwach. ändert nichts; stützt „Punkte nur im Prüfungsheft" und „Prüfe dich" ohne Punkte.
12. Befund: Gestufte Aufgabensets (MAKOS; Bruder/Feldt-Caesar 2018) entsprechen der Leiter. Z. 49–57. ändert nichts.

Antworten auf die vier offenen Fragen:
- „Prüfe dich" im Lernblatt: Ja (RCT Kl. 7, alle Lehrwerke, DDR 1986 „Komplexe Übungen"). Grenze: bei 1–3 Fertigkeiten ist die Mischung schmal; die RCT mischte über Kapitel.
- Zone als Diagnose mit Verweis statt Schalter: Ja für den Verweis (DZLM, Lehrwerke); Länge nach Stand statt Zeit ist nur Deutung; zur Länge kein Beleg.
- Wachhalten über das Basisheft statt neuer Blattart: Funktion belegt, Form nicht; kurz, gemischt, regelmäßig, ohne Note. Das Basisheft trägt es, wenn es kürzer wird und nach gelernten Themen gefiltert ist.
- Musterbeispiel bei „schwach": Ja, mit Ausblenden – stärkste Beleglage der Datei. Regelfall ohne Beispiel bleibt richtig (Expertise-Umkehr). Stellung des Merkkastens: kein Beleg.

Nicht eingebunden (Teil D): Hattie-Werte (Methode kritisiert); Abrufeffekt (in Mathe nicht gesichert); zeitlich gerahmte Übung (Kl. 1); Hausaufgaben r ≈ 0,22 (korrelativ); Kernprozesse; MAKOS-Reihenfolge „zuerst Grund- und Umkehraufgabe" (Sprossenfolge → Katalog; widerspricht ziel.md § 1 „oben … Umkehrung" – Hinweis für die Katalogarbeit); Dichtezahlen; Merkkasten vorn/hinten, Päckchenlänge 4–8 (kein Beleg); Grundwissentest Bayern; Namensfrage „Fokus"→„Training" (Beschluss 28.09.); „Mischblatt" als vierte Blattart; [wf]-Zitate (Rohrer 2020, Rohrer/Taylor 2006) vor Übernahme am Original prüfen. Nebenbefund: ziel.md steht auf dem 25.09.; pruefungsblatt.md v0.15 führt noch „Vorbereitung".

---

## Teil E – Nachhilfe-Situationen (quellen/nachhilfe-situationen.md) → K5

1. Klassenarbeit landet im Prüfungsheft. Situation A. Befund: Die Klassenarbeit ist der häufigste Anlass (71 % Eltern, 67 % Schüler); Z. 60, 80–83 (Jürgens/Dieckmann 2007; Studienkreis/Forsa 2013). Beleglage: mittel bis schwach. Deckt das Blatt sie ab? Teils: ziel.md § 3 „Klassenarbeit, Test: kein eigenes Format", aber pruefungsblatt.md 1.1: „„prüfung", „probeprüfung", „test", „klassenarbeit" → Probeprüfung (2.6)" – eine Arbeit in Klasse 8 wird zur P10-Probe mit 135 Minuten.
   Vorschlag: „Klassenarbeit, Test: kein eigenes Format und immer ein Unterrichtsblatt; das Prüfungsheft baut nur für die Abschlussprüfung." Prompt: pruefungsblatt.md 1.1 – „test" und „klassenarbeit" fallen als Auslöser weg; Deutungszeile nennt erzeugeUnterrichtsblatt().
2. Bei einer Klassenarbeit ohne Ausblick. Befund: Nachhilfe wirkt eher, wenn sie an den Unterricht gekoppelt ist; Z. 97 (EEF), Z. 184–191 (Deutung). Beleglage: mittel. Deckt das Blatt sie ab? Nein: ziel.md § 3 „Ohne Angabe: mit Wiederholung, und mit Ausblick, wenn das Thema in blaetter/ noch nicht liegt" – keine Ausnahme für die Arbeit.
   Vorschlag: „Bei einer Klassenarbeit gilt ohne Angabe: mit Wiederholung, ohne Ausblick – die Arbeit fragt, was bis jetzt dran war." Prompt: unterrichtsblatt.md 1.1 und 2.6; Deutungszeile „ohne Ausblick (Klassenarbeit)".
3. Lösungen der Zone mit Auswertungszeile. Situation E und C. Befund: Förderung wirkt, wenn eine Diagnose den Bedarf bestimmt; MSK ordnet jedem Fehler Ursache und Förderung zu; Z. 99, 105, 134, 161–165. Beleglage: mittel. Deckt das Blatt sie ab? Teils: Lösungen der Zone sagen nur, welche Nummer welchen Zweig trägt (unterrichtsblatt.md 2.2).
   Vorschlag: „Die Lösungen der Zone tragen je Fallstrick-Aufgabe eine Zeile für den Lehrer: welche falsche Antwort auf welche ältere Lücke zeigt und mit welcher Eingabe er den Fokus darauf bestellt. Auf dem Blatt steht davon nichts." Prompt: unterrichtsblatt.md 2.2 (letzter Punkt) und 3.4, etwa „3c falsch (Nenner addiert) → Brüche addieren; neuer Chat: ‚brüche addieren'". (Deckt sich mit Teil D Befund 6.)
4. Ein Foto der Aufgabe bestellt den Fokus. Situation B. Befund: Förderung wirkt, wenn sie auf den konkreten Bedarf zielt; Z. 98 (EEF), Z. 196–199, 272–274 (Deutung). Beleglage: mittel. Deckt das Blatt sie ab? Teils: unterrichtsblatt.md 1.7 macht aus einer Aufgabe im Bild ein Lernblatt, pruefungsblatt.md 1.6 bei eindeutigem Typ einen Fokus – Widerspruch.
   Vorschlag: „Ein Fokus wird über den Einheits- oder Typnamen bestellt, über die Nummern eines früheren Blatts oder über das Foto der einen Aufgabe, an der der Schüler hing." Prompt: unterrichtsblatt.md 1.7 übernimmt die Regel aus pruefungsblatt.md 1.6.
5. Das Blatt trägt die Übung zwischen den Stunden. Befund: Eine Sitzung je Woche bringt kaum große Effekte; kurze, häufige Sitzungen, verteiltes Üben und Übungstests wirken; Z. 93 (Nickow 2020), Z. 96, 107–112 (Dunlosky 2013), 122–125. Beleglage: stark für die Wirkung, Übertragung aufs Blatt ungeprüft. Deckt das Blatt sie ab? Teils: ziel.md § 1 „nicht auf eine Stunde bemessen", aber Erfolgskriterium „mit Hilfe des Lehrers … nicht allein".
   Vorschlag: „Was am Tisch angefangen ist, setzt der Schüler zu Hause allein fort und prüft es an der Lösungsdatei; deshalb steht jede Hauptnummer für sich, mit eigener Anweisung." Prompt: unterrichtsblatt.md 0 (Leitziel); Prüfung nach 5.1, dass keine Anweisung auf die mündliche Erklärung verweist.
6. Die Schreibweise der Schule gilt auch ohne Arbeit. Befund: Z. 97, 99 (EEF), 116–118. Beleglage: mittel. Deckt das Blatt sie ab? Teils: ziel.md § 3 „Gegebene Übungsaufgaben setzen Form und untere Höhe" gilt nur für die Klassenarbeit.
   Vorschlag: „Bringt der Lehrer Aufgaben oder Heftseiten der Schule mit, übernimmt das Blatt deren Schreibform und Bezeichnungen, mit oder ohne Arbeit; die Leiter bleibt." Prompt: unterrichtsblatt.md 1.7 und 0 (Konventionen); Deutungszeile „Schreibform aus Heft".
7. Abhaken an der obersten Sprosse. Befund: Eine Prüffrage entscheidet, ob es weiter oder zurück geht; Z. 137, 157–158 (Wiliam), Z. 111. Beleglage: schwach für die Form. Deckt das Blatt sie ab? Teils: „Der Schüler hakt am Ende ab, was er kann" ist Selbstauskunft ohne Prüfung.
   Vorschlag: „Der Schüler hakt am Ende ab, was er kann; abgehakt wird eine Nummer, deren oberste gerechnete Sprosse stimmt." Prompt: Abhakseite 2.3 h bekommt eine Anweisungszeile.
8. Ein Blatt für alle ist bestätigt. Befund: 34 % der Nachhilfeschüler stehen bei 1 bis 3; Z. 36–40 (Klemm/Hollenbach-Biele 2016), Z. 68. Keine Änderung.

Nicht eingebunden (Teil E): Dialog Frage 1/2 mit Tabelle F1 × F2 (Dialog über die Lage des Schülers; Anlass A kommt über „klassenarbeit", B über Typname oder Foto); Schülerprofil; Standort-Blatt für E (neue Blattart, Kern in Befund 3); Mischblatt und Antwort „wachhalten" (neue Blattart); Schalter „nur obere/untere Sprossen" (schneidet nach Stand); Kopplung „schwach" an Stand; Länge je Anlass; kürzere Zone bei Thema in blaetter/ (verdeckter Schülerbezug); Sitzungsfrequenz (Organisation); Diagnose-Aufgabenformen und Itemquellen (Bank, Katalog – außerhalb dieses Teils); Anlass D (abgedeckt durch § 4); Versetzung, Lernstrategien; Wirksamkeit nach Tutorenart. Nebenbefund: pruefungsblatt.md v0.15 führt noch „Vorbereitung".
