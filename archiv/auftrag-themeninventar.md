# Auftrag: Themeninventar der vier Prüfungskataloge

## Ausgangslage

Die vier Prüfungskataloge (msa, fhr, abi, iqb) benennen denselben Stoff
verschieden. Vor der Themenkonkordanz (`themen.csv`, Wurzel) braucht die
Werkstatt ein vollständiges, gezähltes Inventar aller Themennamen. Dieser
Auftrag baut nur das Inventar. Das Zusammenführen der Namen entscheidet der
Chat, nicht dieses Skript.

Gezählt wird aus den Katalogen, nicht aus den Typenlisten: `abitur/abitur-typen.csv`
ist für abi und iqb gemeinsam und trägt kein Profilfeld, die Kataloge dagegen
liegen je Profil getrennt vor.

Quellen (alle mit Trennzeichen `;`, Feldern in Anführungszeichen, Kopfzeile):

- msa: `msa/msa-katalog-basis.csv` und `msa/msa-katalog-kontext.csv` (zusammen ein Profil)
- fhr: `fhr/fhr-katalog.csv`
- abi: `abitur/abi-katalog.csv`
- iqb: `abitur/iqb-katalog.csv`

Alle fünf Dateien haben dieselben 37 Felder; gebraucht werden `leitidee`,
`thema`, `typ`.

## Schritte

1. Lege `werkzeuge/themen-inventar.py` an. Das Skript liest die fünf Dateien mit
   dem `csv`-Modul (`delimiter=';'`, Encoding utf-8), läuft aus der Repo-Wurzel
   (`python werkzeuge/themen-inventar.py`) und ändert keine Datei außer seiner
   eigenen Ausgabe.

2. Das Skript bildet je Profil (msa, fhr, abi, iqb) und je Paar
   (`leitidee`, `thema`):
   - Zahl der Katalogzeilen,
   - Zahl der verschiedenen Werte in `typ`,
   - die drei häufigsten `typ`-Werte als Anschauung.
   Leere `thema`-Werte werden nicht übersprungen, sondern als `(leer)` geführt.

3. Das Skript liest zusätzlich die Dateinamen in `katalog/`: alle `*.md` ohne
   führenden Unterstrich, Endung abgeschnitten. Das ist die Referenzliste der
   Sek-I-Themennamen.

4. Das Skript schreibt `werkzeuge/themen-inventar.md`, Abschnitte in dieser
   Reihenfolge:
   - **Kennzahlen**: je Profil Zeilen gesamt, Themen gesamt, Typen gesamt.
   - **Themen je Profil**: je Profil eine Tabelle, nach Leitidee und dann nach
     Zeilenzahl absteigend sortiert, Spalten: Leitidee, Thema, Zeilen, Typen,
     drei häufigste Typen.
   - **Namensgleiche Themen**: jeder Themenname, der in mehr als einem Profil
     wortgleich vorkommt, mit den Profilen.
   - **Sek-I-Referenz**: die Namen aus `katalog/`, und je Name, ob er wortgleich
     als Thema in einem Profil vorkommt.
   - **Befunde**: Themen, die in einer Typenliste (`msa/msa-typen.csv`,
     `fhr/fhr-typen.csv`, `abitur/abitur-typen.csv`) stehen, aber in keinem
     Katalog auftauchen, und umgekehrt.

5. Führe das Skript aus.

## Prüfungen

Nenne im Bericht die Zeilensummen je Profil und die Themenzahlen und stelle sie
diesen Werten aus der letzten Übergabe gegenüber: msa 393 Zeilen / 25 Themen,
fhr 253 / 28, abi 794 / 43, iqb 1443 / 47. Weicht etwas ab, berichte die
Abweichung und ändere nichts daran; das Inventar zählt, was in den Dateien
steht.

Prüfe außerdem: keine Katalogdatei und keine Typenliste wurde verändert
(`git status` zeigt nur `werkzeuge/themen-inventar.py`,
`werkzeuge/themen-inventar.md`, `README.md` und die Verschiebung des Auftrags).

## README

Trage in `README.md` unter `werkzeuge/` zwei Zeilen ein:
`themen-inventar.py`, `themen-inventar.md` – Themennamen aller vier
Prüfungskataloge gezählt; Vorstufe der Themenkonkordanz.

## Abschluss

Verschiebe diese Auftragsdatei nach `archiv/auftrag-themeninventar.md` und
committe alles in einem Commit.

## Regeln

- Ändere keine Katalog-, Typen- oder Profildatei.
- Lösche nichts; Verschieben statt Löschen.
- Erfinde keine Themennamen und normalisiere keine Schreibweisen; das Inventar
  gibt die Namen wortgleich wieder, samt Tippfehlern.
- Rate nicht bei Unklarheiten: brich ab und berichte.

## Bericht

Kurz, in diesen Punkten: Kennzahlen je Profil mit Abgleich gegen die Sollwerte
oben, Zahl der namensgleichen Themen, Zahl der Sek-I-Namen mit und ohne Treffer,
Auffälligkeiten aus dem Befunde-Abschnitt, geänderte Dateien. Die Tabellen
selbst nicht in den Bericht kopieren – der Chat liest
`werkzeuge/themen-inventar.md` nach dem Push per Raw-URL.

Letzte Zeile des Berichts: Push origin drücken
