# Tragfähigkeit der Themen – Nachfrage in Blatt 0
Stand 2026-09-21, Katalog auf Commit c05e6f0.
Erzeugt von `werkzeuge/tragfaehigkeit.py` (v0.1) aus den Blatt-0-Abschnitten der Einträge; abgeleitet, nie von Hand ändern. Der Katalog misst sonst nur Prüfungslast (Zeilen je Thema); hier steht die zweite Achse: wie oft ein Thema von anderen Einträgen gebraucht wird.

Gemessen: 73 Einträge (`katalog/*.md` ohne `_*` und `index.md`); je Eintrag der Abschnitt „### Voraussetzungen (Blatt 0)“ bis zur nächsten Überschrift, darin die Verweise der Form `<name>.md`, mit oder ohne Einheitsangabe. Ein Eintrag zählt je genanntem Thema einmal, gleich wie oft er es nennt; Selbstverweise zählen nicht; keine Gewichtung nach Einheit oder Profil. Zeilen = eigene Katalogzeilen, Summe der Spalte `zeilen` in `themen.csv` (Prüfungslast).

## A Nachfrage – wie oft ein Thema vorausgesetzt wird
Absteigend nach der Zahl der nachfragenden Einträge, bei Gleichstand alphabetisch; alle Einträge, auch die ohne Nachfrage. Hohe Nachfrage bei niedriger Zeilenzahl heißt: das Thema wird nie Stundenthema, kostet aber Zeit in jeder Stunde, in der es fehlt.

