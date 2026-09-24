# Auftrag: Inhaltsverzeichnisse der Landesausgaben über die
Deutsche Nationalbibliothek sichern

Stand 2026-09-25 (Fassung 2, ersetzt die Fassung vom Vormittag).
Ordner mathe-nachhilfe. Modell Sonnet.

## Ausgangslage

Die Deutsche Nationalbibliothek führt zu fast jedem Schulbuch das
Inhaltsverzeichnis als PDF: Katalogsatz https://d-nb.info/<IDN>,
Inhaltsverzeichnis https://d-nb.info/<IDN>/04. Die Sätze sind über
die SRU-Schnittstelle abfragbar (werkzeuge/dnb-sru.py, geprüft am
25.09.2026: Fundamente der Mathematik 7–10 liefert je drei Seiten
Inhaltsverzeichnis). Das ersetzt Leseproben und Warenkorb. Die
DNB-Titel nennen das Bundesland meist nicht; die Landesausgabe
wird über die ISBN auf der Verlagsseite bestätigt.

Zweck: je Werk und Klasse die Kapitelfolge als Text für den
Themenkatalog (Verortung je Sprosse über mehrere Bücher).

## Schon bestätigt (ISBN und IDN, Landesausgabe geprüft)

Cornelsen, Fundamente der Mathematik, Ausgabe B ab 2024 (Berlin,
Brandenburg; Gymnasium, Gesamtschule, ISS, Oberschule):
- Kl. 7: 9783060428090, IDN 1315139596
- Kl. 8: 9783060428137, IDN 1322564353
- Kl. 9: 9783060428175, IDN 1338042475
- Kl. 10: 9783060428212, IDN 1373177926
Dazu Ausgabe B ab 2017, Kl. 9: 9783060098538, IDN 1095896164
(Vorgängerausgabe; Kl. 7, 8, 10 dieser Ausgabe mitsuchen).

## Zu suchen

- Westermann, Mathematik – Ausgabe 2023 für Berlin, Brandenburg,
  Sachsen-Anhalt, Thüringen (Oberschule), Schulbuch Kl. 7–10
  (Arbeitshefte 9783141524727/-734 sind in der DNB; die Schulbuch-
  ISBNs über die Westermann-Reihenseite ermitteln)
- Westermann, Mathematik heute, Ausgabe 2014 für die Sekundarstufe
  I in Berlin und Brandenburg, Kl. 7–10 (Schülerband 7:
  9783507812604, Vorgängerreihe der Ausgabe 2023)
- Westermann, Elemente der Mathematik SI, Ausgabe 2016 für
  Berlin/Brandenburg, Kl. 7–10, und Ausgabe 2025, soweit erschienen
  (Kl. 10 der Ausgabe 2016 fehlt als Plan)
- Westermann, Sekundo, Ausgabe 2017 für Berlin und Brandenburg,
  Kl. 7–10 (Pläne liegen; Inhaltsverzeichnis als Gegenprobe)
- Klett, Schnittpunkt Mathematik, Differenzierende Ausgabe (BE,
  BB u. a.) ab 2017, Kl. 7–10
- Klett, Lambacher Schweizer: prüfen, ob eine Ausgabe
  Berlin/Brandenburg existiert; sonst Allgemeine Ausgabe Kl. 7–10
  als Gegenprobe zum Fahrplan
Nebenfund: kapiert.de (Westermann) legt Inhaltsverzeichnisse unter
/fileadmin/redakteure/Lehrwerke/Mathematik/Inhaltsverzeichnis/ ab;
dort suchen, wenn die DNB zu einem Band keins hat.

## Regeln

- Python nur über %LocalAppData%\Programs\Python\Python312\
  python.exe; git über die git.exe von GitHub Desktop; PowerShell.
  git mit -c core.pager=cat, commit -m, nicht pushen.
- Nichts löschen. Kein Login, keine Registrierung, kein Warenkorb.
  Verlagsseiten nur lesen (Filter anklicken erlaubt).
- Je Werk höchstens fünfzehn Minuten Suche; danach „nicht
  gefunden" mit Suchbegriffen. Keine Bewertung, keine Zuordnung
  zum Katalog.
- Dateien unter hefte/ sind lokal (.gitignore); Textfassungen
  unter quellen/ werden committet. Das Inhaltsverzeichnis wird
  als Text übernommen (Kapitelnummer, Titel, Seite), sonst nichts
  aus dem Buch.

## Schritte

1. werkzeuge/dnb-sru.py prüfen: python dnb-sru.py 'tit="Fundamente
   der Mathematik" and jhr=2025' muss den Satz 1338042475 mit
   TOC:ja zeigen. Sonst Skript reparieren (Endpunkt
   services.dnb.de/sru/dnb, MARC21-xml), nicht die Aufgabe.
2. Je Werk: ISBNs der Schulbücher Kl. 7–10 ermitteln (Verlagsseite,
   Reihe, Landesausgabe im Titel oder in „Bundesland"), dann DNB:
   num=<ISBN> oder Titelsuche; IDN und TOC-Link notieren. Fehlt der
   TOC-Link in der DNB, kapiert.de bzw. Verlagsseite prüfen.
3. PDF nach hefte/lehrwerke/<verlag>-<werk>-<ausgabe>-<klasse>-
   inhalt.pdf (lokal); Text mit pdftotext -layout; je Werk eine
   Datei quellen/quelle-<verlag>-<werk>-bb-<ausgabe>-inhalt.txt:
   Kopf (Werk, Ausgabe, Schulform laut Verlag, je Klasse ISBN und
   IDN, Adresse d-nb.info/<IDN>/04, Datum), dann je Klasse
   „== Klasse n ==" und das Inhaltsverzeichnis. Prüfung: je Klasse
   mindestens die Kapitel erster Ebene mit Seitenzahl.
4. quellen/lehrwerke-fundliste.md: zweite Tabelle
   „Inhaltsverzeichnisse" (Verlag, Werk, Ausgabe, Klasse, ISBN,
   IDN, Fund, Vollständigkeit). quellen/quellen.md: die neuen
   Textdateien nach dem Muster der vorhandenen Einträge. README.md:
   dnb-sru.py und die Textdateien je ein Satz.
5. Commit „quellen: Inhaltsverzeichnisse Landesausgaben BE/BB (DNB)".
   Auftrag nach archiv/ verschieben, Commit „archiv:
   auftrag-lehrwerke-inhalt".

## Bericht

Als quellen/lehrwerke-inhalt-bericht-2026-09.md (im Commit) und im
Chat: erste Zeile das Modell. Je Werk und Klasse eine Zeile: ISBN,
IDN, Fund (DNB / kapiert / Verlag / nicht gefunden), Kapitel erster
Ebene, vollständig ja/nein. Eigene Entscheidungen. Letzte Zeile:
„Push origin drücken".
