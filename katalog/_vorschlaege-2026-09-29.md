# Vorschläge 29.09.2026 – Katalogbefund 3–8 und Sek-II-Nachzug

Stand 29.09.2026, Katalog auf Commit c8c16ef (Auftrag Nacht 2026-09-29, Teil 8; der Abschnitt „Sek-II-Nachzug“ gehört zu Teil 4 Punkt 7). Zeilennummern „Z.“ der Einträge und der Belegdateien beziehen sich auf diesen Stand.

Zweck: Vorschlag für das Urteil im Chat nach beschluss-2026-09-26.md Punkt 5 („Befund Katalog 2 (Sprossenregel) und 3–8 … werden als Vorschlagsdateien mit Beleg je Zeile vorbereitet; das Urteil fällt im Chat“). **Nichts ist in die Einträge übernommen**; kein Eintrag, keine Belegdatei und keine Stellenliste ist geändert. Marken in eckigen Klammern baut werkzeuge/marken-bau.py – dafür steht hier kein Handwert, sondern die Abweichung mit Fundstellen und die Entscheidung, die an Belegdatei oder Stellenliste zu treffen wäre.

Zählung: 6 Punkte · 22 vorgeschlagene Zeilen · 1 Zeile „kein Beleg gefunden“

Lesart: Eine „vorgeschlagene Zeile“ ist eine Zeile im Format des Eintrags (Typzeile, Sprossenkette, Erkennungsschritt, Kastenzeile, Lerneinheit, Zielmarke), die neu dazukommt oder eine bestehende ersetzt; sie steht im Codeblock, darunter der Einfügeort und „Beleg:“. Beleg ist nur eine Prüfungs-id (msa/, fhr/, abitur/), eine Lehrwerksstelle aus katalog/_klassen-belege.md (Reihe, Klasse, Seite, Verzeichniszeile, Zeile dort) oder eine Stelle eines Rahmenlehrplans unter quellen/; LISUM-Planungshilfen (quellen/quelle-lisum-planungshilfen-7bis10.txt) stehen als Zusatz daneben. Die Eingaben des Testlaufs 25.09. (blaetter/testlauf-2026-09-25/lesezettel.md) erklären den Befund, sind aber kein Beleg. Sprossen und Erkennungsschritte sind außerhalb der Belegklammern ziffernfrei geschrieben (Kastenzahlen-Sperre, katalog/_pruef_katalog.py); wo eine bestehende Sprosse Ziffern trägt, sind sie unverändert übernommen.

Probe: Alle 22 Zeilen wurden in eine Kopie des Katalogs auf c8c16ef eingesetzt (Hilfsskript im Scratchpad, nichts im Repo); katalog/_pruef_katalog.py meldet je Eintrag keinen neuen Treffer (quadratische-funktionen, lineare-funktionen, daten, binomische-formeln, prozentrechnung, kurvenuntersuchung „ERGEBNIS: ok“; terme.md dieselben zwei Blatt-0-Treffer wie vorher, Z. 28–29 „3 − 7“ und „3 · (−4)“), die Sek-II-Zählzeilen von daten.md und kurvenuntersuchung.md bleiben gleich, katalog/_pruef_struktur.py gibt dieselbe Ausgabe wie ohne die Vorschläge.

## Katalogbefund 3 – quadratische-funktionen.md, Einheit 4: p-q-Sonderfälle

**Befund** (befund-testlauf-2026-09-25.md, Katalog 3): „quadratische-funktionen.md Einheit 4: p-q-Sonderfälle (Radikand null, negativ) fehlen in der Kette (Eingabe 7).“ Stand heute: offen. Der Commit c8c16ef hat nur die Änderungszeile im Kopf (Z. 3) und den Kasten Einheit 4 (Z. 73–74, Schreibform „0 = p(x)“) geändert; Typzeile, Kette und die Sonderfall-Zeile Z. 77 sind unverändert.

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 25 (Typen Einheit 4): „Nullstellen aus der Normalform mit der p-q-Formel · vorher durch den Streckfaktor teilen · Nullstellen mit Wurzel als Ergebnis (Näherungswert)“ – kein Typ für den Wert unter der Wurzel; die Zahl der Nullstellen steht nur als „Zahl der Nullstellen am Scheitel begründen“.
- Z. 104 (Sprossen): „… → Zahl der Nullstellen am Scheitel begründen → Nullstellen aus der Normalform mit der p-q-Formel, ganzzahlig → Wurzel bleibt stehen, Näherungswert → …“ – der Sonderfall nur über den Scheitel, nicht über die Formel.
- Widerspruch zum eigenen Kasten, Z. 77: „Zwei Lösungen: zwei Schnittpunkte. Eine Lösung: Berührpunkt. Keine Lösung (Wurzel aus einer negativen Zahl): kein gemeinsamer Punkt.“ – der Kasten lehrt die Sonderfälle, Typzeile und Kette üben sie nicht.
- Das Verfahren steht im Nachbareintrag (quadratische-gleichungen.md Z. 26 „unter der Wurzel null: genau eine Lösung · unter der Wurzel negativ: keine Lösung“, Z. 108 als Sprossen); hier fehlt die Deutung am Graphen (Nullstelle, Berührpunkt, kein gemeinsamer Punkt).

**Vorschlag 3.1 – Typzeile Einheit 4 (ersetzt Z. 25)**

```
Einheit 4: Nullstellen aus der Scheitelpunktform durch Wurzelziehen · Zahl der Nullstellen am Scheitel begründen · Nullstellen aus der Normalform mit der p-q-Formel · Wert unter der Wurzel null: genau eine Nullstelle, der Scheitel liegt auf der x-Achse · Wert unter der Wurzel negativ: keine Nullstelle · vorher durch den Streckfaktor teilen · Nullstellen mit Wurzel als Ergebnis (Näherungswert) · Argument zu gegebenem Funktionswert (Gleichung aufstellen, ordnen, lösen) · Schnittpunkte Gerade und Parabel (gleichsetzen, alles auf eine Seite, lösen, y-Werte über die Gerade) [OS 10, GYM 9] · Parabel in Scheitelpunktform gleichsetzen (Klammer auflösen) · Zahl der gemeinsamen Punkte von Gerade und Parabel am Wert unter der Wurzel (zwei Schnittpunkte, ein Berührpunkt, keiner) · Punktprobe als Schnittpunkt-Nachweis (in beide Funktionen einsetzen) · Gerade ohne gemeinsamen Punkt mit der Parabel angeben (waagerecht jenseits des Scheitels) · Schnittpunkte zweier Parabeln berechnen (LISUM G, kein P10-Original) · Fehler finden (nur eine Lösung; y-Werte vergessen; Vorzeichen beim Umstellen; Klammer ohne Mittelglied aufgelöst) · Begründen (warum Nullstellen Schnittpunkte mit der x-Achse sind; warum eine waagerechte Gerade unter dem Scheitel die nach oben geöffnete Parabel nicht trifft; warum der Wert null unter der Wurzel nur eine Nullstelle ergibt).
```

Neu sind drei Typen und ein Begründen-Teil; alles andere wortgleich Z. 25, die Typklammer „[OS 10, GYM 9]“ bleibt Sache von marken-bau.py.

Beleg: [RLP G] quelle-rlp-teil-c-mathematik-2023.txt Z. 2852–2855 „Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen und Formulierung diesbezüglicher Aussagen und Begründungen“; Z. 2898–2902 Merkmale „Schnittpunkte mit den Koordinatenachsen“ quadratischer Funktionen; [Lehrwerk] _klassen-belege.md Z. 3671–3672 „Schnittpunkt Kl. 10, S. 23: „7 Nullstellen““, „Schnittpunkt Kl. 10, S. 26: „8 Schnittpunkte““, Z. 3677 „Elemente Kl. 9 (Ausgabe 2016), S. 87: „2.8 Schnittpunkte von Parabeln und Geraden““, Förderheft Z. 3685 „Schnittpunkt-Förderheft Kl. 10, S. 11: „Nullstellen (1)““; [Prüfung] fhr 2025-A-1d (Nachweis „die Diskriminante von x^2 + (4/3)x + 4/3 = 0 ist negativ, weitere Nullstellen gibt es nicht“ – Sek II), msa 2021-OS-K7c („(x + 7)² = 0 hat genau eine Lösung“), 2026-FOR-K5d (genau ein gemeinsamer Punkt, Berührung im Scheitel), 2020-GYM-B2b (kein gemeinsamer Punkt zweier Parabeln; Fehlerquelle „… aus der negativen Diskriminante (2x² = −1) nur „keine Lösung“ ohne inhaltliche Begründung über die Wertebereiche folgern“); [LISUM-PH Jg. 9 EBR/FOR] Z. 1841–1844 „Lösen quadratischer Gleichungen, auch durch Anwenden der p-q-Formel“, „Untersuchen der Lösbarkeit von quadratischen Gleichungen und Lösungsvielfalt“, „Berechnen der Schnittpunkte von Parabeln bzw. von Parabel und Gerade“. Kein P10-Original rechnet den Sonderfall über die Formel (Suche über msa-katalog-basis/-kontext/-gym: nur die genannten).

