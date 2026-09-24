# Auftrag Nacht 2026-09-25: Klassenbelege aus den Lehrwerken,
# weitere Inhaltsverzeichnisse, fremde Aufgabensammlungen

Modell: Opus (Zuordnung Einheit – Kapitelzeile lässt Lesarten
offen). Läuft ohne den Lehrer: keine Rückfrage, Standdatei,
Commit je Teil, Fehlerregel je Teil.

## Ausgangslage

ziel.md (Stand 25.09.2026) § 1 „Zeitachse": Der Katalog soll an
jeder Lerneinheit tragen, in welcher Klasse die Lehrwerke der
Oberschule und die des Gymnasiums sie lehren – so fein, wie die
Inhaltsverzeichnisse es hergeben (am Typ, wo ein Buch ihn nennt,
sonst an der Einheit), samt Verlagsmarken für „nicht für alle"
(Vertiefen, LVL, Sonderfälle, Wissen kompakt). Dieser Auftrag
schreibt die Vorschlagsliste dafür (Teil 2). Vorher holt er die
Verzeichnisse, die noch fehlen (Teil 1), und danach sichert er
freie Aufgabensammlungen anderer Länder für die 22 Prüfungshöhen
ohne P10-Original (Teil 3). Du änderst keinen Katalogeintrag: Die
Vorschlagsdateien schlagen vor, der Lehrer entscheidet.

Muster für Form und Lesart: katalog/_niveaustufen-belege.md
(Kopf, Zahlenblock, je Eintrag ein Abschnitt, Zitat wortgleich
mit Fundstelle, „keine Stelle" ist ein Ergebnis, „Ermessen:" mit
Grund). Lies ihren Kopf und einen Eintragsabschnitt, bevor du
Teil 2 beginnst.

