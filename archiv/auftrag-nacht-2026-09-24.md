# Auftrag: drei unabhängige Teile für einen unbeaufsichtigten Lauf

Stand 2026-09-24. Ordner mathe-nachhilfe. Modell Sonnet.

## Ausgangslage

Der Lehrer ist nicht am Rechner. Drei Teile, die nichts
voneinander wissen; ein Commit je Teil; scheitert ein Teil nach
zwei Anläufen, wird er in msa/nacht-stand.md als „offen: <Grund>"
vermerkt und der nächste Teil beginnt. Nichts wartet auf den
Lehrer. Die Standdatei msa/nacht-stand.md legst du zu Beginn an
(drei Zeilen: Teil 1–3 „offen") und schreibst sie nach jedem Teil
fort; ein Neustart nach Abbruch beginnt beim ersten Teil ohne
„erledigt".

## Regeln

- Python nur über %LocalAppData%\Programs\Python\Python312\
  python.exe; git über die git.exe von GitHub Desktop; PowerShell.
  git mit -c core.pager=cat, commit -m, nicht pushen.
- Nichts löschen. Keine Handedits an CSV. Etiketten (Typen,
  Themen) werden nicht umbenannt oder zusammengezogen; ein neuer
  Typ nur nach Kern § 6, Vorschläge zum Zusammenziehen in den
  Bericht.
- Texte aus PDF mit pdftotext -layout, sonst pypdf/PyMuPDF; Seiten
  rendern mit pdftoppm oder PyMuPDF; geht beides nicht, Text allein
  und „Bild nicht gesehen" in bemerkung.
- Dateien unter hefte/ sind lokal (.gitignore) und werden nicht
  committet; Textfassungen in quellen/ werden committet.

## Teil 1: EBR-Heft 2026 erfassen (Profil msa, papier EBR)

Der Lehrer hat am 24.09.2026 entschieden, das Heft zu erfassen
(bisher zurückgestellt: konzept.md, Satz „EBR-Hefte bleiben
zurückgestellt, solange kein EBR-Schüler da ist", und
msa-pruefungen.md § 2). Zweck: Vergleich EBR gegen FOR je Typ, um
zu entscheiden, ob EBR im Themenkatalog eine eigene Marke braucht.

1. Datei: hefte/msa/2026-ebr.pdf (Server: 26_P10_Ma_EBR_A.pdf,
   msa-quellen.md § 5). Fehlt sie lokal, mit curl von der
   Jahresseite (msa-quellen.md § 1) holen.
2. Erfassen nach CLAUDE.md § 2 und msa/msa.md: papier EBR, ids
   2026-EBR-B1a usw., Aufbau wie FOR 2026 (msa.md § 3: getrennte
   Hefte ab 2026, EBR 40 BE, keine Sternchen), Zeilen in die
   Katalogdateien Basis/Kontext wie bei FOR. Gegenprobe:
   Punktsumme 40 laut Deckblatt – weicht das Deckblatt ab, gilt
   das Deckblatt, und die Abweichung steht im Bericht.
3. Nachführen im selben Commit: msa-pruefungen.md § 2 (Zeile
   EBR 2026 auf „erfasst, n Zeilen") und Änderungslog;
   msa-quellen.md § 2/§ 5 (Status der Datei); konzept.md: den
   Satz zur Zurückstellung ersetzen durch „EBR 2026 erfasst am
   24.09.2026 (Grund: Marke im Themenkatalog), Vergleich EBR/FOR
   steht aus";
   faellig.md § 1 msa: „EBR bleibt zurückgestellt" streichen,
   Zeile Heft 2027 auf „FOR und EBR holen". werkzeuge/ertrag.py
   laufen lassen (EBR-Zeilen zählen dort mit; im Bericht die
   Zahl der Typen nennen, deren Ertrag sich dadurch ändert).
   werkzeuge/themen-pruef.py Rückgabe 0.
4. Vergleich EBR/FOR: werkzeuge/gym-vergleich.py um eine
   Option --gruppen erweitern (Gruppe A = papier EBR, Gruppe B =
   papier FOR und OS), Ausgabe msa/ebr-vergleich.md nach dem
   Muster von gym-vergleich.md (Typen und Themen: nur A, nur B,
   beide; Haupt und Haupt+Neben). Commit „msa: Heft 2026 EBR
   erfasst, n Zeilen; Vergleich EBR/FOR".

## Teil 2: Stoffverteilungspläne der Landesausgaben sichern

Zweck: Grundlage für die Lehrwerkfrage im Themenkatalog (bisher
nur der Klett-Fahrplan Lambacher Schweizer Berlin,
quellen/quelle-klett-fahrplan-ls-aa-berlin-2024.txt). Gesucht
sind frei zugängliche Stoffverteilungspläne, Fahrpläne oder
Synopsen zum Rahmenlehrplan 1–10 Berlin-Brandenburg, Mathematik
Klasse 7–10, für die Landesausgaben Berlin/Brandenburg von:

- Klett: Lambacher Schweizer (Gymnasium), Schnittpunkt
  Mathematik (Oberschule/ISS), Mathe live (falls BE/BB-Ausgabe)
- Westermann: Elemente der Mathematik, Mathematik Neue Wege,
  Sekundo oder maßstab (falls BE/BB-Ausgabe)
- Cornelsen: Fundamente der Mathematik, Fokus Mathematik (falls
  BE/BB-Ausgabe)

1. Je Werk und Klasse die Verlagsseite mit curl absuchen (Suche
   nach „Stoffverteilungsplan", „Synopse", „Fahrplan",
   „Berlin/Brandenburg", „Rahmenlehrplan"); höchstens zehn
   Minuten je Werk. Kein Login, kein Formular, keine Registrierung.
2. Gefundene PDF nach hefte/lehrwerke/<verlag>-<werk>-<klasse>-
   <jahr>.pdf sichern (lokal), Text mit pdftotext -layout nach
   quellen/quelle-<verlag>-<werk>-bb-<jahr>.txt (eine Datei je
   Werk, alle Klassen hintereinander, Trennzeile mit Klasse);
   Eintrag in quellen/quellen.md nach dem Muster der vorhandenen
   Einträge (Titel, Umfang, Stand, Adresse, Datum).
3. Fundliste quellen/lehrwerke-fundliste.md: je Werk eine Zeile –
   Verlag, Werk, Landesausgabe BE/BB ja/nein/unklar, Schulform laut
   Verlag, Klassen, was gefunden wurde (Datei) oder „nicht frei
   verfügbar" oder „nicht gefunden (Suchbegriffe: …)". Nichts
   bewerten, nichts erfassen. README.md: die neuen Dateien unter
   quellen/ je ein Satz. Commit „quellen: Stoffverteilungspläne
   Landesausgaben BE/BB gesichert, Fundliste".

## Teil 3: Vorbehalt in fhr-vorgaben.md prüfen

Schritt 0 des Jahreschecks (fhr/fhr-vorgaben.md § 4): jede Zeile
von § 1 bis § 3 gegen die Papiere halten – Prüfungsschwerpunkte
2026/27 und 2027/28, Rundschreiben MBJS_RS_07-26, Hefte. Die
Papiere liegen unter hefte/fhr/sonstiges/ (Auftrag N); fehlen
sie, mit curl von der Übersichtsseite (fhr-quellen.md § 1) holen.

1. Je Angabe: Fundstelle im Papier (Datei, Seite) und Ergebnis
   „bestätigt", „abweichend: <Papier sagt …>" oder „nicht
   belegbar". Ergebnis als fhr/fhr-vorgaben-pruefung-2026-09.md.
2. Nur „bestätigt"-Zeilen bekommen in fhr-vorgaben.md die
   Fundstelle nachgetragen; abweichende Angaben werden nicht
   geändert, sondern stehen im Bericht – der Lehrer entscheidet.
   Den Vorbehalt im Kopf nicht streichen (das setzt voraus, dass
   keine Abweichung offen ist). faellig.md § 2: Posten auf
   „Prüfung erfolgt 2026-09-24, Abweichungen offen: n" setzen.
   Commit „fhr: Vorgaben gegen die Papiere geprüft".

## Abschluss

- empty_zeilen.py (Repo-Wurzel, Hilfsskript aus dem Abgleichlauf)
  nach archiv/ verschieben (git mv). Auftrag nach archiv/
  verschieben. nacht-stand.md bleibt in msa/. Commit „archiv:
  auftrag-nacht-2026-09-24, empty_zeilen.py".

## Bericht

Als msa/nacht-bericht-2026-09-24.md (im Abschluss-Commit) und im
Chat: erste Zeile das Modell. Teil 1: Zeilen Basis/Kontext, BE
Soll/Ist, neue Typen mit Definition, „?"-Zeilen, Vergleichszahlen
EBR/FOR (nur EBR / nur FOR-OS / beide), Zahl der Typen mit
geändertem Ertrag. Teil 2: die Fundliste in Kurzform (je Werk eine
Zeile). Teil 3: Zahl bestätigt / abweichend / nicht belegbar, die
Abweichungen im Wortlaut. Teile „offen" mit Grund, eigene
Entscheidungen. Letzte Zeile: „Push origin drücken".
