# Übergabe verbessereBlaetter – 2026-10-17 (für Chat „Abitur 2“)

Eigene Datei des Abitur-Chats (Bau: uebergabe.md; Durchsicht:
uebergabe-durchsicht.md). Nach plan.md Linie 8 kein eigener nächster
Schritt; Entscheidungen nur aus plan.md § 10.

## 1 Ziel

Originalprüfungen Abitur als Bücher in Drive (GK fertig, LK folgt)
und der Wortlaut der GK-Originale als Datenvorrat wie bei P10.

## 2 Arbeitsgrundlage

- plan.md § 7, Absatz „Daneben, eigener Chat Abitur“ mit Stand
  17.10.; Form: § 10 16.10. q und 17.10. l; Namen: 17.10. k;
  CAS-Vermerk: 17.10. h; Zeitspannen absteigend: 17.10. j.
- Buch: aufgabenbank-privat werkzeuge/abibuch.py (Anleitung „Neues
  Heft aufnehmen“ im Kopf); Drive Mathe/Bücher „Originalprüfungen
  Abitur GK.pdf“ (112 S., 12,6 MB).
- Wortlaut: aufgabenbank-privat abitur/gk-originale.jsonl (Format
  wie hauptteil-originale.jsonl, Feld heftnummer), Erzeuger
  werkzeuge/abi-originale.py (Modell schreibt nur stamm, aufgabe,
  grafik ab; Rest Skript).
- Hefte: Rechner des Lehrers C:\Users\holge\mathe\mathe-nachhilfe\
  hefte\abi (Zugriff per device_request_folder_access; Stage in
  kleinen Gruppen, die vier Scans 2022–2025 einzeln – sonst
  Zeitüberschreitung). Katalog: mathe-nachhilfe abitur/abi-katalog.csv.

## 3 Arbeitsstand

- Erledigt 17.10.: Buch GK (ohne Lösungen) mit Themenregister,
  Scans geradegerückt und zugeschnitten, in Drive.
- Erledigt 17.10.: Pilot Wortlaut 2026-bb-gk, 45 Zeilen, alle
  Prüfungen bestanden.
- Offen, Go nicht gegeben: Wortlaut der übrigen 9 GK-Hefte. Vorschlag
  war: je Heft ein Agent, vier parallel, je in eigene Datei, am Ende
  zusammenführen; 2017–2021 (Textebene, 49 S.) Sonnet ≈ 0,7 Mio,
  2022–2025 (Scans, 44 S.) Opus ≈ 1,0 Mio; zusammen 2–3 Punkte,
  ≈ 40 min.
- Danach (Lehrer „ja“ 17.10.): Buch LK gleich gebaut – bb-ea 2017/
  2018, bebb-lk 2022–2025, bb-ea 2026; 2019–2021 fehlt; abibuch.py
  auf GK/LK umschaltbar; Sonnet-Agent ≈ 0,15 Mio; Vorspann vorher als
  Textentwurf abstimmen.

## 4 Rahmen

- Woche 57 % am 17.10. nach dem Zuschnitt (mit Nebenchats); Pilot
  danach 0,15 Mio. Reset Mo 18:00.
- Messwerte: Buch GK 0,18 Mio/15 min; Zuschnitt+Register 0,24 Mio/
  18 min; Pilot Wortlaut 0,15 Mio/6 min (Schätzung 0,1).
- Nicht anfassen: aufgabenbank-privat buecher/, buch-durchsuchbar.py,
  buchregister.py, buch-lesezeichen.py, pruefungsbuch.py (Chat Bau).
- Abiturblätter ruhen bis zum Gespräch über das Abitur.
- Sparsamkeit (gelernt 17.10.): Vorspann/Verzeichnisse erst als
  Text abstimmen, dann einmal bauen und zeigen; nicht je Wunsch neu
  bauen und als Bild ansehen.
- Wochenstand selbst lesen: nur, wenn der Lehrer sich im Browser der
  Claude-App bei claude.ai anmeldet (17.10. nicht angemeldet).

## 5 Offene Punkte

- Lösungsteil: Form mit dem Lehrer besprechen (Katalog-Kurzlösung
  ist stellenweise holprig, z. B. „∫ von 0 bis 1“; IQB-Verweis bei
  Pool-Dubletten; CAS-Vermerk 17.10. h).
- Katalognummern weichen vom Heft ab (Teil-A-Wahl 1.4–1.9 statt
  1.4.1–1.5.3; Aufgabenteil 2 als f–i): Register/Lösungen sollen die
  Heftnummer zeigen (Feld heftnummer im Wortlaut).
- 2025 S. 6 (Buchseite 19): Rest der Nachbarspalte rechts, Strich
  unten – Lehrer noch nicht geäußert.
- Verworfen: Register nach Typen (341 Typen, 281 nur einmal);
  Anleitungsseite im Buch.

## 6 Nächster Arbeitsschritt

plan.md § 7, Absatz „Daneben, eigener Chat Abitur“.
