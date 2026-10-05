# Übergabe verbessereBlaetter – 2026-10-05 (Chat 04./05.10., Opus, ab abends Fable)

Vorherige Übergabe: archiv/uebergabe-2026-10-04.md.

Erster Handgriff im neuen Chat: `offen.html` (Wurzel) mit SendUserFile,
display „render“, schicken. Oben steht der Baum „P10 Skript“ mit
Kapiteln und Abschnitten, darunter das Skript-Ziel und der Absatz
„Zuschnitt der Abschnitte“ mit allen Beschlüssen vom 04./05.10.; unten
die Liste „Zu prüfen ab Montag 18:00“. Ändert sich etwas: Texte in
`werkzeuge/baum-offen.py` (SKRIPT_ZIEL, Themen), Skript ausführen;
Listen in offen.html von Hand; committen, neu schicken.

## 1 Ziel

Schnell gute Blätter für die Stunde, P10 (vier Schüler) und Abitur
2027 GK (Nr. 15) zuerst. Phase jetzt: Vorratslauf fortsetzen und das
erste Skript bauen.

## 2 Arbeitsgrundlage

- `offen.html` – maßgeblich für alle Beschlüsse zur Bedienung und zum
  Skript (Baum, Zuschnittsregeln, Lösungsdatei, Verzeichnisse,
  Bausteine, Messwerte, offene Punkte).
- `msa/skript-zuschnitt-p10.csv` (+ `.md`, gebaut) – Zuschnitt P10:
  Gebiet, Kapitel, Abschnitt, Stufe, Hauptplatz-ids, Nebenplatz-ids.
  Entwurf; Geometrie und Funktionen vorläufig bestätigt, Daten + Zufall
  nicht angesehen.
- `abitur/skript-zuschnitt-abi-gk.csv` (+ `.md`) – Zuschnitt Abitur GK
  BB 2022–2026, 52 Abschnitte, Entwurf eines Agenten; unsichere
  Zuordnungen stehen im Agentenbericht nicht im Repo, nur die Datei.
- `werkzeuge/skript-zuschnitt.py [p10|abi-gk]` – prüft (jede
  Teilaufgabe genau ein Hauptplatz) und baut die Übersicht.
- `archiv/vorrat-p10-2022-2026-2026-10-05.csv`, `archiv/vorrat-abi-gk-2022-2026-2026-10-05.csv`
  – Beitabellen des Vorratslaufs Block 1 (id; kurz; zwischen; stich;
  neben; abh; sympy), Standdateien `*-stand.md` mit Bericht;
  `werkzeuge/vorrat-pruef.py`, `vorrat-sympy-*.py`.
- `werkzeuge/handreichung-abi.py` (KNOPF = Themenknöpfe Abitur, jetzt
  mit Erwartungswert); `aufgabenbank-privat/schueler.md`.

## 3 Arbeitsstand

Fest (04./05.10., Wortlaut in offen.html):

- Skript-Zuschnitt: Abschnitt = Handgriff (erster Kopf-Schritt, an den
  echten Teilaufgaben gefunden); so lang wie nötig; nichts fällt weg,
  Seltenes hinten mit „selten geprüft“, aufgefüllt aus älteren
  Jahrgängen, Berlin, IQB, anderen Ländern, zuletzt eigene Aufgaben
  (Marke „eigene Aufgabe“), Herkunft in der Fundstelle; Abhängigkeit
  ist kein Schnittgrund (Zwischenergebnis steht dabei); Hauptplatz je
  Teilaufgabe, Nebenplatz nur als eigene Stufe, gezählt nur Hauptplatz,
  „kennst du aus …“ am Nebenplatz; gemischte Abschnitte zum
  Unterscheiden aus Nebenplätzen (Pythagoras oder Winkelfunktion?).
- Ebenen: Gebiet → Kapitel (letzter Knopf) → Abschnitt → Stufe;
  Abschnitte per Freitext, keine tieferen Knöpfe. P10-Kapitel:
  Dreiecke · Flächen · Körper / Lineare · Quadratische ·
  Gleichungssysteme · Wachstum / Prozent · Daten · Wahrscheinlichk.;
  je Gebiet „Weitere (RLP)“ und „Alles“. Basisteil bleibt ganz und
  gemischt (Original, Antwortbogen), kein Basis-Skript; 27 Basisaufgaben
  zusätzlich als unterste Stufe im Hauptteil. Abitur: Stochastik hat
  den Knopf „Erwartungswert“ (9 GK-Teilaufgaben, 28 BE).
- Prüfstein am Kapitelende: eine ganze echte Aufgabe, eigener Wortlaut,
  Punkte, Fundstelle, ohne Überschriften und Hilfen; vorn kein
  Ziel-Beispiel; Abitur: je Gebiet (offen).
- Seitenaufbau: Überschrift in Prüfungsformulierung · „kommt das
  dran?“ · „neu: …“ je Stufe · Leitaufgabe groß, „weitere dieser Art“
  kompakt mit Fundstelle · Kontrollwert und Tipp (ein Stichwort)
  verdeckt am Fuß derselben Seite · vorn immer eine Übersicht in
  Lernreihenfolge mit Stichwörtern; alphabetisches Verzeichnis nur bei
  „Alles“ als Lückenfüller; Fokusblatt ohne Verzeichnis.
