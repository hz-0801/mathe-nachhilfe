# Tragfähigkeit der Themen – Nachfrage in Blatt 0
Stand 2026-09-21, Katalog auf Commit 4822149.
Erzeugt von `werkzeuge/tragfaehigkeit.py` (v0.1) aus den Blatt-0-Abschnitten der Einträge; abgeleitet, nie von Hand ändern. Der Katalog misst sonst nur Prüfungslast (Zeilen je Thema); hier steht die zweite Achse: wie oft ein Thema von anderen Einträgen gebraucht wird.

Gemessen: 73 Einträge (`katalog/*.md` ohne `_*` und `index.md`); je Eintrag der Abschnitt „### Voraussetzungen (Blatt 0)“ bis zur nächsten Überschrift, darin die Verweise der Form `<name>.md`, mit oder ohne Einheitsangabe. Ein Eintrag zählt je genanntem Thema einmal, gleich wie oft er es nennt; Selbstverweise zählen nicht; keine Gewichtung nach Einheit oder Profil. Zeilen = eigene Katalogzeilen, Summe der Spalte `zeilen` in `themen.csv` (Prüfungslast).

## A Nachfrage – wie oft ein Thema vorausgesetzt wird
Absteigend nach der Zahl der nachfragenden Einträge, bei Gleichstand alphabetisch; alle Einträge, auch die ohne Nachfrage. Hohe Nachfrage bei niedriger Zeilenzahl heißt: das Thema wird nie Stundenthema, kostet aber Zeit in jeder Stunde, in der es fehlt.