**Vorschlag 3.2 – Sprossenkette Einheit 4 (ersetzt Z. 104)**

```
- Nullstellen und Schnittpunkte (Einheit 4): gleichzusetzende Terme markieren (Vorstufe) → Nullstellen aus der Scheitelpunktform durch Wurzelziehen, ganzzahlig (4×) → Zahl der Nullstellen am Scheitel begründen → Nullstellen aus der Normalform mit der p-q-Formel, ganzzahlig → Wert unter der Wurzel null: genau eine Nullstelle, Gegenprobe am Scheitel auf der x-Achse → Wert unter der Wurzel negativ: keine Nullstelle, Gegenprobe an der Lage des Scheitels → Wurzel bleibt stehen, Näherungswert → vorher durch den Streckfaktor teilen → Argument zu gegebenem Funktionswert → Schnittpunkte Gerade und Parabel in Normalform, ganzzahlig → Parabel in Scheitelpunktform (Klammer auflösen) → y-Werte über die Gerade und Punkte angeben → Wert unter der Wurzel null: die Gerade berührt die Parabel in einem Punkt → Wert unter der Wurzel negativ: Gerade und Parabel haben keinen gemeinsamen Punkt → Punktprobe als Schnittpunkt-Nachweis in beiden Funktionen → Gerade ohne gemeinsamen Punkt angeben (waagerecht jenseits des Scheitels) → Schnittpunkte zweier Parabeln berechnen, beide in Normalform (ohne Original; Zielmarke nach RLP und LISUM-PH, EBR/FOR-Reihe) → Prüfungshöhe: Schnittpunkte einer fallenden Geraden mit einer Parabel in Scheitelpunktform berechnen (P10-Form 2022-OS-K3c, Stern); Nullstellen einer Normalform mit Wurzel als Ergebnis (P10-Form 2025-OS-K5c, Stern); x-Werte zu einem gegebenen y-Wert bei einer nach unten geöffneten Parabel (P10-Form 2023-OS-K4c, Stern).
```

Neu sind vier Sprossen (je Sonderfall eine für Nullstellen und eine für Schnittpunkte, ein Merkmal je Sprosse), eingefügt an der Stelle, an der quadratische-gleichungen.md Z. 108 dieselben Fälle führt („p ungerade … → Wert unter der Wurzel null: eine Lösung → Wert unter der Wurzel negativ: keine Lösung → …“); Prüfungshöhe wortgleich.

Beleg: wie 3.1; für die Stellung hinter dem ganzzahligen Grundfall zusätzlich quadratische-gleichungen.md Z. 26 und 108 (Verfahrenseintrag, dort mit denselben Belegen: [LS-AA Kl. 9 II 5] = _klassen-belege.md Z. 3779 „LS Kl. 9: „Kapitel II Quadratische Gleichungen“ (Z. 185) › „5 Lösungsformel für quadratische Gleichungen““).

**Hinweise.** Die Sprossenfolge der Einheit 4 prüft auch Teil 7 (katalog/_vorschlaege-sprossen-2026-09-29.md); stellt der Chat dort um, sind die vier neuen Sprossen hinter „Nullstellen aus der Normalform mit der p-q-Formel“ bzw. hinter „y-Werte über die Gerade“ mitzunehmen. Neue Typnamen sind nach der Übernahme in werkzeuge/klassen-belege-typen.txt und katalog/_klassen-belege.md nicht vorhanden – beide sind abgeleitet und neu zu bauen, nicht von Hand zu ändern.

## Katalogbefund 4 – lineare-funktionen.md: vier Typen ohne Sprossen

**Befund** (Katalog 4): „lineare-funktionen.md: Sprossen für Argument zum Funktionswert, Parameter deuten, Gerade durch zwei Punkte zeichnen, Schnittpunkt rechnerisch fehlen (Eingabe 4).“ Stand heute: offen (letzte Änderung am Eintrag 7613213, Marken-Zeilen; Typen und Ketten unverändert).

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 22 „Parameter deuten (steigend, fallend, parallel, Sonderfall m = 0) [OS 8]“ – keine Sprosse in Z. 83 („Graph zeichnen“) oder Z. 84 („Ablesen“).
- Z. 23 „Argument zum Funktionswert [OS 8]“ – nur eine Sprosse in Z. 85: „… → x Dezimal → Argument zum Wert (Gleichung lösen) → Punktprobe ja/nein gemischt → Nullstelle (Funktionswert null) → Prüfungshöhe: Punktprobe mit Bruch-m.“
- Z. 24 „Gerade durch zwei Punkte zeichnen“ und „Schnittpunkt zweier Geraden rechnerisch [OS 8, GYM 8]“ – Z. 86 „Gleichung bestimmen (Einheit 4)“ endet mit „Prüfungshöhe: zwei Punkte mit Bruch-m“, ohne Zeichen- und Schnittpunkt-Sprosse; Z. 87 nennt den Schnittpunkt nur als Prüfungshöhe der Tarife („ab wann günstiger (Schnittpunkt im Kontext)“).
- Z. 92 (Zuordnung): „Einheit 4 – Gerade durch zwei Punkte zeichnen, Geradengleichung aus zwei Punkten“ – ein P10-Typ ohne Kette.

**Vorschlag 4.1 – neue Kette „Parameter deuten“ (einfügen nach Z. 84, „- Ablesen (Einheit 2): …“)**

```
- Parameter deuten (Einheit 2): „Steigt oder fällt die Gerade?“ ankreuzen (Vorstufe) → am Vorzeichen von m entscheiden, ob die Gerade steigt oder fällt (4×) → von zwei Geraden die steilere am Betrag von m erkennen → gleiches m: parallele Geraden erkennen und zu einer Geraden eine Parallele angeben → m gleich null: waagerechte Gerade, Gleichung ohne x → n als Schnittpunkt mit der y-Achse deuten, gleiches n: gemeinsamer Punkt auf der y-Achse → n gleich null: Gerade durch den Ursprung → zu einer Gleichung Aussagen über Steigen, Schnittpunkt mit der y-Achse und Ursprung als wahr oder falsch beurteilen → zu einer genannten Eigenschaft den passenden Graphen wählen → m und n im Sachzusammenhang deuten (Änderung je Einheit, Anfangswert) → Prüfungshöhe: zu einer Gleichung unter vier Aussagen die beiden richtigen über Monotonie, Schnittpunkt mit der y-Achse und Ursprung ankreuzen (P10-Form 2021-OS-K2b, Niveau I); zu den Eigenschaften „Anstieg“ und „parallel zur x-Achse“ je den passenden Graphen wählen (2019-OS-K2b, Niveau I); die Bedeutung von x, y und dem Achsenabschnitt einer Kerzengleichung angeben (2021-OS-K6c, Stern; Typ bei lineare-gleichungssysteme.md); im Gymnasialpapier die Lage zweier Geraden mit gleicher Steigung bestimmen (2014-GYM-B1i, Niveau II).
```

Beleg: [RLP F] Z. 2816–2823 „Bestimmen und Beschreiben von Merkmalen linearer Funktionen der Form y = ax + b (Steigung, Änderungsrate, Nullstelle, y-Achsenabschnitt, Einfluss der Parameter auf den Verlauf des Graphen)“; [Lehrwerk] _klassen-belege.md Z. 3248 „Typ: Parameter deuten (steigend, fallend, parallel, Sonderfall m = 0) – Sekundo Kl. 8, S. 122: „Sonderfälle linearer Funktionen““, Z. 3251 „… – Schnittpunkt Kl. 8, S. 74: „5 Parallele und senkrechte Geraden““, Z. 3220 „Sekundo Kl. 8, S. 125: „Die Bedeutung von m und c bei Graphen zur Funktion y = mx + c““; [Prüfung] msa 2021-OS-K2b, 2019-OS-K2b, 2016-OS-B1c, 2021-OS-K6c, 2014-GYM-K2a, 2014-GYM-B1i, 2016-GYM-B1c; [LISUM-PH Jg. 8] Z. 1057–1059 „Untersuchen des Einflusses des Parameters n …“, „Interpretieren des Parameters n als y-Achsenabschnitt …“, Z. 1085 „Untersuchen der Lagebeziehung von zwei Geraden (Parallelität, ggf. auch Identität)“. Die Vorstufe ist der vorhandene Erkennungsschritt Z. 37.

**Vorschlag 4.2 – Kette „Funktionswert“ ohne Argument und Nullstelle (ersetzt Z. 85)**

```
- Funktionswert (Einheit 3): x positiv ganz (4×) → x negativ → x Dezimal → Punktprobe ja/nein gemischt → Prüfungshöhe: Punktprobe mit Bruch-m.
```

