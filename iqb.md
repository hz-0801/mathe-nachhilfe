# PROFIL IQB – Gemeinsame Abituraufgabenpools der Länder, Mathematik
Version 0.1 · 13.09.2026 · Kennung iqb · gilt mit Kern v0.3 (Schema-Version 2)

## 1 Prüfung

Der Aufgabenpool des IQB (Institut zur Qualitätsentwicklung im Bildungswesen)
für die schriftliche Abiturprüfung im Fach Mathematik. Die Länder entnehmen dem
Pool Aufgaben für ihre Prüfungen; welches Land welche Aufgabe genommen hat, ist
nicht erkennbar. Der Pool ist länderneutral, gliedert sich nach Anforderungsniveau
(grundlegend, erhöht), Prüfungsteil (A hilfsmittelfrei, B mit Hilfsmitteln) und
Sachgebiet (Analysis, Analytische Geometrie/Lineare Algebra in den Alternativen A1
und A2, Stochastik). Jede Aufgabe wird mit Erwartungshorizont, Standardbezug
(Zuordnung der Teilaufgaben zu den Kompetenzen K1–K6 und den
Anforderungsbereichen I–III) und Bewertungshinweisen veröffentlicht.

Rolle im Katalog: Der Pool ist Typenquelle und Eichmaß. Er liefert 624 gelöste
Aufgaben mit amtlichem Erwartungshorizont, wo die Landeshefte des Profils abi
keine Lösungen haben, und er eicht über den Standardbezug die Schätzung in
`niveau_geschaetzt`. Die Landeshefte bleiben das Formatmodell der Prüfung; der
Pool sagt nichts darüber, wie eine Prüfung zusammengestellt wird. Zusammengeführt
werden abi und iqb später über die Typen, nicht über die Dateien (konzept.md,
Entscheidung 23).

Sagt der Lehrer IQB, Pool oder Poolaufgabe, ist dieses Profil gemeint. Abi, GK, LK
meinen weiterhin das Profil abi.

Bestand: 624 Dateien, Sondierung 13.09.2026 (iqb-quellen.md). Erfasst wird
zuerst Prüfungsteil A vollständig (328 Dateien, 22 Stapel); Teil B liegt, bis
Teil A durch ist und die Kennzahlen stehen.

## 2 Ablage und Quellen

Basis-URL der Katalogdateien: https://raw.githubusercontent.com/hz-0801/mathe-nachhilfe/main/
(alle Dateien flach in der Wurzel; bei anderer Ablage nur diese Zeile ändern).
Katalogdateien dieses Profils: iqb-quellen.md, iqb-quellen.csv,
iqb-pruefungen.md, iqb-typen.csv, iqb-katalog.csv. Eine Katalogdatei wie bei abi;
das Feld `block` trennt Teil A und Teil B.

Aufgaben: https://www.iqb.hu-berlin.de/media/exercise_files/Abituraufgaben_Mathematik/<Kennung>_Aufgabe.pdf
Die Kennungen stehen vollständig in iqb-quellen.csv; geholt wird mit curl. Ein
zweiter Download je Aufgabe ist nicht nötig, die Datei enthält alles.

Gerüst für Erfassung und Prüfung: iqb-bau.py. Es liest Kopfzeile und
Formvokabular aus katalog-prompt.md § 5, Sachgebiete und Themen aus diesem
Profil § 5–6, die Stapelzuordnung aus iqb-quellen.csv, und schreibt die beiden
CSV-Dateien nur, wenn alle Prüfungen bestehen – einschließlich der
Schwellenwerte aus § 7.

Amtliche Lösungen liegen für jede Aufgabe vor. Es gilt Kern § 3 d in der Fassung
„amtliche Lösung vorhanden" wie im Profil fhr: der Erwartungshorizont ist
maßgeblich, eigene Rechnung ist Kontrolle, `ergebnis` trägt den Zusatz
„amtlich". Der Erwartungshorizont „stellt für jede Teilaufgabe eine mögliche
Lösung dar"; er ist ein Lösungsweg, keine Punkteaufteilung – die BE stehen nur je
Teilaufgabe.

