# Befund Bestand (Zählung, ohne Urteil)

Quelle A: Klon aufgabenbank, `bank/<eintrag>/` ohne `_basis`. Quelle B: Kataloge in mathe-nachhilfe. Erzeugt von `werkzeuge/bestand.py`.

## A. Aufgabenbank je Eintrag

Aufg = Zeilen in e<n>.jsonl; Zone = Zeilen zone.jsonl; Einh = Einheiten; Spr = Sprossen (Einheit, Kette, Sprosse); S1/S2/S3+ = Sprossen mit 1, 2, mindestens 3 Aufgaben (S3+ = Ersatz-fähig: nach der Blattaufgabe bleiben zwei für Rückblick und Check); Lücke = S1+S2; Vst-h = Zeilen mit hoehe vorstufe; Vst-f = Feld vorstufe; Tipp = Feld tipp; Weg = Zeilen weg.jsonl (angefangene Lösung/Weg); v2+ = Zeilen mit Variante ab 2; Kern = Zeilen hoehe grundfall; Mu = muster.md vorhanden.

| Eintrag | Aufg | Zone | Einh | Spr | S1 | S2 | S3+ | Lücke | Vst-h | Vst-f | Tipp | Weg | v2+ | Kern | Mu |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|:-:|
| lineare-gleichungssysteme | 300 | 48 | 5 | 103 | 21 | 5 | 77 | 26 | 32 | 0 | 0 | 0 | 197 | 41 | nein |
| einheiten | 288 | 46 | 4 | 96 | 6 | 10 | 80 | 16 | 32 | 0 | 0 | 0 | 192 | 35 | nein |
| lineare-gleichungen | 206 | 28 | 4 | 67 | 9 | 4 | 54 | 13 | 24 | 0 | 0 | 59 | 139 | 25 | ja |
| quadratische-funktionen | 267 | 46 | 4 | 85 | 0 | 9 | 76 | 9 | 18 | 0 | 0 | 58 | 182 | 20 | nein |
| daten | 528 | 55 | 7 | 162 | 0 | 5 | 157 | 5 | 48 | 0 | 0 | 0 | 366 | 56 | nein |
| zufallsexperimente-und-pfadregeln | 334 | 41 | 8 | 103 | 0 | 5 | 98 | 5 | 36 | 0 | 0 | 0 | 231 | 40 | ja |
| flaechen | 213 | 31 | 5 | 67 | 0 | 4 | 63 | 4 | 24 | 0 | 0 | 0 | 146 | 25 | nein |
| gleichungen-loesen | 185 | 38 | 4 | 59 | 0 | 4 | 55 | 4 | 16 | 0 | 0 | 0 | 126 | 20 | nein |
| wahrscheinlichkeit | 222 | 22 | 4 | 70 | 0 | 4 | 66 | 4 | 32 | 0 | 0 | 0 | 152 | 20 | nein |
| geraden | 155 | 30 | 4 | 47 | 0 | 3 | 44 | 3 | 32 | 0 | 0 | 0 | 108 | 20 | ja |
| kenngroessen-von-verteilungen | 160 | 26 | 4 | 50 | 0 | 3 | 47 | 3 | 16 | 0 | 0 | 0 | 110 | 20 | nein |
| koerper | 300 | 28 | 5 | 94 | 0 | 3 | 91 | 3 | 24 | 0 | 0 | 0 | 206 | 25 | nein |
| lagebeziehungen | 122 | 27 | 4 | 37 | 0 | 3 | 34 | 3 | 20 | 0 | 0 | 0 | 85 | 20 | ja |
| symmetrie-abbildungen | 219 | 30 | 3 | 69 | 0 | 3 | 66 | 3 | 24 | 0 | 0 | 0 | 150 | 20 | nein |
| zuordnungen | 237 | 23 | 4 | 70 | 0 | 3 | 67 | 3 | 40 | 0 | 0 | 0 | 167 | 30 | nein |
| ableitungsregeln | 112 | 30 | 3 | 34 | 0 | 2 | 32 | 2 | 20 | 0 | 0 | 0 | 78 | 15 | ja |
| bedingte-wahrscheinlichkeit-und-bayes | 88 | 27 | 3 | 27 | 0 | 2 | 25 | 2 | 12 | 0 | 0 | 0 | 61 | 15 | nein |
| brueche-dezimalzahlen | 287 | 30 | 5 | 82 | 0 | 2 | 80 | 2 | 28 | 0 | 0 | 0 | 205 | 30 | ja |
| ebenen | 181 | 30 | 4 | 55 | 0 | 2 | 53 | 2 | 20 | 0 | 0 | 0 | 126 | 25 | ja |
| hypergeometrische-verteilung | 43 | 19 | 2 | 13 | 0 | 2 | 11 | 2 | 8 | 0 | 0 | 0 | 30 | 10 | nein |
| hypothesentests | 91 | 22 | 3 | 27 | 0 | 2 | 25 | 2 | 12 | 0 | 0 | 0 | 64 | 15 | nein |
| kombinatorik | 110 | 22 | 3 | 34 | 0 | 2 | 32 | 2 | 12 | 0 | 0 | 0 | 76 | 15 | nein |
| normalverteilung-und-sigma-regeln | 77 | 27 | 3 | 23 | 0 | 2 | 21 | 2 | 12 | 0 | 0 | 0 | 54 | 15 | nein |
| orthogonalitaet | 138 | 26 | 4 | 41 | 0 | 2 | 39 | 2 | 28 | 0 | 0 | 0 | 97 | 20 | nein |
| scharen-von-geraden-und-ebenen | 129 | 28 | 4 | 38 | 0 | 2 | 36 | 2 | 20 | 0 | 0 | 0 | 91 | 20 | nein |
| schnittmengen | 99 | 26 | 3 | 30 | 0 | 2 | 28 | 2 | 16 | 0 | 0 | 0 | 69 | 15 | nein |
| skalarprodukt-und-winkel | 132 | 31 | 4 | 39 | 0 | 2 | 37 | 2 | 28 | 0 | 0 | 0 | 93 | 20 | ja |
| spiegelung | 91 | 26 | 3 | 27 | 0 | 2 | 25 | 2 | 20 | 0 | 0 | 0 | 64 | 15 | nein |
| unabhaengigkeit | 90 | 26 | 3 | 27 | 0 | 2 | 25 | 2 | 16 | 0 | 0 | 0 | 63 | 15 | nein |
| vierfeldertafel | 56 | 22 | 2 | 17 | 0 | 2 | 15 | 2 | 12 | 0 | 0 | 0 | 39 | 10 | nein |
| zufallsgroessen-und-verteilungen | 56 | 14 | 2 | 17 | 0 | 2 | 15 | 2 | 12 | 0 | 0 | 0 | 39 | 10 | nein |
| ableitung-und-aenderungsrate | 184 | 30 | 4 | 57 | 0 | 1 | 56 | 1 | 12 | 0 | 0 | 0 | 127 | 20 | ja |
| abstaende | 151 | 31 | 4 | 44 | 0 | 1 | 43 | 1 | 28 | 0 | 0 | 0 | 107 | 20 | ja |
| bruchrechnung | 242 | 26 | 5 | 68 | 0 | 1 | 67 | 1 | 28 | 0 | 0 | 0 | 174 | 30 | ja |
| grenzwerte-und-verhalten-im-unendlichen | 105 | 31 | 3 | 31 | 0 | 1 | 30 | 1 | 16 | 0 | 0 | 0 | 74 | 15 | nein |
| integrationsregeln | 41 | 15 | 2 | 12 | 0 | 1 | 11 | 1 | 8 | 0 | 0 | 0 | 29 | 10 | nein |
| kreis | 184 | 26 | 3 | 53 | 0 | 1 | 52 | 1 | 16 | 0 | 0 | 0 | 131 | 15 | nein |
| pyramide-kegel-kugel | 241 | 48 | 3 | 71 | 0 | 1 | 70 | 1 | 32 | 0 | 0 | 0 | 170 | 15 | nein |
| quadratische-gleichungen | 348 | 34 | 5 | 104 | 0 | 1 | 103 | 1 | 36 | 0 | 0 | 0 | 244 | 35 | nein |
| rekonstruktion-von-bestaenden | 100 | 22 | 3 | 30 | 0 | 1 | 29 | 1 | 8 | 0 | 0 | 0 | 70 | 15 | nein |
| strahlensaetze | 256 | 39 | 3 | 74 | 0 | 1 | 73 | 1 | 20 | 0 | 0 | 0 | 182 | 20 | nein |
| terme | 345 | 26 | 6 | 101 | 0 | 1 | 100 | 1 | 24 | 0 | 0 | 0 | 244 | 41 | ja |
| umkehrfunktion | 66 | 25 | 2 | 20 | 0 | 1 | 19 | 1 | 8 | 0 | 0 | 0 | 46 | 10 | nein |
| uneigentliche-integrale | 43 | 16 | 2 | 12 | 0 | 1 | 11 | 1 | 8 | 0 | 0 | 0 | 31 | 10 | nein |
| vektoren-und-rechenoperationen | 110 | 27 | 3 | 33 | 0 | 1 | 32 | 1 | 16 | 0 | 0 | 0 | 77 | 15 | ja |
| binomialverteilung | 257 | 37 | 5 | 72 | 0 | 0 | 72 | 0 | 24 | 0 | 0 | 0 | 185 | 25 | ja |
| binomische-formeln | 146 | 30 | 3 | 45 | 0 | 0 | 45 | 0 | 16 | 0 | 0 | 0 | 101 | 15 | ja |
| extremalprobleme | 114 | 26 | 3 | 34 | 0 | 0 | 34 | 0 | 12 | 0 | 0 | 0 | 80 | 15 | ja |
| flaecheninhalt-durch-integration | 213 | 26 | 5 | 55 | 0 | 0 | 55 | 0 | 20 | 0 | 0 | 0 | 158 | 25 | ja |
| flaecheninhalt-und-volumen-im-raum | 168 | 29 | 4 | 47 | 0 | 0 | 47 | 0 | 20 | 0 | 0 | 0 | 121 | 20 | nein |
| funktionsklassen-und-eigenschaften | 277 | 28 | 6 | 81 | 0 | 0 | 81 | 0 | 24 | 0 | 0 | 0 | 196 | 30 | ja |
| funktionsscharen-und-ortskurven | 192 | 30 | 5 | 57 | 0 | 0 | 57 | 0 | 16 | 0 | 0 | 0 | 135 | 25 | nein |
| konfidenzintervalle | 72 | 26 | 3 | 20 | 0 | 0 | 20 | 0 | 12 | 0 | 0 | 0 | 52 | 15 | nein |
| kurvenuntersuchung | 329 | 29 | 5 | 96 | 0 | 0 | 96 | 0 | 28 | 0 | 0 | 0 | 233 | 30 | ja |
| lineare-funktionen | 280 | 26 | 5 | 73 | 0 | 0 | 73 | 0 | 24 | 0 | 0 | 0 | 207 | 30 | nein |
| linearkombination-und-lineare-abhaengigkeit | 40 | 18 | 2 | 11 | 0 | 0 | 11 | 0 | 8 | 0 | 0 | 0 | 29 | 10 | nein |
| matrizen-und-uebergangsprozesse | 188 | 27 | 5 | 54 | 0 | 0 | 54 | 0 | 20 | 0 | 0 | 0 | 134 | 25 | nein |
| potenz-exponentialfunktionen | 402 | 62 | 5 | 115 | 0 | 0 | 115 | 0 | 44 | 0 | 0 | 0 | 287 | 55 | nein |
| potenzen-wurzeln | 226 | 46 | 3 | 64 | 0 | 0 | 64 | 0 | 24 | 0 | 0 | 0 | 162 | 15 | nein |
| prozentrechnung | 277 | 32 | 5 | 75 | 0 | 0 | 75 | 0 | 28 | 0 | 0 | 0 | 202 | 25 | ja |
| punkte-und-strecken-im-koordinatensystem | 212 | 43 | 5 | 60 | 0 | 0 | 60 | 0 | 20 | 0 | 0 | 0 | 152 | 25 | nein |
| pythagoras | 267 | 38 | 3 | 76 | 0 | 0 | 76 | 0 | 28 | 0 | 0 | 0 | 191 | 21 | ja |
| rationale-zahlen | 189 | 23 | 4 | 56 | 0 | 0 | 56 | 0 | 24 | 0 | 0 | 0 | 133 | 20 | ja |
| reelle-zahlen | 214 | 33 | 3 | 63 | 0 | 0 | 63 | 0 | 12 | 0 | 0 | 0 | 151 | 15 | nein |
| rekonstruktion-von-funktionsgleichungen | 119 | 27 | 3 | 35 | 0 | 0 | 35 | 0 | 12 | 0 | 0 | 0 | 84 | 15 | nein |
| rotationsvolumen | 62 | 25 | 2 | 18 | 0 | 0 | 18 | 0 | 8 | 0 | 0 | 0 | 44 | 10 | nein |
| stammfunktion-und-hauptsatz | 129 | 25 | 4 | 37 | 0 | 0 | 37 | 0 | 16 | 0 | 0 | 0 | 92 | 20 | ja |
| tangente-normale-schnittwinkel | 237 | 26 | 5 | 67 | 0 | 0 | 67 | 0 | 28 | 0 | 0 | 0 | 170 | 25 | ja |
| trigonometrie | 327 | 38 | 4 | 89 | 0 | 0 | 89 | 0 | 27 | 0 | 0 | 0 | 238 | 22 | nein |
| trigonometrische-funktionen | 222 | 46 | 4 | 70 | 0 | 0 | 70 | 0 | 16 | 0 | 0 | 0 | 152 | 20 | nein |
| winkel-dreiecke | 305 | 22 | 5 | 93 | 0 | 0 | 93 | 0 | 36 | 0 | 0 | 0 | 212 | 30 | nein |
| zinsrechnung | 146 | 35 | 2 | 42 | 0 | 0 | 42 | 0 | 13 | 0 | 0 | 0 | 104 | 15 | nein |
| **Summe (72 Einträge)** | 13542 | 2174 | 276 | 4025 | 36 | 114 | 3875 | 150 | 1514 | 0 | 0 | 117 | 9517 | 1551 | 24 |

