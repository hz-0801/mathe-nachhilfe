# Tragfähigkeit der Themen – Nachfrage in Blatt 0
Stand 2026-09-25, Katalog auf Commit f9632e3.
Erzeugt von `werkzeuge/tragfaehigkeit.py` (v0.2) aus den Blatt-0-Abschnitten der Einträge; abgeleitet, nie von Hand ändern. Der Katalog misst sonst nur Prüfungslast (Zeilen je Thema); hier steht die zweite Achse: wie oft ein Thema von anderen Einträgen gebraucht wird.

Gemessen: 73 Einträge (`katalog/*.md` ohne `_*` und `index.md`); je Eintrag der Abschnitt „### Voraussetzungen (Blatt 0)“ bis zur nächsten Überschrift, darin die Verweise der Form `<name>.md`, mit oder ohne Einheitsangabe. Ein Eintrag zählt je genanntem Thema einmal, gleich wie oft er es nennt; Selbstverweise zählen nicht; keine Gewichtung nach Einheit oder Profil. Zeilen = eigene Katalogzeilen, Summe der Spalte `zeilen` in `themen.csv` (Prüfungslast).

## A Nachfrage – wie oft ein Thema vorausgesetzt wird
Absteigend nach der Zahl der nachfragenden Einträge, bei Gleichstand alphabetisch; alle Einträge, auch die ohne Nachfrage. Hohe Nachfrage bei niedriger Zeilenzahl heißt: das Thema wird nie Stundenthema, kostet aber Zeit in jeder Stunde, in der es fehlt.

