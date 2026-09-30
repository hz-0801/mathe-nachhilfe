# Übergabe verbessereBlaetter – 2026-09-30 nachts (Chat 29.09. 08:14 bis 30.09. 01:00)

Vorherige Übergabe: archiv/uebergabe-2026-09-29.md (früh).

## 1 Ziel

Der bestmögliche Themenkatalog, die Aufgabenbank und die Prompts,
damit aus wenigen Wörtern druckfertige Blätter entstehen. Maßstab
ist ziel.md (28.09.); Leitbild: ein Blatt für alle Schüler, aus der
Bank zusammengesetzt, Chat als Schalter.

## 2 Arbeitsgrundlage

- mathe-nachhilfe: ziel.md (28.09., unverändert); katalog/ auf
  f038ccb (sieben Änderungen vom 29.09., § 3); faellig.md (Posten
  aus dem Tag in § 2, Messwerte Kontingent); bericht-katalog-
  nachzug.md (Liste der 24 Einträge, alle erledigt).
- aufgabenbank auf 0f1ee71: bank.md 29b (fünfte Fassung:
  Vorstufen 0, −1, −2; eine Prüfungssprosse je Kette mit allen
  Originalen; Musterbeispiel muster.md; Körperregel beim Nachzug;
  Dublette = ein Original); auftrag-eintrag.md 29e; werkzeuge/
  bank-pruef.py v0.10 (`--katalog` aus der Mappe); werkzeuge/
  punkte-nachziehen.py (ids nach Nachzug); werkzeuge/einmalig/
  (Umbauskripte der Nachzüge); bank/<eintrag>/stand.md je Eintrag
  mit Entscheidungen und Befunden vom 29.09.
- anweisungen: projekt-verbessereBlaetter.md 28c, kandidaten.md
  28c (unverändert; neue Kandidaten unten in § 4).
- blattbau unverändert: unterrichtsblatt.md v4.4, pruefungsblatt.md
  v0.15.
- TER-S1, TER-S2 weiter nur im alten Chat (Lehrer).

## 3 Arbeitsstand

Erledigt 29.09.:
- Vorstufen-Lauf über die vorhandenen Schreibform-Notizen der
  DDR-Bücher (61 Notizen, Vier-Fragen-Prüfstein): sieben
  Katalogänderungen in fünf Einträgen – terme E4 Vorstufe
  „Zerlegen mit vorgegebenem Faktor“ (vor „Faktor vorgegeben“),
  prozentrechnung E4 Sprosse „nur ein Prozent bestimmen“,
  bruchrechnung E3 Sprosse „Stammbruch von einem Bruch“ (Vorrat)
  und Kastenzeile 3 · 2/5 = 3/1 · 2/5, tangente E1 Vorstufe „nur
  den Anstieg“, stammfunktion E2 „nur einsetzen“ als Vorstufe vor
  den Grundfall (d78032a, f038ccb).
- Prüfstein terme als Unteragent (217 495 Token), danach alle 23
  übrigen Einträge in vier Schüben (4, 6, 6, 7 Agenten parallel,
  Opus; 1,08 / 1,66 / 1,68 / 2,11 Mio Token). Alle 24 Einträge auf
  Katalog 29.09., bank.md 29b, Pflichtformen P1–P8, Päckchen,
  muster.md; Prüfskript `--katalog` überall 0/0. Bank: 73 Ordner,
  15 294 Zeilen.
- bank/_punkte.csv nach jedem Schub nachgezogen (ids umbenannt,
  neue Urteile durch kleine Opus-Agenten: 12, 62, 34); Gegenprobe
  bestanden.
- Regeln aus den Befunden der Schübe in bank.md, Vorlage und
  Prüfskript (§ 4).
- Kontingent gemessen (§ 4).

Nicht erledigt: Gegenlese der Nachzüge (Posten faellig.md);
Schalter-Prompt; pruefungsblatt.md 1.1; K2, K3, K5 (jetzt mit
Beleg), K6, K7; Katalogbefunde aus den stand.md-Dateien (unten).

## 4 Verbindliche Entscheidungen (29.09.)

Frühere Übergaben gelten weiter (archiv/).