| Thema | Nachfrager | Zeilen | Nachfrager (Namen) |
|---|---|---|---|
| lineare-gleichungen | 16 | 9 | bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, daten, flaecheninhalt-und-volumen-im-raum, funktionsscharen-und-ortskurven, geraden, gleichungen-loesen, kenngroessen-von-verteilungen, lagebeziehungen, lineare-gleichungssysteme, matrizen-und-uebergangsprozesse, scharen-von-geraden-und-ebenen, unabhaengigkeit, vektoren-und-rechenoperationen, vierfeldertafel, zufallsexperimente-und-pfadregeln |
| gleichungen-loesen | 15 | 43 | ableitung-und-aenderungsrate, abstaende, bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, einheiten, extremalprobleme, flaecheninhalt-durch-integration, grenzwerte-und-verhalten-im-unendlichen, konfidenzintervalle, kurvenuntersuchung, lineare-gleichungssysteme, scharen-von-geraden-und-ebenen, tangente-normale-schnittwinkel, umkehrfunktion, zufallsexperimente-und-pfadregeln |
| potenzen-wurzeln | 15 | 12 | ableitungsregeln, daten, einheiten, funktionsklassen-und-eigenschaften, funktionsscharen-und-ortskurven, grenzwerte-und-verhalten-im-unendlichen, integrationsregeln, kenngroessen-von-verteilungen, kombinatorik, punkte-und-strecken-im-koordinatensystem, reelle-zahlen, stammfunktion-und-hauptsatz, vektoren-und-rechenoperationen, zinsrechnung, zufallsexperimente-und-pfadregeln |
| prozentrechnung | 15 | 23 | ableitung-und-aenderungsrate, bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, flaecheninhalt-und-volumen-im-raum, geraden, kenngroessen-von-verteilungen, kombinatorik, konfidenzintervalle, matrizen-und-uebergangsprozesse, normalverteilung-und-sigma-regeln, punkte-und-strecken-im-koordinatensystem, skalarprodukt-und-winkel, unabhaengigkeit, vierfeldertafel, zufallsexperimente-und-pfadregeln |
| lineare-funktionen | 14 | 28 | ableitung-und-aenderungsrate, ableitungsregeln, bedingte-wahrscheinlichkeit-und-bayes, ebenen, extremalprobleme, funktionsklassen-und-eigenschaften, geraden, gleichungen-loesen, hypothesentests, konfidenzintervalle, rekonstruktion-von-funktionsgleichungen, stammfunktion-und-hauptsatz, tangente-normale-schnittwinkel, umkehrfunktion |
| quadratische-gleichungen | 14 | 2 | abstaende, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, funktionsklassen-und-eigenschaften, funktionsscharen-und-ortskurven, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, kenngroessen-von-verteilungen, konfidenzintervalle, lagebeziehungen, orthogonalitaet, scharen-von-geraden-und-ebenen, unabhaengigkeit, zufallsexperimente-und-pfadregeln |
| punkte-und-strecken-im-koordinatensystem | 10 | 83 | ebenen, flaecheninhalt-und-volumen-im-raum, geraden, lagebeziehungen, lineare-gleichungssysteme, scharen-von-geraden-und-ebenen, schnittmengen, skalarprodukt-und-winkel, spiegelung, vektoren-und-rechenoperationen |
| pythagoras | 10 | 17 | abstaende, extremalprobleme, flaecheninhalt-und-volumen-im-raum, potenzen-wurzeln, punkte-und-strecken-im-koordinatensystem, reelle-zahlen, rotationsvolumen, tangente-normale-schnittwinkel, umkehrfunktion, vektoren-und-rechenoperationen |
| vektoren-und-rechenoperationen | 10 | 20 | abstaende, ebenen, flaecheninhalt-und-volumen-im-raum, geraden, linearkombination-und-lineare-abhaengigkeit, matrizen-und-uebergangsprozesse, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, skalarprodukt-und-winkel, spiegelung |
| ableitungsregeln | 9 | 24 | ableitung-und-aenderungsrate, extremalprobleme, funktionsscharen-und-ortskurven, gleichungen-loesen, integrationsregeln, kurvenuntersuchung, rekonstruktion-von-funktionsgleichungen, stammfunktion-und-hauptsatz, tangente-normale-schnittwinkel |
| bruchrechnung | 9 | 0 | ableitungsregeln, bedingte-wahrscheinlichkeit-und-bayes, daten, hypergeometrische-verteilung, kenngroessen-von-verteilungen, kombinatorik, unabhaengigkeit, zufallsexperimente-und-pfadregeln, zufallsgroessen-und-verteilungen |
| potenz-exponentialfunktionen | 9 | 21 | ableitung-und-aenderungsrate, ableitungsregeln, binomialverteilung, funktionsklassen-und-eigenschaften, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, matrizen-und-uebergangsprozesse, trigonometrische-funktionen, umkehrfunktion |
| skalarprodukt-und-winkel | 9 | 42 | abstaende, ebenen, flaecheninhalt-und-volumen-im-raum, geraden, lagebeziehungen, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, scharen-von-geraden-und-ebenen, vektoren-und-rechenoperationen |
| strahlensaetze | 9 | 0 | abstaende, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, funktionsklassen-und-eigenschaften, geraden, gleichungen-loesen, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, schnittmengen |
| wahrscheinlichkeit | 9 | 37 | binomialverteilung, hypothesentests, kenngroessen-von-verteilungen, kombinatorik, normalverteilung-und-sigma-regeln, unabhaengigkeit, vierfeldertafel, zufallsexperimente-und-pfadregeln, zufallsgroessen-und-verteilungen |
| ebenen | 8 | 48 | abstaende, lagebeziehungen, linearkombination-und-lineare-abhaengigkeit, orthogonalitaet, scharen-von-geraden-und-ebenen, schnittmengen, skalarprodukt-und-winkel, spiegelung |
| funktionsklassen-und-eigenschaften | 8 | 200 | ableitungsregeln, einheiten, flaecheninhalt-durch-integration, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, kurvenuntersuchung, rekonstruktion-von-bestaenden, rekonstruktion-von-funktionsgleichungen |
| quadratische-funktionen | 8 | 31 | ableitung-und-aenderungsrate, ableitungsregeln, funktionsklassen-und-eigenschaften, funktionsscharen-und-ortskurven, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, kurvenuntersuchung, rekonstruktion-von-funktionsgleichungen |
| terme | 8 | 4 | ableitungsregeln, extremalprobleme, funktionsscharen-und-ortskurven, gleichungen-loesen, integrationsregeln, lagebeziehungen, lineare-gleichungssysteme, vektoren-und-rechenoperationen |
| flaechen | 7 | 26 | einheiten, extremalprobleme, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, tangente-normale-schnittwinkel, umkehrfunktion |
| geraden | 7 | 36 | abstaende, ebenen, lagebeziehungen, linearkombination-und-lineare-abhaengigkeit, orthogonalitaet, schnittmengen, skalarprodukt-und-winkel |
| koerper | 7 | 28 | ebenen, einheiten, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, rotationsvolumen, schnittmengen, vektoren-und-rechenoperationen |
| lineare-gleichungssysteme | 7 | 20 | ebenen, linearkombination-und-lineare-abhaengigkeit, matrizen-und-uebergangsprozesse, orthogonalitaet, rekonstruktion-von-funktionsgleichungen, scharen-von-geraden-und-ebenen, schnittmengen |
| orthogonalitaet | 7 | 43 | abstaende, ebenen, flaecheninhalt-und-volumen-im-raum, geraden, lagebeziehungen, punkte-und-strecken-im-koordinatensystem, scharen-von-geraden-und-ebenen |
| binomialverteilung | 6 | 155 | hypergeometrische-verteilung, hypothesentests, kenngroessen-von-verteilungen, kombinatorik, konfidenzintervalle, normalverteilung-und-sigma-regeln |
| einheiten | 6 | 23 | ableitung-und-aenderungsrate, daten, flaecheninhalt-durch-integration, funktionsklassen-und-eigenschaften, rekonstruktion-von-bestaenden, rotationsvolumen |
| kreis | 6 | 0 | abstaende, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, skalarprodukt-und-winkel, zufallsexperimente-und-pfadregeln |
| kurvenuntersuchung | 6 | 150 | ableitung-und-aenderungsrate, ableitungsgraph-und-funktionsgraph, extremalprobleme, funktionsscharen-und-ortskurven, stammfunktion-und-hauptsatz, umkehrfunktion |
| stammfunktion-und-hauptsatz | 6 | 52 | flaecheninhalt-durch-integration, funktionsscharen-und-ortskurven, normalverteilung-und-sigma-regeln, rekonstruktion-von-bestaenden, rotationsvolumen, uneigentliche-integrale |
| symmetrie-abbildungen | 6 | 3 | funktionsklassen-und-eigenschaften, grenzwerte-und-verhalten-im-unendlichen, punkte-und-strecken-im-koordinatensystem, spiegelung, umkehrfunktion, vektoren-und-rechenoperationen |
| daten | 5 | 70 | bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, matrizen-und-uebergangsprozesse, vierfeldertafel, zufallsgroessen-und-verteilungen |
| linearkombination-und-lineare-abhaengigkeit | 5 | 1 | ebenen, geraden, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, scharen-von-geraden-und-ebenen |
| zufallsexperimente-und-pfadregeln | 5 | 237 | bedingte-wahrscheinlichkeit-und-bayes, hypergeometrische-verteilung, kombinatorik, unabhaengigkeit, vierfeldertafel |
| ableitung-und-aenderungsrate | 4 | 54 | ableitungsregeln, kurvenuntersuchung, rekonstruktion-von-bestaenden, tangente-normale-schnittwinkel |
| flaecheninhalt-durch-integration | 4 | 124 | einheiten, normalverteilung-und-sigma-regeln, umkehrfunktion, uneigentliche-integrale |
| pyramide-kegel-kugel | 4 | 0 | ebenen, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, rotationsvolumen |
| rationale-zahlen | 4 | 7 | funktionsklassen-und-eigenschaften, grenzwerte-und-verhalten-im-unendlichen, integrationsregeln, stammfunktion-und-hauptsatz |
| reelle-zahlen | 4 | 0 | ableitungsregeln, binomialverteilung, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen |
| trigonometrie | 4 | 28 | gleichungen-loesen, potenzen-wurzeln, skalarprodukt-und-winkel, tangente-normale-schnittwinkel |
| zuordnungen | 4 | 13 | ableitung-und-aenderungsrate, linearkombination-und-lineare-abhaengigkeit, rekonstruktion-von-bestaenden, vektoren-und-rechenoperationen |
| abstaende | 3 | 58 | flaecheninhalt-und-volumen-im-raum, scharen-von-geraden-und-ebenen, spiegelung |
| binomische-formeln | 3 | 0 | ableitungsregeln, gleichungen-loesen, rotationsvolumen |
| brueche-dezimalzahlen | 3 | 17 | ableitungsregeln, kombinatorik, zufallsexperimente-und-pfadregeln |
| grenzwerte-und-verhalten-im-unendlichen | 3 | 22 | gleichungen-loesen, umkehrfunktion, uneigentliche-integrale |
| kenngroessen-von-verteilungen | 3 | 73 | binomialverteilung, hypothesentests, normalverteilung-und-sigma-regeln |
| kombinatorik | 3 | 32 | binomialverteilung, hypergeometrische-verteilung, zufallsexperimente-und-pfadregeln |
| lagebeziehungen | 3 | 38 | lineare-gleichungssysteme, scharen-von-geraden-und-ebenen, schnittmengen |
| schnittmengen | 3 | 31 | lineare-gleichungssysteme, scharen-von-geraden-und-ebenen, spiegelung |
| trigonometrische-funktionen | 3 | 0 | funktionsklassen-und-eigenschaften, gleichungen-loesen, rekonstruktion-von-funktionsgleichungen |
| vierfeldertafel | 3 | 29 | bedingte-wahrscheinlichkeit-und-bayes, unabhaengigkeit, zufallsexperimente-und-pfadregeln |
| winkel-dreiecke | 3 | 19 | orthogonalitaet, punkte-und-strecken-im-koordinatensystem, skalarprodukt-und-winkel |
| ableitungsgraph-und-funktionsgraph | 2 | 21 | ableitung-und-aenderungsrate, stammfunktion-und-hauptsatz |
| bedingte-wahrscheinlichkeit-und-bayes | 2 | 39 | unabhaengigkeit, zufallsexperimente-und-pfadregeln |
| integrationsregeln | 2 | 2 | flaecheninhalt-durch-integration, stammfunktion-und-hauptsatz |
| tangente-normale-schnittwinkel | 2 | 127 | ableitungsregeln, stammfunktion-und-hauptsatz |
| funktionsscharen-und-ortskurven | 1 | 142 | lagebeziehungen |
| hypergeometrische-verteilung | 1 | 7 | binomialverteilung |
| normalverteilung-und-sigma-regeln | 1 | 20 | konfidenzintervalle |
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
| zinsrechnung | 0 | 5 | – |

