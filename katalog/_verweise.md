# Verweise und Namen – Prüfung des Themenkatalogs
Stand 2026-09-21, Katalog auf Commit ae3d874.
Erzeugt von `werkzeuge/verweis-pruef.py` (v0.1) aus den Einträgen, `themen.csv`, `abitur/abitur-vokabular.md`, den vier `abitur/abi-*-geltung.md` und den Typenkatalogen `msa/msa-typen.csv` und `fhr/fhr-typen.csv`; abgeleitet, nie von Hand ändern. Fünf Prüfungen der inneren Stimmigkeit vor dem Umbau der Blatt-Prompte: Dateiverweise, Einheitennummern, Namensgleichheit, Gegenrichtung, Formlücke. Befunde werden berichtet, nicht behoben; wo eine Zuordnung nicht eindeutig ist, steht der Fall in einer eigenen Liste statt in einer Entscheidung.

Gemessen: 73 Einträge (`katalog/*.md` ohne `_*` und `index.md`). Lesarten wie in `werkzeuge/tragfaehigkeit.py` (v0.1), importiert, nicht nachgebaut: Verweis = Zeichenkette der Form `<name>.md` (auch in Klammern oder Backticks; ein Pfad davor wird mitgenommen), Blatt-0-Abschnitt = „### Voraussetzungen (Blatt 0)“ bis zur nächsten Überschrift, Nennung in Wortform = „Thema “ vor einem Großbuchstaben (Heuristik), Fundort einer Datei außerhalb von `katalog/` = Suche im Repo nach dem Dateinamen. Abschnitt einer Fundstelle = die nächste Überschrift davor (#, ##, ###); in den Listen abgekürzt: Kopf (Titel und Statuszeilen), Verortung, Lerneinheiten, Typen (Typen je Lerneinheit), Blatt 0, Merkkasten, Fehler (Typische Fehler), Schwache (Für schwache Schüler), Prüfungsform, Offene Punkte, Prüfliste. Zeilennummern zählen ab 1 in der Datei. Zahl der Lerneinheiten eines Eintrags = Zeilen im Abschnitt „### Lerneinheiten“, die mit „<n>. “ beginnen.

## 1 Dateiverweise
Jeder Verweis `<name>.md` in jedem Abschnitt jedes Eintrags, nicht nur in Blatt 0. Gruppe (a): das Ziel liegt in `katalog/` (Katalogeintrag, Selbstverweis, Katalogeintrag mit Pfadangabe oder eine andere Datei des Ordners); Gruppe (b): das Ziel liegt anderswo im Repo (ohne Pfadangabe über den Fundort, mit Pfadangabe über den Pfad relativ zur Wurzel); Gruppe (c): keine Datei dieses Namens im Repo. Gruppe (b) und (c) vollständig, je Ziel eine Zeile und darunter je Quelldatei die Abschnitte (×n = mehrfach im Abschnitt).

2752 Verweise in 73 Einträgen. Gruppe (a) Ziel in `katalog/`: 2505 – davon 2367 auf andere Katalogeinträge, 54 Selbstverweise, 1 auf Katalogeinträge mit Pfadangabe, 83 auf andere Dateien in `katalog/` (`_*.md`, `index.md`). Gruppe (b) Ziel anderswo im Repo: 231 Verweise auf 54 Dateien. Gruppe (c) Ziel gibt es nicht: 16 Verweise auf 5 Namen.

### Gruppe (b) – Ziel anderswo im Repo
- **abi-pruefungen.md** (liegt in abitur/) – 4 Verweise aus 2 Einträgen
  - ableitung-und-aenderungsrate.md (Offene Punkte ×2)
  - gleichungen-loesen.md (Offene Punkte ×2)
- **abitur-vokabular.md** (liegt in abitur/) – 14 Verweise aus 11 Einträgen
  - binomialverteilung.md (Blatt 0 ×2)
  - daten.md (Verortung)
  - ebenen.md (Verortung)
  - einheiten.md (Verortung, Prüfungsform)
  - hypothesentests.md (Prüfungsform)
  - konfidenzintervalle.md (Verortung)
  - lagebeziehungen.md (Prüfungsform)
  - lineare-gleichungssysteme.md (Verortung)
  - matrizen-und-uebergangsprozesse.md (Verortung ×2)
  - normalverteilung-und-sigma-regeln.md (Prüfungsform)
  - zufallsexperimente-und-pfadregeln.md (Prüfungsform)
- **faellig.md** (liegt in Wurzel) – 52 Verweise aus 42 Einträgen
  - ableitung-und-aenderungsrate.md (Offene Punkte)
  - ableitungsgraph-und-funktionsgraph.md (Offene Punkte)
  - ableitungsregeln.md (Offene Punkte)
  - abstaende.md (Offene Punkte)
  - bedingte-wahrscheinlichkeit-und-bayes.md (Offene Punkte)
  - binomialverteilung.md (Offene Punkte)
  - ebenen.md (Offene Punkte ×2)
  - extremalprobleme.md (Offene Punkte)
  - flaecheninhalt-durch-integration.md (Offene Punkte ×2)
  - flaecheninhalt-und-volumen-im-raum.md (Offene Punkte)
  - funktionsklassen-und-eigenschaften.md (Offene Punkte)
  - funktionsscharen-und-ortskurven.md (Offene Punkte ×2)
  - geraden.md (Offene Punkte)
  - gleichungen-loesen.md (Offene Punkte)
  - grenzwerte-und-verhalten-im-unendlichen.md (Offene Punkte)
  - hypothesentests.md (Offene Punkte)
  - integrationsregeln.md (Offene Punkte ×2)
  - kenngroessen-von-verteilungen.md (Offene Punkte)
  - kombinatorik.md (Offene Punkte)
  - konfidenzintervalle.md (Offene Punkte)
  - kurvenuntersuchung.md (Offene Punkte)
  - lagebeziehungen.md (Offene Punkte)
  - linearkombination-und-lineare-abhaengigkeit.md (Offene Punkte)
  - matrizen-und-uebergangsprozesse.md (Offene Punkte)
  - normalverteilung-und-sigma-regeln.md (Offene Punkte)
  - orthogonalitaet.md (Offene Punkte)
  - punkte-und-strecken-im-koordinatensystem.md (Offene Punkte)
  - rekonstruktion-von-bestaenden.md (Offene Punkte ×2)
  - rekonstruktion-von-funktionsgleichungen.md (Offene Punkte ×2)
  - rotationsvolumen.md (Offene Punkte ×2)
  - scharen-von-geraden-und-ebenen.md (Offene Punkte)
  - schnittmengen.md (Offene Punkte)
  - skalarprodukt-und-winkel.md (Offene Punkte)
  - spiegelung.md (Offene Punkte)
  - stammfunktion-und-hauptsatz.md (Offene Punkte ×2)
  - tangente-normale-schnittwinkel.md (Offene Punkte)
  - umkehrfunktion.md (Offene Punkte)
  - unabhaengigkeit.md (Offene Punkte)
  - uneigentliche-integrale.md (Offene Punkte ×2)
  - vektoren-und-rechenoperationen.md (Offene Punkte)
  - vierfeldertafel.md (Offene Punkte)
  - zufallsexperimente-und-pfadregeln.md (Offene Punkte ×2)
- **fhr.md** (liegt in fhr/) – 15 Verweise aus 5 Einträgen
  - binomialverteilung.md (Offene Punkte)
  - daten.md (Verortung, Prüfungsform)
  - einheiten.md (Verortung ×3, Prüfungsform ×2, Offene Punkte)
  - kombinatorik.md (Kopf, Verortung, Prüfungsform, Offene Punkte)
  - zufallsexperimente-und-pfadregeln.md (Verortung, Offene Punkte)
- **iqb.md** (liegt in abitur/) – 3 Verweise aus 1 Eintrag
  - lineare-gleichungssysteme.md (Verortung, Prüfungsform ×2)
- **konzept.md** (liegt in Wurzel) – 94 Verweise aus 47 Einträgen
  - ableitung-und-aenderungsrate.md (Kopf, Prüfungsform)
  - ableitungsgraph-und-funktionsgraph.md (Kopf, Verortung, Lerneinheiten, Prüfungsform, Offene Punkte)
  - ableitungsregeln.md (Kopf, Prüfungsform)
  - abstaende.md (Kopf, Prüfungsform)
  - bedingte-wahrscheinlichkeit-und-bayes.md (Kopf, Prüfungsform)
  - binomialverteilung.md (Kopf, Prüfungsform)
  - daten.md (Prüfungsform)
  - ebenen.md (Kopf, Prüfungsform)
  - einheiten.md (Prüfungsform)
  - extremalprobleme.md (Kopf, Prüfungsform)
  - flaecheninhalt-durch-integration.md (Kopf, Prüfungsform)
  - flaecheninhalt-und-volumen-im-raum.md (Kopf, Prüfungsform)
  - funktionsklassen-und-eigenschaften.md (Kopf, Prüfungsform)
  - funktionsscharen-und-ortskurven.md (Kopf, Prüfungsform)
  - geraden.md (Kopf, Prüfungsform)
  - gleichungen-loesen.md (Kopf, Prüfungsform)
  - grenzwerte-und-verhalten-im-unendlichen.md (Kopf, Prüfungsform)
  - hypergeometrische-verteilung.md (Kopf ×2, Prüfungsform)
  - hypothesentests.md (Kopf, Prüfungsform)
  - integrationsregeln.md (Kopf, Prüfungsform)
  - kenngroessen-von-verteilungen.md (Kopf, Prüfungsform)
  - kombinatorik.md (Prüfungsform)
  - konfidenzintervalle.md (Kopf, Prüfungsform)
  - kurvenuntersuchung.md (Kopf, Prüfungsform)
  - lagebeziehungen.md (Kopf, Prüfungsform)
  - lineare-gleichungssysteme.md (Prüfungsform)
  - linearkombination-und-lineare-abhaengigkeit.md (Kopf, Prüfungsform)
  - matrizen-und-uebergangsprozesse.md (Kopf, Prüfungsform)
  - normalverteilung-und-sigma-regeln.md (Kopf, Prüfungsform)
  - orthogonalitaet.md (Kopf, Prüfungsform)
  - punkte-und-strecken-im-koordinatensystem.md (Kopf, Prüfungsform)
  - rekonstruktion-von-bestaenden.md (Kopf, Prüfungsform)
  - rekonstruktion-von-funktionsgleichungen.md (Kopf, Prüfungsform)
  - rotationsvolumen.md (Kopf, Prüfungsform)
  - scharen-von-geraden-und-ebenen.md (Kopf, Prüfungsform)
  - schnittmengen.md (Kopf, Prüfungsform)
  - skalarprodukt-und-winkel.md (Kopf, Prüfungsform)
  - spiegelung.md (Kopf, Prüfungsform)
  - stammfunktion-und-hauptsatz.md (Kopf, Prüfungsform)
  - tangente-normale-schnittwinkel.md (Kopf, Prüfungsform)
  - umkehrfunktion.md (Kopf, Prüfungsform)
  - unabhaengigkeit.md (Kopf, Prüfungsform)
  - uneigentliche-integrale.md (Kopf, Prüfungsform)
  - vektoren-und-rechenoperationen.md (Kopf, Prüfungsform)
  - vierfeldertafel.md (Kopf, Prüfungsform)
  - zufallsexperimente-und-pfadregeln.md (Kopf, Prüfungsform)
  - zufallsgroessen-und-verteilungen.md (Kopf, Prüfungsform)
- **quellen/quellen.md** (liegt in quellen/) – 1 Verweis aus 1 Eintrag
  - binomialverteilung.md (Offene Punkte)
