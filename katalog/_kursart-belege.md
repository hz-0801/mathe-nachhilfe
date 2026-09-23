# Belege der Kursart je Lerneinheit und Haupttyp (Sekundarstufe II)
Stand 2026-09-24, Katalog auf Commit 72325d0.
Erzeugt im Auftrag `archiv/auftrag-niveaustufen-belege.md` aus den 44 Sek-II-Einträgen (`katalog/index.md`, Tabelle Sekundarstufe II), den vier Geltungstabellen `abitur/abi-be-gk-geltung.md`, `abi-be-lk-geltung.md`, `abi-bb-gk-geltung.md`, `abi-bb-ea-geltung.md`, `quellen/quelle-rlp-gost-be-2022-mathematik.txt`, `quellen/quelle-rlp-gost-bb-2022-mathematik.txt` sowie `abitur/abi-katalog.csv`, `abitur/iqb-katalog.csv`, `fhr/fhr-katalog.csv` und `themen.csv`; abgeleitet, nie von Hand ändern. Vorschlagsliste für die LK-Marke, die der Unterrichtsblatt-Prompt ab v4.3 braucht: was Geltungstabellen, Rahmenlehrpläne der gymnasialen Oberstufe und die Prüfungsform je Lerneinheit und je Haupttyp hergeben. Kein Eintrag wird geändert, nichts wird entschieden; eine Einheit, für die ein Plantext keine Stelle hergibt, bleibt dort ohne Stelle – das ist ein Ergebnis, kein Mangel.

Quellen und ihre Lesart:
- Geltung: die vier Geltungstabellen führen je Zielprüfung Thema und ja/nein. Die Brücke vom Eintrag zum Thema ist `themen.csv` (Spalte `kanonisch` → `thema`); ein Eintrag kann mehrere Themen tragen. Zitiert wird die Tabellenzeile wortgleich mit ihrer Zeilennummer; fehlt das Thema in einer Tabelle, steht „nicht geführt“.
- `quellen/quelle-rlp-gost-be-2022-mathematik.txt` – Berlin, Kapitel „Eingangsvoraussetzungen und abschlussorientierte Standards“, § 3.2.2: je Leitidee zuerst ein Block „Grundkursfach und Leistungskursfach“, danach ein Block „Zusätzlich: Leistungskursfach“. Der Text ist einspaltig; zitiert wird die Standardzeile ohne ihren Aufzählungsstrich und ohne die Kurshalbjahresangabe am rechten Rand.
- `quellen/quelle-rlp-gost-bb-2022-mathematik.txt` – Brandenburg, Kapitel „Inhaltsbezogene Kompetenzen“: je Kurshalbjahr Q1 bis Q4 zuerst ein Block „Grund- und Leistungskursfach“, danach ein Block „Zusätzlich im Leistungskursfach“. Der Text ist zweispaltig (links „Inhaltsbezogene Kompetenzen“, rechts „Inhalte“); die Spaltengrenze wird aus der Lage der Aufzählungsstriche in der Umgebung der Zeile bestimmt, zitiert wird eine der beiden Spalten ohne ihren Aufzählungsstrich und ohne den Leitideencode.
- Beide Plantexte trennen Wörter am Zeilenende. Ein Zitat über zwei Zeilen wird wortgleich wiedergegeben; die Silbentrennung bleibt stehen. Jedes Zitat ist ein zusammenhängender Ausschnitt genau einer Zeile des Quelltexts; die Zeilennummern sind nachgeschlagen, nicht geschätzt.
- Prüfungsform: die Kursart einer Katalogzeile folgt aus ihrem `papier`. GK sind `-gk`-Hefte (be-gk, bb-gk) und die Pool-Stapel grundlegenden Niveaus (`-ga`), LK sind `-lk`- und `-ea`-Hefte und die Pool-Stapel erhöhten Niveaus. `fhr` kennt keine Kursart (Fachoberschule) und wird nur mit der Zahl seiner Zeilen genannt.
- `katalog/<eintrag>.md` – Zeilennummern zählen ab 1 in der Datei. Die Kursartmarke des Eintrags wird in der Zeile der Lerneinheit gesucht (Wörter „LK-Zusatz“, „GK-Kern“, „nur be-lk und bb-ea“, „nur LK“, „nur GK“, „Leistungskursfach“, „Grundkursfach“, „LK“, „GK“); ein „…“ am Ende zeigt, dass der Ausschnitt gekürzt ist.

Lesart der Zuordnung: Die Kursart einer Einheit ist die Kursart des Blocks, in dem der Standard steht, der den Inhalt der Einheit nennt – je Land eigens, weil die beiden Länder verschieden schneiden. Wo ein Land den Inhalt gar nicht nennt, steht „keine Stelle“; wo die Zuordnung eine Auslegung verlangt, steht „Ermessen:“ mit der Begründung. Die Datei nennt Kursarten; sie setzt keine Marke im Katalog und formuliert keine Prompt-Regel.

Spanne (Zeile d je Eintrag): „kein Planinhalt“, wenn die Geltung viermal nein ist; sonst „ja“, wenn der Eintrag Einheiten oder Typenzeilen beider Kursarten hat, „nur LK“, wenn nichts im Grundkurs liegt, „nur GK“, wenn nichts im Leistungskurs liegt.

## Zahlen
Einträge gesamt: 44 (die 44 Sek-II-Einträge aus `katalog/index.md`, Tabelle Sekundarstufe II).
Lerneinheiten gesamt: 155.
Spanne ja: 37; nur LK: 5; nur GK: 0; kein Planinhalt: 2.
Einträge ohne jede Stelle im GOST-Text: ableitungsgraph-und-funktionsgraph.
Ermessensfälle gesamt: 45.
Befunde gesamt: 7 in 7 Einträgen.
Geprüfte Zitate beim Bau: 158 Stellen im Berliner Plan, 149 im Brandenburger Plan, 127 Kursartmarken in den Einträgen.

### ableitung-und-aenderungsrate
- Geltung je Zielprüfung:
  - Thema „Ableitung und Änderungsrate“ (`themen.csv`):
    - be-gk: ja – `| Ableitung und Änderungsrate | ja |` [abi-be-gk-geltung.md Zeile 20]
    - be-lk: ja – `| Ableitung und Änderungsrate | ja |` [abi-be-lk-geltung.md Zeile 20]
    - bb-gk: ja – `| Ableitung und Änderungsrate | ja |` [abi-bb-gk-geltung.md Zeile 20]
    - bb-ea: ja – `| Ableitung und Änderungsrate | ja |` [abi-bb-ea-geltung.md Zeile 20]
- Lerneinheiten:
  - 1. Mittlere Änderungsrate und Sekante
    - Eintrag, Zeile 11: „(Q1, GK-Kern „Differenzenquotient“, „mittlere Steigung einer Kurve in einem Intervall“; FOS „mittlere Änderung“; OHiMi 2.2 „mittlere …“
    - GOST Berlin [Zeile 1087]: „Sekanten- und Tangentensteigungen zu Funktionsgraphen bestimmen,“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 901–902]: „Sekanten- und Tangentensteigungen an Funktionsgraphen bestimmen,“
      Q1, Grund- und Leistungskursfach
  - 2. Ableitung an einer Stelle
    - Eintrag, Zeile 12: „(Q1, GK-Kern „Ableitung einer Funktion an einer Stelle“, „lokale Änderungsrate und Anstieg der Tangente“, „lokale Änderungsrate auch in …“
    - GOST Berlin [Zeile 1179]: „die Ableitung insbesondere als lokale Änderungsrate deuten,“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 950–951]: „die Ableitung insbesondere als lokale Änderungsrate deuten,“
      Q1, Grund- und Leistungskursfach
  - 3. Von der Sekante zur Tangente
    - Eintrag, Zeile 13: „LK-Zusatz „Approximation durch lineare Funktionen“; OHiMi 2.2 „Ableitung an einer Stelle“) ← Eingabe „grenzwert der sekantensteigung“, …“
    - GOST Berlin [Zeilen 1050–1051]: „einen propädeutischen Grenzwertbegriffs insbesondere bei der Bestimmung von Ableitung und Integral nutzen,“
      Zahlen und Operationen [L1], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 878–879]: „Grenzwerte auf der Grundlage eines propädeutischen Grenzwertbegriffs“
      Q1, Grund- und Leistungskursfach
    - Ermessen: Der Übergang von der Sekante zur Tangente steht in beiden Plänen nicht als eigene Zeile; zugeordnet ist die Grenzwertzeile, die die Bestimmung der Ableitung nennt.
  - 4. Die Rate als Funktion
    - Eintrag, Zeile 14: „(Q1, GK-Kern „Ableitungsfunktion auch in Sachzusammenhängen“, „Änderungsrate im Sachzusammenhang“; FOS „Modellierung von Verläufen … im …“
    - GOST Berlin [Zeile 1180]: „Änderungsraten funktional beschreiben (Ableitungsfunktion) und interpretieren,“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 955–956]: „Änderungsraten funktional beschreiben und interpretieren,“
      Q1, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 14 Zeilen GK / 9 Zeilen LK, 20 Haupttypen
    - Mittlere Änderungsrate aus dem Funktionsterm im Sachzusammenhang berechnen: 1 GK / 1 LK
    - Mittlere Änderungsrate aus dem Graphen im Sachzusammenhang bestimmen: 1 GK / 1 LK
    - Sekantengleichung durch zwei Punkte eines Graphen ermitteln: 1 GK / 1 LK
    - Ableitungswert berechnen und als Tangentensteigung veranschaulichen: 1 GK / 0 LK
    - Aufgabenstellung zu einer Gleichung aus Differenzenquotient und Ableitung formulieren: 0 GK / 1 LK
    - Eignung eines Modells über das Vorzeichen der Änderungsrate nach einer Nullstelle beurteilen: 0 GK / 1 LK
    - Gleiche Ableitungswerte zweier Funktionen nachweisen und als parallele Tangenten deuten: 1 GK / 0 LK
    - Größte Änderungsrate über das Maximum der Ableitung im Sachzusammenhang berechnen: 1 GK / 0 LK
    - Kleinste Tangentensteigung über das Minimum der Ableitung bestimmen: 1 GK / 0 LK
    - Länge des Zeitraums mit Mindeständerungsrate über die Lösungen von f'(x) = c berechnen: 1 GK / 0 LK
    - Mittlere und momentane Änderungsrate im Sachzusammenhang vergleichen: 1 GK / 0 LK
    - Mittlere Änderungsraten zweier Modelle vergleichen: 1 GK / 0 LK
    - Negativen Wert einer Änderungsrate im Sachzusammenhang deuten: 0 GK / 1 LK
    - Proportionalität zwischen Bestand und Änderungsrate im Sachzusammenhang nachweisen: 1 GK / 0 LK
    - Steigungen aller Sekanten durch einen Punkt des Graphen angeben: 0 GK / 1 LK
    - Stelle mit lokaler gleich mittlerer Änderungsrate bestimmen: 1 GK / 0 LK
    - Umlaufzeit aus der Gesamtlänge eines symmetrischen Streckenzugs mit Halbkreisen und der Durchschnittsgeschwindigkeit berechnen: 1 GK / 0 LK
    - Zeitpunkt der größten Rate aus der Ableitung angeben: 0 GK / 1 LK
    - Zeitpunkt und Größe der maximalen Rate über die Ableitung der Ratenfunktion berechnen: 0 GK / 1 LK
    - Zeitpunkte größter Differenz zweier Änderungsraten über die Extremstellen der Differenzfunktion berechnen: 1 GK / 0 LK
  - iqb: 17 Zeilen GK / 14 Zeilen LK, 26 Haupttypen
    - Zeitpunkt und Größe der maximalen Rate über die Ableitung der Ratenfunktion berechnen: 1 GK / 2 LK
    - Länge des Zeitraums mit Mindeständerungsrate über die Lösungen von f'(x) = c berechnen: 2 GK / 0 LK
    - Mittlere Änderungsrate aus dem Graphen im Sachzusammenhang bestimmen: 1 GK / 1 LK
    - Zeitpunkt der größten Rate aus der Ableitung angeben: 0 GK / 2 LK
    - Ableitungswert berechnen und als Tangentensteigung veranschaulichen: 1 GK / 0 LK
    - Aussage über den Vergleich der Steigungen zweier Graphen auf einem Intervall mit Gegenbeispiel beurteilen: 1 GK / 0 LK
    - Aussage über die Steigung am Graphen beurteilen: 0 GK / 1 LK
    - Aussage über die Zunahme der Zusatzkosten über Differenzen von Funktionswerten beurteilen: 1 GK / 0 LK
    - Differenz und Differenzenquotient im Sachzusammenhang deuten: 1 GK / 0 LK
    - Eignung eines Modells über das Vorzeichen der Änderungsrate nach einer Nullstelle beurteilen: 0 GK / 1 LK
    - Gleichung für die mittlere Änderungsrate lösen und Lösung im Sachzusammenhang deuten: 1 GK / 0 LK
    - Größte und kleinste Rate im Zeitraum über Ableitung und Randwerte berechnen: 0 GK / 1 LK
    - Kleinste Tangentensteigung über das Minimum der Ableitung bestimmen: 1 GK / 0 LK
    - Koordinaten eines Punktes des Ratengraphen im Sachzusammenhang deuten: 1 GK / 0 LK
    - Mittlere Steigung berechnen und Tangentensteigung im Wendepunkt grafisch bestimmen: 0 GK / 1 LK
    - Mittlere und momentane Änderungsrate im Sachzusammenhang vergleichen: 1 GK / 0 LK
    - Mittlere Änderungsrate aus dem Funktionsterm im Sachzusammenhang berechnen: 0 GK / 1 LK
    - Mittlere Änderungsrate über ein Intervall berechnen: 1 GK / 0 LK
    - Negativen Wert einer Änderungsrate im Sachzusammenhang deuten: 0 GK / 1 LK
    - Proportionalität zwischen Bestand und Änderungsrate im Sachzusammenhang nachweisen: 1 GK / 0 LK
    - Sekantenwinkel gegen eine Schranke am Graphen beurteilen: 0 GK / 1 LK
    - Steigung einer Geraden am Graphen begründen: 1 GK / 0 LK
    - Steigungen aller Sekanten durch einen Punkt des Graphen angeben: 0 GK / 1 LK
    - Stelle mit lokaler gleich mittlerer Änderungsrate bestimmen: 1 GK / 0 LK
    - Stelle mit vorgegebener momentaner Änderungsrate über die Ableitung berechnen: 0 GK / 1 LK
    - Term für die mittlere Änderungsrate über Einheitsintervalle nachweisen und Zeitpunkt des Unterschreitens einer Schranke berechnen: 1 GK / 0 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 31 GK / 23 LK)

### ableitungsgraph-und-funktionsgraph
- Geltung je Zielprüfung:
  - Thema „Ableitungsgraph und Funktionsgraph“ (`themen.csv`):
    - be-gk: ja – `| Ableitungsgraph und Funktionsgraph | ja |` [abi-be-gk-geltung.md Zeile 24]
    - be-lk: ja – `| Ableitungsgraph und Funktionsgraph | ja |` [abi-be-lk-geltung.md Zeile 24]
    - bb-gk: ja – `| Ableitungsgraph und Funktionsgraph | ja |` [abi-bb-gk-geltung.md Zeile 24]
    - bb-ea: ja – `| Ableitungsgraph und Funktionsgraph | ja |` [abi-bb-ea-geltung.md Zeile 24]
- Lerneinheiten:
  - keine (Verweiseintrag ohne Abschnitt „Lerneinheiten“)
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 7 Zeilen GK / 4 Zeilen LK, 10 Haupttypen
    - Graphen von Funktion und Ableitung einander zuordnen: 1 GK / 1 LK
    - Art eines Extrempunkts aus dem Vorzeichenwechsel am Ableitungsgraphen begründen: 1 GK / 0 LK
    - Beziehung f'(a) · f''(a) = −1 als Orthogonalität der Tangenten an Graph und Ableitungsgraph deuten: 1 GK / 0 LK
    - Fehlenden Wendepunkt über die Berührnullstelle des Graphen der zweiten Ableitung begründen: 0 GK / 1 LK
    - Monotonie aus dem Vorzeichen der Ableitung am Graphen begründen: 1 GK / 0 LK
    - Sattelpunkt über die Berührnullstelle des Ableitungsgraphen begründen: 1 GK / 0 LK
    - Stellen mit vorgegebenem Anstieg und Wendestelle am Graphen der Ableitung ablesen: 0 GK / 1 LK
    - Vorzeichen der Ableitung an vorgegebenen Stellen aus dem Funktionsgraphen angeben: 1 GK / 0 LK
    - Wendepunkt des Funktionsgraphen aus dem Extrempunkt des Ableitungsgraphen erläutern: 1 GK / 0 LK
    - Zeitpunkt der maximalen Änderungsrate am Graphen der zweiten Ableitung ablesen und begründen: 0 GK / 1 LK
  - iqb: 4 Zeilen GK / 6 Zeilen LK, 7 Haupttypen
    - Graphen von Funktion und Ableitung einander zuordnen: 1 GK / 2 LK
    - Monotonie aus dem Vorzeichen der Ableitung am Graphen begründen: 1 GK / 1 LK
    - Achsensymmetrie des Ableitungsgraphen aus f'(−x) = f'(x) deuten und Graphen skizzieren: 0 GK / 1 LK
    - Anzahl der gemeinsamen Punkte zweier Graphen aus dem Vergleich ihrer Ableitungsgraphen begründen: 0 GK / 1 LK
    - Aussage über zwei Größen anhand von Funktionsgraph und Ableitungsgraph beurteilen: 1 GK / 0 LK
    - Größten jährlichen Zuwachs einer Rate über die Rechtskrümmung des Graphen begründen: 1 GK / 0 LK
    - Tangentensteigung aus dem Graphen der Ableitung ablesen: 0 GK / 1 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: keine Stelle; Typenzeilen: 11 GK / 10 LK)
- Befund: Verweiseintrag ohne Abschnitt „Lerneinheiten“: Teil b bleibt leer, die Kursart lässt sich hier nur über die Typenzeilen bestimmen.

### ableitungsregeln
- Geltung je Zielprüfung:
  - Thema „Ableitungsregeln“ (`themen.csv`):
    - be-gk: ja – `| Ableitungsregeln | ja |` [abi-be-gk-geltung.md Zeile 21]
    - be-lk: ja – `| Ableitungsregeln | ja |` [abi-be-lk-geltung.md Zeile 21]
    - bb-gk: ja – `| Ableitungsregeln | ja |` [abi-bb-gk-geltung.md Zeile 21]
    - bb-ea: ja – `| Ableitungsregeln | ja |` [abi-bb-ea-geltung.md Zeile 21]
- Lerneinheiten:
  - 1. Potenz-, Faktor- und Summenregel
    - Eintrag, Zeile 11: „(Q1, GK-Kern „Konstanten-, Potenz-, Faktor-, Summenregel“; FOS „Ableitungsregeln: Konstanten-, Faktor-, Summen- und Potenzregel (auch mit …“
    - GOST Berlin [Zeilen 1181–1182]: „Potenzfunktionen mit ganzzahligen Exponenten, ganzrationale und Exponentialfunktionen ableiten, auch unter Verwendung der Konstanten-, Potenz-, Faktor-“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 959–960]: „Funktionen ableiten, auch unter Verwendung der Konstanten-, Potenz-,“
      Q1, Grund- und Leistungskursfach
  - 2. Kettenregel
    - Eintrag, Zeile 12: „(Q1, GK-Kern „Kettenregel mit linearer bzw. quadratischer innerer Funktion“, „Verkettungen von ganzrationalen Funktionen und natürlichen …“
    - GOST Berlin [Zeilen 1184–1185]: „die Produktregel und die Kettenregel (mit linearer bzw. quadratischer innerer Funktion) zum Ableiten verwenden,“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 963–964]: „Kettenregel mit linearer bzw. quadratischer innerer Funktion“
      Q1, Grund- und Leistungskursfach
  - 3. Produktregel
    - Eintrag, Zeile 13: „(Q1, GK-Kern „Produktregel“, „multiplikative Verknüpfungen zweier Funktionen“; OHiMi 2.2 „Produktregel“; FOS: kein Stoff)“
    - GOST Berlin [Zeilen 1184–1185]: „die Produktregel und die Kettenregel (mit linearer bzw. quadratischer innerer Funktion) zum Ableiten verwenden,“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 959–960]: „Funktionen ableiten, auch unter Verwendung der Konstanten-, Potenz-,“
      Q1, Grund- und Leistungskursfach
    - Ermessen: Brandenburg führt Produkt- und Kettenregel in derselben Zeile wie die Grundregeln; eine eigene Zeile zur Produktregel gibt es dort nicht.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 2 Zeilen GK / 5 Zeilen LK, 4 Haupttypen
    - Ableitung eines Produkts mit e-Funktion in vorgegebener Form nachweisen: 1 GK / 3 LK
    - Ableitung eines Produkts aus x und einer e-Funktion mit Produkt- und Kettenregel bilden: 0 GK / 1 LK
    - Ableitung mit Parameter in faktorisierter Form nachweisen: 0 GK / 1 LK
    - Ableitungsfunktion und Stammfunktion einer ganzrationalen Funktion angeben: 1 GK / 0 LK
  - iqb: 3 Zeilen GK / 6 Zeilen LK, 8 Haupttypen
    - Ableitung eines Produkts mit e-Funktion in vorgegebener Form nachweisen: 1 GK / 1 LK
    - Ableitung als Quadrat eines Produkts von Linearfaktoren nachweisen: 1 GK / 0 LK
    - Ableitung eines Produkts aus Graphenwerten mit der Produktregel bestimmen: 1 GK / 0 LK
    - Ableitung eines Produkts aus x und einer e-Funktion mit Produkt- und Kettenregel bilden: 0 GK / 1 LK
    - Ableitung mit Parameter in faktorisierter Form nachweisen: 0 GK / 1 LK
    - Bedingung für eine waagerechte Tangente eines Produkts mit e^x nachweisen: 0 GK / 1 LK
    - Tangente an eine Verkettung aus zwei abgebildeten Graphen über die Kettenregel bestimmen: 0 GK / 1 LK
    - Verschiebung zwischen Graph und hundertster Ableitung berechnen: 0 GK / 1 LK
  - fhr: 8 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 5 GK / 11 LK)

### abstaende
- Geltung je Zielprüfung:
  - Thema „Abstände“ (`themen.csv`):
    - be-gk: ja – `| Abstände | ja |` [abi-be-gk-geltung.md Zeile 43]
    - be-lk: ja – `| Abstände | ja |` [abi-be-lk-geltung.md Zeile 43]
    - bb-gk: ja – `| Abstände | ja |` [abi-bb-gk-geltung.md Zeile 43]
    - bb-ea: ja – `| Abstände | ja |` [abi-bb-ea-geltung.md Zeile 43]
- Lerneinheiten:
  - 1. Abstand zweier Punkte
    - Eintrag, Zeile 11: „(Q3, GK-Kern „Punkt – Punkt“; OHiMi 2.3 „Betrag eines Vektors“)“
    - GOST Berlin [Zeilen 1098–1099]: „Abstände (Punkt-Punkt, Punkt-Ebene, Gerade-Ebene, Ebene-Ebene) bestimmen.“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1220–1221]: „Abstände zwischen Punkten, Geraden und Ebenen bestimmen,“
      Q3, Grund- und Leistungskursfach
  - 2. Abstand Punkt–Ebene
    - Eintrag, Zeile 12: „(Q3, GK-Kern „Punkt – Ebene“; OHiMi 2.3 „Hessesche Normalenform“)“
    - GOST Berlin [Zeilen 1098–1099]: „Abstände (Punkt-Punkt, Punkt-Ebene, Gerade-Ebene, Ebene-Ebene) bestimmen.“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1220–1221]: „Abstände zwischen Punkten, Geraden und Ebenen bestimmen,“
      Q3, Grund- und Leistungskursfach
  - 3. Lotfußpunkt
    - Eintrag, Zeile 13: „(Q3, LK-Zusatz „Punkt – Gerade“; der Pool prüft auch grundlegend, siehe Befund Niveaustufung)“
    - GOST Berlin [Zeile 1109]: „Abstände (Punkt-Gerade, Gerade-Gerade) bestimmen,“
      Messen [L2], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1296–1297]: „Abstände zwischen Punkten und Geraden bestimmen,“
      Q3, Zusätzlich im Leistungskursfach
    - Ermessen: Den Lotfußpunkt nennt keiner der beiden Pläne. Zugeordnet ist die Zeile zum Abstand Punkt–Gerade, die in beiden Ländern im LK-Zusatz steht – das Verfahren der Einheit.
  - 4. Abstand als Argument
    - Eintrag, Zeile 14: „(Q3, GK-Kern „Gerade – Ebene“, „Ebene – Ebene“; Eingangsvoraussetzung L3 Pythagoras, Thales, Ähnlichkeit)“
    - GOST Berlin [Zeilen 1098–1099]: „Abstände (Punkt-Punkt, Punkt-Ebene, Gerade-Ebene, Ebene-Ebene) bestimmen.“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1220–1221]: „Abstände zwischen Punkten, Geraden und Ebenen bestimmen,“
      Q3, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 15 Zeilen GK / 12 Zeilen LK, 20 Haupttypen
    - Punkt mit vorgegebenem Abstand zur Ebene auf der Lotgeraden bestimmen: 1 GK / 2 LK
    - Streckenlänge im Raum berechnen: 3 GK / 0 LK
    - Abstand eines Punktes von einer Ebene mit der Hesseschen Normalform berechnen: 1 GK / 1 LK
    - Abstand zweier Punkte auf parallelen Ebenen mit dem Abstand der Ebenen vergleichen: 2 GK / 0 LK
    - Parameter aus der Gleichschenkligkeit eines Dreiecks berechnen: 1 GK / 1 LK
    - Abstand eines Punktes von einer Geraden über Lotgerade und Schnittpunkt aus einem Lösungsweg erläutern: 1 GK / 0 LK
    - Existenz eines Kreispunkts mit vorgegebener Koordinate über den Radius widerlegen: 0 GK / 1 LK
    - Gerade in einer Ebene parallel zu einer Geraden mit kleinstem Abstand bestimmen: 0 GK / 1 LK
    - Gleichen Abstand eines Punktes zu einer Geradenschar über den Lotfußpunkt beurteilen: 0 GK / 1 LK
    - Horizontalen Abstand zweier Punkte als kürzer als ihre Verbindungsstrecke begründen: 1 GK / 0 LK
    - Lotfußpunkt auf einer Geraden über das Skalarprodukt mit dem Richtungsvektor berechnen: 1 GK / 0 LK
    - Lotfußpunkt aus Geradengleichung und Orthogonalitätsbedingung im Gleichungspaar deuten: 1 GK / 0 LK
    - Lotgerade von einem Punkt auf eine Ebene angeben: 0 GK / 1 LK
    - Lösungsweg für den Lotfußpunkt eines Punktes auf einer Geraden beschreiben: 1 GK / 0 LK
    - Lösungsweg für den Punkt gleichen Abstands zu allen Seitenflächen einer Pyramide erläutern: 0 GK / 1 LK
    - Punkt auf einer Strecke mit vorgegebenem Abstand zu einer Ebene bestimmen: 0 GK / 1 LK
    - Punkt mit gleichem Abstand zu allen Seitenflächen über die Symmetrieachse bestimmen: 0 GK / 1 LK
    - Rechenweg für die kürzeste Linie über eine Kante aus Lotfußpunkt und Symmetrie erläutern: 1 GK / 0 LK
    - Strecke in einer geneigten Ebene über einen Höhenschnitt bestimmen: 0 GK / 1 LK
    - Verhältnis zweier Abstände über den Strahlensatz an der Pyramidenspitze begründen: 1 GK / 0 LK
  - iqb: 13 Zeilen GK / 18 Zeilen LK, 25 Haupttypen
    - Parameter aus der Gleichschenkligkeit eines Dreiecks berechnen: 2 GK / 2 LK
    - Punkt mit vorgegebenem Abstand zur Ebene auf der Lotgeraden bestimmen: 1 GK / 2 LK
    - Streckenlänge im Raum berechnen: 1 GK / 1 LK
    - Abstand einer vertikalen Fläche zu einer Achse über den Mittelpunkt der Oberkante begründen: 0 GK / 1 LK
    - Abstand eines Punktes von einer Ebene mit der Hesseschen Normalform berechnen: 0 GK / 1 LK
    - Abstand eines Punktes zu einer Ebene über eine Schrägstrecke nach oben abschätzen: 1 GK / 0 LK
    - Aufgabenstellung zu einer Drehung um eine Kante aus Lotfußpunkt und Rechenweg formulieren: 0 GK / 1 LK
    - Aufgabenstellung zum Abstand eines Punktes von einer Scharebene aus dem Lösungsweg formulieren: 0 GK / 1 LK
    - Erreichbarkeit der Grundfläche über den größten Abstand zu einem Punkt beurteilen: 1 GK / 0 LK
    - Existenz eines Kreispunkts mit vorgegebener Koordinate über den Radius widerlegen: 0 GK / 1 LK
    - Gerade in einer Ebene parallel zu einer Geraden mit kleinstem Abstand bestimmen: 0 GK / 1 LK
    - Gleichen Abstand eines Punktes zu einer Geradenschar über den Lotfußpunkt beurteilen: 0 GK / 1 LK
    - Lotfußpunkt auf einer Geraden über das Skalarprodukt mit dem Richtungsvektor berechnen: 0 GK / 1 LK
    - Lotfußpunkt aus Geradengleichung und Orthogonalitätsbedingung im Gleichungspaar deuten: 1 GK / 0 LK
    - Lotfußpunkt außerhalb einer Figur als Grund für größere Abstände aller Figurpunkte zeichnerisch begründen: 0 GK / 1 LK
    - Lösungsweg für den Lotfußpunkt eines Punktes auf einer Geraden beschreiben: 1 GK / 0 LK
    - Lösungsweg für den Punkt gleichen Abstands zu allen Seitenflächen einer Pyramide erläutern: 0 GK / 1 LK
    - Lösungsweg für einen Punkt mit gleichem Abstand zu drei Strecken über Lotfußpunkt und Abstandsgleichheit erläutern: 0 GK / 1 LK
    - Nächsten und fernsten Punkt des Deckflächenrands eines Zylinders zu einem Randpunkt der Grundfläche bestimmen: 0 GK / 1 LK
    - Punkt auf einer Geraden mit vorgegebenem Abstand zu einer zweiten Geraden über eine Skizze und den Sinus berechnen: 1 GK / 0 LK
    - Punkte mit gleichem Abstand zu drei Eckpunkten eines rechtwinkligen Dreiecks über den Thaleskreis ermitteln: 1 GK / 0 LK
    - Rechenweg für die kürzeste Linie über eine Kante aus Lotfußpunkt und Symmetrie erläutern: 1 GK / 0 LK
    - Sprungweite als Abstand zweier Punkte einer Parameterkurve in der Grundebene berechnen: 0 GK / 1 LK
    - Untere Schranke für den Abstand zweier Punkte mit einer unbekannten Koordinate nachweisen: 1 GK / 0 LK
    - Verhältnis zweier Abstände über den Strahlensatz an der Pyramidenspitze begründen: 1 GK / 0 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: GK-Block und LK-Block; Typenzeilen: 28 GK / 30 LK)

### bedingte-wahrscheinlichkeit-und-bayes
- Geltung je Zielprüfung:
  - Thema „Bedingte Wahrscheinlichkeit und Bayes“ (`themen.csv`):
    - be-gk: ja – `| Bedingte Wahrscheinlichkeit und Bayes | ja |` [abi-be-gk-geltung.md Zeile 53]
    - be-lk: ja – `| Bedingte Wahrscheinlichkeit und Bayes | ja |` [abi-be-lk-geltung.md Zeile 53]
    - bb-gk: ja – `| Bedingte Wahrscheinlichkeit und Bayes | ja |` [abi-bb-gk-geltung.md Zeile 53]
    - bb-ea: ja – `| Bedingte Wahrscheinlichkeit und Bayes | ja |` [abi-bb-ea-geltung.md Zeile 53]
- Lerneinheiten:
  - 1. Der Quotient
    - Eintrag, Zeile 11: „(Q2, GK-Kern „bedingte Wahrscheinlichkeit“; OHiMi 2.4 Quotient)“
    - GOST Berlin [Zeilen 1241–1242]: „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln untersuchen und damit Problemstellungen im Kontext bedingter Wahrscheinlichkeiten lösen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1136–1137]: „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln unter-“
      Q2, Grund- und Leistungskursfach
  - 2. Bayes
    - Eintrag, Zeile 12: „(Q2, GK-Kern „Satz von der totalen Wahrscheinlichkeit“, „Satz von Bayes“ – nur Brandenburg nennt die Namen)“
    - GOST Berlin [Zeilen 1241–1242]: „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln untersuchen und damit Problemstellungen im Kontext bedingter Wahrscheinlichkeiten lösen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1147]: „Satz von Bayes“
      Q2, Grund- und Leistungskursfach
  - 3. Mit Parameter
    - Eintrag, Zeile 13: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1241–1242]: „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln untersuchen und damit Problemstellungen im Kontext bedingter Wahrscheinlichkeiten lösen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1136–1137]: „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln unter-“
      Q2, Grund- und Leistungskursfach
    - Ermessen: Den Parameterfall (bedingte Wahrscheinlichkeit mit Unbekannter) nennt kein Plan eigens; zugeordnet ist die Zeile zur bedingten Wahrscheinlichkeit.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 6 Zeilen GK / 5 Zeilen LK, 4 Haupttypen
    - Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen: 3 GK / 1 LK
    - Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen: 1 GK / 2 LK
    - Monotonie einer bedingten Wahrscheinlichkeit bei Änderung eines Anteils beurteilen: 1 GK / 2 LK
    - Bayes-Term mit Parameter grafisch lösen und Parameter und Funktionswert im Sachzusammenhang deuten: 1 GK / 0 LK
  - iqb: 18 Zeilen GK / 10 Zeilen LK, 12 Haupttypen
    - Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen: 7 GK / 1 LK
    - Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen: 3 GK / 2 LK
    - Bedingte Anteile aus der Vierfeldertafel vergleichen: 1 GK / 2 LK
    - Monotonie einer bedingten Wahrscheinlichkeit bei Änderung eines Anteils beurteilen: 1 GK / 2 LK
    - Bayes-Term im Sachzusammenhang deuten: 2 GK / 0 LK
    - Bayes-Term für drei Behälter nachweisen und Kugelzahl bestimmen: 0 GK / 1 LK
    - Bayes-Term mit Parameter grafisch lösen und Parameter und Funktionswert im Sachzusammenhang deuten: 1 GK / 0 LK
    - Bedingte Wahrscheinlichkeit aus dem Baumdiagramm mit einer Schranke vergleichen: 1 GK / 0 LK
    - Bedingte Wahrscheinlichkeit aus der Vierfeldertafel mit absoluten Häufigkeiten angeben: 1 GK / 0 LK
    - Graph einer bedingten Wahrscheinlichkeit in Abhängigkeit von einem Parameter über Randwerte ohne Rechnung zuordnen: 1 GK / 0 LK
    - Mindestwert einer Erkennungswahrscheinlichkeit aus einer Bedingung an eine bedingte Wahrscheinlichkeit bestimmen: 0 GK / 1 LK
    - Term für eine bedingte Wahrscheinlichkeit mit Parameter aufstellen: 0 GK / 1 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 24 GK / 15 LK)

### binomialverteilung
- Geltung je Zielprüfung:
  - Thema „Binomialverteilung“ (`themen.csv`):
    - be-gk: ja – `| Binomialverteilung | ja |` [abi-be-gk-geltung.md Zeile 57]
    - be-lk: ja – `| Binomialverteilung | ja |` [abi-be-lk-geltung.md Zeile 57]
    - bb-gk: ja – `| Binomialverteilung | ja |` [abi-bb-gk-geltung.md Zeile 57]
    - bb-ea: ja – `| Binomialverteilung | ja |` [abi-bb-ea-geltung.md Zeile 57]
- Lerneinheiten:
  - 1. Bernoulli-Experiment und Bernoulli-Kette
    - Eintrag, Zeile 11: „(Q2, GK-Kern; OHiMi 2.4 „Ansätze zur Berechnung“)“
    - GOST Berlin [Zeile 1195]: „die Binomialverteilung zur Beschreibung stochastischer Situationen nutzen.“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1108–1109]: „Bernoulli-Experiment Bernoulli-Kette“
      Q2, Grund- und Leistungskursfach
  - 2. Bernoulli-Formel
    - Eintrag, Zeile 12: „(Q2, GK-Kern; OHiMi 2.4 Bernoulli-Formel auswendig)“
    - GOST Berlin [Zeile 1248]: „die Binomialverteilung und ihre Kenngrößen (n, p) nutzen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1107–1108]: „die Binomialverteilung und ihre Kenngrößen nutzen und die Binomialvertei-“
      Q2, Grund- und Leistungskursfach
  - 3. Kumulierte Wahrscheinlichkeiten
    - Eintrag, Zeile 13: „(Q2, GK-Kern „Punkt- und Intervallwahrscheinlichkeiten“, „kumulative Darstellungen“; Teil B mit Rechner)“
    - GOST Berlin [Zeile 1248]: „die Binomialverteilung und ihre Kenngrößen (n, p) nutzen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1114–1115]: „Binomialverteilung im Histogramm, auch kumulative Darstellungen“
      Q2, Grund- und Leistungskursfach
  - 4. Umkehraufgaben
    - Eintrag, Zeile 14: „(Q2, GK-Kern; LS-AA „Problemlösen mit der Binomialverteilung“; Landeshefte mit Logarithmus, Pool mit Probieren)“
    - GOST Berlin [Zeile 1248]: „die Binomialverteilung und ihre Kenngrößen (n, p) nutzen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1112–1113]: „Punkt- und Intervallwahrscheinlichkeiten für die Anzahl an Erfolgen“
      Q2, Grund- und Leistungskursfach
    - Ermessen: Die Umkehraufgabe (n oder p aus einer Wahrscheinlichkeit) nennt kein Plan eigens; zugeordnet ist die Inhaltszeile zu Punkt- und Intervallwahrscheinlichkeiten.
  - 5. Verteilung im Diagramm
    - Eintrag, Zeile 15: „(Q2, GK-Kern „Binomialverteilung im Histogramm, auch kumulative Darstellungen“, „Eigenschaften auf der Grundlage graphischer Darstellungen“; …“
    - GOST Berlin [Zeile 1248]: „die Binomialverteilung und ihre Kenngrößen (n, p) nutzen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1114–1115]: „Binomialverteilung im Histogramm, auch kumulative Darstellungen“
      Q2, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 37 Zeilen GK / 20 Zeilen LK, 30 Haupttypen
    - Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln: 2 GK / 5 LK
    - Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen: 6 GK / 0 LK
    - Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln: 2 GK / 4 LK
    - Mindestanzahl von Versuchen einer Bernoulli-Kette über das Gegenereignis bestimmen: 5 GK / 1 LK
    - Kumulierte Binomialsumme als Sachaussage formulieren: 3 GK / 0 LK
    - Aussage über die Stelle des Maximums der Binomialverteilung über den Erwartungswert beurteilen: 2 GK / 0 LK
    - Term für eine Wahrscheinlichkeit einer Bernoulli-Kette angeben: 1 GK / 1 LK
    - Trefferwahrscheinlichkeit aus einer Bedingung an die Wahrscheinlichkeit für null Treffer bestimmen: 2 GK / 0 LK
    - Wahrscheinlichkeit über die Verteilung der Gegenzufallsgröße im Diagramm erläutern: 1 GK / 1 LK
    - Aussage zur Änderung einer Wahrscheinlichkeit bei größerer Stichprobe beurteilen: 1 GK / 0 LK
    - Aussage über die Halbierung einer Potenzwahrscheinlichkeit bei doppeltem Umfang allgemein widerlegen: 0 GK / 1 LK
    - Bedingung an ein Anzahlverhältnis in eine Binomialwahrscheinlichkeit übersetzen: 1 GK / 0 LK
    - Behauptung zur Monotonie einer Wahrscheinlichkeit an Beispielwerten prüfen: 1 GK / 0 LK
    - Binomialverteilung einer Zufallsgröße über die Bernoulli-Bedingungen begründen: 1 GK / 0 LK
    - Binomialverteilung über den Widerspruch zwischen Symmetrie und einer Einzelwahrscheinlichkeit ausschließen: 0 GK / 1 LK
    - Einzelwahrscheinlichkeit aus Symmetrie und kumulierten Werten berechnen: 1 GK / 0 LK
    - Fehlerwahrscheinlichkeit einer Einheit binomial berechnen und als Trefferwahrscheinlichkeit einer zweiten Binomialverteilung verwenden: 1 GK / 0 LK
    - Grenze k einer kumulierten Wahrscheinlichkeit gegen eine Schranke mit dem Rechner ermitteln: 1 GK / 0 LK
    - Kleinsten Radius einer symmetrischen Umgebung um den Erwartungswert für eine Mindestwahrscheinlichkeit ermitteln: 0 GK / 1 LK
    - Mindestumfang für eine Mindestwahrscheinlichkeit von mehr als k Treffern ermitteln: 0 GK / 1 LK
    - Modalwert einer Binomialverteilung bestimmen: 1 GK / 0 LK
    - Ungeeignetheit des Binomialmodells begründen: 1 GK / 0 LK
    - Unpassende Säulendiagramme zu einer Binomialverteilung begründet ausschließen: 1 GK / 0 LK
    - Wahrscheinlichkeit einer relativen Abweichung vom Erwartungswert nach oben berechnen: 0 GK / 1 LK
    - Wahrscheinlichkeit eines Intervalls aus dem Säulendiagramm einer Verteilung ablesen: 1 GK / 0 LK
    - Wahrscheinlichkeit für Gewinn und Extrapreis über die Aufteilung einer Bernoulli-Kette in zwei Abschnitte berechnen: 0 GK / 1 LK
    - Wahrscheinlichkeit für genau einen Treffer bei zwei Versuchen berechnen: 0 GK / 1 LK
    - Wahrscheinlichkeit für mindestens zwei Treffer bei drei Versuchen nachweisen: 0 GK / 1 LK
    - Wahrscheinlichkeit für zwei unabhängige Spieler als Produkt binomialer Wahrscheinlichkeiten berechnen: 1 GK / 0 LK
    - Werte zu Wahrscheinlichkeitsbedingungen aus dem Säulendiagramm ablesen: 1 GK / 0 LK
  - iqb: 61 Zeilen GK / 37 Zeilen LK, 52 Haupttypen
    - Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln: 10 GK / 6 LK
    - Kumulierte Binomialsumme als Sachaussage formulieren: 5 GK / 2 LK
    - Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln: 2 GK / 3 LK
    - Term für eine Wahrscheinlichkeit einer Bernoulli-Kette angeben: 2 GK / 3 LK
    - Unpassende Säulendiagramme zu einer Binomialverteilung begründet ausschließen: 2 GK / 2 LK
    - Ungeeignetheit des Binomialmodells begründen: 2 GK / 1 LK
    - Aussage über die Stelle des Maximums der Binomialverteilung über den Erwartungswert beurteilen: 2 GK / 0 LK
    - Binomialverteilung einer Zufallsgröße über die Bernoulli-Bedingungen begründen: 2 GK / 0 LK
    - Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen: 2 GK / 0 LK
    - Einzelwahrscheinlichkeit aus Symmetrie und kumulierten Werten berechnen: 2 GK / 0 LK
    - Fehlerwahrscheinlichkeit einer Einheit binomial berechnen und als Trefferwahrscheinlichkeit einer zweiten Binomialverteilung verwenden: 1 GK / 1 LK
    - Grenze k einer kumulierten Wahrscheinlichkeit gegen eine Schranke mit dem Rechner ermitteln: 1 GK / 1 LK
    - Kleinsten Radius einer symmetrischen Umgebung um den Erwartungswert für eine Mindestwahrscheinlichkeit ermitteln: 1 GK / 1 LK
    - Mindestumfang für eine Mindestwahrscheinlichkeit von mehr als k Treffern ermitteln: 1 GK / 1 LK
    - Sachaussage zu einer Ungleichung mit Binomialsumme formulieren: 2 GK / 0 LK
    - Trefferwahrscheinlichkeit aus einer Bedingung an die Wahrscheinlichkeit für null Treffer bestimmen: 2 GK / 0 LK
    - Wahrscheinlichkeit für genau einen Treffer bei zwei Versuchen berechnen: 1 GK / 1 LK
    - Wahrscheinlichkeit über die Verteilung der Gegenzufallsgröße im Diagramm erläutern: 1 GK / 1 LK
    - Achsen eines Verteilungsdiagramms über Erwartungswert und größte Einzelwahrscheinlichkeit skalieren: 1 GK / 0 LK
    - Aufgabenstellung zu einer Potenz der Gegenwahrscheinlichkeit formulieren und Ansatz erläutern: 0 GK / 1 LK
    - Aussage zur Änderung einer Wahrscheinlichkeit bei größerer Stichprobe beurteilen: 1 GK / 0 LK
    - Aussage über die Halbierung einer Potenzwahrscheinlichkeit bei doppeltem Umfang allgemein widerlegen: 0 GK / 1 LK
    - Aussage über eine Summe von Wahrscheinlichkeiten am Säulendiagramm entscheiden: 0 GK / 1 LK
    - Aussagen über Bernoulli-Experiment und Bernoulli-Kette im Sachzusammenhang beurteilen: 1 GK / 0 LK
    - Aussagen über Verteilungen verschiedener Gruppen am Säulendiagramm beurteilen: 1 GK / 0 LK
    - Aussagen über kumulierte Wahrscheinlichkeit und Trefferwahrscheinlichkeit aus dem Säulendiagramm einer Binomialverteilung beurteilen: 1 GK / 0 LK
    - Bedingte Restwahrscheinlichkeit nach bekannten Ergebnissen über die Binomialverteilung berechnen: 1 GK / 0 LK
    - Bedingung an ein Anzahlverhältnis in eine Binomialwahrscheinlichkeit übersetzen: 1 GK / 0 LK
    - Bedingung an p für das Verhältnis zweier symmetrisch liegender Einzelwahrscheinlichkeiten angeben: 0 GK / 1 LK
    - Einzelwahrscheinlichkeit aus dem Diagramm kumulierter Wahrscheinlichkeiten ermitteln: 0 GK / 1 LK
    - Einzelwahrscheinlichkeit einer Binomialverteilung aus n und Erwartungswert berechnen: 1 GK / 0 LK
    - Kleinste Umgebungsbreite unterhalb des Erwartungswerts für eine Mindestwahrscheinlichkeit ermitteln: 1 GK / 0 LK
    - Kumulierte Binomialwahrscheinlichkeit und Pfadwahrscheinlichkeit einer festen Anfangsfolge berechnen: 1 GK / 0 LK
    - Mindestanzahl von Versuchen für mindestens drei Treffer mit vorgegebener Wahrscheinlichkeit durch Probieren ermitteln: 0 GK / 1 LK
    - Modalwert einer Binomialverteilung bestimmen: 1 GK / 0 LK
    - Obere Grenze einer im Diagramm markierten kumulierten Wahrscheinlichkeit über den Erwartungswert ermitteln: 0 GK / 1 LK
    - Parameter n und p aus einem Verhältnis zweier Einzelwahrscheinlichkeiten und dem Erwartungswert berechnen: 0 GK / 1 LK
    - Stichprobenumfang aus dem Erwartungswert berechnen und Einzelwahrscheinlichkeit ermitteln: 1 GK / 0 LK
    - Stichprobenumfang zu einer vorgegebenen Einzelwahrscheinlichkeit mit dem Rechner suchen: 1 GK / 0 LK
    - Summenbedingung bei wiederholtem Wurf in eine Binomialwahrscheinlichkeit übersetzen und nachweisen: 1 GK / 0 LK
    - Summenterme der Binomialverteilung auf ein vorgegebenes Mindestens-Ereignis prüfen und begründen: 1 GK / 0 LK
    - Trefferwahrscheinlichkeit aus einer Gleichung zweier Einzelwahrscheinlichkeiten berechnen: 0 GK / 1 LK
    - Trefferwahrscheinlichkeit aus einer kumulierten Wahrscheinlichkeit auf ganze Prozent durch Probieren ermitteln: 1 GK / 0 LK
    - Verteilung der Gegenzufallsgröße im Diagramm darstellen: 0 GK / 1 LK
    - Wahrscheinlichkeit einer prozentualen Abweichung vom Erwartungswert nach beiden Seiten berechnen: 1 GK / 0 LK
    - Wahrscheinlichkeit einer relativen Abweichung vom Erwartungswert nach oben berechnen: 0 GK / 1 LK
    - Wahrscheinlichkeit eines symmetrischen Intervalls über die Symmetrie der Binomialverteilung berechnen: 0 GK / 1 LK
    - Wahrscheinlichkeit eines zweistufigen Prüfplans über Binomialwahrscheinlichkeiten berechnen: 1 GK / 0 LK
    - Wahrscheinlichkeit für mindestens zwei Treffer bei drei Versuchen nachweisen: 0 GK / 1 LK
    - Werte zu Wahrscheinlichkeitsbedingungen aus dem Säulendiagramm ablesen: 1 GK / 0 LK
    - Wirkung eines kleineren Stichprobenumfangs auf eine Annahmewahrscheinlichkeit ohne Rechnung beurteilen: 1 GK / 0 LK
    - Zufallsgröße mit gleicher Binomialverteilung in einem anderen Experiment angeben: 0 GK / 1 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 98 GK / 57 LK)

### ebenen
- Geltung je Zielprüfung:
  - Thema „Ebenen“ (`themen.csv`):
    - be-gk: ja – `| Ebenen | ja |` [abi-be-gk-geltung.md Zeile 38]
    - be-lk: ja – `| Ebenen | ja |` [abi-be-lk-geltung.md Zeile 38]
    - bb-gk: ja – `| Ebenen | ja |` [abi-bb-gk-geltung.md Zeile 38]
    - bb-ea: ja – `| Ebenen | ja |` [abi-bb-ea-geltung.md Zeile 38]
- Lerneinheiten:
  - 1. Parameterform einer Ebene
    - Eintrag, Zeile 11: „(Q3, GK-Kern „Spannvektoren“, „Parameterform“; OHiMi 2.3 „Ebenen: Parameterform“)“
    - GOST Berlin [Zeilen 1142–1143]: „Geraden und Ebenen (durch Parameter-, Koordinaten- und Normalenform) analytisch beschreiben und Lagebeziehungen untersuchen (vgl. L2).“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1268–1269]: „Geraden und Ebenen analytisch beschreiben und Lagebeziehungen von“
      Q3, Grund- und Leistungskursfach
  - 2. Normalenvektor und Koordinatengleichung
    - Eintrag, Zeile 12: „(Q3, GK-Kern „Normalenvektor“, „Koordinatenform“, „Normalenform“, „Zusammenhang zwischen Parameter-, Normalen- und Koordinatengleichung“; …“
    - GOST Berlin [Zeilen 1142–1143]: „Geraden und Ebenen (durch Parameter-, Koordinaten- und Normalenform) analytisch beschreiben und Lagebeziehungen untersuchen (vgl. L2).“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1274–1275]: „Koordinatenform Normalenform“
      Q3, Grund- und Leistungskursfach
  - 3. Ebenen im Koordinatensystem
    - Eintrag, Zeile 13: „(Q3, GK-Kern „Darstellung von ... Ebenen ... in dreidimensionalen kartesischen Koordinatensystemen“; OHiMi 2.3 „Darstellung und Beschreibung …“
    - GOST Berlin [Zeilen 1134–1135]: „geometrische Sachverhalte in Ebene und Raum koordinatisieren (geometrische Interpretation von Gleichungssystemen und ihrer Lösungen) und im Koordinaten-“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1225–1226]: „geometrische Sachverhalte in Ebene und Raum koordinatisieren und im Ko-“
      Q3, Grund- und Leistungskursfach
  - 4. Parallele Ebenen
    - Eintrag, Zeile 14: „(Q3, GK-Kern „Lagebeziehungen zwischen: ... Ebenen“; OHiMi 2.3 „Lagebeziehungen zwischen Punkten, Geraden und Ebenen“)“
    - GOST Berlin [Zeilen 1142–1143]: „Geraden und Ebenen (durch Parameter-, Koordinaten- und Normalenform) analytisch beschreiben und Lagebeziehungen untersuchen (vgl. L2).“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1268–1269]: „Geraden und Ebenen analytisch beschreiben und Lagebeziehungen von“
      Q3, Grund- und Leistungskursfach
    - Ermessen: Parallele Ebenen sind ein Sonderfall der Lagebeziehung; eine eigene Zeile gibt es in keinem Plan.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 12 Zeilen GK / 8 Zeilen LK, 10 Haupttypen
    - Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen: 6 GK / 3 LK
    - Koordinatengleichung einer parallelen Ebene durch einen Punkt aufstellen: 2 GK / 0 LK
    - Parametergleichung einer Ebene aus Punkten angeben: 1 GK / 1 LK
    - Koordinatenform einer Ebene aus der Normalenform durch Ausmultiplizieren angeben: 1 GK / 0 LK
    - Koordinatengleichung einer Ebene aus Gerade und Punkt nachweisen: 0 GK / 1 LK
    - Lage einer Ebene zu einer Koordinatenachse aus der Koordinatengleichung begründen: 1 GK / 0 LK
    - Lage einer Figur in einer Koordinatenebene aus Eckpunkt und orthogonaler Geraden begründen: 0 GK / 1 LK
    - Normalenvektor als Ortsvektor eines Ebenenpunktes bestimmen: 0 GK / 1 LK
    - Normalenvektor aus der Orthogonalität zu Vielfachen der Spannvektoren begründen: 0 GK / 1 LK
    - Parallelität zweier Ebenen über die Normalenvektoren und eine Punktprobe begründen: 1 GK / 0 LK
  - iqb: 13 Zeilen GK / 15 Zeilen LK, 16 Haupttypen
    - Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen: 5 GK / 6 LK
    - Achsenparallele Ebene einer Bewegung aus der Parameterdarstellung angeben: 0 GK / 2 LK
    - Lage einer Ebene zu einer Koordinatenachse aus der Koordinatengleichung begründen: 1 GK / 1 LK
    - Darstellung einer Ebene im Schrägbild als Gerade beurteilen: 0 GK / 1 LK
    - Eindeutigkeit einer Ebene durch vier Punkte über die Kollinearität dreier Punkte begründen: 1 GK / 0 LK
    - Komponente des Normalenvektors aus der Orthogonalität zur Koordinatenebene begründen: 0 GK / 1 LK
    - Konstante einer Koordinatengleichung durch Einsetzen eines Punktes bestimmen: 1 GK / 0 LK
    - Koordinatengleichung einer parallelen Ebene durch einen Punkt aufstellen: 1 GK / 0 LK
    - Lage einer Figur in einer Koordinatenebene aus Eckpunkt und orthogonaler Geraden begründen: 0 GK / 1 LK
    - Normalenvektor als Ortsvektor eines Ebenenpunktes bestimmen: 0 GK / 1 LK
    - Normalenvektor aus der Orthogonalität zu Vielfachen der Spannvektoren begründen: 0 GK / 1 LK
    - Normalenvektor einer Ebene aus zwei Richtungsvektoren über Skalarprodukte bestimmen: 1 GK / 0 LK
    - Parallele Ebene mit vorgegebenem Volumenverhältnis eines Prismas ermitteln: 1 GK / 0 LK
    - Parametergleichung einer Ebene aus Punkten angeben: 1 GK / 0 LK
    - Vertikale Lage einer Fläche über einen Normalenvektor mit x₃-Komponente null nachweisen: 1 GK / 0 LK
    - Übereinstimmung einer Ebene mit einer Koordinatenebene beurteilen: 0 GK / 1 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 25 GK / 23 LK)

### extremalprobleme
- Geltung je Zielprüfung:
  - Thema „Extremalprobleme“ (`themen.csv`):
    - be-gk: ja – `| Extremalprobleme | ja |` [abi-be-gk-geltung.md Zeile 27]
    - be-lk: ja – `| Extremalprobleme | ja |` [abi-be-lk-geltung.md Zeile 27]
    - bb-gk: ja – `| Extremalprobleme | ja |` [abi-bb-gk-geltung.md Zeile 27]
    - bb-ea: ja – `| Extremalprobleme | ja |` [abi-bb-ea-geltung.md Zeile 27]
- Lerneinheiten:
  - 1. Figur und Term
    - Eintrag, Zeile 11: „(Q1, GK-Kern; FOS „Umfang und Flächeninhalt ebener Figuren in Zusammenhang mit Funktionsgraphen“)“
    - GOST Berlin [Zeilen 1167–1168]: „hänge nutzen (z. B. in Fragestellungen zu Sachsituationen, die auf Rekonstruktion von Funktionsgleichungen, Extremalprobleme etc. führen),“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 924–925]: „Extremalprobleme, auch im Kontext außermathematischer Problemstellungen“
      Q1, Grund- und Leistungskursfach
  - 2. Zielfunktion aus Haupt- und Nebenbedingung
    - Eintrag, Zeile 12: „(Q1, GK-Kern „Extremalprobleme“; FOS „Ermitteln der Zielfunktion“)“
    - GOST Berlin [Zeilen 1167–1168]: „hänge nutzen (z. B. in Fragestellungen zu Sachsituationen, die auf Rekonstruktion von Funktionsgleichungen, Extremalprobleme etc. führen),“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 924–925]: „Extremalprobleme, auch im Kontext außermathematischer Problemstellungen“
      Q1, Grund- und Leistungskursfach
  - 3. Maximum bestimmen und deuten
    - Eintrag, Zeile 13: „(Q1, GK-Kern „Extremalprobleme“, „Randextrema“; FOS „Untersuchung auf lokale Extrema“)“
    - GOST Berlin [Zeilen 1186–1187]: „die Ableitung zur Bestimmung von Monotonie, Extrema und Wendepunkten (notwendige Bedingung und inhaltliche Begründungen für die Existenz) von“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 968–969]: „die Ableitung zur Bestimmung von Monotonie, Extrem- und Wendepunkten“
      Q1, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 6 Zeilen GK / 1 Zeilen LK, 4 Haupttypen
    - Maximalen vertikalen Abstand zweier Graphen über die Differenzfunktion nachweisen: 4 GK / 0 LK
    - Achsenparalleles Rechteck maximaler Fläche zwischen Ursprung und Graphenpunkt bestimmen: 1 GK / 0 LK
    - Ausschluss einer Stelle als Maximalstelle einer Rechtecksfläche über die notwendige Bedingung nachweisen: 1 GK / 0 LK
    - Dreieck zu Schnittpunkten mit einer Parallelen zur x-Achse einzeichnen: 0 GK / 1 LK
  - iqb: 4 Zeilen GK / 3 Zeilen LK, 6 Haupttypen
    - Parameter für den größten Flächeninhalt über die Ableitung bestimmen: 1 GK / 1 LK
    - Aufgabenstellung zu einer Extremwertaufgabe mit Dreiecksfläche aus dem Lösungsweg formulieren und Schritte erläutern: 0 GK / 1 LK
    - Einbeschriebenes Trapez zu einem Parameterwert in die Abbildung einzeichnen: 1 GK / 0 LK
    - Flächeninhaltsterm eines Dreiecks unter dem Graphen begründen: 0 GK / 1 LK
    - Flächenterm eines einbeschriebenen Trapezes über die Mittelparallele geometrisch herleiten: 1 GK / 0 LK
    - Term für die Schenkellänge eines einbeschriebenen Trapezes aufstellen: 1 GK / 0 LK
  - fhr: 9 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 10 GK / 4 LK)

### flaecheninhalt-durch-integration
- Geltung je Zielprüfung:
  - Thema „Flächeninhalt durch Integration“ (`themen.csv`):
    - be-gk: ja – `| Flächeninhalt durch Integration | ja |` [abi-be-gk-geltung.md Zeile 30]
    - be-lk: ja – `| Flächeninhalt durch Integration | ja |` [abi-be-lk-geltung.md Zeile 30]
    - bb-gk: ja – `| Flächeninhalt durch Integration | ja |` [abi-bb-gk-geltung.md Zeile 30]
    - bb-ea: ja – `| Flächeninhalt durch Integration | ja |` [abi-bb-ea-geltung.md Zeile 30]
- Lerneinheiten:
  - 1. Fläche zwischen Graph und x-Achse
    - Eintrag, Zeile 11: „(Q2 GK-Kern L2; FOS „Fläche zwischen dem Graphen einer Funktion und der x-Achse“, „Orientierung von Flächen“; OHiMi „Ermittlung von …“
    - GOST Berlin [Zeilen 1090–1091]: „Inhalte von Flächen, die durch Funktionsgraphen (von Potenzfunktionen f mit f(x) = xn, n ∈ ZZ , n ≠ −1 , ganzrationalen und Exponentialfunktionen) begrenzt“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1053–1054]: „Inhalte von Flächen, die durch Funk-tionsgraphen begrenzt sind, bestimmen,“
      Q2, Grund- und Leistungskursfach
  - 2. Fläche zwischen zwei Graphen
    - Eintrag, Zeile 12: „(Q2 GK-Kern L2 „von Funktionsgraphen … begrenzt“; FOS „Fläche zwischen zwei Funktionsgraphen“)“
    - GOST Berlin [Zeilen 1090–1091]: „Inhalte von Flächen, die durch Funktionsgraphen (von Potenzfunktionen f mit f(x) = xn, n ∈ ZZ , n ≠ −1 , ganzrationalen und Exponentialfunktionen) begrenzt“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1054–1055]: „Flächeninhalt von Flächen, welche von Funktionsgraphen, den Koordinatenach-“
      Q2, Grund- und Leistungskursfach
  - 3. Zusammengesetzte Flächen, Maßstab und Volumen
    - Eintrag, Zeile 13: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1090–1091]: „Inhalte von Flächen, die durch Funktionsgraphen (von Potenzfunktionen f mit f(x) = xn, n ∈ ZZ , n ≠ −1 , ganzrationalen und Exponentialfunktionen) begrenzt“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1053–1054]: „Inhalte von Flächen, die durch Funk-tionsgraphen begrenzt sind, bestimmen,“
      Q2, Grund- und Leistungskursfach
    - Ermessen: Maßstab und Volumen als Anwendung der Flächenrechnung nennt kein Plan eigens; Brandenburg hat nur den Zusatz „auch in Anwendungszusammenhängen“ in der Inhaltsspalte (Zeilen 1057–1058).
  - 4. Flächenbedingungen
    - Eintrag, Zeile 14: „(Q2 GK-Kern L2 „auch in Anwendungszusammenhängen“; Teil-A-Belege, siehe Kasten)“
    - GOST Berlin [Zeilen 1090–1091]: „Inhalte von Flächen, die durch Funktionsgraphen (von Potenzfunktionen f mit f(x) = xn, n ∈ ZZ , n ≠ −1 , ganzrationalen und Exponentialfunktionen) begrenzt“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1337–1338]: „Bestimmung von Scharparametern bzw. Integrationsgrenzen bei gegebenem“
      Q4, Zusätzlich im Leistungskursfach
    - Ermessen: Die Rückrichtung (Grenze oder Parameter aus einem vorgegebenen Flächeninhalt) steht nur in Brandenburg, dort im LK-Zusatz des vierten Kurshalbjahrs.
  - 5. Das Integral als Flächenbilanz
    - Eintrag, Zeile 15: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeile 1190]: „das bestimmte Integral deuten, insbesondere als (re-) konstruierten Bestand,“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1067–1068]: „das bestimmte Integral deuten, insbesondere als (re-)konstruierten Be-“
      Q2, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 28 Zeilen GK / 14 Zeilen LK, 33 Haupttypen
    - Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen: 3 GK / 4 LK
    - Integralwert: Mittelwert einer Funktion als Integral geteilt durch die Intervalllänge berechnen und deuten: 2 GK / 1 LK
    - Fläche: Fläche zwischen Graph und x-Achse aus zwei Flächenstücken berechnen: 2 GK / 0 LK
    - Fläche: Abschnittsweise begrenzte Fläche durch Integration berechnen: 0 GK / 1 LK
    - Fläche: An der Sehne gespiegelte Randlinien skizzieren und Lösungsweg für den Flächenzuwachs beschreiben: 1 GK / 0 LK
    - Fläche: Differenz von Kreisfläche und Flügelflächen veranschaulichen und berechnen: 1 GK / 0 LK
    - Fläche: Eingeschlossene Fläche aus Integral, Symmetrie und Halbkreisen berechnen: 1 GK / 0 LK
    - Fläche: Fläche zwischen Graph und Koordinatenachsen berechnen: 1 GK / 0 LK
    - Fläche: Fläche zwischen Graph und waagerechter Gerade zwischen zwei nachgewiesenen Schnittstellen berechnen: 1 GK / 0 LK
    - Fläche: Fläche zwischen Graph, x-Achse und zwei senkrechten Geraden mit vorgegebener Stammfunktion berechnen: 1 GK / 0 LK
    - Fläche: Fläche zwischen zwei Graphen mit verschiedenen Grenzen als Differenz zweier Integrale berechnen: 1 GK / 0 LK
    - Fläche: Flächeninhalt zwischen Graph und waagerechter Gerade als Term in der Grenze nachweisen: 1 GK / 0 LK
    - Fläche: Flächeninhalt zwischen Graph und x-Achse am Bild mit einem berechneten Integralwert vergleichen: 0 GK / 1 LK
    - Fläche: Lösungsschritte zu einem Flächenverhältnis von Segment und Dreieck geometrisch deuten und Flächen einzeichnen: 1 GK / 0 LK
    - Fläche: Lösungsschritte zur Fläche zwischen zwei Scharkurven geometrisch deuten und Parameterungleichung untersuchen: 0 GK / 1 LK
    - Fläche: Parameter einer Geraden aus dem Flächeninhalt zwischen Graph und Gerade bestimmen: 1 GK / 0 LK
    - Fläche: Querschnittsfläche eines Rotationskörpers als doppeltes Integral mit Maßstab berechnen: 1 GK / 0 LK
    - Fläche: Querschnittsfläche zwischen Graph und Streckenzug als Integral minus Trapez und Dreieck berechnen: 1 GK / 0 LK
    - Fläche: Querschnittsfläche zwischen Tangente und Graph als Dreieck minus Integral berechnen und mit der Breite zum Volumen umrechnen: 1 GK / 0 LK
    - Fläche: Senkrechte Gerade zur Halbierung einer Fläche über den Flächenterm bestimmen: 1 GK / 0 LK
    - Fläche: Änderung eines Flächeninhalts beim Ersetzen des Graphen durch die Sehne untersuchen: 1 GK / 0 LK
    - Integralwert: Aussage über zwei Integrale über die Lage des Graphen zur x-Achse beurteilen: 1 GK / 0 LK
    - Integralwert: Existenz eines Flächenstücks mit vorgegebenem Inhalt über die Stammfunktion begründen: 1 GK / 0 LK
    - Integralwert: Integral als Flächeninhalt für alle Scharkurven über das Vorzeichen des Terms beurteilen: 0 GK / 1 LK
    - Integralwert: Integral mit Wert null am Graphen begründen: 0 GK / 1 LK
    - Integralwert: Integral über die Summe aus ungerader Funktion und Konstante ohne Stammfunktion begründen: 0 GK / 1 LK
    - Integralwert: Integral über eine Summe aus e-Funktion und linearem Term gegen eine Schranke nachweisen: 0 GK / 1 LK
    - Integralwert: Integralabschätzung über ein Rechteck und Flächenvergleich am Graphen erläutern und im Sachzusammenhang deuten: 0 GK / 1 LK
    - Integralwert: Integrale der Ableitung über das Vorzeichen des Ableitungsgraphen vergleichen: 1 GK / 0 LK
    - Integralwert: Integralwert grafisch durch Kästchenzählen bestimmen: 1 GK / 0 LK
    - Integralwert: Negativen Integralwert als Differenz zweier Flächeninhalte am Graphen erläutern: 0 GK / 1 LK
    - Integralwert: Näherungswert eines Integrals als Vielecksfläche am Graphen begründen: 1 GK / 0 LK
    - Integralwert: Summe zweier Integrale als Flächeninhalt beurteilen: 1 GK / 0 LK
  - iqb: 36 Zeilen GK / 26 Zeilen LK, 49 Haupttypen
    - Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen: 5 GK / 2 LK
    - Fläche: Fläche zwischen Graph und x-Achse aus zwei Flächenstücken berechnen: 2 GK / 0 LK
    - Fläche: Parameter einer Geraden aus dem Flächeninhalt zwischen Graph und Gerade bestimmen: 1 GK / 1 LK
    - Integralwert: Eindeutige Lösung einer Flächengleichung über die Monotonie des Flächeninhalts begründen: 1 GK / 1 LK
    - Integralwert: Integral mit Wert null am Graphen begründen: 0 GK / 2 LK
    - Integralwert: Integral über die Summe aus ungerader Funktion und Konstante ohne Stammfunktion begründen: 1 GK / 1 LK
    - Integralwert: Integralwert grafisch durch Kästchenzählen bestimmen: 2 GK / 0 LK
    - Integralwert: Näherungswert eines Integrals als Vielecksfläche am Graphen begründen: 2 GK / 0 LK
    - Fläche: Achsenschnittpunkt einer Geraden aus einer Flächenbedingung über Rechteck und Dreieck bestimmen: 0 GK / 1 LK
    - Fläche: Aufgabenstellung zu einem Volumen aus Fläche zwischen Graph und Gerade und Maßstab formulieren und erläutern: 1 GK / 0 LK
    - Fläche: Aufgabenstellung zu einer Summe zweier Integrale formulieren und die Integrale als Teilflächen im Sachzusammenhang deuten: 1 GK / 0 LK
    - Fläche: Aussage über den Flächeninhalt zwischen zwei Scharkurven als Parameterungleichung untersuchen: 0 GK / 1 LK
    - Fläche: Fläche zwischen Graph und Hochpunktgerade über eine Periode berechnen: 1 GK / 0 LK
    - Fläche: Fläche zwischen Graph und Koordinatenachsen berechnen: 1 GK / 0 LK
    - Fläche: Fläche zwischen Graph und zwei Tangenten berechnen: 0 GK / 1 LK
    - Fläche: Fläche zwischen Graph, x-Achse und waagerechter Gerade aus Rechteck und Integral berechnen: 0 GK / 1 LK
    - Fläche: Flächeninhalt aus einem vorgegebenen Term mit Stammfunktion berechnen: 0 GK / 1 LK
    - Fläche: Flächeninhalt einer Vorderansicht als Integral mit Maßstab und Abzug berechnen: 0 GK / 1 LK
    - Fläche: Flächeninhalt zwischen Graph und waagerechter Gerade als Term in der Grenze nachweisen: 1 GK / 0 LK
    - Fläche: Flächeninhalt zwischen Graph, Achse und zwei Parallelen über Rechtecke und Integral berechnen: 0 GK / 1 LK
    - Fläche: Flächeninhalt zwischen Graph, x-Achse und senkrechter Gerade im Sachzusammenhang mit Maßstab berechnen: 0 GK / 1 LK
    - Fläche: Flächeninhalt zwischen Graph, x-Achse und senkrechter Gerade über das Integral nachweisen: 0 GK / 1 LK
    - Fläche: Flächenstück zwischen zwei Scharkurven und der x-Achse markieren und Gleichung für den Parameter aus dem Flächeninhalt angeben: 1 GK / 0 LK
    - Fläche: Gerade zur Halbierung der Fläche zwischen Scharkurve und Koordinatenachsen ermitteln: 0 GK / 1 LK
    - Fläche: Parallele Gerade zur Halbierung einer Fläche über ein Achsendreieck bestimmen: 1 GK / 0 LK
    - Fläche: Prozentuale Abweichung einer Dreiecksnäherung vom Flächeninhalt zwischen Scharkurve und Achsen als parameterunabhängig nachweisen: 0 GK / 1 LK
    - Fläche: Radius eines flächengleichen Halbkreisprofils aus einem Integral bestimmen und Materialmasse berechnen: 1 GK / 0 LK
    - Fläche: Senkrechte Gerade zur Halbierung einer Fläche über den Flächenterm bestimmen: 1 GK / 0 LK
    - Fläche: Verschiebung für die Halbierung einer Fläche über ein Integral bestimmen: 1 GK / 0 LK
    - Fläche: Wasservolumen in einer Mulde aus Fläche zwischen Wasserlinie und Graph mal Breite berechnen: 0 GK / 1 LK
    - Integralwert: Anzahl der Lösungen einer Integralgleichung über gleitende Streifen am Graphen untersuchen: 0 GK / 1 LK
    - Integralwert: Existenz einer Grenze mit Integralwert null über den Vorzeichenwechsel und die Stetigkeit am Graphen begründen: 1 GK / 0 LK
    - Integralwert: Existenz einer oberen Grenze mit Integralwert null über den Flächenausgleich ohne Rechnung begründen: 1 GK / 0 LK
    - Integralwert: Flächenterm einer an y = x gespiegelten Figur über Rechteck und Integral begründen: 0 GK / 1 LK
    - Integralwert: Grenzen für ein positives Produkt zweier Integrale über die Vorzeichen der Hyperbeläste angeben und begründen: 1 GK / 0 LK
    - Integralwert: Integral als Flächeninhalt für alle Scharkurven über das Vorzeichen des Terms beurteilen: 0 GK / 1 LK
    - Integralwert: Integral als Flächeninhalt zwischen Graph und x-Achse deuten und über die Stammfunktion berechnen: 1 GK / 0 LK
    - Integralwert: Integral einer Differenzfunktion grafisch abschätzen: 1 GK / 0 LK
    - Integralwert: Integral null über die Punktsymmetrie begründen: 1 GK / 0 LK
    - Integralwert: Integral über die Punktsymmetrie zum Wendepunkt als Dreiecksfläche unter einer Sekante begründen: 1 GK / 0 LK
    - Integralwert: Integralabschätzung über ein Rechteck und Flächenvergleich am Graphen erläutern und im Sachzusammenhang deuten: 0 GK / 1 LK
    - Integralwert: Integralwert über die Punktsymmetrie und ein Quadrat geometrisch begründen: 0 GK / 1 LK
    - Integralwert: Lösung einer Integralgleichung über die Punktsymmetrie und ein Rechteck am Graphen begründen: 1 GK / 0 LK
    - Integralwert: Nullwert eines Integrals über eine Differenzfunktion mit drei Schnittstellen als Flächengleichheit deuten: 1 GK / 0 LK
    - Integralwert: Summe zweier Integrale als Flächeninhalt beurteilen: 1 GK / 0 LK
    - Integralwert: Ungleichung zweier Integrale über das Vorzeichen des Teilintegrals am Graphen begründen: 1 GK / 0 LK
    - Integralwert: Vorgehen zur grafischen Bestimmung eines Integrals beschreiben: 1 GK / 0 LK
    - Integralwert: Vorzeichen eines Differenzintegrals über Flächenvergleich am Graphen begründen und im Sachzusammenhang deuten: 0 GK / 1 LK
    - Integralwert: Vorzeichen eines Integrals am Graphen beurteilen: 0 GK / 1 LK
  - fhr: 20 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: GK-Block und LK-Block; Typenzeilen: 64 GK / 40 LK)

### flaecheninhalt-und-volumen-im-raum
- Geltung je Zielprüfung:
  - Thema „Flächeninhalt und Volumen im Raum“ (`themen.csv`):
    - be-gk: ja – `| Flächeninhalt und Volumen im Raum | ja |` [abi-be-gk-geltung.md Zeile 44]
    - be-lk: ja – `| Flächeninhalt und Volumen im Raum | ja |` [abi-be-lk-geltung.md Zeile 44]
    - bb-gk: ja – `| Flächeninhalt und Volumen im Raum | ja |` [abi-bb-gk-geltung.md Zeile 44]
    - bb-ea: ja – `| Flächeninhalt und Volumen im Raum | ja |` [abi-bb-ea-geltung.md Zeile 44]
- Lerneinheiten:
  - 1. Dreiecksflächen
    - Eintrag, Zeile 11: „(Q3, GK-Kern „Flächeninhalte von geometrischen Objekten“; OHiMi 2.3 „Flächenberechnung: Dreieck“)“
    - GOST Berlin [Zeilen 1139–1140]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometrischen Objekten anwenden,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1257–1258]: „Flächeninhalte von geometrischen Objekte, die durch Koordinaten und mit Vek-“
      Q3, Grund- und Leistungskursfach
  - 2. Vierecksflächen
    - Eintrag, Zeile 12: „(Q3, GK-Kern; OHiMi 2.3 „Rechteck“; Trapez- und Rautenformel in FS-IQB 1.1)“
    - GOST Berlin [Zeilen 1139–1140]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometrischen Objekten anwenden,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1257–1258]: „Flächeninhalte von geometrischen Objekte, die durch Koordinaten und mit Vek-“
      Q3, Grund- und Leistungskursfach
  - 3. Volumen und Oberfläche von Pyramide und Prisma: Grundfläche mal Höhe, bei der Pyramide der Faktor ein Drittel; die Höhe als Abstand der Spitze zur Grundflächenebene (waagerechte Grundfläche: z-Differenz; senkrechte Kante über Skalarprodukte erkennen); die Grundfläche aus den Kästen eins und zwei (Drachen, Trapez, Raute, rechtwinkliges Dreieck); Oberflächen (Seitenhöhe über Pythagoras
    - Eintrag, Zeile 13: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1139–1140]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometrischen Objekten anwenden,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1255–1256]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometri-“
      Q3, Grund- und Leistungskursfach
    - Ermessen: Volumen und Oberfläche von Körpern nennt der GOST-Text beider Länder in der Analytischen Geometrie nicht; zugeordnet ist die Zeile zum Arbeiten mit ebenflächig begrenzten Objekten.
  - 4. Zusammengesetzte Körper, Verhältnisse und Parameter: Zerlegen und Ergänzen (Differenz zweier Pyramiden am abgeschnittenen Quader, Quader plus Dachprisma, Prisma plus Pyramide, vorgelegte Volumenterme Faktor für Faktor deuten), Volumenverhältnisse ohne Zahlenwerte (Formeln dividieren, Anteile am Quader begründen), Ähnlichkeit (der parallele Schnitt trennt eine ähnliche Teilpyramide ab
    - Eintrag, Zeile 14: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1139–1140]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometrischen Objekten anwenden,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1255–1256]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometri-“
      Q3, Grund- und Leistungskursfach
    - Ermessen: Wie Einheit 3: zusammengesetzte Körper und Volumenverhältnisse stehen in keinem Plan.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 14 Zeilen GK / 12 Zeilen LK, 22 Haupttypen
    - Ebene Figur: Parameter einer Ecke aus dem Flächeninhalt eines gleichschenkligen Dreiecks bestimmen: 2 GK / 0 LK
    - Körper: Kürzeste und längste Kante und Volumen einer Pyramide über einem Drachenviereck berechnen: 1 GK / 1 LK
    - Körper: Pyramidenvolumen aus Grundfläche und Höhe berechnen: 1 GK / 1 LK
    - Körper: Trapezgrundfläche nachweisen und Pyramidenvolumen berechnen: 1 GK / 1 LK
    - Ebene Figur: Eckpunkte eines gleichschenkligen Trapezes aus einem Flächenverhältnis zum Quadrat bestimmen: 1 GK / 0 LK
    - Ebene Figur: Flächeninhalt eines Dreiecks aus den Spurpunkten einer Ebene berechnen: 0 GK / 1 LK
    - Ebene Figur: Flächeninhalt eines Trapezes im Raum über die Höhe zwischen den parallelen Seiten berechnen: 1 GK / 0 LK
    - Ebene Figur: Flächeninhalt eines gleichschenkligen Dreiecks über die Höhe zur Basis berechnen: 0 GK / 1 LK
    - Ebene Figur: Flächenterm eines Dreiecks als Quadrat minus Randdreiecke in der Abbildung veranschaulichen: 0 GK / 1 LK
    - Ebene Figur: Flächenverhältnis von Dreieck und Trapez über einen Vektorterm ermitteln: 1 GK / 0 LK
    - Ebene Figur: Flächenverhältnis zweier Quadrate aus den Seitenlängen nachweisen: 1 GK / 0 LK
    - Ebene Figur: Innenwinkel einer Raute und Gesamtfläche der Dachflächen berechnen: 1 GK / 0 LK
    - Ebene Figur: Trapezfläche zwischen einer geneigten Ebene und einer waagerechten Ebene in einem Quader berechnen: 1 GK / 0 LK
    - Körper: Ebene parallel zu einer Koordinatenebene zur Halbierung eines Pyramidenvolumens über die Ähnlichkeit bestimmen: 0 GK / 1 LK
    - Körper: Oberflächeninhalt einer quadratischen Pyramide berechnen: 0 GK / 1 LK
    - Körper: Rotationskörper einer Scharfläche als halben Kegel beschreiben und Volumen bestimmen: 0 GK / 1 LK
    - Körper: Volumen aus Prisma und aufgesetzter Pyramide berechnen: 0 GK / 1 LK
    - Körper: Volumen eines Teilkörpers eines Würfels berechnen: 0 GK / 1 LK
    - Körper: Volumen zweier Pyramiden vergleichen und prozentualen Mehrwert berechnen: 0 GK / 1 LK
    - Körper: Volumenansatz als Differenz zweier Pyramiden erläutern und Parameter bestimmen: 1 GK / 0 LK
    - Körper: Volumenterm eines Dachs als Pyramide minus Eckpyramiden begründen: 1 GK / 0 LK
    - Körper: Volumenverhältnis zweier Körper über Formeln ohne Zahlenwerte ermitteln: 1 GK / 0 LK
  - iqb: 30 Zeilen GK / 22 Zeilen LK, 45 Haupttypen
    - Ebene Figur: Flächeninhalt eines gleichschenkligen Dreiecks über die Höhe zur Basis berechnen: 2 GK / 2 LK
    - Ebene Figur: Parameter eines Punktes aus einer Flächengleichheit bestimmen: 1 GK / 1 LK
    - Körper: Höhe einer Pyramide aus dem Volumen bestimmen: 1 GK / 1 LK
    - Körper: Kürzeste und längste Kante und Volumen einer Pyramide über einem Drachenviereck berechnen: 1 GK / 1 LK
    - Körper: Volumen eines Teilkörpers als Differenz zweier Pyramiden berechnen und erläutern: 1 GK / 1 LK
    - Ebene Figur: Diagonalenschnittpunkt und Flächeninhalt eines Quadrats aus dem Spurpunkt einer Geraden bestimmen: 1 GK / 0 LK
    - Ebene Figur: Flächenformel einer Raute als halbes Diagonalenprodukt mit einer Skizze begründen: 1 GK / 0 LK
    - Ebene Figur: Flächengleichheit zweier Dreiecke mit gemeinsamer Seite über gleiche Höhen an einer Skizze begründen: 0 GK / 1 LK
    - Ebene Figur: Flächeninhalt eines Dreiecks aus den Spurpunkten einer Ebene berechnen: 0 GK / 1 LK
    - Ebene Figur: Flächeninhalt eines Rechtecks aus Kantenlängen berechnen und rechten Winkel zweier Flächen prüfen: 0 GK / 1 LK
    - Ebene Figur: Flächeninhalt eines Trapezes im Raum über die Höhe zwischen den parallelen Seiten berechnen: 1 GK / 0 LK
    - Ebene Figur: Flächeninhalt eines ebenen Vierecks mit zwei parallelen senkrechten Seiten aus Seitenlänge und Pfahlabstand berechnen: 0 GK / 1 LK
    - Ebene Figur: Flächeninhalt eines rechtwinkligen Dreiecks über die Kathetenlängen nachweisen: 0 GK / 1 LK
    - Ebene Figur: Flächenterm eines Dreiecks als Quadrat minus Randdreiecke in der Abbildung veranschaulichen: 0 GK / 1 LK
    - Ebene Figur: Flächenterm eines Vierecks als Rechteck plus rechtwinkliges Dreieck erläutern: 1 GK / 0 LK
    - Ebene Figur: Flächenverhältnis von Dreieck und Trapez über einen Vektorterm ermitteln: 1 GK / 0 LK
    - Ebene Figur: Innenwinkel einer Raute und Gesamtfläche der Dachflächen berechnen: 1 GK / 0 LK
    - Ebene Figur: Kongruenz aller Dreiecke aus Raumdiagonale, Flächendiagonale und Kante begründen und Flächeninhalt berechnen: 0 GK / 1 LK
    - Ebene Figur: Parameter aus Seitenlänge und Flächeninhalt eines Rechtecks bestimmen: 1 GK / 0 LK
    - Ebene Figur: Parameter einer Ecke aus dem Flächeninhalt eines gleichschenkligen Dreiecks bestimmen: 1 GK / 0 LK
    - Ebene Figur: Schattendreieck in der Grundebene zeichnen und seinen Flächeninhalt berechnen: 1 GK / 0 LK
    - Ebene Figur: Teilverhältnis auf einer Kante deuten und Teilfläche eines Rechtecks berechnen: 0 GK / 1 LK
    - Ebene Figur: Zuschauerzahl aus dem Flächeninhalt eines Trapezes im Raum und dem Platzbedarf berechnen: 0 GK / 1 LK
    - Körper: Füllvolumen eines gedrehten Behälters am Graphen ergänzen und Grenzwinkel deuten: 1 GK / 0 LK
    - Körper: Höhe eines Prismas aus dem Mantelflächeninhalt bestimmen: 1 GK / 0 LK
    - Körper: Oberflächeninhalt des Rotationskegels eines rechtwinkligen Dreiecks berechnen: 1 GK / 0 LK
    - Körper: Oberflächeninhalt einer quadratischen Pyramide berechnen: 0 GK / 1 LK
    - Körper: Oberflächeninhalt eines Prismas über einem rechtwinkligen Dreieck berechnen: 1 GK / 0 LK
    - Körper: Parameter für das größte Volumen einer Pyramide bestimmen: 1 GK / 0 LK
    - Körper: Parameter für einen Volumenanteil zweier gegenläufiger Pyramiden im Quader bestimmen: 1 GK / 0 LK
    - Körper: Passung eines Zylinders in ein Gefäß über die Höhe aus dem Volumen prüfen: 1 GK / 0 LK
    - Körper: Rechteck als Quadrat ausschließen und Volumen einer Pyramide über dem Rechteck berechnen: 0 GK / 1 LK
    - Körper: Rotationskörper einer Scharfläche als halben Kegel beschreiben und Volumen bestimmen: 0 GK / 1 LK
    - Körper: Trapezgrundfläche nachweisen und Pyramidenvolumen berechnen: 0 GK / 1 LK
    - Körper: Volumen aus Prisma und aufgesetzter Pyramide berechnen: 0 GK / 1 LK
    - Körper: Volumen einer Pyramide über einem rechtwinkligen Dreieck mit Pythagoras berechnen: 1 GK / 0 LK
    - Körper: Volumen eines Hauses als Quader plus Dachprisma mit Trapezquerschnitt berechnen: 1 GK / 0 LK
    - Körper: Volumen eines Prismas mit Trapezquerschnitt im Sachzusammenhang berechnen und mit einer Vorgabe vergleichen: 1 GK / 0 LK
    - Körper: Volumen eines Prismas über einer Raute berechnen: 1 GK / 0 LK
    - Körper: Volumen eines Teilkörpers eines Würfels berechnen: 0 GK / 1 LK
    - Körper: Volumen eines geraden Prismas über einem Dreieck nachweisen: 1 GK / 0 LK
    - Körper: Volumenanteil einer Pyramide am Quader ohne Volumenberechnung begründen: 0 GK / 1 LK
    - Körper: Volumenrechnung eines Prismas aus einem Lösungsweg erläutern: 1 GK / 0 LK
    - Körper: Volumenverhältnis zweier Körper über Formeln ohne Zahlenwerte ermitteln: 1 GK / 0 LK
    - Körper: Volumenverlauf eines Restkörpers in Abhängigkeit vom Parameter als linear begründen und Graphen zuordnen: 1 GK / 0 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 44 GK / 34 LK)

### funktionsklassen-und-eigenschaften
- Geltung je Zielprüfung:
  - Thema „Funktionsklassen und Eigenschaften“ (`themen.csv`):
    - be-gk: ja – `| Funktionsklassen und Eigenschaften | ja |` [abi-be-gk-geltung.md Zeile 17]
    - be-lk: ja – `| Funktionsklassen und Eigenschaften | ja |` [abi-be-lk-geltung.md Zeile 17]
    - bb-gk: ja – `| Funktionsklassen und Eigenschaften | ja |` [abi-bb-gk-geltung.md Zeile 17]
    - bb-ea: ja – `| Funktionsklassen und Eigenschaften | ja |` [abi-bb-ea-geltung.md Zeile 17]
- Lerneinheiten:
  - 1. Funktionswert und Punkt
    - Eintrag, Zeile 11: „(Q1, GK-Kern „Funktionseigenschaften, auch in Anwendungszusammenhängen“; FOS „Funktionsbegriff“, „Achsenschnittpunkte“; OHiMi 2.2 …“
    - GOST Berlin [Zeilen 1165–1166]: „Potenzfunktionen mit ganzzahligen Exponenten, ganzrationale und Exponentialfunktionen zur Beschreibung und Untersuchung quantifizierbarer Zusammen-“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 923–924]: „Funktionen zur Beschreibung und Untersuchung quantifizierbarer Zusam-“
      Q1, Grund- und Leistungskursfach
  - 2. Nullstellen
    - Eintrag, Zeile 12: „(Q1, GK-Kern „Nullstellen“, „Schnittpunkte mit den Koordinatenachsen“; FOS „Lösungsverfahren ganzrationaler Gleichungen“, „Nullstellen und …“
    - GOST Berlin [Zeilen 1165–1166]: „Potenzfunktionen mit ganzzahligen Exponenten, ganzrationale und Exponentialfunktionen zur Beschreibung und Untersuchung quantifizierbarer Zusammen-“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 929]: „Nullstellen“
      Q1, Grund- und Leistungskursfach
  - 3. Definitionsbereich, Wertemenge und Schranken: den größtmöglichen Definitionsbereich einer Logarithmusfunktion aus der Bedingung Argument größer null, auch mit Parameter; Wertemengen am Term ablesen (e-Funktion positiv und nie null, Sinus zwischen minus eins und plus eins, Quadrat ab null), bei Verkettungen von innen nach außen; Schranken über das Vorzeichen des e-Terms begründen (der Grenzwert wird nicht angenommen); Werte und ihre Häufigkeit auf einer Periode; Abschätzungen gegen die x-Achse. (Q1, GK-Kern „Definitions- und Wertebereich“; LK-Zusatz ln als Funktionsklasse; FOS „Funktionsbegriff“ mit „Definitions- und Wertebereich“, ohne eigene fhr-Zeile; OHiMi 2.2 „Definitionsbereich, Wertebereich“) ← Eingabe „definitionsbereich“, „wertemenge“, „wertebereich“, „schranke“, „nie null“
    - Eintrag, Zeile 13: „(Q1, GK-Kern „Definitions- und Wertebereich“; LK-Zusatz ln als Funktionsklasse; FOS „Funktionsbegriff“ mit „Definitions- und Wertebereich“, ohne eigene fhr-Zeile; OHiMi 2.2 …“
    - GOST Berlin [Zeilen 1165–1166]: „Potenzfunktionen mit ganzzahligen Exponenten, ganzrationale und Exponentialfunktionen zur Beschreibung und Untersuchung quantifizierbarer Zusammen-“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Berlin [Zeilen 1200–1201]: „Wurzelfunktionen, gebrochenrationale Funktionen und Funktionen wie ln, sin, cos zur Beschreibung und Untersuchung quantifizierbarer Zusammenhänge nutzen, Q1/2“
      Funktionaler Zusammenhang [L4], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeile 928]: „Definitions- und Wertebereich“
      Q1, Grund- und Leistungskursfach
    - Ermessen: Der größtmögliche Definitionsbereich einer Logarithmusfunktion setzt die ln-Funktion voraus; sie steht in Berlin im LK-Zusatz, in Brandenburg im LK-Zusatz des ersten Kurshalbjahrs.
  - 4. Symmetrie
    - Eintrag, Zeile 14: „(Q1, GK-Kern „Punktsymmetrie bzgl. des Koordinatenursprungs und Axialsymmetrie bzgl. der Ordinatenachse“; FOS „Symmetrie bezüglich y-Achse …“
    - GOST Berlin [Zeilen 1165–1166]: „Potenzfunktionen mit ganzzahligen Exponenten, ganzrationale und Exponentialfunktionen zur Beschreibung und Untersuchung quantifizierbarer Zusammen-“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 932–933]: „Punktsymmetrie bzgl. des Koordinatenursprungs und“
      Q1, Grund- und Leistungskursfach
  - 5. Transformationen
    - Eintrag, Zeile 15: „(Q1, GK-Kern „Sinus- und Kosinusfunktionen: Einfluss der Parameter auf den Verlauf der Funktionsgraphen“; OHiMi 2.2 „Zusammenhang zwischen …“
    - GOST Berlin [Zeilen 1165–1166]: „Potenzfunktionen mit ganzzahligen Exponenten, ganzrationale und Exponentialfunktionen zur Beschreibung und Untersuchung quantifizierbarer Zusammen-“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 941–942]: „Einfluss der Parameter auf den Verlauf der Funktionsgraphen“
      Q1, Grund- und Leistungskursfach
  - 6. Graph und Term
    - Eintrag, Zeile 16: „(Q1, GK-Kern „Funktionseigenschaften“; FOS „Wertetabelle, Darstellung der Funktionsgraphen“; OHiMi 2.2 „qualitative Beschreibung des Verlaufs …“
    - GOST Berlin [Zeilen 1165–1166]: „Potenzfunktionen mit ganzzahligen Exponenten, ganzrationale und Exponentialfunktionen zur Beschreibung und Untersuchung quantifizierbarer Zusammen-“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 926–927]: „Funktionseigenschaften, auch in Anwendungszusammenhängen:“
      Q1, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 34 Zeilen GK / 19 Zeilen LK, 33 Haupttypen
    - Nullstellen und Werte: Punkt, Nullstelle oder Schnittstelle durch Einsetzen nachweisen: 4 GK / 2 LK
    - Symmetrie: Symmetrieart am Term über die Exponenten begründen: 3 GK / 3 LK
    - Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen: 3 GK / 1 LK
    - Nullstellen und Werte: Nullstelle und y-Achsenschnittpunkt eines Produkts mit e-Funktion angeben: 3 GK / 0 LK
    - Transformation: Abbildung zwischen zwei Graphen angeben: 1 GK / 2 LK
    - Nullstellen und Werte: Definitionsbereich einer Logarithmusfunktion angeben: 0 GK / 2 LK
    - Nullstellen und Werte: Nullstellen einer ganzrationalen Funktion durch Ausklammern und Faktorisieren berechnen: 2 GK / 0 LK
    - Nullstellen und Werte: Vertikalen Abstand zweier Punkte als Differenz von Funktionswerten berechnen: 1 GK / 1 LK
    - Extrempunkte: Abstand von Extrempunkten einer gestreckten Sinusfunktion vergleichen: 1 GK / 0 LK
    - Extrempunkte: Flächeninhalt eines Dreiecks aus Extrempunkten der Sinusfunktion berechnen: 1 GK / 0 LK
    - Nullstellen und Werte: Nullstelle über die Symmetrie begründen und übrige Nullstellen einer biquadratischen Funktion bestimmen: 1 GK / 0 LK
    - Nullstellen und Werte: Nullstellen aus Linearfaktoren im Sachzusammenhang nennen und ihre Vollständigkeit über die Faktorstruktur begründen: 0 GK / 1 LK
    - Nullstellen und Werte: Nullstellen aus der faktorisierten Form angeben: 1 GK / 0 LK
    - Nullstellen und Werte: Nullstellenfreiheit und Wertemenge einer e-Funktion aus dem Term begründen: 1 GK / 0 LK
    - Nullstellen und Werte: Passenden Graphen zu einem Funktionsterm über Funktionswerte auswählen: 1 GK / 0 LK
    - Nullstellen und Werte: Schnittpunkt mit der y-Achse und Steigung des Graphen dort angeben: 0 GK / 1 LK
    - Nullstellen und Werte: Schnittpunkte des Graphen mit beiden Koordinatenachsen berechnen: 1 GK / 0 LK
    - Nullstellen und Werte: Zurückgelegten Weg aus Hin- und Rückbewegung über Funktionswerte berechnen: 1 GK / 0 LK
    - Nullstellen und Werte: y-Achsenschnittpunkt angeben und Anzahl der Nullstellen aus der faktorisierten Form ermitteln: 1 GK / 0 LK
    - Symmetrie: Fehlende Punktsymmetrie aus der Wertemenge begründen: 0 GK / 1 LK
    - Symmetrie: Höhe einer waagerechten Sekante aus dem Abstand ihrer Schnittpunkte über die Symmetrie bestimmen: 0 GK / 1 LK
    - Symmetrie: Punktsymmetrie über f(−x) = −f(x) nachweisen, eindeutige Nullstelle begründen und Grenzwert angeben: 0 GK / 1 LK
    - Transformation: An der x-Achse gespiegelte Funktion angeben und Durchmesser aus dem Funktionswert mit Maßstab berechnen: 1 GK / 0 LK
    - Transformation: Aussage über eine Verschiebung zwischen zwei Graphen beurteilen: 1 GK / 0 LK
    - Transformation: Funktionsterm nach Verschiebung in x-Richtung durch den Ursprung ermitteln: 1 GK / 0 LK
    - Transformation: Graphen einer periodischen Funktion mit vorgegebenem Maximum und Periode skizzieren: 0 GK / 1 LK
    - Transformation: Periode einer Kosinusfunktion im Sachzusammenhang deuten und Stelle stärkster Zunahme am Graphen angeben: 0 GK / 1 LK
    - Transformation: Streckfaktor aus einer Flächenbedingung für den gestauchten Graphen bestimmen: 1 GK / 0 LK
    - Transformation: Streckfaktor und Verschiebung aus zwei Termen durch Koeffizientenvergleich ermitteln und die Abbildung beschreiben: 1 GK / 0 LK
    - Transformation: Terme der an den Koordinatenachsen gespiegelten Randlinien angeben: 1 GK / 0 LK
    - Transformation: Um 90° gedrehte Gerade und Bildpunkt einer Drehung um den Ursprung angeben: 1 GK / 0 LK
    - Transformation: Verschiebung einer Geraden aus dem Abstand der parallelen Geraden über das Steigungsdreieck ermitteln: 1 GK / 0 LK
    - Transformation: Wertemenge einer transformierten Funktion begründen: 0 GK / 1 LK
  - iqb: 58 Zeilen GK / 41 Zeilen LK, 73 Haupttypen
    - Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen: 4 GK / 4 LK
    - Symmetrie: Symmetrieart am Term über die Exponenten begründen: 2 GK / 3 LK
    - Transformation: Abbildung zwischen zwei Graphen angeben: 3 GK / 2 LK
    - Extrempunkte: Hochpunkt aus dem Graphen ablesen und im Sachzusammenhang deuten: 1 GK / 1 LK
    - Nullstellen und Werte: Gleichheit zweier Funktionswerte durch Einsetzen im Sachzusammenhang nachweisen: 1 GK / 1 LK
    - Nullstellen und Werte: Passenden Graphen zu einem Funktionsterm über Funktionswerte auswählen: 2 GK / 0 LK
    - Nullstellen und Werte: Punkt, Nullstelle oder Schnittstelle durch Einsetzen nachweisen: 1 GK / 1 LK
    - Nullstellen und Werte: Schnittstellen zweier Graphen im Sachzusammenhang ablesen: 1 GK / 1 LK
    - Nullstellen und Werte: Stelle zu einem vorgegebenen Funktionswert am Graphen ablesen: 1 GK / 1 LK
    - Symmetrie: Punktsymmetrie zum Wendepunkt über die Verschiebung einer ungeraden Funktion begründen: 1 GK / 1 LK
    - Transformation: Graph eines in y-Richtung gestreckten Scharmitglieds begründen und skizzieren: 2 GK / 0 LK
    - Transformation: Periode einer Kosinusfunktion im Sachzusammenhang deuten und Stelle stärkster Zunahme am Graphen angeben: 1 GK / 1 LK
    - Transformation: Verschiebung einer Exponentialfunktion als Streckung nachweisen: 1 GK / 1 LK
    - Transformation: Verschobenen Graphen in die Abbildung skizzieren: 2 GK / 0 LK
    - Extrempunkte: Abstand von Extrempunkten einer gestreckten Sinusfunktion vergleichen: 1 GK / 0 LK
    - Extrempunkte: Existenz eines Hochpunkts aus dem Grad und einem Tiefpunkt begründen und Koordinaten angeben: 1 GK / 0 LK
    - Extrempunkte: Flächeninhalt eines Dreiecks aus Extrempunkten der Sinusfunktion berechnen: 1 GK / 0 LK
    - Extrempunkte: Gerade durch die Hochpunkte einer Kosinusfunktion begründen: 1 GK / 0 LK
    - Nullstellen und Werte: Anfangswert eines Bestands als Funktionswert an der Stelle null berechnen: 1 GK / 0 LK
    - Nullstellen und Werte: Ausdehnung einer Figur in x-Richtung aus der Ausdehnung in y-Richtung über Funktionswerte ermitteln: 1 GK / 0 LK
    - Nullstellen und Werte: Aussage zur Modellgüte über die Summe vorzeichenbehafteter Abweichungen beurteilen: 0 GK / 1 LK
    - Nullstellen und Werte: Aussage über das Verhältnis zweier Funktionswerte durch Einsetzen widerlegen: 0 GK / 1 LK
    - Nullstellen und Werte: Aussage über die Achsenskalierung einer Abbildung beurteilen: 1 GK / 0 LK
    - Nullstellen und Werte: Aussage über eine Rate aus dem Nullabschnitt einer abschnittsweise definierten Funktion begründen: 0 GK / 1 LK
    - Nullstellen und Werte: Bereich mit Funktionswerten über einer Schranke aus dem Graphen bestimmen: 1 GK / 0 LK
    - Nullstellen und Werte: Durchmesser der Grundfläche eines Rotationskörpers aus der Nullstelle der Profilfunktion mit Maßstab nachweisen: 1 GK / 0 LK
    - Nullstellen und Werte: Einhalten einer Schranke über das Vorzeichen des e-Terms begründen: 1 GK / 0 LK
    - Nullstellen und Werte: Funktionswert und Änderungsbeträge zweier Zeitabschnitte im Sachzusammenhang vergleichen: 0 GK / 1 LK
    - Nullstellen und Werte: Geradengleichung aus der Abbildung begründen: 1 GK / 0 LK
    - Nullstellen und Werte: Gesamtlänge aus einer Nullstelle und der Achsensymmetrie im Sachzusammenhang berechnen: 0 GK / 1 LK
    - Nullstellen und Werte: Gleichheit zweier Sachgrößen als Bedingung an den Funktionswert übersetzen und Stelle am Graphen ablesen: 0 GK / 1 LK
    - Nullstellen und Werte: Höhen an den Rändern einer Profillinie als Funktionswerte berechnen: 0 GK / 1 LK
    - Nullstellen und Werte: Lage eines Graphen unterhalb der x-Achse über eine Logarithmus-Abschätzung beurteilen: 0 GK / 1 LK
    - Nullstellen und Werte: Länge der Verbindungsstrecke zweier Graphenpunkte als Näherung der Bogenlänge berechnen: 0 GK / 1 LK
    - Nullstellen und Werte: Minimalwert einer verschobenen Sinusfunktion begründen: 0 GK / 1 LK
    - Nullstellen und Werte: Nullstelle null am Term ohne konstanten Summanden begründen: 1 GK / 0 LK
    - Nullstellen und Werte: Nullstellen aus Linearfaktoren im Sachzusammenhang nennen und ihre Vollständigkeit über die Faktorstruktur begründen: 0 GK / 1 LK
    - Nullstellen und Werte: Nullstellen berechnen und Grenzverhalten einer ganzrationalen Funktion angeben: 1 GK / 0 LK
    - Nullstellen und Werte: Nullstellenfreiheit und Wertemenge einer e-Funktion aus dem Term begründen: 1 GK / 0 LK
    - Nullstellen und Werte: Prozentuale Abweichung eines Modellwerts vom Messwert berechnen: 1 GK / 0 LK
    - Nullstellen und Werte: Punktprobe an einer Geraden rechnerisch zeigen und Gerade einzeichnen: 1 GK / 0 LK
    - Nullstellen und Werte: Schnittpunkt mit der y-Achse und Steigung des Graphen dort angeben: 1 GK / 0 LK
    - Nullstellen und Werte: Stelle zu einem Funktionswert am Graphen im Sachzusammenhang ablesen: 1 GK / 0 LK
    - Nullstellen und Werte: Summe von Funktionswerten mit Maßstab als Gesamtlänge im Sachzusammenhang deuten: 0 GK / 1 LK
    - Nullstellen und Werte: Tiefstelle und Stelle zu einem Funktionswert am Graphen im Sachzusammenhang ablesen: 1 GK / 0 LK
    - Nullstellen und Werte: Ungleichung für einen Funktionswert im Sachzusammenhang deuten: 0 GK / 1 LK
    - Nullstellen und Werte: Wert einer Funktion berechnen und die zugehörige Stelle einer zweiten Funktion am Graphen ablesen: 0 GK / 1 LK
    - Nullstellen und Werte: Wertemenge einer verketteten e-Funktion angeben: 1 GK / 0 LK
    - Nullstellen und Werte: Wertemenge und Häufigkeit der Werte einer Sinusfunktion auf einer Periode angeben: 1 GK / 0 LK
    - Nullstellen und Werte: Zeitliche Entwicklung eines Bestands über ein Intervall grafisch darstellen: 1 GK / 0 LK
    - Nullstellen und Werte: Zurückgelegten Weg aus Hin- und Rückbewegung über Funktionswerte berechnen: 1 GK / 0 LK
    - Nullstellen und Werte: y-Achsenabschnitt einer Geraden durch einen festen Punkt als Term in der Steigung angeben: 1 GK / 0 LK
    - Symmetrie: Fehlende Punktsymmetrie aus der Wertemenge begründen: 0 GK / 1 LK
    - Symmetrie: Höhe einer waagerechten Sekante aus dem Abstand ihrer Schnittpunkte über die Symmetrie bestimmen: 0 GK / 1 LK
    - Symmetrie: Punktsymmetrie über f(−x) = −f(x) nachweisen, eindeutige Nullstelle begründen und Grenzwert angeben: 0 GK / 1 LK
    - Symmetrie: Symmetrie eines Produkts symmetrischer Funktionen allgemein nachweisen: 0 GK / 1 LK
    - Symmetrie: Weiteren Extrempunkt aus der Symmetrie des Graphen angeben: 0 GK / 1 LK
    - Symmetrie: Weiteren Wendepunkt über die Punktsymmetrie ohne Rechnung begründen: 1 GK / 0 LK
    - Transformation: Ableitungswert einer verschobenen Funktion über die Ausgangsfunktion berechnen: 1 GK / 0 LK
    - Transformation: Anzahl verschiedener Ergebnisse bei vertauschter Reihenfolge von Spiegelung und Verschiebungen begründen: 1 GK / 0 LK
    - Transformation: Aussage über eine Verschiebung zwischen zwei Graphen beurteilen: 1 GK / 0 LK
    - Transformation: Bild des Graphen unter Spiegelung, Streckung und Verschiebung als Ableitungsgraph nachweisen: 1 GK / 0 LK
    - Transformation: Extrempunkt eines transformierten Graphen angeben: 0 GK / 1 LK
    - Transformation: Funktionsterm nach Streckung in x-Richtung und Verschiebung angeben: 1 GK / 0 LK
    - Transformation: Graph einer gestreckten und verschobenen Potenzfunktion skizzieren: 1 GK / 0 LK
    - Transformation: Graphen einer periodischen Funktion mit vorgegebenem Maximum und Periode skizzieren: 0 GK / 1 LK
    - Transformation: Integrationsgrenzen und Faktor für ein Integral über den transformierten Graphen bestimmen: 1 GK / 0 LK
    - Transformation: Streckfaktoren aus dem Term ablesen und Flächengleichheit der Bilddreiecke über das Produkt der Faktoren beurteilen: 0 GK / 1 LK
    - Transformation: Streckfaktoren aus der Zuordnung zweier Punkte deuten und berechnen: 1 GK / 0 LK
    - Transformation: Term und Intervall des an der y-Achse gespiegelten Graphen angeben: 0 GK / 1 LK
    - Transformation: Verschiebung und Streckung der Grundhyperbel aus dem Term beschreiben: 1 GK / 0 LK
    - Transformation: Wertebereich einer gestreckten und verschobenen Sinusfunktion angeben: 1 GK / 0 LK
    - Transformation: Wertemenge einer transformierten Funktion begründen: 0 GK / 1 LK
  - fhr: 48 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: GK-Block und LK-Block; Typenzeilen: 92 GK / 60 LK)

### funktionsscharen-und-ortskurven
- Geltung je Zielprüfung:
  - Thema „Funktionsscharen und Ortskurven“ (`themen.csv`):
    - be-gk: nein – `| Funktionsscharen und Ortskurven | nein |` [abi-be-gk-geltung.md Zeile 25]
    - be-lk: ja – `| Funktionsscharen und Ortskurven | ja |` [abi-be-lk-geltung.md Zeile 25]
    - bb-gk: nein – `| Funktionsscharen und Ortskurven | nein |` [abi-bb-gk-geltung.md Zeile 25]
    - bb-ea: ja – `| Funktionsscharen und Ortskurven | ja |` [abi-bb-ea-geltung.md Zeile 25]
- Lerneinheiten:
  - 1. Scharbegriff und Parameterwert
    - Eintrag, Zeile 11: „(Q1 LK „Funktionsscharen mit einem Parameter“; Pool prüft auch grundlegend)“
    - GOST Berlin [Zeilen 1202–1203]: „in einfachen Fällen Verknüpfungen und Verkettungen (zwei Funktionsklassen) sowie Scharen von Funktionen zur Beschreibung quantifizierbarer Zusammen-“
      Funktionaler Zusammenhang [L4], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeile 1005]: „Funktionsscharen mit einem Parameter“
      Q1, Zusätzlich im Leistungskursfach
  - 2. Eigenschaften aller Graphen am Term
    - Eintrag, Zeile 12: „(Q1 LK; L4)“
    - GOST Berlin [Zeilen 1202–1203]: „in einfachen Fällen Verknüpfungen und Verkettungen (zwei Funktionsklassen) sowie Scharen von Funktionen zur Beschreibung quantifizierbarer Zusammen-“
      Funktionaler Zusammenhang [L4], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1014–1015]: „in einfachen Fällen Verknüpfungen und Verkettungen von Scharen von“
      Q1, Zusätzlich im Leistungskursfach
  - 3. Extrem- und Wendepunkte mit Parameter
    - Eintrag, Zeile 13: „(Q1 LK; Kriterien aus kurvenuntersuchung.md)“
    - GOST Berlin [Zeilen 1202–1203]: „in einfachen Fällen Verknüpfungen und Verkettungen (zwei Funktionsklassen) sowie Scharen von Funktionen zur Beschreibung quantifizierbarer Zusammen-“
      Funktionaler Zusammenhang [L4], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1006–1007]: „Ortskurven von Extrem- und Wendepunkten“
      Q1, Zusätzlich im Leistungskursfach
  - 4. Parameter aus Bedingungen bestimmen
    - Eintrag, Zeile 14: „(LK-Zusatz Integralrechnung „Bestimmung von Scharparametern … bei gegebenem Volumen oder Flächeninhalt“)“
    - GOST Berlin [Zeilen 1202–1203]: „in einfachen Fällen Verknüpfungen und Verkettungen (zwei Funktionsklassen) sowie Scharen von Funktionen zur Beschreibung quantifizierbarer Zusammen-“
      Funktionaler Zusammenhang [L4], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1014–1015]: „in einfachen Fällen Verknüpfungen und Verkettungen von Scharen von“
      Q1, Zusätzlich im Leistungskursfach
  - 5. Ortskurve und Kurvenvergleich
    - Eintrag, Zeile 15: „(Q1 LK „Ortskurven von Extrem- und Wendepunkten“)“
    - GOST Berlin [Zeilen 1202–1203]: „in einfachen Fällen Verknüpfungen und Verkettungen (zwei Funktionsklassen) sowie Scharen von Funktionen zur Beschreibung quantifizierbarer Zusammen-“
      Funktionaler Zusammenhang [L4], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1006–1007]: „Ortskurven von Extrem- und Wendepunkten“
      Q1, Zusätzlich im Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 1 Zeilen GK / 55 Zeilen LK, 46 Haupttypen
    - Scharparameter aus einem Punkt des Graphen angeben: 0 GK / 4 LK
    - Parameterwerte nach der Anzahl der Extrempunkte über die Lösbarkeit der Extremstellengleichung begründen: 0 GK / 3 LK
    - Fläche zwischen Graph und x-Achse in Abhängigkeit vom Scharparameter berechnen: 0 GK / 2 LK
    - Gemeinsamen Extrempunkt einer Funktionenschar nachweisen: 0 GK / 2 LK
    - Graph der Schar zum Parametervorzeichen über das Grenzverhalten zuordnen: 0 GK / 2 LK
    - Ortskurve der Extrempunkte einer Schar durch Elimination des Parameters bestimmen: 0 GK / 2 LK
    - Scharparameter aus einer Nullstelle und einem Flächeninhalt bestimmen: 0 GK / 2 LK
    - Ableitung einer Schar als Vielfaches der Ableitung eines Scharmitglieds nachweisen: 0 GK / 1 LK
    - Ableitung einer Schar nachweisen und zusammenhängenden Monotoniebereich ohne Rechnung begründen: 0 GK / 1 LK
    - Abstand des Hochpunkts zu den Tiefpunkten einer Schar in Abhängigkeit vom Parameter berechnen: 0 GK / 1 LK
    - Achsenschnittpunkte einer Schar bestimmen und Flächeninhalt des Achsendreiecks als Term im Parameter nachweisen: 0 GK / 1 LK
    - Anzahl der Nullstellen einer Schar in Abhängigkeit vom Parameter über die Diskriminante ermitteln: 0 GK / 1 LK
    - Aussage über den Ableitungsgraphen einer Schar als Tangente an den Scharfgraphen beurteilen: 0 GK / 1 LK
    - Einfluss eines multiplikativen Parameters auf den Graphen im Vergleich mit dem Ausgangsgraphen beschreiben: 1 GK / 0 LK
    - Einzigen Extrempunkt einer Schar mit vorgegebener x-Koordinate nachweisen und y-Koordinate berechnen: 0 GK / 1 LK
    - Extrempunkte aller Scharkurven aus dem Ableitungsgraphen eines Scharmitglieds ohne Rechnung begründen: 0 GK / 1 LK
    - Folgerungen aus gemeinsamen Eigenschaften einer Schar für den Verlauf der Graphen angeben: 0 GK / 1 LK
    - Gemeinsame Punkte aller Graphen einer Schar bestimmen: 0 GK / 1 LK
    - Gemeinsamen und parameterabhängigen Wendepunkt einer Schar nachweisen: 0 GK / 1 LK
    - Genau zwei Nullstellen einer Schar aus der faktorisierten Form begründen und angeben: 0 GK / 1 LK
    - Gleichmäßige Streckung eines Scharfgraphen als Graph einer anderen Scharfunktion nachweisen: 0 GK / 1 LK
    - Grenzverhalten einer Potenzschar nach der Parität des Exponenten begründen: 0 GK / 1 LK
    - Grenzverhalten einer Schar für x → +∞ nach dem Parametervorzeichen angeben: 0 GK / 1 LK
    - Konstanten Abstand von Extrem- und Wendestelle einer Schar nachweisen: 0 GK / 1 LK
    - Mittelpunkte der Strecken zum Ursprung auf einem gegebenen Graphen allgemein nachweisen: 0 GK / 1 LK
    - Nullstellen einer Funktionenschar mit Fallunterscheidung ermitteln: 0 GK / 1 LK
    - Nullstellenfreiheit aller Scharkurven aus dem gemeinsamen Tiefpunktwert beurteilen: 0 GK / 1 LK
    - Ortskurve der Extrempunkte einer Schar als Gerade über Sonderfall und Streckungseigenschaft begründen: 0 GK / 1 LK
    - Parameter des Extrempunkts mit kleinstem Abstand zum Ursprung an der Ortskurve näherungsweise erläutern und angeben: 0 GK / 1 LK
    - Parameterwert für genau eine waagerechte Tangente bestimmen: 0 GK / 1 LK
    - Parameterwerte mit waagerechter Tangente über die Lösbarkeit der Ableitungsgleichung untersuchen: 0 GK / 1 LK
    - Punktsymmetrie aller Scharkurven und gemeinsame Tangente im Ursprung nachweisen: 0 GK / 1 LK
    - Scharparameter aus der Differenz zweier Scharfunktionswerte über eine Potenzgleichung bestimmen: 0 GK / 1 LK
    - Scharparameter aus der Flächengleichheit von Quadrat und Flächenstück bestimmen: 0 GK / 1 LK
    - Scharparameter aus einem Punkt bestimmen und Wendepunkt nachweisen: 0 GK / 1 LK
    - Scharparameter für eine vorgegebene Tangente in einem Punkt untersuchen: 0 GK / 1 LK
    - Scharparameter für eine vorgegebene Wendestelle berechnen: 0 GK / 1 LK
    - Scharparameter für einen vorgegebenen Flächeninhalt eines Vierecks aus Hochpunkt und Achsenpunkten bestimmen: 0 GK / 1 LK
    - Schnittwinkel von Scharkurve und Ortskurve als nur von der Ortskurve abhängig begründen: 0 GK / 1 LK
    - Steigung und Achsenschnittpunkt des linearen Sonderfalls einer Schar angeben: 0 GK / 1 LK
    - Tangente im y-Achsenschnittpunkt aufstellen und als gemeinsame Tangente aller Scharkurven begründen: 0 GK / 1 LK
    - Tiefpunkt einer Schar mit zwei Parametern nachweisen und Hochpunkt über die Punktsymmetrie begründen: 0 GK / 1 LK
    - Tiefpunkt oder Sattelpunkt nach der Parität des Exponenten unterscheiden: 0 GK / 1 LK
    - Trapez aus Funktions- und Ableitungswerten einer Schar begründen und Flächengleichheit für k und k + 1 nachweisen: 0 GK / 1 LK
    - Vorzeichen der Funktionswerte einer Schar begründen: 0 GK / 1 LK
    - Waagerechte Tangente aller Scharkurven in einem gemeinsamen Punkt nachweisen: 0 GK / 1 LK
  - iqb: 16 Zeilen GK / 70 Zeilen LK, 76 Haupttypen
    - Scharparameter aus einem Punkt des Graphen angeben: 0 GK / 5 LK
    - Fläche zwischen Graph und x-Achse in Abhängigkeit vom Scharparameter berechnen: 0 GK / 2 LK
    - Gemeinsame Punkte aller Graphen einer Schar bestimmen: 0 GK / 2 LK
    - Graph der Schar zum Parametervorzeichen über das Grenzverhalten zuordnen: 0 GK / 2 LK
    - Hochpunkt einer Parabelschar mit Parameterkoordinaten nachweisen: 1 GK / 1 LK
    - Scharparameter aus einem vorgegebenen Flächeninhalt zwischen Graph und x-Achse berechnen: 1 GK / 1 LK
    - Spiegelung an der x-Achse als Scharmitglied nachweisen: 1 GK / 1 LK
    - Abstand der Hochpunkte zweier benachbarter Scharparabeln berechnen: 1 GK / 0 LK
    - Abstand der y-Achsenabschnitte zweier benachbarter Scharkurven berechnen: 0 GK / 1 LK
    - Abstand des Hochpunkts zu den Tiefpunkten einer Schar in Abhängigkeit vom Parameter berechnen: 0 GK / 1 LK
    - Aussage über den Ableitungsgraphen einer Schar als Tangente an den Scharfgraphen beurteilen: 0 GK / 1 LK
    - Bedingungen für den sprungfreien Übergang von Funktionswert und Ableitung angeben: 0 GK / 1 LK
    - Eignung der Scharfunktionen über die Lage einer dritten Extremstelle beurteilen: 0 GK / 1 LK
    - Einfluss eines additiven Scharparameters auf den Graphen beschreiben: 1 GK / 0 LK
    - Einzigen Wendepunkt einer Schar nachweisen und angeben: 0 GK / 1 LK
    - Existenz von Scharparametern mit beliebig vielen Schnittstellen begründen: 0 GK / 1 LK
    - Extrempunkt einer Schar mit Art nach dem Parametervorzeichen bestimmen: 0 GK / 1 LK
    - Folgerungen aus gemeinsamen Eigenschaften einer Schar für den Verlauf der Graphen angeben: 0 GK / 1 LK
    - Gemeinsamen Punkt von Scharkurve und ihrem Ableitungsgraphen in Abhängigkeit vom Parameter berechnen: 1 GK / 0 LK
    - Genau zwei Nullstellen einer Schar aus der faktorisierten Form begründen und angeben: 0 GK / 1 LK
    - Gleiche Steigung aller Graphen einer Schar im Ursprung nachweisen: 0 GK / 1 LK
    - Gleichmäßige Streckung eines Scharfgraphen als Graph einer anderen Scharfunktion nachweisen: 0 GK / 1 LK
    - Gleichung zwischen Scharparameter und Nullstelle aus der Nullstellenbedingung herleiten: 0 GK / 1 LK
    - Gleichungen eines Bestimmungssystems für Scharparameter im Sachzusammenhang deuten: 0 GK / 1 LK
    - Graph der Schar zu einem Parameterwert in die Abbildung skizzieren: 0 GK / 1 LK
    - Grenzverhalten einer Potenzschar nach der Parität des Exponenten begründen: 0 GK / 1 LK
    - Grenzverhalten einer Schar angeben und parameterunabhängigen Funktionswert nachweisen: 0 GK / 1 LK
    - Hochpunkt einer Schar mit Parameterfaktor bestimmen: 0 GK / 1 LK
    - Hochpunkt im Ursprung über das Vorzeichen begründen und Tiefstelle einer Schar berechnen: 0 GK / 1 LK
    - Lage und Art der Extrempunkte einer Schar bestimmen und Parameter für einen vorgegebenen Abstand der Extrempunkte berechnen: 0 GK / 1 LK
    - Mittelpunkte der Strecken zum Ursprung auf einem gegebenen Graphen allgemein nachweisen: 0 GK / 1 LK
    - Nullstellen einer Schar am Term begründen und Tangentensteigungen dort nachweisen: 0 GK / 1 LK
    - Nullstellen einer Schar am faktorisierten Term angeben: 1 GK / 0 LK
    - Nullstellen einer Schar angeben und Vorzeichen des y-Achsenabschnitts begründen: 0 GK / 1 LK
    - Ortskurve der Extrempunkte einer Schar als Gerade über Sonderfall und Streckungseigenschaft begründen: 0 GK / 1 LK
    - Parameter einer Parabelschar aus dem knickfreien Übergang zu einem Graphen bestimmen: 0 GK / 1 LK
    - Parameter einer Schar aus einem vorgegebenen Punkt auf dem Graphen bestimmen: 1 GK / 0 LK
    - Parameter einer Schar aus einer vorgegebenen Ausdehnung einer Figur bestimmen: 1 GK / 0 LK
    - Parameter einer Schar aus gleichen Winkeln zweier Graphen mit einer Strecke bestimmen und Lage eines Punktes prüfen: 1 GK / 0 LK
    - Parameter für genau zwei gemeinsame Punkte von Graph und Scharparabel über die Diskriminante bestimmen: 1 GK / 0 LK
    - Parameterunabhängigkeit der Fläche zwischen zwei Scharkurven nachweisen: 0 GK / 1 LK
    - Parameterwerte nach der Anzahl der Extrempunkte über die Lösbarkeit der Extremstellengleichung begründen: 0 GK / 1 LK
    - Positivität, y-Achsenabschnitt und Steigung einer Schar begründen und berechnen: 0 GK / 1 LK
    - Punktsymmetrie aller Graphen einer Schar zum Ursprung nachweisen: 0 GK / 1 LK
    - Punktsymmetrie zweier Scharkurven zueinander aus einer Identität nachweisen und deuten: 0 GK / 1 LK
    - Scharparameter aus Anfangswert und Grenzwert über das Vorzeichen des Exponenten bestimmen: 0 GK / 1 LK
    - Scharparameter aus der Flächengleichheit von Quadrat und Flächenstück bestimmen: 0 GK / 1 LK
    - Scharparameter aus der Weite berechnen und Höhe des Hochpunkts angeben: 0 GK / 1 LK
    - Scharparameter aus der y-Koordinate der Tiefpunkte ermitteln: 0 GK / 1 LK
    - Scharparameter aus einem Punkt bestimmen und Wendepunkt nachweisen: 0 GK / 1 LK
    - Scharparameter aus einer Integralbedingung bestimmen: 0 GK / 1 LK
    - Scharparameter aus einer Nullstelle und einem Flächeninhalt bestimmen: 0 GK / 1 LK
    - Scharparameter den Graphen über Spiegelung und Extremstelle zuordnen: 0 GK / 1 LK
    - Scharparameter den Graphen über den y-Achsenabschnitt zuordnen: 0 GK / 1 LK
    - Scharparameter der Ausgangsfunktion angeben und Eignung zweier Scharfunktionen am Graphen beurteilen: 0 GK / 1 LK
    - Scharparameter für Hoch- und Tiefpunkt als Gegenecken eines achsenparallelen Quadrats bestimmen: 0 GK / 1 LK
    - Scharparameter für den Mittelpunkt der Extrempunkte auf der x-Achse bestimmen: 1 GK / 0 LK
    - Scharparameter für ein vorgegebenes Verhältnis zweier Radien einer Profilkurve berechnen: 1 GK / 0 LK
    - Scharparameter für eine vorgegebene Wendestelle berechnen: 0 GK / 1 LK
    - Scharparameter für einen Extrempunkt als Quadratecke bestimmen und Flächeninhalt berechnen: 0 GK / 1 LK
    - Scharparameter für einen Wendepunkt auf einer Geraden berechnen: 0 GK / 1 LK
    - Scharparameter für einen vorgegebenen Flächeninhalt eines Vierecks aus Hochpunkt und Achsenpunkten bestimmen: 0 GK / 1 LK
    - Scharparameter für einen vorgegebenen Flächeninhalt zwischen Graph und x-Achse bestimmen: 1 GK / 0 LK
    - Scharparameter für genau eine Nullstelle über die Lage der Extrempunkte angeben: 1 GK / 0 LK
    - Scharparameter für genau eine waagerechte Tangente aus dem Graphen bestimmen: 0 GK / 1 LK
    - Steigung der Ortsgeraden der Hochpunkte einer Schar aus zwei Hochpunkten berechnen: 0 GK / 1 LK
    - Steigung und Achsenschnittpunkt des linearen Sonderfalls einer Schar angeben: 0 GK / 1 LK
    - Strenge Monotonie einer Schar über die Diskriminante der Ableitung für einen Parameterbereich nachweisen: 0 GK / 1 LK
    - Symmetrieachse einer Scharkurve aus der Verschiebung einer geraden Funktion begründen: 0 GK / 1 LK
    - Tiefpunkt einer Schar mit zwei Parametern nachweisen und Hochpunkt über die Punktsymmetrie begründen: 0 GK / 1 LK
    - Trapez aus Funktions- und Ableitungswerten einer Schar begründen und Flächengleichheit für k und k + 1 nachweisen: 0 GK / 1 LK
    - Verschobene Scharfunktion als gerade Funktion nachweisen: 0 GK / 1 LK
    - Vorzeichen aller Funktionswerte einer Schar am Term begründen: 0 GK / 1 LK
    - Vorzeichen der Funktionswerte einer Schar begründen: 0 GK / 1 LK
    - Vorzeichen der Stammfunktionen einer Schar durch Fallunterscheidung untersuchen: 0 GK / 1 LK
    - Wendepunkt einer Schar im Ursprung mit der x-Achse als Wendetangente nachweisen: 1 GK / 0 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur LK-Block; Typenzeilen: 17 GK / 125 LK)

### geraden
- Geltung je Zielprüfung:
  - Thema „Geraden“ (`themen.csv`):
    - be-gk: ja – `| Geraden | ja |` [abi-be-gk-geltung.md Zeile 37]
    - be-lk: ja – `| Geraden | ja |` [abi-be-lk-geltung.md Zeile 37]
    - bb-gk: ja – `| Geraden | ja |` [abi-bb-gk-geltung.md Zeile 37]
    - bb-ea: ja – `| Geraden | ja |` [abi-bb-ea-geltung.md Zeile 37]
- Lerneinheiten:
  - 1. Geradengleichung aufstellen und lesen
    - Eintrag, Zeile 11: „(Q3, GK-Kern „Richtungsvektor“, „analytische Beschreibung von Geraden …: Parameterform“; OHiMi 2.3 „Geraden: Parameterform“)“
    - GOST Berlin [Zeilen 1142–1143]: „Geraden und Ebenen (durch Parameter-, Koordinaten- und Normalenform) analytisch beschreiben und Lagebeziehungen untersuchen (vgl. L2).“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1268–1269]: „Geraden und Ebenen analytisch beschreiben und Lagebeziehungen von“
      Q3, Grund- und Leistungskursfach
  - 2. Punktprobe und Punkte auf der Geraden
    - Eintrag, Zeile 12: „(Q3, GK-Kern „Lagebeziehungen zwischen: Punkt und Gerade“; OHiMi 2.3 „Lagebeziehungen …“, „Betrag eines Vektors“)“
    - GOST Berlin [Zeilen 1142–1143]: „Geraden und Ebenen (durch Parameter-, Koordinaten- und Normalenform) analytisch beschreiben und Lagebeziehungen untersuchen (vgl. L2).“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1282]: „Punkt und Gerade“
      Q3, Grund- und Leistungskursfach
  - 3. Lage als Anhang
    - Eintrag, Zeile 13: „(Q3, GK-Kern „Lagebeziehungen zwischen: … Geraden“; OHiMi 2.3)“
    - GOST Berlin [Zeilen 1142–1143]: „Geraden und Ebenen (durch Parameter-, Koordinaten- und Normalenform) analytisch beschreiben und Lagebeziehungen untersuchen (vgl. L2).“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1283]: „Geraden“
      Q3, Grund- und Leistungskursfach
  - 4. Sachgeraden
    - Eintrag, Zeile 14: „(Q3, GK-Kern L2/L3; die Prüfungsform trägt Teil B mit Maßstab „1 LE = …“)“
    - GOST Berlin [Zeilen 1142–1143]: „Geraden und Ebenen (durch Parameter-, Koordinaten- und Normalenform) analytisch beschreiben und Lagebeziehungen untersuchen (vgl. L2).“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1268–1269]: „Geraden und Ebenen analytisch beschreiben und Lagebeziehungen von“
      Q3, Grund- und Leistungskursfach
    - Ermessen: Sachgeraden (Gerade als Weg, Parameter als Zeit) nennt kein Plan eigens.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 12 Zeilen GK / 3 Zeilen LK, 12 Haupttypen
    - Punktprobe an einer Geraden durchführen: 3 GK / 1 LK
    - Echt parallele und senkrecht schneidende Gerade zu einer gegebenen Geraden angeben: 1 GK / 0 LK
    - Existenz eines Geradenschnittpunkts über die gemeinsame Ebene begründen: 1 GK / 0 LK
    - Gerade in einer Ebene durch einen Punkt parallel zu einer Koordinatenebene angeben: 1 GK / 0 LK
    - Geradengleichung durch zwei Punkte aufstellen: 1 GK / 0 LK
    - Geradengleichung durch zwei Punkte aufstellen und windschiefe Lage begründen: 1 GK / 0 LK
    - Kollinearität dreier Punkte über die Verbindungsvektoren nachweisen: 1 GK / 0 LK
    - Lösungsweg zur Bestimmung eines Punktes auf einer Geraden beschreiben: 1 GK / 0 LK
    - Nichtidentität zweier Geraden über die Richtungsvektoren begründen: 0 GK / 1 LK
    - Parallelität zweier Geraden über die Richtungsvektoren prüfen: 1 GK / 0 LK
    - Punkt auf einer Geraden mit vorgegebenem Abstand zum Aufpunkt bestimmen: 0 GK / 1 LK
    - Schnitt einer senkrecht schneidenden Geraden mit einer parallelen Geraden beurteilen: 1 GK / 0 LK
  - iqb: 15 Zeilen GK / 6 Zeilen LK, 14 Haupttypen
    - Punktprobe an einer Geraden durchführen: 4 GK / 3 LK
    - Geradengleichung durch zwei Punkte aufstellen und windschiefe Lage begründen: 1 GK / 1 LK
    - Höhe eines Punktes auf einer Strecke aus der Entfernung vom Anfang berechnen: 1 GK / 0 LK
    - Höhenunterschied zweier übereinanderliegender Punkte auf Seilgeraden bestimmen: 1 GK / 0 LK
    - Lösungsansatz für eine bewegte Gerade durch einen festen Punkt erläutern und im Sachzusammenhang deuten: 1 GK / 0 LK
    - Lösungsweg zur Bestimmung eines Punktes auf einer Geraden beschreiben: 1 GK / 0 LK
    - Neigung einer Strecke in Prozent aus Höhendifferenz und Horizontalabstand berechnen: 1 GK / 0 LK
    - Nichtidentität zweier Geraden über die Richtungsvektoren begründen: 0 GK / 1 LK
    - Nichtidentität zweier paralleler Geraden über den Verbindungsvektor begründen: 1 GK / 0 LK
    - Parallele Gerade durch einen Teilpunkt einer Strecke bestimmen: 1 GK / 0 LK
    - Parallelität einer Geraden zu einer Koordinatenachse über die Koordinaten begründen: 0 GK / 1 LK
    - Parametergleichung einer Strecke im Sachzusammenhang deuten: 1 GK / 0 LK
    - Punkt auf einer Geraden mit vorgegebenem Abstand zum Aufpunkt bestimmen: 1 GK / 0 LK
    - Punkt auf einer Geraden mit vorgegebener Koordinate angeben: 1 GK / 0 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 27 GK / 9 LK)

### gleichungen-loesen
- Geltung je Zielprüfung:
  - Thema „Gleichungen lösen“ (`themen.csv`):
    - be-gk: ja – `| Gleichungen lösen | ja |` [abi-be-gk-geltung.md Zeile 15]
    - be-lk: ja – `| Gleichungen lösen | ja |` [abi-be-lk-geltung.md Zeile 15]
    - bb-gk: ja – `| Gleichungen lösen | ja |` [abi-bb-gk-geltung.md Zeile 15]
    - bb-ea: ja – `| Gleichungen lösen | ja |` [abi-bb-ea-geltung.md Zeile 15]
- Lerneinheiten:
  - 1. Ganzrationale Gleichungen
    - Eintrag, Zeile 11: „(Q1, GK-Kern „lineare, allgemeine quadratische und biquadratische Gleichungen sowie Gleichungen höheren Grades (Polynomdivision, …“
    - GOST Berlin [Zeilen 1052–1053]: „geeignete Verfahren zur Lösung von Gleichungen und Gleichungssystemen auswählen,“
      Zahlen und Operationen [L1], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 885–886]: „geeignete Verfahren zur Lösung von Gleichungen und Gleichungssystemen“
      Q1, Grund- und Leistungskursfach
  - 2. Gleichungen mit e-Funktion und Logarithmus
    - Eintrag, Zeile 12: „(Q1, GK-Kern „natürliche Exponentialgleichungen (natürlicher Logarithmus und Logarithmengesetze)“
    - GOST Berlin [Zeilen 1052–1053]: „geeignete Verfahren zur Lösung von Gleichungen und Gleichungssystemen auswählen,“
      Zahlen und Operationen [L1], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 890–891]: „natürliche Exponentialgleichungen (lösen unter Anwendung des natürlichen Loga-“
      Q1, Grund- und Leistungskursfach
  - 3. Gleichungen aufstellen und grafisch oder numerisch lösen
    - Eintrag, Zeile 13: „(Q1, GK-Kern „Änderungsrate im Sachzusammenhang“, „Nullstellen“; OHiMi 2.1 „einfache Bruchgleichungen“; LK „goniometrische Gleichungen“; BE …“
    - GOST Berlin [Zeilen 1052–1053]: „geeignete Verfahren zur Lösung von Gleichungen und Gleichungssystemen auswählen,“
      Zahlen und Operationen [L1], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 885–886]: „geeignete Verfahren zur Lösung von Gleichungen und Gleichungssystemen“
      Q1, Grund- und Leistungskursfach
  - 4. Ungleichungen
    - Eintrag, Zeile 14: „(Q1, GK-Kern „Funktionseigenschaften“ als Herkunft; OHiMi 2.1 „Gleichungen durch Faktorisieren lösen“, „einfache Betragsgleichungen“ – …“
    - GOST Berlin: keine Stelle
    - GOST Brandenburg: keine Stelle
    - Ermessen: Ungleichungen nennt keiner der beiden Pläne in der Qualifikationsphase – weder Berlin noch Brandenburg. Keine Stelle.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 10 Zeilen GK / 5 Zeilen LK, 12 Haupttypen
    - Lösungsmenge einer Ungleichung zwischen zwei Funktionstermen über die faktorisierte Differenz bestimmen: 1 GK / 1 LK
    - Schnittstelle von Graph und Ableitungsgraph nachweisen: 1 GK / 1 LK
    - Schnittstellen zweier Graphen durch Lösen einer quadratischen Gleichung nachweisen: 2 GK / 0 LK
    - Achsenparallele Quadrate mit Eckpunkt auf dem Graphen skizzieren, Gleichungen für die Seitenlängen angeben und Umfangsverhältnis beschreiben: 0 GK / 1 LK
    - Funktionalgleichung mit Zeitverschiebung grafisch lösen und im Sachzusammenhang deuten: 1 GK / 0 LK
    - Gleichung aus Differenzenquotient und Ableitung lösen: 1 GK / 0 LK
    - Lösungsweg für den Gültigkeitsbereich einer Näherung über eine Betragsungleichung beschreiben: 1 GK / 0 LK
    - Nullstelle einer Exponentialfunktion durch Logarithmieren bestimmen: 0 GK / 1 LK
    - Parameter einer Exponentialfunktion aus einer Ungleichung für einen Funktionswert im Sachzusammenhang ermitteln: 1 GK / 0 LK
    - Schnittpunkt zweier Graphen über eine biquadratische Gleichung berechnen: 1 GK / 0 LK
    - Schnittstellen zweier Graphen über den gemeinsamen Exponentialfaktor nachweisen: 0 GK / 1 LK
    - Termgleichheit zweier Darstellungen einer ganzrationalen Funktion durch Ausmultiplizieren nachweisen: 1 GK / 0 LK
  - iqb: 8 Zeilen GK / 11 Zeilen LK, 19 Haupttypen
    - Alle Zeitpunkte für einen Wert einer Sinusfunktion in einem Intervall berechnen: 0 GK / 1 LK
    - Anfangswert angeben und Stelle für einen vorgegebenen Wert einer Exponentialfunktion berechnen: 0 GK / 1 LK
    - Anfangswert angeben und Zeitpunkt für einen Bestand bei logistischem Wachstum berechnen: 0 GK / 1 LK
    - Exponentialgleichung für einen Funktionswert durch Logarithmieren lösen und als Abstand im Sachzusammenhang angeben: 0 GK / 1 LK
    - Fehlenden Schnittpunkt zweier Graphen über eine unlösbare Gleichung begründen: 0 GK / 1 LK
    - Funktionalgleichung mit Zeitverschiebung grafisch lösen und im Sachzusammenhang deuten: 1 GK / 0 LK
    - Gemeinsame Punkte zweier Graphen als einzige durch Ausklammern nachweisen: 1 GK / 0 LK
    - Gleichung aus Differenzenquotient und Ableitung lösen: 1 GK / 0 LK
    - Gleichung f(t) = f(t − c) für gleiche Werte im Abstand c mit dem Rechner lösen und im Graphen darstellen: 0 GK / 1 LK
    - Gleichung für zwei Graphenpunkte mit festem horizontalem Abstand und Höhenunterschied aufstellen: 0 GK / 1 LK
    - Lösungen einer Differenzgleichung als Schnittstellen zweier Graphen grafisch beschreiben und angeben: 1 GK / 0 LK
    - Nullstelle einer Exponentialfunktion durch Logarithmieren bestimmen: 0 GK / 1 LK
    - Nullstelle einer Logarithmusfunktion berechnen: 0 GK / 1 LK
    - Schnittpunkte einer Geraden mit einer Hyperbel über eine quadratische Gleichung berechnen: 1 GK / 0 LK
    - Schnittstellen zweier Graphen durch Lösen einer quadratischen Gleichung nachweisen: 1 GK / 0 LK
    - Schnittstellen zweier Graphen über den gemeinsamen Exponentialfaktor nachweisen: 0 GK / 1 LK
    - Steigung im Schnittpunkt von Graph und Ableitungsgraph bestimmen: 1 GK / 0 LK
    - Stellen mit vorgegebenem Funktionswert durch Ausklammern berechnen: 1 GK / 0 LK
    - Zeitpunkt für einen Anteil des Maximalwerts einer Sinusfunktion berechnen: 0 GK / 1 LK
  - fhr: 9 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 18 GK / 16 LK)

### grenzwerte-und-verhalten-im-unendlichen
- Geltung je Zielprüfung:
  - Thema „Grenzwerte und Verhalten im Unendlichen“ (`themen.csv`):
    - be-gk: ja – `| Grenzwerte und Verhalten im Unendlichen | ja |` [abi-be-gk-geltung.md Zeile 19]
    - be-lk: ja – `| Grenzwerte und Verhalten im Unendlichen | ja |` [abi-be-lk-geltung.md Zeile 19]
    - bb-gk: ja – `| Grenzwerte und Verhalten im Unendlichen | ja |` [abi-bb-gk-geltung.md Zeile 19]
    - bb-ea: ja – `| Grenzwerte und Verhalten im Unendlichen | ja |` [abi-bb-ea-geltung.md Zeile 19]
- Lerneinheiten:
  - 1. Ganzrationale Funktionen
    - Eintrag, Zeile 11: „(Q1, GK-Kern „Verhalten im Unendlichen“, „Axialsymmetrie bzgl. der Ordinatenachse“; FOS „Verhalten im Unendlichen“, „Symmetrie bezüglich …“
    - GOST Berlin [Zeilen 1050–1051]: „einen propädeutischen Grenzwertbegriffs insbesondere bei der Bestimmung von Ableitung und Integral nutzen,“
      Zahlen und Operationen [L1], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 878–879]: „Grenzwerte auf der Grundlage eines propädeutischen Grenzwertbegriffs“
      Q1, Grund- und Leistungskursfach
  - 2. Produkte aus Polynom und e-Funktion
    - Eintrag, Zeile 12: „(Q1, GK-Kern „Grenzwertverhalten von Funktionsgraphen (x → ±∞)“
    - GOST Berlin [Zeilen 1050–1051]: „einen propädeutischen Grenzwertbegriffs insbesondere bei der Bestimmung von Ableitung und Integral nutzen,“
      Zahlen und Operationen [L1], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 878–879]: „Grenzwerte auf der Grundlage eines propädeutischen Grenzwertbegriffs“
      Q1, Grund- und Leistungskursfach
  - 3. Waagerechte Asymptoten
    - Eintrag, Zeile 13: „(Q1, GK-Kern „Grenzwertverhalten“, „Monotonie“, „Nullstellen“; OHiMi 2.2 „Zusammenhang zwischen Funktionsgraph und Funktionsgleichung nach … …“
    - GOST Berlin [Zeilen 1205–1206]: „die Ableitung mithilfe der Approximation durch lineare Funktionen deuten und Asymptoten ermitteln,“
      Funktionaler Zusammenhang [L4], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeile 938]: „Verhalten im Unendlichen“
      Q1, Grund- und Leistungskursfach
    - Ermessen: Länderunterschied: Asymptoten stehen in Berlin im LK-Zusatz, in Brandenburg als Funktionseigenschaft „Verhalten im Unendlichen“ im Grund- und Leistungskursfach.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 9 Zeilen GK / 3 Zeilen LK, 4 Haupttypen
    - Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben: 4 GK / 1 LK
    - Grenzverhalten einer ganzrationalen Funktion angeben: 2 GK / 1 LK
    - Nullstelle und Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben: 2 GK / 1 LK
    - Grenzwert für x gegen unendlich angeben und Verlauf des Graphen beschreiben: 1 GK / 0 LK
  - iqb: 3 Zeilen GK / 3 Zeilen LK, 4 Haupttypen
    - Grenzwert für x gegen unendlich angeben und Verlauf des Graphen beschreiben: 2 GK / 0 LK
    - Nullstelle und Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben: 1 GK / 1 LK
    - Monotonie, Nullstelle und Grenzwert einer e-Funktion am Term begründen: 0 GK / 1 LK
    - Nullstellenfreiheit und Grenzwerte eines Bruchs mit e-Funktion am Term begründen: 0 GK / 1 LK
  - fhr: 4 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: GK-Block und LK-Block; Typenzeilen: 12 GK / 6 LK)

### hypergeometrische-verteilung
- Geltung je Zielprüfung:
  - Thema „Hypergeometrische Verteilung“ (`themen.csv`):
    - be-gk: nein – `| Hypergeometrische Verteilung | nein |` [abi-be-gk-geltung.md Zeile 59]
    - be-lk: nein – `| Hypergeometrische Verteilung | nein |` [abi-be-lk-geltung.md Zeile 59]
    - bb-gk: ja – `| Hypergeometrische Verteilung | ja |` [abi-bb-gk-geltung.md Zeile 59]
    - bb-ea: ja – `| Hypergeometrische Verteilung | ja |` [abi-bb-ea-geltung.md Zeile 59]
- Lerneinheiten:
  - 1. Genau k Treffer ohne Zurücklegen: die Situation erkennen (feste kleine Gesamtheit, Ziehen ohne Zurücklegen
    - Eintrag, Zeile 11: „(Q2, GK-Kern „Ziehen ohne Zurücklegen“; OHiMi 2.4 „Ansätze“; IQB-VER 4 vorausgesetzt)“
    - GOST Berlin [Zeilen 1245–1246]: „Anwendungssituationen mithilfe des Urnenmodells (mit und ohne Zurücklegen) untersuchen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1124–1125]: „Ziehen ohne Zurücklegen (hypergeometrische Verteilung)“
      Q2, Grund- und Leistungskursfach
  - 2. Kumulieren gegen eine Schranke: hypergeometrische Einzelwahrscheinlichkeiten aufsummieren und die größte (oder kleinste) Trefferzahl gegen eine Schranke bestimmen
    - Eintrag, Zeile 12: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1245–1246]: „Anwendungssituationen mithilfe des Urnenmodells (mit und ohne Zurücklegen) untersuchen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1121–1122]: „Anwendungssituationen mithilfe von Urnenmodellen untersuchen,“
      Q2, Grund- und Leistungskursfach
    - Ermessen: Das Kumulieren hypergeometrischer Wahrscheinlichkeiten nennt kein Plan; zugeordnet ist die Urnenmodellzeile.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 1 Zeilen GK / 4 Zeilen LK, 3 Haupttypen
    - Wahrscheinlichkeit beim Ziehen ohne Zurücklegen über das Gegenereignis berechnen: 1 GK / 2 LK
    - Größte Trefferzahl, bis zu der die kumulierte hypergeometrische Wahrscheinlichkeit unter einer Schranke bleibt, ermitteln: 0 GK / 1 LK
    - Hypergeometrische Wahrscheinlichkeit für genau k Treffer über Binomialkoeffizienten nachweisen: 0 GK / 1 LK
  - iqb: 1 Zeilen GK / 1 Zeilen LK, 1 Haupttypen
    - Hypergeometrische Wahrscheinlichkeit für genau k Treffer über Binomialkoeffizienten nachweisen: 1 GK / 1 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 2 GK / 5 LK)

### hypothesentests
- Geltung je Zielprüfung:
  - Thema „Hypothesentests“ (`themen.csv`):
    - be-gk: nein – `| Hypothesentests | nein |` [abi-be-gk-geltung.md Zeile 61]
    - be-lk: ja – `| Hypothesentests | ja |` [abi-be-lk-geltung.md Zeile 61]
    - bb-gk: nein – `| Hypothesentests | nein |` [abi-bb-gk-geltung.md Zeile 61]
    - bb-ea: ja – `| Hypothesentests | ja |` [abi-bb-ea-geltung.md Zeile 61]
- Lerneinheiten:
  - 1. Entscheidungsregel bestimmen: die Nullhypothese liefert p und die Binomialverteilung der Testgröße, die Alternative die Seite des Ablehnungsbereichs (rechtsseitig bei „mehr als“, linksseitig bei „weniger als“); die Grenze über kumulierte Wahrscheinlichkeiten so wählen, dass das Signifikanzniveau eingehalten wird
    - Eintrag, Zeile 11: „(Q4 LK; Prüfform jedes Testjahrs)“
    - GOST Berlin [Zeilen 1255–1256]: „Hypothesentests bei Binomialverteilungen interpretieren und die Unsicherheit (Fehler 1. und 2. Art) der Ergebnisse begründen,“
      Daten und Zufall [L5], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1340–1341]: „Hypothesentests bei Binomial-verteilungen interpretieren und die Unsi-“
      Q4, Zusätzlich im Leistungskursfach
  - 2. Die Nullhypothese wählen: aus der Sicht des Entscheiders
    - Eintrag, Zeile 12: „(Q4 LK; BE Kap. 4 „kein sicheres Urteil“)“
    - GOST Berlin [Zeilen 1255–1256]: „Hypothesentests bei Binomialverteilungen interpretieren und die Unsicherheit (Fehler 1. und 2. Art) der Ergebnisse begründen,“
      Daten und Zufall [L5], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1345–1346]: „Signifikanzniveau, Ablehnungsbereich und Entscheidungsregel“
      Q4, Zusätzlich im Leistungskursfach
  - 3. Fehlerarten und Güte: den Fehler zweiter Art für selbst gewählte Anteile berechnen (p dort wählen, wo die Nullhypothese falsch ist), einordnen und im Sachzusammenhang beschreiben; Mindestanteile für eine Fehlerschranke; die Gütekurve lesen (Ablehnwahrscheinlichkeit in Abhängigkeit von p
    - Eintrag, Zeile 13: „(Q4 LK; Prüfungshöhe)“
    - GOST Berlin [Zeilen 1255–1256]: „Hypothesentests bei Binomialverteilungen interpretieren und die Unsicherheit (Fehler 1. und 2. Art) der Ergebnisse begründen,“
      Daten und Zufall [L5], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeile 1347]: „Fehler 1. und 2. Art“
      Q4, Zusätzlich im Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 0 Zeilen GK / 10 Zeilen LK, 6 Haupttypen
    - Entscheidungsregel eines einseitigen Signifikanztests bestimmen: 0 GK / 3 LK
    - Fehler zweiter Art für selbst gewählte Anteile berechnen und einordnen: 0 GK / 2 LK
    - Wahl der Nullhypothese aus der Sicht des Entscheiders begründen: 0 GK / 2 LK
    - Lücke in einem Lösungsweg zur Ablehnungsgrenze begründen und ergänzen: 0 GK / 1 LK
    - Mindestanteil für eine Schranke des Fehlers zweiter Art ermitteln und den Fehler im Sachzusammenhang beschreiben: 0 GK / 1 LK
    - Untere Schranke für den Stichprobenumfang eines Tests über den Fehler erster Art am Graphen begründen: 0 GK / 1 LK
  - iqb: 0 Zeilen GK / 12 Zeilen LK, 8 Haupttypen
    - Entscheidungsregel eines einseitigen Signifikanztests bestimmen: 0 GK / 3 LK
    - Wahl der Nullhypothese aus der Sicht des Entscheiders begründen: 0 GK / 3 LK
    - Fehler zweiter Art aus dem Graphen der Ablehnwahrscheinlichkeit ermitteln: 0 GK / 1 LK
    - Fehler zweiter Art für selbst gewählte Anteile berechnen und einordnen: 0 GK / 1 LK
    - Lücke in einem Lösungsweg zur Ablehnungsgrenze begründen und ergänzen: 0 GK / 1 LK
    - Mindestanteil für eine Schranke des Fehlers zweiter Art ermitteln und den Fehler im Sachzusammenhang beschreiben: 0 GK / 1 LK
    - Nutzen eines größeren Stichprobenumfangs über den Fehler zweiter Art an den Gütekurven begründen: 0 GK / 1 LK
    - Stichprobenumfang eines Tests aus Ablehnungsgrenze und Fehler erster Art am Graphen ermitteln: 0 GK / 1 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: nur LK – keine Zeile und keine Einheit im Grundkurs (Einheiten: nur LK-Block; Typenzeilen: 0 GK / 22 LK)

### integrationsregeln
- Geltung je Zielprüfung:
  - Thema „Integrationsregeln“ (`themen.csv`):
    - be-gk: ja – `| Integrationsregeln | ja |` [abi-be-gk-geltung.md Zeile 29]
    - be-lk: ja – `| Integrationsregeln | ja |` [abi-be-lk-geltung.md Zeile 29]
    - bb-gk: ja – `| Integrationsregeln | ja |` [abi-bb-gk-geltung.md Zeile 29]
    - bb-ea: ja – `| Integrationsregeln | ja |` [abi-bb-ea-geltung.md Zeile 29]
- Lerneinheiten:
  - 1. Der Regelsatz
    - Eintrag, Zeile 11: „(Q2 GK-Kern; OHiMi „Integrationsregeln“)“
    - GOST Berlin [Zeilen 1193–1194]: „Integrale von Funktionen (Potenzfunktionen f mit f(x) = xn, n ∈ ZZ , n ≠ −1, ganzrationalen und Exponentialfunktionen) mittels Stammfunktionen bestimmen,“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1090–1091]: „Integrationsregeln: Potenzregel“
      Q2, Grund- und Leistungskursfach
  - 2. Vorgegebene Regeln anwenden
    - Eintrag, Zeile 12: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1193–1194]: „Integrale von Funktionen (Potenzfunktionen f mit f(x) = xn, n ∈ ZZ , n ≠ −1, ganzrationalen und Exponentialfunktionen) mittels Stammfunktionen bestimmen,“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1085–1086]: „Integrale von Funktionen mittels Stammfunktionen bilden,“
      Q2, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 0 Zeilen GK / 1 Zeilen LK, 1 Haupttypen
    - Integral über eine vorgegebene Regel für g' · e^g berechnen: 0 GK / 1 LK
  - iqb: 0 Zeilen GK / 1 Zeilen LK, 1 Haupttypen
    - Integral über eine vorgegebene Regel für g' · e^g berechnen: 0 GK / 1 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 0 GK / 2 LK)
- Befund: Die Prüfungsform kennt nur zwei Zeilen, beide auf erhöhtem Niveau; die Stellen im Plan stehen in beiden Ländern im Grund- und Leistungskursfach. Die Spanne „ja“ kommt hier allein von den Einheiten, nicht von den Zeilen.

### kenngroessen-von-verteilungen
- Geltung je Zielprüfung:
  - Thema „Kenngrößen von Verteilungen“ (`themen.csv`):
    - be-gk: ja – `| Kenngrößen von Verteilungen | ja |` [abi-be-gk-geltung.md Zeile 58]
    - be-lk: ja – `| Kenngrößen von Verteilungen | ja |` [abi-be-lk-geltung.md Zeile 58]
    - bb-gk: ja – `| Kenngrößen von Verteilungen | ja |` [abi-bb-gk-geltung.md Zeile 58]
    - bb-ea: ja – `| Kenngrößen von Verteilungen | ja |` [abi-bb-ea-geltung.md Zeile 58]
- Lerneinheiten:
  - 1. Erwartungswert berechnen und deuten: die Verteilung beschaffen (Tabelle, Sachtext, Baumpfade, Kosten je Ausgang; fehlende Wahrscheinlichkeit über die Summe 1), die gewichtete Summe bilden (bei Anzahlen n · p), das Ergebnis deuten
    - Eintrag, Zeile 11: „(Q2 BB, GK-Kern; OHiMi 2.4 „Erwartungswert von Zufallsgrößen“; FOS Pflichtthema 4)“
    - GOST Berlin [Zeilen 1094–1095]: „Erwartungswert und Standardabweichung der Binomialverteilung bestimmen und deuten,“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Berlin [Zeilen 1107–1108]: „Erwartungswert und Standardabweichung diskreter Zufallsgrößen bestimmen und deuten,“
      Messen [L2], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1064–1065]: „Erwartungswert und Standardabweichung diskreter Zufallsgrößen bestim-“
      Q2, Grund- und Leistungskursfach
    - Ermessen: Länderunterschied: Erwartungswert und Standardabweichung stehen in Berlin für die Binomialverteilung im Grund- und Leistungskursfach, für diskrete Zufallsgrößen im LK-Zusatz; Brandenburg führt die diskreten Zufallsgrößen im Grund- und Leistungskursfach.
  - 2. Rückwärts
    - Eintrag, Zeile 12: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1094–1095]: „Erwartungswert und Standardabweichung der Binomialverteilung bestimmen und deuten,“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1064–1065]: „Erwartungswert und Standardabweichung diskreter Zufallsgrößen bestim-“
      Q2, Grund- und Leistungskursfach
  - 3. Varianz und Standardabweichung: die allgemeinen Formeln (gewichtete quadrierte Abweichung, Wurzel), die Binomialformeln μ = n · p und σ = √(n · p · (1 − p)) vorwärts und rückwärts (Parameter aus Kenngrößen, Symmetrie liefert p), Argumente über die Formel (Parabel in p, Symmetrie von p und Gegenwahrscheinlichkeit, Wachstum mit der Wurzel aus n). (BB Q2 GK-Kern, BE Q4 GK binomial bzw. LK allgemein; [IQB-VER 4] vorausgesetzt) ← Eingabe „standardabweichung“, „varianz“, „sigma“, „streuung“
    - Eintrag, Zeile 13: „(BB Q2 GK-Kern, BE Q4 GK binomial bzw. LK allgemein; [IQB-VER 4] vorausgesetzt)“
    - GOST Berlin [Zeilen 1094–1095]: „Erwartungswert und Standardabweichung der Binomialverteilung bestimmen und deuten,“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Berlin [Zeilen 1107–1108]: „Erwartungswert und Standardabweichung diskreter Zufallsgrößen bestimmen und deuten,“
      Messen [L2], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1116–1117]: „Kenngrößen von Wahrscheinlichkeits-verteilungen“
      Q2, Grund- und Leistungskursfach
  - 4. Kenngrößen am Säulendiagramm: den ganzzahligen Erwartungswert an der höchsten Säule ablesen und daraus p, n oder Verhältnisse bestimmen, die Parität von n aus zwei gleich hohen Säulen begründen, ein Sigma-Intervall auf ganze Werte übertragen und die Wahrscheinlichkeit als Summe der Säulenhöhen ablesen. (GOST-Inhalt „Eigenschaften auf der Grundlage graphischer Darstellungen“; OHiMi 2.4 „Histogramme“; alle Zeilen Teil A, gehäuft seit 2024) ← Eingabe „höchste säule“, „diagramm erwartungswert“, „sigma-intervall“, „säulendiagramm binomial“
    - Eintrag, Zeile 14: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1094–1095]: „Erwartungswert und Standardabweichung der Binomialverteilung bestimmen und deuten,“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1065–1066]: „Eigenschaften auf der Grundlage graphischer Darstellungen“
      Q2, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 13 Zeilen GK / 10 Zeilen LK, 13 Haupttypen
    - Unbekannte Größe aus einer Erwartungswertbedingung bestimmen: 2 GK / 5 LK
    - Erwartungswert einer Zufallsgröße im Sachzusammenhang berechnen: 3 GK / 2 LK
    - Erwartungswert der Auszahlung mit dem Einsatz vergleichen: 1 GK / 0 LK
    - Erwartungswertgleichung für einen Glücksradparameter aus den Spielregeln herleiten: 1 GK / 0 LK
    - Parameter einer Binomialverteilung aus Erwartungswert und Standardabweichung bestimmen: 1 GK / 0 LK
    - Parität von n aus zwei gleich hohen Säulen der Verteilung begründen: 1 GK / 0 LK
    - Prozentuale Abweichung einer Anzahl vom Erwartungswert berechnen: 1 GK / 0 LK
    - Restwahrscheinlichkeit und Erwartungswert eines Teilgewinns aus dem Gesamterwartungswert bestimmen: 0 GK / 1 LK
    - Summand eines Erwartungswertterms im Sachzusammenhang deuten: 1 GK / 0 LK
    - Trefferwahrscheinlichkeit aus dem ganzzahligen Erwartungswert im Diagramm ermitteln: 1 GK / 0 LK
    - Wahrscheinlichkeit eines Sigma-Intervalls aus dem Säulendiagramm ermitteln: 0 GK / 1 LK
    - Würfelbeschriftung aus Erwartungswert und Trefferbedingung untersuchen: 0 GK / 1 LK
    - Zwei Wahrscheinlichkeiten einer Verteilung aus dem Erwartungswert und der Summe 1 bestimmen: 1 GK / 0 LK
  - iqb: 25 Zeilen GK / 23 Zeilen LK, 32 Haupttypen
    - Unbekannte Größe aus einer Erwartungswertbedingung bestimmen: 5 GK / 8 LK
    - Trefferwahrscheinlichkeit aus dem ganzzahligen Erwartungswert im Diagramm ermitteln: 1 GK / 2 LK
    - Erwartungswert der Auszahlung mit dem Einsatz vergleichen: 2 GK / 0 LK
    - Erwartungswertgleichung für einen Glücksradparameter aus den Spielregeln herleiten: 1 GK / 1 LK
    - Achsen des Graphen der Standardabweichung in Abhängigkeit von p skalieren und erläutern: 1 GK / 0 LK
    - Aussage über gleiche Erwartungswerte aufeinanderfolgender Parameterwerte über eine Gleichung beurteilen: 0 GK / 1 LK
    - Erwartungswert aus einer Verteilung mit fehlender Wahrscheinlichkeit berechnen: 0 GK / 1 LK
    - Erwartungswert der Augensumme aus dem Erwartungswert der Trefferzahl berechnen: 1 GK / 0 LK
    - Erwartungswert der Kosten pro Stück aus einer Wahrscheinlichkeitstabelle berechnen: 1 GK / 0 LK
    - Erwartungswert einer weiteren Runde mit dem sicheren Betrag vergleichen und eine Empfehlung begründen: 0 GK / 1 LK
    - Erwartungswert eines Spielgewinns über die Pfade eines Baumdiagramms berechnen: 1 GK / 0 LK
    - Gleiche Standardabweichung zweier komplementärer Zufallsgrößen begründen: 0 GK / 1 LK
    - Kugelbeschriftung aus dem Erwartungswert der Summe beim Ziehen ohne Zurücklegen berechnen: 1 GK / 0 LK
    - Kugelzahl für den größten Erwartungswert der Auszahlung ermitteln: 0 GK / 1 LK
    - Mindestanzahl aus einer Erwartungswertbedingung n · p > c ermitteln: 0 GK / 1 LK
    - Monotonie der Varianz einer Binomialverteilung in p über die Parabel begründen: 1 GK / 0 LK
    - Parameter einer Binomialverteilung aus Erwartungswert und Standardabweichung bestimmen: 1 GK / 0 LK
    - Parameter n aus Erwartungswert und Symmetrie einer Binomialverteilung ermitteln: 0 GK / 1 LK
    - Parität von n aus zwei gleich hohen Säulen der Verteilung begründen: 1 GK / 0 LK
    - Prozentuale Abweichung einer Anzahl vom Erwartungswert berechnen: 1 GK / 0 LK
    - Restwahrscheinlichkeit und Erwartungswert eines Teilgewinns aus dem Gesamterwartungswert bestimmen: 0 GK / 1 LK
    - Standardabweichung einer Binomialverteilung aus n und Erwartungswert berechnen: 0 GK / 1 LK
    - Standardabweichung über einen Summanden der Varianz abschätzen: 1 GK / 0 LK
    - Stichprobenumfang für eine verdoppelte Standardabweichung der Binomialverteilung ermitteln: 1 GK / 0 LK
    - Summand eines Erwartungswertterms im Sachzusammenhang deuten: 1 GK / 0 LK
    - Untere Schranke für eine Kugelbeschriftung aus dem Erwartungswert der Summe ohne Rechnung begründen: 1 GK / 0 LK
    - Verhältnis der Varianzen zweier Binomialverteilungen aus dem Erwartungswert im Diagramm bestimmen: 1 GK / 0 LK
    - Verhältnis zweier Auszahlungen aus dem Ausgleich der Erwartungswerte berechnen: 1 GK / 0 LK
    - Wahrscheinlichkeit eines Sigma-Intervalls aus dem Säulendiagramm ermitteln: 0 GK / 1 LK
    - Wertebereich des Erwartungswerts aus Ungleichungen für die Wahrscheinlichkeiten bestimmen: 0 GK / 1 LK
    - Würfelbeschriftung aus Erwartungswert und Trefferbedingung untersuchen: 0 GK / 1 LK
    - Zwei Wahrscheinlichkeiten einer Verteilung aus dem Erwartungswert und der Summe 1 bestimmen: 1 GK / 0 LK
  - fhr: 2 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: GK-Block und LK-Block; Typenzeilen: 38 GK / 33 LK)

### kombinatorik
- Geltung je Zielprüfung:
  - Thema „Kombinatorik“ (`themen.csv`):
    - be-gk: ja – `| Kombinatorik | ja |` [abi-be-gk-geltung.md Zeile 50]
    - be-lk: ja – `| Kombinatorik | ja |` [abi-be-lk-geltung.md Zeile 50]
    - bb-gk: ja – `| Kombinatorik | ja |` [abi-bb-gk-geltung.md Zeile 50]
    - bb-ea: ja – `| Kombinatorik | ja |` [abi-bb-ea-geltung.md Zeile 50]
- Lerneinheiten:
  - 1. Zählprinzip und Anordnungen
    - Eintrag, Zeile 11: „(Q2, GK-Kern „kombinatorische Abzählverfahren“; OHiMi 2.4 n! und n^k; FOS „Permutationen, Variationen“)“
    - GOST Berlin [Zeilen 1245–1246]: „Anwendungssituationen mithilfe des Urnenmodells (mit und ohne Zurücklegen) untersuchen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1121]: „kombinatorische Abzählverfahren“
      Q2, Grund- und Leistungskursfach
  - 2. Auswahlen und Binomialkoeffizient
    - Eintrag, Zeile 12: „(Q2, GK-Kern; OHiMi 2.4 „Kombinationen ohne Wiederholung“ mit Eigenschaften; FOS „Kombinationen“; FS-IQB 1.4)“
    - GOST Berlin [Zeilen 1245–1246]: „Anwendungssituationen mithilfe des Urnenmodells (mit und ohne Zurücklegen) untersuchen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1121]: „kombinatorische Abzählverfahren“
      Q2, Grund- und Leistungskursfach
    - Ermessen: Den Binomialkoeffizienten nennt kein Plan beim Namen; zugeordnet ist die Inhaltszeile „kombinatorische Abzählverfahren“.
  - 3. Zählen mit Bedingungen und Wahrscheinlichkeitsterme
    - Eintrag, Zeile 13: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1245–1246]: „Anwendungssituationen mithilfe des Urnenmodells (mit und ohne Zurücklegen) untersuchen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1121–1122]: „Anwendungssituationen mithilfe von Urnenmodellen untersuchen,“
      Q2, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 2 Zeilen GK / 2 Zeilen LK, 4 Haupttypen
    - Anteil der Kennwörter aus einer Teilmenge der Zeichen mit Wiederholung berechnen: 0 GK / 1 LK
    - Anzahl der Kennwörter mit fester Buchstabenfolge und zwei Zusatzzeichen berechnen: 0 GK / 1 LK
    - Anzahl der Sitzordnungen mit Abstandsbedingung berechnen: 1 GK / 0 LK
    - Auswahlen mit Abstandsbedingung aufzählen: 1 GK / 0 LK
  - iqb: 5 Zeilen GK / 8 Zeilen LK, 12 Haupttypen
    - Anzahl der Sitzordnungen mit Abstandsbedingung berechnen: 2 GK / 0 LK
    - Anteil der Kennwörter aus einer Teilmenge der Zeichen mit Wiederholung berechnen: 0 GK / 1 LK
    - Anzahl der Kennwörter mit fester Buchstabenfolge und zwei Zusatzzeichen berechnen: 0 GK / 1 LK
    - Anzahl der Kombinationen aus zwei getrennten Auswahlgruppen ermitteln: 1 GK / 0 LK
    - Anzahl der Zahlenkombinationen mit einer vierfachen Ziffer aus drei Ziffern berechnen: 0 GK / 1 LK
    - Anzahl der Zusammensetzungen mit Mengenbedingungen je Sorte bestimmen: 0 GK / 1 LK
    - Anzahl geordneter Auswahlen ohne Wiederholung berechnen: 1 GK / 0 LK
    - Auswahlen mit Abstandsbedingung aufzählen: 1 GK / 0 LK
    - Faktoren eines kombinatorischen Terms im Sachzusammenhang deuten: 0 GK / 1 LK
    - Kleinstes n, für das die Wahrscheinlichkeit lauter verschiedener Ergebnisse unter eine Schranke fällt, ermitteln: 0 GK / 1 LK
    - Term für das Gegenereignis einer festen Häufigkeitsverteilung bei mehreren Würfen angeben: 0 GK / 1 LK
    - Term für die Wahrscheinlichkeit aufstellen, dass jede Zahl mindestens einmal fällt: 0 GK / 1 LK
  - fhr: 15 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 7 GK / 10 LK)

### konfidenzintervalle
- Geltung je Zielprüfung:
  - Thema „Konfidenzintervalle“ (`themen.csv`):
    - be-gk: nein – `| Konfidenzintervalle | nein |` [abi-be-gk-geltung.md Zeile 62]
    - be-lk: nein – `| Konfidenzintervalle | nein |` [abi-be-lk-geltung.md Zeile 62]
    - bb-gk: nein – `| Konfidenzintervalle | nein |` [abi-bb-gk-geltung.md Zeile 62]
    - bb-ea: nein – `| Konfidenzintervalle | nein |` [abi-bb-ea-geltung.md Zeile 62]
- Lerneinheiten:
  - 1. Das Intervall lesen und deuten: die Überdeckungsdeutung (verträglich heißt: der angenommene Anteil wird vom Intervall überdeckt
    - Eintrag, Zeile 11: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1249–1250]: „in einfachen Fällen aufgrund von Stichproben auf die Gesamtheit schließen (k-σ-Intervalle, Signifikanzbegriff).“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1321–1322]: „in einfachen Fällen aufgrund von Stichproben auf die Gesamtheit schließen.“
      Q4, Grund- und Leistungskursfach
    - Ermessen: Konfidenz-, Vertrauens- oder Prognoseintervalle nennt kein Plan; zugeordnet ist die Zeile zum Schluss von der Stichprobe auf die Gesamtheit.
  - 2. Mit der Näherungsformel rechnen: die Grenzgleichung nach p lösen (quadratisch
    - Eintrag, Zeile 12: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1249–1250]: „in einfachen Fällen aufgrund von Stichproben auf die Gesamtheit schließen (k-σ-Intervalle, Signifikanzbegriff).“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1323–1324]: „Schätzung von Wahrscheinlichkeiten aus relativen Häufigkeiten mit den k-σ-Regeln“
      Q4, Grund- und Leistungskursfach
  - 3. Argumente über Formel und Verträglichkeit: die Länge des Intervalls bei doppeltem Umfang (Faktor eins durch Wurzel zwei
    - Eintrag, Zeile 13: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1249–1250]: „in einfachen Fällen aufgrund von Stichproben auf die Gesamtheit schließen (k-σ-Intervalle, Signifikanzbegriff).“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1323–1324]: „Schätzung von Wahrscheinlichkeiten aus relativen Häufigkeiten mit den k-σ-Regeln“
      Q4, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 0 Zeilen GK / 0 Zeilen LK, 0 Haupttypen
  - iqb: 0 Zeilen GK / 12 Zeilen LK, 9 Haupttypen
    - Anteil mit genau k von n Konfidenzintervallen verträglich aus dem Diagramm angeben: 0 GK / 2 LK
    - Anzahl überdeckender Konfidenzintervalle als binomialverteilt begründen und Wahrscheinlichkeit berechnen: 0 GK / 2 LK
    - Konfidenzintervall aus den Graphen der Grenzfunktionen ablesen und eine Vermutung auf Verträglichkeit beurteilen: 0 GK / 2 LK
    - Grenzen eines Konfidenzintervalls aus dem Stichprobenergebnis über die Näherungsformel berechnen und im Diagramm zuordnen: 0 GK / 1 LK
    - Kleinsten Stichprobenumfang für die Unverträglichkeit eines Anteils mit einer Annahme über die Näherungsformel ermitteln: 0 GK / 1 LK
    - Konfidenzintervall aus dem Diagramm identifizieren und Stichprobenergebnis aus der Grenze berechnen: 0 GK / 1 LK
    - Länge eines Konfidenzintervalls bei doppeltem Stichprobenumfang über den Faktor 1/√2 begründen: 0 GK / 1 LK
    - Obere Grenze eines Konfidenzintervalls über den Stichprobenanteil begründen und Verträglichkeit einer Annahme beschreiben: 0 GK / 1 LK
    - Verträglichkeit zweier Annahmen mit demselben Stichprobenanteil über den Stichprobenumfang beurteilen: 0 GK / 1 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: kein Planinhalt – die Geltung ist viermal nein (Einheiten: nur GK-Block; Typenzeilen: 0 GK / 12 LK)
- Befund: Die Geltung ist viermal nein, deshalb „kein Planinhalt“ – der IQB-Pool führt das Thema mit zwölf Zeilen auf erhöhtem Niveau, keiner auf grundlegendem.

### kurvenuntersuchung
- Geltung je Zielprüfung:
  - Thema „Kurvenuntersuchung“ (`themen.csv`):
    - be-gk: ja – `| Kurvenuntersuchung | ja |` [abi-be-gk-geltung.md Zeile 23]
    - be-lk: ja – `| Kurvenuntersuchung | ja |` [abi-be-lk-geltung.md Zeile 23]
    - bb-gk: ja – `| Kurvenuntersuchung | ja |` [abi-bb-gk-geltung.md Zeile 23]
    - bb-ea: ja – `| Kurvenuntersuchung | ja |` [abi-bb-ea-geltung.md Zeile 23]
- Lerneinheiten:
  - 1. Monotonie und erste Ableitung
    - Eintrag, Zeile 11: „(Q1, GK-Kern; FOS „Monotonie und 1. Ableitung“)“
    - GOST Berlin [Zeilen 1186–1187]: „die Ableitung zur Bestimmung von Monotonie, Extrema und Wendepunkten (notwendige Bedingung und inhaltliche Begründungen für die Existenz) von“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 968–969]: „die Ableitung zur Bestimmung von Monotonie, Extrem- und Wendepunkten“
      Q1, Grund- und Leistungskursfach
  - 2. Extrempunkte
    - Eintrag, Zeile 12: „(Q1, GK-Kern; FOS „lokale Extrempunkte“, „Sattelpunkte“)“
    - GOST Berlin [Zeilen 1186–1187]: „die Ableitung zur Bestimmung von Monotonie, Extrema und Wendepunkten (notwendige Bedingung und inhaltliche Begründungen für die Existenz) von“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Berlin [Zeilen 1208–1209]: „Ableitungen zur Bestimmung von Extrema und Wendepunkten (notwendige Bedingung und hinreichende) von Funktionen nutzen,“
      Funktionaler Zusammenhang [L4], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 968–969]: „die Ableitung zur Bestimmung von Monotonie, Extrem- und Wendepunkten“
      Q1, Grund- und Leistungskursfach
    - Ermessen: Länderunterschied: die hinreichende Bedingung steht in Berlin im LK-Zusatz, in Brandenburg im Grund- und Leistungskursfach (Inhaltszeile 970–972).
  - 3. Krümmung und Wendepunkte
    - Eintrag, Zeile 13: „(Q1, GK-Kern; FOS „Krümmung und 2. Ableitung“, „Wendepunkte und Sattelpunkte“)“
    - GOST Berlin [Zeilen 1186–1187]: „die Ableitung zur Bestimmung von Monotonie, Extrema und Wendepunkten (notwendige Bedingung und inhaltliche Begründungen für die Existenz) von“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 968–969]: „die Ableitung zur Bestimmung von Monotonie, Extrem- und Wendepunkten“
      Q1, Grund- und Leistungskursfach
    - Ermessen: Die Krümmung nennt Brandenburg nur in der Inhaltsspalte derselben Zeile („Zusammenhang zwischen Krümmungsverhalten und zweiter Ableitung“, Zeilen 973–976); zitiert ist die Kompetenzzeile.
  - 4. Graph und Ableitungsgraph
    - Eintrag, Zeile 14: „(Q1, GK-Kern „den Ableitungsgraphen aus dem Funktionsgraphen entwickeln“; FOS nur „grafische Darstellung“ und „graphisches Differenzieren“)“
    - GOST Berlin [Zeile 1189]: „Ableitungsgraphen aus Funktionsgraphen entwickeln und umgekehrt,“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 982–983]: „den Ableitungsgraphen aus dem Funktionsgraphen entwickeln.“
      Q1, Grund- und Leistungskursfach
  - 5. Kurvenuntersuchung im Sachzusammenhang
    - Eintrag, Zeile 15: „(Q1, GK-Kern „lokale Änderungsrate auch in Sachzusammenhängen“, „Randextrema“; FOS „Modellierung von Verläufen und Formen … im …“
    - GOST Berlin [Zeilen 1165–1166]: „Potenzfunktionen mit ganzzahligen Exponenten, ganzrationale und Exponentialfunktionen zur Beschreibung und Untersuchung quantifizierbarer Zusammen-“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 926–927]: „Funktionseigenschaften, auch in Anwendungszusammenhängen:“
      Q1, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 45 Zeilen GK / 13 Zeilen LK, 39 Haupttypen
    - Lage und Art aller lokalen Extrempunkte bestimmen: 6 GK / 0 LK
    - Hochpunkt eines Produkts aus Polynom und e-Funktion berechnen: 4 GK / 1 LK
    - Wendepunkte über die zweite Ableitung berechnen: 5 GK / 0 LK
    - Extrempunkt an vorgegebener Stelle nachweisen: 2 GK / 1 LK
    - Graphen einer Funktion in ein vorgegebenes Koordinatensystem einzeichnen: 3 GK / 0 LK
    - Monotonie über das Vorzeichen der Ableitung am Term nachweisen: 1 GK / 1 LK
    - Zeitpunkt stärkster Abnahme über das Minimum der Ableitung berechnen: 2 GK / 0 LK
    - Abstand zweier Extrempunkte verschiedener Graphen mit einer Schranke vergleichen: 1 GK / 0 LK
    - Achsenschnittpunkte angeben und Hochpunkt aus der gegebenen Ableitung begründen: 1 GK / 0 LK
    - Anstieg null nachweisen und fehlende Extremstelle über die doppelte Nullstelle der Ableitung ohne Rechnung begründen: 0 GK / 1 LK
    - Aussagen über Funktions- und Ableitungswert nahe dem Tiefpunkt ohne Rechnung beurteilen: 1 GK / 0 LK
    - Aussagen über die Normale an der Wendestelle und den Wertebereich der Ableitung beurteilen: 1 GK / 0 LK
    - Einzigen Tiefpunkt über die streng monotone Ableitung nachweisen und berechnen: 0 GK / 1 LK
    - Existenz eines Wendepunkts aus Tiefpunkt und Grenzverhalten über eine Skizze begründen: 1 GK / 0 LK
    - Extrempunkte berechnen und ihre Verbindungsgerade als Winkelhalbierende nachweisen: 1 GK / 0 LK
    - Extremstelle einer Logarithmusfunktion über die Ableitung oder die Symmetrie begründen: 0 GK / 1 LK
    - Extremstelle über den Vorzeichenwechsel der Ableitung in ein Intervall einschließen: 1 GK / 0 LK
    - Extremstellen aus den Nullstellen der Ableitung berechnen: 1 GK / 0 LK
    - Fehlende Extrempunkte über eine positive Ableitung begründen: 0 GK / 1 LK
    - Graphen skizzieren und Aussage über die Anzahl gemeinsamer Punkte von Tangente und Graph beurteilen: 1 GK / 0 LK
    - Graphen zu vorgegebenen Nullstellen, Extrem- und Wendestellen skizzieren: 0 GK / 1 LK
    - Größten Funktionswert über Monotonie, Grenzverhalten und Symmetrie begründen und Wertemenge angeben: 0 GK / 1 LK
    - Lage eines Punktes aus Bedingungen an Funktionswert und Ableitung am Graphen beschreiben: 1 GK / 0 LK
    - Maximum eines Bestands an vorgegebener Stelle im Sachzusammenhang nachweisen: 1 GK / 0 LK
    - Maße und Masse eines umschließenden Quaders eines Rotationskörpers aus Hochpunkt und Bereich mit Maßstab berechnen: 1 GK / 0 LK
    - Mindestgrad einer ganzrationalen Funktion aus Eigenschaften der Ableitung begründen: 0 GK / 1 LK
    - Mittleren Wert einer periodisch schwankenden Größe am Graphen ablesen: 1 GK / 0 LK
    - Monotonieintervalle und Wertebereich einer Differenzfunktion auf einem Intervall über die Ableitung ermitteln: 1 GK / 0 LK
    - Monotonieverhalten aus einem bekannten Extrempunkt angeben: 1 GK / 0 LK
    - Passung eines Profils in einen Karton über Breite und Tiefe aus Nullstellen und Tiefpunkt prüfen: 1 GK / 0 LK
    - Stellen mit maximalem Funktionswert einschließlich Rand bestimmen: 0 GK / 1 LK
    - Verlauf eines Graphen im Sachzusammenhang beschreiben: 1 GK / 0 LK
    - Volumen eines umschließenden Quaders aus den Achsenschnittpunkten mit Maßstab berechnen: 1 GK / 0 LK
    - Wendepunkt als Zeitpunkt stärkster Zu- oder Abnahme im Sachzusammenhang deuten: 1 GK / 0 LK
    - Wendepunkt mit negativer Steigung am Graphen markieren und begründen: 1 GK / 0 LK
    - Wendepunkt mit vorgegebenen Koordinaten über die zweite Ableitung nachweisen und den symmetrischen Wendepunkt angeben: 0 GK / 1 LK
    - Werte für einen Ableitungswert und eine Wendestelle am Graphen ablesen: 1 GK / 0 LK
    - Wertebereich einer ganzrationalen Funktion über den globalen Tiefpunkt ermitteln: 0 GK / 1 LK
    - Zweite Ableitung nachweisen und Wendepunkt an vorgegebener Stelle zeigen: 1 GK / 0 LK
  - iqb: 35 Zeilen GK / 18 Zeilen LK, 37 Haupttypen
    - Extrempunkt an vorgegebener Stelle nachweisen: 5 GK / 1 LK
    - Hochpunkt eines Produkts aus Polynom und e-Funktion berechnen: 2 GK / 1 LK
    - Verlauf eines Graphen im Sachzusammenhang beschreiben: 2 GK / 1 LK
    - Wendepunkt als Zeitpunkt stärkster Zu- oder Abnahme im Sachzusammenhang deuten: 3 GK / 0 LK
    - Gewinnbereich als Bereich zwischen den Schnittstellen von Erlösgerade und Kostengraph zeichnerisch bestimmen: 1 GK / 1 LK
    - Maximum einer ganzrationalen Funktion im Sachzusammenhang über die Ableitung berechnen: 1 GK / 1 LK
    - Monotonie über das Vorzeichen der Ableitung am Term nachweisen: 1 GK / 1 LK
    - Wendepunkt an vorgegebener Stelle nachweisen und Wendetangente aufstellen: 1 GK / 1 LK
    - Zeitpunkt stärkster Abnahme über das Minimum der Ableitung berechnen: 1 GK / 1 LK
    - Ableitungswert an der Wendestelle als stärksten Anstieg der Rate im Sachzusammenhang deuten: 0 GK / 1 LK
    - Abstand zweier Extrempunkte über die Punktsymmetrie berechnen: 1 GK / 0 LK
    - Abstand zwischen Parabel und waagerechter Gerade über den Scheitel beschreiben: 1 GK / 0 LK
    - Achsenschnittpunkte angeben und Hochpunkt aus der gegebenen Ableitung begründen: 1 GK / 0 LK
    - Anzahl der Schnittpunkte von Geraden durch den Wendepunkt mit dem Graphen nach der Steigung unterscheiden: 0 GK / 1 LK
    - Aufgabenstellung zu Extremstellen und Wertedifferenz aus dem Lösungsweg formulieren und erläutern: 1 GK / 0 LK
    - Berührung des Graphen mit der x-Achse über die Extrempunkte begründen: 1 GK / 0 LK
    - Differenzfunktion und ihr Maximum aus einem Lösungsweg im Sachzusammenhang deuten: 1 GK / 0 LK
    - Extremstellen berechnen und Monotonieverhalten angeben: 1 GK / 0 LK
    - Fehlende Extrempunkte über eine positive Ableitung begründen: 0 GK / 1 LK
    - Funktionswert an der Stelle stärkster Abnahme am Graphen ablesen: 1 GK / 0 LK
    - Gemeinsamen Punkt zweier Graphen über gleiche Flächeninhalte indirekt begründen: 0 GK / 1 LK
    - Gerade durch die beiden Wendepunkte aufstellen und parallele Gerade mit genau einem gemeinsamen Punkt einzeichnen: 1 GK / 0 LK
    - Graphen zu vorgegebenen Nullstellen, Extrem- und Wendestellen skizzieren: 0 GK / 1 LK
    - Hochpunkt mit vorgegebenen Koordinaten und waagerechte Tangente im Ursprung rechnerisch nachweisen: 1 GK / 0 LK
    - Lage zweier Graphen aus dem Graphen ihrer Differenzfunktion beschreiben: 1 GK / 0 LK
    - Logarithmus einer Exponentialfunktion als lineare Funktion nachweisen und Steigung und Achsenabschnitt angeben: 0 GK / 1 LK
    - Länge der Monotoniebereiche zweier Modellfunktionen vergleichen und eine Aussage beurteilen: 1 GK / 0 LK
    - Maximalen Neigungswinkel über die Wendestelle berechnen und mit einer Schranke vergleichen: 0 GK / 1 LK
    - Maximum eines Bestands an vorgegebener Stelle im Sachzusammenhang nachweisen: 1 GK / 0 LK
    - Mindestgrad einer ganzrationalen Funktion aus Eigenschaften der Ableitung begründen: 0 GK / 1 LK
    - Nullstellen einer e-Funktion nachweisen und Tiefstelle berechnen: 1 GK / 0 LK
    - Nullstellen und Extremstelle einer Parabel berechnen: 1 GK / 0 LK
    - Passung eines Profils in einen Karton über Breite und Tiefe aus Nullstellen und Tiefpunkt prüfen: 1 GK / 0 LK
    - Tiefpunkt angeben und Fehlen weiterer Extrempunkte über die Ableitung nachweisen: 1 GK / 0 LK
    - Wendepunkt über den Vorzeichenwechsel der zweiten Ableitung aus der Kettenregel am Graphen nachweisen: 0 GK / 1 LK
    - Wendestelle nachweisen und Winkel der Wendetangente mit der x-Achse über die Steigung −1 zeigen: 1 GK / 0 LK
    - Wendestellen einer Sinusfunktion als ganzzahlig nachweisen und die beiden Wendetangentensteigungen zeigen: 0 GK / 1 LK
  - fhr: 39 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: GK-Block und LK-Block; Typenzeilen: 80 GK / 31 LK)

### lagebeziehungen
- Geltung je Zielprüfung:
  - Thema „Lagebeziehungen“ (`themen.csv`):
    - be-gk: ja – `| Lagebeziehungen | ja |` [abi-be-gk-geltung.md Zeile 39]
    - be-lk: ja – `| Lagebeziehungen | ja |` [abi-be-lk-geltung.md Zeile 39]
    - bb-gk: ja – `| Lagebeziehungen | ja |` [abi-bb-gk-geltung.md Zeile 39]
    - bb-ea: ja – `| Lagebeziehungen | ja |` [abi-bb-ea-geltung.md Zeile 39]
- Lerneinheiten:
  - 1. Punktprobe und Seitenlage
    - Eintrag, Zeile 11: „(Q3, GK-Kern „Lagebeziehungen zwischen: … Punkt und Ebene“; OHiMi 2.3 „Lagebeziehungen …“)“
    - GOST Berlin [Zeilen 1142–1143]: „Geraden und Ebenen (durch Parameter-, Koordinaten- und Normalenform) analytisch beschreiben und Lagebeziehungen untersuchen (vgl. L2).“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1281–1282]: „Lagebeziehungen zwischen: Punkt und Gerade“
      Q3, Grund- und Leistungskursfach
  - 2. Parameter aus der Lagebedingung
    - Eintrag, Zeile 12: „(Q3, GK-Kern „Lagebeziehungen …“ rückwärts gelesen; Teil-A-Praxis des Pools)“
    - GOST Berlin [Zeilen 1142–1143]: „Geraden und Ebenen (durch Parameter-, Koordinaten- und Normalenform) analytisch beschreiben und Lagebeziehungen untersuchen (vgl. L2).“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Berlin [Zeilen 1148–1149]: „die Lagebeziehungen von Punkten, Geraden und Ebenen (auch Scharen) untersuchen.“
      Raum und Form [L3], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1300–1301]: „die Lagebeziehungen von Geraden und Ebenen untersuchen.“
      Q3, Zusätzlich im Leistungskursfach
    - Ermessen: Parameter in der Lagebedingung führen auf Scharen; die stehen in beiden Ländern nur im LK-Zusatz.
  - 3. Gerade und Ebene
    - Eintrag, Zeile 13: „(Q3, GK-Kern „Lagebeziehungen zwischen: … Gerade und Ebene“; LK „auch Scharen“)“
    - GOST Berlin [Zeilen 1142–1143]: „Geraden und Ebenen (durch Parameter-, Koordinaten- und Normalenform) analytisch beschreiben und Lagebeziehungen untersuchen (vgl. L2).“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1284]: „Gerade und Ebene“
      Q3, Grund- und Leistungskursfach
  - 4. Lagebefunde im Sachzusammenhang
    - Eintrag, Zeile 14: „(Q3, GK-Kern; die Prüfungsform trägt Teil B mit Maßstab und Bereichsprüfung)“
    - GOST Berlin [Zeilen 1142–1143]: „Geraden und Ebenen (durch Parameter-, Koordinaten- und Normalenform) analytisch beschreiben und Lagebeziehungen untersuchen (vgl. L2).“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1268–1269]: „Geraden und Ebenen analytisch beschreiben und Lagebeziehungen von“
      Q3, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 8 Zeilen GK / 5 Zeilen LK, 7 Haupttypen
    - Punkt und Ebene: Punktprobe an einer Ebenengleichung durchführen: 5 GK / 0 LK
    - Gerade und Ebene: Lage einer Geraden in einer Ebene durch Einsetzen nachweisen: 1 GK / 1 LK
    - Punkt und Ebene: Parameter einer Ebenengleichung aus einem enthaltenen Punkt bestimmen: 0 GK / 2 LK
    - Gerade und Ebene: Kreisbahn einer Drehung um eine Kante als Kreis in einer Ebene mit Mittelpunkt begründen: 0 GK / 1 LK
    - Gerade und Ebene: Lage einer Geradenschar zu einer Ebene mit Fallunterscheidung nach dem Parameter untersuchen: 0 GK / 1 LK
    - Gerade und Ebene: Parallelität einer Geraden zu einer Koordinatenebene über die z-Koordinaten entscheiden: 1 GK / 0 LK
    - Punkt und Ebene: Lage eines Punktes zwischen zwei parallelen Ebenen über Einsetzen in die Koordinatengleichungen begründen: 1 GK / 0 LK
  - iqb: 10 Zeilen GK / 15 Zeilen LK, 15 Haupttypen
    - Punkt und Ebene: Parameter einer Ebenengleichung aus einem enthaltenen Punkt bestimmen: 2 GK / 3 LK
    - Punkt und Ebene: Punktprobe an einer Ebenengleichung durchführen: 3 GK / 2 LK
    - Gerade und Ebene: Lage einer Geraden in einer Ebene durch Einsetzen nachweisen: 0 GK / 2 LK
    - Gerade und Ebene: Spurpunkt einer Lichtgeraden als Schatten auf der Wand aus einem Lösungsweg erläutern: 2 GK / 0 LK
    - Gerade und Ebene: Berühren einer Geraden mit einem Netz über die Höhe des Durchstoßpunkts in der Netzebene untersuchen: 0 GK / 1 LK
    - Gerade und Ebene: Existenz unendlich vieler Ebenen ohne Punkt mit drei gleichen Koordinaten begründen: 0 GK / 1 LK
    - Gerade und Ebene: Kreisbahn einer Drehung um eine Kante als Kreis in einer Ebene mit Mittelpunkt begründen: 0 GK / 1 LK
    - Gerade und Ebene: Parallelität einer Geraden zu einer Koordinatenebene über die z-Koordinaten entscheiden: 1 GK / 0 LK
    - Gerade und Ebene: Schattenpunkt auf einer Wand als Schnitt von Lichtstrahl und Ebene untersuchen: 0 GK / 1 LK
    - Punkt und Ebene: Aufgabenstellung zu einer Punktprobe auf einer Kante aus dem Lösungsweg formulieren: 1 GK / 0 LK
    - Punkt und Ebene: Auftreffpunkt einer Bahnkurve auf der Grundebene berechnen und Lage innerhalb des Spielfelds prüfen: 0 GK / 1 LK
    - Punkt und Ebene: Aussage über das Innere eines Dreiecks unter Koordinatentausch mit einem Gegenbeispiel widerlegen: 0 GK / 1 LK
    - Punkt und Ebene: Parameterwerte für gemeinsame Punkte einer Pyramidenschar mit einer Ebene untersuchen: 0 GK / 1 LK
    - Punkt und Ebene: Punkt der Ebene mit drei gleichen Koordinaten bestimmen: 0 GK / 1 LK
    - Punkt und Ebene: Verlauf zweier Ebenen durch das Innere eines Körpers über Punktproben und Vorzeichen untersuchen: 1 GK / 0 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: GK-Block und LK-Block; Typenzeilen: 18 GK / 20 LK)

### linearkombination-und-lineare-abhaengigkeit
- Geltung je Zielprüfung:
  - Thema „Linearkombination und lineare Abhängigkeit“ (`themen.csv`):
    - be-gk: ja – `| Linearkombination und lineare Abhängigkeit | ja |` [abi-be-gk-geltung.md Zeile 36]
    - be-lk: ja – `| Linearkombination und lineare Abhängigkeit | ja |` [abi-be-lk-geltung.md Zeile 36]
    - bb-gk: ja – `| Linearkombination und lineare Abhängigkeit | ja |` [abi-bb-gk-geltung.md Zeile 36]
    - bb-ea: ja – `| Linearkombination und lineare Abhängigkeit | ja |` [abi-bb-ea-geltung.md Zeile 36]
- Lerneinheiten:
  - 1. Kollinearität und lineare Abhängigkeit
    - Eintrag, Zeile 11: „(Q3, GK-Kern „lineare Abhängigkeit und lineare Unabhängigkeit von Vektoren“; OHiMi 2.3 „Untersuchung von Vektoren auf lineare Abhängigkeit …“
    - GOST Berlin [Zeilen 1137–1138]: „elementare Operationen mit geometrischen Vektoren ausführen und Vektoren auf Kollinearität untersuchen,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1242–1243]: „lineare Abhängigkeit und lineare Unabhängigkeit von Vektoren“
      Q3, Grund- und Leistungskursfach
  - 2. Linearkombination mit Nebenbedingung
    - Eintrag, Zeile 12: „(Q3, GK-Kern „Darstellung von Vektoren als Linearkombinationen anderer Vektoren“; die Deutung als Strecke ist Prüfungspraxis ohne eigenen …“
    - GOST Berlin [Zeilen 1137–1138]: „elementare Operationen mit geometrischen Vektoren ausführen und Vektoren auf Kollinearität untersuchen,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1240–1241]: „Darstellung von Vektoren als Linear-kombinationen anderer Vektoren“
      Q3, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 0 Zeilen GK / 1 Zeilen LK, 1 Haupttypen
    - Lage eines Punktes auf einer Strecke über eine Linearkombination nachweisen: 0 GK / 1 LK
  - iqb: 0 Zeilen GK / 0 Zeilen LK, 0 Haupttypen
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 0 GK / 1 LK)
- Befund: Wie bei den Integrationsregeln: eine einzige Zeile, auf erhöhtem Niveau; die Stellen im Plan stehen in beiden Ländern im Grund- und Leistungskursfach.

### matrizen-und-uebergangsprozesse
- Geltung je Zielprüfung:
  - Thema „Matrizen und Übergangsprozesse“ (`themen.csv`):
    - be-gk: nein – `| Matrizen und Übergangsprozesse | nein |` [abi-be-gk-geltung.md Zeile 47]
    - be-lk: nein – `| Matrizen und Übergangsprozesse | nein |` [abi-be-lk-geltung.md Zeile 47]
    - bb-gk: nein – `| Matrizen und Übergangsprozesse | nein |` [abi-bb-gk-geltung.md Zeile 47]
    - bb-ea: nein – `| Matrizen und Übergangsprozesse | nein |` [abi-bb-ea-geltung.md Zeile 47]
- Lerneinheiten:
  - 1. Matrizen als Rechenobjekte
    - Eintrag, Zeile 11: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1056–1057]: „einfache Sachverhalte mit Tupeln (Listen, Vektoren) bzw. Matrizen (Koeffizientenmatrizen, Tabellen) beschreiben.“
      Zahlen und Operationen [L1], Grundkursfach und Leistungskursfach
    - GOST Brandenburg: keine Stelle
    - Ermessen: Brandenburg kennt Matrizen nicht: die entsprechende Zeile des dritten Kurshalbjahrs nennt nur Tupel („einfache Sachverhalte mit Tupeln beschreiben“, Zeilen 1209–1210). Keine Stelle.
  - 2. Vektoren unter Matrizen
    - Eintrag, Zeile 12: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1056–1057]: „einfache Sachverhalte mit Tupeln (Listen, Vektoren) bzw. Matrizen (Koeffizientenmatrizen, Tabellen) beschreiben.“
      Zahlen und Operationen [L1], Grundkursfach und Leistungskursfach
    - GOST Brandenburg: keine Stelle
    - Ermessen: wie Einheit 1: keine Stelle in Brandenburg.
  - 3. Verflechtung
    - Eintrag, Zeile 13: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1056–1057]: „einfache Sachverhalte mit Tupeln (Listen, Vektoren) bzw. Matrizen (Koeffizientenmatrizen, Tabellen) beschreiben.“
      Zahlen und Operationen [L1], Grundkursfach und Leistungskursfach
    - GOST Brandenburg: keine Stelle
    - Ermessen: wie Einheit 1: keine Stelle in Brandenburg.
  - 4. Übergangsmodell
    - Eintrag, Zeile 14: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1056–1057]: „einfache Sachverhalte mit Tupeln (Listen, Vektoren) bzw. Matrizen (Koeffizientenmatrizen, Tabellen) beschreiben.“
      Zahlen und Operationen [L1], Grundkursfach und Leistungskursfach
    - GOST Brandenburg: keine Stelle
    - Ermessen: Übergangs- und Prozessmatrizen nennt auch Berlin nicht; die Berliner Zeile nennt Matrizen nur als Beschreibungsmittel („Koeffizientenmatrizen, Tabellen“).
  - 5. Stationär und langfristig
    - Eintrag, Zeile 15: keine Kursartmarke in der Einheitszeile
    - GOST Berlin: keine Stelle
    - GOST Brandenburg: keine Stelle
    - Ermessen: Stationäre Verteilung und Langfristverhalten nennt keiner der beiden Pläne. Keine Stelle.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 0 Zeilen GK / 0 Zeilen LK, 0 Haupttypen
  - iqb: 80 Zeilen GK / 74 Zeilen LK, 115 Haupttypen
    - Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen: 6 GK / 3 LK
    - Übergangsprozess: Matrixeintrag im Sachzusammenhang deuten: 2 GK / 3 LK
    - Matrizenalgebra: Alle Vektoren mit M · v = t · v für festes t bestimmen: 2 GK / 2 LK
    - Matrizenalgebra: Matrix-Vektor-Produkt berechnen: 4 GK / 0 LK
    - Verflechtung: Rohstoffbedarf über die Verflechtungsmatrix berechnen: 0 GK / 4 LK
    - Übergangsprozess: Unbekannte der Übergangsmatrix und des Bestands aus einem stationären Vektor bestimmen: 2 GK / 1 LK
    - Matrizenalgebra: Alle mit einer Matrix vertauschbaren Matrizen ermitteln: 0 GK / 2 LK
    - Matrizenalgebra: Erhalt der Spaltensumme unter einer stochastischen Matrix allgemein nachweisen: 0 GK / 2 LK
    - Matrizenalgebra: Inverse Matrix über A · B = E bestimmen: 2 GK / 0 LK
    - Matrizenalgebra: Parameter eines Vektors aus einer Matrix-Vektor-Gleichung bestimmen: 1 GK / 1 LK
    - Verflechtung: Eintrag der Gesamtmatrix aus dem Diagramm bestätigen und Nulleintrag begründen: 2 GK / 0 LK
    - Verflechtung: Format der Bedarfsmatrix aus der Anzahl der Stufenprodukte begründen: 2 GK / 0 LK
    - Verflechtung: Gesamtmatrix im Sachzusammenhang deuten: 0 GK / 2 LK
    - Verflechtung: Maximale Kostensteigerung eines Rohstoffs aus einer Kostenschranke bestimmen: 0 GK / 2 LK
    - Verflechtung: Maximale Produktionsmenge aus dem Rohstoffvorrat ermitteln: 0 GK / 2 LK
    - Verflechtung: Produktionsmengen aus dem Rohstoffverbrauch über ein Gleichungssystem ermitteln: 2 GK / 0 LK
    - Verflechtung: Rohstoffmenge aus den übrigen Rohstoffen über die Gesamtmatrix bestimmen: 0 GK / 2 LK
    - Übergangsprozess: Spanne einer Komponente nach einem Schritt bei teilweise bekannter Verteilung ermitteln: 2 GK / 0 LK
    - Übergangsprozess: Stationäre Verteilung mit vorgegebener Gesamtzahl berechnen und einen Anteil beurteilen: 1 GK / 1 LK
    - Übergangsprozess: Term mit Matrixpotenz und Zugang im Sachzusammenhang auswählen und deuten: 2 GK / 0 LK
    - Übergangsprozess: Verteilung nach einem Übergang berechnen und einen Anteil angeben: 2 GK / 0 LK
    - Übergangsprozess: Zeitpunkt für das Unterschreiten eines Anteils der Populationsgröße über einen konstanten Faktor bestimmen: 1 GK / 1 LK
    - Matrizenalgebra: Abbildungsmatrix als Spiegelung an einer Koordinatenachse deuten: 0 GK / 1 LK
    - Matrizenalgebra: Abbildungsmatrix aus einer geometrischen Bedingung an den Bildpunkt bestimmen: 0 GK / 1 LK
    - Matrizenalgebra: Alle Vektoren mit M · v = t · v durch Fallunterscheidung bestimmen: 1 GK / 0 LK
    - Matrizenalgebra: Aufbau von Vertauschungsmatrizen mit vorgegebener Wirkung beschreiben: 1 GK / 0 LK
    - Matrizenalgebra: Bedingung für eine selbstinverse Matrix mit Parametern herleiten: 1 GK / 0 LK
    - Matrizenalgebra: Einträge einer Faktormatrix aus dem Produkt mit einer bekannten Matrix bestimmen: 0 GK / 1 LK
    - Matrizenalgebra: Existenz mehrerer Lösungen von M · a = 0 begründen: 1 GK / 0 LK
    - Matrizenalgebra: Existenz von Matrizen mit vorgegebener Eigenschaft über ein Gleichungssystem beurteilen: 0 GK / 1 LK
    - Matrizenalgebra: Faktor aus M² als Vielfachem der Einheitsmatrix ermitteln: 0 GK / 1 LK
    - Matrizenalgebra: Fehlende Einträge einer Matrixpotenz über Zeile mal Spalte und Spaltensumme berechnen: 1 GK / 0 LK
    - Matrizenalgebra: Ganzzahlige Einträge einer Matrix aus ihrem Quadrat bestimmen: 1 GK / 0 LK
    - Matrizenalgebra: Gleichung mit inverser Matrix über die Eigenvektorbeziehung lösen: 0 GK / 1 LK
    - Matrizenalgebra: Hohe Potenz einer Vertauschungsmatrix über das Quadrat gleich Einheitsmatrix bestimmen: 0 GK / 1 LK
    - Matrizenalgebra: Inverse einer Vertauschungsmatrix angeben: 1 GK / 0 LK
    - Matrizenalgebra: Kollinearität von M · x − x mit einem Vektor untersuchen: 1 GK / 0 LK
    - Matrizenalgebra: Konstanten Faktor der Komponentensumme von Q · u über die Spaltensummen nachweisen: 0 GK / 1 LK
    - Matrizenalgebra: Matrix mit vorgegebener Eigenschaft angeben: 0 GK / 1 LK
    - Matrizenalgebra: Mögliche Formate einer Matrix aus der Bildbarkeit eines Produkts beschreiben: 1 GK / 0 LK
    - Matrizenalgebra: Orthogonalität einer Matrix über das Produkt mit der Transponierten nachweisen: 0 GK / 1 LK
    - Matrizenalgebra: Parameter aus der Gültigkeit der binomischen Formel für zwei Matrizen bestimmen: 1 GK / 0 LK
    - Matrizenalgebra: Parameter einer Matrix aus der Orthogonalität von v und M · v bestimmen: 0 GK / 1 LK
    - Matrizenalgebra: Parameter einer Matrix aus einer Matrix-Vektor-Gleichung untersuchen: 1 GK / 0 LK
    - Matrizenalgebra: Parameter für gleiche Spur von Matrix und Inverser bestimmen: 0 GK / 1 LK
    - Matrizenalgebra: Parameterbereich für endliche Grenzwerte der Matrixpotenzen über eine Potenzfolge bestimmen: 0 GK / 1 LK
    - Matrizenalgebra: Quadrat einer Matrix mit Parameter berechnen: 1 GK / 0 LK
    - Matrizenalgebra: Quadrat einer Summe zweier Matrizen mit C · D = −D · C vereinfachen: 1 GK / 0 LK
    - Matrizenalgebra: Unlösbarkeit einer Matrix-Vektor-Gleichung über eine Nullzeile begründen: 1 GK / 0 LK
    - Matrizenalgebra: Wirkung einer Permutationsmatrix beschreiben und Einträge aus M · A · M = A bestimmen: 0 GK / 1 LK
    - Verflechtung: Bedarf eines neuen Endprodukts an Zwischenprodukten aus der Produktgleichung der Matrizen ermitteln: 0 GK / 1 LK
    - Verflechtung: Fehlenden Eintrag des Diagramms aus der Bedarfsmatrix angeben und deuten: 0 GK / 1 LK
    - Verflechtung: Höchstmenge aus einer Kostenschranke bei festem Mengenverhältnis ermitteln: 1 GK / 0 LK
    - Verflechtung: Kostengleichung mit Zeilenvektor, Matrix und Auftragsvektor erläutern und lösen: 0 GK / 1 LK
    - Verflechtung: Matrix-Vektor-Gleichung mit konkreten Zahlen im Sachzusammenhang deuten: 1 GK / 0 LK
    - Verflechtung: Matrixeintrag aus Mengenbedingungen ermitteln: 1 GK / 0 LK
    - Verflechtung: Nichtinvertierbarkeit der Gesamtmatrix im Sachzusammenhang deuten: 0 GK / 1 LK
    - Verflechtung: Produktionsmenge aus einer Anteilsbedingung an den Rohstoffverbrauch bei festem Lagerverbrauch ermitteln: 0 GK / 1 LK
    - Verflechtung: Rohstoffbedarf in Abhängigkeit von einem Matrixparameter als Gerade darstellen und erläutern: 0 GK / 1 LK
    - Verflechtung: Unbekannte Bedarfe im Diagramm aus der Gesamtmatrix bestimmen: 0 GK / 1 LK
    - Verflechtung: Verflechtungsdiagramm zu einer Matrix zeichnen: 1 GK / 0 LK
    - Verflechtung: Verflechtungsmatrix aus Sachbedingungen und Matrixprodukt bestimmen: 0 GK / 1 LK
    - Verflechtung: Verflechtungsmatrix aus dem Diagramm angeben: 1 GK / 0 LK
    - Übergangsprozess: Anteil nach zwei Übergängen aus dem Diagramm berechnen: 1 GK / 0 LK
    - Übergangsprozess: Anteil zu entfernender Individuen für einen stationären Zustand berechnen: 0 GK / 1 LK
    - Übergangsprozess: Aussage über eine Komponente nach einem Übergang bei gleicher Ausgangsverteilung beurteilen: 1 GK / 0 LK
    - Übergangsprozess: Aussage über eine gleichbleibende Komponente aus einer Matrixzeile beurteilen: 1 GK / 0 LK
    - Übergangsprozess: Aussagen über Anteile nach zwei Übergängen mit M² beurteilen: 1 GK / 0 LK
    - Übergangsprozess: Bereich eines Anteils in Abhängigkeit vom Matrixparameter über die Randwerte ermitteln: 1 GK / 0 LK
    - Übergangsprozess: Diagramm der zeitlichen Entwicklung eines Zustands aus dem Übergangsdiagramm auswählen und begründen: 0 GK / 1 LK
    - Übergangsprozess: Eintrag von M² berechnen und Zeile von M² im Sachzusammenhang deuten: 1 GK / 0 LK
    - Übergangsprozess: Einträge der Grenzmatrix im Sachzusammenhang deuten: 0 GK / 1 LK
    - Übergangsprozess: Entwicklung einer Population aus einer Potenz der inversen Matrix beschreiben: 0 GK / 1 LK
    - Übergangsprozess: Exponentielles Wachstum aus einem Eigenvektor begründen und Kurve zuordnen: 1 GK / 0 LK
    - Übergangsprozess: Fehler in einem Übergangsdiagramm gegen die Matrix begründen: 0 GK / 1 LK
    - Übergangsprozess: Geänderte Übergangsmatrix aus zwei Vorschlägen nach dem beschriebenen Wechselverhalten auswählen und begründen: 1 GK / 0 LK
    - Übergangsprozess: Gleichung aus gleichen Komponentensummen von Ausgabe- und Rückgabevektor nachweisen und deuten: 1 GK / 0 LK
    - Übergangsprozess: Gleichungssystem für die Verteilung vor einem Übergang aufstellen: 1 GK / 0 LK
    - Übergangsprozess: Größtmögliche Anzahl im Vorquartal über die inverse Matrix und Nichtnegativität bestimmen: 0 GK / 1 LK
    - Übergangsprozess: Kleinsten Zeitpunkt für das Unterschreiten eines Anteils aus dem Matrixterm bestimmen: 0 GK / 1 LK
    - Übergangsprozess: Komponentensumme eines Produkts mit der diagonalfreien Matrix als Wechslerzahl deuten: 1 GK / 0 LK
    - Übergangsprozess: Konstante prozentuale Abnahme einer Gruppe ohne Zugänge aus der Matrix begründen: 1 GK / 0 LK
    - Übergangsprozess: Langfristige Entwicklung aus M³ als Vielfachem der Einheitsmatrix durch Fallunterscheidung beschreiben: 1 GK / 0 LK
    - Übergangsprozess: Langfristige Verteilung aus dem Übergangsdiagramm beschreiben: 0 GK / 1 LK
    - Übergangsprozess: Matrix bei geänderter Reihenfolge der Zustände angeben: 0 GK / 1 LK
    - Übergangsprozess: Matrixeintrag aus einer Potenz der inversen Matrix bestimmen: 0 GK / 1 LK
    - Übergangsprozess: Matrixeintrag und Spaltensumme eins im Sachzusammenhang deuten: 1 GK / 0 LK
    - Übergangsprozess: Matrixparameter aus einer Komponente nach einem Schritt bestimmen: 1 GK / 0 LK
    - Übergangsprozess: Matrixparameter aus einer Komponente nach zwei Schritten bestimmen: 0 GK / 1 LK
    - Übergangsprozess: Monotone Entwicklung der Anteile aus der Übergangstabelle begründen: 0 GK / 1 LK
    - Übergangsprozess: Mögliche Übergangsmatrix aus Ausgabe- und Rückgabezahlen zweier Stationen mit freiem Parameter ermitteln: 1 GK / 0 LK
    - Übergangsprozess: Parameter einer Übergangsmatrix aus einer Zykluslänge bestimmen: 0 GK / 1 LK
    - Übergangsprozess: Potenz der Übergangsmatrix als mehrschrittigen Übergang deuten: 1 GK / 0 LK
    - Übergangsprozess: Potenz der Übergangsmatrix gleich Einheitsmatrix als Zyklus deuten: 1 GK / 0 LK
    - Übergangsprozess: Quadrat der Übergangsmatrix aus dem Diagramm berechnen: 0 GK / 1 LK
    - Übergangsprozess: Quadrat der Übergangsmatrix berechnen und M² · v als Zustand nach zwei Schritten deuten: 1 GK / 0 LK
    - Übergangsprozess: Rückrechnung eines Verteilungsvektors über die Inverse von M² beschreiben: 0 GK / 1 LK
    - Übergangsprozess: Spielregel zu den Übergangswahrscheinlichkeiten eines Feldes angeben: 0 GK / 1 LK
    - Übergangsprozess: Stationäre Verteilung bei absorbierendem Zustand angeben: 0 GK / 1 LK
    - Übergangsprozess: Term für die Verteilung mit zwischenzeitlichem Abgang über Diagonalmatrix und Matrixpotenzen angeben: 1 GK / 0 LK
    - Übergangsprozess: Unbekannte Anzahl aus einer Bedingung an den Folgezustand berechnen: 0 GK / 1 LK
    - Übergangsprozess: Unbekannte Komponente der Ausgangsverteilung aus dem Ergebnisvektor über ein Gleichungssystem ermitteln: 1 GK / 0 LK
    - Übergangsprozess: Unmöglichkeit einer Verteilung über eine negative Vorgängerkomponente begründen: 1 GK / 0 LK
    - Übergangsprozess: Unmöglichkeit eines konstanten Zustands über eine negative Lösung begründen: 0 GK / 1 LK
    - Übergangsprozess: Verhältnis der Anfangsbestände aus einer Gleichverteilung nach einem Übergang bestimmen: 0 GK / 1 LK
    - Übergangsprozess: Vorherige Verteilung über die inverse Matrix berechnen und prozentuale Abnahme einer Komponente angeben: 1 GK / 0 LK
    - Übergangsprozess: Wechselzahlen nach einem Übergang berechnen und Gleichgewicht deuten: 1 GK / 0 LK
    - Übergangsprozess: Zeile der Übergangsmatrix aus dem Diagramm angeben: 0 GK / 1 LK
    - Übergangsprozess: Zustand mit dem kleinsten Wechselanteil aus der Matrix ablesen: 1 GK / 0 LK
    - Übergangsprozess: Zustände nach einem und zwei Schritten aus einem Anfangszustand berechnen: 0 GK / 1 LK
    - Übergangsprozess: Übergangsdiagramm zur Matrix auswählen und fehlende Werte angeben: 1 GK / 0 LK
    - Übergangsprozess: Übergangsgleichung mit Matrix aus dem Diagramm aufstellen und Variablen deuten: 1 GK / 0 LK
    - Übergangsprozess: Übergangsmatrix aus dem Diagramm unter zwei Darstellungen auswählen und ergänzen: 1 GK / 0 LK
    - Übergangsprozess: Übergangsmatrix aus dem Übergangsdiagramm aufstellen: 0 GK / 1 LK
    - Übergangsprozess: Übergangsverhalten einer parametrisierten Matrix nach Fällen im Sachzusammenhang beschreiben: 0 GK / 1 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: kein Planinhalt – die Geltung ist viermal nein (Einheiten: nur GK-Block; Typenzeilen: 80 GK / 74 LK)
- Befund: Die Geltung ist viermal nein, deshalb „kein Planinhalt“ – der IQB-Pool führt das Thema trotzdem mit 80 Zeilen auf grundlegendem und 74 auf erhöhtem Niveau. Das ist kein Widerspruch: die Auswahl-Einschränkung steht allein in den Geltungsdateien (konzept.md § 4 Entscheidung 35).

### normalverteilung-und-sigma-regeln
- Geltung je Zielprüfung:
  - Thema „Normalverteilung und Sigma-Regeln“ (`themen.csv`):
    - be-gk: nein – `| Normalverteilung und Sigma-Regeln | nein |` [abi-be-gk-geltung.md Zeile 60]
    - be-lk: ja – `| Normalverteilung und Sigma-Regeln | ja |` [abi-be-lk-geltung.md Zeile 60]
    - bb-gk: nein – `| Normalverteilung und Sigma-Regeln | nein |` [abi-bb-gk-geltung.md Zeile 60]
    - bb-ea: ja – `| Normalverteilung und Sigma-Regeln | ja |` [abi-bb-ea-geltung.md Zeile 60]
- Lerneinheiten:
  - 1. Modell und Glockenkurve: die Dichtefunktion lesen und skizzieren (μ als Symmetrieachse und Maximumsstelle, σ als Breitenmaß
    - Eintrag, Zeile 11: „(Q4 LK; OHiMi-LK „Interpretationen von Darstellungen“; Teil-A-Stoff)“
    - GOST Berlin [Zeilen 1257–1258]: „exemplarisch diskrete und stetige Zufallsgrößen unterscheiden und die „Glockenform“ als Grundvorstellung von normalverteilten Zufallsgrößen nutzen,“
      Daten und Zufall [L5], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1348–1349]: „exemplarisch diskrete und stetige Zufallsgrößen unterscheiden und die“
      Q4, Zusätzlich im Leistungskursfach
  - 2. Wahrscheinlichkeiten berechnen: Intervall- und einseitige Wahrscheinlichkeiten mit dem Rechner, die Sigma-Regeln der Formelsammlung, Symmetrie und Gegenereignis (außerhalb wird halbiert), Sachbedingungen übersetzen („weicht um höchstens … ab“ als symmetrisches Intervall um den Sollwert, diskrete Anzahlen im stetigen Modell über halbe Schritte), Näherungen ohne Rechner (Rechteck unter der Dichte). (Q4 LK; FS-IQB Abschnitt „Sigma-Regeln“) ← Eingabe „normalverteilung wahrscheinlichkeit“, „sigma-regeln“, „intervall normalverteilung“
    - Eintrag, Zeile 12: „(Q4 LK; FS-IQB Abschnitt „Sigma-Regeln“)“
    - GOST Berlin [Zeilen 1259–1260]: „stochastische Situationen untersuchen, die zu annähernd normalverteilten Zufallsgrößen führen.“
      Daten und Zufall [L5], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1351–1352]: „Einfluss von Erwartungswert und Standardabweichung auf die Normalverteilung“
      Q4, Zusätzlich im Leistungskursfach
  - 3. Umkehraufgaben und Argumente: μ aus einer Wahrscheinlichkeitsvorgabe bei bekanntem σ, Grenzen und Quantile, μ und σ am Graphen der Verteilungsfunktion (die Stelle mit dem Wert ein Halb) und am Dichteterm ablesen ([IQB-VER 4] vorausgesetzt), Argumente über die Parameter (Monotonie in σ, das beste Intervall fester Länge liegt symmetrisch um μ). (Q4 LK; Prüfungshöhe des Pools in Teil B) ← Eingabe „umkehraufgabe normalverteilung“, „mu gesucht“, „quantil“, „parameter ablesen“
    - Eintrag, Zeile 13: „(Q4 LK; Prüfungshöhe des Pools in Teil B)“
    - GOST Berlin [Zeilen 1259–1260]: „stochastische Situationen untersuchen, die zu annähernd normalverteilten Zufallsgrößen führen.“
      Daten und Zufall [L5], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1357–1358]: „stochastische Situationen untersuchen, die zu annähernd normalverteilten Zu-“
      Q4, Zusätzlich im Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 0 Zeilen GK / 3 Zeilen LK, 3 Haupttypen
    - Vernachlässigbare Wahrscheinlichkeit eines unrealistischen Werts als Modellargument begründen: 0 GK / 1 LK
    - Wahrscheinlichkeit einer Abweichung um höchstens k über die Normalverteilung mit einer Schranke vergleichen: 0 GK / 1 LK
    - Wahrscheinlichkeit eines Intervalls der Normalverteilung mit dem Rechner berechnen: 0 GK / 1 LK
  - iqb: 0 Zeilen GK / 17 Zeilen LK, 15 Haupttypen
    - Wahrscheinlichkeit eines Intervalls der Normalverteilung mit dem Rechner berechnen: 0 GK / 3 LK
    - Dichtefunktion mit gleichem Erwartungswert und größerer Standardabweichung skizzieren: 0 GK / 1 LK
    - Dichtefunktionen zu verschobenem Erwartungswert und kleinerer Standardabweichung skizzieren und Wirkung auf eine Wahrscheinlichkeit begründen: 0 GK / 1 LK
    - Eignung der Normalverteilung trotz negativer Werte im Definitionsbereich begründen: 0 GK / 1 LK
    - Erwartungswert einer Normalverteilung aus einer Wahrscheinlichkeitsvorgabe ermitteln und weitere Wahrscheinlichkeit berechnen: 0 GK / 1 LK
    - Implikation zweier Wahrscheinlichkeitsbedingungen der Normalverteilung über eine Schranke für σ begründen: 0 GK / 1 LK
    - Maximale Wahrscheinlichkeit eines Intervalls fester Länge über die Lage um den Erwartungswert begründen: 0 GK / 1 LK
    - Näherung einer Normalverteilungswahrscheinlichkeit über Rechteck und Symmetrie erläutern: 0 GK / 1 LK
    - Parameter aus der Dichtefunktion ablesen und Bedingungen an Wahrscheinlichkeiten der Normalverteilung prüfen: 0 GK / 1 LK
    - Parameter einer Normalverteilung aus dem Graphen der Verteilungsfunktion ermitteln: 0 GK / 1 LK
    - Quantil einer Normalverteilung bestimmen und Wahrscheinlichkeit dafür bei einer zweiten Verteilung beurteilen: 0 GK / 1 LK
    - Vernachlässigbare Wahrscheinlichkeit eines unrealistischen Werts als Modellargument begründen: 0 GK / 1 LK
    - Wahrscheinlichkeit außerhalb eines symmetrischen Intervalls über die Symmetrie der Normalverteilung berechnen: 0 GK / 1 LK
    - Wahrscheinlichkeit einer Abweichung um höchstens k über die Normalverteilung mit einer Schranke vergleichen: 0 GK / 1 LK
    - Wahrscheinlichkeit eines Einzelwerts einer stetigen Zufallsgröße angeben: 0 GK / 1 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: nur LK – keine Zeile und keine Einheit im Grundkurs (Einheiten: nur LK-Block; Typenzeilen: 0 GK / 20 LK)

### orthogonalitaet
- Geltung je Zielprüfung:
  - Thema „Orthogonalität“ (`themen.csv`):
    - be-gk: ja – `| Orthogonalität | ja |` [abi-be-gk-geltung.md Zeile 42]
    - be-lk: ja – `| Orthogonalität | ja |` [abi-be-lk-geltung.md Zeile 42]
    - bb-gk: ja – `| Orthogonalität | ja |` [abi-bb-gk-geltung.md Zeile 42]
    - bb-ea: ja – `| Orthogonalität | ja |` [abi-bb-ea-geltung.md Zeile 42]
- Lerneinheiten:
  - 1. Rechte Winkel an Dreiecken nachweisen
    - Eintrag, Zeile 11: „(Q3, GK-Kern „Orthogonalität von Vektoren“; OHiMi 2.3)“
    - GOST Berlin [Zeile 1141]: „das Skalarprodukt geometrisch deuten,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1263]: „Orthogonalität von Vektoren“
      Q3, Grund- und Leistungskursfach
  - 2. Rechte Winkel rückwärts
    - Eintrag, Zeile 12: „(Q3, GK-Kern „Orthogonalität von Vektoren“ rückwärts gelesen; OHiMi 2.3)“
    - GOST Berlin [Zeile 1141]: „das Skalarprodukt geometrisch deuten,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1263]: „Orthogonalität von Vektoren“
      Q3, Grund- und Leistungskursfach
  - 3. Senkrecht zu Geraden und Ebenen
    - Eintrag, Zeile 13: „(Q3, GK-Kern „Orthogonalität von Geraden, Ebenen, Geraden und Ebenen“; OHiMi 2.3)“
    - GOST Berlin [Zeile 1141]: „das Skalarprodukt geometrisch deuten,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1218–1219]: „Orthogonalität von Geraden, Ebenen, Geraden und Ebenen“
      Q3, Grund- und Leistungskursfach
  - 4. Lot und Extremum
    - Eintrag, Zeile 14: „(Q3, GK-Kern; Eingangsvoraussetzung L3 „Ähnlichkeit“ für die Lotfiguren)“
    - GOST Berlin [Zeilen 1098–1099]: „Abstände (Punkt-Punkt, Punkt-Ebene, Gerade-Ebene, Ebene-Ebene) bestimmen.“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1220–1221]: „Abstände zwischen Punkten, Geraden und Ebenen bestimmen,“
      Q3, Grund- und Leistungskursfach
    - Ermessen: Lot und Extremum: das Verfahren steht als Abstandsbestimmung in beiden Plänen, als Extremwertzugang in keinem.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 9 Zeilen GK / 5 Zeilen LK, 11 Haupttypen
    - Dreieck: Rechten Winkel eines Dreiecks mit Parameter nachweisen: 1 GK / 1 LK
    - Geraden und Ebenen: Normalenvektor einer Ebene in Parameterform über Skalarprodukte nachweisen: 2 GK / 0 LK
    - Geraden und Ebenen: Orthogonalität zu einer Ebene über Kollinearität mit dem Normalenvektor begründen: 0 GK / 2 LK
    - Dreieck: Koordinate eines Punktes auf einer Kante für einen rechten Winkel über das Skalarprodukt berechnen: 0 GK / 1 LK
    - Dreieck: Nichtrechtwinkligkeit in einem Eckpunkt über das Skalarprodukt nachweisen: 0 GK / 1 LK
    - Dreieck: Parameter für einen rechten Winkel über das Skalarprodukt ermitteln: 1 GK / 0 LK
    - Dreieck: Rechten Winkel und Kathetenlängen eines Dreiecks nachweisen: 1 GK / 0 LK
    - Geraden und Ebenen: Ebene senkrecht zu zwei gegebenen Ebenen angeben: 1 GK / 0 LK
    - Geraden und Ebenen: Orthogonalität zweier Geraden über das Skalarprodukt untersuchen: 1 GK / 0 LK
    - Geraden und Ebenen: Parameter für die Orthogonalität zweier Ebenen bestimmen: 1 GK / 0 LK
    - Geraden und Ebenen: Punkt aus Orthogonalitäts- und Ebenenbedingung bestimmen: 1 GK / 0 LK
  - iqb: 14 Zeilen GK / 15 Zeilen LK, 19 Haupttypen
    - Geraden und Ebenen: Orthogonalität zu einer Ebene über Kollinearität mit dem Normalenvektor begründen: 1 GK / 3 LK
    - Dreieck: Parameter für einen rechten Winkel über das Skalarprodukt ermitteln: 3 GK / 0 LK
    - Dreieck: Rechten Winkel eines Dreiecks mit Parameter nachweisen: 2 GK / 1 LK
    - Dreieck: Rechten Winkel und Kathetenlängen eines Dreiecks nachweisen: 2 GK / 0 LK
    - Geraden und Ebenen: Höhe eines Quaders aus der Orthogonalität der Raumdiagonalen bestimmen und Volumen oder Oberflächeninhalt berechnen: 0 GK / 2 LK
    - Geraden und Ebenen: Orthogonalität zweier Geraden über das Skalarprodukt untersuchen: 1 GK / 1 LK
    - Dreieck: Eckpunkt eines gleichschenklig-rechtwinkligen Dreiecks mit Kathete in einer Koordinatenebene ermitteln: 0 GK / 1 LK
    - Dreieck: Gleichung für den Parameter des flächenkleinsten gleichschenkligen Dreiecks über die Orthogonalität von Höhe und Gerade begründen: 1 GK / 0 LK
    - Dreieck: Koordinate eines Punktes auf einer Kante für einen rechten Winkel über das Skalarprodukt berechnen: 0 GK / 1 LK
    - Dreieck: Nichtrechtwinkligkeit in einem Eckpunkt über das Skalarprodukt nachweisen: 1 GK / 0 LK
    - Dreieck: Parameter für den maximalen Spitzenwinkel eines gleichschenkligen Dreiecks über die minimale Höhe und die Orthogonalität zur Geraden ermitteln: 0 GK / 1 LK
    - Dreieck: Punkte auf einer Koordinatenachse mit rechtem Winkel zu zwei Punkten bestimmen: 0 GK / 1 LK
    - Dreieck: Rechten Winkel aus der Lage zu den Koordinatenachsen begründen: 0 GK / 1 LK
    - Dreieck: Streckenverhältnis am Lot im Quadrat über ähnliche Dreiecke begründen: 0 GK / 1 LK
    - Dreieck: Teilverhältnis eines Punktes auf einer Strecke aus einem rechten Winkel ermitteln: 0 GK / 1 LK
    - Geraden und Ebenen: Mittelsenkrechte einer Strecke parallel zu einer Koordinatenebene bestimmen: 0 GK / 1 LK
    - Geraden und Ebenen: Normalenvektor einer Ebene in Parameterform über Skalarprodukte nachweisen: 1 GK / 0 LK
    - Geraden und Ebenen: Parameter für die Orthogonalität zweier Ebenen bestimmen: 1 GK / 0 LK
    - Geraden und Ebenen: Punkt aus Orthogonalitäts- und Ebenenbedingung bestimmen: 1 GK / 0 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 23 GK / 20 LK)

### punkte-und-strecken-im-koordinatensystem
- Geltung je Zielprüfung:
  - Thema „Punkte und Strecken im Koordinatensystem“ (`themen.csv`):
    - be-gk: ja – `| Punkte und Strecken im Koordinatensystem | ja |` [abi-be-gk-geltung.md Zeile 34]
    - be-lk: ja – `| Punkte und Strecken im Koordinatensystem | ja |` [abi-be-lk-geltung.md Zeile 34]
    - bb-gk: ja – `| Punkte und Strecken im Koordinatensystem | ja |` [abi-bb-gk-geltung.md Zeile 34]
    - bb-ea: ja – `| Punkte und Strecken im Koordinatensystem | ja |` [abi-bb-ea-geltung.md Zeile 34]
- Lerneinheiten:
  - 1. Punkte darstellen und Lage lesen
    - Eintrag, Zeile 11: „(Q3, GK-Kern „geometrische Sachverhalte … koordinatisieren und im Koordinatensystem darstellen“; OHiMi 2.3 „Darstellung und Beschreibung von …“
    - GOST Berlin [Zeilen 1134–1135]: „geometrische Sachverhalte in Ebene und Raum koordinatisieren (geometrische Interpretation von Gleichungssystemen und ihrer Lösungen) und im Koordinaten-“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1225–1226]: „geometrische Sachverhalte in Ebene und Raum koordinatisieren und im Ko-“
      Q3, Grund- und Leistungskursfach
  - 2. Streckenlängen, Mittelpunkt und Teilpunkte
    - Eintrag, Zeile 12: „(Q3, GK-Kern L2 „Betrag eines Vektors bzw. Länge einer Strecke“, „Mittelpunkt einer Strecke“, „Abstände zwischen: Punkt – Punkt“, L3 …“
    - GOST Berlin [Zeilen 1096–1097]: „Streckenlängen und Winkelgrößen im Raum (auch mithilfe des Skalarprodukts) bestimmen,“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1230]: „Teilverhältnisse von Strecken“
      Q3, Grund- und Leistungskursfach
  - 3. Dreiecke nachweisen
    - Eintrag, Zeile 13: „GK-Kern L2/L3; OHiMi 2.3 „Betrag eines Vektors“, „Skalarprodukt“, „Orthogonalität von Vektoren“) ← Eingabe „gleichschenklig nachweisen“, …“
    - GOST Berlin [Zeilen 1139–1140]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometrischen Objekten anwenden,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1255–1256]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometri-“
      Q3, Grund- und Leistungskursfach
  - 4. Vierecke nachweisen
    - Eintrag, Zeile 14: „(Q3, GK-Kern L3 „Beschreibung geometrischer Objekte mittels Vektoren“, „Flächeninhalte von geometrischen Objekten …“; Eingangsvoraussetzung …“
    - GOST Berlin [Zeilen 1139–1140]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometrischen Objekten anwenden,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1255–1256]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometri-“
      Q3, Grund- und Leistungskursfach
  - 5. Körper im Koordinatensystem und Drehungen
    - Eintrag, Zeile 15: „(Q3, GK-Kern „Darstellung von … Körpern in … dreidimensionalen kartesischen Koordinatensystemen“; OHiMi 2.3)“
    - GOST Berlin [Zeilen 1139–1140]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometrischen Objekten anwenden,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1225–1226]: „Darstellung von Punktmengen, Geraden, Ebenen, ebenen Figuren und Körpern in“
      Q3, Grund- und Leistungskursfach
    - Ermessen: Drehungen im Koordinatensystem nennt kein Plan; zugeordnet ist die Inhaltszeile zur Darstellung von Körpern.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 18 Zeilen GK / 6 Zeilen LK, 22 Haupttypen
    - Ebene Figur: Gleichschenkligkeit oder Gleichseitigkeit eines Dreiecks über die Seitenlängen prüfen: 2 GK / 0 LK
    - Ebene Figur: Trapez über parallele Seiten nachweisen und Flächeninhalt berechnen: 2 GK / 0 LK
    - Ebene Figur: Ansatz für einen rechten Innenwinkel eines Vierecks über das Skalarprodukt mit unbekannter Koordinate erläutern: 1 GK / 0 LK
    - Ebene Figur: Benachbarte Ecke eines Quadrats über den Diagonalenschnittpunkt als Spurpunkt nachweisen: 0 GK / 1 LK
    - Ebene Figur: Gleichschenkligkeit eines Dreiecks mit Parameter über die Schenkellängen nachweisen: 1 GK / 0 LK
    - Ebene Figur: Gleichschenkligkeit über kongruente rechtwinklige Dreiecke begründen: 0 GK / 1 LK
    - Ebene Figur: Raute über vier gleich lange Seiten nachweisen: 1 GK / 0 LK
    - Ebene Figur: Trapez mit zwei gleich langen Seiten über Kollinearität und Seitenlängen nachweisen: 1 GK / 0 LK
    - Ebene Figur: Viereck in ein Schrägbild einzeichnen: 1 GK / 0 LK
    - Ebene Figur: Vierten Eckpunkt einer Raute zu einem gleichschenkligen Dreieck über die Punktspiegelung am Seitenmittelpunkt bestimmen: 1 GK / 0 LK
    - Ebene Figur: Zwei Ecken eines gleichschenkligen Dreiecks mit gleichem Abstand zu einem Mittelpunkt angeben: 1 GK / 0 LK
    - Körper: Kantenlänge eines Würfels aus gegenüberliegenden Oktaederecken nachweisen: 0 GK / 1 LK
    - Körper: Kantenlänge eines Würfels mit einer Ecke auf einer Pyramidenkante berechnen und Lage im Inneren begründen: 1 GK / 0 LK
    - Körper: Koordinaten der Eckpunkte eines beschriebenen Körpers wählen: 0 GK / 1 LK
    - Körper: Koordinaten eines Eckpunkts eines Prismas angeben: 1 GK / 0 LK
    - Körper: Netz einer Pyramide vervollständigen: 1 GK / 0 LK
    - Punkt: Begegnungspunkt zweier gleichzeitig startender Bewegungen auf einer Strecke aus den Geschwindigkeiten berechnen: 1 GK / 0 LK
    - Punkt: Bildpunkt einer Drehung um eine Kante in eine Koordinatenebene über Lotfußpunkt und Abstand berechnen: 1 GK / 0 LK
    - Punkt: Koordinaten eines Punktes auf einer Strecke in Abhängigkeit von seiner Höhe ermitteln: 0 GK / 1 LK
    - Punkt: Lösungsweg für den Bildpunkt einer Drehung um eine Kante über Lotfußpunkt und Abstand beschreiben: 0 GK / 1 LK
    - Punkt: Mittelpunkt einer Kante nachweisen und symmetrischen Schnittpunkt angeben: 1 GK / 0 LK
    - Punkt: Zweiten Punkt auf einer Geraden mit gleichem Abstand zu einem Geradenpunkt über den Richtungsvektor angeben: 1 GK / 0 LK
  - iqb: 40 Zeilen GK / 19 Zeilen LK, 50 Haupttypen
    - Ebene Figur: Trapez über parallele Seiten nachweisen und Flächeninhalt berechnen: 2 GK / 2 LK
    - Körper: Koordinaten eines Eckpunkts eines Prismas angeben: 2 GK / 1 LK
    - Ebene Figur: Parallelogramm als Rechteck über das Skalarprodukt nachweisen: 1 GK / 1 LK
    - Ebene Figur: Parallelogramm über gleiche Verbindungsvektoren nachweisen: 0 GK / 2 LK
    - Ebene Figur: Rechtwinkliges gleichschenkliges Dreieck aus den Koordinaten begründen und Flächeninhalt angeben: 1 GK / 1 LK
    - Körper: Eckenzahl der Schnittvielecke einer Ebenenschar mit einem Körper und Sonderfälle angeben: 2 GK / 0 LK
    - Ebene Figur: Ansatz für einen rechten Innenwinkel eines Vierecks über das Skalarprodukt mit unbekannter Koordinate erläutern: 1 GK / 0 LK
    - Ebene Figur: Benachbarte Ecke eines Quadrats über den Diagonalenschnittpunkt als Spurpunkt nachweisen: 0 GK / 1 LK
    - Ebene Figur: Berührpunkt des Inkreises einer Raute über Lage auf der Seite und Orthogonalität zum Mittelpunkt begründen: 1 GK / 0 LK
    - Ebene Figur: Drachenviereck über zwei Paare gleich langer Seiten nachweisen: 1 GK / 0 LK
    - Ebene Figur: Dreieck in ein Schrägbild einzeichnen: 1 GK / 0 LK
    - Ebene Figur: Eckpunkt auf einer Achse aus dem Umfang eines Dreiecks bestimmen: 0 GK / 1 LK
    - Ebene Figur: Eckpunkt eines Quadrats in einer Ebene aus zwei benachbarten Ecken berechnen: 1 GK / 0 LK
    - Ebene Figur: Eckpunkt eines flächen- und umfangsgleichen Dreiecks über eine Parallelverschiebung angeben: 0 GK / 1 LK
    - Ebene Figur: Eckpunkte einer Raute mit einer Seite auf einer Geraden bestimmen: 0 GK / 1 LK
    - Ebene Figur: Gleichschenkligkeit eines Dreiecks mit Parameter über die Schenkellängen nachweisen: 1 GK / 0 LK
    - Ebene Figur: Gleichschenkligkeit über Seitenlängen nachweisen und Parallelität einer Kante zur Grundfläche begründen: 1 GK / 0 LK
    - Ebene Figur: Gleichschenkligkeit über kongruente rechtwinklige Dreiecke begründen: 0 GK / 1 LK
    - Ebene Figur: Größeren Teil einer Wand über die Lage der Diagonalen begründen: 1 GK / 0 LK
    - Ebene Figur: Lage dreier Punkte auf einem Kreis über den Thaleskreis begründen: 1 GK / 0 LK
    - Ebene Figur: Lage eines Dreiecks parallel zu einer Koordinatenebene und symmetrisch zu einer anderen begründen: 1 GK / 0 LK
    - Ebene Figur: Parallelität zweier Seiten und rechten Winkel eines Vierecks über Vektoren nachweisen: 1 GK / 0 LK
    - Ebene Figur: Parallelogramm über gleiche Verbindungsvektoren nachweisen und Rechteck über das Skalarprodukt ausschließen: 1 GK / 0 LK
    - Ebene Figur: Projektion eines Parallelogramms in eine Koordinatenebene einzeichnen: 0 GK / 1 LK
    - Ebene Figur: Raute über gleiche Seitenvektoren nachweisen und Quadrat über das Skalarprodukt ausschließen: 1 GK / 0 LK
    - Ebene Figur: Raute über vier gleich lange Seiten nachweisen: 1 GK / 0 LK
    - Ebene Figur: Rechteck mit Parameter nachweisen und Seitenlänge in Abhängigkeit vom Parameter berechnen: 1 GK / 0 LK
    - Ebene Figur: Symmetrisches Achteck in der Koordinatenebene vervollständigen: 1 GK / 0 LK
    - Ebene Figur: Trapez mit zwei gleich langen Seiten über Kollinearität und Seitenlängen nachweisen: 1 GK / 0 LK
    - Ebene Figur: Viereck in ein Schrägbild einzeichnen: 1 GK / 0 LK
    - Körper: Anteil der Bodenfläche unter einer Mindesthöhe über den Strahlensatz am Dachquerschnitt berechnen: 1 GK / 0 LK
    - Körper: Eckpunkt mit vorgegebenen Vorzeichen nach einer Verschiebung angeben: 1 GK / 0 LK
    - Körper: Gesamtlänge der Dachkanten einer Pyramide mit Zuschlag berechnen: 1 GK / 0 LK
    - Körper: Geschwindigkeit entlang einer Kante aus Kantenlänge und Zeit berechnen: 1 GK / 0 LK
    - Körper: Kantenlänge eines Würfels aus gegenüberliegenden Oktaederecken nachweisen: 0 GK / 1 LK
    - Körper: Koordinaten der Eckpunkte eines beschriebenen Körpers wählen: 1 GK / 0 LK
    - Körper: Körper in ein räumliches Koordinatensystem einzeichnen: 1 GK / 0 LK
    - Körper: Lage des Höhenfußpunkts einer Pyramide über die Projektion in die Grundflächenebene entscheiden: 1 GK / 0 LK
    - Körper: Länge eines Streckenzugs aus Kanten und Diagonalen eines Quaders im Sachzusammenhang berechnen: 0 GK / 1 LK
    - Körper: Parallelität der Grundfläche einer Pyramide zu einer Koordinatenebene begründen und Höhe angeben: 1 GK / 0 LK
    - Körper: Punkt auf dem Rand der Grundfläche eines Zylinders nachweisen: 0 GK / 1 LK
    - Punkt: Bildpunkte einer Drehung um eine Koordinatenachse mit vorgegebener Koordinate angeben: 0 GK / 1 LK
    - Punkt: Koordinaten eines Punktes auf einer Strecke in Abhängigkeit von seiner Höhe ermitteln: 0 GK / 1 LK
    - Punkt: Lage eines bewegten Punktes gegenüber einer Mauer über Zeitpunkt und Höhe untersuchen: 0 GK / 1 LK
    - Punkt: Lage zweier Punkte zu einer Koordinatenebene begründen: 1 GK / 0 LK
    - Punkt: Länge einer Strecke aus einer Vektorbeziehung der Ortsvektoren berechnen: 1 GK / 0 LK
    - Punkt: Mittelpunkt des Kreises durch drei Punkte der Ebene über Mittelsenkrechte und Abstandsgleichung berechnen: 1 GK / 0 LK
    - Punkt: Mittelpunkt einer Kante nachweisen und symmetrischen Schnittpunkt angeben: 1 GK / 0 LK
    - Punkt: Teilpunkte einer Strecke in drei gleiche Abschnitte berechnen: 1 GK / 0 LK
    - Punkt: Ursprüngliche Länge einer Strecke aus der Streckenlänge und einer prozentualen Verlängerung berechnen: 1 GK / 0 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 58 GK / 25 LK)

### rekonstruktion-von-bestaenden
- Geltung je Zielprüfung:
  - Thema „Rekonstruktion von Beständen“ (`themen.csv`):
    - be-gk: ja – `| Rekonstruktion von Beständen | ja |` [abi-be-gk-geltung.md Zeile 31]
    - be-lk: ja – `| Rekonstruktion von Beständen | ja |` [abi-be-lk-geltung.md Zeile 31]
    - bb-gk: ja – `| Rekonstruktion von Beständen | ja |` [abi-bb-gk-geltung.md Zeile 31]
    - bb-ea: ja – `| Rekonstruktion von Beständen | ja |` [abi-bb-ea-geltung.md Zeile 31]
- Lerneinheiten:
  - 1. Bestand aus Rate
    - Eintrag, Zeile 11: „(Q2 GK-Kern L2 „Bestände aus Änderungsraten und Anfangsbestand berechnen“)“
    - GOST Berlin [Zeile 1089]: „Bestände aus Änderungsraten und Anfangsbestand berechnen,“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1050–1051]: „Bestände aus Änderungsraten und Anfangsbestand berechnen,“
      Q2, Grund- und Leistungskursfach
  - 2. Rate und Bestand als Paar
    - Eintrag, Zeile 12: „(Q2 GK-Kern L4 „das bestimmte Integral deuten, insbesondere als (re-)“
    - GOST Berlin [Zeile 1190]: „das bestimmte Integral deuten, insbesondere als (re-) konstruierten Bestand,“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1067–1068]: „das bestimmte Integral deuten, insbesondere als (re-)konstruierten Be-“
      Q2, Grund- und Leistungskursfach
  - 3. Am Ratengraphen
    - Eintrag, Zeile 13: „(Q2 GK-Kern L4; Bildarbeit des Pools)“
    - GOST Berlin [Zeile 1190]: „das bestimmte Integral deuten, insbesondere als (re-) konstruierten Bestand,“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1067–1068]: „(Re-)konstruktion eines Bestandes aus Änderungsraten in Anwendungs-situatio-“
      Q2, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 1 Zeilen GK / 7 Zeilen LK, 7 Haupttypen
    - Integral einer Rate berechnen und als Gesamtmenge im Sachzusammenhang deuten: 0 GK / 2 LK
    - Funktion als Bestandsfunktion über Ableitung und Anfangswert begründen und Endwert bestätigen: 0 GK / 1 LK
    - Integral der Differenz zweier Änderungsraten berechnen und als Bestandsdifferenz deuten: 1 GK / 0 LK
    - Term für einen Bestand aus einer Rate über ein Integral angeben: 0 GK / 1 LK
    - Zeitpunkt des größten Bestands aus dem Vorzeichenwechsel der Rate begründen: 0 GK / 1 LK
    - Zeitpunkt gleichen Bestands am Ratengraphen über gleich große Flächen markieren und begründen: 0 GK / 1 LK
    - Zunahme eines Bestands als Differenz der Bestandsfunktion und mittlere Änderungsrate im Zeitraum berechnen: 0 GK / 1 LK
  - iqb: 8 Zeilen GK / 11 Zeilen LK, 16 Haupttypen
    - Integral einer Rate berechnen und als Gesamtmenge im Sachzusammenhang deuten: 0 GK / 2 LK
    - Term für einen Bestand aus einer Rate über ein Integral angeben: 0 GK / 2 LK
    - Zeitpunkt des größten Bestands aus dem Vorzeichenwechsel der Rate begründen: 1 GK / 1 LK
    - Anfangsbestand aus Endbestand und Fläche unter dem Ableitungsgraphen ermitteln: 1 GK / 0 LK
    - Bestand nach einem Zeitraum aus Anfangsbestand und Integral der Änderungsrate berechnen: 1 GK / 0 LK
    - Bestandsänderung grafisch als Fläche unter dem Ratengraphen bestimmen: 1 GK / 0 LK
    - Funktion als Bestandsfunktion über Ableitung und Anfangswert begründen und Endwert bestätigen: 0 GK / 1 LK
    - Gleichheit der Flächen unter Eingangs- und Ausgangsrate als gleiche Gesamtzahl im Sachzusammenhang erläutern: 0 GK / 1 LK
    - Gleichung für den Zeitpunkt eines Bestandswerts über ein Integral der Rate angeben: 1 GK / 0 LK
    - Integralfunktion einer Rate und ihren Grenzwert als Bestand und Endwert im Sachzusammenhang deuten: 0 GK / 1 LK
    - Nullstelle eines Differenzintegrals als Zeitpunkt gleicher Strecke deuten und ihre Lage begründen: 1 GK / 0 LK
    - Zeitpunkt gleichen Bestands am Ratengraphen über gleich große Flächen markieren und begründen: 0 GK / 1 LK
    - Zunahme eines Bestands als Differenz der Bestandsfunktion und mittlere Änderungsrate im Zeitraum berechnen: 0 GK / 1 LK
    - Zunahme eines Bestands aus dem Vorzeichen der Rate begründen: 1 GK / 0 LK
    - Zurückgelegte Strecke als Integral der Geschwindigkeit mit Umrechnung der Einheiten berechnen: 0 GK / 1 LK
    - Zurückgelegte Strecke aus dem Integral der Geschwindigkeit und einer Phase konstanter Geschwindigkeit berechnen: 1 GK / 0 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 9 GK / 18 LK)

### rekonstruktion-von-funktionsgleichungen
- Geltung je Zielprüfung:
  - Thema „Rekonstruktion von Funktionsgleichungen“ (`themen.csv`):
    - be-gk: ja – `| Rekonstruktion von Funktionsgleichungen | ja |` [abi-be-gk-geltung.md Zeile 26]
    - be-lk: ja – `| Rekonstruktion von Funktionsgleichungen | ja |` [abi-be-lk-geltung.md Zeile 26]
    - bb-gk: ja – `| Rekonstruktion von Funktionsgleichungen | ja |` [abi-bb-gk-geltung.md Zeile 26]
    - bb-ea: ja – `| Rekonstruktion von Funktionsgleichungen | ja |` [abi-bb-ea-geltung.md Zeile 26]
- Lerneinheiten:
  - 1. Ansatz und Punktbedingungen
    - Eintrag, Zeile 11: „(GK-Kern „Rekonstruktion von Funktionsgleichungen“; FOS Pflichtthema 1 und 2; OHiMi 2.2 „aus graphischen Darstellungen“)“
    - GOST Berlin [Zeilen 1167–1168]: „hänge nutzen (z. B. in Fragestellungen zu Sachsituationen, die auf Rekonstruktion von Funktionsgleichungen, Extremalprobleme etc. führen),“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 923]: „Rekonstruktion von Funktionsgleichungen“
      Q1, Grund- und Leistungskursfach
  - 2. Bedingungen mit Ableitung
    - Eintrag, Zeile 12: „(GK-Kern; FOS „Symmetrie, Anstieg, Extrem-, Wende- und Sattelstellen“; OHiMi 2.2 „aus Funktionseigenschaften“)“
    - GOST Berlin [Zeilen 1167–1168]: „hänge nutzen (z. B. in Fragestellungen zu Sachsituationen, die auf Rekonstruktion von Funktionsgleichungen, Extremalprobleme etc. führen),“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 923]: „Rekonstruktion von Funktionsgleichungen“
      Q1, Grund- und Leistungskursfach
  - 3. Sonderansätze und Modellkritik
    - Eintrag, Zeile 13: „(LK-Funktionsklassen sin/cos und ln als Ansätze; GK-Kern sin/cos-Parameter als Beschreibungsmittel)“
    - GOST Berlin [Zeilen 1167–1168]: „hänge nutzen (z. B. in Fragestellungen zu Sachsituationen, die auf Rekonstruktion von Funktionsgleichungen, Extremalprobleme etc. führen),“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 923–924]: „Funktionen zur Beschreibung und Untersuchung quantifizierbarer Zusam-“
      Q1, Grund- und Leistungskursfach
    - Ermessen: Modellkritik (Gültigkeitsbereich, Grenzen des Ansatzes) nennt kein Plan eigens.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 7 Zeilen GK / 8 Zeilen LK, 11 Haupttypen
    - Ganzrationale Funktion dritten Grades aus Wert- und Steigungsbedingungen rekonstruieren: 2 GK / 1 LK
    - Funktionsgleichung aus knickfreiem Übergang und einer Wertbedingung rekonstruieren: 2 GK / 0 LK
    - Quadratische Funktion aus Wert- und Steigungsbedingungen rekonstruieren: 2 GK / 0 LK
    - Funktionsgleichung aus der Ableitung und einer Tangente über die Integrationskonstante rekonstruieren: 0 GK / 1 LK
    - Ganzrationale Funktion aus Symmetrie und Randbedingungen rekonstruieren: 0 GK / 1 LK
    - Lineare Funktion durch zwei Punkte nachweisen: 1 GK / 0 LK
    - Maximum eines Parabelmodells aus einem Zeitraum ohne Durchschnittswachstum und einer Differenzbedingung ermitteln: 0 GK / 1 LK
    - Parabel ohne lineares Glied aus dem knickfreien Übergang begründen und Parameter aus einem Flächeninhalt berechnen: 0 GK / 1 LK
    - Parameter einer Exponentialfunktion aus der Änderungsrate zum Anfangszeitpunkt bestimmen: 0 GK / 1 LK
    - Parameter einer Linearkombination aus Funktion und Gerade aus zwei Punkten bestimmen: 0 GK / 1 LK
    - Unmöglichkeit einer einzigen Parabel für ein knickfreies Profil mit zwei waagerechten Tangenten begründen: 0 GK / 1 LK
  - iqb: 3 Zeilen GK / 7 Zeilen LK, 10 Haupttypen
    - Ganzrationale Funktion dritten Grades aus drei Nullstellen und einem Punkt rekonstruieren: 0 GK / 1 LK
    - Parameter einer Exponentialfunktion aus zwei Punkten des Graphen bestimmen: 1 GK / 0 LK
    - Parameter einer Linearkombination aus Funktion und Gerade aus zwei Punkten bestimmen: 0 GK / 1 LK
    - Parameter einer Logarithmusfunktion aus Asymptote und Punkt ermitteln: 0 GK / 1 LK
    - Parameter einer Sinusfunktion aus Extremstelle und Funktionswert bestimmen: 1 GK / 0 LK
    - Parameter einer Sinusfunktion aus zwei aufeinanderfolgenden Extrempunkten bestimmen: 0 GK / 1 LK
    - Quadratische Funktion aus Wert- und Steigungsbedingungen rekonstruieren: 1 GK / 0 LK
    - Quadratische Funktion aus senkrechtem Schnitt mit einer Geraden und einer Extrempunktbedingung ermitteln: 0 GK / 1 LK
    - Sinusfunktion mit gleichen Nullstellen und gleichem Flächeninhalt wie ein Graph bestimmen: 0 GK / 1 LK
    - Steigung einer aus Periode und Extrempunkt rekonstruierten Kosinusfunktion allgemein bestimmen: 0 GK / 1 LK
  - fhr: 10 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 10 GK / 15 LK)

### rotationsvolumen
- Geltung je Zielprüfung:
  - Thema „Rotationsvolumen“ (`themen.csv`):
    - be-gk: nein – `| Rotationsvolumen | nein |` [abi-be-gk-geltung.md Zeile 33]
    - be-lk: ja – `| Rotationsvolumen | ja |` [abi-be-lk-geltung.md Zeile 33]
    - bb-gk: nein – `| Rotationsvolumen | nein |` [abi-bb-gk-geltung.md Zeile 33]
    - bb-ea: ja – `| Rotationsvolumen | ja |` [abi-bb-ea-geltung.md Zeile 33]
- Lerneinheiten:
  - 1. Die Volumenformel
    - Eintrag, Zeile 11: „(FOS „Rotationsvolumen“ als Pflichtform mit linearen und quadratischen Funktionen; GOST LK „auch zusammengesetzte Rotationskörper“)“
    - GOST Berlin [Zeilen 1110–1111]: „das Volumen von Körpern bestimmen, die durch Rotation um die Abszissenachse entstehen.“
      Messen [L2], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1331–1332]: „das Volumen von Körpern bestimmen, die durch Rotation um die Abszissen-“
      Q4, Zusätzlich im Leistungskursfach
  - 2. Um den Körper herum
    - Eintrag, Zeile 12: „(GOST LK; Poolpraxis)“
    - GOST Berlin [Zeilen 1110–1111]: „das Volumen von Körpern bestimmen, die durch Rotation um die Abszissenachse entstehen.“
      Messen [L2], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeile 1336]: „zusammengesetzte Rotationskörper“
      Q4, Zusätzlich im Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 0 Zeilen GK / 4 Zeilen LK, 3 Haupttypen
    - Umbeschriebenes Prisma zu einem Rotationskörper bestimmen: 0 GK / 2 LK
    - Fehlerhaftes Verfahren zur Volumenberechnung beurteilen und berichtigen: 0 GK / 1 LK
    - Integralfunktion im Sachzusammenhang deuten: 0 GK / 1 LK
  - iqb: 0 Zeilen GK / 5 Zeilen LK, 5 Haupttypen
    - Aufgabenstellung zu einem Rotationsvolumen-Anteil aus dem Lösungsweg formulieren: 0 GK / 1 LK
    - Gleichung für die Füllhöhe aus einem Rotationsvolumen zwischen variablen Grenzen aufstellen: 0 GK / 1 LK
    - Integranden als Querschnittsfläche über den Satz des Pythagoras deuten und Umrechnungsfaktor erläutern: 0 GK / 1 LK
    - Rotationsvolumen über einbeschriebene Zylinder abschätzen: 0 GK / 1 LK
    - Wasservolumen als Differenz aus Rotationsvolumen und Kugelvolumen nach unten abschätzen: 0 GK / 1 LK
  - fhr: 4 Zeilen, keine Kursart (Fachoberschule)
- Spanne: nur LK – keine Zeile und keine Einheit im Grundkurs (Einheiten: nur LK-Block; Typenzeilen: 0 GK / 9 LK)

### scharen-von-geraden-und-ebenen
- Geltung je Zielprüfung:
  - Thema „Scharen von Geraden und Ebenen“ (`themen.csv`):
    - be-gk: nein – `| Scharen von Geraden und Ebenen | nein |` [abi-be-gk-geltung.md Zeile 45]
    - be-lk: ja – `| Scharen von Geraden und Ebenen | ja |` [abi-be-lk-geltung.md Zeile 45]
    - bb-gk: nein – `| Scharen von Geraden und Ebenen | nein |` [abi-bb-gk-geltung.md Zeile 45]
    - bb-ea: ja – `| Scharen von Geraden und Ebenen | ja |` [abi-bb-ea-geltung.md Zeile 45]
- Lerneinheiten:
  - 1. Die Schar als Familie
    - Eintrag, Zeile 11: „(Q3 LK „Scharen“)“
    - GOST Berlin [Zeilen 1148–1149]: „die Lagebeziehungen von Punkten, Geraden und Ebenen (auch Scharen) untersuchen.“
      Raum und Form [L3], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1300–1301]: „die Lagebeziehungen von Geraden und Ebenen untersuchen.“
      Q3, Zusätzlich im Leistungskursfach
  - 2. Parameter aus Lagebedingungen
    - Eintrag, Zeile 12: „(Q3 LK; Paarregeln aus orthogonalitaet.md mit Parameter)“
    - GOST Berlin [Zeilen 1148–1149]: „die Lagebeziehungen von Punkten, Geraden und Ebenen (auch Scharen) untersuchen.“
      Raum und Form [L3], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1301–1302]: „Geraden und Ebenen auch unter Verwendung von Parametern in den Koordinaten“
      Q3, Zusätzlich im Leistungskursfach
    - Ermessen: Das Wort „(Scharen)“ steht in Brandenburg als eigene Zeile 1303 am Ende derselben Inhaltszeile.
  - 3. Parameter aus Maßbedingungen
    - Eintrag, Zeile 13: „(Q3 LK; Formeln aus skalarprodukt-und-winkel.md und abstaende.md)“
    - GOST Berlin [Zeilen 1148–1149]: „die Lagebeziehungen von Punkten, Geraden und Ebenen (auch Scharen) untersuchen.“
      Raum und Form [L3], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1300–1301]: „die Lagebeziehungen von Geraden und Ebenen untersuchen.“
      Q3, Zusätzlich im Leistungskursfach
    - Ermessen: Maßbedingungen an Scharen (Abstand, Winkel, Volumen mit Parameter) nennt kein Plan eigens.
  - 4. Scharen am Körper
    - Eintrag, Zeile 14: „(Q3 LK; Körperarbeit in Teil B)“
    - GOST Berlin [Zeilen 1148–1149]: „die Lagebeziehungen von Punkten, Geraden und Ebenen (auch Scharen) untersuchen.“
      Raum und Form [L3], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1300–1301]: „die Lagebeziehungen von Geraden und Ebenen untersuchen.“
      Q3, Zusätzlich im Leistungskursfach
    - Ermessen: Scharen am Körper nennt kein Plan eigens.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 0 Zeilen GK / 22 Zeilen LK, 21 Haupttypen
    - Zugehörigkeit einer Ebene zu einer Schar prüfen: 0 GK / 2 LK
    - Anzahl der Eckpunkte der Schnittfigur einer Ebenenschar mit einem Quader nach Parameterbereichen angeben: 0 GK / 1 LK
    - Ganzzahligen Scharparameter aus einer Bereichsbedingung an den Durchstoßpunkt bestimmen: 0 GK / 1 LK
    - Gemeinsamen Punkt aller Ebenen einer Schar nachweisen: 0 GK / 1 LK
    - Geradenschar der Schnittgeraden einer Ebenenschar mit einer Koordinatenebene bestimmen: 0 GK / 1 LK
    - Identität aller Geraden einer Schar beurteilen: 0 GK / 1 LK
    - Kleinsten Parameterwert, ab dem eine Ebenenschar einen Körper nicht mehr trifft, begründen: 0 GK / 1 LK
    - Koordinatenebene senkrecht zu allen Ebenen einer Schar angeben: 0 GK / 1 LK
    - Lotfußpunkte vom Ursprung auf Spurgeraden von Scharebenen einzeichnen: 0 GK / 1 LK
    - Nichtparallelität verschiedener Ebenen einer Schar über die Normalenvektoren nachweisen: 0 GK / 1 LK
    - Parameter einer Geradenschar aus einem vorgegebenen Durchstoßpunkt bestimmen: 0 GK / 1 LK
    - Punkte einer Geraden, für die eine Ebene durch eine Achse vier vorgegebene Kanten eines Körpers schneidet, ermitteln: 0 GK / 1 LK
    - Scharebene für einen Parameterwert angeben und Schnittfigur mit der Pyramide einzeichnen: 0 GK / 1 LK
    - Scharparameter für Parallelität von Ebene und Gerade ermitteln: 0 GK / 1 LK
    - Scharparameter für den minimalen Flächeninhalt eines Schnittdreiecks über die Orthogonalität zur Kante ermitteln: 0 GK / 1 LK
    - Scharparameter für einen vorgegebenen Abstand eines Punktes zur Scharebene bestimmen: 0 GK / 1 LK
    - Scharparameter für einen vorgegebenen Schnittwinkel zwischen Achse und Ebene ermitteln: 0 GK / 1 LK
    - Scharparameter, für den eine Kante in der Scharebene liegt, nachweisen: 0 GK / 1 LK
    - Schnittwinkel einer Geraden mit allen Ebenen einer Schar als parameterunabhängig nachweisen: 0 GK / 1 LK
    - Weiteren Eckpunkt des Schnittdreiecks einer Scharebene mit einem Körper ermitteln: 0 GK / 1 LK
    - Windschiefe Lage einer Geraden zu einer Geradenschar nachweisen: 0 GK / 1 LK
  - iqb: 2 Zeilen GK / 25 Zeilen LK, 24 Haupttypen
    - Anzahl der Eckpunkte der Schnittfigur einer Ebenenschar mit einem Quader nach Parameterbereichen angeben: 1 GK / 2 LK
    - Scharparameter für einen vorgegebenen Winkel zwischen Ebene und Scharebene berechnen: 0 GK / 2 LK
    - Existenz eines Scharparameters für eine Gerade in der Ebene untersuchen: 0 GK / 1 LK
    - Gemeinsame Gerade aller Ebenen einer Schar aus der Abbildung begründen: 0 GK / 1 LK
    - Gemeinsamen Punkt aller Ebenen einer Schar nachweisen: 0 GK / 1 LK
    - Identität aller Geraden einer Schar beurteilen: 0 GK / 1 LK
    - Koordinatenebene senkrecht zu allen Ebenen einer Schar angeben: 0 GK / 1 LK
    - Koordinatengleichung einer Ebene aufstellen und Parameter eines Scharpunkts in der Ebene bestimmen: 0 GK / 1 LK
    - Lotfußpunkte vom Ursprung auf Spurgeraden von Scharebenen einzeichnen: 0 GK / 1 LK
    - Mögliche Lage des Achsendreiecks einer Ebenenschar über die Vorzeichen der Achsenabschnitte entscheiden und den Parameterbereich bestimmen: 0 GK / 1 LK
    - Nachbarschaft zweier Quadratecken auf einer Geradenschar durch Fallunterscheidung ausschließen: 0 GK / 1 LK
    - Nichtparallelität verschiedener Ebenen einer Schar über die Normalenvektoren nachweisen: 0 GK / 1 LK
    - Ortsvektor und Richtungsvektor der Geraden durch die Punkte einer Punktschar nachweisen: 0 GK / 1 LK
    - Parallelität aller Geraden einer Schar begründen: 0 GK / 1 LK
    - Parameterbereich, in dem eine Ebenenschar dieselben Kanten eines Körpers schneidet, bestimmen: 0 GK / 1 LK
    - Scharebene für einen Parameterwert angeben und Schnittfigur mit der Pyramide einzeichnen: 0 GK / 1 LK
    - Scharparameter für Orthogonalität von Gerade und Ebene bestimmen: 0 GK / 1 LK
    - Scharparameter für Parallelität von Ebene und Gerade ermitteln: 0 GK / 1 LK
    - Scharparameter für den minimalen Flächeninhalt eines Schnittdreiecks über die Orthogonalität zur Kante ermitteln: 0 GK / 1 LK
    - Scharparameter für einen vorgegebenen Schnittwinkel zwischen Achse und Ebene ermitteln: 0 GK / 1 LK
    - Schnittwinkel einer Geraden mit allen Ebenen einer Schar als parameterunabhängig nachweisen: 0 GK / 1 LK
    - Spurpunkt einer Scharebene auf einer Koordinatenachse nachweisen: 1 GK / 0 LK
    - Windschiefe Lage einer Geraden zu einer Geradenschar nachweisen: 0 GK / 1 LK
    - Zugehörigkeit einer Ebene zu einer Schar prüfen: 0 GK / 1 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur LK-Block; Typenzeilen: 2 GK / 47 LK)
- Befund: Der Eintrag führt das Thema als „nur be-lk und bb-ea“; die Geltungstabellen bestätigen das (be-gk nein, bb-gk nein, be-lk ja, bb-ea ja). Der IQB-Pool trägt dennoch zwei Zeilen auf grundlegendem Niveau: `2018MgrundlegendBAGLAA2WTR1-1e` („Spurpunkt einer Scharebene auf einer Koordinatenachse nachweisen“) und `2018MgrundlegendBAGLAA2WTR1-1f` („Anzahl der Eckpunkte der Schnittfigur einer Ebenenschar mit einem Quader nach Parameterbereichen angeben“), beide im Stapel 2018-iqb-ga. Nach der Regel aus Schritt 3d („ja, wenn der Eintrag Einheiten oder Typen beider Kursarten hat“) ergibt das „ja“, nicht „nur LK“.

### schnittmengen
- Geltung je Zielprüfung:
  - Thema „Schnittmengen“ (`themen.csv`):
    - be-gk: ja – `| Schnittmengen | ja |` [abi-be-gk-geltung.md Zeile 40]
    - be-lk: ja – `| Schnittmengen | ja |` [abi-be-lk-geltung.md Zeile 40]
    - bb-gk: ja – `| Schnittmengen | ja |` [abi-bb-gk-geltung.md Zeile 40]
    - bb-ea: ja – `| Schnittmengen | ja |` [abi-bb-ea-geltung.md Zeile 40]
- Lerneinheiten:
  - 1. Schnittpunkt von Gerade und Ebene
    - Eintrag, Zeile 11: „(Q3, GK-Kern „Schnittmenge: … einer Geraden und einer Ebene“; IQB-VER 3.2 zu den vorausgesetzten Fällen)“
    - GOST Berlin [Zeilen 1142–1143]: „Geraden und Ebenen (durch Parameter-, Koordinaten- und Normalenform) analytisch beschreiben und Lagebeziehungen untersuchen (vgl. L2).“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1289]: „einer Geraden und einer Ebene“
      Q3, Grund- und Leistungskursfach
  - 2. Schnittpunkt zweier Geraden
    - Eintrag, Zeile 12: „(Q3, GK-Kern „Schnittmenge: zweier Geraden“; L1 „Bestimmung von Schnittmengen“)“
    - GOST Berlin [Zeilen 1142–1143]: „Geraden und Ebenen (durch Parameter-, Koordinaten- und Normalenform) analytisch beschreiben und Lagebeziehungen untersuchen (vgl. L2).“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1288]: „zweier Geraden“
      Q3, Grund- und Leistungskursfach
  - 3. Spuren, Schnittgeraden und Schnittfiguren
    - Eintrag, Zeile 13: „(Q3, GK-Kern „Darstellung …“; LK „Schnittmenge zweier Ebenen“)“
    - GOST Berlin [Zeilen 1142–1143]: „Geraden und Ebenen (durch Parameter-, Koordinaten- und Normalenform) analytisch beschreiben und Lagebeziehungen untersuchen (vgl. L2).“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1304]: „Schnittmenge zweier Ebenen“
      Q3, Zusätzlich im Leistungskursfach
    - Ermessen: Länderunterschied: die Schnittgerade zweier Ebenen steht in Brandenburg im LK-Zusatz; Berlin trennt hier nicht und führt Lagebeziehungen im Grund- und Leistungskursfach.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 9 Zeilen GK / 5 Zeilen LK, 12 Haupttypen
    - Schnittpunkt von Gerade und Ebene berechnen: 1 GK / 2 LK
    - Durchstoßpunkt einer achsenparallelen Geraden mit einer Ebene berechnen und Abstand im Sachzusammenhang angeben: 1 GK / 0 LK
    - Gegebene Rechnung zum Geradenschnittpunkt erläutern: 0 GK / 1 LK
    - Halbierung eines Quadrats durch gegebene Ebenen entscheiden und begründen: 1 GK / 0 LK
    - Lage zweier Ebenen über die Normalenvektoren entscheiden und Schnittgerade berechnen: 1 GK / 0 LK
    - Parameter aus dem Schnitt zweier Geraden ermitteln: 1 GK / 0 LK
    - Schnittfigur einer Ebene mit einem Würfel einzeichnen: 0 GK / 1 LK
    - Schnittpunkt einer parameterabhängigen Geraden mit einer Kante und Teilverhältnis bestimmen: 1 GK / 0 LK
    - Spitze einer Pyramide als Schnittpunkt einer Kantengeraden mit einer Koordinatenachse berechnen: 0 GK / 1 LK
    - Spurgerade einer Ebene in einer Koordinatenebene in das Schrägbild einzeichnen: 1 GK / 0 LK
    - Spurpunkte einer Ebene auf den Koordinatenachsen bestimmen: 1 GK / 0 LK
    - Zeit bis zum Erreichen einer Ebene aus dem Geradenparameter bestimmen: 1 GK / 0 LK
  - iqb: 8 Zeilen GK / 9 Zeilen LK, 11 Haupttypen
    - Schnittpunkt von Gerade und Ebene berechnen: 0 GK / 3 LK
    - Koordinate eines Punktes aus der Schnittfigur zeichnerisch ermitteln und Vorgehen beschreiben: 1 GK / 1 LK
    - Parameter aus dem Schnitt zweier Geraden ermitteln: 2 GK / 0 LK
    - Schattenpunkt bei paralleler Projektion bestimmen: 2 GK / 0 LK
    - Spurgerade einer Ebene in einer Koordinatenebene in das Schrägbild einzeichnen: 1 GK / 1 LK
    - Endpunkt der Schnittstrecke eines Vierecks mit einer achsenparallelen Ebene bestimmen: 0 GK / 1 LK
    - Höhe des Endpunkts einer Strecke auf einer senkrechten Geraden über den Schnitt mit einer Kante berechnen: 0 GK / 1 LK
    - Rechenweg für den Schnittpunkt einer Geraden mit einer Ebene durch drei Punkte beschreiben: 0 GK / 1 LK
    - Schnittfigur einer Ebene mit einem Würfel einzeichnen: 0 GK / 1 LK
    - Schnittpunkt einer parameterabhängigen Geraden mit einer Kante und Teilverhältnis bestimmen: 1 GK / 0 LK
    - Spitze einer Pyramide als Schnittpunkt einer Kantengeraden mit einer Koordinatenachse berechnen: 1 GK / 0 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: GK-Block und LK-Block; Typenzeilen: 17 GK / 14 LK)

### skalarprodukt-und-winkel
- Geltung je Zielprüfung:
  - Thema „Skalarprodukt und Winkel“ (`themen.csv`):
    - be-gk: ja – `| Skalarprodukt und Winkel | ja |` [abi-be-gk-geltung.md Zeile 41]
    - be-lk: ja – `| Skalarprodukt und Winkel | ja |` [abi-be-lk-geltung.md Zeile 41]
    - bb-gk: ja – `| Skalarprodukt und Winkel | ja |` [abi-bb-gk-geltung.md Zeile 41]
    - bb-ea: ja – `| Skalarprodukt und Winkel | ja |` [abi-bb-ea-geltung.md Zeile 41]
- Lerneinheiten:
  - 1. Das Skalarprodukt als Objekt
    - Eintrag, Zeile 11: „(Q3, GK-Kern „das Skalarprodukt geometrisch deuten“; OHiMi 2.3 „Skalarprodukt in Koordinatenform und koordinatenfreier Form“)“
    - GOST Berlin [Zeile 1141]: „das Skalarprodukt geometrisch deuten,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1260]: „das Skalarprodukt geometrisch deuten,“
      Q3, Grund- und Leistungskursfach
  - 2. Winkel zwischen Vektoren, Kanten und Geraden
    - Eintrag, Zeile 12: „(Q3, GK-Kern L2 „Winkel zwischen Geraden“, L3 „Winkel zwischen zwei Vektoren“; OHiMi 2.3 „Ansätze zur Winkelberechnung“)“
    - GOST Berlin [Zeilen 1096–1097]: „Streckenlängen und Winkelgrößen im Raum (auch mithilfe des Skalarprodukts) bestimmen,“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1262]: „Winkel zwischen zwei Vektoren“
      Q3, Grund- und Leistungskursfach
  - 3. Neigungswinkel von Ebenen
    - Eintrag, Zeile 13: „(Q3, GK-Kern L2 „Winkel zwischen … Ebenen und Ebenen“; OHiMi 2.3 „Ansätze zur Winkelberechnung“)“
    - GOST Berlin [Zeilen 1096–1097]: „Streckenlängen und Winkelgrößen im Raum (auch mithilfe des Skalarprodukts) bestimmen,“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1216–1217]: „Winkel zwischen Geraden, Geraden und Ebenen, Ebenen und Ebenen“
      Q3, Grund- und Leistungskursfach
  - 4. Winkel von Geraden gegen Ebenen und Bogenmaße
    - Eintrag, Zeile 14: „(Q3, GK-Kern L2 „Winkel zwischen Geraden … und Ebenen“; OHiMi 2.3 „Ansätze zur Winkelberechnung“)“
    - GOST Berlin [Zeilen 1096–1097]: „Streckenlängen und Winkelgrößen im Raum (auch mithilfe des Skalarprodukts) bestimmen,“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1216–1217]: „Winkel zwischen Geraden, Geraden und Ebenen, Ebenen und Ebenen“
      Q3, Grund- und Leistungskursfach
    - Ermessen: Das Bogenmaß nennt kein Plan der Qualifikationsphase.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 8 Zeilen GK / 6 Zeilen LK, 5 Haupttypen
    - Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen: 5 GK / 3 LK
    - Winkel zwischen zwei Kanten über das Skalarprodukt berechnen: 1 GK / 2 LK
    - Innenwinkel eines Vierecks über das Skalarprodukt der Seitenvektoren berechnen: 1 GK / 0 LK
    - Rechten Winkel zwischen zwei Seiten einer Figur über das Skalarprodukt nachweisen: 1 GK / 0 LK
    - Schnittwinkel zwischen Gerade und Ebene über Richtungs- und Normalenvektor berechnen: 0 GK / 1 LK
  - iqb: 15 Zeilen GK / 13 Zeilen LK, 17 Haupttypen
    - Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen: 4 GK / 5 LK
    - Winkel zwischen zwei Kanten über das Skalarprodukt berechnen: 2 GK / 1 LK
    - Schnittwinkel zwischen Gerade und Ebene über Richtungs- und Normalenvektor berechnen: 2 GK / 0 LK
    - Abhängigkeit eines Skalarprodukts nur von der Seitenlänge allgemein begründen: 1 GK / 0 LK
    - Art des Ergebnisses von Ausdrücken mit Skalarprodukt ankreuzen: 0 GK / 1 LK
    - Aussagen über Winkel zwischen Vektoren mit fester Komponentensumme beurteilen: 1 GK / 0 LK
    - Innenwinkel eines Dreiecks über gleiche Seitenlängen als gleichseitig bestimmen: 0 GK / 1 LK
    - Innenwinkel eines Vierecks über das Skalarprodukt der Seitenvektoren berechnen: 1 GK / 0 LK
    - Innenwinkel zwischen Dachebene und vertikaler Wand über den Neigungswinkel berechnen: 1 GK / 0 LK
    - Länge eines Kreisbogens durch drei Punkte über den Winkel am Mittelpunkt berechnen: 0 GK / 1 LK
    - Neigung einer Ebene in Prozent über den Winkel zur Koordinatenebene prüfen: 1 GK / 0 LK
    - Neigungswinkel einer Strecke gegen die Horizontale über ihre Projektion berechnen: 0 GK / 1 LK
    - Parameter für einen Winkel von mindestens 90° über das Skalarprodukt ermitteln: 0 GK / 1 LK
    - Rechten Winkel zwischen zwei Seiten einer Figur über das Skalarprodukt nachweisen: 0 GK / 1 LK
    - Schnittwinkel zweier Geraden über das Skalarprodukt berechnen: 1 GK / 0 LK
    - Winkel zwischen einer Seitenfläche und der Horizontalen als Grenzwinkel im Sachzusammenhang bestimmen: 1 GK / 0 LK
    - Winkelart aus dem Vorzeichen des Skalarprodukts beurteilen: 0 GK / 1 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 23 GK / 19 LK)

### spiegelung
- Geltung je Zielprüfung:
  - Thema „Spiegelung“ (`themen.csv`):
    - be-gk: ja – `| Spiegelung | ja |` [abi-be-gk-geltung.md Zeile 46]
    - be-lk: ja – `| Spiegelung | ja |` [abi-be-lk-geltung.md Zeile 46]
    - bb-gk: ja – `| Spiegelung | ja |` [abi-bb-gk-geltung.md Zeile 46]
    - bb-ea: ja – `| Spiegelung | ja |` [abi-bb-ea-geltung.md Zeile 46]
- Lerneinheiten:
  - 1. Punkte spiegeln
    - Eintrag, Zeile 11: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1139–1140]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometrischen Objekten anwenden,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1255–1256]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometri-“
      Q3, Grund- und Leistungskursfach
    - Ermessen: Spiegelungen nennt weder der Berliner noch der Brandenburger Plan; zugeordnet ist in beiden Ländern die Zeile zum Arbeiten mit Vektoren an geometrischen Objekten.
  - 2. Spiegelebene und Spiegelgerade bestimmen
    - Eintrag, Zeile 12: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1139–1140]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometrischen Objekten anwenden,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1255–1256]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometri-“
      Q3, Grund- und Leistungskursfach
    - Ermessen: wie Einheit 1: keine eigene Stelle.
  - 3. Symmetrieebenen von Körpern
    - Eintrag, Zeile 13: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1139–1140]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometrischen Objekten anwenden,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1255–1256]: „Beschreibung geometrischer Objekte mittels Vektoren“
      Q3, Grund- und Leistungskursfach
    - Ermessen: wie Einheit 1: keine eigene Stelle.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 4 Zeilen GK / 3 Zeilen LK, 6 Haupttypen
    - Symmetrieebene eines Körpers unter vorgegebenen Gleichungen auswählen und eine ausschließen: 1 GK / 1 LK
    - Spiegelebene aus Punkt und Spiegelpunkt bestimmen: 1 GK / 0 LK
    - Spiegelebene zweier sich schneidender Geraden bestimmen: 0 GK / 1 LK
    - Spiegelpunkt an einem Punkt bestimmen: 1 GK / 0 LK
    - Spiegelpunkt an einer Ebene über den bekannten Lotfußpunkt bestimmen: 1 GK / 0 LK
    - Spiegelpunkt an einer Ebene über die Lotgerade bestimmen: 0 GK / 1 LK
  - iqb: 7 Zeilen GK / 13 Zeilen LK, 15 Haupttypen
    - Symmetrieebene eines Körpers unter vorgegebenen Gleichungen auswählen und eine ausschließen: 2 GK / 1 LK
    - Symmetrieebenen eines Körpers aus den Koordinaten begründen: 0 GK / 3 LK
    - Spiegelebene aus Punkt und Spiegelpunkt bestimmen: 1 GK / 1 LK
    - Koordinaten gespiegelter Eckpunkte aus den Symmetrieebenen eines Körpers angeben: 0 GK / 1 LK
    - Punkt auf der Spiegelachse mit vorgegebenem Abstandsverhältnis zur Spiegelebene bestimmen: 0 GK / 1 LK
    - Spiegelebene zweier sich schneidender Geraden bestimmen: 0 GK / 1 LK
    - Spiegelgerade einer Geraden an einer Ebene aus Fixpunkt und bekanntem Spiegelpunkt angeben: 0 GK / 1 LK
    - Spiegelgerade zweier Geraden zeichnen und Punkt der Winkelhalbierenden als Vektorterm angeben: 0 GK / 1 LK
    - Spiegelpunkt an einem Punkt bestimmen: 1 GK / 0 LK
    - Spiegelpunkt an einer Ebene über den bekannten Lotfußpunkt bestimmen: 1 GK / 0 LK
    - Spiegelpunkt an einer Ebene über die Lotgerade bestimmen: 0 GK / 1 LK
    - Symmetrie zweier Punkte bezüglich einer Koordinatenachse über die Koordinaten begründen: 0 GK / 1 LK
    - Symmetrieebene eines Körpers angeben und ihre Schnittfigur mit dem Körper einzeichnen: 1 GK / 0 LK
    - Symmetrieebene eines geraden Prismas über die Symmetrieachse der Grundfläche begründen: 1 GK / 0 LK
    - Symmetrieebene eines zusammengesetzten Körpers über verschiedene Höhen der Teilkörper ausschließen: 0 GK / 1 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 11 GK / 16 LK)

### stammfunktion-und-hauptsatz
- Geltung je Zielprüfung:
  - Thema „Stammfunktion und Hauptsatz“ (`themen.csv`):
    - be-gk: ja – `| Stammfunktion und Hauptsatz | ja |` [abi-be-gk-geltung.md Zeile 28]
    - be-lk: ja – `| Stammfunktion und Hauptsatz | ja |` [abi-be-lk-geltung.md Zeile 28]
    - bb-gk: ja – `| Stammfunktion und Hauptsatz | ja |` [abi-bb-gk-geltung.md Zeile 28]
    - bb-ea: ja – `| Stammfunktion und Hauptsatz | ja |` [abi-bb-ea-geltung.md Zeile 28]
- Lerneinheiten:
  - 1. Stammfunktion
    - Eintrag, Zeile 11: „(Q2 GK-Kern „Integrieren als Umkehrung des Differenzierens“; OHiMi „Stammfunktionen elementarer Funktionen“)“
    - GOST Berlin [Zeilen 1193–1194]: „Integrale von Funktionen (Potenzfunktionen f mit f(x) = xn, n ∈ ZZ , n ≠ −1, ganzrationalen und Exponentialfunktionen) mittels Stammfunktionen bestimmen,“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1085–1086]: „Integrale von Funktionen mittels Stammfunktionen bilden,“
      Q2, Grund- und Leistungskursfach
  - 2. Hauptsatz
    - Eintrag, Zeile 12: „(Q2 GK-Kern „Hauptsatz der Differential- und Integralrechnung“, „Integrale von Funktionen mittels Stammfunktionen bilden“; OHiMi „bestimmtes …“
    - GOST Berlin [Zeilen 1191–1192]: „geometrisch anschaulich den Hauptsatz als Beziehung zwischen Ableiten und Integrieren begründen,“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1070–1071]: „geometrisch anschaulich den Hauptsatz als Beziehung zwischen Ableiten“
      Q2, Grund- und Leistungskursfach
  - 3. Der Graphenblick
    - Eintrag, Zeile 13: „(Q2 GK-Kern „Zusammenhang zwischen den Funktionsgraphen der Funktion, der Ableitungsfunktion und der Stammfunktion“)“
    - GOST Berlin [Zeilen 1191–1192]: „geometrisch anschaulich den Hauptsatz als Beziehung zwischen Ableiten und Integrieren begründen,“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1072–1073]: „Zusammenhang zwischen den Funk-tionsgraphen der Funktion, der Ableitungs-“
      Q2, Grund- und Leistungskursfach
  - 4. Integralfunktion
    - Eintrag, Zeile 14: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeile 1190]: „das bestimmte Integral deuten, insbesondere als (re-) konstruierten Bestand,“
      Funktionaler Zusammenhang [L4], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1067–1068]: „das bestimmte Integral deuten, insbesondere als (re-)konstruierten Be-“
      Q2, Grund- und Leistungskursfach
    - Ermessen: Die Integralfunktion als Funktion der oberen Grenze nennt kein Plan eigens.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 13 Zeilen GK / 8 Zeilen LK, 15 Haupttypen
    - Stammfunktion durch Ableiten nachweisen: 4 GK / 1 LK
    - Aussage über Extrempunkte einer Stammfunktion beurteilen: 1 GK / 1 LK
    - Extremstelle aller Stammfunktionen über den Vorzeichenwechsel der gegebenen Ableitung begründen: 1 GK / 1 LK
    - Aussage über den Krümmungswechsel der Stammfunktionen über das Vorzeichen von f am Graphen beurteilen: 1 GK / 0 LK
    - Bestimmtes Integral einer ganzrationalen Funktion berechnen: 1 GK / 0 LK
    - Bestimmtes Integral mit vorgegebener Stammfunktion berechnen: 1 GK / 0 LK
    - Faktor für einen Stammfunktionsterm der Form r/x · f(x) bestimmen: 0 GK / 1 LK
    - Funktion aus einer gegebenen Stammfunktion durch Ableiten bestimmen: 1 GK / 0 LK
    - Funktionswert von f als Tangentensteigung am Graphen der Stammfunktion bestimmen: 0 GK / 1 LK
    - Graph einer Stammfunktion durch einen Punkt skizzieren: 1 GK / 0 LK
    - Integral der Ableitung als Differenz von Funktionswerten berechnen: 0 GK / 1 LK
    - Integral über f aus dem Graphen der Stammfunktion bestimmen: 0 GK / 1 LK
    - Integrationsgrenzen mit Integral null über die zweite Ableitung am Graphen der Ableitung angeben: 0 GK / 1 LK
    - Stammfunktion aus einer vorgegebenen Integralgleichung ermitteln: 1 GK / 0 LK
    - Stammfunktionen mit vorgegebenem vertikalem Abstand zum Graphen einer Stammfunktion angeben: 1 GK / 0 LK
  - iqb: 15 Zeilen GK / 16 Zeilen LK, 21 Haupttypen
    - Bestimmtes Integral einer ganzrationalen Funktion berechnen: 3 GK / 0 LK
    - Bestimmtes Integral mit vorgegebener Stammfunktion berechnen: 1 GK / 2 LK
    - Stammfunktion durch Ableiten nachweisen: 1 GK / 2 LK
    - Stammfunktion mit einer Wertebedingung bestimmen: 2 GK / 1 LK
    - Graph einer Stammfunktion durch einen Punkt skizzieren: 1 GK / 1 LK
    - Integral über f aus dem Graphen der Stammfunktion bestimmen: 1 GK / 1 LK
    - Anzahl der Nullstellen einer Integralfunktion am Graphen beurteilen: 0 GK / 1 LK
    - Aussage über Extrempunkte einer Stammfunktion beurteilen: 1 GK / 0 LK
    - Bestimmtes Integral einer trigonometrischen Funktion über eine Periode berechnen: 1 GK / 0 LK
    - Funktionswert von f als Tangentensteigung am Graphen der Stammfunktion bestimmen: 0 GK / 1 LK
    - Ganzzahlige Nullstellen einer Integralfunktion über gleiche Grenzen und Symmetrie begründen: 0 GK / 1 LK
    - Höchstens eine positive Nullstelle jeder Stammfunktion über die Monotonie aus dem Vorzeichen des Integranden begründen: 0 GK / 1 LK
    - Höchstzahl der Nullstellen einer Integralfunktion über den Grad begründen: 0 GK / 1 LK
    - Maximum einer Integralfunktion über die Nullstelle des Integranden begründen und im Sachzusammenhang deuten: 0 GK / 1 LK
    - Maximumstelle aller Stammfunktionen über den Vorzeichenwechsel des Integranden begründen: 1 GK / 0 LK
    - Prozentuale Abweichung eines Näherungswerts vom exakten Wert berechnen: 1 GK / 0 LK
    - Stammfunktion eines Polynomterms nach dem Ausmultiplizieren angeben: 0 GK / 1 LK
    - Stammfunktionen mit der x-Achse als Tangente über die Nullstellen der Funktion ermitteln: 1 GK / 0 LK
    - Tiefpunkt aller Stammfunktionen auf der y-Achse über den Vorzeichenwechsel von f begründen und Stammfunktion mit Tiefpunkt im Ursprung bestimmen: 1 GK / 0 LK
    - Weitere Nullstelle einer Integralfunktion über die Flächenbilanz am Graphen begründen: 0 GK / 1 LK
    - Wendestelle einer Integralfunktion über die Ableitung des Integranden begründen und Funktionswert berechnen: 0 GK / 1 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 28 GK / 24 LK)

### tangente-normale-schnittwinkel
- Geltung je Zielprüfung:
  - Thema „Tangente, Normale, Schnittwinkel“ (`themen.csv`):
    - be-gk: ja – `| Tangente, Normale, Schnittwinkel | ja |` [abi-be-gk-geltung.md Zeile 22]
    - be-lk: ja – `| Tangente, Normale, Schnittwinkel | ja |` [abi-be-lk-geltung.md Zeile 22]
    - bb-gk: ja – `| Tangente, Normale, Schnittwinkel | ja |` [abi-bb-gk-geltung.md Zeile 22]
    - bb-ea: ja – `| Tangente, Normale, Schnittwinkel | ja |` [abi-bb-ea-geltung.md Zeile 22]
- Lerneinheiten:
  - 1. Tangentengleichung im Punkt
    - Eintrag, Zeile 11: „(Q1, GK-Kern „Gleichung der Tangente in einem Punkt des Funktionsgraphen“; FOS „Tangentenanstieg“, „Bestimmung einer Tangentengleichung“; …“
    - GOST Berlin [Zeile 1087]: „Sekanten- und Tangentensteigungen zu Funktionsgraphen bestimmen,“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 903–904]: „Gleichung der Tangente in einem Punkt des Funktionsgraphen unter Verwendung“
      Q1, Grund- und Leistungskursfach
  - 2. Tangente als Berührung
    - Eintrag, Zeile 12: „(Q1, GK-Kern; FOS „Bestimmung einer Tangentengleichung“ nur als Grundform; OHiMi 2.2 „Gleichungen von Sekanten, Tangenten und Normalen“)“
    - GOST Berlin [Zeile 1087]: „Sekanten- und Tangentensteigungen zu Funktionsgraphen bestimmen,“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 901–902]: „Sekanten- und Tangentensteigungen an Funktionsgraphen bestimmen,“
      Q1, Grund- und Leistungskursfach
  - 3. Normale
    - Eintrag, Zeile 13: „(Q1, GK-Kern „Tangenten- und Normalengleichungen“; FOS „Bestimmung … einer Normalengleichung“; OHiMi 2.2 „Gleichungen von Sekanten, Tangenten …“
    - GOST Berlin [Zeile 1087]: „Sekanten- und Tangentensteigungen zu Funktionsgraphen bestimmen,“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 939]: „Tangenten- und Normalengleichungen“
      Q1, Grund- und Leistungskursfach
    - Ermessen: Länderunterschied: die Normale nennt nur Brandenburg („Tangenten- und Normalengleichungen“); Berlin führt nur Tangentensteigungen.
  - 4. Steigungswinkel und Schnittwinkel
    - Eintrag, Zeile 14: „(Q1, GK-Kern „Schnittwinkel zwischen Funktionsgraphen“ – im Plan, nicht in der Anlage; kein FOS-Stoff)“
    - GOST Berlin [Zeile 1087]: „Sekanten- und Tangentensteigungen zu Funktionsgraphen bestimmen,“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 906]: „Schnittwinkel zwischen Funktionsgraphen“
      Q1, Grund- und Leistungskursfach
    - Ermessen: Länderunterschied: den Schnittwinkel nennt nur Brandenburg.
  - 5. Dreiecke und Figuren aus Tangente, Normale und Achsen
    - Eintrag, Zeile 15: „(Q1, GK-Kern; Sek-I-Geometrie als Werkzeug; fhr nur die Dreiecksfläche an einer Geraden)“
    - GOST Berlin [Zeile 1087]: „Sekanten- und Tangentensteigungen zu Funktionsgraphen bestimmen,“
      Messen [L2], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 939]: „Tangenten- und Normalengleichungen“
      Q1, Grund- und Leistungskursfach
    - Ermessen: Figuren aus Tangente, Normale und Achsen nennt kein Plan eigens.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 30 Zeilen GK / 21 Zeilen LK, 44 Haupttypen
    - Tangentengleichung in einem Punkt des Graphen aufstellen: 4 GK / 1 LK
    - Flächeninhalt oder Umfang des Dreiecks aus Tangente und Koordinatenachsen berechnen: 1 GK / 1 LK
    - Gerade als Tangente in einem vorgegebenen Punkt über Funktionswert und Ableitung nachweisen: 2 GK / 0 LK
    - Schnittwinkel zweier Graphen im gemeinsamen Punkt über die Tangentensteigungen berechnen: 2 GK / 0 LK
    - Aussage über den größten y-Achsenabschnitt der Tangenten eines Graphen beurteilen: 0 GK / 1 LK
    - Bereich der Stellen mit Mindeststeigungswinkel der Tangente über eine quadratische Ungleichung ermitteln: 1 GK / 0 LK
    - Berührpunkt der Tangente mit gleichschenkligem Achsendreieck über die Steigung −1 berechnen: 0 GK / 1 LK
    - Berührpunkt der Tangente mit vorgegebener Steigung berechnen: 1 GK / 0 LK
    - Dreiecke aus Wendetangente, Normale und Koordinatenachsen einzeichnen und ihre Ähnlichkeit begründen: 1 GK / 0 LK
    - Flächeninhalt des Dreiecks aus Tangente, Gerade und x-Achse berechnen: 0 GK / 1 LK
    - Flächeninhalt des von Tangente, Normale und y-Achse begrenzten Dreiecks berechnen: 1 GK / 0 LK
    - Flächeninhalt eines Rechtecks aus Nullstellen und Normale als parameterunabhängig nachweisen: 0 GK / 1 LK
    - Gemeinsame Tangente zweier Graphen im Schnittpunkt nachweisen und angeben: 1 GK / 0 LK
    - Gleichschenkligkeit des Dreiecks aus Tangente und Koordinatenachsen allgemein begründen: 0 GK / 1 LK
    - Gleichung als Tangentenbedingung geometrisch deuten: 1 GK / 0 LK
    - Lösungsweg für eine gemeinsame Normale zweier Kurven erläutern: 1 GK / 0 LK
    - Mittelpunkt eines den Graphen berührenden Kreises über die Normale im Berührpunkt bestimmen: 0 GK / 1 LK
    - Näherungsweise tangentiale Einmündung einer Geraden nachweisen: 0 GK / 1 LK
    - Parallele Tangente über die Ableitung finden und skizzieren: 1 GK / 0 LK
    - Parameter aus dem senkrechten Schnitt zweier Graphen bestimmen: 0 GK / 1 LK
    - Rechenschritte zur Winkelbestimmung aus Höhen- und Horizontalabstand beurteilen und berichtigen: 1 GK / 0 LK
    - Rechenweg zur Tangente von einem Punkt an den Graphen erläutern und Aufgabenstellung formulieren: 0 GK / 1 LK
    - Scharparameter für ein gleichseitiges Dreieck aus den Tangenten an Graph und Spiegelgraph und der y-Achse bestimmen: 0 GK / 1 LK
    - Scharparameter für einen vorgegebenen Schnittwinkel des Graphen mit der y-Achse bestimmen: 0 GK / 1 LK
    - Schnittwinkel zwischen Tangente und Gerade über die Anstiege berechnen: 1 GK / 0 LK
    - Schranke für den Anstieg der Tangenten einer Schar begründen: 0 GK / 1 LK
    - Steigungswinkel einer Tangente berechnen und Aussage über den Schnittwinkel mit einer Geraden prüfen: 1 GK / 0 LK
    - Steigungswinkel und y-Achsenabschnitt der Wendetangente berechnen: 1 GK / 0 LK
    - Stelle mit parallelen Tangenten an Graph und Ableitungsgraph über f' = f'' ermitteln: 1 GK / 0 LK
    - Stellen mit vorgegebenem Tangentenanstieg nachweisen: 0 GK / 1 LK
    - Stellen mit waagerechter Tangente aus der faktorisierten Ableitung angeben: 0 GK / 1 LK
    - Tangente am gespiegelten Punkt über die Achsensymmetrie angeben: 1 GK / 0 LK
    - Tangente aufstellen und weiteren gemeinsamen Punkt mit dem Graphen berechnen: 1 GK / 0 LK
    - Tangente mit gegebener Gleichung in die Abbildung einzeichnen: 0 GK / 1 LK
    - Tangentenabschnitt auf der x-Achse als Quotient f/f' am Graphen begründen: 0 GK / 1 LK
    - Tangentengleichung aus der Abbildung ablesen: 0 GK / 1 LK
    - Tangentengleichung im Ursprung aufstellen und Grenze einer Dreiecksfläche aus dem Flächeninhalt berechnen: 1 GK / 0 LK
    - Tangentengleichung und Schnittwinkel der Tangente mit der x-Achse bestimmen: 1 GK / 0 LK
    - Umfang des Achsendreiecks einer Tangente berechnen und Umkreismittelpunkt angeben: 1 GK / 0 LK
    - Umfang des Dreiecks aus zwei Tangenten und der x-Achse berechnen: 1 GK / 0 LK
    - Ursprungsgerade durch einen Graphenpunkt als Winkelhalbierende zwischen x-Achse und Tangente bestimmen: 0 GK / 1 LK
    - Waagerechte Tangente an einer vorgegebenen Stelle nachweisen und Funktionswert berechnen: 1 GK / 0 LK
    - y-Achsenabschnitt der Tangente allgemein nachweisen: 0 GK / 1 LK
    - Öffnungswinkel an der Spitze eines Rotationskörpers über die Tangentensteigung prüfen: 1 GK / 0 LK
  - iqb: 30 Zeilen GK / 31 Zeilen LK, 48 Haupttypen
    - Tangentengleichung in einem Punkt des Graphen aufstellen: 6 GK / 0 LK
    - Abstand eines Punktes von einem Graphen über die Normalenbedingung deuten: 0 GK / 2 LK
    - Berührpunkt der Tangente mit vorgegebener Steigung berechnen: 1 GK / 1 LK
    - Gleichschenkligkeit des Dreiecks aus Tangente und Koordinatenachsen allgemein begründen: 1 GK / 1 LK
    - Mittelpunkt eines den Graphen berührenden Kreises über die Normale im Berührpunkt bestimmen: 1 GK / 1 LK
    - Tangentengleichung aus der Abbildung ablesen: 1 GK / 1 LK
    - Tangentensteigung in einem Punkt über die Ableitung nachweisen: 0 GK / 2 LK
    - Winkel zwischen Graph und senkrechter Kante über die Ableitung berechnen: 0 GK / 2 LK
    - y-Achsenabschnitt der Tangente allgemein nachweisen: 1 GK / 1 LK
    - Abstand des Ursprungs zu einer Geraden über das Lot berechnen: 1 GK / 0 LK
    - Auftreffwinkel einer Flugkurve über die Ableitung an der Nullstelle berechnen: 0 GK / 1 LK
    - Aussage über den Bremsweg bei konstanter Abnahme über die Tangente und ein Dreieck untersuchen: 0 GK / 1 LK
    - Berührpunkt der Tangente mit gleichschenkligem Achsendreieck über die Steigung −1 berechnen: 0 GK / 1 LK
    - Einsehbarkeit eines Kurvenstücks von einem Punkt aus über die Tangente durch diesen Punkt untersuchen: 0 GK / 1 LK
    - Ergebnis eines Lösungswegs als y-Achsenabschnitt der parallelen Tangente deuten: 1 GK / 0 LK
    - Faktorisierung von f(x) − t(x) nachweisen und weiteren Schnittpunkt von Tangente und Graph begründen: 0 GK / 1 LK
    - Fehlen einer gemeinsamen Tangente zweier Graphen über die Vorzeichen der Steigungen begründen: 1 GK / 0 LK
    - Fehlende waagerechte Tangente über Vorzeichen am Graphen begründen: 0 GK / 1 LK
    - Flächeninhalt des Dreiecks aus Tangente, Gerade und x-Achse berechnen: 0 GK / 1 LK
    - Flächeninhalt eines Rechtecks aus Nullstellen und Normale als parameterunabhängig nachweisen: 0 GK / 1 LK
    - Flächeninhalt oder Umfang des Dreiecks aus Tangente und Koordinatenachsen berechnen: 1 GK / 0 LK
    - Gemeinsame Tangente zweier Graphen im Schnittpunkt nachweisen und angeben: 1 GK / 0 LK
    - Gerade senkrecht zu einer gegebenen Tangente durch einen Punkt aufstellen: 0 GK / 1 LK
    - Gleichung als Tangentenbedingung geometrisch deuten: 1 GK / 0 LK
    - Länge der Normalen vom Graphenpunkt bis zur x-Achse berechnen: 0 GK / 1 LK
    - Nullstelle der Tangente an einen gestreckten Graphen als parameterunabhängig nachweisen: 0 GK / 1 LK
    - Näherung durch die Tangente mit dem Funktionswert im Sachzusammenhang vergleichen: 0 GK / 1 LK
    - Parallele Tangente über die Ableitung finden und skizzieren: 1 GK / 0 LK
    - Parameter aus dem senkrechten Schnitt zweier Graphen bestimmen: 0 GK / 1 LK
    - Parameter einer Logarithmusfunktion aus einer gemeinsamen Tangente mit einer Scharkurve berechnen und Tangentengleichung angeben: 0 GK / 1 LK
    - Relative Abweichung zwischen Tangente und Funktion als Ungleichung im Sachzusammenhang deuten: 1 GK / 0 LK
    - Schnittpunkt zweier Tangenten nachweisen und Tangenten einzeichnen: 1 GK / 0 LK
    - Schnittwinkel eines Graphen mit einer waagerechten Geraden über die Ableitung berechnen: 1 GK / 0 LK
    - Steigungen der Geraden durch den Wendepunkt mit genau einem gemeinsamen Punkt über die Wendetangente eingrenzen: 1 GK / 0 LK
    - Steigungswinkel des Graphen in einem Punkt über die Ableitung berechnen: 1 GK / 0 LK
    - Steigungswinkel und Nebenwinkel am Übergang zweier Profilstücke einzeichnen und im Sachzusammenhang deuten: 0 GK / 1 LK
    - Tangente am gespiegelten Punkt über die Achsensymmetrie angeben: 1 GK / 0 LK
    - Tangente durch einen entfernten Punkt über die Rationalität der Steigung ausschließen: 0 GK / 1 LK
    - Tangente durch einen vorgegebenen Punkt am Graphen einzeichnen und ihre Gleichung ablesen: 1 GK / 0 LK
    - Tangente im Ursprung als Gerade durch zwei Punkte nachweisen: 0 GK / 1 LK
    - Tangente mit gegebener Gleichung in die Abbildung einzeichnen: 0 GK / 1 LK
    - Tangente mit vorgegebener Steigung außerhalb eines Punktes angeben: 0 GK / 1 LK
    - Tangenten durch einen Punkt der y-Achse an den Graphen skizzieren: 1 GK / 0 LK
    - Tangentenabschnitt auf der x-Achse als Quotient f/f' am Graphen begründen: 0 GK / 1 LK
    - Tangentengleichung und Schnittwinkel der Tangente mit der x-Achse bestimmen: 1 GK / 0 LK
    - Umfang des Achsendreiecks einer Tangente berechnen und Umkreismittelpunkt angeben: 1 GK / 0 LK
    - Umfang des Dreiecks aus zwei Tangenten und der x-Achse berechnen: 1 GK / 0 LK
    - Weiteren Schnittpunkt von Tangente und Graph aus einer vorgegebenen Faktorisierung begründen: 1 GK / 0 LK
  - fhr: 15 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 60 GK / 52 LK)

### umkehrfunktion
- Geltung je Zielprüfung:
  - Thema „Umkehrfunktion“ (`themen.csv`):
    - be-gk: ja – `| Umkehrfunktion | ja |` [abi-be-gk-geltung.md Zeile 18]
    - be-lk: ja – `| Umkehrfunktion | ja |` [abi-be-lk-geltung.md Zeile 18]
    - bb-gk: ja – `| Umkehrfunktion | ja |` [abi-bb-gk-geltung.md Zeile 18]
    - bb-ea: ja – `| Umkehrfunktion | ja |` [abi-bb-ea-geltung.md Zeile 18]
- Lerneinheiten:
  - 1. Umkehrbarkeit, Bereiche und Term
    - Eintrag, Zeile 11: „(Eingangsvoraussetzung L4; Q2 LK „ln als Umkehrfunktion der e-Funktion“; OHiMi 2.2 „Zusammenhang zwischen Funktion und Umkehrfunktion“, „Definitionsbereich, …“
    - GOST Berlin [Zeilen 1211 und 1213]: „die ln-Funktion als Stammfunktion von x →     und als Umkehrfunktion der e-Funktion nutzen,“
      Funktionaler Zusammenhang [L4], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1180 und 1182]: „die natürliche Logarithmusfunktion als Stammfunktion von x → x und als Um-“
      Q2, Zusätzlich im Leistungskursfach
    - Ermessen: In beiden Texten ist der Bruch 1/x über mehrere Zeilen gesetzt (Berlin 1210 und 1212, Brandenburg 1181 und 1183); im Zitat bleibt an seiner Stelle eine Lücke.
  - 2. Spiegelung an der Winkelhalbierenden
    - Eintrag, Zeile 12: „(OHiMi 2.2 „Zusammenhang zwischen Funktion und Umkehrfunktion“; Q1 LK-Klassen; Pool erhöht 2025–2026)“
    - GOST Berlin [Zeilen 1211 und 1213]: „die ln-Funktion als Stammfunktion von x →     und als Umkehrfunktion der e-Funktion nutzen,“
      Funktionaler Zusammenhang [L4], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1185–1186]: „natürliche Exponentialfunktion als Umkehrfunktion der natürlichen Logarithmus-“
      Q2, Zusätzlich im Leistungskursfach
    - Ermessen: Die Spiegelung an der Winkelhalbierenden nennt kein Plan der Qualifikationsphase; zugeordnet ist die Umkehrfunktionszeile.
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 0 Zeilen GK / 1 Zeilen LK, 1 Haupttypen
    - Flächenbeziehung zwischen Funktion und Umkehrfunktion über die Spiegelung an y = x beurteilen: 0 GK / 1 LK
  - iqb: 0 Zeilen GK / 5 Zeilen LK, 5 Haupttypen
    - Definitionsbereich der Umkehrfunktion angeben und ihren Term nachweisen: 0 GK / 1 LK
    - Flächenbeziehung zwischen Funktion und Umkehrfunktion über die Spiegelung an y = x beurteilen: 0 GK / 1 LK
    - Flächeninhalt eines Vierecks aus Berührpunkten und Spiegelpunkten als Trapez begründen: 0 GK / 1 LK
    - Tangente an Funktion und Umkehrfunktion über die Spiegelung an y = x begründen: 0 GK / 1 LK
    - Umkehrbarkeit auf einem Intervall begründen und Definitions- und Wertebereich der Umkehrfunktion angeben: 0 GK / 1 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: nur LK – keine Zeile und keine Einheit im Grundkurs (Einheiten: nur LK-Block; Typenzeilen: 0 GK / 6 LK)
- Befund: Die Geltung ist viermal ja, die Stellen in beiden Plänen stehen aber ausschließlich im Leistungskurszusatz; Grundkursstoff ist das Thema nur als Eingangsvoraussetzung (so auch die Verortung des Eintrags).

### unabhaengigkeit
- Geltung je Zielprüfung:
  - Thema „Unabhängigkeit“ (`themen.csv`):
    - be-gk: ja – `| Unabhängigkeit | ja |` [abi-be-gk-geltung.md Zeile 54]
    - be-lk: ja – `| Unabhängigkeit | ja |` [abi-be-lk-geltung.md Zeile 54]
    - bb-gk: ja – `| Unabhängigkeit | ja |` [abi-bb-gk-geltung.md Zeile 54]
    - bb-ea: ja – `| Unabhängigkeit | ja |` [abi-bb-ea-geltung.md Zeile 54]
- Lerneinheiten:
  - 1. Unabhängigkeit prüfen: die Produktregel P(A ∩ B) = P(A) · P(B) an Anteilen oder absoluten Häufigkeiten prüfen (Tafel oder Anzahlen erst beschaffen
    - Eintrag, Zeile 11: „(Q2, GK-Kern; OHiMi 2.4 „stochastische Unabhängigkeit“; FOS Pflichtthema 4)“
    - GOST Berlin [Zeilen 1243–1244]: „Teilvorgänge mehrstufiger Zufallsexperimente auf stochastische Unabhängigkeit anhand einfacher Beispiele untersuchen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1148–1149]: „Teilvorgänge mehrstufiger Zufalls-experimente auf stochastische Unabhän-“
      Q2, Grund- und Leistungskursfach
  - 2. Rückwärts
    - Eintrag, Zeile 12: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1243–1244]: „Teilvorgänge mehrstufiger Zufallsexperimente auf stochastische Unabhängigkeit anhand einfacher Beispiele untersuchen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1149–1150]: „stochastische Abhängigkeit und Unabhängigkeit von Ereignissen“
      Q2, Grund- und Leistungskursfach
  - 3. Unabhängigkeit als Argument: die Ausgleichs-Fehlvorstellung widerlegen
    - Eintrag, Zeile 13: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1243–1244]: „Teilvorgänge mehrstufiger Zufallsexperimente auf stochastische Unabhängigkeit anhand einfacher Beispiele untersuchen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1148–1149]: „Teilvorgänge mehrstufiger Zufalls-experimente auf stochastische Unabhän-“
      Q2, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 4 Zeilen GK / 4 Zeilen LK, 7 Haupttypen
    - Stochastische Unabhängigkeit zweier Ereignisse über die Produktregel untersuchen: 1 GK / 1 LK
    - Anteil für stochastische Unabhängigkeit ohne Rechnung angeben und begründen: 0 GK / 1 LK
    - Aussage über den Ausgleich eines beobachteten Anteils bei weiteren Versuchen über die Unabhängigkeit beurteilen: 1 GK / 0 LK
    - Unabhängigkeit über den Vergleich von bedingter und unbedingter Wahrscheinlichkeit untersuchen und deuten: 1 GK / 0 LK
    - Unabhängigkeit über den Vergleich zweier bedingter Anteile untersuchen: 1 GK / 0 LK
    - Wahrscheinlichkeit eines Ereignisses aus Unabhängigkeit und einer Schnittwahrscheinlichkeit bestimmen: 0 GK / 1 LK
    - Wahrscheinlichkeit eines Fehlers aus der Vereinigung zweier unabhängiger Fehler berechnen: 0 GK / 1 LK
  - iqb: 6 Zeilen GK / 9 Zeilen LK, 8 Haupttypen
    - Stochastische Unabhängigkeit zweier Ereignisse über die Produktregel untersuchen: 1 GK / 4 LK
    - Aussage über den Ausgleich eines beobachteten Anteils bei weiteren Versuchen über die Unabhängigkeit beurteilen: 1 GK / 1 LK
    - Unabhängigkeit über den Vergleich zweier bedingter Anteile untersuchen: 2 GK / 0 LK
    - Wahrscheinlichkeit eines Ereignisses aus Unabhängigkeit und einer Schnittwahrscheinlichkeit bestimmen: 1 GK / 1 LK
    - Anteil für stochastische Unabhängigkeit ohne Rechnung angeben und begründen: 0 GK / 1 LK
    - Gleichung für p aus der Unabhängigkeit zweier Ereignisse im Baumdiagramm aufstellen: 0 GK / 1 LK
    - Parameter für die Unabhängigkeit zweier Ereignisse aus der Vierfeldertafel ermitteln: 0 GK / 1 LK
    - Unabhängigkeit über den Vergleich von bedingter und unbedingter Wahrscheinlichkeit untersuchen und deuten: 1 GK / 0 LK
  - fhr: 4 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 10 GK / 13 LK)

### uneigentliche-integrale
- Geltung je Zielprüfung:
  - Thema „Uneigentliche Integrale“ (`themen.csv`):
    - be-gk: nein – `| Uneigentliche Integrale | nein |` [abi-be-gk-geltung.md Zeile 32]
    - be-lk: ja – `| Uneigentliche Integrale | ja |` [abi-be-lk-geltung.md Zeile 32]
    - bb-gk: nein – `| Uneigentliche Integrale | nein |` [abi-bb-gk-geltung.md Zeile 32]
    - bb-ea: ja – `| Uneigentliche Integrale | ja |` [abi-bb-ea-geltung.md Zeile 32]
- Lerneinheiten:
  - 1. Der Begriff
    - Eintrag, Zeile 11: „(Q2 LK „Inhalte unbegrenzter Flächen mittels uneigentlicher Integrale“)“
    - GOST Berlin [Zeilen 1104–1105]: „Inhalte von Flächen, die durch Funktionsgraphen begrenzt sind, bestimmen (ggf. näherungsweise), auch mithilfe uneigentlicher Integrale und unter“
      Messen [L2], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1174–1175]: „Inhalte unbegrenzter Flächen mittels uneigentlicher Integrale:“
      Q2, Zusätzlich im Leistungskursfach
  - 2. Die Näherungsdeutung
    - Eintrag, Zeile 12: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1104–1105]: „Inhalte von Flächen, die durch Funktionsgraphen begrenzt sind, bestimmen (ggf. näherungsweise), auch mithilfe uneigentlicher Integrale und unter“
      Messen [L2], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1176–1177]: „Integral über einen unbeschränkten Intervall“
      Q2, Zusätzlich im Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 0 Zeilen GK / 1 Zeilen LK, 1 Haupttypen
    - Näherung eines Integrals mit großer oberer Grenze durch ein festes Integral geometrisch deuten: 0 GK / 1 LK
  - iqb: 0 Zeilen GK / 1 Zeilen LK, 1 Haupttypen
    - Näherung eines Integrals mit großer oberer Grenze durch ein festes Integral geometrisch deuten: 0 GK / 1 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: nur LK – keine Zeile und keine Einheit im Grundkurs (Einheiten: nur LK-Block; Typenzeilen: 0 GK / 2 LK)

### vektoren-und-rechenoperationen
- Geltung je Zielprüfung:
  - Thema „Vektoren und Rechenoperationen“ (`themen.csv`):
    - be-gk: ja – `| Vektoren und Rechenoperationen | ja |` [abi-be-gk-geltung.md Zeile 35]
    - be-lk: ja – `| Vektoren und Rechenoperationen | ja |` [abi-be-lk-geltung.md Zeile 35]
    - bb-gk: ja – `| Vektoren und Rechenoperationen | ja |` [abi-bb-gk-geltung.md Zeile 35]
    - bb-ea: ja – `| Vektoren und Rechenoperationen | ja |` [abi-bb-ea-geltung.md Zeile 35]
- Lerneinheiten:
  - 1. Vektorbegriff, Betrag und Kollinearität
    - Eintrag, Zeile 11: „(Q3, GK-Kern „Vektorbegriff (Verschiebung, Pfeilklasse)“
    - GOST Berlin [Zeilen 1137–1138]: „elementare Operationen mit geometrischen Vektoren ausführen und Vektoren auf Kollinearität untersuchen,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1231–1232]: „elementare Operationen mit geometrischen Vektoren ausführen und Vekto-“
      Q3, Grund- und Leistungskursfach
  - 2. Vektorterme am Körper
    - Eintrag, Zeile 12: „(Q3, GK-Kern „Vektoraddition“, „Multiplikation eines Vektors mit einer reellen Zahl“, „Darstellung von Vektoren als Linearkombinationen …“
    - GOST Berlin [Zeilen 1139–1140]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometrischen Objekten anwenden,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1255–1256]: „Vektoren beim Arbeiten mit geradlinig bzw. ebenflächig begrenzten geometri-“
      Q3, Grund- und Leistungskursfach
  - 3. Skalarprodukt im Sachzusammenhang
    - Eintrag, Zeile 13: „(Q3, GK-Kern L1 „Tupel in Form von Punkten und Vektoren angeben“; das Skalarprodukt als Operation aus der L3-Zeile)“
    - GOST Berlin [Zeile 1141]: „das Skalarprodukt geometrisch deuten,“
      Raum und Form [L3], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1260]: „das Skalarprodukt geometrisch deuten,“
      Q3, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 0 Zeilen GK / 1 Zeilen LK, 1 Haupttypen
    - Lage eines Punktes zu einem Vektorterm im Quader beschreiben: 0 GK / 1 LK
  - iqb: 9 Zeilen GK / 10 Zeilen LK, 16 Haupttypen
    - Koordinate eines Vektors aus vorgegebener Länge bestimmen: 1 GK / 1 LK
    - Punkt zu einem Vektorterm in das Schrägbild einzeichnen: 1 GK / 1 LK
    - Verbindungsvektor zweier Kantenmittelpunkte als Linearkombination der Kantenvektoren angeben: 0 GK / 2 LK
    - Blickrichtungsvektoren zu schematischen Ansichten angeben und eine weitere Ansicht zeichnen: 0 GK / 1 LK
    - Fehlende Koordinate eines Punktes aus der Parallelität zweier Kanten bestimmen: 0 GK / 1 LK
    - Lage eines Punktes zu einem Vektorterm im Quader beschreiben: 1 GK / 0 LK
    - Mengen aus einem Mischungsverhältnis und einem vorgegebenen Skalarprodukt berechnen: 1 GK / 0 LK
    - Ortsvektor eines gedrehten Punktes als Term aufstellen: 1 GK / 0 LK
    - Punkt aus einer Linearkombination von Kantenvektoren in das Schrägbild einzeichnen: 1 GK / 0 LK
    - Skalarprodukt zweier Sachvektoren als Gesamtpreis deuten: 1 GK / 0 LK
    - Unterschiedliche Beträge von Vektoren mit fester Komponentensumme über ein Beispiel begründen: 1 GK / 0 LK
    - Vektorterm für einen Eckpunkt eines Pyramidenstumpfs begründen: 0 GK / 1 LK
    - Vektorterm für einen Punkt aus Lotfußpunkt, Abstand und Richtungsvektor angeben: 0 GK / 1 LK
    - Verbindungsvektor zweier Würfelecken mit gleicher Länge wie eine Raumdiagonale und nicht kollinear angeben: 0 GK / 1 LK
    - Verschobenen Punkt über den Diagonalenschnittpunkt bestimmen: 1 GK / 0 LK
    - Vierten Eckpunkt eines Quadrats über eine Vektoraddition bestimmen: 0 GK / 1 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 9 GK / 11 LK)

### vierfeldertafel
- Geltung je Zielprüfung:
  - Thema „Vierfeldertafel“ (`themen.csv`):
    - be-gk: ja – `| Vierfeldertafel | ja |` [abi-be-gk-geltung.md Zeile 52]
    - be-lk: ja – `| Vierfeldertafel | ja |` [abi-be-lk-geltung.md Zeile 52]
    - bb-gk: ja – `| Vierfeldertafel | ja |` [abi-bb-gk-geltung.md Zeile 52]
    - bb-ea: ja – `| Vierfeldertafel | ja |` [abi-bb-ea-geltung.md Zeile 52]
- Lerneinheiten:
  - 1. Die Tafel füllen: Aufbau (zwei Merkmale mit Gegenereignissen, vier Felder, Ränder, Summe eins bzw. Gesamtzahl), Füllregeln (Ränder zuerst, Felder als Differenzen der Ränder), der Kernschritt bei bedingten Angaben („Anteil innerhalb einer Gruppe“ ist bedingt
    - Eintrag, Zeile 11: „(Q2, GK-Kern „Vierfeldertafel“; OHiMi 2.4)“
    - GOST Berlin [Zeilen 1241–1242]: „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln untersuchen und damit Problemstellungen im Kontext bedingter Wahrscheinlichkeiten lösen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1144]: „Vierfeldertafel“
      Q2, Grund- und Leistungskursfach
  - 2. Aus der Tafel rechnen: die Vereinigung „A oder B“ als eins minus Gegenfeld (oder über den Additionssatz), das ausschließende Entweder-oder als Summe der beiden gemischten Felder, fehlende absolute Häufigkeiten durch Subtraktion, Anteile aus Anteilen und bedingten Anteilen kombinieren. (Q2, GK-Kern; OHiMi 2.4 „Additionssatz“) ← Eingabe „a oder b tafel“, „entweder oder“, „vereinigung tafel“
    - Eintrag, Zeile 12: „(Q2, GK-Kern; OHiMi 2.4 „Additionssatz“)“
    - GOST Berlin [Zeilen 1241–1242]: „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln untersuchen und damit Problemstellungen im Kontext bedingter Wahrscheinlichkeiten lösen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1136–1137]: „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln unter-“
      Q2, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 6 Zeilen GK / 2 Zeilen LK, 3 Haupttypen
    - Vierfeldertafel aus Anteilen vervollständigen: 4 GK / 2 LK
    - Fehlende absolute Häufigkeit über die Vierfeldertafel berechnen: 1 GK / 0 LK
    - Wahrscheinlichkeit einer Vereinigung aus der Vierfeldertafel über das Gegenereignis berechnen: 1 GK / 0 LK
  - iqb: 14 Zeilen GK / 7 Zeilen LK, 8 Haupttypen
    - Vierfeldertafel aus Anteilen vervollständigen: 9 GK / 4 LK
    - Aussage über ein Entweder-oder-Ereignis aus der Vierfeldertafel beurteilen: 1 GK / 1 LK
    - Anteil aus Anteilen und bedingten Anteilen über die Vierfeldertafel berechnen: 1 GK / 0 LK
    - Fehlende absolute Häufigkeit über die Vierfeldertafel berechnen: 1 GK / 0 LK
    - Tabelle mit drei Spalten analog zur Vierfeldertafel aus Anteilen vervollständigen: 0 GK / 1 LK
    - Vierfeldertafel mit Parameter vervollständigen und einen Parameterwert ausschließen: 0 GK / 1 LK
    - Vierfeldertafel mit absoluten Häufigkeiten aus Gruppengrößen und bedingten Anteilen vervollständigen: 1 GK / 0 LK
    - Wahrscheinlichkeit einer Vereinigung aus der Vierfeldertafel über das Gegenereignis berechnen: 1 GK / 0 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 20 GK / 9 LK)

### zufallsexperimente-und-pfadregeln
- Geltung je Zielprüfung:
  - Thema „Baumdiagramm und Pfadregeln“ (`themen.csv`):
    - be-gk: ja – `| Baumdiagramm und Pfadregeln | ja |` [abi-be-gk-geltung.md Zeile 51]
    - be-lk: ja – `| Baumdiagramm und Pfadregeln | ja |` [abi-be-lk-geltung.md Zeile 51]
    - bb-gk: ja – `| Baumdiagramm und Pfadregeln | ja |` [abi-bb-gk-geltung.md Zeile 51]
    - bb-ea: ja – `| Baumdiagramm und Pfadregeln | ja |` [abi-bb-ea-geltung.md Zeile 51]
  - Thema „Ereignisse und Mengenoperationen“ (`themen.csv`):
    - be-gk: ja – `| Ereignisse und Mengenoperationen | ja |` [abi-be-gk-geltung.md Zeile 48]
    - be-lk: ja – `| Ereignisse und Mengenoperationen | ja |` [abi-be-lk-geltung.md Zeile 48]
    - bb-gk: ja – `| Ereignisse und Mengenoperationen | ja |` [abi-bb-gk-geltung.md Zeile 48]
    - bb-ea: ja – `| Ereignisse und Mengenoperationen | ja |` [abi-bb-ea-geltung.md Zeile 48]
  - Thema „Zufallsexperimente und Urnenmodelle“ (`themen.csv`):
    - be-gk: ja – `| Zufallsexperimente und Urnenmodelle | ja |` [abi-be-gk-geltung.md Zeile 49]
    - be-lk: ja – `| Zufallsexperimente und Urnenmodelle | ja |` [abi-be-lk-geltung.md Zeile 49]
    - bb-gk: ja – `| Zufallsexperimente und Urnenmodelle | ja |` [abi-bb-gk-geltung.md Zeile 49]
    - bb-ea: ja – `| Zufallsexperimente und Urnenmodelle | ja |` [abi-bb-ea-geltung.md Zeile 49]
- Lerneinheiten:
  - 1. Ereignisse als Mengen
    - Eintrag, Zeile 12: „(Q2, GK-Kern „Grundbegriffe der Mengenlehre“; OHiMi 2.4 Additionssatz; FOS „elementare Begriffe“)“
    - GOST Berlin [Zeilen 1241–1242]: „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln untersuchen und damit Problemstellungen im Kontext bedingter Wahrscheinlichkeiten lösen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1136–1137]: „Grundbegriffe der Mengenlehre: leere Menge“
      Q2, Grund- und Leistungskursfach
  - 2. Laplace-Experimente in der Oberstufe
    - Eintrag, Zeile 13: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1245–1246]: „Anwendungssituationen mithilfe des Urnenmodells (mit und ohne Zurücklegen) untersuchen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1121–1122]: „Anwendungssituationen mithilfe von Urnenmodellen untersuchen,“
      Q2, Grund- und Leistungskursfach
    - Ermessen: Laplace-Experimente nennt kein Plan der Qualifikationsphase eigens; sie sind Eingangsvoraussetzung.
  - 3. Pfadregeln bei unabhängigen Stufen
    - Eintrag, Zeile 14: „(Q2, GK-Kern „zwei- und dreistufige Zufallsexperimente“; OHiMi 2.4 „Baumdiagramm, Pfadregeln“; FOS „mehrstufige Zufallsexperimente“)“
    - GOST Berlin [Zeilen 1241–1242]: „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln untersuchen und damit Problemstellungen im Kontext bedingter Wahrscheinlichkeiten lösen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1143]: „Baumdiagramm und Pfadregeln“
      Q2, Grund- und Leistungskursfach
  - 4. Ziehen ohne Zurücklegen und Umlegen
    - Eintrag, Zeile 15: „(Q2, GK-Kern „Ziehen ohne Zurücklegen“; OHiMi 2.4 Pfadregeln; FOS – die punktreichste fhr-Form)“
    - GOST Berlin [Zeilen 1245–1246]: „Anwendungssituationen mithilfe des Urnenmodells (mit und ohne Zurücklegen) untersuchen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1124–1125]: „Ziehen ohne Zurücklegen (hypergeometrische Verteilung)“
      Q2, Grund- und Leistungskursfach
  - 5. Mammutbäume
    - Eintrag, Zeile 16: „(Q2, GK-Kern „kombinatorische Abzählverfahren“; OHiMi 2.4 Kombinatorik; IQB-VER 4 Ziehen ohne Zurücklegen mit Binomialkoeffizienten)“
    - GOST Berlin [Zeilen 1241–1242]: „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln untersuchen und damit Problemstellungen im Kontext bedingter Wahrscheinlichkeiten lösen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1143]: „Baumdiagramm und Pfadregeln“
      Q2, Grund- und Leistungskursfach
  - 6. Situationsbäume
    - Eintrag, Zeile 17: „(Q2, GK-Kern „Baumdiagramm und Pfadregeln“, „Satz von der totalen Wahrscheinlichkeit“; Vorstufe von Vierfeldertafel und Bayes)“
    - GOST Berlin [Zeilen 1241–1242]: „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln untersuchen und damit Problemstellungen im Kontext bedingter Wahrscheinlichkeiten lösen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeile 1148]: „zwei- und dreistufige Zufallsexperimente“
      Q2, Grund- und Leistungskursfach
  - 7. Term und Ereignis
    - Eintrag, Zeile 18: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1241–1242]: „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln untersuchen und damit Problemstellungen im Kontext bedingter Wahrscheinlichkeiten lösen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1136–1137]: „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln unter-“
      Q2, Grund- und Leistungskursfach
  - 8. Rückwärts
    - Eintrag, Zeile 19: keine Kursartmarke in der Einheitszeile
    - GOST Berlin [Zeilen 1241–1242]: „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln untersuchen und damit Problemstellungen im Kontext bedingter Wahrscheinlichkeiten lösen,“
      Daten und Zufall [L5], Grundkursfach und Leistungskursfach
    - GOST Brandenburg [Zeilen 1136–1137]: „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln unter-“
      Q2, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 49 Zeilen GK / 31 Zeilen LK, 53 Haupttypen
    - Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben: 3 GK / 3 LK
    - Baumdiagramm zu einer zweistufigen Situation erstellen: 1 GK / 3 LK
    - Fehlenden Anteil im Baumdiagramm aus einer Randwahrscheinlichkeit berechnen: 1 GK / 3 LK
    - Term und Ereignis: Fehlende Werte in einem Wahrscheinlichkeitsterm bestimmen: 2 GK / 2 LK
    - Ziehen ohne Zurücklegen: Wahrscheinlichkeit beim zweimaligen Ziehen ohne Zurücklegen berechnen: 4 GK / 0 LK
    - Pfadwahrscheinlichkeit einer vorgegebenen Ergebnisfolge als Produkt berechnen: 1 GK / 2 LK
    - Anteil für genau eines von zwei Ereignissen aus Anteilen und Schnitt berechnen: 2 GK / 0 LK
    - Baumdiagramm mit aus einer Pfadwahrscheinlichkeit erschlossener Einzelwahrscheinlichkeit erstellen: 1 GK / 1 LK
    - Laplace-Experiment: Vergleich zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen: 1 GK / 1 LK
    - Laplace-Experiment: Wahrscheinlichkeit eines Vergleichsereignisses beim Wurf zweier Würfel über die Ergebnistabelle nachweisen: 2 GK / 0 LK
    - Pfadwahrscheinlichkeit für lauter gleiche Ergebnisse als Potenz berechnen: 1 GK / 1 LK
    - Totale Wahrscheinlichkeit über die Pfadregeln nachweisen: 2 GK / 0 LK
    - Verhältnis zweier Pfadwahrscheinlichkeiten im Baumdiagramm prüfen: 1 GK / 1 LK
    - Ziehen ohne Zurücklegen: Wahrscheinlichkeit für höchstens k einer Sorte über Binomialkoeffizienten berechnen: 2 GK / 0 LK
    - Absolute Anzahl aus einer Pfadwahrscheinlichkeit mit einer Schranke vergleichen: 0 GK / 1 LK
    - Anteil aus dem Ergebnis eines Befragungsverfahrens berechnen: 1 GK / 0 LK
    - Anteil aus einem Verhältnis zweier Pfadwahrscheinlichkeiten berechnen: 1 GK / 0 LK
    - Anteil aus einer quadratischen Gleichung für ein zweistufiges Bestehen berechnen: 1 GK / 0 LK
    - Anteil in der Restgruppe über die totale Wahrscheinlichkeit einordnen: 1 GK / 0 LK
    - Anzahlvergleich zweier Teilgruppen über Pfadwahrscheinlichkeiten nachweisen: 0 GK / 1 LK
    - Baumdiagramm eines Befragungsverfahrens mit unbekanntem Anteil vervollständigen: 1 GK / 0 LK
    - Baumdiagramm mit Abbruchbedingung erstellen: 1 GK / 0 LK
    - Behauptung über die größere Wahrscheinlichkeit einer Augensumme bei zwei Würfeln über die Pfade widerlegen: 1 GK / 0 LK
    - Ergebnisse zu einer Mengenoperation zweier Ereignisse angeben: 1 GK / 0 LK
    - Fehlende Wahrscheinlichkeiten im Baumdiagramm über die Pfadregel ermitteln: 1 GK / 0 LK
    - Gewinnwahrscheinlichkeiten in einem Wechselspiel vergleichen: 1 GK / 0 LK
    - Laplace-Experiment: Laplace-Wahrscheinlichkeit als Anteil der günstigen Fälle angeben: 1 GK / 0 LK
    - Laplace-Experiment: Sektorenzahlen eines Glücksrads aus Wahrscheinlichkeiten ermitteln: 0 GK / 1 LK
    - Laplace-Experiment: Wahrscheinlichkeit für drei verschiedene Ergebnisse über Pfadprodukt und Reihenfolgen nachweisen: 1 GK / 0 LK
    - Pfadwahrscheinlichkeit zweier Stufen aus dem Sachtext berechnen: 1 GK / 0 LK
    - Term P(A) + P(B) − 2 · P(A ∩ B) als Wahrscheinlichkeit für genau eines der Ereignisse deuten: 0 GK / 1 LK
    - Term für die Wahrscheinlichkeit eines Produktereignisses bei n Würfen ermitteln: 0 GK / 1 LK
    - Term und Ereignis: Bedingte Wahrscheinlichkeit und Schnittwahrscheinlichkeit im Sachzusammenhang deuten: 1 GK / 0 LK
    - Term und Ereignis: Produkt aus Potenz und Binomialterm als Ereignis mit festem Abschnitt deuten: 0 GK / 1 LK
    - Term und Ereignis: Schnittwahrscheinlichkeit zweier Ereignisse im Sachzusammenhang deuten: 1 GK / 0 LK
    - Wahrscheinlichkeit bei zweistufigem Umlegen zwischen Urnen berechnen: 0 GK / 1 LK
    - Wahrscheinlichkeit einer Summe über alle Ergebnisfolgen mit Reihenfolgen berechnen: 1 GK / 0 LK
    - Wahrscheinlichkeit einer ungeraden Summe über Pfade berechnen: 1 GK / 0 LK
    - Wahrscheinlichkeit einer vorgegebenen Augensumme bei zwei Würfen über Pfade berechnen: 1 GK / 0 LK
    - Wahrscheinlichkeit eines Vergleichs zweier Zufallsgeräte über Pfade berechnen: 0 GK / 1 LK
    - Wahrscheinlichkeit für ein zweistufiges Experiment mit zufälliger Urnenzusammensetzung berechnen: 0 GK / 1 LK
    - Wahrscheinlichkeit für k Treffer unmittelbar hintereinander unter n Versuchen berechnen: 1 GK / 0 LK
    - Wahrscheinlichkeit für mindestens einen von zwei unabhängigen Erfolgen über das Gegenereignis berechnen: 1 GK / 0 LK
    - Wahrscheinlichkeit für mindestens oder höchstens einmal bei mehreren Stufen über das Gegenereignis berechnen: 0 GK / 1 LK
    - Wahrscheinlichkeit für zwei gleichfarbige Kugeln beim Ziehen mit Zurücklegen als Summe zweier Pfade berechnen: 1 GK / 0 LK
    - Ziehen ohne Zurücklegen: Entfernte Kugel aus einer Wahrscheinlichkeit für verschiedene Farben entscheiden: 1 GK / 0 LK
    - Ziehen ohne Zurücklegen: Gleiche Chance verschiedener Ziehungspositionen beim Ziehen ohne Zurücklegen begründen: 1 GK / 0 LK
    - Ziehen ohne Zurücklegen: Kugelzahl für eine begrenzte Anzahl von Farbreihenfolgen beim Ziehen ohne Zurücklegen begründen: 0 GK / 1 LK
    - Ziehen ohne Zurücklegen: Kugelzahlen aus zwei Astwahrscheinlichkeiten eines unvollständigen Baumdiagramms ermitteln: 0 GK / 1 LK
    - Ziehen ohne Zurücklegen: Mindestanzahl beim Ziehen ohne Zurücklegen über das Gegenereignis bestimmen: 0 GK / 1 LK
    - Ziehen ohne Zurücklegen: Wahrscheinlichkeit für ausschließlich eine Sorte beim mehrfachen Ziehen als Produkt berechnen: 1 GK / 0 LK
    - Ziehen ohne Zurücklegen: Wahrscheinlichkeit für eine Mehrheit einer Sorte beim dreimaligen Ziehen ohne Zurücklegen berechnen: 1 GK / 0 LK
    - Ziehen ohne Zurücklegen: Wahrscheinlichkeit für genau drei aufeinanderfolgende gleichfarbige Kugeln beim Ziehen ohne Zurücklegen berechnen: 0 GK / 1 LK
  - iqb: 82 Zeilen GK / 47 Zeilen LK, 72 Haupttypen
    - Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben: 9 GK / 6 LK
    - Baumdiagramm zu einer zweistufigen Situation erstellen: 4 GK / 3 LK
    - Ziehen ohne Zurücklegen: Wahrscheinlichkeit beim zweimaligen Ziehen ohne Zurücklegen berechnen: 5 GK / 0 LK
    - Laplace-Experiment: Vergleich zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen: 1 GK / 3 LK
    - Pfadwahrscheinlichkeit einer vorgegebenen Ergebnisfolge als Produkt berechnen: 2 GK / 2 LK
    - Pfadwahrscheinlichkeit für lauter gleiche Ergebnisse als Potenz berechnen: 2 GK / 2 LK
    - Term und Ereignis: Fehlende Werte in einem Wahrscheinlichkeitsterm bestimmen: 2 GK / 2 LK
    - Fehlenden Anteil im Baumdiagramm aus einer Randwahrscheinlichkeit berechnen: 1 GK / 2 LK
    - Laplace-Experiment: Sektorwinkel eines Glücksrads aus einer Wahrscheinlichkeitsbedingung berechnen: 2 GK / 1 LK
    - Verhältnis zweier Pfadwahrscheinlichkeiten im Baumdiagramm prüfen: 1 GK / 2 LK
    - Anteil eines Entweder-oder-Ereignisses aus einer Tafel berechnen: 1 GK / 1 LK
    - Anteil für genau eines von zwei Ereignissen aus Anteilen und Schnitt berechnen: 2 GK / 0 LK
    - Anteil über die totale Wahrscheinlichkeit aus dem Baumdiagramm berechnen: 2 GK / 0 LK
    - Baumdiagramm mit aus einer Pfadwahrscheinlichkeit erschlossener Einzelwahrscheinlichkeit erstellen: 1 GK / 1 LK
    - Ergebnisse zu einer Mengenoperation zweier Ereignisse angeben: 2 GK / 0 LK
    - Fehlende Wahrscheinlichkeiten im Baumdiagramm über die Pfadregel ermitteln: 2 GK / 0 LK
    - Gewinnwahrscheinlichkeiten in einem Wechselspiel vergleichen: 1 GK / 1 LK
    - Laplace-Experiment: Laplace-Wahrscheinlichkeit als Anteil der günstigen Fälle angeben: 2 GK / 0 LK
    - Pfadwahrscheinlichkeit zweier Stufen aus dem Sachtext berechnen: 2 GK / 0 LK
    - Term und Ereignis: Schnittwahrscheinlichkeit zweier Ereignisse im Sachzusammenhang deuten: 2 GK / 0 LK
    - Totale Wahrscheinlichkeit über die Pfadregeln nachweisen: 2 GK / 0 LK
    - Wahrscheinlichkeit einer Summe über alle Ergebnisfolgen mit Reihenfolgen berechnen: 2 GK / 0 LK
    - Wahrscheinlichkeit einer vorgegebenen Augensumme bei zwei Würfen über Pfade berechnen: 0 GK / 2 LK
    - Wahrscheinlichkeit für mindestens oder höchstens einmal bei mehreren Stufen über das Gegenereignis berechnen: 1 GK / 1 LK
    - Ziehen ohne Zurücklegen: Kugelzahl aus einer Wahrscheinlichkeitsbedingung beim Umlegen einer Kugel bestimmen: 0 GK / 2 LK
    - Absolute Anzahl aus einer Pfadwahrscheinlichkeit mit einer Schranke vergleichen: 0 GK / 1 LK
    - Anteil aus dem Ergebnis eines Befragungsverfahrens berechnen: 1 GK / 0 LK
    - Anteil aus einem Verhältnis zweier Pfadwahrscheinlichkeiten berechnen: 1 GK / 0 LK
    - Anteil aus einer quadratischen Gleichung für ein zweistufiges Bestehen berechnen: 1 GK / 0 LK
    - Anteil einer Eigenschaft aus einer Randomized-Response-Befragung über die totale Wahrscheinlichkeit nachweisen: 1 GK / 0 LK
    - Anteil in der Restgruppe über die totale Wahrscheinlichkeit einordnen: 1 GK / 0 LK
    - Anzahlvergleich zweier Teilgruppen über Pfadwahrscheinlichkeiten nachweisen: 0 GK / 1 LK
    - Astwahrscheinlichkeit im Baumdiagramm einer Befragung im Sachzusammenhang deuten: 1 GK / 0 LK
    - Baumdiagramm eines Befragungsverfahrens mit unbekanntem Anteil vervollständigen: 1 GK / 0 LK
    - Baumdiagramm mit Abbruchbedingung erstellen: 0 GK / 1 LK
    - Bedingte Wahrscheinlichkeit einer Teilgruppe aus totaler Wahrscheinlichkeit und der anderen Teilgruppe berechnen: 1 GK / 0 LK
    - Gegenereignis einer Vereinigung im Sachzusammenhang beschreiben: 1 GK / 0 LK
    - Laplace-Experiment: Ergebnisse eines zusammengesetzten Experiments zu einem Zahlenwert aufzählen: 1 GK / 0 LK
    - Laplace-Experiment: Kleinere Gesamtzahl von Kugeln aus gekürzten Anteilen begründen: 1 GK / 0 LK
    - Laplace-Experiment: Kugelzahl aus zwei Wahrscheinlichkeitsbedingungen vor und nach einem Austausch ermitteln: 0 GK / 1 LK
    - Laplace-Experiment: Sektorwinkel eines Glücksrads aus der Maximierung einer Wahrscheinlichkeit ermitteln: 1 GK / 0 LK
    - Laplace-Experiment: Urnenmodell zu einer vorgegebenen Verteilung beschreiben: 0 GK / 1 LK
    - Laplace-Experiment: Wahrscheinlichkeit durch Abzählen günstiger Ergebnisse berechnen: 1 GK / 0 LK
    - Laplace-Experiment: Wahrscheinlichkeit einer Augensumme beim Wurf zweier Würfel begründen: 1 GK / 0 LK
    - Laplace-Experiment: Wahrscheinlichkeit eines sicheren Ereignisses beim Umlegen einer Kugel begründen: 0 GK / 1 LK
    - Laplace-Experiment: Wahrscheinlichkeit für drei verschiedene Ergebnisse über Pfadprodukt und Reihenfolgen nachweisen: 0 GK / 1 LK
    - Laplace-Experiment: Wahrscheinlichkeiten zweier Extremsummen über die Häufigkeit der Beschriftung vergleichen: 1 GK / 0 LK
    - Laplace-Experiment: Wahrscheinlichkeitsterm nach Hinzufügen von Kugeln als Anteil begründen: 1 GK / 0 LK
    - Laplace-Experiment: Zunahme einer Wahrscheinlichkeit nach Hinzufügen von Kugeln über eine Termdifferenz begründen: 1 GK / 0 LK
    - Term für die Wahrscheinlichkeit eines Produktereignisses bei n Würfen ermitteln: 0 GK / 1 LK
    - Term für die Wahrscheinlichkeit eines mehrstufigen Pfads angeben: 0 GK / 1 LK
    - Term und Ereignis: Bedingte Wahrscheinlichkeit und Schnittwahrscheinlichkeit im Sachzusammenhang deuten: 1 GK / 0 LK
    - Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitswert als Potenz angeben: 1 GK / 0 LK
    - Term und Ereignis: Produkt aus Potenz und Binomialterm als Ereignis mit festem Abschnitt deuten: 1 GK / 0 LK
    - Term und Ereignis: Wahrscheinlichkeitsterm über das Gegenereignis gleicher Ergebnisse begründen: 1 GK / 0 LK
    - Term und Ereignis: Zufallsexperiment und Ereignis zu einer Potenz der Gegenwahrscheinlichkeit beschreiben: 1 GK / 0 LK
    - Wahrscheinlichkeit bei zweistufigem Umlegen zwischen Urnen berechnen: 0 GK / 1 LK
    - Wahrscheinlichkeit des Gegenereignisses einer Vereinigung nachweisen und als Ereignis angeben: 1 GK / 0 LK
    - Wahrscheinlichkeit einer ungeraden Summe über Pfade berechnen: 1 GK / 0 LK
    - Wahrscheinlichkeit eines Gewinns über alle günstigen Summenpfade nachweisen: 1 GK / 0 LK
    - Wahrscheinlichkeit eines Schnitts aus einem Randanteil und dem Anteil ohne beide Mängel nachweisen: 1 GK / 0 LK
    - Wahrscheinlichkeit eines Spielausgangs über Pfade mit Abbruch berechnen: 1 GK / 0 LK
    - Wahrscheinlichkeit eines Vergleichs zweier Zufallsgeräte über Pfade berechnen: 0 GK / 1 LK
    - Wahrscheinlichkeit für das Erreichen eines Feldes über die Pfadregel berechnen: 0 GK / 1 LK
    - Wahrscheinlichkeit für ein zweistufiges Experiment mit zufälliger Urnenzusammensetzung berechnen: 0 GK / 1 LK
    - Wahrscheinlichkeit für k Treffer unmittelbar hintereinander unter n Versuchen berechnen: 1 GK / 0 LK
    - Wahrscheinlichkeit für mehrere Wiederholungen ohne Abbruch als Potenz berechnen: 0 GK / 1 LK
    - Ziehen ohne Zurücklegen: Anzahl einer Sorte aus der Wahrscheinlichkeit für zwei verschiedene Sorten bestimmen: 1 GK / 0 LK
    - Ziehen ohne Zurücklegen: Kugelzahl aus dem Vergleich der zweiten Zugwahrscheinlichkeit mit und ohne Zurücklegen berechnen: 0 GK / 1 LK
    - Ziehen ohne Zurücklegen: Mögliche Anzahlen nach dem Umlegen zweier Kugeln angeben: 0 GK / 1 LK
    - Ziehen ohne Zurücklegen: Wahrscheinlichkeit für genau k einer Sorte beim mehrfachen Ziehen über Pfade berechnen: 1 GK / 0 LK
    - Ziehen ohne Zurücklegen: Wahrscheinlichkeit für spätestens den dritten Zug über das Gegenereignis berechnen: 1 GK / 0 LK
  - fhr: 28 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: nur GK-Block; Typenzeilen: 131 GK / 78 LK)

### zufallsgroessen-und-verteilungen
- Geltung je Zielprüfung:
  - Thema „Zufallsgrößen und Verteilungen“ (`themen.csv`):
    - be-gk: ja – `| Zufallsgrößen und Verteilungen | ja |` [abi-be-gk-geltung.md Zeile 56]
    - be-lk: ja – `| Zufallsgrößen und Verteilungen | ja |` [abi-be-lk-geltung.md Zeile 56]
    - bb-gk: ja – `| Zufallsgrößen und Verteilungen | ja |` [abi-bb-gk-geltung.md Zeile 56]
    - bb-ea: ja – `| Zufallsgrößen und Verteilungen | ja |` [abi-bb-ea-geltung.md Zeile 56]
- Lerneinheiten:
  - 1. Verteilung aufstellen: die Werte der Zufallsgröße aus den Regeln gewinnen (alle Ergebnisfolgen durchrechnen), die Tabelle durch Abzählen füllen (günstige Paare je Wert), fehlende Wahrscheinlichkeiten über die Summe eins
    - Eintrag, Zeile 11: „(Q2, GK-Kern „Zufallsgrößen als Zuordnung“, „Verteilung in Tabellen“)“
    - GOST Berlin [Zeilen 1214–1215]: „Zufallsgrößen und Wahrscheinlichkeitsverteilungen zur Beschreibung stochastischer Situationen nutzen.“
      Funktionaler Zusammenhang [L4], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1103–1104]: „Zufallsgrößen und Wahrscheinlichkeitsverteilungen zur Beschreibung“
      Q2, Grund- und Leistungskursfach
    - Ermessen: Länderunterschied: Zufallsgrößen und Wahrscheinlichkeitsverteilungen stehen in Berlin im LK-Zusatz, in Brandenburg im Grund- und Leistungskursfach des zweiten Kurshalbjahrs.
  - 2. Verteilung lesen: die Symmetrie einer Verteilung nutzen (Restwahrscheinlichkeit gleich verteilen, kumulierte Werte daraus), beschriebene Zufallsgrößen den Säulendiagrammen zuordnen (Symmetrie, Verhältnisse einzelner Säulen). (Q2, GK-Kern „Verteilung in … Diagrammen“; OHiMi 2.4 Histogramme) ← Eingabe „verteilung zuordnen“, „symmetrische verteilung“, „säulendiagramm zufallsgröße“
    - Eintrag, Zeile 12: „(Q2, GK-Kern „Verteilung in … Diagrammen“; OHiMi 2.4 Histogramme)“
    - GOST Berlin [Zeilen 1214–1215]: „Zufallsgrößen und Wahrscheinlichkeitsverteilungen zur Beschreibung stochastischer Situationen nutzen.“
      Funktionaler Zusammenhang [L4], Zusätzlich: Leistungskursfach
    - GOST Brandenburg [Zeilen 1105–1106]: „Wahrscheinlichkeitsverteilung einer Zufallsgröße in Tabellen und Diagrammen“
      Q2, Grund- und Leistungskursfach
- Haupttypen der Prüfungsform, Zeilen nach Kursart (GK = be-gk, bb-gk, iqb grundlegend; LK = be-lk, bb-ea, iqb erhöht):
  - abi: 0 Zeilen GK / 1 Zeilen LK, 1 Haupttypen
    - Wahrscheinlichkeit eines Ereignisses aus einer symmetrischen Verteilung und einem Einzelwert bestimmen: 0 GK / 1 LK
  - iqb: 2 Zeilen GK / 3 Zeilen LK, 5 Haupttypen
    - Mögliche Werte einer Auszahlung aus zweistufigen Spielregeln nachweisen: 1 GK / 0 LK
    - Verteilungen zweier Zufallsgrößen den Säulendiagrammen zuordnen: 0 GK / 1 LK
    - Wahrscheinlichkeit p aus der Summe 1 im Diagramm nachweisen: 0 GK / 1 LK
    - Wahrscheinlichkeitsverteilung der Augensumme in einer Tabelle vervollständigen: 0 GK / 1 LK
    - Wahrscheinlichkeitsverteilung über ein unmögliches Ergebnis vervollständigen: 1 GK / 0 LK
  - fhr: 0 Zeilen, keine Kursart (Fachoberschule)
- Spanne: ja – Einheiten oder Typen in beiden Kursarten (Einheiten: GK-Block und LK-Block; Typenzeilen: 2 GK / 4 LK)