Grund: Argument und Nullstelle lösen eine Gleichung, Funktionswert und Punktprobe setzen ein – zwei Verfahren; beide Sprossen gehen in die Kette 4.3. Damit entfällt auch die Stellung „Nullstelle zwischen Punktprobe und Prüfungshöhe“, die das Blatt der Eingabe 4 umbauen musste.

Beleg: [Prüfung] msa 2017-OS-K5b (Funktionswert an einer negativen Stelle mit Bruchsteigung), 2026-FOR-K5b (Punktprobe mit negativem Argument), 2023-OS-B1i (den Punkt finden, der nicht auf der Geraden liegt); [RLP F] Z. 2811–2813 „Ermitteln und Nutzen von ausgewählten Punkten linearer Funktionen“; [LISUM-PH Jg. 8] Z. 1080 „Untersuchen, ob vorgegebene Punkte zu dem Graphen einer linearen Funktion gehören (Punktprobe, …)“.

**Vorschlag 4.3 – neue Kette „Argument zum Funktionswert“ (einfügen nach der Zeile aus 4.2)**

```
- Argument zum Funktionswert (Einheit 3): zu einem ganzzahligen Funktionswert das Argument bestimmen, Wert gleich Funktionsterm setzen und lösen, m positiv und ganzzahlig (4×) → Funktionswert negativ → m negativ (durch eine negative Zahl teilen) → m als Dezimalzahl oder Bruch → Probe durch Einsetzen → Funktionswert null: die Nullstelle → Argument am Graphen ablesen und mit der Rechnung vergleichen → im Sachzusammenhang: nach wie vielen Einheiten ein Wert erreicht ist, Ergebnis passend runden → Prüfungshöhe: eine Gleichung zu einem Sparplan aufstellen und daraus die kleinste Zahl von Monaten bestimmen, nach der ein Zielbetrag erreicht ist, aufgerundet (P10-Form 2022-OS-K6b, Niveau II); die Zeit bis zum Abbrennen einer Kerze als Nullstelle (2021-OS-K6d, Niveau I); die Nullstelle einer fallenden Geraden aus der Gleichung (2022-OS-K3a, Niveau I).
```

Beleg: [RLP F] Z. 2811–2813 „Ermitteln und Nutzen von ausgewählten Punkten linearer Funktionen“, Z. 2819–2820 Merkmal „Nullstelle“; [Lehrwerk] _klassen-belege.md Z. 3275 „Typ: Argument zum Funktionswert – Mathematik 2023 Kl. 8, S. 182: „Vertiefen: x-Koordinate berechnen““ (Verlagsmarke „Vertiefen“), Z. 3273–3274 Typzeilen „Nullstelle berechnen“ Fundamente Kl. 8, S. 121 „4.6 Nullstellen“ und LS Kl. 8 „5 Nullstellen und Schnittpunkte“; [Prüfung] msa 2022-OS-K6b (y = 55x + 990, 55x + 990 ≥ 2 000 → x ≥ 18,4, also neunzehn Monate), 2021-OS-K6d, 2022-OS-K3a, 2023-GYM-B1a, 2020-GYM-K3c; [LISUM-PH Jg. 8] Z. 1084 „Bestimmen von Nullstelle und Achsenschnittpunkten (durch Rechnungen und Ablesen am Graphen)“.

**Vorschlag 4.4 – neue Kette „Gerade durch zwei Punkte zeichnen“ (einfügen nach Z. 86, „- Gleichung bestimmen (Einheit 4): …“)**

```
- Gerade durch zwei Punkte zeichnen (Einheit 4): zwei Punkte mit ganzzahligen Koordinaten im ersten Quadranten eintragen und die Gerade ziehen (4×) → Punkte mit negativen Koordinaten, alle vier Quadranten → ein Punkt liegt auf einer Achse → eine Koordinate mit einer Hälfte auf dem Kästchenraster → die Gerade über beide Punkte hinaus bis zum Rand des Koordinatensystems ziehen → am gezeichneten Graphen y-Achsenabschnitt und Steigung mit dem Steigungsdreieck ablesen und die Gleichung angeben → die Achsen selbst anlegen und einteilen, dann die Gerade durch zwei Punkte zeichnen → Prüfungshöhe: die Gerade durch zwei Punkte mit negativen und halben Koordinaten zeichnen, zwei Aussagen zu Monotonie und Schnittpunkt mit der y-Achse beurteilen und eine Gleichung angeben (P10-Form 2025-OS-K5a, Niveau II, vier Punkte); das Koordinatensystem anlegen, die Gerade zeichnen und eine vorgegebene Gleichung nachweisen (2017-OS-K5a, Niveau II).
```

Beleg: [Prüfung] msa-typen „Gerade durch zwei Punkte zeichnen“ mit den Originalen 2025-OS-K5a (A(−2|6), B(3|−1,5), f(x) = −1,5x + 3) und 2017-OS-K5a (K(−4|−1), L(2|2), Achsen anlegen, y = ½x + 1 nachweisen); [RLP F] Z. 2811–2813 „Darstellen von Zuordnungen und linearen Funktionen im Koordinatensystem“, „Ermitteln und Nutzen von ausgewählten Punkten linearer Funktionen“; [Lehrwerk] _klassen-belege.md Z. 3296 „Fundamente Kl. 8, S. 118: „4.5 Geraden durch zwei Punkte““, Z. 3299 „Elemente Kl. 8 (Ausgabe 2016), S. 106: „2.5.1 Geraden durch zwei Punkte““.

**Vorschlag 4.5 – neue Kette „Schnittpunkt zweier Geraden rechnerisch“ (einfügen nach der Zeile aus 4.4)**

```
- Schnittpunkt zweier Geraden rechnerisch (Einheit 4): zwei Funktionsterme mit verschiedenen ganzzahligen Steigungen gleichsetzen, x ganzzahlig (4×) → x negativ → x als Dezimalzahl → den y-Wert mit einer Gleichung berechnen und mit der anderen prüfen, den Schnittpunkt als Punkt schreiben → gleiche Steigung: kein Schnittpunkt (parallel) oder alle Punkte gemeinsam (identisch) → den Schnittpunkt am Graphen ablesen und mit der Rechnung vergleichen → Prüfungshöhe: kein Original im Oberschulpapier als Haupttyp; im Gymnasialpapier die Koordinaten des Schnittpunkts zweier Geraden durch Gleichsetzen (2023-GYM-B1b, Niveau II, drei Punkte) und die Aussage, dass sich zwei Geraden mit verschiedenen Anstiegen in genau einem Punkt schneiden, mit Kontrolle durch Gleichsetzen (2021-GYM-B2b, Niveau II); im Sachzusammenhang die Strecke, ab der ein Tarif günstiger wird (2015-GYM-K3a; im Oberschulpapier 2016-OS-K6b im Lösungsweg – dort Prüfungshöhe der Kette „Anwendung (Einheit 5)“).
```

Beleg: [RLP G] Z. 2914–2918 „Nutzen von Lösungsprinzipien für lineare Gleichungssysteme zur Berechnung von Schnittpunkten von Funktionsgraphen“; [Lehrwerk] _klassen-belege.md Z. 3305 „Typ: Schnittpunkt zweier Geraden rechnerisch – LS Kl. 8: „5 Nullstellen und Schnittpunkte““, Z. 3306 „… – Mathematik 2023 Kl. 8, S. 183: „Vertiefen: Schnittpunkt zweier Geraden““, Z. 3311 „… – Sekundo Kl. 8, S. 129: „Schnittpunkt zweier Geraden““, Z. 3312 „… – Sekundo Kl. 9, S. 49: „Schnittpunkte zweier Geraden““; [Prüfung] msa 2023-GYM-B1b, 2021-GYM-B2b, 2015-GYM-K3a (200 + 1,5x = 2x → 400 km), 2016-OS-K6b; [LISUM-PH Jg. 8] Terme und Gleichungen Z. 937–938 „Lösen von Gleichungssystemen im Zusammenhang mit linearen Funktionen durch Gleichsetzen (Schnittpunkt berechnen)“, Lineare Funktionen Z. 1085–1086 „… Bestimmung des Schnittpunktes (durch Ablesen am Graphen, Punktprobe)“.

**Hinweise.** Keine Vorstufe in 4.3 bis 4.5: der Eintrag hat dafür keinen Erkennungsschritt ohne Ergebnis; der vorhandene Schritt Z. 39 („Setze für x eine ganze Zahl ein und rechne aus“) verlangt eine Rechnung und ist Gegenstand von Prompt-Befund 23, nicht dieses Punkts. Nebenbefund ohne Vorschlag: Z. 79 („Steigung als Bruch, Nullstelle berechnen, Gleichung aus zwei Punkten, Schnittpunkt rechnerisch sind F“) gegen RLP Z. 2912–2918 – der RLP führt „Ermitteln der Funktionsgleichung einer linearen Funktion aus zwei gegebenen Punkten“ und die Berechnung von Schnittpunkten von Funktionsgraphen auf G; die Planungshilfe Jg. 8 (Reihe F) führt beides. Das ist eine Stufenfrage für die nächste Pflege des Eintrags.

