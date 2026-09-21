# Verweise und Namen – Prüfung des Themenkatalogs
Stand 2026-09-21, Katalog auf Commit 795ca0a.
Erzeugt von `werkzeuge/verweis-pruef.py` (v0.2) aus den Einträgen, `themen.csv`, `abitur/abitur-vokabular.md`, den vier `abitur/abi-*-geltung.md` und den Typenkatalogen `msa/msa-typen.csv` und `fhr/fhr-typen.csv`; abgeleitet, nie von Hand ändern. Fünf Prüfungen der inneren Stimmigkeit vor dem Umbau der Blatt-Prompte: Dateiverweise, Einheitennummern, Namensgleichheit, Gegenrichtung, Formlücke. Befunde werden berichtet, nicht behoben; wo eine Zuordnung nicht eindeutig ist, steht der Fall in einer eigenen Liste statt in einer Entscheidung.

Gemessen: 73 Einträge (`katalog/*.md` ohne `_*` und `index.md`). Lesarten wie in `werkzeuge/tragfaehigkeit.py` (v0.2), importiert, nicht nachgebaut: Verweis = Zeichenkette der Form `<name>.md` (auch in Klammern oder Backticks; ein Pfad davor wird mitgenommen), Blatt-0-Abschnitt = „### Voraussetzungen (Blatt 0)“ bis zur nächsten Überschrift, Nennung in Wortform = „Thema “ vor einem Großbuchstaben (Heuristik; folgt dem Titel unmittelbar „ (<name>.md“, ist es ein Verweis und keine Nennung in Wortform), Fundort einer Datei außerhalb von `katalog/` = Suche im Repo nach dem Dateinamen. Abschnitt einer Fundstelle = die nächste Überschrift davor (#, ##, ###); in den Listen abgekürzt: Kopf (Titel und Statuszeilen), Verortung, Lerneinheiten, Typen (Typen je Lerneinheit), Blatt 0, Merkkasten, Fehler (Typische Fehler), Schwache (Für schwache Schüler), Prüfungsform, Offene Punkte, Prüfliste. Zeilennummern zählen ab 1 in der Datei. Zahl der Lerneinheiten eines Eintrags = Zeilen im Abschnitt „### Lerneinheiten“, die mit „<n>. “ beginnen.

## 1 Dateiverweise
Jeder Verweis `<name>.md` in jedem Abschnitt jedes Eintrags, nicht nur in Blatt 0. Gruppe (a): das Ziel liegt in `katalog/` (Katalogeintrag, Selbstverweis, Katalogeintrag mit Pfadangabe oder eine andere Datei des Ordners); Gruppe (b): das Ziel liegt anderswo im Repo (ohne Pfadangabe über den Fundort, mit Pfadangabe über den Pfad relativ zur Wurzel); Gruppe (c): keine Datei dieses Namens im Repo. Gruppe (b) und (c) vollständig, je Ziel eine Zeile und darunter je Quelldatei die Abschnitte (×n = mehrfach im Abschnitt).