- Vorstufen: die Vorstufe vor dem Grundfall ist Sprosse 0, weitere
  davor −1, −2 (id s-1); der Grundfall ist immer 1 (bank.md).
- Je Verfahrenskette genau eine Prüfungssprosse, die letzte, mit
  allen Originalen der Katalogzeile (je Original zwei Zeilen, ohne
  Original drei). Grund: das Blatt zieht „was die Prüfung fragt“.
- Musterbeispiel: bank/<eintrag>/muster.md, je Verfahrenskette ein
  Abschnitt (Annahme statt „einmal je Eintrag“ in ziel.md, weil
  jedes Blatt am Grundfall seiner Einheit beginnt); Form Schritt |
  Zeile, Bausteine setzt der Zusammenbau (layout 55).
- Sperre: Terme, Zahlenpaare, Gleichungen aus Kasten, Typischen
  Fehlern und Originalen; einzelne Kastenzahlen sind frei (sie sind
  der Stoff). Merkkasten bleibt „nur auf Zuruf“ (ziel.md).
- Nachzug eines bestehenden Ordners: Übernahme geht vor der
  Körperregel; Zeilen bleiben wortgleich, auch wenn der
  Sprossentext länger wurde, solange die Aufgabe dieselbe bleibt;
  Pflichtformen werden durch Umschreiben hergestellt, nicht
  ergänzt; Schrittnamen nur in neuen und umgeschriebenen Lösungen.
- Pooldublette zählt als ein Original (Kennung, die in der Mappe
  zuerst steht); gilt für Neues, der Bestand bleibt bis zur
  Gegenlese.
- Punkte: verlangt die Bankzeile mehr als das Original, ist sie
  „ganz“; nach jedem Nachzug punkte-nachziehen.py, dann Urteile.
- Prüfskript: pruef "" bei pflicht fehler erlaubt (P1-Serie);
  \janein-Lösung beginnt mit ja/nein; „Zeichne nichts“ ist kein
  Zeichenauftrag; \int, \sum, \lim und Co. erlaubt.
- Agentenläufe: je Eintrag ein eigener Klon (/tmp/bank-<eintrag>),
  Zwischendateien nie im geteilten Scratchpad; Umbauskripte nach
  werkzeuge/einmalig/; bis sieben Agenten parallel ohne
  Push-Konflikt (Messwert 29.09.).
- Kontingent (Messwerte Nutzungsanzeige, Woche seit Montag 18:00):
  8 % nach Katalog-Nachzug und terme, 12 % nach Schub 1, 18 % nach
  Schub 2, 28 % nach Schub 3, 39 % nach Schub 4 (Nebenchat lief
  mit). Rund 1–1,5 % je Bank-Eintrag, etwa 3,5–5 % je Million
  Token. Fable 21 % für diesen Chat. Die Hochrechnung der Anzeige
  („geht Freitag aus“) ist deren Schätzung aus dem Tagestempo.
- Seitenlauf über die DDR-Bände (jede Musterlösung eines Kapitels
  lesen) nur bei Blatt-Befund für einen Eintrag, nie über alle
  Bände (faellig.md).
- Kandidaten für kandidaten.md (beim nächsten Umzug eintragen, hier
  noch nicht geschrieben): (a) Hinweise im Kopf eines Agenten-
  Auftrags müssen aus der Quelle stammen, die der Agent selbst
  liest (Mappe), nicht aus einer Zählung des Chats – der Hinweis
  zu ebenen war falsch, der Agent hat richtig die Mappe genommen.
  (b) Parallele Agenten je in einem eigenen Klon, Zwischendateien
  nie im Scratchpad. (c) Musterlösungen alter Lehrwerke sind eine
  Quelle für Vorstufen: je Zeile der Lösung die vier Fragen (nicht
  Sprosse; als Aufgabe stellbar; eigenes Fehlerbild; Sturzstelle).

## 5 Offene Punkte