- Lösungsdatei, alle Prüfungen und Arten: eigene Datei; links Lösung
  mit Einheit, rechts höchstens ein Zwischenwert oder Formel/Begriff;
  Stichworte, Begründungen mit ⇒; so knapp wie möglich, Aufgabe nie
  über Seitenwechsel; keine Lücken-Zeile für den Lehrer (nur bei
  „schwach“); Zusätze: Skript Tipp + Kontrollwerte, P10-Basis
  Antwortbogen.
- Vorrat Block 1 auf dem Skript-Ausschnitt erledigt (Beitabellen,
  346 nachgerechnet, 2 Katalogfehler im Feld zwischenergebnis, s.
  faellig.md). Empfehlung des Chats: Beitabelle bleibt eigene Datei,
  die der Skript-Bau liest; Katalog nur korrigieren (zwischenergebnis,
  abhaengig_von). Lehrer hat noch nicht entschieden.

Nicht erledigt: Unterbau-Verweis (Vorschlag „Klappt das nicht? →
Grundlagen: …“ unter der ersten Stufe, Lehrer: später); P10-Einzelheiten
(Dreiecke teilen, Prozent gemischt, Seitenzahl am Knopf) am ersten
gebauten Skript; Abitur-GK-Zuschnitt Kapitel für Kapitel prüfen;
Handreichungs-PDFs; Vorratslauf Rest.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Frühere Übergaben gelten weiter, soweit hier und in offen.html nichts
anderes steht. Tragend:

- Originale bleiben beim Lehrer; das Skript hat nur eigenen Wortlaut
  mit Fundstelle. Ketten übt der Schüler an den Originalen, das Skript
  übt gezielt (Begründung des Lehrers 04.10. für Weg B).
- Die Regel „höchstens jede siebte Teilaufgabe braucht ein Ergebnis von
  woanders“ gilt für Themenknöpfe, nicht für Abschnitte im Skript.
- Serie (kurze Blätter mit Wiederkehr) liegt; Auslöser: vier
  P10-Schüler haben je zwei, drei Skript-Themen durchgearbeitet.
- Nächster Schritt aus einer Übergabe wird geprüft, nicht übernommen
  (Lehrer 04.10.: „warum sollten wir damit anfangen?“).
- Messwerte: Fable-Agent 209 000 Token → Woche +1, Fable +2; zwei
  Fable-Agenten 556 000 Token → Woche 90 → 93 %, Fable 91 → 95 %
  (≈ 185 000 Token je Wochenpunkt). Fable zählt immer auch auf die
  Woche; bindend ist die Woche. Reset Montag 05.10. 18:00; bis 15:30
  5 % Rest halten (Stand 93 % am Morgen).
- Modellwahl nächste Phase: Opus im Chat; Agenten für Vorrat-Teile
  Opus (Fable nur, wenn der Lehrer es wählt).

## 5 Offene Punkte und Verworfenes

- Beitabelle oder Katalog (oben, § 3 letzter Punkt) – Entscheidung des
  Lehrers.
- Zwei zweifelhafte abhaengig_von-Werte in P10 (2022-OS-K7b ← K7a,
  2022-OS-K5e ← K5d): keine echte Rechenabhängigkeit, übernommen.
- Feld neben (jede mitbenutzte Fertigkeit) ≠ typ_neben (zweite
  bepunktete Leistung): getrennt halten, „kommt das dran?“ zählt nur
  typ/typ_neben.
- Abitur-Prüfstein je Gebiet statt je Kapitel: am ersten Abitur-Skript.
- Konsistenz ziel.md, bankblatt.md, zusammenbau.py (faellig.md § 2)
  weiter offen; dazu die Lücken-Zeile und „eine Seite je Heft“.
- Verworfen (04.10.): Basis-Skript nach Typ getrennt (Basisteil prüft
  das Umschalten); „je Stufe höchstens zwei, Rest als Fundstelle“
  (alle Teilaufgaben stehen auf dem Blatt, überblätterbar);
  Abschnitte als Knöpfe (ein Klick mehr bei jeder Bestellung);
  Stichwortverzeichnis vorn (zeigt keinen Weg; Übersicht in
  Lernreihenfolge stattdessen); Kontrollwert offen neben der Aufgabe
  (Vorlage statt Hilfe).

## 6 Nächster Arbeitsschritt

Nach 18:00: (1) Lehrer entscheidet Beitabelle oder Katalog; dann
Katalogkorrektur und abhaengig_von über das Bau-Skript (Agent). (2)
Vorratslauf Rest in Teilen, je Teil ein Agent mit Standdatei und
Commit je Teilstück, nach jedem Teil Nutzungsanzeige ablesen: zuerst
P10 2014–2021 und Abitur GK 2017–2021, dann Felder 6–10 der
Montagsliste (offen.html), dann LK, iqb, fhr. (3) Erstes P10-Skript
bauen (Kapitel Prozent oder Lineare, Schüler Nr. 1–5) als Prüfstein
für Zuschnitt, Seitenaufbau und Lösungsdatei; die P10-Einzelheiten
dort entscheiden.
