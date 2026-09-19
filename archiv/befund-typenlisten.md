# BEFUND – Die drei Typenlisten nebeneinander
Stand 17.09.2026 (Auftrag D „Namensschema, Erweiterbarkeit, Begründungen",
Teil 3). Nur Vergleich und Vorschläge; nichts zusammengelegt, nichts
umbenannt. Über die Vorschläge in § 3 entscheidet der Lehrer. Dateiname
nach namensschema.md § 2 (Befunddatei `befund-<gegenstand>.md`).

Verglichen: typen.csv (Profil msa, 185 Typen, 393 Katalogzeilen),
fhr-typen.csv (fhr, 135 Typen, 253 Zeilen), abitur-typen.csv (abi und iqb,
1323 Typen, 2237 Zeilen). Zahlen per Skript (Scratchpad typvgl*.py).

## 1 Nebeneinander

| Merkmal | typen.csv (msa) | fhr-typen.csv | abitur-typen.csv |
|---|---|---|---|
| Spaltensatz | typ;leitidee;thema;definition;beispiel_id;status | gleich | gleich |
| Format | Semikolon, alle Felder gequotet, UTF-8 ohne BOM, LF | gleich | gleich |
| Leitideen | 5 (Rahmenlehrplan 1–10: Zahlen und Operationen, Größen und Messen, Raum und Form, Gleichungen und Funktionen, Daten und Zufall) + 1 Typ ohne Leitidee | 4 (Differentialrechnung, Integralrechnung, Stochastik, Grundlagen – Grundlagen ist Zutat des Profils) | 3 Sachgebiete (Analysis, Analytische Geometrie, Stochastik) |
| Themen | 33, Substantive („Prozentrechnung", „Kenngrößen") und Tätigkeiten („Terme umformen", „Diagramme lesen und beurteilen") | 29, davon 9 als Tätigkeit („Ableitungen bilden", „Symmetrie nachweisen", „Graph zeichnen und zuordnen") | 49 (48 verschieden), fast nur Substantive („Kurvenuntersuchung", „Baumdiagramm und Pfadregeln"); Tätigkeit nur „Gleichungen lösen" |
| Gleichnamige Themen | msa∩fhr: Prozentrechnung, Terme umformen | fhr∩abi: Baumdiagramm und Pfadregeln, Gleichungen lösen | msa∩abi: Lineare Gleichungssysteme |
| Benennung des Typs | Gegenstand + Handlung, kurz (Median 32 Zeichen, 16–50); 5 ohne Verb („Pythagoras Hypotenuse", „Wahrscheinlichkeit einstufig") – die Beispiele des Kerns § 6 | Gegenstand + Handlung, mittel (Median 43, 20–66); 20 ohne Verb, Nominalphrasen („Ableitung ganzrationale Funktion", „Mittelwert aus Häufigkeitstabelle", „Tangentengleichung im Punkt") | Gegenstand + Handlung, lang (Median 83, 31–151), oft mit Lösungsweg im Namen („… über die zweite Ableitung …", „… aus n und Erwartungswert …"); 472 mit Klassenpräfix „Klasse: " (abitur-vokabular.md § 4); 1 ohne Verb am Ende (Nebensatz) |
| Endverb | berechnen 63, bestimmen 19, angeben 9, zuordnen 9, ablesen 6 | berechnen 34, bestimmen 9, angeben 7, einzeichnen 6 | berechnen 263, begründen 173, bestimmen 171, nachweisen 114, angeben 114, ermitteln 80, deuten 65 |
| Stufenzahl im Namen | „zweistufig", „mehrstufig" | „zweistufig" nur unter Baumdiagramm und Pfadregeln (Themenbedingung, fhr.md § 9), sonst „mehrstufig" | „zweistufig", „mehrstufig", „zweimaliges Ziehen" |
| Definition | ein Satz, Median 103 Zeichen, oft mit Abgrenzung („Gegenrichtung zu …") | ein Satz, Median 118 | ein bis zwei Sätze, Median 159, mit Lösungsweg und Grenzfällen („welche Figur, steht in der Zeile") |
| beispiel_id | 2025-OS-K3b (Jahr-papier-BlockAufgabeBuchstabe) | 2026-C-1a | abi-ids (2025-bebb-lk-B2.1c) und Pool-Kennungen (2026MgrundlegendAAnalysis11-a) gemischt |
| status | gültig (185) | geprüft (125), neu (10) | neu (1323) |
| Sortierung | nach Leitidee (Lehrplanreihenfolge), Thema, Typ (Typen-Check 05.09.2026) | Erfassungsreihenfolge (52 Leitideenblöcke) | Erfassungsreihenfolge (174 Blöcke) |
| Leere Felder | 1 Typ ohne leitidee und thema („Behauptung prüfen", leitideenübergreifend, nur typ_neben) | keine | keine |
| Pflege | Typen-Check von Hand (konzept.md § 10), kein Skript | fhr-bau.py (NEUE_TYPEN), Abgleichlauf von Hand (fhr.md § 9) | Bau-Skripte (NEUE_TYPEN) und abgleich.py; Präfixregel und Zeilenthema = Typthema skriptgeprüft |
| Regel Zeilenthema | Thema der Zeile frei (Kern v0.3) | Punkt-Schwerpunkt bei mehrleistigen Zeilen (fhr.md § 6) | Zeilenthema = Typthema, erzwungen (abitur-vokabular.md § 4) |

## 2 Abweichungen

1. **Statuswerte:** drei Vokabulare für dasselbe Feld – msa „gültig", fhr
   „geprüft"/„neu", abitur nur „neu". Der Kern § 6 verlangt „neu" beim
   Anlegen und sagt nichts zum weiteren Wert; kein Skript liest oder setzt
   das Feld (abgleich.py lässt es unverändert). In abitur-typen.csv sind nach
   23 Abgleichläufen alle 1323 Typen „neu" – das Feld trägt dort keine
   Information.
2. **Verb am Ende:** msa 5 und fhr 20 Typnamen ohne Handlungsverb; abitur
   durchgehend mit. Der Kern nennt in § 6 selbst zwei verblose Beispiele
   („Pythagoras Hypotenuse", „Wahrscheinlichkeit zweistufig unabhängig") –
   die Regel „Gegenstand plus Handlung" ist dort nicht streng gemeint.
3. **Synonyme Handlungsverben:** berechnen/bestimmen/ermitteln stehen in
   allen Listen nebeneinander (abitur: 263/171/80), angeben/ablesen ebenso.
   Der Kern sagt „ohne Synonyme"; die Handlung des Schnitts kommt aber aus
   format, nicht aus dem Verb (Kern § 5), das Verb im Namen hat keine
   Skriptbedeutung.
4. **Themenbenennung:** dieselbe Sache heißt in zwei oder drei Listen
   verschieden (§ 3, Vorschlag 3). Themen als Tätigkeit kommen in allen drei
   Listen vor, sind also kein Unterschied der Listen.
5. **Namenslänge und Lösungsweg im Namen:** abitur-Namen sind doppelt so lang
   wie msa-Namen und tragen den Lösungsweg („über das Skalarprodukt", „aus
   der faktorisierten Form"); msa und fhr tragen ihn in der Definition. Folge
   der Trennregel „anderer Lösungsweg → trennen" (Kern § 6) bei 1323 Typen
   auf 48 Themen; msa braucht bei 185 Typen auf 33 Themen keine so feine
   Trennung.
6. **Klassenpräfix** nur in abitur (Entscheidung 24/25).
7. **Sortierung:** msa sortiert, fhr und abitur in Erfassungsreihenfolge.
8. **Ein Typ ohne Leitidee** (msa „Behauptung prüfen"); die Bau-Skripte von
   fhr und abi würden eine solche Zeile abweisen.
9. **Regel für das Zeilenthema** dreifach verschieden (Tabelle, letzte
   Zeile).
10. **beispiel_id-Muster** folgt dem id-Muster des Profils (namensschema.md
    § 1); in abitur-typen.csv zwei Muster in einer Spalte.

## 3 Vorschläge zur Vereinheitlichung (nicht ausgeführt)

| Nr. | Vorschlag | Was sich ändert | Betroffene Zeilen | Was es bringt |
|---|---|---|---|---|
| 1 | Statuswerte im Kern § 6 festlegen: „neu" beim Anlegen, „geprüft" nach dem ersten Abgleichlauf, der den Typ gesehen hat; „gültig" entfällt | Kern § 6 ein Satz; typen.csv 185 × gültig → geprüft; abitur-typen.csv 1323 × neu → geprüft (alle Typen bis Lauf 23 sind durch mindestens einen Abgleichlauf gegangen) oder: abgleich.py setzt künftig „geprüft" für jeden Typ, der zum Zeitpunkt eines Laufs schon in der Liste steht; fhr unverändert | 1508 Typenzeilen, 0 Katalogzeilen, 0 Skriptprüfungen (kein Skript liest status) | das Feld sagt wieder etwas: welche Typen ein Abgleichlauf gesehen hat; ein Vokabular für alle Listen |
| 2 | Verb am Ende für die 25 verblosen Typnamen (msa 5, fhr 20): „Pythagoras Hypotenuse" → „Hypotenuse mit dem Satz des Pythagoras berechnen", „Mittelwert aus Häufigkeitstabelle" → „… berechnen", „Ableitung ganzrationale Funktion" → „Ableitung einer ganzrationalen Funktion bilden" | 25 Typenzeilen; die Katalogzeilen, die sie in typ oder typ_neben tragen: msa 38, fhr 91; Kern § 6 Beispiele | 25 Typen, 129 Katalogzeilen (per Skript, wie abgleich.py) | einheitliches Muster Gegenstand + Handlung in allen Listen; für neue Profile ein Vorbild ohne Ausnahmen |
| 3 | Gleiche Sache, gleicher Themenname über die Profile: Kenngrößen (msa) / Statistische Kenngrößen (fhr) / Lage- und Streumaße einer Stichprobe (abi); Zählen und Kombinatorik / Kombinatorische Abzählverfahren / Kombinatorik; Wahrscheinlichkeit mehrstufig / Mehrstufige Zufallsexperimente; Daten darstellen / Daten darstellen und aufbereiten; Extremwertaufgaben / Extremalprobleme; Rotationsvolumen um die x-Achse / Rotationsvolumen; Unabhängigkeit von Ereignissen / Unabhängigkeit; Verhalten im Unendlichen / Grenzwerte und Verhalten im Unendlichen; Funktionsgleichung bestimmen / Rekonstruktion von Funktionsgleichungen; Lineare Gleichungen + Quadratische Gleichungen (msa) / Gleichungen lösen (fhr, abi). Leitname jeweils der abitur-Name (größte Liste, aus Prüfungsschwerpunkten abgeleitet) | Themenlisten in msa.md § 6 und fhr.md § 6, THEMEN in fhr-bau.py und fhr-typenbibliothek.py; Feld thema in Typen- und Katalogzeilen | msa: 6 Themen, 24 Typen, 63 Katalogzeilen; fhr: 9 Themen, 42 Typen, 88 Katalogzeilen; abitur unverändert | der Themenkatalog (konzept.md § 3) soll je Thema einen Eintrag über alle Prüfungsarten führen – gleiche Namen ersparen dort eine Zuordnungstabelle; Blattbau über Profile hinweg findet Verwandtes unter einem Namen |
| 4 (ausgeführt 17.09.2026, Auftrag E Punkt 6: Leitidee und Thema der ersten Fundstelle, über msa-bau.py) | Den msa-Typ „Behauptung prüfen" einem Thema zuordnen oder als Nebentyp ohne Thema im Kern erlauben | 1 Typenzeile oder ein Satz im Kern § 6 | 1 | msa-Liste besteht die Prüfung der anderen Bau-Skripte (Vorbereitung eines msa-bau.py) |
| 5 | Sortierung der Listen: nach Leitidee, Thema, Typ (wie msa) beim nächsten Abgleichlauf | Zeilenreihenfolge in fhr-typen.csv und abitur-typen.csv; abgleich.py schreibt sortiert | 1458 Zeilen (nur Reihenfolge) | Diff-Lesbarkeit; gleiche Typen desselben Themas stehen beieinander – aber: byteidentische HEAD-Reruns älterer Läufe sind dann nicht mehr möglich, und git-Diffs des Sortierlaufs sind unlesbar. Nur, wenn der Lehrer die Reihenfolge braucht |

**Sachlich begründete Abweichungen – kein Vorschlag:**

- **Synonyme Handlungsverben** (Abweichung 3): das Verb hat keine
  Skriptbedeutung, die Handlung kommt aus format; eine Bereinigung kostete
  abitur 251, msa 19, fhr 9 Umbenennungen und die zugehörigen Katalogzeilen
  für keinen messbaren Nutzen. Höchstens eine Regel für neue Namen
  („berechnen" statt „bestimmen/ermitteln", wenn gerechnet wird).
- **Namenslänge und Lösungsweg im Namen** (Abweichung 5): folgt aus der
  Größe der abitur-Liste und der Trennregel des Kerns; msa und fhr auf
  dieselbe Länge zu bringen brächte nichts, abitur zu kürzen würde Typen
  zusammenwerfen, die der Abgleich bewusst getrennt hat.
- **Klassenpräfix** nur in abitur: Entscheidung 24/25 für den Schnitt Thema
  × Klasse × Handlung; msa und fhr haben keinen solchen Schnitt (fhr
  Typenbibliothek nach Thema und Typ). Übertragung nur mit einer eigenen
  Klassenliste je Profil – kein Bedarf.
- **Regel für das Zeilenthema** dreifach: msa ist auf Kern v0.3 stehen
  geblieben, fhr hat den Punkt-Schwerpunkt bewusst gewählt (fhr.md § 6,
  Fall 2024-B-2a), abi/iqb erzwingen Gleichheit (Entscheidung 26). Eine
  Vereinheitlichung wäre eine Kernänderung und ein Abgleichlauf über fhr
  (etwa 5 Zeilen, die vom Typthema abweichen, fhr.md § 7); der Kern § 6
  erlaubt seit v0.4 ausdrücklich beides.
- **Themen als Tätigkeit** in allen Listen: kein Listenunterschied.
- **beispiel_id-Muster**: folgt dem id-Muster des Profils, das die Zeile
  identifiziert; die gemischte Spalte in abitur-typen.csv ist die Folge der
  geteilten Liste und gewollt (abitur-vokabular.md § 6).
- **Leitideen und Themenzahl**: verschiedene Prüfungen, verschiedene
  Lehrpläne (Rahmenlehrplan 1–10, Rahmenlehrplan FOS, Bildungsstandards);
  die drei Ebenen sind je Profil zu Recht verschieden (Entscheidung 12, 13).

## 4 Typen, die in zwei Listen vorkommen

Kein Typname steht wörtlich in zwei Listen (auch nicht ohne Klassenpräfix
und Groß-/Kleinschreibung). Dieselbe Fertigkeit unter verschiedenem Namen,
gefunden über Wortmengen (≥ 0,5 gemeinsame Wörter ohne Handlungsverben) und
Definitionsvergleich; „gleich geschnitten" heißt: dieselbe Fertigkeit,
dieselbe Grenze zu Nachbartypen.

| Fertigkeit | msa | fhr | abitur | Gleich geschnitten? |
|---|---|---|---|---|
| Masse aus Volumen und Dichte | Masse aus Volumen und Dichte berechnen (Einheiten umrechnen) | Masse aus Volumen und Dichte (Größen und Einheiten) | – (nur als Nebenleistung in Kontexten) | ja; msa nennt zusätzlich Füllgrad und Leermasse, fhr nur den Grundfall – Definitionen deckungsgleich im Kern; Namen unterscheiden sich nur um das Verb |
| Geradengleichung aus zwei Punkten | Geradengleichung aus zwei Punkten (Lineare Funktionen) | Geradengleichung aus zwei Punkten bestimmen (Funktionsgleichung bestimmen) | Geradengleichung durch zwei Punkte aufstellen (Geraden) – Parameterform im Raum | msa/fhr ja (Steigung und Achsenabschnitt, f(x) = mx + n); abitur nein – andere Fertigkeit (Stütz- und Richtungsvektor), zu Recht getrennt |
| Relative Häufigkeit | Relative Häufigkeit angeben (Kenngrößen) | Relative Häufigkeit berechnen (Daten darstellen und aufbereiten) | Relative Häufigkeit aus absoluten Häufigkeiten berechnen (Lage- und Streumaße) | ja, drei Namen für einen Quotienten; abitur enger (Restsumme aus den übrigen Häufigkeiten), msa/fhr der Grundfall – dreimal unter einem anderen Thema |
| Fehlender Wert aus dem Mittelwert | Fehlenden Wert aus Mittelwert bestimmen | Fehlenden Wert aus vorgegebenem Mittelwert bestimmen | – | ja; fhr mit Häufigkeiten (gewichtet), msa mit Liste – derselbe Ansatz (Gleichung aus der Mittelwertformel) |
| Prozentsatz | Prozentsatz berechnen (auch Zinssatz) | Prozentsatz aus Anteil berechnen | – | ja; msa weiter (Zinssatz eingeschlossen, Entscheidung Typen-Check 05.09.) |
| Grundwert | Grundwert berechnen (aus Prozentwert und Prozentsatz) | Grundwert aus Prozentwert berechnen (aus vermindertem oder vermehrtem Wert) | – | **nein**: fhr meint den verminderten/vermehrten Grundwert (Rabatt 20 %, 2026-C-3b), msa den Grundfall; msa hat keinen eigenen Typ für den verminderten Grundwert – derselbe Name stünde für zwei Schnitte |
| Zusammengesetzte Figur | Flächeninhalt zusammengesetzter Figur berechnen (Rechteck und Kreisteile) | Flächeninhalt einer zusammengesetzten Figur berechnen (Rechtecke und Dreiecke) | – | ja (Zerlegen und Addieren); msa schließt Kreisteile ein |
| Median | Median bestimmen | Median aus Werteliste; Median aus Häufigkeitstabelle; Medianklasse aus klassierter Häufigkeitstabelle bestimmen | Medianklasse aus einem Säulendiagramm relativer Häufigkeiten begründen | **nein**: fhr schneidet nach der Datenform (drei Typen), msa hat einen; abitur nur den Klassenfall |
| Fehlende Wahrscheinlichkeiten im Baumdiagramm | Baumdiagramm ergänzen | – (fhr: Baumdiagramm … darstellen = zeichnen, andere Handlung) | Fehlende Wahrscheinlichkeiten im Baumdiagramm über die Pfadregel ermitteln; Fehlenden Anteil im Baumdiagramm aus einer Randwahrscheinlichkeit berechnen | msa/abitur im Kern ja (Knotensumme, Pfadregel); abitur trennt zusätzlich den Fall über die Randwahrscheinlichkeit ab – feiner geschnitten |
| Mehrstufig ohne Zurücklegen | Wahrscheinlichkeit mehrstufig ohne Zurücklegen (berechnen) | Pfadregel mehrstufig ohne Zurücklegen anwenden | Ziehen ohne Zurücklegen: Wahrscheinlichkeit beim zweimaligen Ziehen ohne Zurücklegen berechnen | ja bei msa/fhr (Pfadprodukt mit sinkendem Nenner, zwei oder mehr Stufen); abitur enger (zweimaliges Ziehen, beide mit Eigenschaft) |
| Mehrstufig unabhängig / mit Zurücklegen | Wahrscheinlichkeit mehrstufig unabhängig | Pfadregel mehrstufig mit Zurücklegen anwenden (Potenz der Einzelwahrscheinlichkeit) | Wahrscheinlichkeit für mindestens oder höchstens einmal bei mehreren Stufen über das Gegenereignis berechnen (nur der Gegenereignisfall) | msa/fhr im Kern ja; fhr enger (gleichartige Versuche, Potenz), msa auch verschiedene Geräte |
| Wendepunkte über f'' | – | Wendepunkte über zweite Ableitung | Wendepunkte über die zweite Ableitung berechnen (Kurvenuntersuchung) | ja; abitur nennt die Produktregel bei e^x mit – Namen unterscheiden sich um Artikel und Verb |
| Extrem-/Sattelpunkte über f'' | – | Extrem- und Sattelpunkte über zweite Ableitung | Extrempunkt an vorgegebener Stelle nachweisen; Extremstellen berechnen und Monotonieverhalten angeben; … (mehrere) | **nein**: abitur schneidet nach Aufgabenform (Nachweis an vorgegebener Stelle, Berechnung mit Monotonie, Art über Vorzeichenwechsel), fhr hat den Sammeltyp; Sattelpunkt bei fhr im Namen, bei abitur eigener Typ |
| Ableitung einer ganzrationalen Funktion | – | Ableitung ganzrationale Funktion (erste bis dritte) | Ableitung einer quadratischen Funktion angeben; Ableitung mit Parameter in faktorisierter Form nachweisen | **nein**: abitur hat keinen Typ für das bloße Ableiten einer ganzrationalen Funktion (im Pool immer Schritt eines anderen Typs), nur Sonderfälle |
| Tangentengleichung im Punkt | – | Tangentengleichung im Punkt | Tangentengleichung in einem Punkt des Graphen aufstellen | ja |
| Nullstellen aus der faktorisierten Form | – | Nullstellen aus der faktorisierten Form ablesen | Nullstellen und Werte: Nullstellen aus der faktorisierten Form angeben | ja (abitur nennt doppelte Nullstellen mit) |
| Funktionswert im Sachzusammenhang | Funktionswert berechnen (ohne Sachbezug) | Funktionswert im Sachzusammenhang deuten; Funktionswert an einer Stelle berechnen | Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen | fhr/abitur ja; msa hat nur den Grundfall ohne Sachbezug – drei Listen, drei Schnitte (msa 1, fhr 2, abitur 1 mit Sachbezug plus weitere Sonderfälle) |
| Fläche zwischen Graph und x-Achse | – | Fläche zwischen Graph und x-Achse berechnen (ein Typ) | Fläche: Fläche zwischen Graph und x-Achse aus zwei Flächenstücken berechnen; Fläche: Fläche zwischen Graph und Koordinatenachsen berechnen; … (acht Fläche-Typen) | **nein**: abitur schneidet nach Lage und Begrenzung (Klasse Fläche), fhr nach dem Verfahren (ein Typ) |
| Fläche zwischen zwei Graphen | – | Fläche zwischen zwei Graphen berechnen | Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen | ja (abitur schließt die waagerechte Gerade ein) |
| Vierfeldertafel vervollständigen | – | Vierfeldertafel vervollständigen (aus Anzahlen; Thema Unabhängigkeit) | Vierfeldertafel aus Anteilen vervollständigen; Fehlende absolute Häufigkeit über die Vierfeldertafel berechnen (Thema Vierfeldertafel) | **nein**: abitur trennt Anteile von Anzahlen; fhr hat einen Typ unter einem anderen Thema (fhr.md § 9 bewusst so gelassen) |
| Stochastische Unabhängigkeit prüfen | – | Stochastische Unabhängigkeit prüfen | Stochastische Unabhängigkeit zweier Ereignisse über die Produktregel untersuchen | ja (abitur nennt den gleichwertigen Vergleich bedingter Anteile mit) |
| Erwartungswert berechnen | – | Erwartungswert berechnen | Erwartungswert einer Zufallsgröße im Sachzusammenhang berechnen; Erwartungswert aus einer Verteilung mit fehlender Wahrscheinlichkeit berechnen | fhr/abitur im Kern ja (gewichtete Summe); abitur trennt den Sachtext-Fall und den Fall mit fehlender Wahrscheinlichkeit ab |
| Punktprobe | Punktprobe durchführen (Graph einer Funktion) | – | Nullstellen und Werte: Punkt, Nullstelle oder Schnittstelle durch Einsetzen nachweisen; Punktprobe an einer Geraden durchführen; Punkt und Ebene: Punktprobe an einer Ebenengleichung durchführen | **nein**: abitur bündelt Punkt/Nullstelle/Schnittstelle in einem Typ und trennt Gerade und Ebene ab; msa hat den reinen Graphenfall |
| Lineares Gleichungssystem lösen | Lineares Gleichungssystem lösen (zwei Unbekannte) | – | Lineares Gleichungssystem mit drei Variablen lösen | nein – anderer Gegenstand (2 gegen 3 Variablen), zu Recht getrennt; ein gemeinsamer Name müsste die Variablenzahl in die Zeile verlegen |
| Rechter Winkel | Rechten Winkel begründen (Winkelsumme, Thales, Pythagoras-Umkehrung) | – | Dreieck: Rechten Winkel … nachweisen (Skalarprodukt, vier Typen) | nein – anderer Lösungsweg (Kern § 6: trennen); gleicher Gegenstand, gleiches Verb, verschiedene Fertigkeit |
| Wahrscheinlichkeit über das Gegenereignis | Wahrscheinlichkeit über Gegenereignis berechnen (allgemein) | – | Wahrscheinlichkeit für wenigstens einen Treffer über das Gegenereignis berechnen (Binomialverteilung); Wahrscheinlichkeit für mindestens oder höchstens einmal bei mehreren Stufen über das Gegenereignis berechnen | **nein**: abitur schneidet nach Verteilung bzw. Stufenbau, msa nach dem Rechenschritt 1 − P |

Befund: von 26 Fertigkeiten, die in zwei oder drei Listen vorkommen, sind
16 gleich geschnitten (nur Name, Thema oder ein Randfall verschieden), 8
verschieden geschnitten – fast immer, weil abitur feiner trennt (nach
Aufgabenform, Datenform, Lage oder Verteilung) und msa/fhr den Sammeltyp
führen –, 2 zu Recht getrennt (anderer Lösungsweg oder Gegenstand). Eine
Zusammenführung der Listen (nicht beauftragt) hätte an den 8 Stellen zu
entscheiden, ob der grobe oder der feine Schnitt gilt; Kern § 6 („anderer
Lösungsweg → trennen") spricht für den feinen. Die 16 gleich geschnittenen
Fertigkeiten könnten denselben Namen tragen; Vorschlag 2 gleicht bei den
verblosen fhr-Namen (Wendepunkte, Tangentengleichung, Masse, Median) die
Form an, Vorschlag 3 die Themen, unter denen sie stehen.
