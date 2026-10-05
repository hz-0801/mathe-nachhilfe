# Übernahme Vorrat Abitur GK in den Katalog – Standdatei

Auftrag: Übernahme der Beitabelle `abitur/vorrat-abi-gk-2022-2026.csv`
in `abitur/abi-katalog.csv` (Agent 05.10.2026, Fable 5.1). Teile:
1 Beitabelle übernehmen (neue Felder kurzloesung, neben), 2 leere Spalten
in iqb-katalog.csv, 3 Gegenprobe, 4 Beitabelle nach archiv/, 5 Vorrat
2017–2021 direkt in den Katalog. Ein Neustart macht beim ersten Teil
weiter, der unten nicht als „fertig“ steht.

## Stand

- Start: 2026-10-05T15:33Z
- Teil 1 fertig: Beitabelle über `abitur/vorrat-uebernahme.py` (v0.1) in abi-katalog.csv übernommen (246 Zeilen, Felder kurzloesung nach ergebnis und neben nach typ_neben; abi-bau.py v0.16 führt sie als ZUSATZFELDER, solange die Kopfzeile in katalog-prompt.md sie nicht hat); 69 Abweichungen zwischenergebnis, 11 abhaengig_von ergänzt, verfahren bei 230 Zeilen um Rechenschritte verlängert, 45 reine Begriffe weggefallen, 11 Vektor-Zweifelsfälle (als Punkt belassen); Korrekturen 2025-bebb-gk-B4c 0,0432 und 2026-bb-gk-B3c 7/13 in zwischenergebnis (ergebnis war richtig). Selbstprüfung abi-bau.py bestanden. 2026-10-05T15:37Z
