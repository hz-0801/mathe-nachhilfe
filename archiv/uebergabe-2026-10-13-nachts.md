# Übergabe verbessereBlaetter – 2026-10-13 nachts (Chat „start 30“, Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-13-spaet.md. Nach
plan.md Linie 8 nennt diese Übergabe keinen eigenen nächsten
Schritt. Entscheidungen nur aus plan.md (§ 7 A, § 10 13.10. (e)).

## 1 Ziel

P10 fertig: Der Lehrer bestellt mit wenigen Wörtern und bekommt
schnell gute Blätter aus Daten, ohne Modell beim Setzen (plan.md
§ 1). Jetzt: die Regeln aus der Durchsicht per Agentenrunde auf die
übrigen neun Blätter bringen.

## 2 Arbeitsgrundlage

- plan.md § 7 Schritt A (Absatz „13.10. spät … Weg B“), § 10
  Eintrag 13.10. (e).
- aufgabenbank bau/befunde-M3.md, Block „Durchsicht Blatt für
  Blatt (13.10. abends)“ samt den AZL2-/AZL3-Punkten am Ende: der
  Prüfmaßstab der Runde (Warum – Beispiel – Grenze).
- Muster der Daten: msa/gliederung/koerper.md (Stufen „Volumen
  direkt“, „rückwärts“, „Mantelfläche mit Kosten“, „vergleichen und
  urteilen“ mit Feld „Durchsicht 13.10.“) und flaechen.md.
- Blätter: aufgabenbank bau/pruefung/2026-10-13/<ordner>/ (neun
  offene: koerper-netz, lineare, parabel, qgleichung, grundwert,
  prozent, kenngroessen, diagramme, wahrscheinlichkeit).
- Setzer: `python3 werkzeuge/pruefheft.py --kapitel <k> --art p
  --einheit "<Zuschnitt>"` (aufgabenbank, ohne Modell, 2–3 min);
  Ausgabe bau/pruefheft/…, nach bau/pruefung/<datum>/<ordner>/
  kopieren, Ausgabeordner löschen; register.csv und fassungen.csv
  mitcommitten.

## 3 Arbeitsstand

- Flächen (Y5D4) und Körper Volumen durchgesehen. AZL3 liegt
  gesetzt; Daten danach noch einmal geändert (Anstöße für sich
  verständlich, Nr. 8 nur drei Fälle, ’23 · 5d aufs Blatt) – Neusatz
  offen, kommt mit der Runde.
- Gliederung Körper: Anzeigenamen Volumen gesucht · Formeln
  umstellen · Oberfläche gesucht · vergleichen und urteilen;
  Restvolumen keine Stufe mehr (’24 · 4c bei Volumen direkt, auch in
  zuordnung-koerper.csv, handgriffe-p10.csv, mehr-p10/koerper.csv).
  Interne Stufennamen unverändert.
- Setzer: „Seite ___“ bleibt zusammen (Handwerk, sofort).
- Flächen: Satz „Derselbe Handgriff an einer anderen Formel“
  gestrichen (Neusatz in der Runde).
- Keine Agenten laufen.

## 4 Rahmen

- Woche 22 %, Fable 24 % (letzte Messung 13.10. nachmittags); in
  diesem Chat nur Skripte, nicht neu gemessen. Reset Montag 18:00.
  Vor der Runde Nutzungsanzeige erfragen.
- Schätzung für die Runde (im Chat genannt): fünf Kapitel-Agenten
  Opus medium + Kritiker Opus high ≈ 3–4 Wochenpunkte, Wanduhr
  ≈ 80 min; Grundlage plan.md § 8 Runde 7/8 (≈ 0,5 je Kapitel).
- Kritiker meldet Heranführungen, die er nach den neuen Regeln
  streichen würde, statt sie zu streichen – der Lehrer sieht am
  Muster, ob die Regel trägt (Regeln stützen sich auf zwei Blätter).
- Lehrer sieht danach ein Blatt als Muster und die Stichprobe.
- Uhrzeit: Lehrer arbeitet in UTC+2.

## 5 Offen und Verworfenes

- Seite 3 nur Fundstellen-Tabelle (AZL3, Probe: ohne Tabelle 2
  Seiten) – Setzer in Schritt C für alle Blätter.
- handgriffe-p10.csv weicht schon vor diesem Chat von den
  Gliederungen ab (gliederung-sichten.py --pruefe meldet Prozent,
  Daten); zuordnung.py ordnet Stufen anders als die gespeicherte
  zuordnung-koerper.csv – nicht blind neu erzeugen.
- Fläche/Umfang trennen und Linie Länge: weiter offen (plan.md § 7).
- Verworfen: Blatt für Blatt durch alle elf (zu langsam, dieselben
  Fehler je Blatt; Lehrer 13.10. spät).

## 6 Nächster Arbeitsschritt

plan.md § 7 Schritt A (Weg B, Absatz 13.10. spät).
