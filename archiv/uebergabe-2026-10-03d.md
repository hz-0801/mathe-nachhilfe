# Übergabe verbessereBlaetter – 2026-10-03d (Chat 03.10. abends, Fable/Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-03c.md.

Erster Handgriff im neuen Chat: `offen.html` (Wurzel dieses Repos)
mit SendUserFile, display „render“, an den Lehrer schicken. Oben
steht der Entscheidungsbaum, darunter die offenen Punkte und die
Liste „Zu prüfen ab Montag 18:00“. Ändert sich etwas: Baum in
`werkzeuge/baum-offen.py` ändern, Skript ausführen (schreibt den
Baumteil von offen.html), Liste in offen.html von Hand, neu
schicken, committen.

## 1 Ziel

Schnell gute Blätter für die Stunde, für P10 2027 zuerst, so gebaut,
dass Abitur GK/LK und FHR nur neue Daten brauchen. Phase jetzt: die
Bedienung festlegen (Entscheidungsbaum je Prüfung), gebaut wird
frühestens nach Montag 05.10. 18:00.

## 2 Arbeitsgrundlage

- `offen.html` – Entscheidungsbaum P10 (fertig) mit allen Regeln im
  Absatz unter dem Baum; offene Punkte; Prüfliste ab Montag.
  Maßgeblich.
- `werkzeuge/baum-offen.py` – Baumbeschreibung (Python-Tupel) und
  Zeichnung; der Fokus-Ausschnitt oben wird dort umgestellt.
- `msa/msa-ertrag.csv`, `msa/msa-katalog-kontext.csv`,
  `msa/msa-katalog-basis.csv` – Grundlage aller Zählungen im Chat.
- `msa/msa-vorgaben.md` – Fachbriefe; § 2 erklärt die Lücken
  2021–2023 (Corona-Ausschlüsse) und den Formatwechsel 2028.
- `faellig.md` § 2 – neu: Baum auf Format 2028 umstellen.

## 3 Arbeitsstand

Fertig 03.10. abends: P10-Baum vollständig und vom Lehrer bestätigt
(Commits cbf4b66 … 9c6bb44). Muster für andere Prüfungen erkannt:

1. Ast: Kurzteil der Prüfung (P10: Basis) · Prüfungsplätze nach
   Leitideen gebündelt (P10: Geometrie, Funktionen, Daten + Zufall)
   · Ganze Prüfung.
2. Art: überall Original · Original neu · Skript.
3. Auswahl: jahrgangsgebundene Teile (Basis, ganze Prüfung) → Jahr;
   Themen → beim Original die Prüfungsplätze, bei Original neu
   feiner, soweit Stoff da ist (Schwelle etwa 10 Teilaufgaben in
   fünf Jahren), beim Skript die Katalogeinträge plus „Weitere (RLP)“.
4. Zeitraum (nur Original, Original neu): [neuestes offenes]
   [2022–2026] [ältere] [Jahr wählen], blättern in Fünfjahresblöcken.

Nicht erledigt: Abitur und FHR; Vereinheitlichung (offen.html
Punkt 6); alles Bauen.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Frühere Übergaben gelten weiter, soweit hier nichts anderes steht.
Die Einzelregeln stehen unter dem Baum in offen.html; hier nur die
tragenden:

- Gleicher Ablauf und gleiche Knöpfe überall ist ein Wert an sich;
  Abweichungen nur begründet. Freitext geht immer; ist er unklar,
  nachfragen oder sagen, was nicht passt, und mit Knöpfen zum Ziel
  führen; nur Knöpfe, die zu einem Blatt führen. Etwa vier Knöpfe
  je Stufe, nicht starr (Stufe 1 hat fünf).
- Original = unveränderte Heftseiten, geschnitten nur an
  Aufgabengrenzen. Original neu = neu gesetzt, nach Teilaufgaben,
  passende Teilaufgaben anderer Aufgaben erlaubt, Bau zuletzt
  (Wortlaut Aufgaben 2–7 nicht erfasst). Skript = aus der Bank,
  vollständiges Heft mit Inhaltsverzeichnis, Seitenbereichen,
  Sprungmarken; „Lernblatt mit Prüfungsfilter“, einmal gebaut,
  liegt bereit.
- Lösung immer dabei (vorerst): Basis Streifen, sonst Lösungsblatt
  mit Rechenweg; Skript dazu Kontrollwerte und Tipps für Schwache.
- EBR/FOR: ein Blatt mit * für FOR-Teile (Original neu, Skript);
  Original ab 2026 nach Schülerliste, sonst FOR. Basis ist für beide
  gleich. „Schwach“ nie als Knopf.
- Prüfungsrelevant ist der Rahmenlehrplan (Fachbrief 8), FOR bis
  Niveaustufe G, EBR bis F plus Liste aus G.
- Umfang in Seiten dort, wo die Wahl ihn ändert (Zeitraum-Knöpfe);
  Zahlen nie strikt, nur „so ungefähr“.
- Bis Sommer 2027 schreiben alle P10-Schüler 2027 (kein
  Prüfungsjahr abfragen).
- Lehrer: keine Option ohne Informationsgewinn anbieten; erst eine
  Stufe festzurren, dann die nächste; Vorschläge immer mit Urteil.
- Modellwahl nächste Phase: Opus im Chat.

## 5 Offene Punkte und Verworfenes

Offene Punkte und Prüfliste stehen in offen.html. Dazu:

- Konsistenzbefund: Die Beschlüsse dieses Chats liegen nur in
  offen.html. ziel.md (z. B. „Blatt so lang wie der Teil, keine
  Seitengrenze“, Bauprinzip), bankblatt.md und zusammenbau.py kennen
  Baum, drei Arten, Lösungsformen und „Weitere (RLP)“ noch nicht.
  Nachziehen, wenn die Bäume aller Prüfungen stehen (vor dem Bau).
- Handreichung führt „Prozentrechnung“ als eigenes Thema; im Baum
  steckt Prozent im Original unter „Daten“ – beim nächsten Erneuern
  angleichen.
- Verworfen: Knopf „gemischt“ in der Geometrie (übernimmt die ganze
  Prüfung); Kosinussatz als „gibt es nicht“ (er ist nur nie geprüft,
  steht für FOR im RLP – Prüfliste); Extra-Knopf für kleine Themen
  (Sprossen und Freitext); Prüfungsjahr im Schülerdialog.

## 6 Nächster Arbeitsschritt

offen.html zeigen. Dann den Abitur-Baum nach dem Muster aus § 3
entwerfen: zuerst nur Stufe 1 (Kurzteil = hilfsmittelfreier Teil 1?
Äste Analysis · Geometrie · Stochastik? Ganze Prüfung), mit Zählung
aus abitur/abi-katalog.csv und iqb-katalog.csv wie bei P10
(Plätze je Prüfung über die Jahre). GK und LK sind getrennte Hefte –
Sternchen-Blatt trägt vermutlich nicht; Abweichung begründen. Stufe
für Stufe festzurren, Fokus-Ausschnitt in baum-offen.py umstellen.
