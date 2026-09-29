# Übergabe verbessereBlaetter – 2026-09-29 früh (Chat vom 28.09. 22:44 bis 29.09. 05:10)

Vorherige Übergabe: archiv/uebergabe-2026-09-28b.md (Abend).

## 1 Ziel

Der bestmögliche Themenkatalog, die Aufgabenbank und die Prompts,
damit aus wenigen Wörtern druckfertige Blätter entstehen. Maßstab
ist ziel.md, Stand 28.09.; Leitbild: ein Blatt für alle Schüler,
aus der Bank zusammengesetzt, Chat als Schalter.

## 2 Arbeitsgrundlage

- mathe-nachhilfe: ziel.md (28.09., maßgeblich, unverändert);
  urteil-einbindung-2026-09-28.md (alle 73 Funde beurteilt und
  umgesetzt); bericht-katalog-nachzug.md (Lauf vom 28./29.09.,
  mit der Liste der 24 Einträge, die einen Bank-Auftrag brauchen);
  katalog/ auf f56cace; faellig.md (Bank-Posten in § 2).
- aufgabenbank auf 64d2c06: bank.md mit Pflichtformen P1–P8,
  Päckchen-Regel, Sek-II-Körper; bau/sprachlauf/regeln.md Nr. 1–13;
  bau/layout-befunde.md Nr. 1–59; auftrag-eintrag.md (Vorlage
  27b, noch ohne die neuen Regeln); bank/_strittig.md
  (ungesichtet, K7).
- anweisungen: projekt-verbessereBlaetter.md Stand 28c (Regelweg
  Unteragent), kandidaten.md Stand 28c.
- blattbau unverändert: unterrichtsblatt.md v4.4, pruefungsblatt.md
  v0.15 (1.1 Klassenarbeit noch nicht bereinigt).
- TER-S1, TER-S2 liegen weiter nur im alten Chat (Lehrer).

## 3 Arbeitsstand

Erledigt 28.09. abends bis 29.09. früh:
- 73 Funde der Einbindung beurteilt (61 A, 4 Ä, 6 N; acht offene
  Fälle vom Lehrer entschieden, alle wie vorgeschlagen).
- Katalog-Nachzug als Unteragent aus dem Chat gelaufen (Opus,
  372 368 Token, 43 Minuten, 96 Aufrufe): 13 Sprossen Sek I, 22
  Sprossen Sek II plus 2 Kontrollzeilen und eine Kastenform,
  2025-GYM-K5d Nebentyp, Regeldateien der Bank, README-Landkarte.
  Prüfskripte ohne neue Treffer.
- quer-Funde Sek I direkt umgesetzt (aufgabenbank f6420f0).
- faellig.md bereinigt: Katalogbefund 3–8 und der Katalogauftrag
  vom 26.09. waren seit dem 27.09. umgesetzt (72a01d3, ca7939b,
  6c51f79); die Posten trugen noch „Urteil im Chat“.

Nicht erledigt: Bank auffüllen (§ 6); Teil D/E der Urteile sind in
ziel.md, aber noch nicht im Schalter-Prompt (der ist nicht gebaut)
und nicht in pruefungsblatt.md 1.1; K2 (Abnahme Sprachregeln),
K3 (Sprachlauf Sek II – Regel 13 liegt jetzt vor), K5 („Term durch
Zahl teilen“ fehlt weiter in terme.md), K6 (Rezept S), K7.

## 4 Verbindliche Entscheidungen (28./29.09.)

Frühere Übergaben gelten weiter (archiv/).

- Regelweg: Aufträge, die nur Repo, Python und Paketquellen
  brauchen, startet der Chat selbst als Unteragenten (Opus) und
  der Agent committet und pusht; der Code-Tab nur für den Rechner
  (hefte/, PowerShell, MiKTeX) oder wenn der Lehrer zusehen will.
  Grund: beide zahlen vom Wochenkontingent; der Lehrer tippt nichts.
  Projektanweisung 28c, kandidaten.md 28c.
- Päckchen: fünf Grundfall-Zeilen mit festem Wert; die Fünf bleibt,
  steigt erst nach Befund am Blatt. Sek II: derselbe Körper mit
  festen Eckpunkten, je Variante ein Körper.