| Thema | Nachfrager | Zeilen | Nachfrager (Namen) |
|---|---|---|---|
| bruchrechnung | 28 | 0 | ableitungsregeln, bedingte-wahrscheinlichkeit-und-bayes, daten, einheiten, flaechen, hypergeometrische-verteilung, kenngroessen-von-verteilungen, koerper, kombinatorik, kreis, lineare-funktionen, lineare-gleichungen, lineare-gleichungssysteme, potenz-exponentialfunktionen, potenzen-wurzeln, prozentrechnung, pyramide-kegel-kugel, pythagoras, rationale-zahlen, reelle-zahlen, strahlensaetze, trigonometrische-funktionen, unabhaengigkeit, wahrscheinlichkeit, zinsrechnung, zufallsexperimente-und-pfadregeln, zufallsgroessen-und-verteilungen, zuordnungen |
| lineare-gleichungen | 27 | 9 | bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, daten, einheiten, flaechen, flaecheninhalt-und-volumen-im-raum, funktionsscharen-und-ortskurven, geraden, gleichungen-loesen, kenngroessen-von-verteilungen, koerper, kreis, lagebeziehungen, lineare-funktionen, lineare-gleichungssysteme, matrizen-und-uebergangsprozesse, pyramide-kegel-kugel, pythagoras, quadratische-funktionen, quadratische-gleichungen, scharen-von-geraden-und-ebenen, strahlensaetze, trigonometrie, unabhaengigkeit, vektoren-und-rechenoperationen, vierfeldertafel, zufallsexperimente-und-pfadregeln |
| potenzen-wurzeln | 24 | 12 | ableitungsregeln, binomische-formeln, daten, einheiten, flaechen, funktionsklassen-und-eigenschaften, funktionsscharen-und-ortskurven, grenzwerte-und-verhalten-im-unendlichen, integrationsregeln, kenngroessen-von-verteilungen, koerper, kombinatorik, kreis, potenz-exponentialfunktionen, punkte-und-strecken-im-koordinatensystem, pyramide-kegel-kugel, pythagoras, quadratische-funktionen, quadratische-gleichungen, reelle-zahlen, stammfunktion-und-hauptsatz, vektoren-und-rechenoperationen, zinsrechnung, zufallsexperimente-und-pfadregeln |
| prozentrechnung | 23 | 25 | ableitung-und-aenderungsrate, bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, brueche-dezimalzahlen, daten, einheiten, flaecheninhalt-und-volumen-im-raum, geraden, kenngroessen-von-verteilungen, koerper, kombinatorik, konfidenzintervalle, kreis, matrizen-und-uebergangsprozesse, normalverteilung-und-sigma-regeln, potenz-exponentialfunktionen, punkte-und-strecken-im-koordinatensystem, skalarprodukt-und-winkel, unabhaengigkeit, vierfeldertafel, wahrscheinlichkeit, zinsrechnung, zufallsexperimente-und-pfadregeln |
| brueche-dezimalzahlen | 20 | 18 | ableitungsregeln, bruchrechnung, daten, einheiten, kombinatorik, kreis, potenz-exponentialfunktionen, potenzen-wurzeln, prozentrechnung, pyramide-kegel-kugel, rationale-zahlen, reelle-zahlen, strahlensaetze, terme, trigonometrie, wahrscheinlichkeit, winkel-dreiecke, zinsrechnung, zufallsexperimente-und-pfadregeln, zuordnungen |
| lineare-funktionen | 20 | 30 | ableitung-und-aenderungsrate, ableitungsregeln, bedingte-wahrscheinlichkeit-und-bayes, ebenen, extremalprobleme, funktionsklassen-und-eigenschaften, geraden, gleichungen-loesen, hypothesentests, konfidenzintervalle, kurvenuntersuchung, lineare-gleichungssysteme, potenz-exponentialfunktionen, pythagoras, quadratische-funktionen, rekonstruktion-von-funktionsgleichungen, stammfunktion-und-hauptsatz, tangente-normale-schnittwinkel, trigonometrische-funktionen, umkehrfunktion |
| einheiten | 15 | 24 | ableitung-und-aenderungsrate, brueche-dezimalzahlen, daten, flaechen, flaecheninhalt-durch-integration, funktionsklassen-und-eigenschaften, koerper, pyramide-kegel-kugel, pythagoras, rekonstruktion-von-bestaenden, rotationsvolumen, strahlensaetze, trigonometrie, winkel-dreiecke, zuordnungen |
| gleichungen-loesen | 15 | 43 | ableitung-und-aenderungsrate, abstaende, bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, einheiten, extremalprobleme, flaecheninhalt-durch-integration, grenzwerte-und-verhalten-im-unendlichen, konfidenzintervalle, kurvenuntersuchung, lineare-gleichungssysteme, scharen-von-geraden-und-ebenen, tangente-normale-schnittwinkel, umkehrfunktion, zufallsexperimente-und-pfadregeln |
| kreis | 15 | 0 | abstaende, brueche-dezimalzahlen, daten, flaechen, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, koerper, punkte-und-strecken-im-koordinatensystem, pyramide-kegel-kugel, pythagoras, skalarprodukt-und-winkel, strahlensaetze, trigonometrische-funktionen, winkel-dreiecke, zufallsexperimente-und-pfadregeln |
| quadratische-gleichungen | 15 | 2 | abstaende, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, funktionsklassen-und-eigenschaften, funktionsscharen-und-ortskurven, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, kenngroessen-von-verteilungen, konfidenzintervalle, lagebeziehungen, orthogonalitaet, quadratische-funktionen, scharen-von-geraden-und-ebenen, unabhaengigkeit, zufallsexperimente-und-pfadregeln |
| rationale-zahlen | 15 | 8 | binomische-formeln, funktionsklassen-und-eigenschaften, grenzwerte-und-verhalten-im-unendlichen, integrationsregeln, lineare-funktionen, lineare-gleichungen, lineare-gleichungssysteme, potenzen-wurzeln, pythagoras, quadratische-funktionen, quadratische-gleichungen, reelle-zahlen, stammfunktion-und-hauptsatz, symmetrie-abbildungen, terme |
| terme | 15 | 4 | ableitungsregeln, binomische-formeln, extremalprobleme, funktionsscharen-und-ortskurven, gleichungen-loesen, integrationsregeln, lagebeziehungen, lineare-funktionen, lineare-gleichungen, lineare-gleichungssysteme, pyramide-kegel-kugel, quadratische-gleichungen, rationale-zahlen, reelle-zahlen, vektoren-und-rechenoperationen |
| flaechen | 13 | 27 | einheiten, extremalprobleme, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, koerper, kreis, punkte-und-strecken-im-koordinatensystem, pyramide-kegel-kugel, pythagoras, symmetrie-abbildungen, tangente-normale-schnittwinkel, trigonometrie, umkehrfunktion |
| pythagoras | 12 | 19 | abstaende, extremalprobleme, flaecheninhalt-und-volumen-im-raum, potenzen-wurzeln, punkte-und-strecken-im-koordinatensystem, pyramide-kegel-kugel, reelle-zahlen, rotationsvolumen, tangente-normale-schnittwinkel, trigonometrie, umkehrfunktion, vektoren-und-rechenoperationen |
| winkel-dreiecke | 12 | 21 | daten, einheiten, flaechen, kreis, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, pythagoras, skalarprodukt-und-winkel, strahlensaetze, symmetrie-abbildungen, trigonometrie, trigonometrische-funktionen |
| quadratische-funktionen | 11 | 33 | ableitung-und-aenderungsrate, ableitungsregeln, binomische-formeln, funktionsklassen-und-eigenschaften, funktionsscharen-und-ortskurven, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, kurvenuntersuchung, quadratische-gleichungen, rekonstruktion-von-funktionsgleichungen, trigonometrische-funktionen |
| punkte-und-strecken-im-koordinatensystem | 10 | 83 | ebenen, flaecheninhalt-und-volumen-im-raum, geraden, lagebeziehungen, lineare-gleichungssysteme, scharen-von-geraden-und-ebenen, schnittmengen, skalarprodukt-und-winkel, spiegelung, vektoren-und-rechenoperationen |
| vektoren-und-rechenoperationen | 10 | 20 | abstaende, ebenen, flaecheninhalt-und-volumen-im-raum, geraden, linearkombination-und-lineare-abhaengigkeit, matrizen-und-uebergangsprozesse, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, skalarprodukt-und-winkel, spiegelung |
| zuordnungen | 10 | 10 | ableitung-und-aenderungsrate, lineare-funktionen, linearkombination-und-lineare-abhaengigkeit, potenz-exponentialfunktionen, prozentrechnung, rekonstruktion-von-bestaenden, strahlensaetze, trigonometrische-funktionen, vektoren-und-rechenoperationen, zinsrechnung |
| ableitungsregeln | 9 | 24 | ableitung-und-aenderungsrate, extremalprobleme, funktionsscharen-und-ortskurven, gleichungen-loesen, integrationsregeln, kurvenuntersuchung, rekonstruktion-von-funktionsgleichungen, stammfunktion-und-hauptsatz, tangente-normale-schnittwinkel |
| koerper | 9 | 31 | ebenen, einheiten, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, pyramide-kegel-kugel, rotationsvolumen, schnittmengen, strahlensaetze, vektoren-und-rechenoperationen |
| potenz-exponentialfunktionen | 9 | 23 | ableitung-und-aenderungsrate, ableitungsregeln, binomialverteilung, funktionsklassen-und-eigenschaften, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, matrizen-und-uebergangsprozesse, trigonometrische-funktionen, umkehrfunktion |
| skalarprodukt-und-winkel | 9 | 42 | abstaende, ebenen, flaecheninhalt-und-volumen-im-raum, geraden, lagebeziehungen, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, scharen-von-geraden-und-ebenen, vektoren-und-rechenoperationen |
| strahlensaetze | 9 | 3 | abstaende, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, funktionsklassen-und-eigenschaften, geraden, gleichungen-loesen, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, schnittmengen |
| symmetrie-abbildungen | 9 | 3 | funktionsklassen-und-eigenschaften, grenzwerte-und-verhalten-im-unendlichen, lineare-funktionen, punkte-und-strecken-im-koordinatensystem, spiegelung, trigonometrische-funktionen, umkehrfunktion, vektoren-und-rechenoperationen, zuordnungen |
| wahrscheinlichkeit | 9 | 39 | binomialverteilung, hypothesentests, kenngroessen-von-verteilungen, kombinatorik, normalverteilung-und-sigma-regeln, unabhaengigkeit, vierfeldertafel, zufallsexperimente-und-pfadregeln, zufallsgroessen-und-verteilungen |
| daten | 8 | 73 | bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, matrizen-und-uebergangsprozesse, trigonometrische-funktionen, vierfeldertafel, wahrscheinlichkeit, zinsrechnung, zufallsgroessen-und-verteilungen |
| ebenen | 8 | 48 | abstaende, lagebeziehungen, linearkombination-und-lineare-abhaengigkeit, orthogonalitaet, scharen-von-geraden-und-ebenen, schnittmengen, skalarprodukt-und-winkel, spiegelung |
| funktionsklassen-und-eigenschaften | 8 | 200 | ableitungsregeln, einheiten, flaecheninhalt-durch-integration, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, kurvenuntersuchung, rekonstruktion-von-bestaenden, rekonstruktion-von-funktionsgleichungen |
| lineare-gleichungssysteme | 8 | 20 | ebenen, linearkombination-und-lineare-abhaengigkeit, matrizen-und-uebergangsprozesse, orthogonalitaet, quadratische-funktionen, rekonstruktion-von-funktionsgleichungen, scharen-von-geraden-und-ebenen, schnittmengen |
| geraden | 7 | 36 | abstaende, ebenen, lagebeziehungen, linearkombination-und-lineare-abhaengigkeit, orthogonalitaet, schnittmengen, skalarprodukt-und-winkel |
| orthogonalitaet | 7 | 43 | abstaende, ebenen, flaecheninhalt-und-volumen-im-raum, geraden, lagebeziehungen, punkte-und-strecken-im-koordinatensystem, scharen-von-geraden-und-ebenen |
| binomialverteilung | 6 | 155 | hypergeometrische-verteilung, hypothesentests, kenngroessen-von-verteilungen, kombinatorik, konfidenzintervalle, normalverteilung-und-sigma-regeln |
| kurvenuntersuchung | 6 | 150 | ableitung-und-aenderungsrate, ableitungsgraph-und-funktionsgraph, extremalprobleme, funktionsscharen-und-ortskurven, stammfunktion-und-hauptsatz, umkehrfunktion |
| stammfunktion-und-hauptsatz | 6 | 52 | flaecheninhalt-durch-integration, funktionsscharen-und-ortskurven, normalverteilung-und-sigma-regeln, rekonstruktion-von-bestaenden, rotationsvolumen, uneigentliche-integrale |
| binomische-formeln | 5 | 0 | ableitungsregeln, gleichungen-loesen, quadratische-funktionen, quadratische-gleichungen, rotationsvolumen |
| linearkombination-und-lineare-abhaengigkeit | 5 | 1 | ebenen, geraden, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, scharen-von-geraden-und-ebenen |
| pyramide-kegel-kugel | 5 | 0 | ebenen, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, pythagoras, rotationsvolumen |
| trigonometrie | 5 | 29 | gleichungen-loesen, potenzen-wurzeln, skalarprodukt-und-winkel, tangente-normale-schnittwinkel, trigonometrische-funktionen |
| zufallsexperimente-und-pfadregeln | 5 | 237 | bedingte-wahrscheinlichkeit-und-bayes, hypergeometrische-verteilung, kombinatorik, unabhaengigkeit, vierfeldertafel |
| ableitung-und-aenderungsrate | 4 | 54 | ableitungsregeln, kurvenuntersuchung, rekonstruktion-von-bestaenden, tangente-normale-schnittwinkel |
| flaecheninhalt-durch-integration | 4 | 124 | einheiten, normalverteilung-und-sigma-regeln, umkehrfunktion, uneigentliche-integrale |
| reelle-zahlen | 4 | 0 | ableitungsregeln, binomialverteilung, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen |
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
Absteigend nach der Zahl der eigenen Voraussetzungen, bei Gleichstand alphabetisch – so viel muss ein Blatt 0 zu diesem Thema abdecken. Nur Einträge mit mindestens einem Verweis; für die 0 übrigen ist die Hürde nicht null, sondern ungemessen (siehe Messlücken).