- Gegenlese aller 24 nachgezogenen Einträge (40–70 neue oder
  umgeschriebene Zeilen je Eintrag); die gegenlese.md/gegenlese2.md
  in den Ordnern zeigen auf alte ids. Dabei die Nachbesserungen aus
  den stand.md-Dateien: skalarprodukt e1 s1 v5 (Antwortfeld deckt
  die Beurteilung nicht), zufallsexperimente übernommene Zeilen mit
  „P = \leerfeld“ in antwort, binomische-formeln e1 Vorstufe ohne
  Baustein (Pfeile), Bestandszeilen mit Poolkennung (ebenen,
  lagebeziehungen, tangente).
- Katalogbefunde aus den stand.md-Dateien (für den nächsten
  Katalogauftrag): binomische-formeln Verweis auf quadratische-
  gleichungen Einheit 2/3; lineare-gleichungen Z. 32 „vor Einheit 1
  und 2“; Erkennungsschritt, der eine Vorstufe wiederholt – bank.md
  „derselbe Handgriff“ ist zu weich, drei Agenten haben nach
  Ermessen entschieden (vektoren, binomialverteilung, abstaende);
  flaecheninhalt neun Kennungen an Prüfungssprossen ohne Mappen-
  eintrag; funktionsklassen 30 CAS-Originale 2017/2018 an keiner
  Sprosse; stammfunktion e2-Vorstufe nennt 2025-bebb-lk-B2.2b, das
  an der Ableitungssprosse liegt; terme e1 ohne Begründen, e3 ohne
  Anwendung (Typenzeile).
- Prüfskript prüft die Pflichtformen P1–P8 nicht (alle Agenten):
  Formprobe je Einheit (drei verschiedene fehler-, drei begruenden-
  Formen) als v0.11, sobald die Gegenlese die Formen bestätigt hat.
- Sperre trifft in der Raumgeometrie jede Körperecke einzeln gegen
  alle Tripel der Mappe (abstaende, skalarprodukt, geraden, ebenen):
  Körper mit kleinen Zahlen sind schwer zu finden; Regel prüfen, ob
  Tripel nur als Körper (drei Ecken zusammen) gesperrt werden.
- Prüfskript erkennt Punkte in der Originalschreibweise „(4; 1)“
  nicht (tangente); Winkel „rund …°“ nicht als Ergebnisstelle.
- Urteilsbalance Ja/Nein: P6 fällt fast immer Nein, P2 immer
  „Richtig“ – die Regel „etwa halb“ ist je Einheit nicht haltbar;
  entweder je Eintrag zählen oder streichen.
- blattbau: Bausteine „Figur aus zwei Rechtecken“ (terme) und
  „Pfeile jedes mit jedem“ (binomische-formeln).
- Schalter-Prompt nach ziel.md; pruefungsblatt.md 1.1; Vorlage:
  Zonen-Kopfzeile doppelt, Textfont-Zeichen.
- winkel-dreiecke.md Z. 125 (Umkehrung) offen, keine Kette.

Verworfen: Einzelzahl-Probe der Kastenzahlen (Stoff, nicht
Beispiel); Verzicht auf den Merkkasten (bleibt „auf Zuruf“, eine
Zeile im Schalter, Formelsammlungsform für Nachschlagen); P9, P10
und die übrigen aus archiv/uebergabe-2026-09-29.md.

## 6 Nächster Arbeitsschritt

Modell: Opus 5.5 (Fable auf Wahl des Lehrers). Läufe als
Unteragenten aus dem Chat, je Eintrag eigener Klon.

1. Gegenlese-Lauf über die 24 nachgezogenen Einträge: Auftrag nach
   dem Muster vom 27./28.09. (gegenlese.md je Eintrag), aber nur
   für neue und umgeschriebene Zeilen (Umbauskripte in
   werkzeuge/einmalig/ und stand.md nennen sie), mit den
   Nachbesserungen aus § 5; sechs bis sieben Agenten je Schub, vor
   jedem Schub Nutzungsanzeige ablesen (Woche 39 % am 30.09. 01:00).
2. Dann Prüfskript v0.11 (Formprobe P1–P8) und die Katalogbefunde
   aus § 5 als ein Katalogauftrag.
3. Erst dann der Schalter-Prompt nach ziel.md; pruefungsblatt.md 1.1
   im selben Zug.
