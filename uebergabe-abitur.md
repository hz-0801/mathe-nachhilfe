# Übergabe verbessereBlaetter – 2026-10-17 (für Chat „Abitur 3“)

Eigene Datei des Abitur-Chats (Bau: uebergabe.md; Durchsicht:
uebergabe-durchsicht.md). Nach plan.md Linie 8 kein eigener nächster
Schritt; Entscheidungen nur aus plan.md § 10.

## 1 Ziel

Originalprüfungen Abitur als Bücher in Drive (GK und LK fertig, FHR
offen) und der Wortlaut der Originale als Datenvorrat, damit der
Setzer später Abiturblätter (Original neu, Skript) ohne Modell setzt.

## 2 Arbeitsgrundlage

- plan.md § 7, Absatz „Daneben, eigener Chat Abitur“; § 10 16.10. q
  (Form der Bücher), 17.10. h (CAS-Vermerk), j (Zeitspannen), k
  (Namen), l, n (Wortlaut jetzt, Vorspann LK).
- Bücher: aufgabenbank-privat werkzeuge/abibuch.py, Schalter
  --kurs gk|lk (Anleitung „Neues Heft aufnehmen“ im Kopf). Drive
  Mathe/Bücher: „Originalprüfungen Abitur GK.pdf“ (112 S.) und
  „Originalprüfungen Abitur LK.pdf“ (91 S., 2026–2017 ohne
  2021–2019). Ablage über den Rechner: C:\Users\holge\Meine Ablage\
  Mathe\Bücher (device_commit_files), nie base64 durch den Chat.
- Wortlaut GK: aufgabenbank-privat abitur/gk-originale.jsonl (467
  Zeilen, alle zehn Hefte), Abschrift je Heft in abitur/abschrift/,
  Erzeuger werkzeuge/abi-originale.py (Modell schreibt nur stamm,
  aufgabe, grafik; `--pruef` prüft den Bestand).
- Hefte: Rechner C:\Users\holge\mathe\mathe-nachhilfe\hefte\abi
  (device_request_folder_access; Scans 2022–2025 einzeln stagen).
  Katalog: mathe-nachhilfe abitur/abi-katalog.csv; FHR: fhr/.

## 3 Arbeitsstand

- Erledigt 17.10. (Abitur 2): Wortlaut GK 2017–2025 (9 Hefte, 422
  Zeilen); heftnummer gefüllt, wo das Heft anders zählt (2022, 2024,
  2025); Zahlentabellen nur in grafik beschrieben; Ablesewerte aus
  Bildern mit „etwa“. abi-originale.py kennt jetzt alle Sonderzeichen
  der GK-Lösungen (′ ₁ φ ∥ ⁿ …).
- Erledigt 17.10. (Abitur 2): Buch LK in Drive; abibuch.py GK/LK.
- GK-Buch in Drive trägt noch „Berlin 2026 nicht erhältlich“
  (unbelegt); im Skript berichtigt, fällt beim nächsten GK-Bau weg.
- Wortlaut LK fehlt (wie GK machbar: 6 Hefte, 360 Zeilen).

## 4 Rahmen

- Woche 61 % am 17.10. ≈ 16:30 (mit Nebenchats), Fable 24 %. Reset
  Mo 18:00.
- Messwerte: Wortlaut je Heft Sonnet (Textebene) ≈ 0,12 Mio / 2–4
  min, Opus (Scan) ≈ 0,13–0,15 Mio / 6–8 min; 9 Hefte 1,29 Mio, 24
  min, 57 → 59 %. Buch LK Sonnet 0,16 Mio / 7 min, 59 → 61 %.
- Agenten, die Seiten rendern, schreiben in einen eigenen Ordner, nie
  nach /tmp (sonst sehen sie fremde Seiten; 2022 ein Lauf verloren).
  Je Agent eigener Klon; Abschriften in eigene Dateien, Zusammenführen
  am Ende mit dem Skript.
- Nicht anfassen: aufgabenbank-privat buecher/, buch-durchsuchbar.py,
  buchregister.py, buch-lesezeichen.py, pruefungsbuch.py (Chat Bau).
- Abiturblätter ruhen bis zum Gespräch über das Abitur.
- Vorspann/Verzeichnisse erst als Text abstimmen, dann einmal bauen.

## 5 Offene Punkte

- Lösungsteil der Abiturbücher: Form mit dem Lehrer besprechen
  (Katalog-Kurzlösung stellenweise holprig; IQB-Verweis bei
  Pool-Dubletten; CAS-Vermerk 17.10. h; Heftnummer statt
  Katalognummer).
- Gespräch über das Abitur (Form der Abiturblätter); dazu die vier
  ruhenden Fragen aus aufgabenbank bau/befunde-M5.md.
- Buch FHR: nach § 10 16.10. q „je Prüfung ein Buch (P10, Abitur GK,
  LK, FHR)“, noch nicht gebaut; Hefte und Katalog in fhr/ prüfen.
- Wortlaut LK, falls die Abiturblätter LK umfassen.
- 2024 GK 2.2 h verweist im Heft auf „Aufgabe f“, gemeint wohl g
  (Druckfehler, im Wortlaut belassen).
- Verworfen: Register nach Typen (341 Typen, 281 nur einmal);
  Anleitungsseite im Buch.

## 6 Nächster Arbeitsschritt

plan.md § 7, Absatz „Daneben, eigener Chat Abitur“.