- **rohdaten/ableitung-und-aenderungsrate.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - ableitung-und-aenderungsrate.md (Kopf)
- **rohdaten/ableitungsgraph-und-funktionsgraph.md** (liegt in rohdaten/) – 2 Verweise aus 2 Einträgen
  - ableitungsgraph-und-funktionsgraph.md (Kopf)
  - kurvenuntersuchung.md (Verortung)
- **rohdaten/ableitungsregeln.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - ableitungsregeln.md (Kopf)
- **rohdaten/abstaende.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - abstaende.md (Kopf)
- **rohdaten/bedingte-wahrscheinlichkeit-und-bayes.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - bedingte-wahrscheinlichkeit-und-bayes.md (Kopf)
- **rohdaten/binomialverteilung.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - binomialverteilung.md (Kopf)
- **rohdaten/daten.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - daten.md (Kopf)
- **rohdaten/ebenen.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - ebenen.md (Kopf)
- **rohdaten/einheiten.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - einheiten.md (Kopf)
- **rohdaten/extremalprobleme.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - extremalprobleme.md (Kopf)
- **rohdaten/flaecheninhalt-durch-integration.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - flaecheninhalt-durch-integration.md (Kopf)
- **rohdaten/flaecheninhalt-und-volumen-im-raum.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - flaecheninhalt-und-volumen-im-raum.md (Kopf)
- **rohdaten/funktionsklassen-und-eigenschaften.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - funktionsklassen-und-eigenschaften.md (Kopf)
- **rohdaten/funktionsscharen-und-ortskurven.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - funktionsscharen-und-ortskurven.md (Kopf)
- **rohdaten/geraden.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - geraden.md (Kopf)
- **rohdaten/gleichungen-loesen.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - gleichungen-loesen.md (Kopf)
- **rohdaten/grenzwerte-und-verhalten-im-unendlichen.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - grenzwerte-und-verhalten-im-unendlichen.md (Kopf)
- **rohdaten/hypergeometrische-verteilung.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - hypergeometrische-verteilung.md (Kopf)
- **rohdaten/hypothesentests.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - hypothesentests.md (Kopf)
- **rohdaten/integrationsregeln.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - integrationsregeln.md (Kopf)
- **rohdaten/kenngroessen-von-verteilungen.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - kenngroessen-von-verteilungen.md (Kopf)
- **rohdaten/kombinatorik.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - kombinatorik.md (Kopf)
- **rohdaten/konfidenzintervalle.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - konfidenzintervalle.md (Kopf)
- **rohdaten/kurvenuntersuchung.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - kurvenuntersuchung.md (Kopf)
- **rohdaten/lagebeziehungen.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - lagebeziehungen.md (Kopf)
- **rohdaten/lineare-gleichungssysteme.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - lineare-gleichungssysteme.md (Kopf)
- **rohdaten/linearkombination-und-lineare-abhaengigkeit.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - linearkombination-und-lineare-abhaengigkeit.md (Kopf)
- **rohdaten/matrizen-und-uebergangsprozesse.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - matrizen-und-uebergangsprozesse.md (Kopf)
- **rohdaten/normalverteilung-und-sigma-regeln.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - normalverteilung-und-sigma-regeln.md (Kopf)
- **rohdaten/orthogonalitaet.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - orthogonalitaet.md (Kopf)
- **rohdaten/punkte-und-strecken-im-koordinatensystem.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - punkte-und-strecken-im-koordinatensystem.md (Kopf)
- **rohdaten/rekonstruktion-von-bestaenden.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - rekonstruktion-von-bestaenden.md (Kopf)
- **rohdaten/rekonstruktion-von-funktionsgleichungen.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - rekonstruktion-von-funktionsgleichungen.md (Kopf)
- **rohdaten/rotationsvolumen.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - rotationsvolumen.md (Kopf)
- **rohdaten/scharen-von-geraden-und-ebenen.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - scharen-von-geraden-und-ebenen.md (Kopf)
- **rohdaten/schnittmengen.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - schnittmengen.md (Kopf)
- **rohdaten/skalarprodukt-und-winkel.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - skalarprodukt-und-winkel.md (Kopf)
- **rohdaten/spiegelung.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - spiegelung.md (Kopf)
- **rohdaten/stammfunktion-und-hauptsatz.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - stammfunktion-und-hauptsatz.md (Kopf)
- **rohdaten/tangente-normale-schnittwinkel.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - tangente-normale-schnittwinkel.md (Kopf)
- **rohdaten/umkehrfunktion.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - umkehrfunktion.md (Kopf)
- **rohdaten/unabhaengigkeit.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - unabhaengigkeit.md (Kopf)
- **rohdaten/uneigentliche-integrale.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - uneigentliche-integrale.md (Kopf)
- **rohdaten/vektoren-und-rechenoperationen.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - vektoren-und-rechenoperationen.md (Kopf)
- **rohdaten/vierfeldertafel.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - vierfeldertafel.md (Kopf)
- **rohdaten/zufallsexperimente-und-pfadregeln.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - zufallsexperimente-und-pfadregeln.md (Kopf)
- **rohdaten/zufallsgroessen-und-verteilungen.md** (liegt in rohdaten/) – 1 Verweis aus 1 Eintrag
  - zufallsgroessen-und-verteilungen.md (Kopf)

### Gruppe (c) – Ziel gibt es nicht
- **fos-stochastik.md** (keine Datei dieses Namens im Repo) – 2 Verweise aus 2 Einträgen
  - kombinatorik.md (Offene Punkte)
  - wahrscheinlichkeit.md (Verortung)
- **gost-ableitung.md** (keine Datei dieses Namens im Repo) – 1 Verweis aus 1 Eintrag
  - trigonometrische-funktionen.md (Offene Punkte)
- **gost-exponential-e.md** (keine Datei dieses Namens im Repo) – 3 Verweise aus 1 Eintrag
  - potenz-exponentialfunktionen.md (Verortung, Offene Punkte ×2)
- **gost-funktionen-grundlagen.md** (keine Datei dieses Namens im Repo) – 8 Verweise aus 5 Einträgen
  - binomische-formeln.md (Verortung)
  - quadratische-funktionen.md (Verortung)
  - quadratische-gleichungen.md (Verortung, Offene Punkte)
  - reelle-zahlen.md (Offene Punkte)
  - trigonometrische-funktionen.md (Verortung, Offene Punkte ×2)
- **gost-stochastik.md** (keine Datei dieses Namens im Repo) – 2 Verweise aus 2 Einträgen
  - kombinatorik.md (Offene Punkte)
  - wahrscheinlichkeit.md (Verortung)

### Gruppe (a), Sonderfälle
Verweise auf Dateien in `katalog/`, die kein Eintrag sind (zählen in `tragfaehigkeit.py` als Verweise auf Nicht-Katalogdateien):
- **_formelsammlung.md** (liegt in katalog/) – 7 Verweise aus 7 Einträgen
  - binomische-formeln.md (Offene Punkte)
  - brueche-dezimalzahlen.md (Offene Punkte)
  - lineare-funktionen.md (Offene Punkte)
  - lineare-gleichungen.md (Offene Punkte)
  - lineare-gleichungssysteme.md (Offene Punkte)
  - terme.md (Offene Punkte)
  - zuordnungen.md (Offene Punkte)
- **_fragen.md** (liegt in katalog/) – 11 Verweise aus 11 Einträgen
  - potenz-exponentialfunktionen.md (Offene Punkte)
  - prozentrechnung.md (Offene Punkte)
  - pyramide-kegel-kugel.md (Offene Punkte)
  - pythagoras.md (Offene Punkte)
  - quadratische-funktionen.md (Offene Punkte)
  - quadratische-gleichungen.md (Offene Punkte)
  - strahlensaetze.md (Offene Punkte)
  - symmetrie-abbildungen.md (Offene Punkte)
  - terme.md (Offene Punkte)
  - trigonometrische-funktionen.md (Offene Punkte)
  - winkel-dreiecke.md (Offene Punkte)
- **_nachlese-voraussetzungen.md** (liegt in katalog/) – 1 Verweis aus 1 Eintrag
  - pythagoras.md (Offene Punkte)
- **_offen.md** (liegt in katalog/) – 4 Verweise aus 3 Einträgen
  - einheiten.md (Verortung, Offene Punkte)
  - lineare-funktionen.md (Offene Punkte)
  - symmetrie-abbildungen.md (Offene Punkte)
- **_quellen.md** (liegt in katalog/) – 4 Verweise aus 3 Einträgen
  - binomialverteilung.md (Offene Punkte)
  - lineare-gleichungen.md (Verortung)
  - prozentrechnung.md (Offene Punkte ×2)
- **_quellenprotokoll.md** (liegt in katalog/) – 5 Verweise aus 4 Einträgen
  - binomische-formeln.md (Verortung)
  - bruchrechnung.md (Verortung, Offene Punkte)
  - brueche-dezimalzahlen.md (Verortung)
  - strahlensaetze.md (Verortung)
- **index.md** (liegt in katalog/) – 50 Verweise aus 48 Einträgen
  - ableitung-und-aenderungsrate.md (Offene Punkte)
  - ableitungsgraph-und-funktionsgraph.md (Offene Punkte)
  - ableitungsregeln.md (Offene Punkte)
  - abstaende.md (Offene Punkte)
  - bedingte-wahrscheinlichkeit-und-bayes.md (Offene Punkte)
  - binomialverteilung.md (Offene Punkte)
  - brueche-dezimalzahlen.md (Prüfungsform, Offene Punkte)
  - ebenen.md (Offene Punkte)
  - extremalprobleme.md (Offene Punkte)
  - flaecheninhalt-durch-integration.md (Offene Punkte)
  - flaecheninhalt-und-volumen-im-raum.md (Offene Punkte)
  - funktionsklassen-und-eigenschaften.md (Offene Punkte)
  - funktionsscharen-und-ortskurven.md (Offene Punkte)
  - geraden.md (Offene Punkte)
  - gleichungen-loesen.md (Offene Punkte)
  - grenzwerte-und-verhalten-im-unendlichen.md (Offene Punkte)
  - hypergeometrische-verteilung.md (Offene Punkte ×2)
  - hypothesentests.md (Offene Punkte)
  - integrationsregeln.md (Offene Punkte)
  - kenngroessen-von-verteilungen.md (Offene Punkte)
  - kombinatorik.md (Offene Punkte)
  - konfidenzintervalle.md (Offene Punkte)
  - kurvenuntersuchung.md (Offene Punkte)
  - lagebeziehungen.md (Offene Punkte)
  - linearkombination-und-lineare-abhaengigkeit.md (Offene Punkte)
  - matrizen-und-uebergangsprozesse.md (Offene Punkte)
  - normalverteilung-und-sigma-regeln.md (Offene Punkte)
  - orthogonalitaet.md (Offene Punkte)
  - punkte-und-strecken-im-koordinatensystem.md (Offene Punkte)
  - rationale-zahlen.md (Prüfungsform)
  - rekonstruktion-von-bestaenden.md (Offene Punkte)
  - rekonstruktion-von-funktionsgleichungen.md (Offene Punkte)
  - rotationsvolumen.md (Offene Punkte)
  - scharen-von-geraden-und-ebenen.md (Offene Punkte)
  - schnittmengen.md (Offene Punkte)
  - skalarprodukt-und-winkel.md (Offene Punkte)
  - spiegelung.md (Offene Punkte)
  - stammfunktion-und-hauptsatz.md (Offene Punkte)
  - symmetrie-abbildungen.md (Offene Punkte)
  - tangente-normale-schnittwinkel.md (Offene Punkte)
  - umkehrfunktion.md (Offene Punkte)
  - unabhaengigkeit.md (Offene Punkte)
  - uneigentliche-integrale.md (Offene Punkte)
  - vektoren-und-rechenoperationen.md (Offene Punkte)
  - vierfeldertafel.md (Offene Punkte)
  - zufallsexperimente-und-pfadregeln.md (Offene Punkte)
  - zufallsgroessen-und-verteilungen.md (Offene Punkte)
  - zuordnungen.md (Offene Punkte)
