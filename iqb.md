# PROFIL IQB – Gemeinsame Abituraufgabenpools der Länder, Mathematik
Version 0.4 · 13.09.2026 · Kennung iqb · gilt mit Kern v0.3 (Schema-Version 2)
Änderungen gegenüber 0.3: § 6 Geltungstabelle Thema × (be-gk, be-lk, bb-gk,
bb-ea) aus den Prüfungsschwerpunkten 2027; § 7 Schranke für neue Typen
deaktiviert, Eichschranke 85 % nach der engen Fassung.
Änderungen gegenüber 0.2 (nach den Stapeln 2026-ea-A und 2025-ga-A): § 7
Erfassungshinweis auf die enge Fassung „Kombinieren mit Deutung heißt III"
umgestellt, mit der Messung; § 7 Dubletten-Fassungsregel, Kennzahlen je Stapel.
Änderungen gegenüber 0.1 (nach dem Stapel 2026-ga-A): § 4 ungegliederte Aufgaben
(teilaufgabe leer, id gleich Kennung) und titel bei Kurzbeschreibung „AG/LA";
§ 6 Lineare Gleichungssysteme auch unter Analytische Geometrie; § 7 Dubletten;
§ 8 Beispielzeilen aus dem Katalog; § 2 iqb-quellen.py.

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
Profil § 5–6, die Stapelzuordnung, Seitenzahlen und Dubletten aus
iqb-quellen.csv, und schreibt die beiden CSV-Dateien nur, wenn alle Prüfungen
bestehen – einschließlich der Schwellenwerte aus § 7. iqb-quellen.py erzeugt
iqb-quellen.csv aus der Übersichtsseite des IQB und dem Scan der Teil-A-Dateien.

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
            Aufgaben ohne Teilaufgabenbuchstaben (in Gruppe 2 häufig: eine
            Aufgabe, 5 BE) sind nach Kern § 4 eine Zeile; teilaufgabe bleibt
            leer und die id ist die Kennung allein: 2026MgrundlegendAAGLAA12.
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
    titel:  das Sachgebiet nach der Kennung, in der Schreibweise der
            Kurzbeschreibung: Analysis · AG/LA (A1) · AG/LA (A2) · Stochastik.
            Die Aufgaben haben keine Überschrift; über titel bleibt die
            Alternative A1/A2 erkennbar, die leitidee nicht trägt. Aufgaben, die
            für beide Alternativen taugen, nennen in der Kurzbeschreibung nur
            „AG/LA"; titel folgt dann der Kennung (Ablage unter A1 oder A2),
            der Befund steht in bemerkung.
    teilaufgabe: ein Kleinbuchstabe; leer bei Aufgaben ohne Gliederung.
    seite:  Seite des Aufgabentexts im PDF (Teil A: 1, selten 1|2), nicht die
            Seite des Erwartungshorizonts. Die Seitenzahl der Datei steht in
            iqb-quellen.csv (Teil A meist 2, 16 Dateien haben 3).
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
            das Feld nichts. Erfassungshinweis aus der Eichung siehe § 7
            („Kombinieren mit Deutung heißt III"). Eichung (Auswertungsregel, keine
            Erfassungsregel): verglichen wird mit dem höchsten Bereich in
            afb_amtlich, weil das Feld einwertig ist und die Teilaufgabe
            insgesamt meint. iqb-bau.py gibt die Trefferquote je Lauf aus.
            Die Beispielaufgaben erklären die Matrix in einer Fußnote: „Für jede
            Kompetenz, die bei der Bearbeitung der Teilaufgabe eine wesentliche
            Rolle spielt, ist der Anforderungsbereich eingetragen, in dem die
            Kompetenz benötigt wird."
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
Spiegelung · Lineare Gleichungssysteme · Matrizen und Übergangsprozesse

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

**Lineare Gleichungssysteme** steht in beiden Listen. abi.md § 5 führt sie nach
den Prüfungsschwerpunkten unter Analysis; der Pool stellt reine LGS-Aufgaben
unter AG/LA (2026MgrundlegendAAGLAA12). Weil leitidee das Sachgebiet der
Kurzbeschreibung trägt und nicht umsortiert wird, braucht die Liste Analytische
Geometrie das Thema ebenfalls. Typen zu LGS werden je Sachgebiet geführt; beim
Abgleich ist zu prüfen, ob dieselbe Fertigkeit unter beiden steht.