| Thema | Voraussetzungen | Voraussetzungen (Namen) |
|---|---|---|
| flaecheninhalt-und-volumen-im-raum | 14 | abstaende, flaechen, koerper, kreis, lineare-gleichungen, orthogonalitaet, prozentrechnung, punkte-und-strecken-im-koordinatensystem, pyramide-kegel-kugel, pythagoras, quadratische-gleichungen, skalarprodukt-und-winkel, strahlensaetze, vektoren-und-rechenoperationen |
| gleichungen-loesen | 14 | ableitungsregeln, binomische-formeln, funktionsklassen-und-eigenschaften, grenzwerte-und-verhalten-im-unendlichen, lineare-funktionen, lineare-gleichungen, potenz-exponentialfunktionen, quadratische-funktionen, quadratische-gleichungen, reelle-zahlen, strahlensaetze, terme, trigonometrie, trigonometrische-funktionen |
| punkte-und-strecken-im-koordinatensystem | 14 | flaechen, koerper, kreis, linearkombination-und-lineare-abhaengigkeit, orthogonalitaet, potenzen-wurzeln, prozentrechnung, pyramide-kegel-kugel, pythagoras, skalarprodukt-und-winkel, strahlensaetze, symmetrie-abbildungen, vektoren-und-rechenoperationen, winkel-dreiecke |
| ableitungsregeln | 12 | ableitung-und-aenderungsrate, binomische-formeln, bruchrechnung, brueche-dezimalzahlen, funktionsklassen-und-eigenschaften, lineare-funktionen, potenz-exponentialfunktionen, potenzen-wurzeln, quadratische-funktionen, reelle-zahlen, tangente-normale-schnittwinkel, terme |
| scharen-von-geraden-und-ebenen | 12 | abstaende, ebenen, gleichungen-loesen, lagebeziehungen, lineare-gleichungen, lineare-gleichungssysteme, linearkombination-und-lineare-abhaengigkeit, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, quadratische-gleichungen, schnittmengen, skalarprodukt-und-winkel |
| zufallsexperimente-und-pfadregeln | 12 | bedingte-wahrscheinlichkeit-und-bayes, bruchrechnung, brueche-dezimalzahlen, gleichungen-loesen, kombinatorik, kreis, lineare-gleichungen, potenzen-wurzeln, prozentrechnung, quadratische-gleichungen, vierfeldertafel, wahrscheinlichkeit |
| einheiten | 11 | bruchrechnung, brueche-dezimalzahlen, flaechen, flaecheninhalt-durch-integration, funktionsklassen-und-eigenschaften, gleichungen-loesen, koerper, lineare-gleichungen, potenzen-wurzeln, prozentrechnung, winkel-dreiecke |
| ableitung-und-aenderungsrate | 10 | ableitungsgraph-und-funktionsgraph, ableitungsregeln, einheiten, gleichungen-loesen, kurvenuntersuchung, lineare-funktionen, potenz-exponentialfunktionen, prozentrechnung, quadratische-funktionen, zuordnungen |
| abstaende | 10 | ebenen, geraden, gleichungen-loesen, kreis, orthogonalitaet, pythagoras, quadratische-gleichungen, skalarprodukt-und-winkel, strahlensaetze, vektoren-und-rechenoperationen |
| binomialverteilung | 10 | daten, gleichungen-loesen, hypergeometrische-verteilung, kenngroessen-von-verteilungen, kombinatorik, lineare-gleichungen, potenz-exponentialfunktionen, prozentrechnung, reelle-zahlen, wahrscheinlichkeit |
| ebenen | 10 | geraden, koerper, lineare-funktionen, lineare-gleichungssysteme, linearkombination-und-lineare-abhaengigkeit, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, pyramide-kegel-kugel, skalarprodukt-und-winkel, vektoren-und-rechenoperationen |
| funktionsklassen-und-eigenschaften | 10 | einheiten, lineare-funktionen, potenz-exponentialfunktionen, potenzen-wurzeln, quadratische-funktionen, quadratische-gleichungen, rationale-zahlen, strahlensaetze, symmetrie-abbildungen, trigonometrische-funktionen |
| pyramide-kegel-kugel | 10 | bruchrechnung, brueche-dezimalzahlen, einheiten, flaechen, koerper, kreis, lineare-gleichungen, potenzen-wurzeln, pythagoras, terme |
| pythagoras | 10 | bruchrechnung, einheiten, flaechen, kreis, lineare-funktionen, lineare-gleichungen, potenzen-wurzeln, pyramide-kegel-kugel, rationale-zahlen, winkel-dreiecke |
| trigonometrische-funktionen | 10 | bruchrechnung, daten, kreis, lineare-funktionen, potenz-exponentialfunktionen, quadratische-funktionen, symmetrie-abbildungen, trigonometrie, winkel-dreiecke, zuordnungen |
| flaecheninhalt-durch-integration | 9 | einheiten, flaechen, funktionsklassen-und-eigenschaften, gleichungen-loesen, integrationsregeln, kreis, quadratische-gleichungen, stammfunktion-und-hauptsatz, strahlensaetze |
| geraden | 9 | lineare-funktionen, lineare-gleichungen, linearkombination-und-lineare-abhaengigkeit, orthogonalitaet, prozentrechnung, punkte-und-strecken-im-koordinatensystem, skalarprodukt-und-winkel, strahlensaetze, vektoren-und-rechenoperationen |
| grenzwerte-und-verhalten-im-unendlichen | 9 | funktionsklassen-und-eigenschaften, gleichungen-loesen, potenz-exponentialfunktionen, potenzen-wurzeln, quadratische-funktionen, quadratische-gleichungen, rationale-zahlen, reelle-zahlen, symmetrie-abbildungen |
| lagebeziehungen | 9 | ebenen, funktionsscharen-und-ortskurven, geraden, lineare-gleichungen, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, quadratische-gleichungen, skalarprodukt-und-winkel, terme |
| lineare-gleichungssysteme | 9 | bruchrechnung, gleichungen-loesen, lagebeziehungen, lineare-funktionen, lineare-gleichungen, punkte-und-strecken-im-koordinatensystem, rationale-zahlen, schnittmengen, terme |
| orthogonalitaet | 9 | ebenen, geraden, lineare-gleichungssysteme, linearkombination-und-lineare-abhaengigkeit, quadratische-gleichungen, skalarprodukt-und-winkel, strahlensaetze, vektoren-und-rechenoperationen, winkel-dreiecke |
| umkehrfunktion | 9 | flaechen, flaecheninhalt-durch-integration, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, kurvenuntersuchung, lineare-funktionen, potenz-exponentialfunktionen, pythagoras, symmetrie-abbildungen |
| vektoren-und-rechenoperationen | 9 | koerper, lineare-gleichungen, potenzen-wurzeln, punkte-und-strecken-im-koordinatensystem, pythagoras, skalarprodukt-und-winkel, symmetrie-abbildungen, terme, zuordnungen |
| bedingte-wahrscheinlichkeit-und-bayes | 8 | bruchrechnung, daten, gleichungen-loesen, lineare-funktionen, lineare-gleichungen, prozentrechnung, vierfeldertafel, zufallsexperimente-und-pfadregeln |
| daten | 8 | bruchrechnung, brueche-dezimalzahlen, einheiten, kreis, lineare-gleichungen, potenzen-wurzeln, prozentrechnung, winkel-dreiecke |
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
| flaechen | 6 | bruchrechnung, einheiten, kreis, lineare-gleichungen, potenzen-wurzeln, winkel-dreiecke |
| konfidenzintervalle | 6 | binomialverteilung, gleichungen-loesen, lineare-funktionen, normalverteilung-und-sigma-regeln, prozentrechnung, quadratische-gleichungen |
| kurvenuntersuchung | 6 | ableitung-und-aenderungsrate, ableitungsregeln, funktionsklassen-und-eigenschaften, gleichungen-loesen, lineare-funktionen, quadratische-funktionen |
| lineare-funktionen | 6 | bruchrechnung, lineare-gleichungen, rationale-zahlen, symmetrie-abbildungen, terme, zuordnungen |
| matrizen-und-uebergangsprozesse | 6 | daten, lineare-gleichungen, lineare-gleichungssysteme, potenz-exponentialfunktionen, prozentrechnung, vektoren-und-rechenoperationen |
| normalverteilung-und-sigma-regeln | 6 | binomialverteilung, flaecheninhalt-durch-integration, kenngroessen-von-verteilungen, prozentrechnung, stammfunktion-und-hauptsatz, wahrscheinlichkeit |
| quadratische-gleichungen | 6 | binomische-formeln, lineare-gleichungen, potenzen-wurzeln, quadratische-funktionen, rationale-zahlen, terme |
| reelle-zahlen | 6 | bruchrechnung, brueche-dezimalzahlen, potenzen-wurzeln, pythagoras, rationale-zahlen, terme |
| rekonstruktion-von-funktionsgleichungen | 6 | ableitungsregeln, funktionsklassen-und-eigenschaften, lineare-funktionen, lineare-gleichungssysteme, quadratische-funktionen, trigonometrische-funktionen |
| rotationsvolumen | 6 | binomische-formeln, einheiten, koerper, pyramide-kegel-kugel, pythagoras, stammfunktion-und-hauptsatz |
| spiegelung | 6 | abstaende, ebenen, punkte-und-strecken-im-koordinatensystem, schnittmengen, symmetrie-abbildungen, vektoren-und-rechenoperationen |
| trigonometrie | 6 | brueche-dezimalzahlen, einheiten, flaechen, lineare-gleichungen, pythagoras, winkel-dreiecke |
| zinsrechnung | 6 | bruchrechnung, brueche-dezimalzahlen, daten, potenzen-wurzeln, prozentrechnung, zuordnungen |
| linearkombination-und-lineare-abhaengigkeit | 5 | ebenen, geraden, lineare-gleichungssysteme, vektoren-und-rechenoperationen, zuordnungen |
| potenzen-wurzeln | 5 | bruchrechnung, brueche-dezimalzahlen, pythagoras, rationale-zahlen, trigonometrie |
| rekonstruktion-von-bestaenden | 5 | ableitung-und-aenderungsrate, einheiten, funktionsklassen-und-eigenschaften, stammfunktion-und-hauptsatz, zuordnungen |
| vierfeldertafel | 5 | daten, lineare-gleichungen, prozentrechnung, wahrscheinlichkeit, zufallsexperimente-und-pfadregeln |
| binomische-formeln | 4 | potenzen-wurzeln, quadratische-funktionen, rationale-zahlen, terme |
| hypergeometrische-verteilung | 4 | binomialverteilung, bruchrechnung, kombinatorik, zufallsexperimente-und-pfadregeln |
| hypothesentests | 4 | binomialverteilung, kenngroessen-von-verteilungen, lineare-funktionen, wahrscheinlichkeit |
| integrationsregeln | 4 | ableitungsregeln, potenzen-wurzeln, rationale-zahlen, terme |
| wahrscheinlichkeit | 4 | bruchrechnung, brueche-dezimalzahlen, daten, prozentrechnung |
| zuordnungen | 4 | bruchrechnung, brueche-dezimalzahlen, einheiten, symmetrie-abbildungen |
| brueche-dezimalzahlen | 3 | einheiten, kreis, prozentrechnung |
| lineare-gleichungen | 3 | bruchrechnung, rationale-zahlen, terme |
| prozentrechnung | 3 | bruchrechnung, brueche-dezimalzahlen, zuordnungen |
| rationale-zahlen | 3 | bruchrechnung, brueche-dezimalzahlen, terme |
| symmetrie-abbildungen | 3 | flaechen, rationale-zahlen, winkel-dreiecke |
| uneigentliche-integrale | 3 | flaecheninhalt-durch-integration, grenzwerte-und-verhalten-im-unendlichen, stammfunktion-und-hauptsatz |
| winkel-dreiecke | 3 | brueche-dezimalzahlen, einheiten, kreis |
| zufallsgroessen-und-verteilungen | 3 | bruchrechnung, daten, wahrscheinlichkeit |
| terme | 2 | brueche-dezimalzahlen, rationale-zahlen |
| ableitungsgraph-und-funktionsgraph | 1 | kurvenuntersuchung |
| bruchrechnung | 1 | brueche-dezimalzahlen |