| Thema | Nachfrager | Zeilen | Nachfrager (Namen) |
|---|---|---|---|
| lineare-gleichungen | 26 | 9 | bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, daten, flaechen, flaecheninhalt-und-volumen-im-raum, funktionsscharen-und-ortskurven, geraden, gleichungen-loesen, kenngroessen-von-verteilungen, koerper, kreis, lagebeziehungen, lineare-funktionen, lineare-gleichungssysteme, matrizen-und-uebergangsprozesse, pyramide-kegel-kugel, pythagoras, quadratische-funktionen, quadratische-gleichungen, scharen-von-geraden-und-ebenen, strahlensaetze, trigonometrie, unabhaengigkeit, vektoren-und-rechenoperationen, vierfeldertafel, zufallsexperimente-und-pfadregeln |
| potenzen-wurzeln | 24 | 12 | ableitungsregeln, binomische-formeln, daten, einheiten, flaechen, funktionsklassen-und-eigenschaften, funktionsscharen-und-ortskurven, grenzwerte-und-verhalten-im-unendlichen, integrationsregeln, kenngroessen-von-verteilungen, koerper, kombinatorik, kreis, potenz-exponentialfunktionen, punkte-und-strecken-im-koordinatensystem, pyramide-kegel-kugel, pythagoras, quadratische-funktionen, quadratische-gleichungen, reelle-zahlen, stammfunktion-und-hauptsatz, vektoren-und-rechenoperationen, zinsrechnung, zufallsexperimente-und-pfadregeln |
| prozentrechnung | 20 | 23 | ableitung-und-aenderungsrate, bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, brueche-dezimalzahlen, flaecheninhalt-und-volumen-im-raum, geraden, kenngroessen-von-verteilungen, koerper, kombinatorik, konfidenzintervalle, kreis, matrizen-und-uebergangsprozesse, normalverteilung-und-sigma-regeln, potenz-exponentialfunktionen, punkte-und-strecken-im-koordinatensystem, skalarprodukt-und-winkel, unabhaengigkeit, vierfeldertafel, wahrscheinlichkeit, zufallsexperimente-und-pfadregeln |
| bruchrechnung | 19 | 0 | ableitungsregeln, bedingte-wahrscheinlichkeit-und-bayes, daten, flaechen, hypergeometrische-verteilung, kenngroessen-von-verteilungen, koerper, kombinatorik, kreis, potenz-exponentialfunktionen, prozentrechnung, pyramide-kegel-kugel, pythagoras, rationale-zahlen, strahlensaetze, unabhaengigkeit, wahrscheinlichkeit, zufallsexperimente-und-pfadregeln, zufallsgroessen-und-verteilungen |
| lineare-funktionen | 17 | 28 | ableitung-und-aenderungsrate, ableitungsregeln, bedingte-wahrscheinlichkeit-und-bayes, ebenen, extremalprobleme, funktionsklassen-und-eigenschaften, geraden, gleichungen-loesen, hypothesentests, konfidenzintervalle, potenz-exponentialfunktionen, pythagoras, quadratische-funktionen, rekonstruktion-von-funktionsgleichungen, stammfunktion-und-hauptsatz, tangente-normale-schnittwinkel, umkehrfunktion |
| einheiten | 15 | 23 | ableitung-und-aenderungsrate, brueche-dezimalzahlen, daten, flaechen, flaecheninhalt-durch-integration, funktionsklassen-und-eigenschaften, koerper, pyramide-kegel-kugel, pythagoras, rekonstruktion-von-bestaenden, rotationsvolumen, strahlensaetze, trigonometrie, winkel-dreiecke, zuordnungen |
| gleichungen-loesen | 15 | 43 | ableitung-und-aenderungsrate, abstaende, bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, einheiten, extremalprobleme, flaecheninhalt-durch-integration, grenzwerte-und-verhalten-im-unendlichen, konfidenzintervalle, kurvenuntersuchung, lineare-gleichungssysteme, scharen-von-geraden-und-ebenen, tangente-normale-schnittwinkel, umkehrfunktion, zufallsexperimente-und-pfadregeln |
| quadratische-gleichungen | 15 | 2 | abstaende, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, funktionsklassen-und-eigenschaften, funktionsscharen-und-ortskurven, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, kenngroessen-von-verteilungen, konfidenzintervalle, lagebeziehungen, orthogonalitaet, quadratische-funktionen, scharen-von-geraden-und-ebenen, unabhaengigkeit, zufallsexperimente-und-pfadregeln |
| flaechen | 13 | 26 | einheiten, extremalprobleme, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, koerper, kreis, punkte-und-strecken-im-koordinatensystem, pyramide-kegel-kugel, pythagoras, symmetrie-abbildungen, tangente-normale-schnittwinkel, trigonometrie, umkehrfunktion |
| kreis | 13 | 0 | abstaende, brueche-dezimalzahlen, flaechen, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, koerper, punkte-und-strecken-im-koordinatensystem, pyramide-kegel-kugel, pythagoras, skalarprodukt-und-winkel, strahlensaetze, winkel-dreiecke, zufallsexperimente-und-pfadregeln |
| terme | 13 | 4 | ableitungsregeln, binomische-formeln, extremalprobleme, funktionsscharen-und-ortskurven, gleichungen-loesen, integrationsregeln, lagebeziehungen, lineare-gleichungen, lineare-gleichungssysteme, pyramide-kegel-kugel, quadratische-gleichungen, rationale-zahlen, vektoren-und-rechenoperationen |
| brueche-dezimalzahlen | 12 | 17 | ableitungsregeln, bruchrechnung, kombinatorik, kreis, potenz-exponentialfunktionen, prozentrechnung, pyramide-kegel-kugel, strahlensaetze, trigonometrie, wahrscheinlichkeit, winkel-dreiecke, zufallsexperimente-und-pfadregeln |
| pythagoras | 12 | 17 | abstaende, extremalprobleme, flaecheninhalt-und-volumen-im-raum, potenzen-wurzeln, punkte-und-strecken-im-koordinatensystem, pyramide-kegel-kugel, reelle-zahlen, rotationsvolumen, tangente-normale-schnittwinkel, trigonometrie, umkehrfunktion, vektoren-und-rechenoperationen |
| punkte-und-strecken-im-koordinatensystem | 10 | 83 | ebenen, flaecheninhalt-und-volumen-im-raum, geraden, lagebeziehungen, lineare-gleichungssysteme, scharen-von-geraden-und-ebenen, schnittmengen, skalarprodukt-und-winkel, spiegelung, vektoren-und-rechenoperationen |
| quadratische-funktionen | 10 | 31 | ableitung-und-aenderungsrate, ableitungsregeln, binomische-formeln, funktionsklassen-und-eigenschaften, funktionsscharen-und-ortskurven, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, kurvenuntersuchung, quadratische-gleichungen, rekonstruktion-von-funktionsgleichungen |
| vektoren-und-rechenoperationen | 10 | 20 | abstaende, ebenen, flaecheninhalt-und-volumen-im-raum, geraden, linearkombination-und-lineare-abhaengigkeit, matrizen-und-uebergangsprozesse, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, skalarprodukt-und-winkel, spiegelung |
| ableitungsregeln | 9 | 24 | ableitung-und-aenderungsrate, extremalprobleme, funktionsscharen-und-ortskurven, gleichungen-loesen, integrationsregeln, kurvenuntersuchung, rekonstruktion-von-funktionsgleichungen, stammfunktion-und-hauptsatz, tangente-normale-schnittwinkel |
| koerper | 9 | 28 | ebenen, einheiten, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, pyramide-kegel-kugel, rotationsvolumen, schnittmengen, strahlensaetze, vektoren-und-rechenoperationen |
| potenz-exponentialfunktionen | 9 | 21 | ableitung-und-aenderungsrate, ableitungsregeln, binomialverteilung, funktionsklassen-und-eigenschaften, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, matrizen-und-uebergangsprozesse, trigonometrische-funktionen, umkehrfunktion |
| rationale-zahlen | 9 | 7 | binomische-formeln, funktionsklassen-und-eigenschaften, grenzwerte-und-verhalten-im-unendlichen, integrationsregeln, pythagoras, quadratische-funktionen, quadratische-gleichungen, stammfunktion-und-hauptsatz, symmetrie-abbildungen |
| skalarprodukt-und-winkel | 9 | 42 | abstaende, ebenen, flaecheninhalt-und-volumen-im-raum, geraden, lagebeziehungen, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, scharen-von-geraden-und-ebenen, vektoren-und-rechenoperationen |
| strahlensaetze | 9 | 0 | abstaende, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, funktionsklassen-und-eigenschaften, geraden, gleichungen-loesen, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, schnittmengen |
| wahrscheinlichkeit | 9 | 37 | binomialverteilung, hypothesentests, kenngroessen-von-verteilungen, kombinatorik, normalverteilung-und-sigma-regeln, unabhaengigkeit, vierfeldertafel, zufallsexperimente-und-pfadregeln, zufallsgroessen-und-verteilungen |
| winkel-dreiecke | 9 | 19 | flaechen, kreis, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, pythagoras, skalarprodukt-und-winkel, strahlensaetze, symmetrie-abbildungen, trigonometrie |
| ebenen | 8 | 48 | abstaende, lagebeziehungen, linearkombination-und-lineare-abhaengigkeit, orthogonalitaet, scharen-von-geraden-und-ebenen, schnittmengen, skalarprodukt-und-winkel, spiegelung |
| funktionsklassen-und-eigenschaften | 8 | 200 | ableitungsregeln, einheiten, flaecheninhalt-durch-integration, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, kurvenuntersuchung, rekonstruktion-von-bestaenden, rekonstruktion-von-funktionsgleichungen |
| lineare-gleichungssysteme | 8 | 20 | ebenen, linearkombination-und-lineare-abhaengigkeit, matrizen-und-uebergangsprozesse, orthogonalitaet, quadratische-funktionen, rekonstruktion-von-funktionsgleichungen, scharen-von-geraden-und-ebenen, schnittmengen |
| geraden | 7 | 36 | abstaende, ebenen, lagebeziehungen, linearkombination-und-lineare-abhaengigkeit, orthogonalitaet, schnittmengen, skalarprodukt-und-winkel |
| orthogonalitaet | 7 | 43 | abstaende, ebenen, flaecheninhalt-und-volumen-im-raum, geraden, lagebeziehungen, punkte-und-strecken-im-koordinatensystem, scharen-von-geraden-und-ebenen |
| symmetrie-abbildungen | 7 | 3 | funktionsklassen-und-eigenschaften, grenzwerte-und-verhalten-im-unendlichen, punkte-und-strecken-im-koordinatensystem, spiegelung, umkehrfunktion, vektoren-und-rechenoperationen, zuordnungen |
| zuordnungen | 7 | 13 | ableitung-und-aenderungsrate, linearkombination-und-lineare-abhaengigkeit, potenz-exponentialfunktionen, prozentrechnung, rekonstruktion-von-bestaenden, strahlensaetze, vektoren-und-rechenoperationen |
| binomialverteilung | 6 | 155 | hypergeometrische-verteilung, hypothesentests, kenngroessen-von-verteilungen, kombinatorik, konfidenzintervalle, normalverteilung-und-sigma-regeln |
| daten | 6 | 70 | bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, matrizen-und-uebergangsprozesse, vierfeldertafel, wahrscheinlichkeit, zufallsgroessen-und-verteilungen |
| kurvenuntersuchung | 6 | 150 | ableitung-und-aenderungsrate, ableitungsgraph-und-funktionsgraph, extremalprobleme, funktionsscharen-und-ortskurven, stammfunktion-und-hauptsatz, umkehrfunktion |
| stammfunktion-und-hauptsatz | 6 | 52 | flaecheninhalt-durch-integration, funktionsscharen-und-ortskurven, normalverteilung-und-sigma-regeln, rekonstruktion-von-bestaenden, rotationsvolumen, uneigentliche-integrale |
| binomische-formeln | 5 | 0 | ableitungsregeln, gleichungen-loesen, quadratische-funktionen, quadratische-gleichungen, rotationsvolumen |
| linearkombination-und-lineare-abhaengigkeit | 5 | 1 | ebenen, geraden, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, scharen-von-geraden-und-ebenen |
| pyramide-kegel-kugel | 5 | 0 | ebenen, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, pythagoras, rotationsvolumen |
| zufallsexperimente-und-pfadregeln | 5 | 237 | bedingte-wahrscheinlichkeit-und-bayes, hypergeometrische-verteilung, kombinatorik, unabhaengigkeit, vierfeldertafel |
| ableitung-und-aenderungsrate | 4 | 54 | ableitungsregeln, kurvenuntersuchung, rekonstruktion-von-bestaenden, tangente-normale-schnittwinkel |
| flaecheninhalt-durch-integration | 4 | 124 | einheiten, normalverteilung-und-sigma-regeln, umkehrfunktion, uneigentliche-integrale |
| reelle-zahlen | 4 | 0 | ableitungsregeln, binomialverteilung, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen |
| trigonometrie | 4 | 28 | gleichungen-loesen, potenzen-wurzeln, skalarprodukt-und-winkel, tangente-normale-schnittwinkel |
| abstaende | 3 | 58 | flaecheninhalt-und-volumen-im-raum, scharen-von-geraden-und-ebenen, spiegelung |
| grenzwerte-und-verhalten-im-unendlichen | 3 | 22 | gleichungen-loesen, umkehrfunktion, uneigentliche-integrale |
| kenngroessen-von-verteilungen | 3 | 73 | binomialverteilung, hypothesentests, normalverteilung-und-sigma-regeln |
| kombinatorik | 3 | 32 | binomialverteilung, hypergeometrische-verteilung, zufallsexperimente-und-pfadregeln |
| lagebeziehungen | 3 | 38 | lineare-gleichungssysteme, scharen-von-geraden-und-ebenen, schnittmengen |
| schnittmengen | 3 | 31 | lineare-gleichungssysteme, scharen-von-geraden-und-ebenen, spiegelung |
| trigonometrische-funktionen | 3 | 0 | funktionsklassen-und-eigenschaften, gleichungen-loesen, rekonstruktion-von-funktionsgleichungen |
| vierfeldertafel | 3 | 29 | bedingte-wahrscheinlichkeit-und-bayes, unabhaengigkeit, zufallsexperimente-und-pfadregeln |
| ableitungsgraph-und-funktionsgraph | 2 | 21 | ableitung-und-aenderungsrate, stammfunktion-und-hauptsatz |
| bedingte-wahrscheinlichkeit-und-bayes | 2 | 39 | unabhaengigkeit, zufallsexperimente-und-pfadregeln |
| integrationsregeln | 2 | 2 | flaecheninhalt-durch-integration, stammfunktion-und-hauptsatz |
| tangente-normale-schnittwinkel | 2 | 127 | ableitungsregeln, stammfunktion-und-hauptsatz |
| funktionsscharen-und-ortskurven | 1 | 142 | lagebeziehungen |
| hypergeometrische-verteilung | 1 | 7 | binomialverteilung |
| normalverteilung-und-sigma-regeln | 1 | 20 | konfidenzintervalle |
| zinsrechnung | 1 | 5 | potenz-exponentialfunktionen |
| zufallsgroessen-und-verteilungen | 1 | 6 | kenngroessen-von-verteilungen |
| extremalprobleme | 0 | 23 | – |
| flaecheninhalt-und-volumen-im-raum | 0 | 78 | – |
| hypothesentests | 0 | 22 | – |
| konfidenzintervalle | 0 | 12 | – |
| matrizen-und-uebergangsprozesse | 0 | 154 | – |
| rekonstruktion-von-bestaenden | 0 | 27 | – |
| rekonstruktion-von-funktionsgleichungen | 0 | 35 | – |
| rotationsvolumen | 0 | 13 | – |
| scharen-von-geraden-und-ebenen | 0 | 49 | – |
| spiegelung | 0 | 27 | – |
| umkehrfunktion | 0 | 6 | – |
| unabhaengigkeit | 0 | 27 | – |
| uneigentliche-integrale | 0 | 2 | – |