Kernmarke: kein Feld in der Bank (Feldliste bank.md); ableitbar aus `hoehe == "grundfall"` (Spalte Kern), bei Bedarf plus `kette_nr`/`sprosse == 1`.

Verteilung Aufgaben je Sprosse (alle Einträge): 1: 36, 2: 114, 3: 2929, 4: 514, 5: 344, 6: 88 (6 = 6 und mehr)

### Einträge ohne muster.md

48 von 72: lineare-gleichungssysteme (300), einheiten (288), quadratische-funktionen (267), daten (528), flaechen (213), gleichungen-loesen (185), wahrscheinlichkeit (222), kenngroessen-von-verteilungen (160), koerper (300), symmetrie-abbildungen (219), zuordnungen (237), bedingte-wahrscheinlichkeit-und-bayes (88), hypergeometrische-verteilung (43), hypothesentests (91), kombinatorik (110), normalverteilung-und-sigma-regeln (77), orthogonalitaet (138), scharen-von-geraden-und-ebenen (129), schnittmengen (99), spiegelung (91), unabhaengigkeit (90), vierfeldertafel (56), zufallsgroessen-und-verteilungen (56), grenzwerte-und-verhalten-im-unendlichen (105), integrationsregeln (41), kreis (184), pyramide-kegel-kugel (241), quadratische-gleichungen (348), rekonstruktion-von-bestaenden (100), strahlensaetze (256), umkehrfunktion (66), uneigentliche-integrale (43), flaecheninhalt-und-volumen-im-raum (168), funktionsscharen-und-ortskurven (192), konfidenzintervalle (72), lineare-funktionen (280), linearkombination-und-lineare-abhaengigkeit (40), matrizen-und-uebergangsprozesse (188), potenz-exponentialfunktionen (402), potenzen-wurzeln (226), punkte-und-strecken-im-koordinatensystem (212), reelle-zahlen (214), rekonstruktion-von-funktionsgleichungen (119), rotationsvolumen (62), trigonometrie (327), trigonometrische-funktionen (222), winkel-dreiecke (305), zinsrechnung (146)