## Katalogbefund 5 – daten.md: Boxplot und Spannweite

**Befund** (Katalog 5): „daten.md: „Boxplot zeichnen [GYM 7]“ ohne OS-Marke, ohne Sprossenkette; „Spannweite [OS 9]“ gegen Einheitsmarke OS 6 (Eingabe 6).“ Stand heute: offen.

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 35 (Typen Einheit 5): „Boxplot lesen (Median, Quartile, Spannweite, Box) [OS 8–9, GYM 7] · Boxplot zeichnen (Vorrat) [GYM 7] · zwei Boxplots vergleichen (Vorrat)“.
- Z. 153 (Kette „Beurteilen (Einheit 5)“): „… → Diagramm mit Achse ab null skizzieren → Boxplot lesen (Vorrat) → Prüfungshöhe: …“ – keine Sprosse für Zeichnen und Vergleichen, keine eigene Kette.
- Widerspruch Z. 182 (Offene Punkte): „Boxplot: Zeichnen (Quartile bestimmen) nur als Vorrat-Sprosse“ – eine solche Sprosse gibt es nicht.
- Z. 34 (Typen Einheit 4): „Spannweite (auch Dezimalzahlen und große Zahlen) [OS 9]“ gegen Z. 21 (Marken Einheit 4): „OS Kl. 6 · GYM Kl. 6–7 (LS 7, Fundamente 6, Elemente 6) · P10 oft · FHR · …“.

**Gegenprobe (Auftrag Teil 8): die Abweichung „Spannweite [OS 9]“ gegen die Einheitsmarke OS 6 mit beiden Fundstellen aus katalog/_klassen-belege.md, im Wortlaut der Belegdatei:**
- Fundstelle der Typklammer „[OS 9]“, Z. 4276: „  - Typ: Spannweite (auch Dezimalzahlen und große Zahlen) – Mathematik 2023 Kl. 9, S. 112: „Streumaße““ – zur Stelle Z. 4250–4251: „  - Mathematik 2023 Kl. 9, S. 112: „Streumaße“ (Z. 424)“ / „    Ermessen: Streumaße: im Katalog nur die Spannweite (Sek I); als deren Typ gelesen.“ Es ist die einzige Typzeile des Typs; marken-bau.py baut daraus „[OS 9]“ (Probelauf auf c8c16ef: „daten 4: Spannweite (auch Dezimalzahlen und große Zahlen) [OS 9]“, „nichts zu ändern“).
- Fundstelle der Einheitsmarke „OS Kl. 6“, Z. 4290: „  - OS: Kl. 6 (Sekundo 7, 8, 9, 10, Mathematik 2023 6, 8, 9, Schnittpunkt 6, 8, Mathematik heute 6, 7); nicht in die Spanne gerechnet: Sekundo 7 (Reihe beginnt in Klasse 7, Bände 5/6 für BE/BB nicht erschienen)“. Getragen wird die 6 unter anderem von Z. 4246: „  - Mathematik 2023 Kl. 6, S. 128: „Kenngrößen: Maximum, Minimum, Spannweite“ (Z. 301, 302)“ – eine Stelle, die die Spannweite ausdrücklich nennt, deren Typzeile Z. 4275 aber nur den Nachbartyp trägt: „  - Typ: Minimum und Maximum aus Liste, Tabelle, Diagramm – Mathematik 2023 Kl. 6, S. 128: „Kenngrößen: Maximum, Minimum, Spannweite““.
- Weitere Stellen, die die Spannweite nennen und keine Typzeile tragen: Z. 4241 „Sekundo Kl. 8, S. 159: „Mittelwert, Median, Modus undSpannweite““, Z. 4242 „Sekundo Kl. 9, S. 150: „Mittelwert, Median und Spannweite““, Z. 4243 „Sekundo Kl. 10, S. 152: „LVL: Mittelwert, Median, Spannweite und Boxplots““, Z. 4249 „Mathematik 2023 Kl. 8, S. 68: „Maximum, Minimum, Spannweite““, Z. 4268 „Elemente Kl. 7 (Ausgabe 2016), S. 97: „Arithmetisches M itte l-M d a lw e rt-S p a n n w e ite““; Förderhefte Z. 4280–4284 (Sekundo Kl. 6–8, Mathematik 2023 Kl. 8–9).
- Amtlich steht die Spannweite tiefer als Kl. 9: [RLP D] Z. 2998–3001 „Ermitteln und Vergleichen von Kennwerten (auch Minimum, Maximum und Spannweite)“; [LISUM-PH Jg. 7/8] Z. 1511 „Bestimmen und Verändern von Kennwerten (Minimum, Maximum, Spannweite, …)“.

**Ursache und zu entscheiden (kein Handwert):** Die Lesart der Belegdatei (Z. 23) setzt eine Typzeile, „wenn die Zeile einen einzelnen Typ der Einheit nennt“; die Kl.-6-Zeile nennt zwei Typen und ist nur dem ersten zugeordnet (werkzeuge/klassen-belege-daten.py Z. 1450: `typ='Minimum und Maximum aus Liste, Tabelle, Diagramm'`). Die Kl.-9-Stelle „Streumaße“ ist über die Stellenliste als „gilt“ gelesen (werkzeuge/marken-bau-stellen.txt Z. 65, Quelle katalog/_marken-entscheidungen.md Z. 69 „Spannweite ist Einheit 4“). Zu entscheiden ist, ob eine Verzeichniszeile, die mehrere Kenngrößen aufzählt, Typzeile für jede genannte ist. Zwei Wege: (a) Belegdatei – in klassen-belege-daten.py die Stelle Z. 1450 (und ggf. Z. 1577 Mathematik 2023 Kl. 8, Z. 2252 und 2323 Sekundo Kl. 8/9) mit Typliste führen wie Z. 164 (`typ=[…, …]`), dann _klassen-belege.md mit klassen-belege.py neu bauen; (b) Stellenliste – je Stelle zwei Zeilen „gilt“ und „Typ daten 4: Spannweite (auch Dezimalzahlen und große Zahlen)“ (ohne „gilt“ zählte die Stelle nach der Regel der Stellenliste nicht mehr für die Einheit). Wirkung, gemessen mit marken-bau.py --probe in einer Kopie von c8c16ef (nichts im Repo geändert): nur die Kl.-6-Zeile → „[OS 6]“; alle Zeilen, die die Spannweite nennen (Mathematik 2023 Kl. 6 und 8, Sekundo Kl. 8 und 9, Elemente Kl. 7) → „[OS 6–8, GYM 7]“; die Einheitsmarke „OS Kl. 6 · GYM Kl. 6–7 …“ bleibt in beiden Fällen gleich.

**„Boxplot zeichnen [GYM 7]“ ohne OS-Marke – Fundstellen und zu entscheiden:** Einzige Typzeile Z. 4327 „  - Typ: Boxplot zeichnen (Vorrat) – Elemente Kl. 7 (Ausgabe 2025), S. 212: „9.5 Boxplots lesen und erstellen““. Die OS-Stellen der Einheit nennen nur „Boxplots“ ohne Handlung und tragen deshalb nur die Typzeile „Boxplot lesen“: Z. 4294 „Sekundo Kl. 8, S. 165: „Quartile und B oxplots““, Z. 4301 „Mathematik 2023 Kl. 8, S. 69: „Boxplots““, Z. 4307 „Schnittpunkt Kl. 8, S. 196: „5 Boxplots““, Z. 4310 „Mathematik heute Kl. 9, S. 146: „Boxplots““ (Typzeilen Z. 4332, 4334, 4335, 4337); dazu ohne Typzeile Z. 4295 „Sekundo Kl. 8, S. 166: „LVL: Boxplot m it dem C o m p u te r““ und Z. 4306 „Schnittpunkt Kl. 8, S. 192: „4 Quartile““. Zu entscheiden: ob eine Kapitelzeile, die nur den Gegenstand nennt („Boxplots“), für Lesen und Zeichnen gilt. Wirkung im selben Probelauf, wenn die vier OS-Stellen zusätzlich Typzeile „Boxplot zeichnen (Vorrat)“ werden: „[OS 8–9, GYM 7]“ – dieselbe Klammer wie „Boxplot lesen“.

**Vorschlag 5.1 – Erkennungsschritt (einfügen nach Z. 57, „- „Sortiert?“ …“)**

```
- „Welcher Strich ist was?“ – an einem gezeichneten Boxplot die fünf Striche den Wörtern Minimum, unteres Quartil, Median, oberes Quartil und Maximum zuordnen; nichts ablesen, nichts rechnen. Vor Einheit 5 (Boxplot). [RLP F „Vergleichen verschiedener Darstellungsformen (auch Boxplots)“; LS-AA Kl. 7 VII 3]
```

