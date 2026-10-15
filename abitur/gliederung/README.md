# Prüfungsgliederung Abitur GK

Je Kapitel eine Datei, Format wie `msa/gliederung/README.md` (Prüfung: abitur; keine Tabelle
„Plätze der Originale“, Originale ergeben sich aus den Zuschnitt-Zeilen). Erzeugt daraus:
`abitur/zuordnung-<kapitel>.csv` (`werkzeuge/zuordnung.py`) und
`abitur/skript-zuschnitt-abi-gk.csv` (`werkzeuge/gliederung-sichten.py`).

Einheiten (Blätter) seit 15.10.2026 (Befund `abitur/befund-zuschnitt-abi-gk-2026-10-15.md`): Kopffelder wie P10 –
`Anzeigenamen`, `Kennung` (AA10 … Analysis, AG10 … Geometrie, AS10 … Stochastik; Platz = Lernfolge über
Kapitelgrenzen), `Ordner`, `Kurzwort` (ana | geo | stoch) – und zusätzlich `Stufen: <Einheit> = a · b · c`
(Stufen des Blatts in Lernfolge). Anders als P10: Stufe = Zuschnitt-Zeile (Unterpunkt), nicht der Block `###`;
ein Block (Handgriffgruppe mit Kern und Bank) gehört mit `**Zuschnitt:**` zu genau einer Einheit, mehrere Blöcke
können zu einer Einheit gehören, Zeilen gleichen Namens bilden zusammen eine Stufe. Hinter der Zeile steht in
`‹…›` die frühere feinere Zeile (Erscheinungsform), nur für Menschen; `werkzeuge/gliederung.py` liest sie nicht.
Punkte (fünf letzte Jahre, plan.md § 10, 15.10. i): Jahre der Teilaufgaben der Stufe (Hauptplatz und neben),
nur GK BB/BE (2022–2025 bebb-gk, 2026 bb-gk); Leser aufgabenbank `werkzeuge/p10einheiten.py`.

## Bestellung

Kopffelder für aufgabenbank `werkzeuge/bestellen.py`, Form wie `msa/gliederung/README.md`
„Bestellung“ (15.10.2026). Blätter GK gibt es seit 15.10. (33, Setzer pruefheft.py v0.17, Mehr im Blattordner als
4-mehr/5-mehr-loesungen); Original neu und Hilfsmittelfrei-Zettel gibt es fürs Abitur noch nicht;
was fehlt, sagt die Zeile „Fehlt“. Pfade mit „mn “ liegen in mathe-nachhilfe.

- Anzeige: Abitur
- Sorte: A = GK | L = LK
- Schülerliste: Abitur
- Fehlt: Original neu und Hilfsmittelfrei-Zettel gibt es fürs Abitur noch nicht, LK-Blätter auch nicht; die Originale liegen beim Lehrer (hefte/abi/, abitur/abi-quellen.md § 8)
- Blatt: werkzeuge/pruefheft.py --pruefung abitur --kapitel {kapitel} --art p --einheit "{einheit}"
- Blattordner: bau/pruefung/{datum}/abitur/{ordner}
- Mehrdateien: 4-mehr.pdf | 5-mehr-loesungen.pdf
- Karte: bau/pruefung/{datum}/abitur/bestellkarte-abi-{kurs}.pdf
- Handreichung: bau/pruefung/{datum}/abitur/handreichung-abi-{kurs}.pdf
