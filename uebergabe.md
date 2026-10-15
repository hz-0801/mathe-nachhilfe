# Übergabe verbessereBlaetter – 2026-10-16 nachts (Chat „Bau“, Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-15-abends.md. Nach
plan.md Linie 8 nennt diese Übergabe keinen eigenen nächsten
Schritt. Entscheidungen nur aus plan.md (§ 10, 15.10. n, n2;
16.10. h). Zwei Chats nebeneinander: „Bau“ (dieser Nachfolger) und
„Durchsicht P10“ (eigene Übergabe uebergabe-durchsicht.md).

## 1 Ziel

P10 fertig und verbessert, Abitur GK aus Daten; dazu Bücher als
ansprechende, durchsuchbare PDFs mit Sprungmarken – für den Lehrer
zum Arbeiten (vergessene Bücher) und für Claude als Anregung.

## 2 Arbeitsgrundlage

- plan.md § 7 (Absatz „15./16.10. nachts erledigt … Jetzt Bau“),
  § 9 (Formelsammlungen, Schulbücher), § 10 (16.10. h), § 8.
- Tafelwerke: aufgabenbank-privat formelsammlung/ – duden-sek1.*,
  paetec-sek1.* (Abschrift .md, Daten .json, Buch .pdf), figuren/
  (Rahmen-CSV, Ausschnitte <kurz>-bild/, Umschlag), README.md mit
  „Regeln für ein Buch-PDF“. Werkzeuge: formelsammlung-satz.py
  (bricht ab, wenn ein Zeichen in der Schrift fehlt),
  formelsammlung-pruef.py (Ziel 0 Meldungen), figuren-ausschnitt.py.
- Schulbücher: werkzeuge/buch-durchsuchbar.py (Fotos → gerade,
  helle Einzelseiten, ohne Modell), buch-sprungmarken.py (Inhalt,
  Lesezeichen, „← zurück“), Lauf buch-durchsuchbar-jesse.sh.
- Scans: Rechner des Lehrers `C:\Users\holge\OneDrive\Desktop\bücher
  scanns` (Zugriff je Chat neu anfragen); holen mit
  device_stage_files (≤ 500 MB je Aufruf, große einzeln).
- Drive: `C:\Users\holge\Meine Ablage\Mathe\Bücher`; Regeln
  anweisungen/wege.md „Ablage der Materialien“.

## 3 Arbeitsstand

- Erledigt: Duden (60 S.) und Paetec (61 S.) gesetzt, Figuren als
  Ausschnitt aus dem entzerrten Original, Titelbild, kurze Namen,
  33 fehlende Zeichen (⊆ ∪ ∩ ∅ …) behoben, „← zurück“. In Drive
  liegen beide noch ohne „← zurück“ (vor der Regel abgelegt).
- Jesse = Cornelsen „Fundamente der Mathematik 10, Gymnasium“
  (Dateien heißen „jesse 9“, Umschlag sagt 10): 256 S., 80 MB,
  durchsuchbar, Inhalt klickbar (61 Verweise), 14 Lesezeichen,
  „← zurück“ – dem Lehrer zum Begutachten geschickt, nicht in Drive.
  Das PDF lag nur im Container dieses Chats; neu erzeugen mit
  werkzeuge/buch-durchsuchbar-jesse.sh (≈ 15 min, ohne Modell,
  braucht tesseract-ocr-deu, ocrmypdf, img2pdf, reportlab).
- Offen beim Lehrer: Begutachtung der drei Buch-PDFs; die vier
  Fragen aus aufgabenbank bau/befunde-M5.md (am 16.10. vorlegen).
- Keine Agenten laufen.

## 4 Rahmen und Messwerte

- Woche 43 % (Anzeige vor Paetec S. 28–43), Fable 24 %, Reset Mo
  18:00. Agenten dieses Chats: Probe S. 19 0,16 Mio; Duden
  Ausschnitte 0,25; Paetec + Titelbild 0,27; Paetec S. 28–43 0,20
  (alle Opus, je unter oder an der Schätzung). Schulbuch per
  Skript: fast kein Token.
- Lehrer: „geht mir zu schnell“, „bevormunde ich nicht“ – keine
  Uhrzeit-Vorgaben für ihn; teure Wege nicht ohne günstigere
  Alternative vorschlagen.
- Duden und Paetec sind beide Duden-Verlag; „Duden“ allein trennt
  nicht (Lehrer 15.10., § 10 t).
- Lehrer arbeitet in UTC+2.

## 5 Offen und Verworfenes

- Paetec S. 2–4 (Abkürzungen, Symbole): vorerst verzichtet.
- Schwache Ausschnitte: Paetec S. 24 (Kritzelei), S. 33/34/36
  (Fotorand); Duden S. 24 (Formelreste), S. 5 (blass).
- Übrige Scans (Klasse 10, Stochastik Stark/Jung, AH 6, Z und G 7;
  „stochastik stark2.pdf“ 0 Byte, „10. 1“ ohne Endung): per Skript
  wie Jesse, nur nach Absprache.
- Feld „Regine: S. n“ in den P10-Gliederungen → „Paetec“ (§ 9).
- Verworfen: Figuren der Tafelwerke neu zeichnen (zu teuer; nur
  auf Bestellung eines Blatts), ganze Scanseite ins PDF.

## 6 Nächster Arbeitsschritt

plan.md § 7 (Absatz „15./16.10. nachts erledigt … Jetzt Bau“).