Beleg: [RLP F] Z. 3091–3093 „Vergleichen verschiedener Darstellungsformen (auch Boxplots)“; [Lehrwerk] _klassen-belege.md Z. 4330 „Typ: Boxplot lesen (Median, Quartile, Spannweite, Box) – LS Kl. 7: „3 Boxplots““ und die übrigen Typzeilen „Boxplot lesen“ Z. 4326–4337; die fünf Wörter wie im Kasten Z. 105.

**Vorschlag 5.2 – neue Kette „Boxplot“ (einfügen nach Z. 153)**

```
- Boxplot (Einheit 5, Vorrat): „Welcher Strich ist was?“ ankreuzen (Vorstufe) → die fünf Kennwerte an einem Boxplot über einer beschrifteten Skala ablesen (4×) → Spannweite und Breite der Box aus den abgelesenen Werten → Aussagen zu einem Boxplot prüfen: in der Box liegt die Hälfte der Werte, unter dem unteren Quartil ein Viertel → Quartile einer sortierten Liste bestimmen, Median der unteren und der oberen Hälfte, ungerade Anzahl → gerade Anzahl → Boxplot zu einer sortierten Liste auf einer vorgegebenen Skala zeichnen → aus einer unsortierten Liste, erst sortieren → zwei Boxplots auf einer gemeinsamen Skala vergleichen: Median, Breite der Box, Spannweite → Prüfungshöhe: kein Original in msa, fhr, abi und iqb; Zielmarke nach RLP F („Vergleichen verschiedener Darstellungsformen (auch Boxplots)“) und LISUM-PH Jahrgangsstufe sieben/acht (⑲, ⑳): zu zwei Datenreihen die Boxplots auf einer gemeinsamen Skala zeichnen und die Verteilungen über Median, Box und Spannweite vergleichen.
```

Beleg: [RLP F] Z. 3081–3093 „Darstellen von Daten (auch in Klassen eingeteilt) in Diagrammen (auch Boxplots und Histogramme)“, „Vergleichen verschiedener Darstellungsformen (auch Boxplots)“; [RLP H] Z. 3110–3115 „Analysieren, Interpretieren von … Streumaßen (z. B. Spannweite und Breite der Box bei Boxplots)“; [Lehrwerk] _klassen-belege.md Z. 4323 und 4326–4327 „Elemente Kl. 7 (Ausgabe 2025), S. 212: „9.5 Boxplots lesen und erstellen““ (Typzeilen lesen und zeichnen), Z. 4306–4307 „Schnittpunkt Kl. 8, S. 192: „4 Quartile““, „S. 196: „5 Boxplots““, Z. 4294 „Sekundo Kl. 8, S. 165: „Quartile und B oxplots““, Z. 4311 „LS Kl. 7: … „3 Boxplots““, Förderheft Z. 4343 „Schnittpunkt-Förderheft Kl. 8, S. 57: „Boxplots““; [LISUM-PH Jg. 7/8] Z. 1475 „Darstellung von Daten in Tabellen, Histogrammen, Boxplots, …“, Z. 1553–1561 ⑲ „(auch Boxplots und Histogramme)“, ⑳ „Vergleichen verschiedener Darstellungsformen (auch Boxplots)“; [Prüfung] keine – Suche „Boxplot|Quartil“ über msa-, fhr-, abi- und iqb-Katalog: 0 Treffer (daten.md Z. 159: „Kein Original zu Boxplot“).

**Vorschlag 5.3 – Kette „Beurteilen“ ohne Boxplot-Sprosse (ersetzt Z. 153)**

```
- Beurteilen (Einheit 5): Achsenanfang ankreuzen (Vorstufe) → Aussage mit einem Wert prüfen (4×) → Aussage mit Vergleich zweier Werte (Anstieg, Rückgang) → „mehr als die Hälfte“, „um ein Drittel“ nachrechnen → „jede 15.“ umrechnen → zwei Teilaussagen getrennt prüfen → abgeschnittene Achse erklären → Verdopplung der Säule gegen Veränderung des Werts → Trend und Fortschreibung → Diagramm mit Achse ab null skizzieren → Prüfungshöhe: eine Aussage zum Verlauf prüfen und die abgeschnittene Achse als Grund der Verzerrung benennen (P10-Form 2019-OS-K5c, Niveau III, Stern); daneben die Verzerrung allein an einer Preisachse erklären (2026-FOR-K3e, Niveau III) und die unzutreffende Aussage eines Zeitungsartikels berichtigen (2018-OS-K3d, Niveau II, Stern).
```

Wortgleich Z. 153 bis auf die gestrichene Sprosse „→ Boxplot lesen (Vorrat)“, die in 5.2 aufgeht.

Beleg: [Prüfung] msa 2019-OS-K5c, 2026-FOR-K3e, 2018-OS-K3d (unverändert); [RLP G] Z. 3102–3104 „Erkennen von typischen Fehlern und Manipulationen bei grafischen Darstellungen“ (Block Z. 3095–3106, Randbuchstabe G in Z. 3102).

**Kein Beleg gefunden:**
- Quartilregel – Daten so wählen, dass die in den Lehrwerken gebräuchlichen Quartilregeln dasselbe Quartil ergeben (so gebaut im Blatt der Eingabe 6): kein Beleg gefunden (die Verzeichniszeilen nennen keine Regel, RLP und Planungshilfe keine, die Prüfungskataloge kein Quartil) – kein Vorschlag.

**Hinweise.** Z. 182 („nur als Vorrat-Sprosse“) stimmt mit 5.2 wieder; „(Einheit 5, Vorrat)“ folgt der Klammerform, die _pruef_katalog.py seit 10d liest. Die Mindeststoff-Zeile Z. 146 („Vorrat: Einheit 5 ganz (F: Boxplots …)“) bleibt.

## Katalogbefund 6 – terme.md Einheit 4 und binomische-formeln.md Vorstufen

**Befund** (Katalog 6): „terme.md Einheit 4 ohne Begründen- und Kontexttyp; binomische-formeln.md Vorstufen verlangen Rechnung (Eingabe 10).“ Stand heute: offen.

**Was fehlt oder widerspricht, im Wortlaut der Einträge:**
- terme.md Z. 24: „Einheit 4: gemeinsamen Zahlfaktor ausklammern · Variable ausklammern · Zahl und Variable ausklammern · Umkehrung prüfen (ausmultiplizieren als Probe) · Fehler finden.“ – als einzige Einheit des Eintrags ohne „Begründen“ und ohne Sachkontext; Z. 76 (Kette) endet ohne Figur und Kontext.
- binomische-formeln.md Z. 37: „„Ist das ein Quadrat?“ – zu Termen ankreuzen, ob sie Quadrate sind (x², 16, 49x², 6x, 10), und die Wurzel daneben schreiben; nichts faktorisieren.“ und Z. 38: „„Passt das Mittelglied?“ – zu x² + 14x + 49 die Wurzeln x und 7 notieren, das doppelte Produkt bilden und ankreuzen, ob es das Mittelglied ist; nichts faktorisieren.“ – beide verlangen ein Ergebnis (Wurzel, Produkt), obwohl die Überschrift Z. 32 sie als Vorstufe führt (Prompt 2.3 a, Befund Prompt 23: „die Vorstufe setzt den Schritt ohne Ergebnis um, das Ausrechnen wird eigene Hauptnummer“).

**Vorschlag 6.1 – terme.md, Typzeile Einheit 4 (ersetzt Z. 24)**

```
Einheit 4: gemeinsamen Zahlfaktor ausklammern · Variable ausklammern · Zahl und Variable ausklammern · Umkehrung prüfen (ausmultiplizieren als Probe) · Flächeninhalt einer Figur aus zwei Rechtecken mit gemeinsamer Seite als Summe der Teilflächen und als Produkt mit Klammer angeben · gleichwertige Sachterme mit gemeinsamem Faktor erkennen (Rabatt auf jeden Preis einzeln oder auf die Summe) · Fehler finden · Begründen (warum ausgeklammerter und ausmultiplizierter Term gleichwertig sind – am Rechteckbild und durch Einsetzen einer Zahl).
```

Beleg: Figur – [Prüfung] msa 2025-OS-B1i (Rechteck der Breite a, in Teile der Höhen b und c geteilt, Ergebnis „A = a · (b + c)“, Fehlerquelle Umfangsterm; Typ „Term zu Figur angeben“, geführt in flaechen.md); [RLP E] Z. 2746–2749 „Angeben von passenden Situationen und grafischen Darstellungen zu vorgegeben Termen und Gleichungen“; [LISUM-PH Jg. 7] Z. 413–414 „Erklären von Termumformungen und Erläutern von Fehlern an bzw. mit geometrischen Figuren und Kontexten“. Sachterm – [Prüfung] msa 2015-OS-K2a (drei Rabattterme, darunter „1/5 · (36 € + 7,50 €)“ und „20 · (12 € + 12 € + 12 € + 7,50 €) / 100“ als richtig beurteilen; Typ „Term zu Sachtext angeben“, geführt in prozentrechnung.md). Begründen – [RLP D] Z. 2727–2733 „Begründen (auch anschaulich) der Gleichheit von Zahlentermen … mithilfe der bekannten Rechengesetze (Kommutativ-, Assoziativ- und Distributivgesetz) (z. B. 12 ∙ 7 = 10 ∙ 7 + 2 ∙ 7)“; [LISUM-PH Jg. 7] Z. 412 „Erkennen, Begründen und Korrigieren fehlerhafter Termumformungen“; [Lehrwerk] Einheit 4 in allen Reihen mit Stelle, _klassen-belege.md Z. 2993–3001 (etwa „LS Kl. 7: … „3 Ausmultiplizieren und Ausklammern““, „Schnittpunkt Kl. 8, S. 8: „1 Ausmultiplizieren. Ausklammern““).

