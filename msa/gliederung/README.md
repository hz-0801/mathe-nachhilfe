# Prüfungsgliederung – Format

Entscheidung A (plan.md § 2 Linie 2, W2, 08.10.2026): drei gepflegte Objekte –
Bank (Aufgabe), Katalog (Lernweg) und je Prüfungsart eine Prüfungsgliederung.
Die Gliederung ist das, was hier liegt: je Prüfungskapitel eine Datei
`msa/gliederung/<kapitel>.md` (P10) bzw. `abitur/gliederung/<kapitel>.md`
(Abitur GK), Leser `werkzeuge/gliederung.py`. Alles andere wird daraus erzeugt
und nicht mehr gepflegt:

| Sicht | erzeugt von |
|---|---|
| `msa/zuordnung-<kapitel>.csv`, `abitur/zuordnung-<kapitel>.csv` | `werkzeuge/zuordnung.py <kapitel>` |
| `msa/skript-zuschnitt-p10.csv`, `abitur/skript-zuschnitt-abi-gk.csv` | `werkzeuge/gliederung-sichten.py` |
| `msa/handgriffe-p10.csv` | `werkzeuge/gliederung-sichten.py` |
| Steckbrief eines Fokus (Bauprogramm `aufgabenbank/werkzeuge/pruefheft.py --fokus`) | Block `## Fokus <name>` dieser Datei, Leser `aufgabenbank/werkzeuge/steckbrief.py` |

Merkkasten, Formel und Typische Fehler stehen nur im Katalog (`katalog/<eintrag>.md`);
die Gliederung verweist („→ katalog/…“), sie kopiert nicht.

## Aufbau einer Datei

    # Gliederung Prozent (P10)          Titel, frei
    Prüfung: msa                       msa | abitur
    Kapitel: prozent                   Schlüssel = Dateiname; Argument von zuordnung.py
    Gebiet: Daten + Zufall             Spalte gebiet des Zuschnitts
    Name: Prozent                      Spalte kapitel des Zuschnitts
    Folge: 8                           Platz des Kapitels im Zuschnitt (Reihenfolge der Dateien)
    Kurzwort: daten | stoch            Kurzwörter des Gebiets für die Bestellung („Lena daten“), seit 15.10.2026;
                                       Leser aufgabenbank werkzeuge/bestellen.py (alle Dateien eines Gebiets gleich)
    Bank: prozentrechnung | zinsrechnung   Bankeinträge (aufgabenbank/bank/<eintrag>)
    Katalog: katalog/prozentrechnung.md | …   Verweise, nur für Menschen
    Skript: nein                       nur Sammlungen ohne Bank (_basisteil, _hilfsmittelfrei)
    Anzeigenamen: <Zuschnitt> = Name  Blattname in Schülersprache, mehrere mit „ | “
    Kennung: <Zuschnitt> = PG50        sprechende Kennung je Einheit (plan.md § 10, 14.10. b; gemeinsam.md
                                       „Kennung mit Fassung“): Sorte · Gebiet · Platz in der Lernfolge mit
                                       Zehnerlücken; die Folge der Blätter über alle Kapitel ist der Platz
    Kennung alt: <Zuschnitt> = P4Z     bis 14.10. gültige Kennung, nur zum Nachschlagen (Register umgeschlüsselt)
    Ordner: <Zuschnitt> = pythagoras   Ausgabeordner unter aufgabenbank bau/pruefung/<datum>/ (seit 14.10.;
                                       Leser aufgabenbank werkzeuge/p10einheiten.py für Karte, Gesamtheft, Mappe)

    ## Stufen                          Stufen in Lernreihenfolge (Heftreihenfolge)
    ### <Stufe>                        Name der Stufe (= Handgriff)
    - **Kern:** ja – <Grund>           ja | nein, nach „ – “ der Grund (kern, kern_grund)
    - **Originale:** <ids>             echte Teilaufgaben der Stufe, alle Jahre (Urteil je Stufe);
                                       fehlt die Zeile, sind es die ids der Zuschnitt-Zeilen
    - **Bank:** <Muster>               Bank-Sprossen: eintrag-eN-kN-sN, dahinter [ids] = nur mit
                                       diesen Originalen (Prüfungshöhe) oder [v1,v2] = nur diese
                                       Varianten, (i) = innermathematisch, jede Zeile zählt
    - **Verwechselbar:** A | B | kap:C Stufen, mit denen der Handgriff verwechselt wird
    - **Zuschnitt:** <Abschnitt>       Abschnitt im Zuschnitt; ohne Unterpunkte eine Zeile mit dem
      - <Zeile> [ids] neben [ids]      Namen der Stufe und den Originalen ab 2022 ohne EBR; mit
                                       Unterpunkten genau diese Zeilen (Hauptplatz, Nebenplatz)
    - **Regine:** S. 24 · 26        Seite(n) der Formel der Stufe im Tafelwerk „Formeln Tabellen
                                       Wissenswertes Sek I“ (Duden Paetec, das die meisten Schüler
                                       haben; Abschrift privat, aufgabenbank-privat formelsammlung/
                                       regine-sek1.md); mehrere mit „ · “, nur Seitenzahlen, kein
                                       Wortlaut; fehlt bei Stufen ohne Formel (13.10.2026). Leser:
                                       Stufe regine [int]; ob ein Setzer es druckt, ist offen
    - **Schülerfrage:** …              Heranführung als erste Aufgabe der Stufe (Felder -Fälle, -Form,
      **Frage:** …                     -Weg, -Skizze; Frage = kurzer Anstoß kursiv unter dem Kopf);
                                       Leser im Setzer aufgabenbank werkzeuge/pruefheft.py
                                       (p_gliederung). Bestand und Herkunft: aufgabenbank
                                       bau/heranfuehrungen-p10.md; je Abschnitt höchstens ein
                                       Erkennen-Schritt und ein Stups in die Formelsammlung
    weitere Felder frei (Katalogstelle, didaktische Notizen); Text zwischen den
    Feldern ignoriert der Leser.

    ## Plätze der Originale            nur P10: Tabelle id | Hauptplatz | Ganz auch |
                                       Zwischenschritt | Begründung (= handgriffe-p10.csv);
                                       Stufen des eigenen Kapitels ohne Präfix, fremde „kapitel:Stufe“,
                                       mehrere mit „; “. Jede Teilaufgabe steht im Kapitel ihres
                                       Hauptplatzes (ersatzweise: ganz auch, Zwischenschritt).

    ## Fokus <name>                    ein Steckbrief, wie bisher katalog/steckbrief/<kapitel>-<name>.md
    Titel: …                           (Format dort, jetzt archiv/steckbrief-README.md), nur die
    Kapitel: … / Stufen: … / Bank: …   Überschriften eine Ebene tiefer: ### 1 Verständnis …
    ### 1 Verständnis                  ### 5 Arten, #### <Art>. `--fokus <name>` findet den Block
    - **Typische Fehler:** → katalog/prozentrechnung.md, Typische Fehler: Grundwert gesucht | …
                                       Verweis: der Leser nimmt die Sätze der Katalogliste, die
                                       mit den genannten Wörtern beginnen (Reihenfolge der Nennung)
    - **Leiter:** → katalog/…          Verweis ohne Auswahl, nur für Menschen