## B Einstiegshürde – wie viele Themen ein Eintrag voraussetzt
Absteigend nach der Zahl der eigenen Voraussetzungen, bei Gleichstand alphabetisch – so viel muss ein Blatt 0 zu diesem Thema abdecken. Nur Einträge mit mindestens einem Verweis; für die 22 übrigen ist die Hürde nicht null, sondern ungemessen (siehe Messlücken).

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
| unabhaengigkeit | 8 | bedingte-wahrscheinlichkeit-und-bayes, bruchrechnung, lineare-gleichungen, prozentrechnung, quadratische-gleichungen, vierfeldertafel, wahrscheinlichkeit, zufallsexperimente-und-pfadregeln |
| extremalprobleme | 7 | ableitungsregeln, flaechen, gleichungen-loesen, kurvenuntersuchung, lineare-funktionen, pythagoras, terme |
| kombinatorik | 7 | binomialverteilung, bruchrechnung, brueche-dezimalzahlen, potenzen-wurzeln, prozentrechnung, wahrscheinlichkeit, zufallsexperimente-und-pfadregeln |
| schnittmengen | 7 | ebenen, geraden, koerper, lagebeziehungen, lineare-gleichungssysteme, punkte-und-strecken-im-koordinatensystem, strahlensaetze |
| tangente-normale-schnittwinkel | 7 | ableitung-und-aenderungsrate, ableitungsregeln, flaechen, gleichungen-loesen, lineare-funktionen, pythagoras, trigonometrie |
| einheiten | 6 | flaechen, flaecheninhalt-durch-integration, funktionsklassen-und-eigenschaften, gleichungen-loesen, koerper, potenzen-wurzeln |
| konfidenzintervalle | 6 | binomialverteilung, gleichungen-loesen, lineare-funktionen, normalverteilung-und-sigma-regeln, prozentrechnung, quadratische-gleichungen |
| lineare-gleichungssysteme | 6 | gleichungen-loesen, lagebeziehungen, lineare-gleichungen, punkte-und-strecken-im-koordinatensystem, schnittmengen, terme |
| matrizen-und-uebergangsprozesse | 6 | daten, lineare-gleichungen, lineare-gleichungssysteme, potenz-exponentialfunktionen, prozentrechnung, vektoren-und-rechenoperationen |
| normalverteilung-und-sigma-regeln | 6 | binomialverteilung, flaecheninhalt-durch-integration, kenngroessen-von-verteilungen, prozentrechnung, stammfunktion-und-hauptsatz, wahrscheinlichkeit |
| rekonstruktion-von-funktionsgleichungen | 6 | ableitungsregeln, funktionsklassen-und-eigenschaften, lineare-funktionen, lineare-gleichungssysteme, quadratische-funktionen, trigonometrische-funktionen |
| rotationsvolumen | 6 | binomische-formeln, einheiten, koerper, pyramide-kegel-kugel, pythagoras, stammfunktion-und-hauptsatz |
| spiegelung | 6 | abstaende, ebenen, punkte-und-strecken-im-koordinatensystem, schnittmengen, symmetrie-abbildungen, vektoren-und-rechenoperationen |
| kurvenuntersuchung | 5 | ableitung-und-aenderungsrate, ableitungsregeln, funktionsklassen-und-eigenschaften, gleichungen-loesen, quadratische-funktionen |
| linearkombination-und-lineare-abhaengigkeit | 5 | ebenen, geraden, lineare-gleichungssysteme, vektoren-und-rechenoperationen, zuordnungen |
| rekonstruktion-von-bestaenden | 5 | ableitung-und-aenderungsrate, einheiten, funktionsklassen-und-eigenschaften, stammfunktion-und-hauptsatz, zuordnungen |
| vierfeldertafel | 5 | daten, lineare-gleichungen, prozentrechnung, wahrscheinlichkeit, zufallsexperimente-und-pfadregeln |
| daten | 4 | bruchrechnung, einheiten, lineare-gleichungen, potenzen-wurzeln |
| hypergeometrische-verteilung | 4 | binomialverteilung, bruchrechnung, kombinatorik, zufallsexperimente-und-pfadregeln |
| hypothesentests | 4 | binomialverteilung, kenngroessen-von-verteilungen, lineare-funktionen, wahrscheinlichkeit |
| integrationsregeln | 4 | ableitungsregeln, potenzen-wurzeln, rationale-zahlen, terme |
| uneigentliche-integrale | 3 | flaecheninhalt-durch-integration, grenzwerte-und-verhalten-im-unendlichen, stammfunktion-und-hauptsatz |
| zufallsgroessen-und-verteilungen | 3 | bruchrechnung, daten, wahrscheinlichkeit |
| potenzen-wurzeln | 2 | pythagoras, trigonometrie |
| reelle-zahlen | 2 | potenzen-wurzeln, pythagoras |
| ableitungsgraph-und-funktionsgraph | 1 | kurvenuntersuchung |
| trigonometrische-funktionen | 1 | potenz-exponentialfunktionen |
| zinsrechnung | 1 | potenzen-wurzeln |

