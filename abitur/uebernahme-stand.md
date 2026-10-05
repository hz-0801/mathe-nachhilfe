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
- Teil 2 fertig: iqb-katalog.csv mit leeren Spalten kurzloesung und neben (vorrat-uebernahme.py --nur-spalten), iqb-bau.py v1.11; Selbstprüfung iqb-bau.py bestanden. 2026-10-05T15:37Z
- Teil 3 fertig: Gegenprobe – abi-katalog 887 Datenzeilen, iqb 1762; alle 246 ids vorhanden, kurzloesung 246 gefüllt, neben 211; 2025-bebb-gk-B4c „P(X = 90) ≈ 0,0432“ und 2026-bb-gk-B3c „t = 7/13“ stehen; werkzeuge/skript-zuschnitt.py abi-gk läuft fehlerfrei (246 Teilaufgaben, 7 Nebenplätze, 52 Abschnitte, Ausgaben unverändert); Stichprobe 2023-bebb-gk-B3d kurzloesung „Q(0,5 | 0,5 | 1,5)“, 2023-bebb-gk-B3e zwischenergebnis „cos α = 1/√3 ≈ 0,577“; die 641 Zeilen außerhalb der Beitabelle nur um die zwei leeren Felder erweitert (Diff gegen HEAD geprüft). 2026-10-05T15:37Z
- Teil 4 fertig: Beitabelle nach archiv/vorrat-abi-gk-2022-2026-2026-10-05.csv (git mv), Verweise in abitur/vorrat-abi-gk-stand.md angepasst; Verweise außerhalb des Schreibbereichs (README.md, faellig.md, uebergabe.md, werkzeuge/vorrat-sympy-abi-gk.py Docstring) bleiben für den Chat. 2026-10-05T15:37Z