**Vorschlag 6.2 – terme.md, Kette Einheit 4 (ersetzt Z. 76)**

```
- Ausklammern (Einheit 4): gemeinsamen Zahlfaktor bei zwei Gliedern (4×) → gemeinsame Variable → Zahl und Variable zusammen → ein Glied ist selbst der Faktor, in der Klammer bleibt die Eins → drei Glieder → Probe durch Ausmultiplizieren → Figur aus zwei Rechtecken mit gemeinsamer Seite: Flächeninhalt als Summe der Teilflächen und als gemeinsame Seite mal Summe der anderen Seiten → gleichwertige Sachterme erkennen: Rabatt auf jeden Preis einzeln gegen Rabatt auf die Summe → Fehler finden: Faktor nur aus einem Glied gezogen → Prüfungshöhe: kein P10-Original; Zielmarke nach RLP F (Distributivgesetz) und LISUM-PH Jahrgangsstufe sieben, Block „Terme äquivalent umformen“ („Klammer mit Faktor vor oder nach der Klammer auflösen und ausklammern“): einen dreigliedrigen Term mit gemeinsamem Zahl- und Variablenfaktor ausklammern und die Probe durch Ausmultiplizieren führen.
```

Neu sind die beiden Sprossen vor „Fehler finden“; Prüfungshöhe wortgleich Z. 76.

Beleg: wie 6.1 (2025-OS-B1i, 2015-OS-K2a, RLP E Z. 2746–2749, LISUM-PH Jg. 7 Z. 410–414); [RLP F] Z. 2757–2758 „Umformen von Termen (auch Distributivgesetz zum Ausmultiplizieren von Summen)“.

**Vorschlag 6.3 – binomische-formeln.md, Erkennungsschritt „Ist das ein Quadrat?“ (ersetzt Z. 37)**

```
- „Ist das ein Quadrat?“ – zu Termen ankreuzen, ob sie Quadrate sind (x², 16, 49x², 6x, 10); keine Wurzel hinschreiben, nichts faktorisieren. Vor Einheit 3. [Serlo 1499; Schnittpunkt Kl. 8, S. 16]
```

Beleg: [Lehrwerk] _klassen-belege.md Z. 3533 „Schnittpunkt Kl. 8, S. 16: „4 Faktorisieren mit binomischen Formeln““, Z. 3538 „Elemente Kl. 8 (Ausgabe 2016), S. 58: „1.10 Faktorisieren einer Summe““, Förderheft Z. 3542 „Schnittpunkt-Förderheft Kl. 8, S. 6: „Faktorisieren mit binomischen Formeln““; [RLP G] Z. 2839–2841 „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter Nutzung der binomischen Formeln)“. Die Wurzel selbst ist Blatt-0-Fertigkeit des Eintrags (Z. 29: „Quadratzahlen bis 15² erkennen und Quadratwurzeln daraus (√49 = 7); … – Einheit 2 und 3“).

**Vorschlag 6.4 – binomische-formeln.md, Erkennungsschritt statt „Passt das Mittelglied?“ (ersetzt Z. 38)**

```
- „Welche Glieder könnten Quadrate sein?“ – in dreigliedrigen Termen (x² + 14x + 49) die beiden Glieder einkreisen, die Quadrate sein könnten, und das Mittelglied unterstreichen; nichts ausrechnen, nichts faktorisieren. Vor Einheit 3. [Serlo 1499; Elemente Kl. 8, S. 58]
```

Beleg: wie 6.3; die Prüfung des Mittelglieds bleibt Typ der Einheit (Z. 21 „erste Formel rückwärts mit Prüfung des Mittelglieds (doppeltes Produkt der Wurzeln)“) und wird in 6.5 eigene Sprosse.

**Vorschlag 6.5 – binomische-formeln.md, Kette „Faktorisieren“ (ersetzt Z. 88)**

```
- Faktorisieren (Einheit 3): „Ist das ein Quadrat?“ und „Welche Glieder könnten Quadrate sein?“ ankreuzen (Vorstufe) → dritte Formel rückwärts, x² minus Quadratzahl (4×) → Mittelglied prüfen: die Wurzeln der beiden Quadrate aufschreiben, ihr doppeltes Produkt bilden und mit dem Mittelglied vergleichen, noch nicht faktorisieren → erste Formel rückwärts mit geprüftem Mittelglied → zweite Formel rückwärts, Minus im Mittelglied → Vorzahl vor x², Quadrat von zwei x → erst gemeinsamen Faktor ausklammern, dann Formel → kein Binom erkennen und begründen (Mittelglied passt nicht, Summe zweier Quadrate) → Probe durch Ausmultiplizieren → Anwendung: Produktform gleich null lösen (quadratische-gleichungen.md Einheit 2) → quadratische Ergänzung (Vorrat) → Prüfungshöhe: Term mit gemeinsamem Faktor und binomischer Formel vollständig faktorisieren und die Probe führen (kein P10-Original; RLP G, LS-AA Kl. 8 II 4).
```

Neu: Vorstufenname und die Sprosse „Mittelglied prüfen“ (das Ausrechnen aus der alten Vorstufe als eigene Hauptnummer); sonst wortgleich Z. 88.

Beleg: wie 6.3; [Prüfung] kein Original zum Faktorisieren mit binomischer Formel (binomische-formeln.md Z. 91: „Kein Original verlangt die dritte Formel, das Faktorisieren oder Terme mit zwei Variablen“; Faktorisieren nur als Alternative in 2020-OS-K3e).

**Hinweise.** Neue Typnamen in 6.1 sind nach der Übernahme in klassen-belege-typen.txt/_klassen-belege.md nicht vorhanden (abgeleitet, neu bauen). Die Offene-Punkte-Zeile terme.md Z. 91 („die Zielmarke der Einheiten 2 bis 4 stützt sich nicht auf ein Original“) bleibt richtig – 2025-OS-B1i und 2015-OS-K2a sind Nebenbelege anderer Typen, keine Originale der Einheit.

## Katalogbefund 7 – prozentrechnung.md: Darstellungen der Einheit 5 und Kasten

**Befund** (Katalog 7): „prozentrechnung.md „Für schwache Schüler“: keine Darstellung für Faktor, Brutto/Netto, Prozentpunkte, Steigung; Kasten Einheit 5 über fünf Zeilen (Eingabe 3).“ Stand heute: offen.

**Was fehlt oder widerspricht, im Wortlaut des Eintrags:**
- Z. 103: „- Veränderung (Einheit 5): „um oder auf“ (Vorstufe) → Prozentwert berechnen und dazu oder weg (4×) → Faktor 1,2 und 0,8 → Veränderung in Prozent aus zwei Werten → alter Wert aus neuem Wert (auf 80 %: neu : 0,8) → Brutto/Netto → Prozentpunkte → Steigung in Prozent → Prüfungshöhe: …“ – die Ketten 1 bis 4 nennen je Sprosse den Streifen (Z. 99–102), die Kette 5 keine Darstellung; die Steigung steht vor einer Prüfungshöhe anderer Art (die Zielmarke Z. 124 nennt 2025-OS-K4b, die Kette nicht).
- Z. 72–79 (Kasten Einheit 5): fünf Regel- und Beispielzeilen plus Formelsammlung-Zeile; die Erhöhung belegt allein zwei Zeilen (Z. 73 Regel, Z. 74 Beispiel).

**Vorschlag 7.1 – Kette Einheit 5 mit Darstellung je Sprosse (ersetzt Z. 103)**

```
- Veränderung (Einheit 5): „um oder auf“ (Vorstufe) → Prozentwert am Streifen berechnen und dazu oder weg (4×) → Faktor 1,2 und 0,8, dargestellt am Streifen, der über hundert Prozent hinaus verlängert oder unter hundert Prozent verkürzt wird → Veränderung in Prozent aus zwei Werten, beide als Streifen untereinander, der alte ist hundert Prozent → alter Wert aus neuem Wert (auf 80 %: neu : 0,8), am Streifen rückwärts auf hundert Prozent → Brutto/Netto am Streifen: der Nettopreis ist hundert Prozent, der Bruttopreis der verlängerte Streifen bis hundertneunzehn oder hundertsieben Prozent → Prozentpunkte an zwei Anteilsstreifen untereinander: der Unterschied als Abschnitt in Prozentpunkten, derselbe Unterschied bezogen auf den alten Anteil in Prozent → Steigung in Prozent an einer Skizze des Steigungsdreiecks: waagerechte Strecke und Höhe beschriftet, nicht die schräge Seite → Prüfungshöhe: prozentuale Veränderung zweier Preise, Differenz auf den alten Wert bezogen und auf eine Dezimalstelle gerundet (P10-Form 2026-FOR-K3c, 2022-OS-K4b, 2016-OS-K2c); dazu der Wert nach einer Erhöhung (2024-OS-B1e), der Preis nach Rabatt über den Faktor (2015-OS-K2b) und die Steigung als Lückensatz deuten und gegen eine zulässige Steigung prüfen (2025-OS-K4b).
```