Verzeichnisse im Repo (quellen/, Format: eine Datei je Reihe,
Trennzeilen „== Klasse n =="; Seitenzahlen stehen in den Zeilen):
- Oberschule: quelle-westermann-sekundo-bb-2017-inhalt.txt (7–10),
  quelle-westermann-mathematik2023-bebbstth-inhalt.txt (7–10),
  quelle-klett-schnittpunkt-mathematik-diff2017-inhalt.txt (7–10),
  quelle-westermann-mathematikheute-bebb-inhalt.txt (7–10).
- Gymnasium: quelle-cornelsen-fundamente-bb-ausgabeb2024-inhalt.txt
  (7–10), quelle-cornelsen-fundamente-bb-ausgabeb2017-inhalt.txt
  (nur 9), quelle-westermann-elemente-der-mathematik-bb-2016u2025-
  inhalt.txt (7–10 und 5–7), quelle-klett-fahrplan-ls-aa-berlin-
  2024.txt (Lambacher Schweizer, Klasse 5–10, Kapitel und
  Lerneinheiten, ohne Seiten – gilt als Verzeichnis).
- Förderhefte (Sorte „Förderheft" in quellen/foerderhefte-
  fundliste.md): quelle-westermann-sekundo-foerder-be_bb2017-
  inhalt.txt, quelle-klett-schnittpunkt-foerder-diff2017-inhalt.txt,
  quelle-westermann-mathematik2023-foerder-bebbstth-inhalt.txt,
  quelle-westermann-mathematikheute-diagnoseundfoerdern-inhalt.txt.
- Stoffverteilungspläne: quelle-westermann-elemente-der-mathematik-
  bb-2016.txt, quelle-westermann-sekundo-bb-2017.txt (Gegenproben,
  nicht Hauptquelle).

Werkzeuge: werkzeuge/dnb-sru.py (CQL als Argument; Treffer mit
IDN, Jahr, ISBN, Titel, TOC ja/-; Inhaltsverzeichnis-PDF unter
https://d-nb.info/<IDN>/04). Beispiele früherer Aufrufe in
quellen/lehrwerke-inhalt-bericht-2026-09.md.

## Regeln

- Shell PowerShell: kein Heredoc, kein sed. Dateien schreiben mit
  [System.IO.File]::WriteAllText(pfad, text,
  (New-Object System.Text.UTF8Encoding($false))) – nicht mit
  Set-Content/Out-File -Encoding UTF8, das erzeugt eine BOM.
  Zeilenenden LF; nach dem Schreiben prüfen (keine BOM, kein CR).
- Python nur %LocalAppData%\Programs\Python\Python312\python.exe;
  git über die git.exe von GitHub Desktop, mit -c core.pager=cat,
  commit -m; kein Push.
- dnb-sru.py mit Anführungszeichen in der Abfrage über --% und
  verdoppelte Anführungszeichen aufrufen, Muster:
  python.exe werkzeuge\dnb-sru.py --% "tit=""Sekundo"" and jhr=2019"
- Texte aus PDF mit pdftotext -layout (poppler); geht das nicht,
  PyMuPDF; pypdf nicht (zerlegt Wörter).
- Nichts löschen; verschieben nur mit git mv. Keine Handedits an
  CSV. Kein Katalogeintrag wird geändert.
- Verlags- und Händlerseiten nur lesen: kein Login, keine
  Registrierung, kein Warenkorb, kein Formular.
- PDFs unter hefte/ sind lokal (.gitignore), Textfassungen und
  Fundlisten unter quellen/ werden committet.
- Grenzen sind Zählgrenzen, nie Zeit. Fehlerregel überall: ein
  Abruf oder Schritt, der zweimal scheitert, wird als „offen"
  mit Grund in Standdatei und Bericht eingetragen; der nächste
  Punkt folgt. Nichts wartet auf den Lehrer.
- Standdatei nacht-stand-2026-09-25.md in der Wurzel: je Teil
  eine Zeile „offen / läuft / erledigt" mit dem letzten
  fertigen Punkt; nach jedem fertigen Punkt fortschreiben; ein
  Neustart liest sie zuerst und macht am ersten nicht erledigten
  Punkt weiter.
- README.md ist die Landkarte: jede neue Datei unter quellen/,
  katalog/ oder in der Wurzel bekommt dort einen Satz, im selben
  Commit.

## Teil 1: Inhaltsverzeichnisse ergänzen

Zweck: Teil 2 soll auf allen Regelreihen stehen, die Berliner
und Brandenburger Schüler haben, und die Zeitachse bis Klasse 5
reichen (ziel.md § 5 „Boden").

1. Lambacher Schweizer, Ausgabe Berlin/Brandenburg (Klett;
   die Ausgabe, zu der der Fahrplan 2024 gehört, oder die
   jüngste Landesausgabe): Inhaltsverzeichnisse Klasse 5–10 aus
   der DNB. Datei quellen/quelle-klett-lambacherschweizer-bb-
   inhalt.txt, Kopf wie die anderen Verzeichnisdateien (Reihe,
   Ausgabe, je Klasse IDN, ISBN, Jahr), Trennzeilen
   „== Klasse n ==". Höchstens 12 DNB-Abfragen.
2. Klasse 5 und 6 der Reihen, die im Repo erst ab Klasse 7
   liegen: Sekundo (BE/BB), Mathematik 2023 (BE/BB/ST/TH),
   Schnittpunkt (Differenzierende Ausgabe), Mathematik heute
   (BE/BB), Fundamente der Mathematik Ausgabe B. Je Reihe eine
   neue Datei quellen/quelle-<verlag>-<reihe>-<ausgabe>-kl5-6-
   inhalt.txt (die vorhandenen Dateien bleiben unverändert).
   Höchstens 8 DNB-Abfragen je Reihe. Gibt es für eine Reihe
   keine Klasse 5/6 (Sekundo beginnt in BE/BB in Klasse 7? –
   prüfen, nicht annehmen), steht das als Zeile in der Fundliste.
3. Weitere Regelreihen mit Landesausgabe Berlin/Brandenburg oder
   Zulassung für Berlin/Brandenburg, die im Repo fehlen: prüfe
   mit je höchstens 4 DNB-Abfragen Mathe live (Klett), Fokus
   Mathematik (Cornelsen), Maßstab (Westermann), mathe.delta
   (Buchner), Mathematik Neue Wege SI (Westermann). Gefundene
   Landesausgaben mit Inhaltsverzeichnis: sichern wie in 1;
   ohne Landesausgabe: nur Zeile in der Fundliste, nicht sichern.
4. quellen/lehrwerke-fundliste.md Teil 3 ergänzen (je Reihe und
   Klasse: gefunden/nicht gefunden/nicht erschienen, IDN);
   quellen/quellen.md je neue Datei ein Eintrag nach dem Muster
   der vorhandenen; README.md je neue Datei ein Satz. Commit
   „quellen: Inhaltsverzeichnisse LS BE/BB, Klasse 5/6, weitere
   Reihen".

Gegenprobe Teil 1: Elemente der Mathematik Klasse 5 liegt schon
im Repo (quelle-westermann-elemente-der-mathematik-bb-2016u2025-
inhalt.txt, Ausgabe 2025). Eine neue Abfrage zu dieser Reihe
muss dieselbe IDN liefern; sonst Befund in den Bericht.

## Teil 2: Klassenbelege je Lerneinheit (Sek I)

Schreibe katalog/_klassen-belege.md. Kopf: Titel, Stand (Datum,
Commit des Katalogs), die benutzten Verzeichnisse mit Dateiname
und Klassenumfang, Lesart. Dann ein Zahlenblock, dann je
Sek-I-Eintrag (29, Tabelle Sek I in katalog/index.md) ein
Abschnitt.

Lesart:
- Eine Lerneinheit ist zugeordnet, wenn eine Kapitel- oder
  Unterkapitelzeile eines Verzeichnisses ihren Inhalt nennt.
  Maßgeblich ist der Inhalt, nicht der Wortlaut („Geraden durch
  zwei Punkte" deckt „Gleichung aus zwei Punkten"). Das Zitat
  ist die Verzeichniszeile wortgleich, mit Seite (wenn das
  Verzeichnis eine nennt) und Zeilennummer der Quelldatei.
- Nennt ein Verzeichnis eine Zeile für einen einzelnen Typ der
  Einheit (die Typen stehen im Eintrag unter „Typen je
  Lerneinheit"), steht sie zusätzlich als Typzeile: „Typ:
  <Typname des Eintrags> – <Reihe> Kl. n, S. x: „<Zeile>"".
- Verlagsmarken werden wortgleich mitgenommen: Vertiefen, LVL,
  Sonderfälle, Wissen kompakt, Bleib fit, Diagnosetest, Training
  und alles Weitere, was ein Verzeichnis als Zusatz oder Auswahl
  kennzeichnet. Eine Zeile je Einheit „Marken: …" oder „Marken:
  keine".
- Liegt der Inhalt einer Einheit in zwei Klassen derselben Reihe
  (Einführung in 7, Erweiterung in 8), stehen beide mit Zitat.
- Findet sich für eine Reihe keine Zeile: „keine Stelle" mit dem
  Grund (Reihe führt das Thema in keinem Band; Thema liegt vor
  Klasse 5; Verzeichnis zu grob – nur Kapitel, kein
  Unterkapitel). „keine Stelle" ist ein Ergebnis, kein Mangel.
- Förderhefte: je Einheit eine Zeile „Förderheft: <Reihe> Kl. n:
  „<Zeile>"" oder „Förderheft: keine Stelle" – sie sagen, was
  die Verlage für schwache Schüler als Mindeststoff führen.
- Wo die Zuordnung eine Auslegung verlangt, „Ermessen:" mit
  Grund; nichts wird erfunden.

Je Eintrag:
- „### <datei> – <Verortung des Eintrags, Klassensatz wortgleich>"
- je Lerneinheit: Nummer und Titel; dann je Reihe eine Zeile
  (Oberschulreihen zuerst, dann Gymnasialreihen), Typzeilen,
  Marken, Förderheft.
- Zusammenfassung je Einheit, zwei Zeilen: „OS: Kl. n (Sekundo n,
  Mathematik 2023 n, Schnittpunkt n, Mathematik heute n)" und
  „GYM: Kl. n (LS n, Fundamente n, Elemente n)"; bei Streuung
  die Spanne („Kl. 9–10") und der Grund.
- je Eintrag zum Schluss: „Spanne OS/GYM: ja/nein" (ja, wenn
  irgendeine Einheit bei OS und GYM in verschiedenen Klassen
  liegt), „Boden: ja/nein" (ja, wenn eine Einheit schon in
  Klasse 5 oder 6 liegt), „Ermessen (n):" mit den Fällen.

Zahlenblock oben: Einträge, Lerneinheiten gesamt, davon mit
mindestens einer Stelle in einer OS-Reihe, in einer GYM-Reihe,
in beiden, in keiner; Einträge mit Spanne OS/GYM ja (Liste),
Boden ja (Liste); Typzeilen gesamt; Ermessensfälle gesamt.

Gegenprobe Teil 2 (bekannte Werte; Abweichung ist ein Befund für
den Bericht, kein Grund, die Lesart zu ändern):
- lineare-funktionen, Einheit 4 „Gleichung bestimmen": Sekundo
  Kl. 8, S. 128 „Bestimmen der Funktionsgleichung zu einer
  Geraden durch zwei Punkte" und S. 129 „Schnittpunkt zweier
  Geraden"; Fundamente 2024 Kl. 8 „4.5 Geraden durch zwei
  Punkte" S. 118; Elemente Kl. 8 „2.5.1 Geraden durch zwei
  Punkte" S. 106; Schnittpunkt Kl. 8 Kapitel 3 „Lineare
  Funktionen". Erwartet: OS Kl. 8, GYM Kl. 8, Spanne nein für
  diese Einheit.
- quadratische-gleichungen: Sekundo Kl. 10 „Quadratische
  Gleichungen" S. 45 und „Lösungsformel für quadratische
  Gleichungen" S. 48; Fundamente 2024 Kl. 9 „3.9 Quadratische
  Gleichungen lösen" S. 114 und „3.10 Lösungsformeln" S. 118;
  Lambacher Schweizer Fahrplan Kl. 9 Kapitel II „Quadratische
  Gleichungen". Erwartet: Spanne OS/GYM ja.
- prozentrechnung: LS Fahrplan Kl. 7 Kapitel III „Prozent- und
  Zinsrechnung", Kl. 6 Kapitel I Lerneinheit 4 „Prozente".
  Erwartet: Boden ja (Einheit 1 in Klasse 6).

Grenzen: keine Zählgrenze für die 29 Einträge – alle werden
bearbeitet. Ist ein Verzeichnis für eine Klasse nicht lesbar
(OCR-Bruch), steht „nicht lesbar (Zeilen a–b)" statt einer
Zuordnung.

Abschluss Teil 2: README.md Abschnitt katalog/ eine Zeile für
_klassen-belege.md (Muster: die Zeile zu _niveaustufen-belege.md).
Commit „katalog: Klassenbelege je Lerneinheit aus den
Lehrwerken (Vorschlagsliste)".

## Teil 3: Freie Aufgabensammlungen anderer Länder

Zweck: 22 Sprossenzeilen im Sek-I-Katalog tragen „kein
P10-Original", 15 davon sind Prüfungshöhen (Liste: die Sprossen-
zeilen mit „kein P10-Original" in katalog/_niveaustufen-belege.md;
in den Einträgen selbst kommt die Wendung öfter vor, gemeint sind
nur diese 22). Für sie sollen später Aufgaben aus freien
amtlichen Tests anderer Länder als Decke dienen. Dieser Teil
sichert die Sammlungen und nennt Fundstellen; er bewertet nicht.

1. Sichern, je Sammlung die jüngsten fünf Jahrgänge, Aufgaben
   und Lösungen, PDF nach hefte/fremd/<land>-<sammlung>-<jahr>-
   <stufe>.pdf (lokal), Textfassung nach hefte-md/ ist nicht
   nötig – Text mit pdftotext -layout nach hefte/fremd/…txt
   (lokal, wie Prüfungshefte; Urheberrecht liegt bei den
   Ländern). Quellen, in dieser Reihenfolge, je Sammlung
   höchstens 12 Abrufe:
   a) Bayern, ISB: Jahrgangsstufentests Mathematik Gymnasium
      Jahrgangsstufe 8 und 10, Realschule 6 und 8.
   b) Bayern: Abschlussprüfung Realschule Mathematik I und II;
      Quali Mittelschule Mathematik.
   c) Sachsen: Kompetenztests Mathematik Klasse 6 und 8
      (Oberschule/Gymnasium), soweit frei.
   d) IQB/VERA-8: freie Beispielaufgaben Mathematik.
   e) Ein weiteres Land nach eigener Wahl, wenn a–d weniger als
      20 Dateien ergeben (Baden-Württemberg Realschulabschluss,
      Niedersachsen Abschlussarbeiten).
