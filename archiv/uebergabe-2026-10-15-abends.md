# Übergabe verbessereBlaetter – 2026-10-15 abends (Chat „Bau“, Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-15-nachmittags.md. Nach
plan.md Linie 8 nennt diese Übergabe keinen eigenen nächsten
Schritt. Entscheidungen nur aus plan.md (§ 10, 15.10. i–m). Zwei
Chats nebeneinander: „Bau“ (dieser Nachfolger) und „Durchsicht P10“
(dessen Übergabe: uebergabe-durchsicht.md);
der Schritt steht in plan.md § 7 (Absatz „15.10. abends erledigt …
Jetzt Bau, zuerst“) und § 9 (Fahrplan Formelsammlungen).

## 1 Ziel

P10 fertig und verbessert, Abitur GK aus Daten; dazu die Tafelwerke
als ansprechende, durchsuchbare PDFs mit Sprungstellen – für den
Lehrer zum Arbeiten (vergessene Bücher) und für Claude als Anregung,
die Kästen einzeln für Blätter nutzbar.

## 2 Arbeitsgrundlage

- plan.md § 7 (Jetzt Bau), § 9 (Fahrplan Formelsammlungen), § 10
  (15.10. m Materialablage), § 8 (Messwerte).
- Tafelwerke: aufgabenbank-privat formelsammlung/duden-sek1.md
  (Abschrift Duden „Formeln und Werte“, S. 4–39 + Vorsatz) und
  regine-sek1.md (Paetec Sek I, das Tafelwerk der Regine-Hildebrandt-
  Schule – kein eigenes Buch „Hildebrandt“). Gesetzt: duden-sek1.pdf
  (65 S.), duden-sek1.json (265 Kästen), README.md. Werkzeuge:
  aufgabenbank-privat werkzeuge/formelsammlung-satz.py (xelatex,
  --kasten <id>), formelsammlung-pruef.py.
- Scans: Rechner des Lehrers `C:\Users\holge\OneDrive\Desktop\bücher
  scanns` (Zugriff in diesem Chat gewährt; neuer Chat fragt neu an):
  „duden 1.pdf“ (24 Fotos, Vorsatz–S. 21), „duden 2.pdf“ (20, S.
  24–43), „duden 3“ (Nachscan S. 22–23, laut Lehrer da; um 20:45
  noch nicht im Ordner – nachsehen), „werk 1, regine.pdf“ (Paetec,
  248 MB). Holen mit device_stage_files (≤ 400 MB, ohne Token).
- Drive: `C:\Users\holge\Meine Ablage\Mathe` (gespiegelt; Ordner
  Bücher, Prüfungen, Eingang, _material). Nur fertige Produkte;
  Regeln in anweisungen/wege.md „Ablage der Materialien“.
- Abitur GK: 33 Blätter, aufgabenbank bau/pruefung/2026-10-15/abitur/,
  neusatz-abi.py, mappe-abi.py, abi-zahlen-pruef.py; Befunde
  bau/befunde-M5.md (Runde 32 Blätter).

## 3 Arbeitsstand

- Erledigt 15.10. nachmittags/abends: Bau-Paket Abitur GK (alle 33
  Blätter aus Daten, Setzer v0.17, Kritiker, Mappe 246 S.),
  P10-Kleinkram, Duden neu gesetzt (Probe), Drive für Desktop
  eingerichtet.
- Offen beim Lehrer, zurückgestellt bis 16.10.: vier Punkte in
  befunde-M5.md (4 Seiten AA30/AA130, Stufe am Blattende in 7
  Blättern, Rechenraum, ’26 · A1.3). Am 16.10. erneut vorlegen,
  sofern der Lehrer nicht selbst darauf kommt.
- Muster für den Lehrer: AA50, AG40, AS80 (noch nicht angesehen).
- Keine Agenten laufen.

## 4 Rahmen und Messwerte

- Woche 41 % (Anzeige 15.10. ≈ 20:30), Fable 24 %, Reset Mo 18:00.
  Bau-Paket: Agenten 3,03 Mio, Anzeige 32 → 41 % (Schätzung 3,7;
  Chat Durchsicht lief parallel). Duden-Satz 0,25 Mio, 18 min.
- Lehrer: „geht mir zu schnell“ – je Nachricht ein Schritt, alles
  vor dem Start absprechen, Handgriffe einzeln mit „Holger:“.
- Drive-Zugang im Chat (Connector) überträgt Dateien als base64:
  1 MB ≈ 0,4 Mio Token – keine PDFs darüber.
- Scans sind iPhone-Fotos (schräg, farbig, Schatten): Figuren
  ausschneiden sähe nach Foto aus.
- Lehrer arbeitet in UTC+2.

## 5 Offen und Verworfenes

- Figuren Duden (140): Weg A ausschneiden oder B neu zeichnen – offen,
  Teil der Regeln für Buch-PDFs.
- Inhaltszeile Duden: „Duden S. n“ steht vor den Punkten statt
  dahinter – beim nächsten Satz richten.
- Übrige Scans (Klasse 10, Jesse 9, Stochastik Stark/Jung, AH 6,
  Z und G 7; „stochastik stark2.pdf“ 0 Byte, „10. 1“ ohne Endung)
  und Originalhefte am Stück mit Sprungmarken nach Drive
  Mathe/Prüfungen: vielleicht So 18.10., nur nach Absprache.
- Setzer p_ergebnis (nur letzte Gleichung als Kontrollwert): plan.md
  § 9.
- Verworfen: Materialien im Repo oder in OneDrive; Drive-Zugang im
  Chat für PDFs (Kosten).

## 6 Nächster Arbeitsschritt

plan.md § 7 (Absatz „Jetzt Bau, zuerst“) und § 9 (Fahrplan
Formelsammlungen).