- **katalog/_quellen.md** (liegt in katalog/) – 1 Verweis aus 1 Eintrag
  - zufallsexperimente-und-pfadregeln.md (Offene Punkte)

Verweise auf Katalogeinträge mit Pfadangabe (`katalog/<name>.md`; zählen in `tragfaehigkeit.py` nicht als Katalogverweis, weil der Pfad mitgenommen wird):
- katalog/flaecheninhalt-durch-integration.md ← punkte-und-strecken-im-koordinatensystem.md (Offene Punkte, Zeile 129)

## 2 Einheitennummern
Eine Einheitenangabe ist „Einheit n“ oder „Einheiten n“ mit einer oder zwei Ziffern, fortgesetzt mit „und“, „bis“, „–“, Komma oder Schrägstrich („Einheit 6 und 8“, „Einheiten 2 bis 4“, „Einheit 2, 3 und 5“). Sie steht hinter einem Verweis, wenn zwischen `<name>.md` und „Einheit“ nur Leerraum, ein Komma oder eine öffnende Klammer steht („x.md Einheit 4“, „x.md, Einheit 4“, „x.md (Einheit 4)“); dann wird die größte genannte Nummer gegen die Zahl der Lerneinheiten der Zieldatei gehalten. Nicht eindeutig zuordenbar und deshalb nur gelistet: (1) der Verweis davor steht in einer Reihung („a.md und b.md Einheit 2“, „a.md, b.md Einheit 2“) – welcher gemeint ist, steht nicht da; (2) zwischen Verweis und Angabe stehen bis zu 4 Wörter ohne Satz- oder Klammerende („x.md, dessen Einheit 5“, „x.md (Sek I, Einheit 3)“) – hier kann auch eine eigene Einheit gemeint sein; (3) die Angabe steht vor dem Verweis mit „in“, „im“, „von“, „aus“, „der“, „des“ oder „bei“ dazwischen („Einheit 4 in x.md“). Alle anderen Einheitenangaben – ohne Verweis in der Zeile, hinter einem Satzende oder weiter entfernt – gelten als eigene Einheiten des Eintrags und werden nicht geprüft; Angaben an Nennungen in Wortform („Thema Terme, Einheit 2“) haben keinen Verweis, dem sie zugeordnet werden könnten (die in Blatt 0 stehen unter Prüfung 5).

3848 Einheitenangaben in den Einträgen. Direkt hinter einem Verweis: 360 (360 geprüft, 0 nicht prüfbar, weil das Ziel kein Katalogeintrag ist); davon Nummer größer als vorhanden: 0. Nicht eindeutig einem Verweis zuordenbar: 23. Die übrigen 3465 stehen ohne Verweis davor oder weiter von ihm entfernt; sie gelten als eigene Einheiten des Eintrags und sind nicht geprüft.

### Nummer größer als vorhanden
- keine

### Direkt hinter einem Verweis, aber nicht prüfbar
- keine

