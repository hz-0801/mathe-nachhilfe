# Prüfungsgliederung Abitur GK

Je Kapitel eine Datei, Format wie `msa/gliederung/README.md` (Prüfung: abitur; keine Tabelle
„Plätze der Originale“, Originale ergeben sich aus den Zuschnitt-Zeilen). Erzeugt daraus:
`abitur/zuordnung-<kapitel>.csv` (`werkzeuge/zuordnung.py`) und
`abitur/skript-zuschnitt-abi-gk.csv` (`werkzeuge/gliederung-sichten.py`).

## Bestellung

Kopffelder für aufgabenbank `werkzeuge/bestellen.py`, Form wie `msa/gliederung/README.md`
„Bestellung“ (15.10.2026). Blätter, Original neu und Basiszettel gibt es fürs Abitur noch nicht;
was fehlt, sagt die Zeile „Fehlt“. Pfade mit „mn “ liegen in mathe-nachhilfe.

- Anzeige: Abitur
- Sorte: A = GK | L = LK
- Schülerliste: Abitur
- Fehlt: Blätter und Original neu gibt es fürs Abitur noch nicht; die Originale liegen beim Lehrer (hefte/abi/, abitur/abi-quellen.md § 8)
- Handreichung: mn abitur/handreichung-abi-{kurs}-2027.pdf
