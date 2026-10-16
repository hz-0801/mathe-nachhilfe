# Übergabe verbessereBlaetter – 2026-10-16 (Chat „Bau 3“, Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-16-mittags.md. Nach
plan.md Linie 8 kein eigener nächster Schritt. Entscheidungen nur
aus plan.md (§ 10, 16.10. h, m, n). Daneben läuft der Chat
„Durchsicht P10“ (uebergabe-durchsicht.md).

## 1 Ziel

P10 fertig und verbessert, Abitur GK aus Daten; dazu Bücher als
übersichtliche, durchsuchbare PDFs mit Sprungmarken – Tafelwerke,
Originalprüfungen je Prüfung, später ein Buch der Lernblätter.

## 2 Arbeitsgrundlage

- plan.md § 7 „Jetzt Bau, in dieser Folge (Lehrer 16.10.)“, Punkt 1
  mit Stand [16.10. erledigt (Chat Bau 3) …]; § 10 (16.10. l, m, n).
- gemeinsam.md „Form der Lösung“ (seit 16.10. mit Namen am Wert).
- aufgabenbank werkzeuge/loesung-pruef.py: `--streng` (Buch der
  Originale) meldet links RECHNUNG, WEG, KLAMMER, URTEIL, RUNDUNG,
  WORT, ZB, NAME; rechts R-WEG, R-WORT, R-WERT, R-GLEICH;
  `--heft "2026 FOR"` prüft ein Heft. Ohne `--streng` unverändert.
- aufgabenbank-privat werkzeuge/pruefungsbuch.py: Lösungen mit
  xelatex und blattbau mathblatt.sty (lzaufg, \lzz), Sprung je Zeile
  per zref-savepos, setzt nicht bei fehlendem Zeichen oder
  Überbreite; `--nur "2026 FOR"` baut ein Probebuch. Aufruf aus
  aufgabenbank-privat: `python3 werkzeuge/pruefungsbuch.py --katalog
  ../mathe-nachhilfe/msa --hefte hefte --aus "<pfad>/P10
  Originalprüfungen.pdf"` (braucht blattbau daneben, xelatex mit
  zref, reportlab, pypdf, poppler).
- Muster: 2026 FOR im Katalog (msa/msa-katalog-basis.csv,
  -kontext.csv, Zeilen 2026-FOR-*), Lehrer „besser“.

## 3 Arbeitsstand

- Erledigt 16.10.: Pilot 2026 FOR (Satz, Prüfskript, 25 Zeilen
  Katalog in Form und mit Namen). Commits mathe-nachhilfe,
  aufgabenbank, aufgabenbank-privat.
- Offen: übrige 13 Hefte – `--streng` meldet 216 Zeilen (NAME 76,
  R-WORT 61, WORT 29, R-GLEICH 22, URTEIL 22, R-WERT 14, R-WEG 10,
  ZB 7, RUNDUNG 7). Weg A gewählt: der Chat korrigiert selbst.
  Ablauf und Schätzung in plan.md § 7.
- Buch P10 noch nicht in Drive (nach Neusatz und Blick des Lehrers).
- Keine Agenten laufen.

## 4 Rahmen und Messwerte

- Woche 48 % vor dem Pilot, 49 % nach Pilot und Umzug (16.10.
  mittags, Nebenchat lief); Fable 24 %; Reset Mo 18:00.
- Lehrer will tokensparend: schmale Listen aus Skripten statt
  Dateien lesen; Prüfung jeder Zeile, keine kleine Stichprobe.
- Lösungen „nicht immer knapp, aber so lassen“ (Lehrer 16.10.).
- Rechtlich (Claude, kein Jurist): Bildungsserver-Hefte für den
  eigenen Unterricht unbedenklich, nicht veröffentlichen.
- Lehrer arbeitet in UTC+2.

## 5 Offen und Verworfenes

- Ankreuzen mit Begründung (2026 FOR 7b „B; A beginnt bei 0 €, C
  linear“): stehen gelassen; gleiche Fälle so lassen.
- Verworfen: Sonnet-Agent mit Stichprobe von 20 Zeilen (Lehrer: zu
  wenig); Weg B' mit Opus-Kritiker über alle Zeilen (Lehrer wählte
  Weg A).
- Daneben offen aus plan.md § 7: Formelblatt ins Buch, die vier
  Fragen aus aufgabenbank bau/befunde-M5.md.

## 6 Nächster Arbeitsschritt

plan.md § 7 (Punkt 1, Stand „16.10. erledigt (Chat Bau 3)“).