2. quellen/fremdsammlungen-fundliste.md: je Sammlung Land,
   Herausgeber, Stufe, Jahrgänge gesichert, Adresse, Lizenz-
   oder Urheberrechtsvermerk wortgleich, Umfang (Seiten), ob
   Lösungen dabei sind. Nicht Gefundenes mit Suchbegriffen.
3. Fundstellen für die 22: katalog/_fremdoriginale-belege.md. Je
   Typ (Eintrag, Einheit, Typname, Sprossenzeile wortgleich):
   Aufgaben in den gesicherten Texten, die diesen Typ prüfen –
   Sammlung, Jahr, Aufgabennummer, die Aufgabe in einem Satz
   beschrieben (nicht abgeschrieben), Punktzahl, wenn angegeben.
   Höchstens fünf Fundstellen je Typ, „keine Fundstelle" ist ein
   Ergebnis. Kein Urteil, keine Auswahl.
4. README.md je neue Datei ein Satz; quellen/quellen.md Eintrag
   für die Fundliste. Commit „quellen: fremde Aufgabensammlungen
   gesichert, Fundstellen für Prüfungshöhen ohne Original".

Gegenprobe Teil 3: In Bayern erscheinen die Jahrgangsstufentests
jährlich zu Schuljahresbeginn; die Fundliste muss für Gymnasium
8 mindestens drei Jahrgänge ab 2019 zeigen, sonst Befund.

## Abschluss

- nacht-stand-2026-09-25.md und diesen Auftrag nach archiv/
  verschieben (git mv; bei Namensgleichheit „b" anhängen).
- Bericht nacht-bericht-2026-09-25.md in der Wurzel, README-
  Zeile. Commit „archiv: auftrag-nacht-2026-09-25, Bericht".

## Bericht

nacht-bericht-2026-09-25.md und im Chat. Erste Zeile das Modell.
Teil 1: je Reihe und Klasse gefunden/nicht, Zahl der neuen
Dateien, Gegenprobe. Teil 2: der Zahlenblock; die Liste der
Einträge mit Spanne OS/GYM; die Ergebnisse der drei Gegenproben
im Wortlaut; die fünf häufigsten Verlagsmarken mit Zahl. Teil 3:
Fundliste in Kurzform; Zahl der 22 mit mindestens einer
Fundstelle. Je Teil: offene Punkte mit Grund, eigene
Entscheidungen. Letzte Zeile: „Push origin drücken".