Neu: die Darstellung in sechs Sprossen und die Steigungs-Prüfungshöhe am Ende (die Kette endet dann nicht mehr mit einer Sprosse ohne Höhe); Ziffern nur dort, wo Z. 103 sie schon trägt.

Beleg: [RLP E] Z. 1897–1900 „Nutzen, Darstellen und Beschreiben von Strategien und Gesetzen bei der Prozentrechnung, z. B. mithilfe des Prozentstreifens (auch Dreisatz und Verhältnisgleichungen)“, Z. 1916 „Nutzen von Prozentsätzen als Operatoren“; [RLP F] Z. 1974–1977 „Nutzen, Darstellen und Beschreiben von Strategien und Gesetzen bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, …)“; [LISUM-PH Jg. 7] Z. 255 „Darstellen von Prozentsätzen, Prozentwerten und Grundwerten auf einem Prozentstreifen“, Z. 301 „Berechnen von Sachkontexten mit vermehrtem oder vermindertem Grundwert“, Z. 326 „Brutto- und Nettopreise berechnen, Mehrwertsteuer berechnen …“; [Lehrwerk] _klassen-belege.md – Faktor: Z. 753 „Typ: neuer Wert über Faktor (1,2; 0,8) – Sekundo Kl. 9, S. 88: „Prozentfaktor““; vermehrter und verminderter Grundwert: Z. 723 „Sekundo Kl. 8, S. 93: „Vermehrter und verminderter G rundwert““, Z. 736 „Schnittpunkt Kl. 8, S. 129: „2 Vermehrter und verminderter Grundwert““, Förderhefte Z. 757, 758, 760; Brutto/Netto: Z. 750–752 (Mathematik 2023 Kl. 7, S. 68; Sekundo Kl. 7, S. 94; Kl. 8, S. 95); Prozentpunkte: Z. 749 „Typ: Prozentpunkte gegen Prozent – Elemente Kl. 7 (Ausgabe 2016), S. 67: „Prozent oder Prozentpunkte - was ist hier gemeint?““; Steigung: Z. 754 „Typ: Steigung in Prozent deuten und berechnen – Sekundo Kl. 10, S. 112: „LVL: Steigung in Prozent““; [Prüfung] msa 2015-OS-K2b und 2024-OS-B1e (Faktor), 2016-OS-K2c, 2022-OS-K4b, 2026-FOR-K3c (Veränderung), 2019-OS-K5a (72 % und 95 % derselben 1 200 Befragten; Fehlerquelle Prozentpunkte als Anzahl), 2025-OS-K4b (Rampe; Stammskizze mit 170 cm waagerecht und 16 cm Höhe), 2017-GYM-K5b (19 % Umsatzsteuer auf alle Beträge – brutto). Die Darstellungsform ist für den Streifen allgemein amtlich (RLP E, LISUM-PH) und für die Steigung durch die Stammskizze von 2025-OS-K4b belegt; „zwei Anteilsstreifen untereinander“ für Prozentpunkte ist Ermessen auf dem allgemeinen Streifen-Beleg.

**Vorschlag 7.2 – Kasten Einheit 5, Erhöhung und Beispiel in einer Zeile (ersetzt Z. 73 und 74)**

```
    Erhöhung um p %: neuer Wert = alter Wert · (1 + p/100); Senkung: · (1 − p/100).      250 € um 12 % erhöht: 250 · 1,12 = 280 €; gesenkt: 250 · 0,88 = 220 €
```

Der Kasten hat danach vier Regelzeilen (Erhöhung, Veränderung in Prozent, Prozentpunkte, Steigung, jede mit Beispiel in derselben Zeile) und die Formelsammlung-Zeile; Z. 75–79 bleiben wortgleich. Zahlen und Rechnung unverändert (250 · 1,12 = 280; 250 · 0,88 = 220), die Kastenzahlen-Sperre ändert sich nicht.

Beleg: [Prüfung] msa 2024-OS-B1e (3,50 € um 20 % erhöht → 4,20 €), 2015-OS-K2b (20 % Rabatt, Faktor 0,8); [RLP E] Z. 1916 „Nutzen von Prozentsätzen als Operatoren“; [LISUM-PH Jg. 7] Z. 301; [Lehrwerk] _klassen-belege.md Z. 753 (Sekundo Kl. 9, S. 88 „Prozentfaktor“).

**Hinweise.** Die Vorlage (blattbau) setzt den Streifen nur bis hundert Prozent; das Blatt der Eingabe 3 hat deshalb für Faktor und Brutto/Netto einen Zahlenstrahl gezeichnet (Lesezettel). Ein Streifen über hundert Prozent ist ein Baustein-Wunsch an die Vorlage, keine Katalogzeile. Die Mindeststoff-Zeile Z. 96 („Faktor 1,2/0,8, Veränderung in Prozent, Brutto/Netto, Prozentpunkte, Steigung sind F oder Vorrat“) bleibt.

## Katalogbefund 8 – kurvenuntersuchung.md: Mindestgrad und Skizze aus Eigenschaften

**Befund** (Katalog 8): „kurvenuntersuchung: Mindestgrad und Skizze aus Eigenschaften nur aus LK-Quellen, ohne LK-Vermerk (Eingabe 9).“ Stand heute: offen (letzte Änderung am Eintrag 3e956a5, Nachzug auf die Katalogzeilen vom 27.09.; der LK-Vermerk fehlt weiter).

**Befund an den Katalogen:** Beide Typen haben je zwei Zeilen, alle aus dem Leistungskurs- bzw. erhöhten Niveau: abi 2023-bebb-lk-A1.1a und 2023-bebb-lk-A1.1b (papier 2023-bebb-lk, „Dublette von: 2023MerhoehtAAnalysis11-a“ bzw. „-b“), iqb 2023MerhoehtAAnalysis11-a und 2023MerhoehtAAnalysis11-b (papier 2023-iqb-ea, Standardbezug „K1 II, K6 I“ bzw. „K4 II, K6 I“). Keine Zeile aus einem Grundkursheft oder dem grundlegenden Pool.