### Einträge mit vielen Sprossen unter 3 Aufgaben

Kriterium (Zählgrenze): mindestens 10 Sprossen unter 3 und mindestens die Hälfte aller Sprossen; Eintrag mit Anteil unter 3 und Zahl.

| Eintrag | Spr | unter 3 | Anteil |
|---|--:|--:|--:|
| (keiner) | | | |

0 Einträge. Einträge ohne jede Sprosse unter 3: binomialverteilung, binomische-formeln, extremalprobleme, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, funktionsklassen-und-eigenschaften, funktionsscharen-und-ortskurven, konfidenzintervalle, kurvenuntersuchung, lineare-funktionen, linearkombination-und-lineare-abhaengigkeit, matrizen-und-uebergangsprozesse, potenz-exponentialfunktionen, potenzen-wurzeln, prozentrechnung, punkte-und-strecken-im-koordinatensystem, pythagoras, rationale-zahlen, reelle-zahlen, rekonstruktion-von-funktionsgleichungen, rotationsvolumen, stammfunktion-und-hauptsatz, tangente-normale-schnittwinkel, trigonometrie, trigonometrische-funktionen, winkel-dreiecke, zinsrechnung

## B. Prüfungskataloge (mathe-nachhilfe)

Zeilen = Katalogzeilen; KL/ZW/NB/SW = Zahl Zeilen mit gefüllter kurzloesung/zwischenergebnis/neben/stichwoerter; ZW0..ZW3+ = Verteilung der Zwischenergebnisse je Zeile (Trenner `|`, nicht innerhalb von (…), […], ⟨…⟩); ZW>P-1 = Zeilen mit mehr Zwischenergebnissen als punkte − 1, Anteil an Zeilen mit lesbaren Punkten (P-ok).