2975 Verweise in 73 Einträgen. Gruppe (a) Ziel in `katalog/`: 2722 – davon 2584 auf andere Katalogeinträge, 54 Selbstverweise, 1 auf Katalogeinträge mit Pfadangabe, 83 auf andere Dateien in `katalog/` (`_*.md`, `index.md`). Gruppe (b) Ziel anderswo im Repo: 237 Verweise auf 55 Dateien. Gruppe (c) Ziel gibt es nicht: 16 Verweise auf 5 Namen.

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
- **befund-geltung-2026-09-21.md** (liegt in Wurzel) – 6 Verweise aus 2 Einträgen
  - konfidenzintervalle.md (Kopf, Prüfungsform, Offene Punkte)
  - matrizen-und-uebergangsprozesse.md (Kopf, Prüfungsform, Offene Punkte)
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
Eine Einheitenangabe ist „Einheit n“ oder „Einheiten n“ mit einer oder zwei Ziffern, fortgesetzt mit „und“, „bis“, „–“, Komma oder Schrägstrich („Einheit 6 und 8“, „Einheiten 2 bis 4“, „Einheit 2, 3 und 5“). Sie steht hinter einem Verweis, wenn zwischen `<name>.md` und „Einheit“ nur Leerraum, ein Komma oder eine öffnende Klammer steht („x.md Einheit 4“, „x.md, Einheit 4“, „x.md (Einheit 4)“) – oder, in der Klammerform der Blatt-0-Abschnitte seit Commit cfa4723, davor noch der Rest des Klammerinhalts und die schließende Klammer („Thema Terme (terme.md), Einheit 2“, „Kreis (kreis.md) Einheit 2“, „(x.md, Blatt 0), Einheit 2“; „Lineare Funktionen (lineare-funktionen.md, Blatt 0)“ ohne Angabe dahinter bekommt keine); dann wird die größte genannte Nummer gegen die Zahl der Lerneinheiten der Zieldatei gehalten. Nicht eindeutig zuordenbar und deshalb nur gelistet: (1) der Verweis davor steht in einer Reihung („a.md und b.md Einheit 2“, „a.md, b.md Einheit 2“) – welcher gemeint ist, steht nicht da; (2) zwischen Verweis und Angabe stehen bis zu 4 Wörter ohne Satz- oder Klammerende („x.md, dessen Einheit 5“, „x.md (Sek I, Einheit 3)“) – hier kann auch eine eigene Einheit gemeint sein; (3) die Angabe steht vor dem Verweis mit „in“, „im“, „von“, „aus“, „der“, „des“ oder „bei“ dazwischen („Einheit 4 in x.md“). Alle anderen Einheitenangaben – ohne Verweis in der Zeile, hinter einem Satzende oder weiter entfernt – gelten als eigene Einheiten des Eintrags und werden nicht geprüft; Angaben an Nennungen in Wortform („Thema Terme, Einheit 2“) haben keinen Verweis, dem sie zugeordnet werden könnten (die in Blatt 0 stehen unter Prüfung 5).

3866 Einheitenangaben in den Einträgen. Direkt hinter einem Verweis: 516 (516 geprüft, 0 nicht prüfbar, weil das Ziel kein Katalogeintrag ist); davon Nummer größer als vorhanden: 1. Nicht eindeutig einem Verweis zuordenbar: 24. Die übrigen 3326 stehen ohne Verweis davor oder weiter von ihm entfernt; sie gelten als eigene Einheiten des Eintrags und sind nicht geprüft.

### Nummer größer als vorhanden
- lineare-gleichungssysteme.md (Schwache, Zeile 117): „rekonstruktion-von-funktionsgleichungen.md … Einheit 5“ – 3 vorhanden; Zitat: …hungssystem ist dort Werkzeug der Rekonstruktion (rekonstruktion-von-funktionsgleichungen.md), Einheit 5 ist für fhr Vorrat.

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
- kurvenuntersuchung.md (Blatt 0, Zeile 31): kurzer Zwischentext – „Einheit 3“ bei lineare-funktionen.md; Zitat: …te, Einheit 2, 3 und 5. Thema Lineare Funktionen (lineare-funktionen.md, Sek I, Einheit 3); der fhr-Typ „Punktprobe am Graphen“ i…
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