Leser: `gliederung.lies(pfad)` liefert Kopf, Stufen (name, kern, kern_grund, originale,
regine, bank, verwechselbar, abschnitt, zeilen, felder), Plätze und die Fokus-Blöcke roh;
`gliederung.fokus_text(G, name)` gibt einen Fokus-Block als Steckbrief-Text zurück.
Die Dateien entstanden am 08.10.2026 durch `werkzeuge/gliederung-extrakt.py` aus
`zuordnung.py` (Stand a1c9fd3), den Zuschnitt-CSVs, `handgriffe-p10.csv` und den
zwei Steckbriefen; seitdem werden sie von Hand gepflegt.

## Bestellung

Kopffelder der Prüfung für die Bestellung (plan.md § 10, 15.10.2026 k; Leser aufgabenbank
`werkzeuge/bestellen.py`). Eine neue Prüfung bekommt diesen Block in ihrem `gliederung/README.md`,
kein Code. Platzhalter: {kapitel}, {einheit}, {heft} (Dateiname eines Hefts ohne .pdf), {datum}, {ordner}.
Pfade mit „privat “ liegen in aufgabenbank-privat, sonst in aufgabenbank.

- Anzeige: P10
- Sorte: P
- Schülerliste: P10
- Papier: FOR | EBR
- Blatt: werkzeuge/pruefheft.py --kapitel {kapitel} --art p --einheit "{einheit}"
- Blattordner: bau/pruefung/{datum}/{ordner}
- Mehr: werkzeuge/pruefheft.py --kapitel {kapitel} --art mehr --alle --einheit "{einheit}"
- Hefte: privat hefte/{heft}.pdf
- Original neu: werkzeuge/originalneu.py --heft {heft}
- Original neu Ordner: privat bau/original-neu/{heft}/pdf
- Basiszettel: bau/zettel/BAS-Z{n}/BAS-Z{n}.pdf
- Karte: bau/pruefung/{datum}/bestellkarte.pdf
- Handreichung: bau/pruefung/{datum}/handreichung-muster.pdf
- Gesamtheft: bau/pruefung/{datum}/gesamtheft-p10.pdf
- Mappe: privat bau/mappe/{datum}/mappe-p10.pdf
