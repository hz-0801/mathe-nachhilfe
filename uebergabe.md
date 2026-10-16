# Übergabe verbessereBlaetter – 2026-10-16 (Chat „Bau“, Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-16-nachts.md. Nach
plan.md Linie 8 kein eigener nächster Schritt. Entscheidungen nur
aus plan.md (§ 10, 16.10. h und m). Daneben läuft der Chat
„Durchsicht P10“ (uebergabe-durchsicht.md); dort entstehen auch die
Lösungsblätter, die dieses Buch übernimmt.

## 1 Ziel

P10 fertig und verbessert, Abitur GK aus Daten; dazu Bücher als
übersichtliche, durchsuchbare PDFs mit Sprungmarken – Tafelwerke,
Originalprüfungen je Prüfung, später ein Buch der Lernblätter.

## 2 Arbeitsgrundlage

- plan.md § 7 (Absatz „16.10. erledigt (Chat Bau) … Jetzt Bau“),
  § 9 (Buch P10, Formelsammlungen, Schulbücher), § 10 (16.10. h, m).
- Buch P10: aufgabenbank-privat werkzeuge/pruefungsbuch.py; Aufruf
  aus aufgabenbank-privat: `python3 werkzeuge/pruefungsbuch.py
  --katalog ../mathe-nachhilfe/msa --hefte hefte --aus "<pfad>/P10
  Originalprüfungen.pdf"` (1 min, ohne Modell; braucht reportlab,
  pypdf, poppler, DejaVu-Schrift). Daten: msa-katalog-basis/-kontext
  .csv (Feld seite, leitidee, kurzloesung), Hefte aufgabenbank-privat
  hefte/.
- Tafelwerke: aufgabenbank-privat formelsammlung/ (README „Regeln
  für ein Buch-PDF“), in Drive Mathe/Bücher.
- Schulbücher: werkzeuge/buch-durchsuchbar.py, buch-sprungmarken.py.
- Drive: `C:\Users\holge\Meine Ablage\Mathe\Bücher`; Scans
  `C:\Users\holge\OneDrive\Desktop\bücher scanns` (Zugriff je Chat
  neu anfragen). Ablage erst nach Begutachtung (anweisungen/wege.md).

## 3 Arbeitsstand

- Erledigt 16.10.: Tafelwerke in Drive (Kopfzeile, „← zurück“);
  Buch P10 Originalprüfungen, 184 S., vom Lehrer durchgesehen (acht
  Runden), Form § 10 (16.10. m): Titelseite in Stichpunkten mit
  Kasten „Prüfung 2027“ und Quelle (Link, QR); S. 2 Prüfungen und
  Lösungen; S. 3 Bereiche in festen Spalten mit Seitenbereichen;
  Steuerung als Knöpfe am rechten Rand mittig; jedes Lösungsheft auf
  eigener Seite. Lösungen vorerst Kurzlösungen aus dem Katalog.
- Formelblatt der P10 fehlt in unseren Heften – Lehrer legt es in
  „bücher scanns“, dann vorn ins Buch.
- Noch nicht in Drive: Buch P10 (wartet auf die Lösungsblätter).
- Lösungen: Katalog P10 in zwei Runden umgeschrieben (163 Zeilen),
  Lehrer noch unzufrieden – nächster Schritt ist der Auftrag in
  plan.md § 7 Punkt 1 (Satz mit mathblatt.sty, Prüfskript schärfen,
  Pilot 2026 FOR; Go erteilt).
- Stochastik: Dateinamen vertauscht – „stochastik stark 1/3/4“ =
  Daniel Jung (StudyHelp), „stochstik jung 1/2“ = Stark (March);
  Scans flach und gut, Weg per Skript empfohlen, Go offen;
  „stochastik stark2.pdf“ 0 Byte (Teil des Jung fehlt).
- Jesse (Cornelsen Fundamente 10): Fotos zu schwach; Lehrer
  überlegt neu scannen (Kopierer/einzeln); Notizen-App max. 24
  Seiten je Scan.
- Keine Agenten laufen.

## 4 Rahmen und Messwerte

- Woche 48 % (Anzeige 16.10. mittags), Reset Mo 18:00. Seit
  dem Umzug fast nur Skripte, keine Agenten.
- Lehrer will kurze, übersichtliche Verzeichnisse; denkt vom
  Gebrauch her (finden, drucken); Feineres gehört ins Buch der
  Lernblätter. Selbst mitdenken, nicht jede Einzelheit erfragen.
- Rechtlich (Claude, kein Jurist): Bildungsserver-Hefte für den
  eigenen Unterricht unbedenklich, nicht veröffentlichen;
  Stark-Hefte nur Auszüge (§ 60a UrhG).
- Lehrer arbeitet in UTC+2.

## 5 Offen und Verworfenes

- Lösungsblätter aus dem Nebenchat: je Heft eine PDF mit festem
  Namen, Lesezeichen je Aufgabe, jedes Heft auf neuer Seite (Lehrer
  gibt es dem Nebenchat mit).
- Verworfen: Originale zugeschnitten und doppelt nach Bereich
  (gehört ins Buch der Lernblätter); Inhalt „nach Abschluss“, „nach
  Teil“, feines Themenregister; Kennzeichen „OS“.

## 6 Nächster Arbeitsschritt

plan.md § 7 (Absatz „Jetzt Bau, in dieser Folge (Lehrer 16.10.)“).
