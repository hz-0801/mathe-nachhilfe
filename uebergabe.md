# Übergabe verbessereBlaetter – 2026-10-04 (Chat 03./04.10., Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-03d.md.

Erster Handgriff im neuen Chat: `offen.html` (Wurzel dieses Repos)
mit SendUserFile, display „render“, an den Lehrer schicken. Oben
stehen das Ziel des Skripts und der Fokus (Original neu, darunter
Original), dann Abitur/FHR/P10-Bäume, die Vergleichstabelle nach
Stufe, offene Punkte und „Zu prüfen ab Montag 18:00“. Ändert sich
etwas: `werkzeuge/baum-offen.py` (Bäume, Texte SKRIPT_ZIEL, FOKUS)
ändern und ausführen; Listen in offen.html von Hand; neu schicken,
committen.

## 1 Ziel

Schnell gute Blätter für die Stunde, P10 und Abitur 2027 zuerst. Phase
jetzt: Bedienung (Entscheidungsbaum) für alle Prüfungen vereinheitlicht
und festgelegt; Bauen frühestens ab Montag 05.10. 18:00.

## 2 Arbeitsgrundlage

- `offen.html` – maßgeblich für alle Beschlüsse zur Bedienung (Texte
  unter den Bäumen, Vergleichstabelle, Skript-Ziel).
- `werkzeuge/baum-offen.py` – erzeugt den Baumteil von offen.html.
- `aufgabenbank-privat/schueler.md` (privates Repo) – Schüler mit
  Nummer, Schulen mit Land und Rechner, Liste gelieferter Blätter.
  Maßgeblich; die Projektdatei Schuelerliste-privat.md ist veraltet.
- `abitur/handreichung-abi-gk-2027.*`, `-lk-2027.*` mit
  `werkzeuge/handreichung-abi.py` (KNOPF = Themen; Entwurf, Lehrer
  will sie noch einmal sehen); `msa/handreichung-reihenfolge.md` mit
  Skript (Daten für die Lernreihenfolge der P10-Handreichung, nicht
  eingebaut).
- `katalog/_skript-filter.md` mit `werkzeuge/skript-filter-mass.py`
  (Anteil geprüfter Lerneinheiten je Eintrag).
- `fhr/fhr-vorgaben.md` – Absatz vor § 2: Berliner FHR ist eine
  eigene Prüfung.

## 3 Arbeitsstand

Fest (03./04.10.), Einzelheiten in offen.html:

- Stufe 1 überall Kurzteil (Basis bzw. Hilfsmittelfrei) · Hauptteil ·
  Ganze Prüfung; FHR ohne Kurzteil. Darunter die Gebiete; jede Ebene,
  die sich aufteilt, endet mit „Alles“.
- Vor dem Baum: Name nur erfragen, wenn keiner genannt; Kurs, Papier,
  Land, Rechner aus schueler.md, fehlt etwas: einmal fragen, eintragen.
- Original: Heftseiten (Abitur-Fotos/Scans durchsuchbar, „Nur für den
  privaten Gebrauch“), Schnitt an Aufgabengrenzen, keine Themenknöpfe
  (Gebiet → Zeitraum), Zeitraum neuestes offenes · 2022–2026 · ältere
  · Jahr wählen. Lösungsblatt: je Heft eine Seite, je Teilaufgabe
  links Lösung, rechts Zwischenwerte, keine Sätze.
- Original neu: Schnitt wie Original, besser gesetzt (Setzregeln in
  offen.html), durchsuchbar; ein Jahr → Stichwortverzeichnis auf dem
  Lösungsblatt, mehrere Jahre → Inhalts- und Stichwortverzeichnis.
  Vorspann gekürzt, Wortlaut der Teilaufgaben bleibt.
- Skript: Ziel in acht Punkten und Richtung fest – echte
  Prüfungsaufgaben nach Handgriff sortiert, leicht → schwer, „kommt das
  dran?“ belegt, Hilfen gestuft, Unterbau aus dem allgemeinen Blatt nur
  bei Bedarf, Wortlaut hart an der Grenze des Erlaubten, Fundstellen als
  Jahr · Aufgabe · Teilaufgabe (Stark-Hefte der Schüler).
- Wer bekommt was: Original und Original neu für den Lehrer; Schüler
  bekommt Skript, Basis als Antwortbogen zum amtlichen Heft, QR-Code.
- Schüler 2027 mit Mathe-Prüfung: P10 Nr. 1, 2, 4, 5 (Nr. 3 offen);
  Abitur Nr. 15 (GK, BB), vielleicht Nr. 10; FHR niemand. Alle
  Schulen BB außer Nr. 18 (keine Mathe-Prüfung).

Nicht erledigt: Skript-Zuschnitt (Handgriffe als Gliederung) und
Bausteine; Lösungsform Skript; FHR-Feinheiten; Handreichungen.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Frühere Übergaben gelten weiter, soweit hier und in offen.html nichts
anderes steht. Tragend:

- Eine Stufe bzw. eine Art (Original → Original neu → Skript) fertig
  besprechen, bevor die nächste kommt; nichts Beschlossenes ungefragt
  neu aufrollen, aber Schwächen als Revision vorlegen.
- Gleicher Ablauf ist ein Wert; Abweichung nur mit Grund.
- Lösung immer dabei.
- Ab Montag 18:00 tokensparend: nichts doppelt lesen, Schritte
  abgestimmt, in Blöcken, nach jedem Block Verfahren prüfen; Qualität
  zuerst.
- Woche stand am 04.10. bei 88 % (Fable 89 %), Reset Montag 18:00.
- Modellwahl nächste Phase: Opus im Chat.

## 5 Offene Punkte und Verworfenes

- Konsistenz: ziel.md, bankblatt.md, zusammenbau.py kennen den neuen
  Baum, die neue Bedeutung von Original neu/Skript, Antwortbogen,
  Lösungsblattform und schueler.md nicht (faellig.md § 2).
- Handreichung P10: Themen nach Punkten, nicht nach Knöpfen; Daten
  für eine Lernreihenfolge liegen, Entscheidung offen. Handreichung
  Abitur: Themen aus KNOPF – nach dem Skript-Zuschnitt angleichen.
- Fernziel: Zettel „Was ist zu tun?“ (Formulierung → Handgriff) und
  Merkblatt je Thema; braucht eine Sammlung der Formulierungen.
- Projektanweisung: Regeln „Offene Punkte rechts“ und „Eine Stufe
  festzurren“ stehen nur in kandidaten.md, nicht in der
  Projektanweisung.
- Verworfen: Original neu nach Teilaufgaben geschnitten (Register statt
  Schnitt); Themenknöpfe beim Original; verdichteter Wortlaut der
  Teilaufgaben; Skript als „Lernblatt mit Prüfungsfilter“; Skript nach
  amtlicher Gliederung (wechselt jährlich); FHR ruhen lassen.

## 6 Nächster Arbeitsschritt

offen.html zeigen. Dann den Zuschnitt des Skripts besprechen: Welche
Handgriffe (Typen aus dem Katalog, gebündelt) bilden die Gliederung je
Gebiet, mit Zählung „wie oft in fünf Jahren, zuletzt, Punkte“ aus den
Katalogen; zuerst Abitur GK (Nr. 15), dann P10. Ab Montag 18:00
parallel der Vorratslauf (faellig.md § 2).