| Katalog | Papier | Zeilen | KL | ZW | NB | SW | ZW0 | ZW1 | ZW2 | ZW3+ | P-ok | ZW>P-1 | Anteil |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| msa-katalog-basis.csv | EBR | 10 | 0 | 1 | 0 | 10 | 9 | 1 | 0 | 0 | 10 | 1 | 10 % |
| msa-katalog-basis.csv | FOR | 10 | 10 | 10 | 2 | 10 | 0 | 10 | 0 | 0 | 10 | 10 | 100 % |
| msa-katalog-basis.csv | OS | 116 | 116 | 45 | 36 | 116 | 71 | 42 | 3 | 0 | 116 | 42 | 36 % |
| msa-katalog-basis.csv | **alle** | 136 | 126 | 56 | 38 | 136 | 80 | 53 | 3 | 0 | 136 | 53 | 39 % |
| msa-katalog-kontext.csv | EBR | 15 | 0 | 4 | 0 | 15 | 11 | 4 | 0 | 0 | 15 | 0 | 0 % |
| msa-katalog-kontext.csv | FOR | 23 | 23 | 23 | 13 | 23 | 0 | 13 | 10 | 0 | 23 | 9 | 39 % |
| msa-katalog-kontext.csv | OS | 244 | 244 | 207 | 146 | 244 | 37 | 122 | 76 | 9 | 244 | 23 | 9 % |
| msa-katalog-kontext.csv | **alle** | 282 | 267 | 234 | 159 | 282 | 48 | 139 | 86 | 9 | 282 | 32 | 11 % |
| msa-katalog-gym.csv | GYM | 248 | 0 | 33 | 0 | 248 | 215 | 33 | 0 | 0 | 248 | 1 | 0 % |
| msa-katalog-gym.csv | **alle** | 248 | 0 | 33 | 0 | 248 | 215 | 33 | 0 | 0 | 248 | 1 | 0 % |
| abi-katalog.csv | 2017-bb-ea | 36 | 0 | 34 | 0 | 36 | 2 | 10 | 15 | 9 | 36 | 3 | 8 % |
| abi-katalog.csv | 2017-bb-ea-cas | 14 | 0 | 14 | 0 | 14 | 0 | 2 | 4 | 8 | 14 | 0 | 0 % |
| abi-katalog.csv | 2017-be-gk | 33 | 33 | 32 | 24 | 33 | 1 | 3 | 10 | 19 | 33 | 3 | 9 % |
| abi-katalog.csv | 2017-be-gk-cas | 16 | 16 | 16 | 13 | 16 | 0 | 1 | 3 | 12 | 16 | 2 | 12 % |
| abi-katalog.csv | 2018-bb-ea | 41 | 0 | 36 | 0 | 41 | 5 | 3 | 8 | 25 | 41 | 13 | 32 % |
| abi-katalog.csv | 2018-bb-ea-cas | 14 | 0 | 14 | 0 | 14 | 0 | 5 | 1 | 8 | 14 | 0 | 0 % |
| abi-katalog.csv | 2018-be-gk | 36 | 36 | 32 | 31 | 36 | 4 | 5 | 11 | 16 | 36 | 2 | 6 % |
| abi-katalog.csv | 2018-be-gk-cas | 16 | 16 | 15 | 14 | 16 | 1 | 0 | 3 | 12 | 16 | 1 | 6 % |
| abi-katalog.csv | 2019-be-gk | 45 | 45 | 35 | 36 | 45 | 10 | 10 | 14 | 11 | 45 | 5 | 11 % |
| abi-katalog.csv | 2020-be-gk | 51 | 51 | 40 | 39 | 51 | 11 | 10 | 19 | 11 | 51 | 6 | 12 % |
| abi-katalog.csv | 2021-be-gk | 56 | 56 | 40 | 43 | 56 | 16 | 13 | 15 | 12 | 56 | 8 | 14 % |
| abi-katalog.csv | 2022-bebb-gk | 57 | 57 | 43 | 54 | 57 | 14 | 22 | 16 | 5 | 57 | 2 | 4 % |
| abi-katalog.csv | 2022-bebb-lk | 68 | 0 | 28 | 0 | 68 | 40 | 27 | 0 | 1 | 68 | 2 | 3 % |
| abi-katalog.csv | 2023-bebb-gk | 58 | 58 | 48 | 47 | 58 | 10 | 20 | 27 | 1 | 58 | 7 | 12 % |
| abi-katalog.csv | 2023-bebb-lk | 66 | 0 | 20 | 0 | 66 | 46 | 20 | 0 | 0 | 66 | 2 | 3 % |
| abi-katalog.csv | 2024-bebb-gk | 47 | 47 | 36 | 37 | 47 | 11 | 17 | 15 | 4 | 47 | 3 | 6 % |
| abi-katalog.csv | 2024-bebb-lk | 53 | 0 | 17 | 0 | 53 | 36 | 16 | 1 | 0 | 53 | 0 | 0 % |
| abi-katalog.csv | 2025-bebb-gk | 39 | 39 | 28 | 34 | 39 | 11 | 13 | 14 | 1 | 39 | 3 | 8 % |
| abi-katalog.csv | 2025-bebb-lk | 46 | 0 | 16 | 0 | 46 | 30 | 11 | 4 | 1 | 46 | 3 | 7 % |
| abi-katalog.csv | 2026-bb-ea | 50 | 0 | 17 | 0 | 50 | 33 | 7 | 5 | 5 | 50 | 6 | 12 % |
| abi-katalog.csv | 2026-bb-gk | 45 | 45 | 38 | 39 | 45 | 7 | 14 | 19 | 5 | 45 | 8 | 18 % |
| abi-katalog.csv | **alle** | 887 | 499 | 599 | 411 | 887 | 288 | 229 | 204 | 166 | 887 | 79 | 9 % |
| iqb-katalog.csv | 2017-iqb-ea | 105 | 0 | 66 | 0 | 105 | 39 | 51 | 8 | 7 | 105 | 7 | 7 % |
| iqb-katalog.csv | 2017-iqb-ea-mms | 55 | 0 | 41 | 0 | 55 | 14 | 20 | 16 | 5 | 55 | 6 | 11 % |
| iqb-katalog.csv | 2017-iqb-ga | 59 | 0 | 47 | 0 | 59 | 12 | 30 | 13 | 4 | 59 | 7 | 12 % |
| iqb-katalog.csv | 2017-iqb-ga-mms | 38 | 0 | 31 | 0 | 38 | 7 | 15 | 10 | 6 | 38 | 5 | 13 % |
| iqb-katalog.csv | 2018-iqb-ea | 95 | 0 | 23 | 0 | 95 | 72 | 19 | 3 | 1 | 95 | 1 | 1 % |
| iqb-katalog.csv | 2018-iqb-ea-mms | 85 | 0 | 74 | 0 | 85 | 11 | 32 | 24 | 18 | 85 | 11 | 13 % |
| iqb-katalog.csv | 2018-iqb-ga | 78 | 0 | 13 | 0 | 78 | 65 | 11 | 2 | 0 | 78 | 0 | 0 % |
| iqb-katalog.csv | 2019-iqb-ea | 20 | 0 | 3 | 0 | 20 | 17 | 3 | 0 | 0 | 20 | 1 | 5 % |
| iqb-katalog.csv | 2019-iqb-ga | 89 | 0 | 17 | 0 | 89 | 72 | 17 | 0 | 0 | 89 | 0 | 0 % |
| iqb-katalog.csv | 2020-iqb-ea | 28 | 0 | 12 | 0 | 28 | 16 | 11 | 0 | 1 | 28 | 2 | 7 % |
| iqb-katalog.csv | 2020-iqb-ga | 66 | 0 | 17 | 0 | 66 | 49 | 16 | 1 | 0 | 66 | 0 | 0 % |
| iqb-katalog.csv | 2021-iqb-ea | 33 | 0 | 9 | 0 | 33 | 24 | 9 | 0 | 0 | 33 | 0 | 0 % |
| iqb-katalog.csv | 2021-iqb-ga | 70 | 0 | 17 | 0 | 70 | 53 | 15 | 2 | 0 | 70 | 0 | 0 % |
| iqb-katalog.csv | 2022-iqb-ea | 101 | 0 | 47 | 0 | 101 | 54 | 45 | 0 | 2 | 101 | 3 | 3 % |
| iqb-katalog.csv | 2022-iqb-ga | 76 | 0 | 12 | 0 | 76 | 64 | 11 | 1 | 0 | 76 | 0 | 0 % |
| iqb-katalog.csv | 2023-iqb-ea | 96 | 0 | 50 | 0 | 96 | 46 | 49 | 1 | 0 | 96 | 2 | 2 % |
| iqb-katalog.csv | 2023-iqb-ga | 85 | 0 | 49 | 0 | 85 | 36 | 47 | 2 | 0 | 85 | 2 | 2 % |
| iqb-katalog.csv | 2024-iqb-ea | 93 | 0 | 25 | 0 | 93 | 68 | 24 | 1 | 0 | 93 | 0 | 0 % |
| iqb-katalog.csv | 2024-iqb-ga | 79 | 0 | 23 | 0 | 79 | 56 | 23 | 0 | 0 | 79 | 3 | 4 % |
| iqb-katalog.csv | 2025-iqb-ea | 81 | 0 | 28 | 0 | 81 | 53 | 23 | 4 | 1 | 81 | 3 | 4 % |
| iqb-katalog.csv | 2025-iqb-ea-mms | 25 | 0 | 8 | 0 | 25 | 17 | 8 | 0 | 0 | 25 | 0 | 0 % |
| iqb-katalog.csv | 2025-iqb-ga | 73 | 0 | 27 | 0 | 73 | 46 | 20 | 4 | 3 | 73 | 4 | 5 % |
| iqb-katalog.csv | 2026-iqb-ea | 97 | 0 | 35 | 0 | 97 | 62 | 17 | 11 | 7 | 97 | 9 | 9 % |
| iqb-katalog.csv | 2026-iqb-ea-mms | 32 | 0 | 14 | 0 | 32 | 18 | 12 | 1 | 1 | 32 | 1 | 3 % |
| iqb-katalog.csv | 2026-iqb-ga | 78 | 0 | 35 | 0 | 78 | 43 | 18 | 8 | 9 | 78 | 10 | 13 % |
| iqb-katalog.csv | 2026-iqb-ga-mms | 25 | 0 | 20 | 0 | 25 | 5 | 20 | 0 | 0 | 25 | 0 | 0 % |
| iqb-katalog.csv | **alle** | 1762 | 0 | 743 | 0 | 1762 | 1019 | 566 | 112 | 65 | 1762 | 77 | 4 % |
| fhr-katalog.csv | A | 83 | 0 | 63 | 0 | 83 | 20 | 15 | 22 | 26 | 83 | 5 | 6 % |
| fhr-katalog.csv | B | 64 | 0 | 42 | 0 | 64 | 22 | 11 | 14 | 17 | 64 | 2 | 3 % |
| fhr-katalog.csv | C | 106 | 0 | 83 | 0 | 106 | 23 | 26 | 26 | 31 | 106 | 5 | 5 % |
| fhr-katalog.csv | **alle** | 253 | 0 | 188 | 0 | 253 | 65 | 52 | 62 | 74 | 253 | 12 | 5 % |
| **alle Kataloge** | | 3568 | 892 | 1853 | 608 | 3568 | 1715 | 1072 | 467 | 314 | 3568 | 254 | 7 % |

