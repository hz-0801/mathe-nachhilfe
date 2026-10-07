# Steckbriefe – Format

Ein Steckbrief beschreibt einen Handgriff (eine oder mehrere P10-Stufen) für
Prüfungsheft, Fokusblatt, allgemeine Blätter und Bank. Das Bauprogramm
(`aufgabenbank/werkzeuge/pruefheft.py`, Leser `werkzeuge/steckbrief.py`) liest
ihn beim Fokusblatt; fehlt er, baut es wie bisher. Dateiname
`<kapitel>-<handgriff>.md`; `--fokus <handgriff>` (oder der ganze Name) findet ihn.

## Aufbau

    # Steckbrief …                      Titel, frei
    Kapitel: prozent                   Kapitel wie zuordnung-<kapitel>.csv
    Stufen: Grundwert | …              Stufen der Zuordnung, mit „|“ getrennt
    Bank: prozentrechnung              Bankeinträge, mit „|“ getrennt

    ## 1 Verständnis                    feste Überschriften: „## <Nummer> <Wort>“
    - **Schlüssel:** Wert               ein Feld je Punkt; Fortsetzung eingerückt
      - Unterpunkt                      Liste (nur Typische Fehler)
    ## 2 Raster
    - **Schlüssel:** Wert               „**Lücke:** …“ im Wert = Lücke im Raster
    ## 3 Formulierungen
    kurz:                               dann „- Satz (Herkunft)“ je Zeile
    lang:
    ## 4 Befunde                        „- …“, nur für Menschen

Der Leser erkennt nur diese Formen; Text dazwischen (Stand, Quellen) ignoriert
er. Klammerzusätze am Schlüssel zählen nicht („Leiter (Katalog Einheit 4)“ =
„Leiter“). Belege in eckigen Klammern und Vermerke „(Vorschlag …)“ kommen nie
aufs Blatt.

## Schlüssel, die das Programm liest (Teil 1)

| Schlüssel | wird zu |
|---|---|
| Verständnis-Bank | erste Sprosse der Leiter: Bank-ids (Sprosse oder Variante), mit „→“ |
| Erste Frage | (nur Inhalt der Verständnis-Bank; selbst nicht gesetzt) |
| Schätzfrage + Schätzfrage-Lösung | Ankreuzaufgabe nach der Verständnis-Sprosse, nur mit Zahlen und „Was kann passen: A · B · C“ |
| Begriff, Formel (Sätze in „…“) | Merkkasten nach der Verständnis-Sprosse |
| Typische Fehler | oben in der Lösungsdatei |
| Leiter-Bank | unterer Teil der Leiter in dieser Folge, jede Sprosse in der Stufe, die sie trägt |
| Vorher können | Rückblick: nur Zeilen von `msa/rueckblick-p10.csv`, deren Voraussetzung hier steht (Abschnitte mit „;“) |

Teil 2 (Sachen, Lücke) und Teil 3 (Fragen) geben eigenen Aufgaben in
Sprüngen der Leiter den Vorzug. Leiter, Darstellung, Begriff und Raster
bleiben zugleich Text für Menschen.

## Teil 5 Arten (seit 07.10.2026, Beschlüsse A3, A4, F3, G1)

    ## 5 Arten
    - **Kurzname:** …                  Name des Handgriffs (Blattname)
    - **Vorher:** … / **Weiter:** …     Kurznamen der Nachbarn (Schlusszeile F3)
    - **Nicht geprüft:** …             Arten aus Lehrwerken ohne BB/BE-Aufgabe
    - **Nicht-geprüft-Merkmal:** …     regulärer Ausdruck: fremde Aufgaben dieser Art fallen weg
    - **Formel:** …                    Merkkasten, nur die Formel (B7)
    - **Rückblick:** keiner | Bank-ids
    - **Erkennen-Frage / Erkennen-Bank / Erkennen-Fälle**   erster Schritt (A1)
    - **Formel-Frage / Formel-Fälle**  „Formel aufstellen“ (A2)
    ### <Art>                          je Art ein Block, Reihenfolge leicht → schwer
    - **Kurzname:** …                  Gruppenüberschrift in Schülersprache
    - **Stufe:** …                     Stufe der Zuordnung (Herkunft fremder Aufgaben)
    - **Zuschnitt:** …                 Stufenname in msa/skript-zuschnitt-p10.csv
    - **Beleg:** …  **P10-Typ:** …  **Typischer Fehler:** …
    - **Geprüft:** 5× (EBR und FOR)    BB/BE ohne GYM; „nur FOR“, wenn alle mit Stern
    - **Aufgaben:** P10-ids            BB/BE-Aufgaben der Art (Hauptplatz oder Zwischenschritt)
    - **Nur gekürzt:** ids (Grund)     nie in voller Fassung (Teilaufgabe verlangt mehr)
    - **Gruppen:** Name: ids | Name: ids   G1; eine Gruppe mit einer Aufgabe läuft ohne Überschrift
                                       (ids: P10-ids oder Kennungen fremder Aufgaben; fremde nur,
                                       wenn handgriffe genau die Stufe der Art nennt, F1)
    - **Leiter-Bank:** Bank-ids mit →  kurze Leiter der Art
    - **Fremd-Merkmal:** …             regulärer Ausdruck auf die Lösung (fremde Aufgaben dieser Art)

Fälle (Erkennen, Formel) als Unterpunkte: Dreiecke „(x|y) (x|y) (x|y);
Seiten a b c; rechter Winkel 1–3 oder 0“ (Seite i liegt Ecke i gegenüber)
oder Sätze „Text → Lösung“. Mit Teil 5 baut `pruefheft.py --fokus` die
Grundform G1; `werkzeuge/zuschnitt-aus-steckbrief.py` (mathe-nachhilfe)
erzeugt daraus die Zeilen von `msa/skript-zuschnitt-p10.csv`.
Gekürzte und bereinigte Fassungen der Originale (T1–T6: ohne das, was nur
andere Teilaufgaben brauchen; Text nur Sache und Frage, wenn eine Skizze
dabei ist) stehen in `msa/gekuerzt-p10.csv` (id; wortlaut_kurz;
skizze_kurz; ergebnis_kurz; zwischen_kurz; wortlaut_voll; skizze_voll).
Skizze: Dreieck im Fälle-Format, eine Beschreibung wie in den
Wortlautdateien oder TikZ (beginnt mit „\“).