511 Blatt-0-Verweise auf andere Katalogeinträge (Kanten A → B); 297 davon ohne Gegenrichtung: B nennt A.md in keinem Abschnitt. Gruppiert nach B (dort stünde die Erwähnung), 46 Einträge B betroffen.
- **ableitungsregeln** (3): funktionsscharen-und-ortskurven, integrationsregeln, rekonstruktion-von-funktionsgleichungen
- **abstaende** (1): flaecheninhalt-und-volumen-im-raum
- **binomialverteilung** (1): konfidenzintervalle
- **binomische-formeln** (3): ableitungsregeln, gleichungen-loesen, rotationsvolumen
- **bruchrechnung** (23): ableitungsregeln, bedingte-wahrscheinlichkeit-und-bayes, einheiten, flaechen, hypergeometrische-verteilung, kenngroessen-von-verteilungen, koerper, kombinatorik, kreis, lineare-funktionen, lineare-gleichungen, lineare-gleichungssysteme, potenz-exponentialfunktionen, potenzen-wurzeln, pyramide-kegel-kugel, pythagoras, reelle-zahlen, strahlensaetze, trigonometrische-funktionen, unabhaengigkeit, zinsrechnung, zufallsexperimente-und-pfadregeln, zufallsgroessen-und-verteilungen
- **brueche-dezimalzahlen** (14): ableitungsregeln, daten, kombinatorik, potenz-exponentialfunktionen, pyramide-kegel-kugel, reelle-zahlen, strahlensaetze, terme, trigonometrie, wahrscheinlichkeit, winkel-dreiecke, zinsrechnung, zufallsexperimente-und-pfadregeln, zuordnungen
- **daten** (5): bedingte-wahrscheinlichkeit-und-bayes, matrizen-und-uebergangsprozesse, trigonometrische-funktionen, zinsrechnung, zufallsgroessen-und-verteilungen
- **einheiten** (6): ableitung-und-aenderungsrate, daten, pythagoras, rekonstruktion-von-bestaenden, rotationsvolumen, trigonometrie
- **flaechen** (8): extremalprobleme, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, pyramide-kegel-kugel, symmetrie-abbildungen, tangente-normale-schnittwinkel, umkehrfunktion
- **flaecheninhalt-durch-integration** (2): normalverteilung-und-sigma-regeln, umkehrfunktion
- **funktionsklassen-und-eigenschaften** (1): rekonstruktion-von-bestaenden
- **funktionsscharen-und-ortskurven** (1): lagebeziehungen
- **gleichungen-loesen** (9): abstaende, bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, einheiten, extremalprobleme, konfidenzintervalle, scharen-von-geraden-und-ebenen, umkehrfunktion, zufallsexperimente-und-pfadregeln
- **grenzwerte-und-verhalten-im-unendlichen** (1): umkehrfunktion
- **koerper** (6): ebenen, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, rotationsvolumen, schnittmengen, vektoren-und-rechenoperationen
- **kreis** (9): abstaende, daten, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, pythagoras, skalarprodukt-und-winkel, strahlensaetze, zufallsexperimente-und-pfadregeln
- **kurvenuntersuchung** (2): stammfunktion-und-hauptsatz, umkehrfunktion
- **lagebeziehungen** (1): lineare-gleichungssysteme
- **lineare-funktionen** (18): ableitung-und-aenderungsrate, ableitungsregeln, bedingte-wahrscheinlichkeit-und-bayes, ebenen, extremalprobleme, funktionsklassen-und-eigenschaften, geraden, gleichungen-loesen, hypothesentests, konfidenzintervalle, kurvenuntersuchung, pythagoras, quadratische-funktionen, rekonstruktion-von-funktionsgleichungen, stammfunktion-und-hauptsatz, tangente-normale-schnittwinkel, trigonometrische-funktionen, umkehrfunktion
- **lineare-gleichungen** (26): bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, daten, einheiten, flaechen, flaecheninhalt-und-volumen-im-raum, funktionsscharen-und-ortskurven, geraden, gleichungen-loesen, kenngroessen-von-verteilungen, koerper, kreis, lagebeziehungen, lineare-funktionen, lineare-gleichungssysteme, matrizen-und-uebergangsprozesse, pyramide-kegel-kugel, pythagoras, quadratische-funktionen, scharen-von-geraden-und-ebenen, strahlensaetze, trigonometrie, unabhaengigkeit, vektoren-und-rechenoperationen, vierfeldertafel, zufallsexperimente-und-pfadregeln
- **lineare-gleichungssysteme** (4): ebenen, linearkombination-und-lineare-abhaengigkeit, orthogonalitaet, scharen-von-geraden-und-ebenen
- **linearkombination-und-lineare-abhaengigkeit** (2): orthogonalitaet, scharen-von-geraden-und-ebenen
- **orthogonalitaet** (1): scharen-von-geraden-und-ebenen
- **potenz-exponentialfunktionen** (9): ableitung-und-aenderungsrate, ableitungsregeln, binomialverteilung, funktionsklassen-und-eigenschaften, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, matrizen-und-uebergangsprozesse, trigonometrische-funktionen, umkehrfunktion
- **potenzen-wurzeln** (14): ableitungsregeln, daten, funktionsklassen-und-eigenschaften, funktionsscharen-und-ortskurven, grenzwerte-und-verhalten-im-unendlichen, integrationsregeln, kenngroessen-von-verteilungen, kombinatorik, kreis, punkte-und-strecken-im-koordinatensystem, pyramide-kegel-kugel, stammfunktion-und-hauptsatz, vektoren-und-rechenoperationen, zufallsexperimente-und-pfadregeln
- **prozentrechnung** (17): ableitung-und-aenderungsrate, bedingte-wahrscheinlichkeit-und-bayes, binomialverteilung, einheiten, flaecheninhalt-und-volumen-im-raum, geraden, kenngroessen-von-verteilungen, koerper, kombinatorik, konfidenzintervalle, matrizen-und-uebergangsprozesse, normalverteilung-und-sigma-regeln, punkte-und-strecken-im-koordinatensystem, skalarprodukt-und-winkel, unabhaengigkeit, vierfeldertafel, zufallsexperimente-und-pfadregeln
- **punkte-und-strecken-im-koordinatensystem** (1): lineare-gleichungssysteme
- **pyramide-kegel-kugel** (4): ebenen, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, rotationsvolumen
- **pythagoras** (8): abstaende, extremalprobleme, flaecheninhalt-und-volumen-im-raum, punkte-und-strecken-im-koordinatensystem, rotationsvolumen, tangente-normale-schnittwinkel, umkehrfunktion, vektoren-und-rechenoperationen
- **quadratische-funktionen** (8): ableitung-und-aenderungsrate, ableitungsregeln, funktionsklassen-und-eigenschaften, funktionsscharen-und-ortskurven, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, kurvenuntersuchung, rekonstruktion-von-funktionsgleichungen
- **quadratische-gleichungen** (14): abstaende, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, funktionsklassen-und-eigenschaften, funktionsscharen-und-ortskurven, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen, kenngroessen-von-verteilungen, konfidenzintervalle, lagebeziehungen, orthogonalitaet, scharen-von-geraden-und-ebenen, unabhaengigkeit, zufallsexperimente-und-pfadregeln
- **rationale-zahlen** (11): binomische-formeln, funktionsklassen-und-eigenschaften, grenzwerte-und-verhalten-im-unendlichen, integrationsregeln, lineare-gleichungssysteme, potenzen-wurzeln, pythagoras, quadratische-funktionen, quadratische-gleichungen, reelle-zahlen, stammfunktion-und-hauptsatz
- **reelle-zahlen** (4): ableitungsregeln, binomialverteilung, gleichungen-loesen, grenzwerte-und-verhalten-im-unendlichen
- **schnittmengen** (1): scharen-von-geraden-und-ebenen
- **skalarprodukt-und-winkel** (1): scharen-von-geraden-und-ebenen
- **stammfunktion-und-hauptsatz** (1): normalverteilung-und-sigma-regeln
- **strahlensaetze** (9): abstaende, flaecheninhalt-durch-integration, flaecheninhalt-und-volumen-im-raum, funktionsklassen-und-eigenschaften, geraden, gleichungen-loesen, orthogonalitaet, punkte-und-strecken-im-koordinatensystem, schnittmengen
- **symmetrie-abbildungen** (6): funktionsklassen-und-eigenschaften, grenzwerte-und-verhalten-im-unendlichen, punkte-und-strecken-im-koordinatensystem, spiegelung, umkehrfunktion, vektoren-und-rechenoperationen
- **tangente-normale-schnittwinkel** (1): stammfunktion-und-hauptsatz
- **terme** (12): ableitungsregeln, extremalprobleme, funktionsscharen-und-ortskurven, gleichungen-loesen, integrationsregeln, lagebeziehungen, lineare-funktionen, lineare-gleichungssysteme, pyramide-kegel-kugel, quadratische-gleichungen, reelle-zahlen, vektoren-und-rechenoperationen
- **trigonometrie** (4): gleichungen-loesen, potenzen-wurzeln, skalarprodukt-und-winkel, tangente-normale-schnittwinkel
- **trigonometrische-funktionen** (3): funktionsklassen-und-eigenschaften, gleichungen-loesen, rekonstruktion-von-funktionsgleichungen
- **vektoren-und-rechenoperationen** (3): ebenen, flaecheninhalt-und-volumen-im-raum, spiegelung
- **wahrscheinlichkeit** (8): binomialverteilung, hypothesentests, kenngroessen-von-verteilungen, normalverteilung-und-sigma-regeln, unabhaengigkeit, vierfeldertafel, zufallsexperimente-und-pfadregeln, zufallsgroessen-und-verteilungen
- **winkel-dreiecke** (4): orthogonalitaet, punkte-und-strecken-im-koordinatensystem, skalarprodukt-und-winkel, trigonometrische-funktionen
- **zuordnungen** (7): ableitung-und-aenderungsrate, linearkombination-und-lineare-abhaengigkeit, prozentrechnung, rekonstruktion-von-bestaenden, trigonometrische-funktionen, vektoren-und-rechenoperationen, zinsrechnung