## Messlücken
Was die Messung nicht sieht – berichtet, nicht gestopft (kein Eintrag wird vom Werkzeug geändert).

Einträge ohne Verweis der Form `<name>.md` im Blatt-0-Abschnitt: 22 von 73. In Klammern die Nennungen in Wortform („Thema …“ vor einem Großbuchstaben, Heuristik) – die Nachfrage, die diese Einträge stellen, fehlt in Tabelle A ganz.
- binomische-formeln (7 Nennungen in Wortform)
- bruchrechnung (2 Nennungen in Wortform)
- brueche-dezimalzahlen (3 Nennungen in Wortform)
- flaechen (7 Nennungen in Wortform)
- koerper (5 Nennungen in Wortform)
- kreis (6 Nennungen in Wortform)
- lineare-funktionen (1 Nennung in Wortform)
- lineare-gleichungen (2 Nennungen in Wortform)
- potenz-exponentialfunktionen (8 Nennungen in Wortform)
- prozentrechnung (2 Nennungen in Wortform)
- pyramide-kegel-kugel (9 Nennungen in Wortform)
- pythagoras (9 Nennungen in Wortform)
- quadratische-funktionen (8 Nennungen in Wortform)
- quadratische-gleichungen (8 Nennungen in Wortform)
- rationale-zahlen (2 Nennungen in Wortform)
- strahlensaetze (9 Nennungen in Wortform)
- symmetrie-abbildungen (7 Nennungen in Wortform)
- terme (0 Nennungen in Wortform)
- trigonometrie (8 Nennungen in Wortform)
- wahrscheinlichkeit (4 Nennungen in Wortform)
- winkel-dreiecke (3 Nennungen in Wortform)
- zuordnungen (2 Nennungen in Wortform)

Einträge mit Dateiverweisen, die daneben Themen in Wortform nennen (8; auch diese Nennungen zählen nicht): daten (5), einheiten (9), kurvenuntersuchung (1), lineare-gleichungssysteme (7), potenzen-wurzeln (5), reelle-zahlen (6), trigonometrische-funktionen (10), zinsrechnung (8).

Einträge ohne Abschnitt „### Voraussetzungen (Blatt 0)“: 0.

Verweise auf Dateien, die kein Katalogeintrag sind: 1.
- abitur-vokabular.md ← binomialverteilung (liegt in abitur/)

## Schwäche der Messung
Die Zahlen messen, was in unseren Blatt-0-Abschnitten steht – also unsere eigene Sorgfalt beim Schreiben, nicht den Unterricht. Wo ein Eintrag seine Voraussetzungen sauber als Dateiverweise aufgelistet hat, steigen die Zahlen seiner Nachbarn; wo er sie in Wortform nennt oder weglässt, fehlen sie hier. Als Rangliste taugt die Messung, als Absolutwert nicht. Die Messlücken oben zeigen, wo sie blind ist.