## Fünf Sätze (Zählung, ohne Urteil über Inhalte)

1. Musterbeispiele: 48 von 72 Einträgen haben keine muster.md; nach Aufgabenzahl fehlen sie am meisten bei daten (528), potenz-exponentialfunktionen (402), quadratische-gleichungen (348), trigonometrie (327) und quadratische-funktionen (267); die Zahl der Grundfall-Ketten (1551 Zeilen hoehe grundfall in 72 Einträgen) ist die Menge, für die Musterabschnitte gebraucht würden, die vorhandenen Abschnitte je Kette sind hier nicht gezählt.
2. Ersatzaufgaben: 3875 von 4025 Sprossen (96 %) haben mindestens 3 Aufgaben, 114 haben 2 und 36 nur 1; die Lücken (150 Sprossen) liegen vor allem in lineare-gleichungssysteme (26, davon 21 mit nur 1), einheiten (16), lineare-gleichungen (13) und quadratische-funktionen (9), 27 Einträge haben keine Sprosse unter 3.
3. Zwischenfragen: In den Katalogen haben 1715 von 3568 Zeilen (48 %) kein Zwischenergebnis, am dichtesten leer bei IQB (1019 von 1762), Gymnasial-Katalog (215 von 248), Abitur (288 von 887; bei den LK-Papieren der Jahre 2022 bis 2025 etwa zwei Drittel leer) und msa-katalog-basis OS (71 von 116).
4. Mehr Zwischenergebnisse als Punkte − 1 gibt es nur in 254 Zeilen (7 %), mit Ausnahme von msa-katalog-basis FOR (10 von 10) und OS-Basis (36 %); gut gefüllt für Zwischenfragen sind msa-katalog-kontext OS (207 von 244), FOR (23 von 23) und die Abitur-GK-Papiere (meist über 70 %).
5. Gerüst-Felder: In der Bank gibt es keine Kernmarke als Feld (ableitbar aus hoehe grundfall), keine angefangenen Lösungen außer 117 Zeilen in weg.jsonl (nur quadratische-funktionen und lineare-gleichungen), das Feld tipp nur an 36 Zeilen in zwei Einträgen und das Feld vorstufe nur an 66 Zeilen, während 1514 Zeilen die Höhe vorstufe tragen.