## Messlücken
Was die Messung nicht sieht – berichtet, nicht gestopft (kein Eintrag wird vom Werkzeug geändert).

Einträge ohne Verweis der Form `<name>.md` im Blatt-0-Abschnitt: 0 von 73. In Klammern die Nennungen in Wortform („Thema …“ vor einem Großbuchstaben, Heuristik; folgt dem Titel unmittelbar „ (<name>.md“ wie in „Thema Terme (terme.md), Einheit 2“, ist es ein Verweis und keine Nennung in Wortform) – die Nachfrage, die diese Einträge stellen, fehlt in Tabelle A ganz.
- keine

Kein Eintrag mit Dateiverweisen nennt daneben Themen in Wortform.

Einträge ohne Abschnitt „### Voraussetzungen (Blatt 0)“: 0.

Verweise auf Dateien, die kein Katalogeintrag sind: 1.
- abitur-vokabular.md ← binomialverteilung (liegt in abitur/)

## Schwäche der Messung
Die Zahlen messen, was in unseren Blatt-0-Abschnitten steht – also unsere eigene Sorgfalt beim Schreiben, nicht den Unterricht. Wo ein Eintrag seine Voraussetzungen sauber als Dateiverweise aufgelistet hat, steigen die Zahlen seiner Nachbarn; wo er sie in Wortform nennt oder weglässt, fehlen sie hier. Die Wortform-Heuristik sieht nur das Wort „Thema“ vor einem Großbuchstaben: Nennungen ohne dieses Wort übersieht sie, und den Dateiverweis einer Nennung erkennt sie nur in der Klammer unmittelbar hinter dem Titel („Thema Terme (terme.md)“). Als Rangliste taugt die Messung, als Absolutwert nicht. Die Messlücken oben zeigen, wo sie blind ist.