- Schrittnamen je Rechenzeile (regeln.md 12) nur für Neues und bei
  Berührung; kein Umschreiblauf über die Bank.
- Aussondern „kein Binom“ ist Vorstufenfrage, nicht Sprosse;
  Formelgestalt ist Lösungsform (layout 59), nicht Sprosse.
- Überschlag prozentrechnung: Sprosse (selbst überschlagen);
  fremde Überschläge beurteilen nur als fehler-Zeile (Form P1).
- Antwortgerüst Vorzeichen/Betrag/Ergebnis nur in den ersten zwei
  Varianten (rationale-zahlen e2/e3).
- Randmaximum (extremalprobleme) Vorrat. Tangente mit Lineal messen
  angenommen (Grafik in der Bank).
- Denkaufgabe (fehler/begruenden) je Fertigkeit, nicht am Blattende
  gesammelt (layout 58).
- Klassenarbeit ohne Ausblick: kein Auslöser im Schalter, bleibt
  Zuruf. Folgetermin-Zeile beim Fokus: nein (nichts hängt an Zeit).
- Prüfstein der Bank-Aufträge: terme (neue Sprossen, P1–P8 und
  Musterbeispiel in einem Lauf), Vorbehalt TER-S1/S2.

## 5 Offene Punkte

- Nummerierung mehrerer Vorstufen je Kette (acht Sek-II-Ketten
  haben jetzt zwei bis drei): bank.md kennt nur sprosse 0 =
  Vorstufe. Am Prüfstein terme klären (E4 hat zwei Vorstufen:
  „Faktor vorgegeben“ neu vor dem Grundfall), dann als Regel.
- Bankzeilen ohne Katalog-Wortlaut: binomische-formeln e3 (3 Zeilen
  „kein Binom erkennen und begründen“), brueche-dezimalzahlen e5
  („Nullen anhängen“ jetzt Sprosse statt Vorstufe) – in die
  Bank-Aufträge dieser Einträge.
- auftrag-eintrag.md (Vorlage 27b) kennt die neuen Regeln nicht
  (P1–P8, Päckchen, Schrittnamen, Antwortgerüst); vor dem Prüfstein
  auf bank.md 29.09. nachziehen.
- Abrechnung: Unteragent-Lauf 372 368 Token; Messwert der
  Nutzungsanzeige vom Lehrer noch nicht abgelesen. Geplante Aufgaben
  weiter unbelegt (Posten faellig.md).
- Prüfungshöhe gegen die Sprache der Originale (Posten faellig.md,
  Auslöser erste Blätter aus der Bank).
- Schalter-Prompt nicht gebaut; pruefungsblatt.md 1.1 nicht
  bereinigt; Vorlage: Zonen-Kopfzeile doppelt, Textfont-Zeichen.
- winkel-dreiecke.md Z. 125 (Umkehrung) ist offener Punkt, keine
  Kette; nichts eingefügt.

Verworfen: P9 (Aufgaben selbst bilden), P10 (Prüfen als
Pflichtelement); Hausaufgabenregel; Wachhalten; Länge 1–3
Fertigkeiten als Regel; DDR-OCR vor dem Einbinden (alle mit Grund
in urteil-einbindung-2026-09-28.md und archiv/uebergabe-2026-09-28b).

## 6 Nächster Arbeitsschritt

Modell: Opus 5.5 (Fable auf Wahl des Lehrers). Läufe als
Unteragent aus dem Chat (§ 4).

1. auftrag-eintrag.md auf bank.md 29.09. nachziehen (P1–P8,
   Päckchen, Schrittnamen, Antwortgerüst, Vorstufen-Nummerierung
   als offene Vorgabe „vorstufe 0, 0a … oder 0, 1“ – der Chat
   entscheidet vor dem Start); Mappe terme neu bauen
   (werkzeuge/mappe.py); Bank-Auftrag terme als Unteragent; Bericht
   auswerten, Vorstufen-Nummerierung als Regel in bank.md.
2. Dann die übrigen 23 Einträge parallel (Unteragenten, je Eintrag
   nur eigener Ordner), danach P1–P8 für alle 72 Einträge.
3. Erst dann der Schalter-Prompt nach ziel.md 28.09.;
   pruefungsblatt.md 1.1 im selben Zug.