**Geltungstabelle.** Ob ein Thema Prüfungsgegenstand ist, hängt von Land und
Niveau ab. Quelle sind die vier Prüfungsschwerpunkte 2027 (Berlin
ps_mathematik_2027_gk/lk, Brandenburg PS_Mathematik_GK/LK_2027; gelesen am
13.09.2026, Ablage in abi-vorgaben.md § 1). ja = in den Schwerpunkten genannt,
nein = nicht genannt. iqb-bau.py liest die Tabelle und zählt je Stapel die
Zeilen, deren Thema für eine Zielprüfung nicht gilt; gefiltert wird über das
Thema, ein Zeilenfeld gibt es dafür nicht (Geltung ist eine Eigenschaft des
Themas, nicht der Zeile). Jedes Thema der Liste braucht eine Zeile.

| Thema | be-gk | be-lk | bb-gk | bb-ea |
|---|---|---|---|---|
| Gleichungen lösen | ja | ja | ja | ja |
| Lineare Gleichungssysteme | ja | ja | ja | ja |
| Funktionsklassen und Eigenschaften | ja | ja | ja | ja |
| Umkehrfunktion | ja | ja | ja | ja |
| Grenzwerte und Verhalten im Unendlichen | ja | ja | ja | ja |
| Ableitung und Änderungsrate | ja | ja | ja | ja |
| Ableitungsregeln | ja | ja | ja | ja |
| Tangente, Normale, Schnittwinkel | ja | ja | ja | ja |
| Kurvenuntersuchung | ja | ja | ja | ja |
| Ableitungsgraph und Funktionsgraph | ja | ja | ja | ja |
| Funktionsscharen und Ortskurven | nein | ja | nein | ja |
| Rekonstruktion von Funktionsgleichungen | ja | ja | ja | ja |
| Extremalprobleme | ja | ja | ja | ja |
| Stammfunktion und Hauptsatz | ja | ja | ja | ja |
| Integrationsregeln | ja | ja | ja | ja |
| Flächeninhalt durch Integration | ja | ja | ja | ja |
| Rekonstruktion von Beständen | ja | ja | ja | ja |
| Uneigentliche Integrale | nein | ja | nein | ja |
| Rotationsvolumen | nein | ja | nein | ja |
| Punkte und Strecken im Koordinatensystem | ja | ja | ja | ja |
| Vektoren und Rechenoperationen | ja | ja | ja | ja |
| Linearkombination und lineare Abhängigkeit | ja | ja | ja | ja |
| Geraden | ja | ja | ja | ja |
| Ebenen | ja | ja | ja | ja |
| Lagebeziehungen | ja | ja | ja | ja |
| Schnittmengen | ja | ja | ja | ja |
| Skalarprodukt und Winkel | ja | ja | ja | ja |
| Orthogonalität | ja | ja | ja | ja |
| Abstände | ja | ja | ja | ja |
| Flächeninhalt und Volumen im Raum | ja | ja | ja | ja |
| Scharen von Geraden und Ebenen | nein | ja | nein | ja |
| Spiegelung | ja | ja | ja | ja |
| Matrizen und Übergangsprozesse | nein | nein | nein | nein |
| Ereignisse und Mengenoperationen | ja | ja | ja | ja |
| Zufallsexperimente und Urnenmodelle | ja | ja | ja | ja |
| Kombinatorik | ja | ja | ja | ja |
| Baumdiagramm und Pfadregeln | ja | ja | ja | ja |
| Vierfeldertafel | ja | ja | ja | ja |
| Bedingte Wahrscheinlichkeit und Bayes | ja | ja | ja | ja |
| Unabhängigkeit | ja | ja | ja | ja |
| Lage- und Streumaße einer Stichprobe | ja | ja | ja | ja |
| Zufallsgrößen und Verteilungen | ja | ja | ja | ja |
| Binomialverteilung | ja | ja | ja | ja |
| Kenngrößen von Verteilungen | ja | ja | ja | ja |
| Hypergeometrische Verteilung | nein | nein | ja | ja |
| Normalverteilung und Sigma-Regeln | nein | ja | nein | ja |
| Hypothesentests | nein | ja | nein | ja |