Amtliche Vorgaben: die Prüfungsschwerpunkte der Länder (abi-vorgaben.md) und die
„Beschreibung der Struktur" des IQB. Dieses Profil liest sie nicht; die
Themenliste in § 6 ist die des Profils abi.

## 3 Aufbau der Dateien

Jede Datei ist eine Aufgabe mit vier Abschnitten: **1 Aufgabe** (Aufgabentext,
BE am rechten Rand je Teilaufgabe, Summe am Ende), **2 Erwartungshorizont** (je
Teilaufgabe ein Lösungsweg, BE wiederholt), **3 Standardbezug** (Tabelle
Teilaufgabe × BE × K1–K6, in den Zellen I, II oder III), **4 Bewertungshinweise**
(Standardtext). Vorweg eine Kurzbeschreibung mit Anforderungsniveau,
Prüfungsteil, Sachgebiet und – in Teil A – Aufgabengruppe, in Teil B dem digitalen
Hilfsmittel. Die Fußzeile trägt die Dokumentkennung mit Unterstrichen
(2026_M_grundlegend_A_Analysis_1_1); der Dateiname ist dieselbe Kennung ohne
Unterstriche.

**Teil A** (hilfsmittelfrei): zwei Seiten, zwei bis drei Teilaufgaben a, b, c,
meist 5 BE je Aufgabe. Aufgabengruppe 1 in den Anforderungsbereichen I und II,
Gruppe 2 mit mindestens einer Teilaufgabe im Bereich III (abi.md § 3). Je Jahr,
Niveau, Sachgebiet und Gruppe gibt es eine bis vier Aufgaben; bei genau einer
trägt der Dateiname keine Nummer (2017MerhoehtAAnalysis2).

**Teil B** (mit Hilfsmitteln): vier bis sechs Seiten, eine Datei je Sachgebiet
und Rechnerfassung (WTR, ab 2022 MMS, davor CAS), darin mehrere durchnummerierte
Aufgaben 1, 2, … mit je bis zu acht Teilaufgaben; sechs bis sechzehn
Teilaufgaben je Datei. Formeln liegen im PDF als Bilder, die Textextraktion
verschluckt sie – Rendern ist Pflicht (Kern § 3 b).

