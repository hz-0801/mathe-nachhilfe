# Übergabe verbessereBlaetter – 2026-10-13 abends (Chat „start 28“, Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-13.md. Nach plan.md
Linie 8 nennt diese Übergabe keinen eigenen nächsten Schritt.
Entscheidungen nur aus plan.md (§ 3, § 7, § 8, § 10, § 11).

## 1 Ziel

P10 fertig: Der Lehrer bestellt mit wenigen Wörtern und bekommt
schnell gute Blätter aus Daten, ohne Modell beim Setzen (plan.md § 1).
Jetzt erst ein Ergebnis über alle Einheiten, Verbesserungen gesammelt.

## 2 Arbeitsgrundlage

- plan.md – § 7 „Ab 13.10. abends“ Schritte A–C; § 8 Messwerte
  Runde 6–8 und Schätzregel; § 10 Einträge 13.10., (b), (c).
- pruefung.md § 5 – neu 13.10.: Häufigkeit als Urteil, Gemischt als
  letzter Abschnitt (Weg C), Fenster verrät die Lösung nicht, Marke
  wie im Heft mit „Basis“ rechts, TR-Zeichen.
- msa/mehr-p10/<kapitel>.csv (geteilt, ersetzt mehr-p10.csv),
  msa/gliederung/*.md, msa/zuordnung-*.csv.
- aufgabenbank werkzeuge/pruefheft.py v0.11, pruefheft-p.md;
  Blätter bau/pruefung/2026-10-13/ (9 Ordner, je bericht.md).
- anweisungen: projekt-verbessereBlaetter.md (13.10.: Dauer mit
  Uhrzeit), kandidaten.md Block 2026-10-13.

## 3 Arbeitsstand

- Aus Daten gesetzt (Kennung, Seiten): TAL3 Lineare 6, XU62 Parabel
  4, YYZ1 Quadratische Gleichung 3, Y5D3 Flächen 3, HK31 Grundwert 1,
  5ZQ1 Prozent 3 (Muster an den Lehrer), VRK1 Wahrscheinlichkeit 4,
  K9X1 Kenngrößen 3, DGH1 Kreis- und Säulendiagramme 3; Körper
  (Netz, Volumen) vom 12.10. mit älterem Setzer.
- Offen: Gleichungssysteme, Wachstum, Dreiecke (5 von Hand gesetzt,
  nicht in Datenform; 10 Zuschnitte), Übersicht/Bestellkarte.
- Keine Agenten laufen. Klone k6*–k8* in /home/claude sind Wegwerf.

## 4 Rahmen

- Woche 22 %, Fable 24 % (13.10. nachmittags); Reset Montag 18:00.
  Runde 6: 18 → 20 %, Runde 7/8: 20 → 22 %.
- Schätzregel: enger Kapitel-Agent, Opus medium ≈ 0,5 Wochenpunkte,
  25–80 min. Runde-5-Werte (high) überschätzen um das Vierfache.
- Kapitel-Agenten parallel nur mit eigenem Klon und eigenen Dateien
  (mehr-p10/<kapitel>.csv, gliederung/<kapitel>.md,
  zuordnung-<kapitel>.csv); register.csv/fassungen.csv nicht
  committen.
- Jeder Vorschlag nennt Wanduhr und Rückkehr-Uhrzeit.

## 5 Offen und Verworfenes

- Linie Länge: Lehrer neigt zu Weg A (folgt dem Stoff), entscheidet
  erst mit allen Blättern; Teil 1/Teil 2 kann der Setzer jederzeit.
- Agentenfragen in den Berichten: Prozent Weg A/B (Grundwert eigenes
  Blatt), Wahrscheinlichkeit Weg A/B (ein oder zwei Blätter),
  Gemischt nur am Blatt einer Einheit (XU62 ohne Abschnitt).
- Setzer-Wünsche für die Sammlung (bau/befunde-M3.md eintragen):
  Lösung links fehlt bei Aussagen prüfen (5ZQ1 Nr. 9); „N₁(2,27|0)“
  statt „N₁(x₁|0) mit x₁ ≈ 2,27“; \kreisdiagramm Beschriftung kleiner
  Sektoren; Overfull-Meldungen; Häufigkeitswort je Einheit.
- Duden sparsam (§ 9, gesondert besprechen); TR nach Prüfungsjahr
  umgesetzt (--pruefungsjahr).
- Verworfen: Gemischt-Blatt je Ast (12.10., ersetzt durch Weg C);
  Zählregel immer/oft/selten; „ohne TR“ an jeder Basisaufgabe.

## 6 Nächster Arbeitsschritt

plan.md § 7 „Ab 13.10. abends“, Schritt A.