Anmerkungen zur Tabelle: Abstände gelten in Berlin nur über Lotfußpunkte,
Abstandsformeln und Hessesche Normalenform sind dort „nicht notwendig"; der
Abstand Punkt–Gerade und windschiefer Geraden steht nur in den LK-Papieren.
Bedingte Wahrscheinlichkeit gilt überall, der Satz von Bayes und das
Axiomensystem von Kolmogorow nur in Brandenburg. Berlin führt statt der
hypergeometrischen Verteilung das „Lotto-Modell" (Ziehen ohne Zurücklegen
über Urnenmodelle); Aufgaben mit Binomialkoeffizienten-Quotienten sind dort
also nicht ausgeschlossen, die Verteilung als Begriff schon – die Tabelle
folgt dem Wortlaut. Berlin verlangt zusätzlich Wurzelgleichungen (GK
„grundlegend", LK) und die Sachkontexte Geschwindigkeit–Weg, Masse–Volumen–
Dichte, Zeit–Uhrzeit, die in der Themenliste keine eigenen Themen haben.
Kettenregel im Berliner GK nur mit linearer innerer Funktion, in Brandenburg
auch quadratisch. Sinus- und Kosinusfunktionen: Ableitung nur bb-gk, bb-ea und
be-lk; be-gk nur die Sek-I-Form. Matrizen sind in keinem der vier Papiere
Prüfungsgegenstand (das Wort fällt nur bei der MMS-Zulassung).

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
  · Neue Typen: Schranke deaktiviert (13.09.2026). Nach drei Stapeln lag der
    Anteil neuer Typen bei 100, 82 und 94 % – die geplanten 60 % hätten jeden
    weiteren Stapel abgebrochen, ohne dass etwas faul ist. Gemessen wird der
    Anteil weiter (Kennzahlen); eine neue Schranke wird erst gesetzt, wenn der
    Typenschnitt für Teil A entschieden ist (iqb-pruefungen.md § 4).
  · Eichung: mindestens 85 % der Zeilen treffen nach der engen Fassung den
    höchsten amtlichen Bereich (ab 10 Zeilen im Stapel scharf).
  · Zeilen mit „ersatzweise" (kein passendes Thema): höchstens 10 % der Zeilen,
    mindestens 2 erlaubt.
  Reißt eine Schranke, ist der Stapel nicht schlecht, sondern die Etiketten sind
  zu prüfen: Typen gegen den Bestand abgleichen, Themen erneut zuordnen,
  Unsicheres nachrechnen – und dann erneut laufen lassen. Erst wenn das nicht
  hilft, wird der Schwellenwert im Skript geändert und die Änderung in
  iqb-pruefungen.md § 5 begründet. Die Werte sind vorerst Schätzung. Der Bericht
  jedes Stapels nennt als **Kennzahlen** die Quote neuer Typen an den
  verwendeten und die Eichtrefferquote (Zeile „Kennzahlen:" von iqb-bau.py, in
  iqb-pruefungen.md § 4 gesammelt); nach drei Stapeln werden Schwellenwerte
  vorgeschlagen, die aus den gemessenen Quoten folgen.
- **Dubletten.** Aufgaben, die für beide AG/LA-Alternativen taugen, liegen im
  Pool zweimal, wortgleich unter A1 und unter A2 (Teil A: 15 Paare, alle AG/LA,
  Scan vom 13.09.2026). Dublette heißt: Aufgabe, Erwartungshorizont **und**
  Standardbezug sind gleich – iqb-quellen.py vergleicht alle drei Abschnitte
  ohne Leerraum (ein Paar unterschied sich nur in „1: 3" gegen „1:3"); bei
  allen 15 Paaren sind auch die Formelbilder gleich, geprüft über die
  Bildobjekte, bei einem Paar nur anders kodiert. Stimmt bei gleicher Aufgabe
  Erwartungshorizont oder Standardbezug nicht überein, ist das keine Dublette,
  sondern eine eigene Fassung: sie bekommt eine eigene Zeile und teilt nur den
  Typ; das Skript meldet solche Fälle und markiert sie nicht (bisher keiner).
  Die Spalte dublette_von in iqb-quellen.csv nennt für die zweite Datei die
  erste (Ordnung nach § 7); Dubletten bekommen keine Zeile und kein Soll,
  iqb-bau.py verlangt sie nicht und weist sie ab. Der Befund steht in
  bemerkung der ersten Datei. Ein Stapel zählt deshalb nach Dateien ohne
  Dubletten (2026-ga-A: 19 Dateien, 18 erfasst).
- **Abgleichlauf nach jedem Stapel** (Kern § 9, „abgleich"): die Etiketten des
  Stapels gegen iqb-typen.csv vereinheitlichen, anhand von gegeben, gesucht,
  verfahren, stichwoerter. Ergebnis als Liste alt → neu in iqb-pruefungen.md § 5.
- **Standardbezug vor Erwartungshorizont lesen? Nein.** Reihenfolge beim
  Erfassen: Aufgabe lesen, niveau_geschaetzt festlegen, dann Erwartungshorizont
  und Standardbezug. Die Schätzung wird nicht nachträglich an den Standardbezug
  angepasst; eine Abweichung ist ein Messwert, kein Fehler.
- **Kombinieren mit Deutung heißt III** (Erfassungshinweis aus der Eichung,
  enge Fassung; Entscheidung nach dem Stapel 2025-ga-A, 13.09.2026). Der
  amtliche Standardbezug setzt III, wo eine Teilaufgabe mehrere Regeln oder
  Verfahren verkettet **und** dabei eine Deutung oder Fallunterscheidung
  verlangt: eine Bedingung aus dem Sachverhalt oder der Geometrie erst in eine
  Gleichung übersetzen (Flächenhalbierung als Integral gleich null, Abstand zum
  Spiegelbild als doppelter Abstand zur Ebene, faires Spiel als Erwartungswert
  gleich Einsatz), eine Aussage beurteilen, eine Symmetrie oder einen
  Sonderfall erkennen und ausnutzen. Reine Verkettungen von Standardschritten
  bleiben II: Ableitung bilden und eine Bruchgleichung lösen, Schnittstelle und
  Steigungen und Winkelbedingung, μ und σ berechnen und im Diagramm ablesen,
  Mittelpunkt und Höhe und Fläche. I bleibt die einzelne Beobachtung oder
  Rechnung, auch wenn sie begründet wird (Graph der Funktion vom
  Ableitungsgraphen unterscheiden: geschätzt II, amtlich I).
  Messung, die zur engen Fassung geführt hat (Treffer der Schätzung gegen den
  höchsten amtlichen Bereich): 2026-ga-A 30 von 33 in beiden Fassungen;
  2026-ea-A weit 34, eng 36 von 37 (Analysis 1.1 b und Stochastik 1.1 b sind
  Routineverkettungen mit amtlich II); 2025-ga-A weit 29, eng 30 von 31 (die
  weite Fassung überschätzt AGLAA11 und AGLAA212-b, die enge unterschätzt nur
  Analysis 2.2 a, wo der Standardbezug die Bruchgleichung mit K5 III belegt).
  Erster Stapel nach der engen Fassung als Regel: 2025-ea-A 30 von 34; die
  Fairnessdeutung (Stochastik 1.1 b) ist dort amtlich nur II, die algebraische
  Verkettung mit Ersatz n · p = E (Stochastik 2.1) amtlich III.
  Die weite Fassung „Kombinieren heißt III" (Stand nach 2026-ga-A) hatte die
  Verkettung allein zum Maß gemacht; sie trifft die amtlich mit III belegten
  Zeilen ebenso, überschätzt aber Routineverkettungen. Im Katalog tragen die
  Zeilen von 2026-ea-A und 2025-ga-A die Schätzung der jeweils geltenden
  Fassung; wo die enge Fassung abweicht, steht sie in bemerkung („Schätzung enge
  Fassung: II").
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

Vier Zeilen aus dem Stapel 2026-ga-A, zur Lesbarkeit als Feld = Wert; in
iqb-katalog.csv stehen dieselben Werte als eine Zeile in der Reihenfolge der
Kopfzeile. Gewählt sind die beiden Zeilen der Probeaufgabe, eine ungegliederte
Aufgabe (5 BE, teilaufgabe leer, id gleich Kennung) und eine Stochastik-Zeile
mit Baumdiagramm. Dieser Abschnitt wird aus dem Katalog erzeugt und weicht
deshalb nicht von ihm ab.

﻿    id = 2026MgrundlegendAAnalysis11-a · jahr = 2026 · papier = 2026-iqb-ga · block = A · aufgabe = 1.1 · titel = Analysis · teilaufgabe = a · seite = 1
    punkte = 2 · stern =  · hilfsmittel = nein · afb_amtlich = I
    leitidee = Analysis · thema = Kurvenuntersuchung · typ = Extrempunkt an vorgegebener Stelle nachweisen · typ_neben =  · stichwoerter = ganzrationale Funktion dritten Grades|notwendige Bedingung|hinreichende Bedingung|zweite Ableitung · voraussetzungen = Potenzregel anwenden|Vorzeichen der zweiten Ableitung deuten
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

    id = 2026MgrundlegendAAGLAA12 · jahr = 2026 · papier = 2026-iqb-ga · block = A · aufgabe = 2 · titel = AG/LA (A1) · teilaufgabe =  · seite = 1
    punkte = 5 · stern =  · hilfsmittel = nein · afb_amtlich = II|III
    leitidee = Analytische Geometrie · thema = Lineare Gleichungssysteme · typ = Lösung eines unterbestimmten Gleichungssystems unter Zusatzbedingungen auswählen · typ_neben =  · stichwoerter = LGS mit drei Unbekannten|Gleichungen II und III Vielfache|Lösungsschar mit Parameter|negativ und ganzzahlig|größtes y · voraussetzungen = abhängige Gleichungen erkennen|Lösungsmenge mit Parameter angeben|Bedingungen an den Parameter übersetzen
    format = Rechnung · operator = Bestimmen Sie · antwort = Zahl
    material = keins · skizze = keine · kontext = ohne · textumfang = mittel
    gegeben = lineares Gleichungssystem I: −4x + z = 4, II: 2y − z = 4, III: 4y − 2z = 8; betrachtet werden nur Lösungen (x; y; z), bei denen x, y und z negativ und ganzzahlig sind · gesucht = die Lösung mit dem größten Wert für y · verfahren = II und III sind Vielfache, das System hat unendlich viele Lösungen; mit z = t folgt x = t/4 − 1 und y = t/2 + 2; alle drei negativ heißt t < −4, ganzzahlig heißt t Vielfaches von 4; größtes y bei t = −8 · schritte = 4 · zahlenraum = ganz|negativ|Bruch · einheiten =  · abhaengig_von = 
    ergebnis = (−3; −2; −8) (amtlich) · zwischenergebnis = allgemeine Lösung (t/4 − 1; t/2 + 2; t) mit t aus IR|Bedingung t < −4 und t Vielfaches von 4
    niveau_geschaetzt = III · fehlerquelle = das System für eindeutig lösbar halten oder die Ganzzahligkeit von x übersehen und t = −6 nehmen · bemerkung = Standardbezug: K1 III, K2 II, K5 III, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben, eine Zeile mit 5 BE. Lineare Gleichungssysteme stehen im Pool unter AG/LA, in der Themenliste deshalb auch unter Analytische Geometrie (iqb.md § 6).

    id = 2026MgrundlegendAStochastik13-b · jahr = 2026 · papier = 2026-iqb-ga · block = A · aufgabe = 1.3 · titel = Stochastik · teilaufgabe = b · seite = 1
    punkte = 2 · stern =  · hilfsmittel = nein · afb_amtlich = I|II
    leitidee = Stochastik · thema = Bedingte Wahrscheinlichkeit und Bayes · typ = Bedingte Wahrscheinlichkeit aus dem Baumdiagramm mit einer Schranke vergleichen · typ_neben =  · stichwoerter = bedingte Wahrscheinlichkeit|Bedingung verspätet|0,18/(0,08 + 0,18)|größer als 50 % · voraussetzungen = Bedingung als Nenner aus zwei Pfaden zusammensetzen
    format = Rechnung · operator = Untersuchen Sie · antwort = Zahl|Text
    material = Diagramm · skizze = zweistufiges Baumdiagramm: erste Stufe A (40 %) und A quer, zweite Stufe je V und V quer; am Ast A–V steht x, am Ende 8 %; am Ast A quer–V steht 30 %, am Ende y; die übrigen Äste ohne Angabe · kontext = Onlinehandel/Versand · textumfang = mittel
    gegeben = Baumdiagramm: P(A) = 0,4, P(A und verspätet) = 0,08, P(nicht A und verspätet) = 0,18; eine zufällig ausgewählte Sendung wird verspätet zugestellt · gesucht = Untersuchung, ob die Wahrscheinlichkeit, dass diese Sendung nicht mit A verschickt wurde, größer als 50 % ist · verfahren = P(nicht A | verspätet) = 0,18/(0,08 + 0,18) berechnen und mit 0,5 vergleichen · schritte = 2 · zahlenraum = dezimal|Prozent · einheiten =  · abhaengig_von = 2026MgrundlegendAStochastik13-a
    ergebnis = 0,18/(0,08 + 0,18) = 0,18/0,26 > 0,5, also ja (amtlich) · zwischenergebnis = 0,18/0,26 ≈ 0,69
    niveau_geschaetzt = II · fehlerquelle = mit 0,3 (Anteil unter den nicht mit A verschickten) statt mit der bedingten Wahrscheinlichkeit unter der Bedingung verspätet antworten · bemerkung = Standardbezug: K1 I, K3 II, K4 II, K5 II, K6 I. Amtlich, eigene Rechnung bestätigt.

Ein „?" hinter einem Wert bedeutet: plausibel, aber nicht am Bild geprüft; der
Grund steht dann in bemerkung. In diesem Stapel kommt es nicht vor.

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
