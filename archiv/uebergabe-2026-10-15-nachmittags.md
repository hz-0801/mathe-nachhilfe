# Übergabe verbessereBlaetter – 2026-10-15 nachmittags (Chat „start 33“, Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-14-vormittags.md. Nach
plan.md Linie 8 nennt diese Übergabe keinen eigenen nächsten
Schritt. Entscheidungen nur aus plan.md (§ 10, 14.10. f–h, 15.10.
i–k). Ab jetzt zwei Chats nebeneinander: „Bau“ und „Durchsicht
P10“; der Schritt jedes Chats steht in plan.md § 7 (Absatz „15.10.
nachmittags erledigt … Jetzt“). Ein neuer Chat sagt im ersten Satz,
welcher der beiden er ist (der Lehrer nennt es im Startwort, sonst
fragen).

## 1 Ziel

P10 fertig und verbessert, Abitur GK als Vorrat aus Daten; der
Lehrer bestellt im Projekt erzeugeBlatt(Bank) mit „Name · Was ·
Zusatz“ (plan.md § 10, 15.10. k) und bekommt die PDFs in Sekunden.

## 2 Arbeitsgrundlage

- plan.md § 7 (Absatz 15.10. nachmittags), § 10 (14.10. f – 15.10.
  k), § 8 (Messwerte).
- Bestellung: aufgabenbank werkzeuge/bestellen.py (Logik aus Daten;
  Test werkzeuge/bestellen-test.py, 46 Fälle), blattbau
  bankblatt.md v6 (vom Lehrer im Projekt eingesetzt 15.10.).
- P10: mathe-nachhilfe msa/gliederung/*.md (Kopffelder Kennung,
  Ordner, Anzeigenamen, Kurzwort), msa/mehr-p10/*.csv (Spalte grafik
  mit Skizzen), msa/handgriffe-p10.csv. 22 Blätter in vier Gebieten
  (neu PZ10–PZ30 Zahlen und Terme).
- Abitur GK: abitur/gliederung/*.md (33 Blätter, Kennung AA/AG/AS),
  abitur/befund-zuschnitt-abi-gk-2026-10-15.md, abitur/mehr-abi-gk/
  kurvenuntersuchung.csv (Pilot AA20); aufgabenbank bau/befunde-M5.md.
- Setzer: aufgabenbank werkzeuge/pruefheft.py v0.16 (P10 und
  Abitur, Mehr mit Skizzen), p10punkte.py (Punkte je Handgriff),
  originalneu.py v0.3 (Figuren privat bau/original-neu/grafik/),
  mappe-p10.py, bestellkarte.py (Prüfung als Argument),
  neusatz-p10.py. Neusatz: `cd aufgabenbank && python3
  werkzeuge/neusatz-p10.py --datum <JJJJ-MM-TT> --mappe` (≈ 14 min,
  länger als 10 min: im Hintergrund starten und abwarten).
- Ausgaben 15.10.: aufgabenbank bau/pruefung/2026-10-15/ (Blätter,
  Karte, Handreichung, Gesamtheft, mappe-p10-ohne.pdf, abitur/);
  privat bau/mappe/2026-10-15/mappe-p10.pdf (372 S.).
- Durchsicht: aufgabenbank bau/befunde-M3.md, Blöcke „Durchsicht
  Mappe P10“ und „Kommentare in der Mappe“ (47 Kommentare wörtlich,
  mit Seite und Kennung; die Seiten beziehen sich auf die Mappe vom
  15.10. mittags, 334 S., vor Zahlen und Terme). Weitere
  Kommentar-PDFs: Kommentare per pypdf (/Annots, /Contents) lesen.

## 3 Arbeitsstand

- Erledigt 14./15.10.: Kennung PG50-3, Punkte je Handgriff,
  Skizzen im Mehr, Mappe mit Inhalt, Handreichung, festen
  Sprungzielen und Abschnittslinks; Bestellung Weg C (M4 technisch);
  Lernblatt-Bestellung; Zahlen und Terme; Original neu mit Figuren;
  Abitur-Zuschnitt, Karte, Setzer, Pilot.
- Offen M4: drei echte Bestellungen des Lehrers.
- Go für das Bau-Paket (bis Woche 50 %) ist noch nicht gegeben;
  zuletzt sagte der Lehrer zweimal „gleich“ – das zählt nicht als Go.
- Keine Agenten laufen.

## 4 Rahmen und Messwerte

- Woche 32 % (Anzeige 15.10. nachmittags), Fable 24 %, Reset
  Montag 18:00. Regel ≈ 0,9 Mio Opus-Token je Punkt hält; enger
  Daten-Agent ≈ 0,2 Mio, Bau-/Setzer-Agent ≈ 0,3–0,35 Mio.
- Lehrer: „zu viele Infos und Fragen auf einmal“ – Antworten kurz,
  eine Frage, Vorschläge als Paket mit Grenze statt Go je Runde
  (plan.md § 7). Warten kostet mehr als späteres Umwerfen: Form
  liegt in Daten, Neusatz per Skript.
- Lehrer arbeitet in UTC+2; Uhrzeiten in seiner Zeit nennen.
- Kommentare des Lehrers kommen künftig als kommentiertes PDF
  (Acrobat Reader/Edge); auslesen, wörtlich ablegen, im Chat
  Durchsicht beantworten.

## 5 Offen und Verworfenes

- Offen (Lehrer), von Claude vorläufig entschieden: plan.md § 7
  (Abitur Du-Form, bis 3 Seiten, PO24-1, Zuschnitt 33).
- Bauauftrag für den Bestell-Chat: sechs Lücken (welche Einheit
  bei bloßem Thema, ohne Kritiker liefern?, zweite Klasse derselben
  Einheit, Blocktitel, Bauordner, duplikate.py) – Chat Durchsicht.
- Aus Prozent/Lineare offen wie zuvor: Folge Gerade und Parabel,
  Prozent vor Grundwert, Stufenfolge Volumen.
- Verworfen: Bestellbaum mit Knöpfen (15.10. k); Mappe bei jeder
  Bestellung mitliefern (zu groß fürs Handy).

## 6 Nächster Arbeitsschritt

plan.md § 7 (Absatz „15.10. nachmittags erledigt … Jetzt“), je nach
Chat Bau oder Durchsicht P10.