### Nicht eindeutig einem Verweis zuordenbar
- ableitung-und-aenderungsrate.md (Verortung, Zeile 5): kurzer Zwischentext – „Einheit 5“ bei kurvenuntersuchung.md; Zitat: …Monotonie, Extrem- und Wendepunkte von f selbst → kurvenuntersuchung.md, dessen Einheit 5 die Sachfragen „größter Wert“ und „stär…
- ableitungsgraph-und-funktionsgraph.md (Verortung, Zeile 6): kurzer Zwischentext – „Einheit 4“ bei kurvenuntersuchung.md; Zitat: …unktionsgraphen“ – die Belege sind dieselben, die kurvenuntersuchung.md für Einheit 4 zitiert.
- ableitungsgraph-und-funktionsgraph.md (Verortung, Zeile 8): kurzer Zwischentext – „Einheit 4“ bei kurvenuntersuchung.md; Zitat: …Graph und Funktionsterm“ – dieselben Kapitel, die kurvenuntersuchung.md der Einheit 4 zuordnet (Zuordnung dort: „Einheit 4 = …
- ableitungsgraph-und-funktionsgraph.md (Merkkasten, Zeile 20): kurzer Zwischentext – „Einheit 4“ bei kurvenuntersuchung.md; Zitat: Verweis: kurvenuntersuchung.md, Merkkasten Einheit 4 (Übersetzungstabelle f ↔ f' ↔ f'', Grad…
- ableitungsgraph-und-funktionsgraph.md (Prüfungsform, Zeile 30): Angabe vor dem Verweis – „Einheit 4“ bei kurvenuntersuchung.md; Zitat: …Ableitungsgraph nicht (auch die fhr-Zielmarke der Einheit 4 in kurvenuntersuchung.md ist leer).
- binomialverteilung.md (Blatt 0, Zeile 29): kurzer Zwischentext – „Einheit 3“ bei wahrscheinlichkeit.md; Zitat: … das Gegenereignis auch in Einheit 3 und 4. Thema wahrscheinlichkeit.md (Sek I, Einheit 3). [GOST Eingangsvoraussetzung L5 „besti…
- funktionsscharen-und-ortskurven.md (Verortung, Zeile 5): Verweisreihung davor – „Einheit 2“ bei gleichungen-loesen.md / funktionsklassen-und-eigenschaften.md; Zitat: … (Substitution, Polynomdivision, e-Gleichungen) → gleichungen-loesen.md und funktionsklassen-und-eigenschaften.md Einheit 2; das Grenzverhalten fester Funktionen u…
- geraden.md (Offene Punkte, Zeile 112): kurzer Zwischentext – „Einheit 3“ bei schnittmengen.md; Zitat: …iegt bei lagebeziehungen.md, der Schnittpunkt bei schnittmengen.md – beim Blattbau ist Einheit 3 die Vorstufe dieser Themen. (3) Zuordnu…
- kombinatorik.md (Verortung, Zeile 5): kurzer Zwischentext – „Einheit 2“ bei binomialverteilung.md; Zitat: …inheit 5 (Anzahl der Reihenfolgen, Lotto-Modell), binomialverteilung.md für die Bernoulli-Formel (Einheit 2, Binomialkoeffizient als Anzahl der Ano…
- kombinatorik.md (Offene Punkte, Zeile 108): kurzer Zwischentext – „Einheit 2“ bei kombinatorik.md; Zitat: …etrische-verteilung.md nennt unter Blatt 0 „Thema kombinatorik.md“ ohne Einheitsnummer (Einheit 2 wäre richtig) – nach Auftrag nicht geän…
- kurvenuntersuchung.md (Verortung, Zeile 5): kurzer Zwischentext – „Einheit 4“ bei ableitungsgraph-und-funktionsgraph.md; Zitat: …leitungsgraph-und-funktionsgraph.md, 21 Zeilen) → ableitungsgraph-und-funktionsgraph.md – Einheit 4 führt hier nur die 15 Zeilen, die die K…
- lineare-gleichungssysteme.md (Blatt 0, Zeile 38): Verweisreihung davor – „Einheit 2 und 4“ bei terme.md / lineare-gleichungen.md; Zitat: … die Werkzeuge des dritten Schritts. Sek-I-Themen terme.md, lineare-gleichungen.md Einheit 2 und 4. [GOST Eingangsvoraussetzung L1 „lösen …
- potenzen-wurzeln.md (Offene Punkte, Zeile 104): kurzer Zwischentext – „Einheit 2“ bei einheiten.md; Zitat: …Messen F Milli bis Kilo, G Nano bis Tera) bleiben einheiten.md, das dort auf Einheit 2 verweist – Index-Zeile einheiten.md ent…
- potenzen-wurzeln.md (Offene Punkte, Zeile 108): kurzer Zwischentext – „Einheit 3 und 4“ bei koerper.md; Zitat: …√49 = 7), trigonometrie.md (Taschenrechnerzeile), koerper.md (Quadrieren und Wurzelziehen Einheit 3 und 4), flaechen.md (√49 Quadratseite) – alle…
- pyramide-kegel-kugel.md (Prüfungsform, Zeile 94): kurzer Zwischentext – „Einheit 2“ bei pythagoras.md; Zitat: …chnen“ (2026-FOR-K2c, Kegelhöhe und Gesamthöhe) → pythagoras.md, Verfahren Stützdreieck hier in Einheit 2; „Restvolumen berechnen“ (2024-OS-K4c) …
- pyramide-kegel-kugel.md (Prüfungsform, Zeile 94): kurzer Zwischentext – „Einheit 1“ bei flaechen.md; Zitat: …enuse“ (2015-OS-K6c, Seitenfläche der Pyramide) → flaechen.md, Verfahren Seitenhöhe hier in Einheit 1; „Kreisfläche berechnen“ (2024-OS-K4a, …
- reelle-zahlen.md (Offene Punkte, Zeile 96): Angabe vor dem Verweis – „Einheit 1“ bei potenzen-wurzeln.md; Zitat: …→ potenz-exponentialfunktionen.md. Alternative C: Einheit 1 in potenzen-wurzeln.md Einheit 3 einbauen (das Lehrwerk hat IV…
- strahlensaetze.md (Offene Punkte, Zeile 98): Angabe vor dem Verweis – „Einheit 5“ bei zuordnungen.md; Zitat: …lensätze (Kl. 9 IV 3). Alternative A: Maßstab als Einheit 5 in zuordnungen.md (der RLP führt den Maßstab bei Zuordnun…
- strahlensaetze.md (Offene Punkte, Zeile 103): kurzer Zwischentext – „Einheit 2“ bei trigonometrie.md; Zitat: …er als letzte Mindeststoff-Sprosse der Einheit 2, trigonometrie.md verweist seit 09b auf Einheit 2 statt „noch leer“; Sinussatz-Originale …
- trigonometrie.md (Offene Punkte, Zeile 114): kurzer Zwischentext – „Einheit 3“ bei flaechen.md; Zitat: …(2015-OS-K5d, 2022-OS-K5e, 2023-OS-K2c): Typen in flaechen.md, Verfahren hier Einheit 3 – flaechen.md nennt den Schenkel „über …
- trigonometrische-funktionen.md (Fehler, Zeile 88): kurzer Zwischentext – „Einheit 2“ bei trigonometrie.md; Zitat: …dius des Einheitskreises ist die Obergrenze. [FD; trigonometrie.md Kasten Einheit 2 „nie größer als eins“]
- trigonometrische-funktionen.md (Offene Punkte, Zeile 130): Verweisreihung davor – „Einheit 3“ bei lineare-funktionen.md / zuordnungen.md; Zitat: …wirkung → quadratische-funktionen.md Einheit 1–2, lineare-funktionen.md, zuordnungen.md Einheit 3 (hier Blatt 0); Exponentialkurve und di…
- zinsrechnung.md (Offene Punkte, Zeile 82): Angabe vor dem Verweis – „Einheit 6“ bei prozentrechnung.md; Zitat: …lensaetze.md Einheit 1. Alternative B: Zinsen als Einheit 6 in prozentrechnung.md (Lehrwerk im selben Kapitel, LISUM-PH a…

Zahl der Lerneinheiten je Eintrag (Zeilen „<n>. “ im Abschnitt „### Lerneinheiten“): ableitung-und-aenderungsrate 4, ableitungsgraph-und-funktionsgraph 0, ableitungsregeln 3, abstaende 4, bedingte-wahrscheinlichkeit-und-bayes 3, binomialverteilung 5, binomische-formeln 3, bruchrechnung 5, brueche-dezimalzahlen 5, daten 6, ebenen 4, einheiten 4, extremalprobleme 3, flaechen 5, flaecheninhalt-durch-integration 5, flaecheninhalt-und-volumen-im-raum 4, funktionsklassen-und-eigenschaften 6, funktionsscharen-und-ortskurven 5, geraden 4, gleichungen-loesen 4, grenzwerte-und-verhalten-im-unendlichen 3, hypergeometrische-verteilung 2, hypothesentests 3, integrationsregeln 2, kenngroessen-von-verteilungen 4, koerper 5, kombinatorik 3, konfidenzintervalle 3, kreis 3, kurvenuntersuchung 5, lagebeziehungen 4, lineare-funktionen 5, lineare-gleichungen 4, lineare-gleichungssysteme 5, linearkombination-und-lineare-abhaengigkeit 2, matrizen-und-uebergangsprozesse 5, normalverteilung-und-sigma-regeln 3, orthogonalitaet 4, potenz-exponentialfunktionen 4, potenzen-wurzeln 3, prozentrechnung 5, punkte-und-strecken-im-koordinatensystem 5, pyramide-kegel-kugel 3, pythagoras 3, quadratische-funktionen 4, quadratische-gleichungen 4, rationale-zahlen 4, reelle-zahlen 3, rekonstruktion-von-bestaenden 3, rekonstruktion-von-funktionsgleichungen 3, rotationsvolumen 2, scharen-von-geraden-und-ebenen 4, schnittmengen 3, skalarprodukt-und-winkel 4, spiegelung 3, stammfunktion-und-hauptsatz 4, strahlensaetze 3, symmetrie-abbildungen 3, tangente-normale-schnittwinkel 5, terme 4, trigonometrie 4, trigonometrische-funktionen 4, umkehrfunktion 2, unabhaengigkeit 3, uneigentliche-integrale 2, vektoren-und-rechenoperationen 3, vierfeldertafel 2, wahrscheinlichkeit 4, winkel-dreiecke 5, zinsrechnung 2, zufallsexperimente-und-pfadregeln 8, zufallsgroessen-und-verteilungen 2, zuordnungen 4.

## 3 Namensgleichheit
Vier Abgleiche, jeder in beide Richtungen. (a) Jede `katalog/<x>.md` hat eine Zeile in `themen.csv` mit `kanonisch` = x; jeder kanonische Name mit `stufe` II (auch „I+II“) hat eine Katalogdatei. (b) Die H1-Überschrift jedes Eintrags gegen die `thema`-Werte seiner Zeilen (Zeilen mit leerem Thema zählen nicht); Abweichungen werden gemeldet, nicht bewertet – ein Eintrag kann mehrere Prüfungsthemen tragen. (c) Die `thema`-Werte der Zeilen mit `profil` abi oder iqb gegen die Themenliste in `abitur-vokabular.md` § 2 (Lesart von `themen-pruef.py`) und gegen die Spalte „Thema“ der Tabelle in § 1 jeder der vier `abi-*-geltung.md`. (d) Die `thema`-Werte der Zeilen mit `profil` msa gegen die Spalte `thema` von `msa/msa-typen.csv`, fhr gegen `fhr/fhr-typen.csv`. Ist eine Themenspalte über die Kopfzeile nicht eindeutig (kein oder mehr als ein Treffer), wird die Teilprüfung abgebrochen und der Grund genannt.

(a) Datei ↔ kanonisch: 73 Katalogdateien, 74 kanonische Namen in `themen.csv`, davon 47 mit Stufe II. Bestanden.

(b) H1 gegen thema-Werte: 39 Einträge mit H1 gleich allen thema-Werten, 27 mit Abweichung, 7 ohne thema-Wert (kein Prüfungsthema).
- ableitungsregeln.md: H1 „Ableitungsregeln“ – gleich: abi, iqb; abweichend: fhr „Ableitungen bilden“
- daten.md: H1 „Daten“ – gleich: –; abweichend: msa „Kenngrößen“, msa „Diagramme lesen und beurteilen“, msa „Daten darstellen“, fhr „Statistische Kenngrößen“, fhr „Daten darstellen und aufbereiten“, iqb „Lage- und Streumaße einer Stichprobe“
- einheiten.md: H1 „Größen und Einheiten“ – gleich: fhr; abweichend: msa „Einheiten umrechnen“
- extremalprobleme.md: H1 „Extremalprobleme“ – gleich: abi, iqb; abweichend: fhr „Extremwertaufgaben“
- flaechen.md: H1 „Flächen“ – gleich: –; abweichend: msa „Flächeninhalt und Umfang“
- flaecheninhalt-durch-integration.md: H1 „Flächeninhalt durch Integration“ – gleich: abi, iqb; abweichend: fhr „Fläche zwischen Graph und x-Achse“, fhr „Fläche zwischen zwei Graphen“, fhr „Körpervolumen aus Grundfläche und Länge“
- funktionsklassen-und-eigenschaften.md: H1 „Funktionsklassen und Eigenschaften“ – gleich: abi, iqb; abweichend: fhr „Graph zeichnen und zuordnen“, fhr „Nullstellen ganzrationaler Funktionen“, fhr „Symmetrie nachweisen“
- gleichungen-loesen.md: H1 „Gleichungen lösen“ – gleich: abi, iqb; abweichend: fhr „Schnittpunkte von Funktionsgraphen“
- grenzwerte-und-verhalten-im-unendlichen.md: H1 „Grenzwerte und Verhalten im Unendlichen“ – gleich: abi, iqb; abweichend: fhr „Verhalten im Unendlichen“
- kenngroessen-von-verteilungen.md: H1 „Kenngrößen von Verteilungen“ – gleich: abi, iqb; abweichend: fhr „Erwartungswert“
- koerper.md: H1 „Körper“ – gleich: –; abweichend: msa „Volumen und Oberfläche“, msa „Körper, Netze, Schrägbilder“
- kombinatorik.md: H1 „Kombinatorik“ – gleich: abi, iqb; abweichend: fhr „Kombinatorische Abzählverfahren“
- kurvenuntersuchung.md: H1 „Kurvenuntersuchung“ – gleich: abi, iqb; abweichend: fhr „Extrem- und Sattelpunkte“, fhr „Wendepunkte“, fhr „Monotonie und Krümmung“
- potenz-exponentialfunktionen.md: H1 „Potenz- und Exponentialfunktionen, Wachstum und Zerfall“ – gleich: –; abweichend: msa „Exponentialfunktionen und Wachstum“
- potenzen-wurzeln.md: H1 „Potenzen, Zehnerpotenzen und Quadratwurzeln“ – gleich: –; abweichend: msa „Potenzen und Wurzeln“, msa „Zehnerpotenzen und Näherungswerte“
- rationale-zahlen.md: H1 „Rationale Zahlen“ – gleich: –; abweichend: msa „Rationale Zahlen rechnen“
- rekonstruktion-von-funktionsgleichungen.md: H1 „Rekonstruktion von Funktionsgleichungen“ – gleich: abi, iqb; abweichend: fhr „Funktionsgleichung bestimmen“
- rotationsvolumen.md: H1 „Rotationsvolumen“ – gleich: abi, iqb; abweichend: fhr „Rotationsvolumen um die x-Achse“
- symmetrie-abbildungen.md: H1 „Symmetrie, Abbildungen und Koordinatensystem“ – gleich: –; abweichend: msa „Symmetrie und Abbildungen“
- tangente-normale-schnittwinkel.md: H1 „Tangente, Normale, Schnittwinkel“ – gleich: abi, iqb; abweichend: fhr „Anstieg und Tangente“, fhr „Normale“
- terme.md: H1 „Terme“ – gleich: –; abweichend: msa „Terme umformen“, fhr „Terme umformen“
- trigonometrie.md: H1 „Trigonometrie“ – gleich: –; abweichend: msa „Trigonometrie im rechtwinkligen Dreieck“, msa „Sinussatz“
- unabhaengigkeit.md: H1 „Unabhängigkeit“ – gleich: abi, iqb; abweichend: fhr „Unabhängigkeit von Ereignissen“
- wahrscheinlichkeit.md: H1 „Wahrscheinlichkeit“ – gleich: –; abweichend: msa „Wahrscheinlichkeit mehrstufig“, msa „Wahrscheinlichkeit einstufig“, msa „Zählen und Kombinatorik“
- winkel-dreiecke.md: H1 „Winkel und Dreiecke“ – gleich: –; abweichend: msa „Ebene Figuren und Winkel“
- zufallsexperimente-und-pfadregeln.md: H1 „Zufallsexperimente und Pfadregeln“ – gleich: –; abweichend: fhr „Mehrstufige Zufallsexperimente“, fhr „Laplace-Wahrscheinlichkeit“, fhr „Baumdiagramm und Pfadregeln“, abi „Baumdiagramm und Pfadregeln“, abi „Zufallsexperimente und Urnenmodelle“, abi „Ereignisse und Mengenoperationen“, iqb „Baumdiagramm und Pfadregeln“, iqb „Zufallsexperimente und Urnenmodelle“, iqb „Ereignisse und Mengenoperationen“
- zuordnungen.md: H1 „Zuordnungen“ – gleich: –; abweichend: msa „Zuordnungen proportional und antiproportional“, msa „Maßstab“

Ohne `thema`-Wert in `themen.csv` (kein Prüfungsthema; H1 zum Nachlesen):
- binomische-formeln.md: H1 „Binomische Formeln“
- bruchrechnung.md: H1 „Bruchrechnung“
- kreis.md: H1 „Kreis“
- pyramide-kegel-kugel.md: H1 „Pyramide, Kegel, Kugel“
- reelle-zahlen.md: H1 „Reelle Zahlen, Potenzgesetze und Wurzelgesetze“
- strahlensaetze.md: H1 „Maßstab, Ähnlichkeit und Strahlensätze“
- trigonometrische-funktionen.md: H1 „Trigonometrische Funktionen“

(c) abi/iqb-Themen: 48 verschiedene thema-Werte der abi/iqb-Zeilen; Listen: abitur-vokabular.md § 2: 48; abi-be-gk-geltung.md § 1: 48; abi-be-lk-geltung.md § 1: 48; abi-bb-gk-geltung.md § 1: 48; abi-bb-ea-geltung.md § 1: 48. Bestanden.

(d) msa/fhr-Themen gegen den Typenkatalog: msa: 32 thema-Werte in `themen.csv`, 32 Themen in `msa/msa-typen.csv`, bestanden; fhr: 28 thema-Werte in `themen.csv`, 29 Themen in `fhr/fhr-typen.csv`, 1 Abweichungen.
- fhr/fhr-typen.csv nennt ein Thema ohne fhr-Zeile in themen.csv: „Gleichungen lösen“

## 4 Gegenrichtung
Nennt Eintrag A unter „Voraussetzungen (Blatt 0)“ den Eintrag B (Kante wie in `tragfaehigkeit.py`: Verweis `<B>.md` ohne Pfad, kein Selbstverweis), wird geprüft, ob B irgendwo in seinem Text `<A>.md` nennt (auch als `katalog/<A>.md`; Nennungen in Wortform zählen nicht). Fehlt das, ist (A, B) ein Paar. Nur aufgelistet, nicht bewertet.

364 Blatt-0-Verweise auf andere Katalogeinträge (Kanten A → B); 229 davon ohne Gegenrichtung: B nennt A.md in keinem Abschnitt. Gruppiert nach B (dort stünde die Erwähnung), 46 Einträge B betroffen.
- **ableitungsregeln** (3): funktionsscharen-und-ortskurven, integrationsregeln, rekonstruktion-von-funktionsgleichungen
- **abstaende** (1): flaecheninhalt-und-volumen-im-raum
- **binomialverteilung** (1): konfidenzintervalle
- **binomische-formeln** (3): ableitungsregeln, gleichungen-loesen, rotationsvolumen
- **bruchrechnung** (8): ableitungsregeln, bedingte-wahrscheinlichkeit-und-bayes, hypergeometrische-verteilung, kenngroessen-von-verteilungen, kombinatorik, unabhaengigkeit, zufallsexperimente-und-pfadregeln, zufallsgroessen-und-verteilungen
- **brueche-dezimalzahlen** (3): ableitungsregeln, kombinatorik, zufallsexperimente-und-pfadregeln
- **daten** (3): bedingte-wahrscheinlichkeit-und-bayes, matrizen-und-uebergangsprozesse, zufallsgroessen-und-verteilungen
- **einheiten** (4): ableitung-und-aenderungsrate, daten, rekonstruktion-von-bestaenden, rotationsvolumen
- **flaechen** (6): extremalprobleme, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, tangente-normale-schnittwinkel, umkehrfunktion
- **flaecheninhalt-durch-integration** (2): normalverteilung-und-sigma-regeln, umkehrfunktion
- **funktionsklassen-und-eigenschaften** (1): rekonstruktion-von-bestaenden
- **funktionsscharen-und-ortskurven** (1): lagebeziehungen
- **gleichungen-loesen** (9): abstaende, bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, einheiten, extremalprobleme, konfidenzintervalle, scharen-von-geraden-und-ebenen, umkehrfunktion, zufallsexperimente-und-pfadregeln
- **grenzwerte-und-verhalten-im-unendlichen** (1): umkehrfunktion
- **koerper** (6): ebenen, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, rotationsvolumen, schnittmengen, vektoren-und-rechenoperationen
- **kreis** (6): abstaende, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, skalarprodukt-und-winkel, zufallsexperimente-und-pfadregeln
- **kurvenuntersuchung** (2): stammfunktion-und-hauptsatz, umkehrfunktion
- **lagebeziehungen** (1): lineare-gleichungssysteme
- **lineare-funktionen** (14): ableitung-und-aenderungsrate, ableitungsregeln, bedingte-wahrscheinlichkeit-und-bayes, ebenen, extremalprobleme, funktionsklassen-und-eigenschaften, geraden, gleichungen-loesen, hypothesentests, konfidenzintervalle, rekonstruktion-von-funktionsgleichungen, stammfunktion-und-hauptsatz, tangente-normale-schnittwinkel, umkehrfunktion
- **lineare-gleichungen** (16): bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, daten, flaecheninhalt-und-volumen-im-raum, funktionsscharen-und-ortskurven, geraden, gleichungen-loesen, kenngroessen-von-verteilungen, lagebeziehungen, lineare-gleichungssysteme, matrizen-und-uebergangsprozesse, scharen-von-geraden-und-ebenen, unabhaengigkeit, vektoren-und-rechenoperationen, vierfeldertafel, zufallsexperimente-und-pfadregeln
- **lineare-gleichungssysteme** (4): ebenen, linearkombination-und-lineare-abhaengigkeit, orthogonalitaet, scharen-von-geraden-und-ebenen
- **linearkombination-und-lineare-abhaengigkeit** (2): orthogonalitaet, scharen-von-geraden-und-ebenen
- **orthogonalitaet** (1): scharen-von-geraden-und-ebenen
- **potenz-exponentialfunktionen** (9): ableitung-und-aenderungsrate, ableitungsregeln, binomialverteilung, funktionsklassen-und-eigenschaften, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, matrizen-und-uebergangsprozesse, trigonometrische-funktionen, umkehrfunktion
- **potenzen-wurzeln** (12): ableitungsregeln, daten, funktionsklassen-und-eigenschaften, funktionsscharen-und-ortskurven, grenzwerte-und-verhalten-im-unendlichen, integrationsregeln, kenngroessen-von-verteilungen, kombinatorik, punkte-und-strecken-im-koordinatensystem, stammfunktion-und-hauptsatz, vektoren-und-rechenoperationen, zufallsexperimente-und-pfadregeln
- **prozentrechnung** (15): ableitung-und-aenderungsrate, bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, flaecheninhalt-und-volumen-im-raum, geraden, kenngroessen-von-verteilungen, kombinatorik, konfidenzintervalle, matrizen-und-uebergangsprozesse, normalverteilung-und-sigma-regeln, punkte-und-strecken-im-koordinatensystem, skalarprodukt-und-winkel, unabhaengigkeit, vierfeldertafel, zufallsexperimente-und-pfadregeln
- **punkte-und-strecken-im-koordinatensystem** (1): lineare-gleichungssysteme
- **pyramide-kegel-kugel** (4): ebenen, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, rotationsvolumen
- **pythagoras** (8): abstaende, extremalprobleme, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, rotationsvolumen, tangente-normale-schnittwinkel, umkehrfunktion, vektoren-und-rechenoperationen
- **quadratische-funktionen** (8): ableitung-und-aenderungsrate, ableitungsregeln, funktionsklassen-und-eigenschaften, funktionsscharen-und-ortskurven, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, kurvenuntersuchung, rekonstruktion-von-funktionsgleichungen
- **quadratische-gleichungen** (14): abstaende, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, funktionsklassen-und-eigenschaften, funktionsscharen-und-ortskurven, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, kenngroessen-von-verteilungen, konfidenzintervalle, lagebeziehungen, orthogonalitaet, scharen-von-geraden-und-ebenen, unabhaengigkeit, zufallsexperimente-und-pfadregeln
- **rationale-zahlen** (4): funktionsklassen-und-eigenschaften, grenzwerte-und-verhalten-im-unendlichen, integrationsregeln, stammfunktion-und-hauptsatz
- **reelle-zahlen** (4): ableitungsregeln, binomialverteilung, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen
- **schnittmengen** (1): scharen-von-geraden-und-ebenen
- **skalarprodukt-und-winkel** (1): scharen-von-geraden-und-ebenen
- **stammfunktion-und-hauptsatz** (1): normalverteilung-und-sigma-regeln
- **strahlensaetze** (9): abstaende, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, funktionsklassen-und-eigenschaften, geraden, gleichungen-loesen, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, schnittmengen
- **symmetrie-abbildungen** (6): funktionsklassen-und-eigenschaften, grenzwerte-und-verhalten-im-unendlichen, punkte-und-strecken-im-koordinatensystem, spiegelung, umkehrfunktion, vektoren-und-rechenoperationen
- **tangente-normale-schnittwinkel** (1): stammfunktion-und-hauptsatz
- **terme** (8): ableitungsregeln, extremalprobleme, funktionsscharen-und-ortskurven, gleichungen-loesen, integrationsregeln, lagebeziehungen, lineare-gleichungssysteme, vektoren-und-rechenoperationen
- **trigonometrie** (4): gleichungen-loesen, potenzen-wurzeln, skalarprodukt-und-winkel, tangente-normale-schnittwinkel
- **trigonometrische-funktionen** (3): funktionsklassen-und-eigenschaften, gleichungen-loesen, rekonstruktion-von-funktionsgleichungen
- **vektoren-und-rechenoperationen** (3): ebenen, flaecheninhalt-und-volumen-im-raum, spiegelung
- **wahrscheinlichkeit** (8): binomialverteilung, hypothesentests, kenngroessen-von-verteilungen, normalverteilung-und-sigma-regeln, unabhaengigkeit, vierfeldertafel, zufallsexperimente-und-pfadregeln, zufallsgroessen-und-verteilungen
- **winkel-dreiecke** (3): orthogonalitaet, punkte-und-strecken-im-koordinatensystem, skalarprodukt-und-winkel
- **zuordnungen** (4): ableitung-und-aenderungsrate, linearkombination-und-lineare-abhaengigkeit, rekonstruktion-von-bestaenden, vektoren-und-rechenoperationen

## 5 Formlücke
Einträge, deren Blatt-0-Abschnitt keinen Verweis auf einen anderen Katalogeintrag enthält – dieselbe Menge wie „Einträge ohne Verweis“ in den Messlücken von `_tragfaehigkeit.md` (Lesart des Vorbilds: Verweise auf Nicht-Katalogdateien und Selbstverweise zählen nicht). Je Eintrag die Zahl der Nennungen in Wortform (Heuristik „Thema “ vor einem Großbuchstaben) und jede Zeile des Abschnitts, die eine trägt, als wörtliches Zitat mit Zeilennummer; steht eine Zeile für mehrere Nennungen, ist ihre Zahl vermerkt.

22 von 73 Einträgen. Wörtliche Lesart (überhaupt kein `<name>.md` im Abschnitt): dieselbe Menge.
- **binomische-formeln** – 7 Nennungen in Wortform in 7 Zeilen:
  - Zeile 23:
    > - Gleichartige Glieder mit einer Variablen zusammenfassen, Vorzahl eins beachten, Potenz getrennt halten – alle Einheiten. Thema Terme, Einheit 2. [RLP E; LS-AA Kl. 8 II 1 Wiederholung]
  - Zeile 24:
    > - Zahl mal Klammer und Minusklammer (Distributivgesetz, alle Vorzeichen drehen): 7·(x + 6) = 7x + 42; −(x − 6) = −x + 6 – Einheit 1 und 2. Thema Terme, Einheit 3. [RLP F; LS-AA Kl. 7 IV 3]
  - Zeile 25:
    > - Ausklammern eines gemeinsamen Zahlfaktors oder einer Variablen: 6x + 12 = 6·(x + 2); x² + 7x = x·(x + 7) – Einheit 3. Thema Terme, Einheit 4. [RLP F; LS-AA Kl. 7 IV 3]
  - Zeile 26:
    > - Multiplizieren mit Vorzeichen und Punkt vor Strich: (−6) · (−7) = 42; 11 − 6 · 7 = −31 – alle Einheiten. Thema Rationale Zahlen. [RLP D/E]
  - Zeile 27:
    > - Quadratzahlen bis 15² erkennen und Quadratwurzeln daraus (√49 = 7); Quadrat einer Variablen (x · x = x²) und einer Vorzahl mit Variable ((7x)² = 49x²) – Einheit 2 und 3. Thema Potenzen und Wurzeln; Terme, Einheit 2. [RLP F; P10 2020-OS-K3c Fehlerquelle Quadrat einer Zahlensumme; 2026-FOR-B1e Vorzahl mit quadriert]
  - Zeile 28:
    > - Termwert berechnen, auch mit negativer Zahl, als Probe einer Umformung: für x = −6 ist x² − 7 = 29 – alle Einheiten. Thema Terme, Einheit 1. [P10 Typ „Termwert berechnen“]
  - Zeile 29:
    > - Scheitelpunktform lesen: (x − 7)² + 11 hat den Scheitel S(7 | 11) – Einheit 2 (Anwendung Normalform). Thema Quadratische Funktionen, Einheit 2. [RLP G]
- **bruchrechnung** – 2 Nennungen in Wortform in 2 Zeilen:
  - Zeile 27:
    > - Bruch als Anteil lesen, am Streifen einzeichnen (drei Achtel markieren) – Einheit 1 und 3. Thema Brüche und Dezimalzahlen. [RLP D, MSK B1A]
  - Zeile 32:
    > - Bruch ↔ Dezimalzahl bei einfachen Brüchen (ein Halb, drei Viertel) – Einheit 5 (gemischte Terme). Thema Brüche und Dezimalzahlen. [RLP D]
- **brueche-dezimalzahlen** – 3 Nennungen in Wortform in 3 Zeilen:
  - Zeile 30:
    > - Größen mit Komma lesen und umrechnen (1,2 kg = 1200 g; 2,50 €) – Einheit 1 (Bruchteil einer Größe) und Einheit 5 (Runden von Größen). Thema Einheiten. [RLP D „Erklären von Größenangaben mit Dezimalzahlen mithilfe der erweiterten Stellenwerttafeln“]
  - Zeile 32:
    > - Prozent als Hundertstel (45 % = 0,45) – Einheit 5. Thema Prozentrechnung, Einheit 1. [RLP E]
  - Zeile 33:
    > - Kreissektor als Anteil vom Vollkreis (120° von 360°) – Einheit 1, nur in der P10-Form mit Sektoren. Thema Kreis, Einheit 3. [P10 2026-FOR-B1b]
- **flaechen** – 7 Nennungen in Wortform in 7 Zeilen:
  - Zeile 27:
    > - Längeneinheiten umrechnen (mm, cm, m), gemischte Angaben angleichen – Einheit 1 und 5. Thema Einheiten. [RLP D, MSK S1A]
  - Zeile 28:
    > - Flächeneinheiten (cm², m²) und Umrechnungszahl 100 – alle Einheiten. Thema Einheiten. [RLP D, MSK S1B]
  - Zeile 29:
    > - Multiplizieren und Dividieren mit Dezimalzahlen (Kommazahl mal Kommazahl, zweistellig geteilt durch einstellig) – alle Einheiten. Thema Bruchrechnung. [P10 Fehlerquellen]
  - Zeile 30:
    > - Formel nach einer Größe umstellen (A = a · b → b = A : a) – Einheit 1, 3 und 4. Thema Lineare Gleichungen, Einheit 4. [RLP E „Umstellen von Formeln“]
  - Zeile 31:
    > - Rechten Winkel erkennen und einzeichnen (Geodreieck) – Einheit 2 bis 4. Thema Winkel. [RLP D]
  - Zeile 32:
    > - Wurzel ziehen bei Quadratzahlen (√49) – Einheit 1 (Quadratseite). Thema Potenzen und Wurzeln. [P10 Typ „Quadratseite aus Fläche“]
  - Zeile 33:
    > - Kreisfläche (π · r²) – nur Einheit 5 mit Kreisteilen. Thema Kreis. [P10]
- **koerper** – 5 Nennungen in Wortform in 5 Zeilen:
  - Zeile 27:
    > - Flächeninhalt von Rechteck, Dreieck, Trapez und Kreis (Grundflächen) – Einheit 2 bis 5. Thema Flächen, Kreis. [RLP D/E]
  - Zeile 28:
    > - Längen- und Volumeneinheiten, Kubikdezimeter als Liter, Kubikzentimeter als Milliliter, Umrechnen zwischen beiden – Einheit 2, 4, 5. Thema Einheiten. [RLP D; P10 2021-OS-K4a]
  - Zeile 29:
    > - Multiplizieren mit Dezimalzahlen und π, Runden; Quadrieren und Wurzelziehen – Einheit 3 und 4. Thema Bruchrechnung Einheit 4, Potenzen und Wurzeln. [RLP D/F]
  - Zeile 30:
    > - Formel nach einer Größe umstellen (V = G · h → h = V : G) – Einheit 2 bis 4. Thema Lineare Gleichungen, Einheit 4. [RLP E „Umstellen von Formeln“]
  - Zeile 31:
    > - Prozentwert berechnen (zehn Prozent von einem Volumen mit Komma) – Einheit 5. Thema Prozentrechnung, Einheit 3. [P10 2019-OS-K4c]
- **kreis** – 6 Nennungen in Wortform in 6 Zeilen:
  - Zeile 23:
    > - Mit Dezimalzahlen multiplizieren und dividieren, Taschenrechner mit π, Ergebnis runden (Näherungswert mal Kommazahl) – alle Einheiten. Thema Bruchrechnung, Einheit 4. [RLP D/E „sinnvolle Genauigkeit“]
  - Zeile 24:
    > - Quadrieren und Wurzelziehen (4,5²; √20,25) – Einheit 2 (r aus A). Thema Potenzen und Wurzeln. [RLP F; P10 2022-OS-K2d]
  - Zeile 25:
    > - Formel nach einer Größe umstellen (u = π · d → d = u : π) – Einheit 1 und 2. Thema Lineare Gleichungen, Einheit 4. [RLP E „Umstellen von Formeln“]
  - Zeile 26:
    > - Winkel messen und zeichnen, Vollwinkel – Einheit 3. Thema Winkel. [RLP D]
  - Zeile 27:
    > - Anteil als Bruch und Prozentsatz bilden (Mittelpunktswinkel zum Vollwinkel als Prozent) – Einheit 3. Thema Brüche und Dezimalzahlen, Prozentrechnung Einheit 2. [P10 2025-OS-B1e]
  - Zeile 28:
    > - Fläche und Umfang unterscheiden; Einheiten cm, cm², m, m² – alle Einheiten. Thema Flächen, Einheit 1. [RLP D]
- **lineare-funktionen** – 1 Nennung in Wortform in 1 Zeile:
  - Zeile 28:
    > - Lineare Gleichung zweischrittig lösen (null gleich einem zweischrittigen Term). [Thema Lineare Gleichungen, Einheit 2] – für Einheit 3 (Nullstelle, Argument) und 4 (Schnittpunkt).
- **lineare-gleichungen** – 2 Nennungen in Wortform in 2 Zeilen:
  - Zeile 23:
    > - Terme zusammenfassen (gleichartige Glieder mit x, Zahl und x gemischt) – ab Einheit 2 (vor dem Umformen), Einheit 3 zwingend. Thema Terme, Einheit 2. [RLP E]
  - Zeile 25:
    > - Klammern auflösen – nur Einheit 3. Thema Terme, Einheit 3. [RLP F]
- **potenz-exponentialfunktionen** – 8 Nennungen in Wortform in 8 Zeilen:
  - Zeile 25:
    > - Erhöhung und Senkung um p Prozent als Faktor: neuer Wert gleich alter Wert mal eins plus p Hundertstel, bei Abnahme minus – alle Einheiten. Thema Prozentrechnung, Einheit 5. [RLP F; LISUM-PH „Prozentsatz als Operator (Wachstumsfaktor)“; P10 2018-OS-K2a Verfahren]
  - Zeile 26:
    > - Prozentwert und Prozentsatz berechnen: Anteil vom Grundwert, Teil geteilt durch Ganzes, Dezimalzahl in Prozent – Einheit 2. Thema Prozentrechnung, Einheit 2 und 3. [RLP E; P10 2018-OS-K2a Nebenweg]
  - Zeile 27:
    > - Potenz mit dem Taschenrechner: Taste ^ oder xʸ, Basis mit Komma, Ergebnis erst am Ende runden – Einheit 3 und 4. Thema Potenzen und Wurzeln, Einheit 1. [P10 2020-OS-K4c, 2025-OS-K7b, 2026-FOR-K7c Voraussetzung „Potenz mit dem Taschenrechner“]
  - Zeile 28:
    > - Zinseszins: Zinsen kommen zum Guthaben, im nächsten Jahr wird das neue Guthaben verzinst, Endkapital als Startkapital mal Faktor hoch Jahre – Einheit 2 und 3 (Brücke, kein neuer Stoff). Thema Zinsrechnung, Einheit 2. [P10 2014-OS-K3c; LISUM-PH Sachkontext Spareinlagen]
  - Zeile 29:
    > - Wertetabelle lesen und Punkte ins Koordinatensystem eintragen, Achseneinteilung wählen, Werte an einer Skala mit größeren Schritten ablesen – Einheit 1 und 4. Thema Zuordnungen, Einheit 1. [RLP D/E; P10 2025-OS-K7a, 2016-OS-K4b, 2017-OS-K7b]
  - Zeile 30:
    > - Lineare Zunahme: gleicher Betrag je Schritt, Graph ist eine Gerade, Startwert auf der y-Achse – Einheit 1. Thema Lineare Funktionen, Einheit 1 und 2. [RLP F; LISUM-PH „Addition einer konstanten Zahl“]
  - Zeile 31:
    > - Dezimalzahlen multiplizieren und runden, Ergebnis mit ≈ und Einheit angeben – alle Einheiten. Thema Bruchrechnung, Einheit 4; Brüche und Dezimalzahlen, Einheit 5. [P10 alle Originale mit Hilfsmitteln]
  - Zeile 32:
    > - Division zweier Tabellenwerte als Quotient schreiben und deuten – Einheit 2. Thema Bruchrechnung, Einheit 3. [P10 2025-OS-K7b Verfahren „Quotienten aufeinanderfolgender Werte“]
- **prozentrechnung** – 2 Nennungen in Wortform in 2 Zeilen:
  - Zeile 27:
    > - Bruch als Anteil lesen und kürzen (drei von zwölf, gekürzt ein Viertel), auf den Nenner hundert erweitern – Einheit 1 und 2. Thema Brüche. [MSK B1B/B2C, RLP D]
  - Zeile 31:
    > - Hoch- und Runterrechnen in einer Tabelle (Dreisatz, proportionale Zuordnung) – Einheit 2 bis 4. Thema Zuordnungen. [MSK S5A, LS-AA Kl. 6 VI 3]
- **pyramide-kegel-kugel** – 9 Nennungen in Wortform in 9 Zeilen:
  - Zeile 25:
    > - Flächeninhalt von Quadrat, Rechteck, Dreieck (Seitenflächen) und Kreis (Grundkreis) – Einheit 1 und 2. Thema Flächen, Kreis Einheit 2. [RLP D/E; P10 2024-OS-K4a]
  - Zeile 26:
    > - Volumen von Prisma und Zylinder als Grundfläche mal Höhe (der Bezugskörper für das Drittel) und Mantel des Zylinders – Einheit 1 und 2. Thema Körper, Einheit 3 und 4. [RLP E; LS-AA Kl. 8 VII; P10 2026-FOR-K2a]
  - Zeile 27:
    > - Satz des Pythagoras: Hypotenuse und Kathete berechnen, Wurzel ziehen – Einheit 1 und 2 (Stützdreieck). Thema Pythagoras. [RLP E/F; LS-AA Kl. 9 V 2 „in Figuren und Körpern“; LISUM-PH „Nutzen des Satzes des Pythagoras für Berechnungen an Pyramiden“; P10 2018-OS-K6d, 2026-FOR-K2c]
  - Zeile 28:
    > - Radius aus Durchmesser – Einheit 2 und 3. Thema Kreis, Einheit 1. [P10 2016-OS-K3b, 2016-OS-K3c, 2018-OS-K6d]
  - Zeile 29:
    > - Quadrieren und hoch drei, Wurzel und Kubikwurzel mit dem Taschenrechner, Rechnen mit π, Runden auf eine sinnvolle Stelle – alle Einheiten. Thema Potenzen und Wurzeln. [RLP F]
  - Zeile 30:
    > - Ein Drittel und vier Drittel einer Zahl: durch drei teilen, mal vier durch drei – alle Einheiten. Thema Brüche und Dezimalzahlen, Einheit 1; Bruchrechnung, Einheit 3. [RLP D]
  - Zeile 31:
    > - Formel aus der Formelsammlung entnehmen und nach einer Größe umstellen (Volumenformel mit Bruchfaktor nach der Höhe) – alle Einheiten. Thema Lineare Gleichungen, Einheit 4. [RLP E „Umstellen von Formeln“; P10 2026-FOR-K2a, 2016-OS-K3c „Formel aus der Formelsammlung entnehmen“]
  - Zeile 32:
    > - Volumeneinheiten cm³ → dm³ = l mit 1000, m³; Masse aus Volumen und Dichte – Einheit 2 und 3. Thema Einheiten. [RLP D; P10 2016-OS-K3d]
  - Zeile 33:
    > - Termumformung mit Variablen: (3r)² = 9 · r², gemeinsamen Faktor herausziehen – Einheit 2 (Niveau III). Thema Terme; Potenzen und Wurzeln. [P10 2026-FOR-K2d]
- **pythagoras** – 9 Nennungen in Wortform in 9 Zeilen:
  - Zeile 23:
    > - Quadrieren mit dem Taschenrechner, auch Dezimalzahlen; Quadratzahlen bis zwanzig hoch zwei aus dem Kopf; Quadrat vor Strich – alle Einheiten. Thema Potenzen und Wurzeln. [RLP F „Beschreiben von Quadrat- und Kubikwurzel“; LS-AA Kl. 8 IV 1]
  - Zeile 24:
    > - Quadratwurzel mit dem Taschenrechner ziehen: erst die Summe oder Differenz unter der Wurzel ausrechnen, dann die Wurzel, dann den Näherungswert runden – alle Einheiten. Thema Potenzen und Wurzeln. [RLP F/G; P10 „Wurzel ziehen“ als Voraussetzung in 2024-OS-K6a, 2025-OS-K2a, 2026-FOR-K2c, 2026-FOR-K4a]
  - Zeile 25:
    > - Rechtwinkliges Dreieck erkennen: Rechtwinkelmarke (Bogen mit Punkt) in der Skizze finden, Dreiecksarten – alle Einheiten. Thema Winkel und Dreiecke, Einheit 3. [RLP D „Systematisieren von Dreiecken“; P10 2022-OS-K5a „nicht rechtwinklig“]
  - Zeile 26:
    > - Formel nach einer Größe umstellen mit Strich, hier c² = a² + b² nach a² – Einheit 2. Thema Lineare Gleichungen, Einheit 4. [RLP E „Umstellen von Formeln“]
  - Zeile 27:
    > - Längeneinheiten: Ergebnis mit Einheit, cm und m vor dem Rechnen angleichen, Runden auf eine Dezimale – alle Einheiten. Thema Einheiten. [RLP D/E „sinnvolle Genauigkeit“; P10 Ergebnisse in m und cm]
  - Zeile 28:
    > - Koordinaten ablesen und Differenzen bilden, auch mit negativen Zahlen – Einheit 3. Thema Lineare Funktionen (Blatt 0); Rationale Zahlen. [RLP E „vier Quadranten“; P10 2019-OS-K2d „Koordinaten stehen nur im Bild“]
  - Zeile 29:
    > - Höhe, Seitenhöhe, Seitenkante, Mantellinie und Radius an Pyramide und Kegel benennen, Radius aus dem Durchmesser – Einheit 3. Thema Pyramide, Kegel, Kugel; Kreis. [P10 2018-OS-K6d, 2026-FOR-K2c Fehlerquellen]
  - Zeile 30:
    > - Eigenschaften von gleichschenkligem Dreieck, gleichschenkligem Trapez, Parallelogramm, Drachen und Rechteck: Höhe, Symmetrieachse, Diagonalen – Einheit 3. Thema Winkel und Dreiecke, Einheit 3; Flächen. [RLP D/E; P10 2025-OS-K2a, 2023-OS-K2c]
  - Zeile 31:
    > - Strecke halbieren, halbe Differenz zweier Seiten bilden (Überstand am Trapez) – Einheit 3. Thema Bruchrechnung. [P10 Fehlerquellen 2015-OS-K6c, 2025-OS-K2a, 2014-OS-K5c „ganze statt halbe Seite“]
- **quadratische-funktionen** – 8 Nennungen in Wortform in 8 Zeilen:
  - Zeile 25:
    > - Quadrieren auch negativer Zahlen und Dezimalzahlen, Quadrat vor Punkt vor Strich: (−7)² = 49, nicht −49; 0,5² = 0,25 – alle Einheiten. Thema Rationale Zahlen, Potenzen und Wurzeln. [RLP E/F; P10 Fehlerquellen 2014-OS-K7a, 2018-OS-K5a, 2024-OS-K3c]
  - Zeile 26:
    > - Koordinaten lesen und eintragen, vier Quadranten, (x | y)-Reihenfolge, Kästchenraster mit 0,5-Einteilung – Einheit 1 und 2. Thema Lineare Funktionen (Blatt 0). [RLP E; P10 2021-OS-B1d Fehlerquelle „Koordinaten vertauschen“]
  - Zeile 27:
    > - Lineare Funktion f(x) = m·x + n: Gerade zeichnen, Funktionswert, Punktprobe, Nullstelle – Einheit 1 und 4. Thema Lineare Funktionen, Einheit 2 und 3. [RLP F; LS-AA Kl. 9 I 1 Wiederholung]
  - Zeile 28:
    > - Binomische Formel ausmultiplizieren und zusammenfassen, auch mit Minus in der Klammer – Einheit 3 und 4. Thema Binomische Formeln. [RLP G „auch unter Nutzung der binomischen Formeln“; LS-AA Kl. 8 II 4]
  - Zeile 29:
    > - Quadratwurzel ziehen, auch mit dem Taschenrechner, Näherungswert runden; aus einer negativen Zahl gibt es keine Wurzel – Einheit 4. Thema Potenzen und Wurzeln. [RLP F/G; LS-AA Kl. 8 IV 1]
  - Zeile 30:
    > - Quadratische Gleichung durch Wurzelziehen lösen und Normalform mit der p-q-Formel lösen, beide Lösungen angeben – Einheit 4. Thema Quadratische Gleichungen. [RLP G „Lösen von Gleichungen (auch quadratische …)“; LS-AA Kl. 9 II 3 und II 5]
  - Zeile 31:
    > - Lineare Gleichung lösen, Terme mit x auf eine Seite bringen, Schreibform mit Strich – Einheit 4. Thema Lineare Gleichungen, Einheit 2. [RLP E]
  - Zeile 32:
    > - Schnittpunkt zweier Geraden durch Gleichsetzen – Einheit 4. Thema Lineare Funktionen, Einheit 4; Lineare Gleichungssysteme, Einheit 2. [RLP G S. 61 Schnittpunkte von Funktionsgraphen]
- **quadratische-gleichungen** – 8 Nennungen in Wortform in 8 Zeilen:
  - Zeile 28:
    > - Quadrieren auch negativer Zahlen und Dezimalzahlen, Quadrat vor Punkt vor Strich: (−11)² = 121, nicht −121; 1,5² = 2,25 – alle Einheiten. Thema Rationale Zahlen, Potenzen und Wurzeln. [RLP E/F; P10 Fehlerquelle 2025-OS-B1h „Vorzeichen beim Einsetzen negativer Werte“]
  - Zeile 29:
    > - Quadratwurzel ziehen: Quadratzahlen bis 15² erkennen (√121 = 11), sonst Taschenrechner und Näherungswert runden (√5 ≈ 2,24); aus einer negativen Zahl gibt es keine Wurzel – Einheit 1 und 3. Thema Potenzen und Wurzeln. [RLP F/G; LS-AA Kl. 8 IV 1–2; P10 2025-OS-K5c Ergebnis mit Wurzel und Näherungswert]
  - Zeile 30:
    > - Lineare Gleichung mit Äquivalenzumformungen und Strich lösen, auch negative Vorzahl und x auf beiden Seiten: x + 5 = 12 | −5; −x = 5; 5x = 15 | : 5 – alle Einheiten (Rückwärtsrechnen, Faktoren null setzen, Ordnen). Thema Lineare Gleichungen, Einheit 2 und 3. [RLP E/F; LS-AA Kl. 7 IV 5]
  - Zeile 31:
    > - Lösung durch Einsetzen prüfen mit (wA)/(fA), auch mit negativer Zahl: x = −5 in x + 17 = 12 → 12 = 12 (wA) – alle Einheiten. Thema Lineare Gleichungen, Einheit 1. [RLP E „Prüfen einer Lösung durch Einsetzen“; P10 2018-OS-B1c, 2022-OS-B1c, 2025-OS-B1h]
  - Zeile 32:
    > - Klammer zuerst und Punkt vor Strich mit negativen Zahlen: (−5) · (−5 + 17) = (−5) · 12 = −60 – Einheit 1 und 2 (Probe). Thema Rationale Zahlen. [P10 2025-OS-B1h Zwischenergebnisse]
  - Zeile 33:
    > - Ausklammern, Ausmultiplizieren und binomische Formeln: x·(x + 5) = x² + 5x; (x + 13)² = x² + 26x + 169; auch mit Minus in der Klammer – Einheit 2 und 3. Thema Terme, Einheit 3; Binomische Formeln. [RLP F/G „auch unter Nutzung der binomischen Formeln“; LS-AA Kl. 8 II 3–4; P10 2022-OS-K3c, 2017-OS-K5d Fehlerquelle „Mittelglied fehlt“]
  - Zeile 34:
    > - Terme ordnen und zusammenfassen, x² zuerst, dann x-Glieder, dann Zahlen: x² − 5 + 12x + 17 → x² + 12x + 12 – Einheit 3. Thema Terme, Einheit 2. [RLP E]
  - Zeile 35:
    > - Scheitelpunktform lesen: (x − 5)² − 11 hat den Scheitel S(5 | −11) und ist nach oben geöffnet; Zahl der Nullstellen am Scheitel – Einheit 1 (Zahl der Lösungen am Graphen). Thema Quadratische Funktionen, Einheit 2. [RLP G; P10 2021-OS-K7c Stichwort „Scheitelpunktform“]
- **rationale-zahlen** – 2 Nennungen in Wortform in 2 Zeilen:
  - Zeile 27:
    > - Dezimalzahlen und Brüche addieren, subtrahieren, multiplizieren (Kommazahlen addieren, Bruch mal ganze Zahl) – Einheit 2 und 3. Thema Bruchrechnung. [RLP D]
  - Zeile 29:
    > - Wert eines Terms mit Platzhalter berechnen (Vorzahl mal x plus Zahl, für einen gegebenen Einsetzwert) – Einheit 3 und 4. Thema Terme. [RLP D]
- **strahlensaetze** – 9 Nennungen in Wortform in 9 Zeilen:
  - Zeile 23:
    > - Dezimalzahlen und ganze Zahlen mal und geteilt durch eine Zahl (auch nicht durch Zehnerpotenzen: dreißig geteilt durch fünfzig), Kommaverschiebung bei zehn, hundert, tausend – Einheit 1 und 3. Thema Bruchrechnung, Einheit 5; Brüche und Dezimalzahlen, Einheit 4. [RLP D; P10 2018-OS-K6c Verfahren „Meter durch fünfzig, dann in Zentimeter“]
  - Zeile 24:
    > - Längeneinheiten umrechnen (m in cm und zurück, km in m, mm in cm), Ergebnis in einer sinnvollen Einheit angeben – Einheit 1 und 3. Thema Einheiten. [RLP D/E „Umwandeln von Einheiten der Länge“; P10 2018-OS-K6c Voraussetzung „m in cm umrechnen“]
  - Zeile 25:
    > - Vielfache und Teiler, „doppelt“, „halb“, „dreifach“, „ein Drittel“ als Rechnung – Einheit 1 und 2. Thema Zuordnungen, Einheit 2. [RLP D; MSK S5A]
  - Zeile 26:
    > - Dreisatz und fester Faktor („pro Portion“; k = Preis je Stück) – Einheit 1 und 3 (Maßstab als fester Faktor). Thema Zuordnungen, Einheit 2. [RLP D/E „auch Maßstab und Prozentrechnung“]
  - Zeile 27:
    > - Verhältnis lesen und als Division schreiben („drei zu fünf“ als Bruch und als Quotient, auch als Dezimalzahl) – Einheit 2 und 3. Thema Bruchrechnung; Zuordnungen, Einheit 2 (Verhältnisgleichung als Vorrat dort). [RLP E „Verhältnisgleichungen“; Lernhelfer]
  - Zeile 28:
    > - Gleichung mit einer Variablen und Verhältnisgleichung nach x umstellen (x geteilt durch die bekannte Strecke gleich dem Verhältnis der zwei anderen; auf beiden Seiten mal nehmen) – Einheit 2 und 3. Thema Lineare Gleichungen, Einheit 2. [RLP E „Lösen von Verhältnisgleichungen (auch Umstellen von Formeln)“]
  - Zeile 29:
    > - Strecken auf Millimeter messen und zeichnen, Rechteck mit dem Geodreieck, Kreis mit dem Zirkel (Radius als halber Durchmesser), Parallelen mit dem Geodreieck zeichnen und erkennen – Einheit 1 bis 3. Thema Winkel und Dreiecke, Einheit 1; Kreis, Einheit 1. [RLP D „Zeichnen von ebenen Figuren mithilfe von Zeichengeräten“; P10 2021-OS-K4c Voraussetzungen „Durchmesser aus Radius; Kreis mit Zirkel“]
  - Zeile 30:
    > - Winkel messen und vergleichen, Winkelsumme im Dreieck (zwei Winkel gleich → der dritte auch) – Einheit 2. Thema Winkel und Dreiecke, Einheit 1 und 3. [RLP D/E]
  - Zeile 31:
    > - Draufsicht, Netz und Schrägbild eines Körpers unterscheiden; Draufsicht eines Zylinders ist ein Kreis, eines Quaders ein Rechteck – Einheit 1 (Zeichenaufgabe). Thema Körper, Einheit 1. [RLP D „Herstellen von Würfelbauten nach Ansichten“; P10 2021-OS-K4c „Draufsicht = Kreis und Rechteck“]
- **symmetrie-abbildungen** – 7 Nennungen in Wortform in 7 Zeilen:
  - Zeile 23:
    > - Kästchen im Raster abzählen und Strecken auf dem Karo abtragen – alle Einheiten. Thema Winkel und Dreiecke, Einheit 1; Flächen, Einheit 1. [RLP C „Zeichnen von Spiegelbildern auf Rasterpapier“]
  - Zeile 24:
    > - Senkrechte und parallele Geraden mit dem Geodreieck zeichnen und erkennen, Abstand eines Punktes von einer Geraden messen – Einheit 1 bis 3. Thema Winkel und Dreiecke, Einheit 1. [RLP D „Zeichnen von Senkrechten und Parallelen mithilfe des Geodreiecks“; LS-AA Kl. 5 II 1]
  - Zeile 25:
    > - Negative Zahlen an der Zahlengeraden ablesen und eintragen – Einheit 1 (vier Quadranten). Thema Rationale Zahlen, Einheit 1. [RLP E „vier Quadranten“; LS-AA Kl. 6 IV 1]
  - Zeile 26:
    > - Vierecksarten und Dreiecksarten an ihren Eigenschaften erkennen und benennen (Quadrat, Rechteck, Raute, Parallelogramm, Drachenviereck, gleichschenkliges Trapez; gleichseitiges und gleichschenkliges Dreieck) – Einheit 2 und 3. Thema Winkel und Dreiecke, Einheit 3. [RLP C „Haus der Vierecke“, D „Systematisieren von Dreiecken“; P10 2022-OS-B1i, 2021-OS-B1j, 2018-OS-B1h Voraussetzungen]
  - Zeile 27:
    > - Diagonalen eines Vierecks einzeichnen und benennen – Einheit 2. Thema Winkel und Dreiecke, Einheit 3; Flächen, Einheit 4. [P10 2021-OS-B1j Verfahren „zwei Mittelsenkrechten und zwei Diagonalen“; 2025-OS-K2a]
  - Zeile 28:
    > - Winkel messen und zeichnen, rechten Winkel erkennen und markieren – Einheit 2 und 3. Thema Winkel und Dreiecke, Einheit 1. [RLP D; LISUM-PH „Länge, Winkel, Drehung, Verschiebung“]
  - Zeile 29:
    > - Strecken messen und gleich lange Strecken abtragen – Einheit 2 und 3. Thema Winkel und Dreiecke, Einheit 1. [RLP C „Erzeugen von Spiegelbildern“]
- **terme** – 0 Nennungen in Wortform
- **trigonometrie** – 8 Nennungen in Wortform in 8 Zeilen:
  - Zeile 25:
    > - Rechtwinkliges Dreieck erkennen, Rechtwinkelmarke (Bogen mit Punkt), Hypotenuse gegenüber dem rechten Winkel, Katheten am rechten Winkel – alle Einheiten. Thema Satz des Pythagoras, Einheit 1; Winkel und Dreiecke, Einheit 3. [RLP D „Systematisieren von Dreiecken“; P10 2018-OS-K4c Fehlerquelle „Dreieck als rechtwinklig behandeln“]
  - Zeile 26:
    > - Winkel benennen (α, β, γ, auch β1, β2, ε), Winkel messen und schätzen, spitz oder stumpf – alle Einheiten. Thema Winkel und Dreiecke, Einheit 1. [RLP D „Messen von Winkeln“; P10 Beschriftungen 2024-OS-K6b, 2026-FOR-K4b]
  - Zeile 27:
    > - Winkelsumme im Dreieck, die beiden spitzen Winkel des rechtwinkligen Dreiecks als Ergänzung, Winkel aus Teilwinkeln (Differenz), Strecke aus Teilstrecken – Einheit 2, 3 und 4. Thema Winkel und Dreiecke, Einheit 1 und 3. [RLP D/E; P10 Nebentypen „Winkelsumme im Dreieck anwenden“, „Winkel aus Teilwinkeln berechnen“, „Strecke aus Teilstrecken berechnen“ in 2016-OS-K7c, 2019-OS-K3c, 2020-OS-K7c, 2021-OS-K3c, 2024-OS-K6d, 2025-OS-K4c]
  - Zeile 29:
    > - Gleichung mit einem Bruch nach einer Größe umstellen, Größe im Zähler (mal) oder im Nenner (geteilt), mit Strich – Einheit 1 und 4. Thema Lineare Gleichungen, Einheit 2 und 4. [RLP E „Umstellen von Formeln“; P10 2020-OS-B1j, 2022-OS-K5d, 2026-FOR-K4c „Gleichung nach der Hypotenuse umstellen“]
  - Zeile 30:
    > - Bruch als Verhältnis lesen und in eine Dezimalzahl umwandeln – Einheit 1 und 2. Thema Brüche und Dezimalzahlen. [RLP D; P10 2019-OS-K3b Zwischenergebnis „cos α = 0,444“]
  - Zeile 31:
    > - Satz des Pythagoras als zweiter Weg zur dritten Seite, Vergleich der Ergebnisse – Einheit 1 und 3. Thema Satz des Pythagoras, Einheit 1 und 2. [RLP E; P10 2016-OS-K7b, 2021-OS-K3b, 2023-OS-K2c „Trigonometrie oder Pythagoras“]
  - Zeile 32:
    > - Längeneinheiten vor dem Rechnen angleichen (m und km, cm und m), Ergebnis mit Einheit, Runden auf eine Dezimale – Einheit 3 und 4. Thema Einheiten. [RLP E „sinnvolle Genauigkeit“; P10 2014-OS-K2b Meter und Kilometer gemischt]
  - Zeile 33:
    > - Höhe, Diagonale, Überstand am Trapez, Fußpunkt auf der Verlängerung beim Parallelogramm, halbe Diagonale im Drachen – Einheit 3. Thema Flächen; Satz des Pythagoras, Einheit 3. [RLP D/E; P10 2020-OS-K5b, 2023-OS-K2c, 2026-FOR-K4b, 2015-OS-K5c]
- **wahrscheinlichkeit** – 4 Nennungen in Wortform in 4 Zeilen:
  - Zeile 25:
    > - Brüche kürzen; Bruch ↔ Dezimalzahl ↔ Prozent (Achtelbruch als Dezimalzahl und Prozentsatz) – Einheit 2 bis 4. Thema Brüche und Dezimalzahlen, Einheit 2 und 4. [P10 2014-OS-K6a, 2017-OS-K6a]
  - Zeile 26:
    > - Brüche multiplizieren (auch drei Faktoren) und gleichnamige Brüche addieren – Einheit 3 und 4. Thema Bruchrechnung, Einheit 3 und 1. [RLP D; P10 2019-OS-K6b]
  - Zeile 27:
    > - Anteil einer Menge nehmen (30 % von 10 Feldern; zwei Drittel von 9 Kugeln) – Einheit 2 (Zufallsgerät entwerfen). Thema Brüche und Dezimalzahlen, Einheit 1; Prozentrechnung, Einheit 3. [P10 2018-OS-B1j, 2019-OS-B1g]
  - Zeile 28:
    > - Relative Häufigkeit berechnen (Anzahl geteilt durch Gesamtzahl) – Einheit 2 (Gesetz der großen Zahlen). Thema Daten, Einheit 1. [RLP D/E]
- **winkel-dreiecke** – 3 Nennungen in Wortform in 3 Zeilen:
  - Zeile 28:
    > - Addieren und Subtrahieren im Bereich bis zum Vollwinkel, auch mit Dezimalzahlen (Vielfaches minus zwei Dezimalgrade) – alle Einheiten. Thema Brüche und Dezimalzahlen, Einheit 5. [P10 2017-OS-K4a Fehlerquelle]
  - Zeile 29:
    > - Längeneinheiten m und km umrechnen (1,5 km = 1500 m) – Einheit 1 (Teilstrecken). Thema Einheiten. [P10 2014-OS-K2b]
  - Zeile 31:
    > - Kreis mit dem Zirkel zeichnen, Radius und Durchmesser unterscheiden – Einheit 4 und 5. Thema Kreis, Einheit 1. [RLP D „Zeichnen ebener Figuren … Zirkel“]
- **zuordnungen** – 2 Nennungen in Wortform in 2 Zeilen:
  - Zeile 27:
    > - Punkte im Koordinatensystem eintragen und ablesen (erster Quadrant) – Einheit 1 und 2. Thema Symmetrie, Abbildungen und Koordinatensystem, Einheit 1 (seit 09e gefüllt). [RLP D]
  - Zeile 29:
    > - Einheiten umrechnen (Cent ↔ Euro, Minuten ↔ Stunden, m ↔ km) – Einheit 4. Thema Einheiten. [P10 Fehlerquellen]

## Schwäche der Messung
Die Prüfungen sehen Zeichenketten, keine Bedeutung. Prüfung 1 findet nur die Form `<name>.md`; ein Thema, das in Wortform genannt ist („Thema Lineare Gleichungen“), hat weder Ziel noch Fundort und fehlt in allen Gruppen – Prüfung 5 zeigt, wie viele Einträge so schreiben. Prüfung 2 ordnet nur zu, was unmittelbar hinter einem Verweis steht; die Nennungen in Wortform tragen ihre Einheitsnummern ungeprüft, und eine Angabe, die einen Satz weiter steht, gilt als eigene Einheit, auch wenn die Zieldatei gemeint war. Die Zahl der Lerneinheiten ist die Zahl der nummerierten Zeilen, nicht die höchste Nummer; der Verweiseintrag hat null. Prüfung 3 vergleicht Namen wortgleich – eine abweichende H1 kann Absicht sein (Sammelthema, mehrere Prüfungsthemen), eine gleiche H1 sagt nichts über den Inhalt. Prüfung 4 zählt eine Erwähnung in jedem Abschnitt gleich, auch eine in der Prüfliste oder in einem offenen Punkt; ob die Gegenrichtung fachlich nötig ist, entscheidet sie nicht. Prüfung 5 zählt mit der Heuristik des Vorbilds; sie übersieht Nennungen ohne das Wort „Thema“ und zählt das Wort auch, wo es kein Verweis ist. Alle fünf messen die Schreibform der Einträge, nicht den Unterricht.