## B Einstiegshürde – wie viele Themen ein Eintrag voraussetzt
Absteigend nach der Zahl der eigenen Voraussetzungen, bei Gleichstand alphabetisch – so viel muss ein Blatt 0 zu diesem Thema abdecken. Nur Einträge mit mindestens einem Verweis; für die 1 übrigen ist die Hürde nicht null, sondern ungemessen (siehe Messlücken).

| Thema | Voraussetzungen | Voraussetzungen (Namen) |
|---|---|---|
| flaecheninhalt-und-volumen-im-raum | 14 | abstaende, flaechen, koerper, kreis, lineare-gleichungen, orthogonalitaet, prozentrechnung, punkte-und-strecken-im-koordinatensystem, pyramide-kegel-kugel, pythagoras, quadratische-gleichungen, skalarprodukt-und-winkel, strahlensaetze, vektoren-und-rechenoperationen |
| gleichungen-loesen | 14 | ableitungsregeln, binomische-formeln, funktionsklassen-und-eigenschaften, grenzwerte-und-verhalten-im-unendlichen, lineare-funktionen, lineare-gleichungen, potenz-exponentialfunktionen, quadratische-funktionen, quadratische-gleichungen, reelle-zahlen, strahlensaetze, terme, trigonometrie, trigonometrische-funktionen |
| punkte-und-strecken-im-koordinatensystem | 14 | flaechen, koerper, kreis, linearkombination-und-lineare-abhaengigkeit, orthogonalitaet, potenzen-wurzeln, prozentrechnung, pyramide-kegel-kugel, pythagoras, skalarprodukt-und-winkel, strahlensaetze, symmetrie-abbildungen, vektoren-und-rechenoperationen, winkel-dreiecke |
| ableitungsregeln | 12 | ableitung-und-aenderungsrate, binomische-formeln, bruchrechnung, brueche-dezimalzahlen, funktionsklassen-und-eigenschaften, lineare-funktionen, potenz-exponentialfunktionen, potenzen-wurzeln, quadratische-funktionen, reelle-zahlen, tangente-normale-schnittwinkel, terme |
| scharen-von-geraden-und-ebenen | 12 | abstaende, ebenen, gleichungen-loesen, lagebeziehungen, lineare-gleichungen, lineare-gleichungssysteme, linearkombination-und-lineare-abhaengigkeit, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, quadratische-gleichungen, schnittmengen, skalarprodukt-und-winkel |
| zufallsexperimente-und-pfadregeln | 12 | bedingte-wahrscheinlichkeit-und-bayes, bruchrechnung, brueche-dezimalzahlen, gleichungen-loesen, kombinatorik, kreis, lineare-gleichungen, potenzen-wurzeln, prozentrechnung, quadratische-gleichungen, vierfeldertafel, wahrscheinlichkeit |
| ableitung-und-aenderungsrate | 10 | ableitungsgraph-und-funktionsgraph, ableitungsregeln, einheiten, gleichungen-loesen, kurvenuntersuchung, lineare-funktionen, potenz-exponentialfunktionen, prozentrechnung, quadratische-funktionen, zuordnungen |
| abstaende | 10 | ebenen, geraden, gleichungen-loesen, kreis, orthogonalitaet, pythagoras, quadratische-gleichungen, skalarprodukt-und-winkel, strahlensaetze, vektoren-und-rechenoperationen |
| binomialverteilung | 10 | daten, gleichungen-loesen, hypergeometrische-verteilung, kenngroessen-von-verteilungen, kombinatorik, lineare-gleichungen, potenz-exponentialfunktionen, prozentrechnung, reelle-zahlen, wahrscheinlichkeit |
| ebenen | 10 | geraden, koerper, lineare-funktionen, lineare-gleichungssysteme, linearkombination-und-lineare-abhaengigkeit, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, pyramide-kegel-kugel, skalarprodukt-und-winkel, vektoren-und-rechenoperationen |
| funktionsklassen-und-eigenschaften | 10 | einheiten, lineare-funktionen, potenz-exponentialfunktionen, potenzen-wurzeln, quadratische-funktionen, quadratische-gleichungen, rationale-zahlen, strahlensaetze, symmetrie-abbildungen, trigonometrische-funktionen |
| pyramide-kegel-kugel | 10 | bruchrechnung, brueche-dezimalzahlen, einheiten, flaechen, koerper, kreis, lineare-gleichungen, potenzen-wurzeln, pythagoras, terme |
| pythagoras | 10 | bruchrechnung, einheiten, flaechen, kreis, lineare-funktionen, lineare-gleichungen, potenzen-wurzeln, pyramide-kegel-kugel, rationale-zahlen, winkel-dreiecke |
| flaecheninhalt-durch-integration | 9 | einheiten, flaechen, funktionsklassen-und-eigenschaften, gleichungen-loesen, integrationsregeln, kreis, quadratische-gleichungen, stammfunktion-und-hauptsatz, strahlensaetze |
| geraden | 9 | lineare-funktionen, lineare-gleichungen, linearkombination-und-lineare-abhaengigkeit, orthogonalitaet, prozentrechnung, punkte-und-strecken-im-koordinatensystem, skalarprodukt-und-winkel, strahlensaetze, vektoren-und-rechenoperationen |
| grenzwerte-und-verhalten-im-unendlichen | 9 | funktionsklassen-und-eigenschaften, gleichungen-loesen, potenz-exponentialfunktionen, potenzen-wurzeln, quadratische-funktionen, quadratische-gleichungen, rationale-zahlen, reelle-zahlen, symmetrie-abbildungen |
| lagebeziehungen | 9 | ebenen, funktionsscharen-und-ortskurven, geraden, lineare-gleichungen, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, quadratische-gleichungen, skalarprodukt-und-winkel, terme |
| orthogonalitaet | 9 | ebenen, geraden, lineare-gleichungssysteme, linearkombination-und-lineare-abhaengigkeit, quadratische-gleichungen, skalarprodukt-und-winkel, strahlensaetze, vektoren-und-rechenoperationen, winkel-dreiecke |
| umkehrfunktion | 9 | flaechen, flaecheninhalt-durch-integration, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, kurvenuntersuchung, lineare-funktionen, potenz-exponentialfunktionen, pythagoras, symmetrie-abbildungen |
| vektoren-und-rechenoperationen | 9 | koerper, lineare-gleichungen, potenzen-wurzeln, punkte-und-strecken-im-koordinatensystem, pythagoras, skalarprodukt-und-winkel, symmetrie-abbildungen, terme, zuordnungen |
| bedingte-wahrscheinlichkeit-und-bayes | 8 | bruchrechnung, daten, gleichungen-loesen, lineare-funktionen, lineare-gleichungen, prozentrechnung, vierfeldertafel, zufallsexperimente-und-pfadregeln |
| funktionsscharen-und-ortskurven | 8 | ableitungsregeln, kurvenuntersuchung, lineare-gleichungen, potenzen-wurzeln, quadratische-funktionen, quadratische-gleichungen, stammfunktion-und-hauptsatz, terme |
| kenngroessen-von-verteilungen | 8 | binomialverteilung, bruchrechnung, lineare-gleichungen, potenzen-wurzeln, prozentrechnung, quadratische-gleichungen, wahrscheinlichkeit, zufallsgroessen-und-verteilungen |
| skalarprodukt-und-winkel | 8 | ebenen, geraden, kreis, prozentrechnung, punkte-und-strecken-im-koordinatensystem, trigonometrie, vektoren-und-rechenoperationen, winkel-dreiecke |
| stammfunktion-und-hauptsatz | 8 | ableitungsgraph-und-funktionsgraph, ableitungsregeln, integrationsregeln, kurvenuntersuchung, lineare-funktionen, potenzen-wurzeln, rationale-zahlen, tangente-normale-schnittwinkel |
| strahlensaetze | 8 | bruchrechnung, brueche-dezimalzahlen, einheiten, koerper, kreis, lineare-gleichungen, winkel-dreiecke, zuordnungen |
| unabhaengigkeit | 8 | bedingte-wahrscheinlichkeit-und-bayes, bruchrechnung, lineare-gleichungen, prozentrechnung, quadratische-gleichungen, vierfeldertafel, wahrscheinlichkeit, zufallsexperimente-und-pfadregeln |
| extremalprobleme | 7 | ableitungsregeln, flaechen, gleichungen-loesen, kurvenuntersuchung, lineare-funktionen, pythagoras, terme |
| koerper | 7 | bruchrechnung, einheiten, flaechen, kreis, lineare-gleichungen, potenzen-wurzeln, prozentrechnung |
| kombinatorik | 7 | binomialverteilung, bruchrechnung, brueche-dezimalzahlen, potenzen-wurzeln, prozentrechnung, wahrscheinlichkeit, zufallsexperimente-und-pfadregeln |
| kreis | 7 | bruchrechnung, brueche-dezimalzahlen, flaechen, lineare-gleichungen, potenzen-wurzeln, prozentrechnung, winkel-dreiecke |
| potenz-exponentialfunktionen | 7 | bruchrechnung, brueche-dezimalzahlen, lineare-funktionen, potenzen-wurzeln, prozentrechnung, zinsrechnung, zuordnungen |
| quadratische-funktionen | 7 | binomische-formeln, lineare-funktionen, lineare-gleichungen, lineare-gleichungssysteme, potenzen-wurzeln, quadratische-gleichungen, rationale-zahlen |
| schnittmengen | 7 | ebenen, geraden, koerper, lagebeziehungen, lineare-gleichungssysteme, punkte-und-strecken-im-koordinatensystem, strahlensaetze |
| tangente-normale-schnittwinkel | 7 | ableitung-und-aenderungsrate, ableitungsregeln, flaechen, gleichungen-loesen, lineare-funktionen, pythagoras, trigonometrie |
| einheiten | 6 | flaechen, flaecheninhalt-durch-integration, funktionsklassen-und-eigenschaften, gleichungen-loesen, koerper, potenzen-wurzeln |
| flaechen | 6 | bruchrechnung, einheiten, kreis, lineare-gleichungen, potenzen-wurzeln, winkel-dreiecke |
| konfidenzintervalle | 6 | binomialverteilung, gleichungen-loesen, lineare-funktionen, normalverteilung-und-sigma-regeln, prozentrechnung, quadratische-gleichungen |
| lineare-gleichungssysteme | 6 | gleichungen-loesen, lagebeziehungen, lineare-gleichungen, punkte-und-strecken-im-koordinatensystem, schnittmengen, terme |
| matrizen-und-uebergangsprozesse | 6 | daten, lineare-gleichungen, lineare-gleichungssysteme, potenz-exponentialfunktionen, prozentrechnung, vektoren-und-rechenoperationen |
| normalverteilung-und-sigma-regeln | 6 | binomialverteilung, flaecheninhalt-durch-integration, kenngroessen-von-verteilungen, prozentrechnung, stammfunktion-und-hauptsatz, wahrscheinlichkeit |
| quadratische-gleichungen | 6 | binomische-formeln, lineare-gleichungen, potenzen-wurzeln, quadratische-funktionen, rationale-zahlen, terme |
| rekonstruktion-von-funktionsgleichungen | 6 | ableitungsregeln, funktionsklassen-und-eigenschaften, lineare-funktionen, lineare-gleichungssysteme, quadratische-funktionen, trigonometrische-funktionen |
| rotationsvolumen | 6 | binomische-formeln, einheiten, koerper, pyramide-kegel-kugel, pythagoras, stammfunktion-und-hauptsatz |
| spiegelung | 6 | abstaende, ebenen, punkte-und-strecken-im-koordinatensystem, schnittmengen, symmetrie-abbildungen, vektoren-und-rechenoperationen |
| trigonometrie | 6 | brueche-dezimalzahlen, einheiten, flaechen, lineare-gleichungen, pythagoras, winkel-dreiecke |
| kurvenuntersuchung | 5 | ableitung-und-aenderungsrate, ableitungsregeln, funktionsklassen-und-eigenschaften, gleichungen-loesen, quadratische-funktionen |
| linearkombination-und-lineare-abhaengigkeit | 5 | ebenen, geraden, lineare-gleichungssysteme, vektoren-und-rechenoperationen, zuordnungen |
| rekonstruktion-von-bestaenden | 5 | ableitung-und-aenderungsrate, einheiten, funktionsklassen-und-eigenschaften, stammfunktion-und-hauptsatz, zuordnungen |
| vierfeldertafel | 5 | daten, lineare-gleichungen, prozentrechnung, wahrscheinlichkeit, zufallsexperimente-und-pfadregeln |
| binomische-formeln | 4 | potenzen-wurzeln, quadratische-funktionen, rationale-zahlen, terme |
| daten | 4 | bruchrechnung, einheiten, lineare-gleichungen, potenzen-wurzeln |
| hypergeometrische-verteilung | 4 | binomialverteilung, bruchrechnung, kombinatorik, zufallsexperimente-und-pfadregeln |
| hypothesentests | 4 | binomialverteilung, kenngroessen-von-verteilungen, lineare-funktionen, wahrscheinlichkeit |
| integrationsregeln | 4 | ableitungsregeln, potenzen-wurzeln, rationale-zahlen, terme |
| wahrscheinlichkeit | 4 | bruchrechnung, brueche-dezimalzahlen, daten, prozentrechnung |
| brueche-dezimalzahlen | 3 | einheiten, kreis, prozentrechnung |
| prozentrechnung | 3 | bruchrechnung, brueche-dezimalzahlen, zuordnungen |
| symmetrie-abbildungen | 3 | flaechen, rationale-zahlen, winkel-dreiecke |
| uneigentliche-integrale | 3 | flaecheninhalt-durch-integration, grenzwerte-und-verhalten-im-unendlichen, stammfunktion-und-hauptsatz |
| winkel-dreiecke | 3 | brueche-dezimalzahlen, einheiten, kreis |
| zufallsgroessen-und-verteilungen | 3 | bruchrechnung, daten, wahrscheinlichkeit |
| potenzen-wurzeln | 2 | pythagoras, trigonometrie |
| rationale-zahlen | 2 | bruchrechnung, terme |
| reelle-zahlen | 2 | potenzen-wurzeln, pythagoras |
| zuordnungen | 2 | einheiten, symmetrie-abbildungen |
| ableitungsgraph-und-funktionsgraph | 1 | kurvenuntersuchung |
| bruchrechnung | 1 | brueche-dezimalzahlen |
| lineare-funktionen | 1 | lineare-gleichungen |
| lineare-gleichungen | 1 | terme |
| trigonometrische-funktionen | 1 | potenz-exponentialfunktionen |
| zinsrechnung | 1 | potenzen-wurzeln |