**Beispielaufgaben.** 47 Dateien ohne Jahr (Kennung beginnt mit
„Beispielaufgaben"), vom IQB vor dem ersten Pool 2017 veröffentlicht; gleicher
Aufbau. Sie werden nach den Jahrgängen erfasst.

**Rechnerfassungen** gibt es nur in Teil B. Teil A ist hilfsmittelfrei und
deshalb ohne CAS-Delta; das ist einer der Gründe, mit Teil A zu beginnen.

## 4 Kürzel und Werte

    Kennung: der Dateiname ohne „_Aufgabe.pdf", z. B. 2026MgrundlegendAAnalysis11.
            Aufbau: Jahr (oder „Beispielaufgaben"), M, Niveau (grundlegend |
            erhoeht), Prüfungsteil (A | B), Sachgebiet (Analysis | AGLAA1 |
            AGLAA2 | Stochastik), dann in Teil A Aufgabengruppe und, wenn die
            Gruppe mehrere Aufgaben hat, die Nummer (11, 12, 2); in Teil B das
            Hilfsmittel (WTR | CAS | MMS) und, wenn es mehrere Dateien gibt, die
            Nummer (WTR1, MMS2, WTR). Die Zerlegung ist eindeutig (iqb-quellen.csv).
    id:     Kennung-Teilaufgabe · 2026MgrundlegendAAnalysis11-a
            In Teil B zusätzlich die Aufgabennummer innerhalb der Datei:
            2026MgrundlegendBAnalysisWTR1-2a (vorläufig, wird vor Teil B
            bestätigt). Die Kennung ist der Rückweg ins Original: Kennung plus
            „_Aufgabe.pdf" ist die Datei. Die id ist umlautfrei („erhoeht" ist
            Schreibweise des IQB, keine Umschrift).
    jahr:   Pooljahr aus der Kennung; „bsp" für die Beispielaufgaben ohne Jahr.
            Auswertungen über das Jahr lassen „bsp" aus.
    papier: Jahr-iqb-Niveau · 2026-iqb-ga · 2026-iqb-ea · bsp-iqb-ga
            Niveau: ga grundlegend, ea erhöht (wie bb-ea im Profil abi).
            Teil B in der Rechnerfassung CAS/MMS: Zusatz -mms (2026-iqb-ga-mms),
            vorläufig, analog zu -cas im Profil abi.
    block:  A | B, der Prüfungsteil.
    aufgabe: Teil A: Aufgabengruppe, bei mehreren Aufgaben der Gruppe
            Gruppe.Nummer wie in der Kennung – 1.1, 1.2, 2. Nicht umnummerieren.
            Teil B (vorläufig): Dateinummer.Aufgabennummer, ohne Dateinummer nur
            die Aufgabennummer.
    titel:  das Sachgebiet der Kurzbeschreibung wörtlich: Analysis · AG/LA (A1) ·
            AG/LA (A2) · Stochastik. Die Aufgaben haben keine Überschrift; über
            titel bleibt die Alternative A1/A2 erkennbar, die leitidee nicht trägt.
    teilaufgabe: ein Kleinbuchstabe.
    seite:  Seite des Aufgabentexts im PDF (Teil A: 1, selten 1|2), nicht die
            Seite des Erwartungshorizonts.
    punkte: BE am rechten Rand der Teilaufgabe.
    stern:  leer. Das Niveau steht in papier.
    hilfsmittel: nein in block A, ja in block B.
    afb_amtlich: aus dem Standardbezug, Pflichtfeld in diesem Profil. Der
            Standardbezug ist eine Matrix Teilaufgabe × K1–K6; in den Zellen
            stehen I, II oder III, leere Zellen bedeuten „Kompetenz nicht
            angesprochen". Das Feld trägt alle vorkommenden Bereiche der
            Teilaufgabe, aufsteigend, ohne Wiederholung, mit „|" getrennt:
            I · I|II · II|III · I|II|III. Nicht nur den höchsten – das Feld hält
            fest, was amtlich ausgewiesen ist, eine Auswahl wäre Deutung. Die
            Matrixzeile mit der Zuordnung zu K1–K6 steht wörtlich in bemerkung
            („Standardbezug: K1 I, K2 II, K5 II").
    niveau_geschaetzt: eigene Schätzung nach Kern § 5, aus dem Aufgabentext
            gebildet, nicht aus dem Standardbezug abgeschrieben – sonst eicht
            das Feld nichts. Eichung (Auswertungsregel, keine Erfassungsregel):
            verglichen wird mit dem höchsten Bereich in afb_amtlich, weil das
            Feld einwertig ist und die Teilaufgabe insgesamt meint. iqb-bau.py
            gibt die Trefferquote je Lauf aus.
    ergebnis: amtliches Ergebnis aus dem Erwartungshorizont mit Zusatz
            „(amtlich)"; weicht die eigene Rechnung ab, bleibt das amtliche in
            ergebnis und die Abweichung geht nach bemerkung. Ergebnisse zu
            Zeigen, Begründen, Angeben als erwartete Antwort in eigenen Worten.
    bemerkung: enthält immer den Standardbezug (siehe afb_amtlich). Passt kein
            Thema der Liste, trägt bemerkung das Wort „ersatzweise" mit dem
            gewählten Thema – iqb-bau.py zählt diese Zeilen (§ 7).

Schreibweisen wie im Profil fhr: Potenzen mit ^, Ableitungen f'(x), f''(x),
Koordinaten P(x; y) und P(x; y; z) mit Semikolon, Vektoren als (1; 0; 0), „|"
trennt nur Mehrfachwerte. Intervalle als −3 <= x <= 3. Unicode-Minus „−",
Malpunkt „·", Wurzel als √. Dezimalkomma wie in der Aufgabe; der Pool schreibt
Brüche und Wurzeln exakt (2√5), der Katalog übernimmt das.

## 5 Sachgebiete

Feld `leitidee` trägt das Sachgebiet: **Analysis · Analytische Geometrie ·
Stochastik**.

Dieselben drei Werte wie im Profil abi, damit die Typen später zusammengeführt
werden können. Die Alternativen A1 und A2 des IQB-Sachgebiets „Analytische
Geometrie/Lineare Algebra" gehen beide nach Analytische Geometrie; die
Alternative steht in titel. A1 ist Vektorgeometrie ohne Ebenen, mit Matrizen und
Übergangsprozessen; A2 ist die Geometrie mit Geraden, Ebenen, Lagebeziehungen
und Abständen, wie sie Berlin und Brandenburg prüfen.

## 6 Themenliste

Übernommen aus abi.md § 6 (Prüfungsschwerpunkte Brandenburg 2027, Rahmenlehrplan
GOST), ergänzt um ein Thema für die Alternative A1. Feste Ebene zwischen
Sachgebiet und Typ; Ergänzungen nur über den Bericht. Bei Änderung in abi.md hier
mitziehen, damit die Typen zusammenführbar bleiben.

**Analysis:** Gleichungen lösen · Lineare Gleichungssysteme · Funktionsklassen und
Eigenschaften · Umkehrfunktion · Grenzwerte und Verhalten im Unendlichen ·
Ableitung und Änderungsrate · Ableitungsregeln · Tangente, Normale, Schnittwinkel ·
Kurvenuntersuchung · Ableitungsgraph und Funktionsgraph · Funktionsscharen und
Ortskurven · Rekonstruktion von Funktionsgleichungen · Extremalprobleme ·
Stammfunktion und Hauptsatz · Integrationsregeln · Flächeninhalt durch Integration ·
Rekonstruktion von Beständen · Uneigentliche Integrale · Rotationsvolumen

**Analytische Geometrie:** Punkte und Strecken im Koordinatensystem · Vektoren und
Rechenoperationen · Linearkombination und lineare Abhängigkeit · Geraden · Ebenen ·
Lagebeziehungen · Schnittmengen · Skalarprodukt und Winkel · Orthogonalität ·
Abstände · Flächeninhalt und Volumen im Raum · Scharen von Geraden und Ebenen ·
Spiegelung · Matrizen und Übergangsprozesse

**Stochastik:** Ereignisse und Mengenoperationen · Zufallsexperimente und
Urnenmodelle · Kombinatorik · Baumdiagramm und Pfadregeln · Vierfeldertafel ·
Bedingte Wahrscheinlichkeit und Bayes · Unabhängigkeit · Lage- und Streumaße einer
Stichprobe · Zufallsgrößen und Verteilungen · Binomialverteilung · Kenngrößen von
Verteilungen · Hypergeometrische Verteilung · Normalverteilung und Sigma-Regeln ·
Hypothesentests

Nur auf erhöhtem Niveau (abi.md § 6): Uneigentliche Integrale, Rotationsvolumen,
Funktionsscharen und Ortskurven, Scharen von Geraden und Ebenen,
Normalverteilung und Sigma-Regeln, Hypothesentests. Im Pool kann Erhöhtes auch
auf grundlegendem Niveau vorkommen, weil der Pool für alle Länder gilt; die
Markierung ist die der Berlin-Brandenburger Schwerpunkte, kein Filter beim
Erfassen.

**Matrizen und Übergangsprozesse** ist eine Zutat dieses Profils: nur in der
Alternative A1, in Berlin und Brandenburg nicht Prüfungsgegenstand. Die
Aufgaben werden trotzdem erfasst (der Pool ist Typenquelle, Kern § 6:
ein Vorkommen ist ein vollwertiger Typ); gefiltert wird über das Thema.

Nicht erfasst werden – wie in abi.md § 6 – Teilaufgaben, deren einzige Leistung
das Erläutern oder Entwickeln eines Beweises (K1 im engen Sinn) oder eine
Simulation ist. Bisher keine Fundstelle; die Regel wird beim ersten Fall geprüft.

**Bekannte Lücken** werden hier wie in abi.md § 6 gesammelt: nächstliegendes
Thema wählen, „ersatzweise" in bemerkung, Entscheidung nach mehreren Stapeln.
Stand v0.1: keine.

## 7 Besonderheiten beim Erfassen

- **Ein Stapel je Lauf.** Die Regel „ein Heft je Lauf" aus CLAUDE.md § 3 gilt
  für Hefte; eine Poolaufgabe ist kein Heft. Die Einheit ist der Stapel: alle
  Aufgaben eines Prüfungsteils, eines Pooljahrs und eines Niveaus (Spalte
  `stapel` in iqb-quellen.csv, z. B. 2026-ga-A mit 19 Dateien). Teil A hat 22
  Stapel zu 10 bis 20 Dateien, also 25 bis 50 Zeilen – der Umfang eines
  Landeshefts. Ein Lauf erfasst genau einen Stapel vollständig; iqb-bau.py
  prüft gegen iqb-quellen.csv, dass keine Datei des Stapels fehlt. Kein halber
  Stapel, keine Zwischenstände, ein Commit je Stapel. Reihenfolge: vom jüngsten
  Pooljahr zum ältesten, je Jahr grundlegend vor erhöht, die Beispielaufgaben
  zuletzt; innerhalb des Stapels Analysis, AG/LA (A1), AG/LA (A2), Stochastik.
- **Qualitätsschranke im Skript, nicht im Urteil des Lehrers.** Der Lehrer liest
  keine Berichte und entscheidet nicht im Lauf. iqb-bau.py bricht deshalb ab,
  wenn ein Schwellenwert gerissen wird; die Werte stehen in SCHWELLEN im Skript
  und sind revidierbar:
  · Zeilen mit „?": höchstens 10 % der Zeilen des Stapels, mindestens 2 erlaubt.
  · Neue Typen: höchstens 60 % der im Stapel verwendeten Typen, sobald der
    Katalog 100 Zeilen hat (davor ist fast jeder Typ neu).
  · Zeilen mit „ersatzweise" (kein passendes Thema): höchstens 10 % der Zeilen,
    mindestens 2 erlaubt.
  Reißt eine Schranke, ist der Stapel nicht schlecht, sondern die Etiketten sind
  zu prüfen: Typen gegen den Bestand abgleichen, Themen erneut zuordnen,
  Unsicheres nachrechnen – und dann erneut laufen lassen. Erst wenn das nicht
  hilft, wird der Schwellenwert im Skript geändert und die Änderung in
  iqb-pruefungen.md § 5 begründet.
- **Abgleichlauf nach jedem Stapel** (Kern § 9, „abgleich"): die Etiketten des
  Stapels gegen iqb-typen.csv vereinheitlichen, anhand von gegeben, gesucht,
  verfahren, stichwoerter. Ergebnis als Liste alt → neu in iqb-pruefungen.md § 5.
- **Standardbezug vor Erwartungshorizont lesen? Nein.** Reihenfolge beim
  Erfassen: Aufgabe lesen, niveau_geschaetzt festlegen, dann Erwartungshorizont
  und Standardbezug. Die Schätzung wird nicht nachträglich an den Standardbezug
  angepasst; eine Abweichung ist ein Messwert, kein Fehler.
- **Kein Aufgabenstamm im engen Sinn**, aber Text vor a) ist der Normalfall
  („Der Graph der in IR definierten Funktion f mit … wird mit G bezeichnet").
  Jede Zeile wiederholt in gegeben, was sie davon braucht (Kern § 4).
  Voraussetzungen wie „G ist symmetrisch zum Koordinatenursprung" aus der
  Teilaufgabe selbst gehören ebenfalls nach gegeben.
- **Mehrere Leistungen** in einer Teilaufgabe bleiben eine Zeile: typ die erste,
  typ_neben die weiteren, format und operator alle (Kern § 4).
- **Angeben ohne Rechnung** („Geben Sie … an") ist in Teil A häufig: format
  Kurzantwort, antwort Zahl oder Term, schritte 0 oder 1. Nachweise („Weisen
  Sie nach", „Zeigen Sie", „Begründen Sie") sind format Begründung mit antwort
  Text, auch wenn gerechnet wird; die Rechnung steht in verfahren.
- **Abbildungen** (Würfelnetze, Graphen, Schrägbilder) gehören nach material
  und skizze so genau, dass sie nachgezeichnet werden können; Werte, die nur
  im Bild stehen, nach gegeben. Formeln im Aufgabentext sind ebenfalls Bilder
  und nur im gerenderten PDF lesbar.
- **Amtliche Ergebnisse** übernehmen, eigene Rechnung mit sympy als Kontrolle;
  Rundungen und Näherungen wie im Erwartungshorizont („≈", exakte Werte mit
  Wurzeln). Der Erwartungshorizont ist nur ein möglicher Weg; verfahren darf
  einen anderen, für Schüler üblichen Weg beschreiben, das Ergebnis bleibt.
- **Kontext:** in Teil A überwiegend „ohne"; Sachkontexte (Atmung, Würfelspiel)
  kurz wie im Kern.

## 8 Beispielzeilen

Die zwei Zeilen der Probeerfassung an 2026MgrundlegendAAnalysis11 (zwei
Teilaufgaben, 5 BE), zur Lesbarkeit als Feld = Wert; in iqb-katalog.csv stehen
dieselben Werte als eine Zeile in der Reihenfolge der Kopfzeile.

    id = 2026MgrundlegendAAnalysis11-a · jahr = 2026 · papier = 2026-iqb-ga · block = A · aufgabe = 1.1 · titel = Analysis · teilaufgabe = a · seite = 1
    punkte = 2 · stern =  · hilfsmittel = nein · afb_amtlich = I
    leitidee = Analysis · thema = Kurvenuntersuchung · typ = Hochpunkt an vorgegebener Stelle nachweisen · typ_neben =  · stichwoerter = ganzrationale Funktion dritten Grades|notwendige Bedingung|hinreichende Bedingung|zweite Ableitung · voraussetzungen = Potenzregel anwenden|Vorzeichen der zweiten Ableitung deuten
    format = Begründung · operator = Weisen Sie nach · antwort = Text
    material = keins · skizze = keine · kontext = ohne · textumfang = kurz
    gegeben = f(x) = x^3 − 3x, definiert in IR; Graph G · gesucht = Nachweis, dass G einen Hochpunkt mit der x-Koordinate −1 hat · verfahren = erste und zweite Ableitung bilden, f'(−1) = 0 und f''(−1) < 0 zeigen · schritte = 3 · zahlenraum = ganz|negativ|Potenz · einheiten =  · abhaengig_von = 
    ergebnis = f'(x) = 3x^2 − 3, f''(x) = 6x; f'(−1) = 0 und f''(−1) = −6 < 0, also Hochpunkt bei x = −1 (amtlich) · zwischenergebnis = f'(x) = 3x^2 − 3|f''(x) = 6x
    niveau_geschaetzt = I · fehlerquelle = nur f'(−1) = 0 zeigen und die hinreichende Bedingung weglassen · bemerkung = Standardbezug: K1 I, K2 I, K5 I. Amtlich, eigene Rechnung bestätigt.

    id = 2026MgrundlegendAAnalysis11-b · jahr = 2026 · papier = 2026-iqb-ga · block = A · aufgabe = 1.1 · titel = Analysis · teilaufgabe = b · seite = 1
    punkte = 3 · stern =  · hilfsmittel = nein · afb_amtlich = I|II
    leitidee = Analysis · thema = Kurvenuntersuchung · typ = Abstand zweier Extrempunkte über die Punktsymmetrie berechnen · typ_neben =  · stichwoerter = Punktsymmetrie zum Ursprung|Hochpunkt|Tiefpunkt|Abstand zweier Punkte · voraussetzungen = Funktionswert berechnen|Abstand zweier Punkte mit dem Satz des Pythagoras|Punktsymmetrie nutzen
    format = Rechnung · operator = Berechnen Sie · antwort = Zahl
    material = keins · skizze = keine · kontext = ohne · textumfang = kurz
    gegeben = f(x) = x^3 − 3x, definiert in IR; Graph G; G ist symmetrisch zum Koordinatenursprung; G hat einen Hochpunkt mit der x-Koordinate −1 · gesucht = Abstand zwischen Hoch- und Tiefpunkt von G · verfahren = f(−1) = 2 berechnen, Hochpunkt H(−1; 2); wegen der Punktsymmetrie ist der Tiefpunkt T(1; −2); Abstand als Länge der Strecke HT, gleich dem Doppelten des Abstands von H zum Ursprung · schritte = 3 · zahlenraum = ganz|negativ|Wurzel · einheiten =  · abhaengig_von = 2026MgrundlegendAAnalysis11-a
    ergebnis = 2 · √((−1)^2 + 2^2) = 2√5 (amtlich) · zwischenergebnis = f(−1) = 2|H(−1; 2)|T(1; −2)
    niveau_geschaetzt = II · fehlerquelle = den Tiefpunkt neu über die Ableitung berechnen statt die Symmetrie zu nutzen, oder nur den Abstand von H zum Ursprung angeben · bemerkung = Standardbezug: K2 II, K4 I, K5 II. Amtlich, eigene Rechnung bestätigt: 2√5 ≈ 4,47.

Beide Zeilen stehen so in iqb-katalog.csv; dieser Abschnitt wird aus dem
Katalog übernommen und weicht nicht von ihm ab.

## 9 Offene Punkte

- Teil B: Kürzel (papier-Zusatz -mms, aufgabe Dateinummer.Aufgabennummer, id mit
  Aufgabennummer) sind vorläufig festgelegt und werden bestätigt, wenn Teil A
  durch ist. Offen ist auch, ob WTR- und MMS-Fassung wie bei abi als
  Leitfassung plus Nachtrag behandelt werden.
- Beispielaufgaben: Veröffentlichungsjahr nicht ermittelt; jahr = „bsp".
- Schwellenwerte in § 7 sind Vorschläge des ersten Laufs; nach drei Stapeln
  prüfen.
- Eichung: Die Trefferquote niveau_geschaetzt gegen den höchsten amtlichen
  Bereich wird je Stapel in iqb-pruefungen.md notiert. Erst ab mehreren
  Stapeln entscheiden, ob die Schätzregel in Kern § 5 (I reproduzieren, II
  Zusammenhänge herstellen, III verallgemeinern und reflektieren) für das
  Abitur nachjustiert werden muss – die Änderung wäre dann eine am Kern.
- Zusammenführung mit abi über die Typen: Verfahren offen (gemeinsamer
  Abgleichlauf über beide Typenlisten?). Bis dahin wächst iqb-typen.csv
  eigenständig; gleiche Fertigkeiten sollen nach Möglichkeit das Etikett aus
  abi-typen.csv tragen – beim Anlegen eines Typs dort nachsehen.
- Aufgabengruppe (1 oder 2) steht nur in aufgabe; ob sie als Merkmal für den
  Blattbau reicht, zeigt die Heft-Phase.