## 5 Formlücke
Einträge, deren Blatt-0-Abschnitt keinen Verweis auf einen anderen Katalogeintrag enthält – dieselbe Menge wie „Einträge ohne Verweis“ in den Messlücken von `_tragfaehigkeit.md` (Lesart des Vorbilds: Verweise auf Nicht-Katalogdateien und Selbstverweise zählen nicht). Je Eintrag die Zahl der Nennungen in Wortform (Heuristik „Thema “ vor einem Großbuchstaben; „Thema Terme (terme.md)“ ist ein Verweis und zählt nicht) und jede Zeile des Abschnitts, die eine trägt, als wörtliches Zitat mit Zeilennummer; steht eine Zeile für mehrere Nennungen, ist ihre Zahl vermerkt.

0 von 73 Einträgen. Wörtliche Lesart (überhaupt kein `<name>.md` im Abschnitt): dieselbe Menge.

## Schwäche der Messung
Die Prüfungen sehen Zeichenketten, keine Bedeutung. Prüfung 1 findet nur die Form `<name>.md`; ein Thema, das in Wortform genannt ist („Thema Lineare Gleichungen“), hat weder Ziel noch Fundort und fehlt in allen Gruppen – Prüfung 5 zeigt, wie viele Einträge so schreiben. Prüfung 2 ordnet nur zu, was unmittelbar hinter einem Verweis oder hinter der Klammer steht, die ihn einschließt; die Nennungen in Wortform tragen ihre Einheitsnummern ungeprüft, und eine Angabe, die einen Satz weiter steht, gilt als eigene Einheit, auch wenn die Zieldatei gemeint war. Umgekehrt kann eine Angabe hinter der schließenden Klammer die eigene Einheit des Eintrags meinen („(x.md), Einheit 5 ist Vorrat“) und wird trotzdem dem Verweis zugeordnet; und in der Klammerform „Thema A (a.md), B (b.md) Einheit 2“ gilt die Angabe dem letzten Verweis, obwohl die Reihung dieselbe Unklarheit trägt wie „a.md, b.md Einheit 2“ – nur die Reihung ohne Klammern wird als unklar gelistet. Die Zahl der Lerneinheiten ist die Zahl der nummerierten Zeilen, nicht die höchste Nummer; der Verweiseintrag hat null. Prüfung 3 vergleicht Namen wortgleich – eine abweichende H1 kann Absicht sein (Sammelthema, mehrere Prüfungsthemen), eine gleiche H1 sagt nichts über den Inhalt. Prüfung 4 zählt eine Erwähnung in jedem Abschnitt gleich, auch eine in der Prüfliste oder in einem offenen Punkt; ob die Gegenrichtung fachlich nötig ist, entscheidet sie nicht. Prüfung 5 zählt mit der Heuristik des Vorbilds; sie übersieht Nennungen ohne das Wort „Thema“, zählt das Wort auch, wo es keine Voraussetzung nennt, und sieht den Dateiverweis einer Nennung nur, wenn er dem Titel unmittelbar in der Klammer folgt. Alle fünf messen die Schreibform der Einträge, nicht den Unterricht.
