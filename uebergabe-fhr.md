# Übergabe verbessereBlaetter – 2026-10-17 (für Chat „FHR 2“)

Eigene Datei des FHR-Chats (Strom D, plan.md § 7). Nach plan.md
Linie 8 kein eigener nächster Schritt; Entscheidungen nur aus
plan.md § 10.

## 1 Ziel

Lösungen für die Sek II (FHR, Abitur GK/LK) in einer Form, die je
Aufgabenart immer gleich aussieht, dazu ein knappes Schema je Art für
die Schüler; zuerst Kurvendiskussion.

## 2 Arbeitsgrundlage

- plan.md § 7 Strom D (Jetzt) und § 10 17.10. o, s (Lösungen).
- mathe-nachhilfe fhr/loesung/: `schema-kurvendiskussion.tex/.pdf`
  (Entwurf 3), `probeB.tex/.pdf` (FHR 2026 C 1 als amtlicher
  Erwartungshorizont + drei Änderungen), `zuordnung-kurvendiskussion
  .csv` (449 Teilaufgaben: FHR 114 kern + 9 rand, Abitur 161 kern +
  165 rand).
- Buch: aufgabenbank-privat werkzeuge/fhrbuch.py; Drive Mathe/Bücher
  „Originalprüfungen FHR.pdf“ (134 S.).
- Hefte FHR: Bildungsserver, von hier per curl erreichbar (Liste in
  fhr/fhr-pruefungen.md). Abitur-Hefte (Verlagsdateien) nur auf dem
  Rechner: C:\Users\holge\mathe\mathe-nachhilfe\hefte\abi, Seiten
  2026-bb-gk: 2.2 S. 22, 3 S. 28, 4 S. 32/33.
- Satz: xelatex mit DejaVu Sans (kein lmodern, kein ulem im
  Container); pgfplots-\foreach in axis vermeiden.

## 3 Arbeitsstand

- Erledigt: Buch FHR in Drive (§ 10 17.10. o); Termin 2027 in
  fhr/fhr-vorgaben.md (Fr 21.05.2027, 9 Uhr).
- Lösungsform: Fassungen 1–4 (eigene Form) verworfen; Weg B
  (Erwartungshorizont + Werkzeug nach „|“, Bezeichner x_E/x_W/x_S,
  Zahlenstrahl) vom Lehrer „viel besser“.
- Schema Kurvendiskussion Entwurf 3 vom Lehrer gebilligt („so passt
  das“), mit Zahlenstrahl-Idee: Teilstriche mit x_E1, x_E2, x_S unter
  dem Wert (Vorschlag, noch nicht gesetzt).
- Wartet: Musterlösung des Lehrers zu FHR 2026 C 1 e).

## 4 Rahmen

- Woche ≥ 64 % am 17.10. ≈ 18 Uhr (Chat Stochastik 1), Reset Mo
  18:00. Messwerte: Buch FHR Sonnet 0,18 Mio, 6 min.
- Abitur-Verlagsseiten nie ins öffentliche Repo (Proben mit
  Abiturseiten nur im Scratchpad oder privat).
- Aus den Kommentaren (Tendenz, noch keine Regel): Kopf nur Kurzform
  ohne „ges./zz/Beh.“; „ges.: m, n in t(x) = mx + n“ und „zz: …“
  stehen im Weg; nichts doppelt; jede Folgerung ausdrücklich; Weg zur
  Faktorisierung zeigen (raten, Horner, Division); ⇒ bündig; keine
  Rechenschritte innerhalb eines Schritts.
- Nicht anfassen: abibuch.py, pruefungsbuch.py, buecher/ (Ströme A/B).

## 5 Offene Punkte

- FHR beim amtlichen Erwartungshorizont lassen (Vorschlag ja; kein
  Abschreiben der 78 Seiten).
- Pilot Lösungen Abitur GK 2026 mit Messung vor der Breite.
- Randthemen der Zuordnung (Scharen, Funktionsklassen, Änderungsrate,
  Gleichungen) je Teilaufgabe entscheiden.
- Weitere Schemata (Integral, Geraden/Ebenen, Binomial, Baum …),
  Liste der etwa 10–15 Aufgabenarten.
- Verworfen: Lösung „höchstens eine Zeile je BE“ (zu knapp);
  Ablaufpläne je Lerneinheit im Katalog (Lehrer: keine Lerneinheiten,
  Tafelwerk-Schema reicht).

## 6 Nächster Arbeitsschritt

plan.md § 7, Strom D „Jetzt“.