## Messlücken
Was die Messung nicht sieht – berichtet, nicht gestopft (kein Eintrag wird vom Werkzeug geändert).

Einträge ohne Verweis der Form `<name>.md` im Blatt-0-Abschnitt: 1 von 73. In Klammern die Nennungen in Wortform („Thema …“ vor einem Großbuchstaben, Heuristik) – die Nachfrage, die diese Einträge stellen, fehlt in Tabelle A ganz.
- terme (0 Nennungen in Wortform)

Einträge mit Dateiverweisen, die daneben Themen in Wortform nennen (29; auch diese Nennungen zählen nicht): binomische-formeln (7), bruchrechnung (2), brueche-dezimalzahlen (3), daten (5), einheiten (9), flaechen (7), koerper (5), kreis (6), kurvenuntersuchung (1), lineare-funktionen (1), lineare-gleichungen (2), lineare-gleichungssysteme (7), potenz-exponentialfunktionen (8), potenzen-wurzeln (5), prozentrechnung (2), pyramide-kegel-kugel (9), pythagoras (9), quadratische-funktionen (8), quadratische-gleichungen (8), rationale-zahlen (2), reelle-zahlen (6), strahlensaetze (9), symmetrie-abbildungen (7), trigonometrie (8), trigonometrische-funktionen (10), wahrscheinlichkeit (4), winkel-dreiecke (3), zinsrechnung (8), zuordnungen (2).

Einträge ohne Abschnitt „### Voraussetzungen (Blatt 0)“: 0.

Verweise auf Dateien, die kein Katalogeintrag sind: 1.
- abitur-vokabular.md ← binomialverteilung (liegt in abitur/)

## Schwäche der Messung
Die Zahlen messen, was in unseren Blatt-0-Abschnitten steht – also unsere eigene Sorgfalt beim Schreiben, nicht den Unterricht. Wo ein Eintrag seine Voraussetzungen sauber als Dateiverweise aufgelistet hat, steigen die Zahlen seiner Nachbarn; wo er sie in Wortform nennt oder weglässt, fehlen sie hier. Als Rangliste taugt die Messung, als Absolutwert nicht. Die Messlücken oben zeigen, wo sie blind ist.
