# Befund Zuschnitt Abitur GK – 15.10.2026

Geprüft: Entwurf `abitur/skript-zuschnitt-abi-gk.md` (49 Abschnitte, 246 Teilaufgaben GK BB/BE
2022–2026: 2022–2025 bebb-gk, 2026 bb-gk) gegen die P10-Regeln aus `pruefung.md`: Blatt = Einheit
mit eigenem Kopf-Schritt; Stufen heißen nach dem Gesuchten; Blatt = alle Originale der letzten fünf
Jahre, etwa zwei Seiten, sonst teilen; Einheiten mit höchstens vier Originalen werden Stufe der
Nachbareinheit; Lernfolge über Kapitelgrenzen. Ergebnis als Daten in `abitur/gliederung/*.md`
(Kopffelder Anzeigenamen, Kennung, Ordner, Stufen; Format `abitur/gliederung/README.md`).

**Ergebnis: 33 Blätter** (Analysis 16, Geometrie 8, Stochastik 9), 2–3 Stufen je Blatt, 4–10
Originale je Blatt. **Teilaufgaben ohne Platz: 0** – jede der 246 hat genau einen Hauptplatz
(`werkzeuge/skript-zuschnitt.py abi-gk`). Sie-/Du-Form nicht entschieden (plan.md Linie 4).

## Was sich am Entwurf geändert hat

Grundsatz: Der Entwurf hatte als Abschnitt den Handgriff und darunter je Erscheinungsform eine
Zeile mit meist einer Teilaufgabe (49 Abschnitte, 170 Zeilen). Das ist eine Stufe zu fein: Ein
Abschnitt ist bei P10 das Blatt, seine Stufen sind das Gesuchte. Jetzt: Abschnitt = Blatt, Zeile =
Stufe (gleichnamige Zeilen fassen die früheren Erscheinungsformen zusammen; die alte Zeile steht in
`‹…›` dahinter). Die Blöcke `###` (Bank, Kern) bleiben, damit Zuordnung und Wortlaut-Daten des
Pilotblatts nicht brechen.

- **Kurvenuntersuchung** (12 → 9 Blätter): Symmetrie (3) zu Grenzverhalten, weil beide am Term
  ohne Ableitung gelesen werden; Funktionsgleichung (3) und Extremalproblem (2) zu „Funktion
  aufstellen“, gemeinsamer Kopf-Schritt „aus Text Gleichungen aufschreiben“; „Graph skizzieren“ (3)
  zu „Graph im Sachzusammenhang“. Stufen nach dem Gesuchten statt nach Funktionsart; die
  e-Funktion bleibt nur dort eigene Stufe, wo der erste Schritt ein anderer ist (Produktregel).
- **Ableitung + Tangente** (5 → 4): Normale (3) zum Dreieck aus Tangente und Normale – dort steht
  sie in drei der fünf Dreiecksaufgaben; Änderungsrate vor Tangente in der Lernfolge (Steigung
  zuerst, dann Gleichung), Winkel und Dreieck nach den Wendepunkten (Wendetangente).
- **Integral** (6 → 3): Stammfunktion (3) + bestimmtes Integral (3) + Parameter aus Flächenbedingung
  (3) = „Integral berechnen“; Fläche (7) + „Lösungsweg erklären“ (3, aus „Integral am Graphen
  deuten“ herausgelöst, weil dort erklärt statt geschätzt wird) = „Flächeninhalt“; Schätzen und
  Vorzeichen (5) + Stammfunktion am Graphen (4) = „Integral am Graphen“.
- **Punkte, Flächen, Körper** (5 → 3): Trapez (2) zu „Längen und Figuren“; Netz (1) zu „Fläche und
  Volumen“, ans Ende der Geometrie, weil die Volumenaufgaben alles Vorige brauchen.
- **Winkel + Abstände** (4 → 3): Abstand (3) + Lotfußpunkt (3) = „Abstände“; Rechter Winkel bleibt
  eigenes Blatt (9), weil es den Normalenvektor vorbereitet.
- **Geraden + Ebenen** (4 → 2): Ebenengleichung (4) zwischen die beiden Punktproben (Gerade,
  Ebene); Lage (4) + Schnittpunkt (2) gemeinsam.
- **Baum + bedingte W.** (8 → 5): Baum zeichnen (3) zu den Pfadregeln; Unabhängigkeit (1) zur
  Vierfeldertafel; „Ergebnisse aufzählen“ (3, bisher nur hilfsmittelfrei ohne Blatt) als unterste
  Stufe zu „Ziehen ohne Zurücklegen“; „Ereignis deuten“ geteilt: bedingte Terme deuten zur
  bedingten Wahrscheinlichkeit, Ereignis zum Term mit „unbekannter Anteil“ (3) zu „Term und
  Anteil am Baum“ (beides liest den Baum rückwärts).
- **Binomialverteilung + Erwartungswert** (7 → 4): „Binomialverteilung begründen“ (1) zur
  Bernoulli-Kette; Mindestanzahl (3) und Grenze k zu „n, p oder k gesucht“; Erwartungswert der
  Binomialverteilung (5) zum Säulendiagramm, weil vier der fünf Aufgaben die Säulen lesen; der
  Block wechselt dafür die Datei. Das Spiel (4) bleibt eigenes Blatt: mit jedem Nachbarn über drei
  Seiten (die drei 2023er Teilaufgaben haben je über 550 Zeichen Sachtext).
- **Hilfsmittelfrei**: wie der P10-Basisteil – eigene Zettel (Teil A je Jahr), jede A-Teilaufgabe
  steht zusätzlich in ihrer Stufe auf dem Blatt; `_hilfsmittelfrei.md` hat keine Stufen mehr.

## Länge

Abitur-Teilaufgaben tragen mehr Sachtext als P10 (Mittel ≈ 190 Zeichen gegeben + gesucht, P10 ≈ 110).
P10 „Flächen“ (12 Originale, ≈ 1200 Zeichen) ist das Maß der Regel „zwei Seiten“; dafür müssten
fast alle Abitur-Blätter geteilt werden, und die Teile hätten meist höchstens vier Originale – was
dieselbe Regel verbietet. Gewählt: höchstens zehn Originale je Blatt; ob es zwei oder drei Seiten
werden, zeigt der erste Satz (wie bei P10 Prozent). Über 2000 Zeichen, Kandidaten zum Teilen
nach dem Satz: Graph im Sachzusammenhang (2620), Flächeninhalt (2380), Integral berechnen (2340,
davon 700 eine Mittelwert-Aufgabe), Abstände (2150), Verschieben (2100), Baumdiagramm (2090),
Spiel (2020).

## Schwach belegte Stufen

Ein Original statt mindestens zwei: Netz ergänzen (AG80, 2024), Fläche gesucht (AG80, ein
Hauptplatz und ein Nebenplatz), Unabhängigkeit prüfen (AS30, dazu ein Nebenplatz). Sie bleiben
Stufe, weil ihr erster Schritt ein eigener ist; Füllfolge nach `pruefung.md` (ältere BB, IQB).

## Stolpersteine für den Bau

- Spiegelpunkt an einer Ebene (2026-bb-gk-A1.2b, AG10) braucht die Lotgerade (AG70): schwerste
  Aufgabe der Stufe, Hinweis „kennst du aus Abstände“.
- Punktprobe mit Normalenvektor (AG40) braucht den rechten Winkel (AG30) – Lernfolge hält das.
- Sachaufgaben der Kurvenuntersuchung (2022 Roboter, 2026 Schiene) verteilen sich auf mehrere
  Blätter; das Zwischenergebnis steht jeweils dabei (Zuschnitt fest 04.10.).