**Was fehlt, im Wortlaut des Eintrags:**
- Z. 17 (Lerneinheit 4): „… einen möglichen Graphen zu vorgegebenen Nullstellen, Extrem- und Wendestellen skizzieren (Wendestelle als Extremstelle von f'); … Mindestgrad aus Eigenschaften der Ableitung; …“; Z. 21 (Niveaustufung): „GK = alle fünf, mit Produkten aus Polynom und e-Funktion; LK = zusätzlich Wurzel-, ln-, sin/cos-Funktionen und Ortskurven …“.
- Z. 28 (Typen Einheit 4): „Mindestgrad einer ganzrationalen Funktion aus Eigenschaften der Ableitung begründen (2)“, „Graphen zu vorgegebenen Nullstellen, Extrem- und Wendestellen skizzieren (2)“ – ohne Vermerk.
- Z. 130 (Kette Einheit 4): „… skizzieren, die Wendestelle als Extremstelle von f' lesen (abi 2023-bebb-lk-A1.1b, iqb 2023MerhoehtAAnalysis11-b) → den Mindestgrad aus den Eigenschaften der Ableitung begründen (abi 2023-bebb-lk-A1.1a) → …“ – dagegen tragen gleichartige Sprossen der Einheiten 2 und 3 den Vermerk: Z. 128 „(LK; abi 2022-bebb-lk-B2.1b)“, Z. 129 „(LK; abi 2022-bebb-lk-B2.2d)“ und „(LK; iqb 2019MerhoehtAAnalysis2-b)“.
- Z. 138 (Zielmarke Einheit 4): „iqb: Skizze und Mindestgrad in Teil A (2023MerhoehtAAnalysis11-a/b)“.

**Gegenbeleg, der beim Urteil mitzudenken ist (kein eigener Vorschlag):** Der Stoff steht für beide Kursarten im Plan – [GOST BE] quelle-rlp-gost-be-2022-mathematik.txt Z. 1189 „Ableitungsgraphen aus Funktionsgraphen entwickeln und umgekehrt, Q1/2“ unter „Grundkursfach und Leistungskursfach“ (Z. 1162); [GOST-OHiMi] quelle-rlp-gost-2022-mathematik-anlage-ohimi.txt Z. 128–130 („… für das Grund- und Leistungskursfach jeweils ausgewiesenen Funktionsklassen“), Z. 143 „qualitative Beschreibung des Verlaufs des Funktionsgraphen“, Z. 151–152 „Rekonstruktion von Funktionsgleichungen aus graphischen Darstellungen bzw. Funktionseigenschaften“, Z. 159–160 „Bestimmung des qualitativen Verlaufs des Funktionsgraphen der Ableitungsfunktion aus dem Funktionsgraphen der Funktion (und umgekehrt)“. Der Kasten Z. 91 führt „Skizze aus Eigenschaften“ deshalb als „Auswendig (Teil A)“. Der Vermerk unten ist darum ein Beleg-Vermerk (geprüft nur LK/erhöht) in der Form, die der Eintrag für solche Fälle schon benutzt („(LK; …)“); ob das Blatt die Sprosse bei GK weglässt (so die Lesart der Eingabe 9 für die übrigen „(LK; …)“-Sprossen), ist damit mitentschieden – der Chat kann stattdessen „nur LK geprüft“ als bloße Auskunft wählen.

**Vorschlag 8.1 – Lerneinheit 4 (Z. 17), zwei Einfügungen**

```
alt: einen möglichen Graphen zu vorgegebenen Nullstellen, Extrem- und Wendestellen skizzieren (Wendestelle als Extremstelle von f');
neu: einen möglichen Graphen zu vorgegebenen Nullstellen, Extrem- und Wendestellen skizzieren (Wendestelle als Extremstelle von f'; LK);
alt: Mindestgrad aus Eigenschaften der Ableitung;
neu: Mindestgrad aus Eigenschaften der Ableitung (LK);
```

Beleg: abi 2023-bebb-lk-A1.1a, 2023-bebb-lk-A1.1b; iqb 2023MerhoehtAAnalysis11-a, 2023MerhoehtAAnalysis11-b.

**Vorschlag 8.2 – Niveaustufung (Z. 21), Einfügung am Satzende**

```
alt: LK = zusätzlich Wurzel-, ln-, sin/cos-Funktionen und Ortskurven (Ortskurven ohne Prüfungsbeleg in der Rohdatei – Vermerk „kein Original“).
neu: LK = zusätzlich Wurzel-, ln-, sin/cos-Funktionen und Ortskurven (Ortskurven ohne Prüfungsbeleg in der Rohdatei – Vermerk „kein Original“); Mindestgrad aus Eigenschaften der Ableitung und Graph zu vorgegebenen Nullstellen, Extrem- und Wendestellen (Einheit 4) nur mit LK-Beleg (2023-bebb-lk-A1.1a/b, Pool erhöht 2023) – der Stoff steht für beide Kursarten in der Anlage OHiMi 2.2.
```

Beleg: wie 8.1; [GOST-OHiMi] Z. 143, 151–152, 159–160.

**Vorschlag 8.3 – Typzeile Einheit 4 (ersetzt Z. 28)**

```
Einheit 4: Graphen einer Funktion in ein Koordinatensystem einzeichnen (5) — Nachweis: Mindestgrad einer ganzrationalen Funktion aus Eigenschaften der Ableitung begründen (2; LK – abi 2023-bebb-lk-A1.1a und seine Poolvorlage iqb 2023MerhoehtAAnalysis11-a) · Gemeinsamen Punkt zweier Graphen über gleiche Flächeninhalte indirekt begründen (1; Ermessen, siehe Offene Punkte) · Logarithmus einer Exponentialfunktion als lineare Funktion nachweisen und Steigung und Achsenabschnitt angeben (1; Ermessen, siehe Offene Punkte) — Deutung: Graphen zu vorgegebenen Nullstellen, Extrem- und Wendestellen skizzieren (2; LK – abi 2023-bebb-lk-A1.1b und iqb 2023MerhoehtAAnalysis11-b) · Aussagen über die Normale an der Wendestelle und den Wertebereich der Ableitung beurteilen (1) · Graphen skizzieren und Aussage über die Anzahl gemeinsamer Punkte von Tangente und Graph beurteilen (1) · Lage eines Punktes aus Bedingungen an Funktionswert und Ableitung am Graphen beschreiben (1) · Lage zweier Graphen aus dem Graphen ihrer Differenzfunktion beschreiben (1) · Wendepunkt mit negativer Steigung am Graphen markieren und begründen (1) · Werte für einen Ableitungswert und eine Wendestelle am Graphen ablesen (1). Dazu: Fehler finden (Graph von f' als Graph von f gelesen; an der Wendestelle ein Extrempunkt gezeichnet; Ableitungswert als Funktionswert abgelesen) · Begründen (warum die Nullstellen von f' unter den Hoch- und Tiefpunkten von f liegen; warum der Graph von f' einen Grad einfacher ist).
```

Nur die beiden Klammern „(2)“ sind erweitert; Zählung Z. 30 unberührt.

Beleg: abi-katalog.csv 2023-bebb-lk-A1.1a/b, iqb-katalog.csv 2023MerhoehtAAnalysis11-a/b (Felder papier, bemerkung wie oben).

**Vorschlag 8.4 – Kette Einheit 4 (ersetzt Z. 130)**

```
- Graph und Ableitungsgraph (Einheit 4): „steigt, fällt, waagerecht“ und die Vorzeichenleiste (Vorstufe, Grundvorstellung) → zu einem gezeichneten Graphen von f die Nullstellen von f' markieren und das Vorzeichen von f' je Abschnitt eintragen (Grundfall, viermal) → Werte für einen Ableitungswert und eine Wendestelle am Graphen ablesen (abi 2022-bebb-gk-A1.2a) → einen Punkt mit vorgegebenen Bedingungen an f' und f'' auf dem Graphen markieren und begründen (abi 2022-bebb-gk-A1.2b) → Graphen von f und f' aus berechneten Punkten in ein vorgegebenes Koordinatensystem einzeichnen, Extremstellen von f als Nullstellen von f' (abi 2020-be-gk-B2.2d, 2019-be-gk-B2.1f) → einen möglichen Graphen zu vorgegebenen Nullstellen, Extrem- und Wendestellen skizzieren, die Wendestelle als Extremstelle von f' lesen (LK; abi 2023-bebb-lk-A1.1b, iqb 2023MerhoehtAAnalysis11-b) → den Mindestgrad aus den Eigenschaften der Ableitung begründen (LK; abi 2023-bebb-lk-A1.1a, iqb 2023MerhoehtAAnalysis11-a) → die Lage zweier Graphen aus dem Graphen ihrer Differenz beschreiben (iqb 2018MgrundlegendBAnalysisWTR-1f) → Prüfungshöhe: Aussagen über die Normale an der Wendestelle und den Wertebereich der Ableitung beurteilen (abi 2024-bebb-gk-B2.1d, Niveau III) und eine Aussage über gemeinsame Punkte von Tangente und Graph an der eigenen Skizze beurteilen (abi 2023-bebb-gk-B2.2e, Niveau III); fhr-Zielmarke: keine – der RLP FOS führt nur „grafische Darstellung“ und „graphisches Differenzieren“, die Rohdatei kein fhr-Original in dieser Einheit.
```

Neu: „LK;“ in zwei Klammern und die fehlende Poolvorlage 2023MerhoehtAAnalysis11-a an der Mindestgrad-Sprosse; sonst wortgleich Z. 130.

Beleg: wie 8.3.

**Vorschlag 8.5 – Zielmarke Einheit 4 (Z. 138), Ausschnitt**

```
alt: abi: Skizze aus Eigenschaften und Aussage beurteilen (2023-bebb-gk-B2.2e, 2023-bebb-lk-A1.1b), Graphen von f und f' einzeichnen (2020-be-gk-B2.2d); iqb: Skizze und Mindestgrad in Teil A (2023MerhoehtAAnalysis11-a/b).
neu: abi: Skizze und Aussage beurteilen (2023-bebb-gk-B2.2e), Skizze aus vorgegebenen Stellen nur im LK (2023-bebb-lk-A1.1b), Graphen von f und f' einzeichnen (2020-be-gk-B2.2d); iqb: Skizze und Mindestgrad in Teil A, nur erhöht (2023MerhoehtAAnalysis11-a/b).
```

Beleg: wie 8.3; abi 2023-bebb-gk-B2.2e (Skizze aus berechneten Punkten H(3 | 4), W(4 | 2), T(5 | 0), Grundkurs) als GK-Seite der Einheit.

**Hinweise.** Teil 4 Punkt 7 zieht die Sek-II-Einträge auf den CAS-Nachtrag nach; kommt dabei eine Zeile in kurvenuntersuchung.md Einheit 4 dazu, verschieben sich Zählung (Z. 30) und die Wortlaute von Z. 28 und 130 – die Vorschläge 8.3 und 8.4 sind dann auf den neuen Stand zu setzen (nur die Klammern ändern sich).

## Sek-II-Nachzug (Teil 4 Punkt 7)

Folgt nach dem CAS-Nachtrag.
