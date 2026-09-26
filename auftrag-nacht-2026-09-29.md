# Auftrag Nacht 2026-09-29: Urteile vom 26.09. umsetzen, Abitur
# nachtragen, Katalogvorschläge vorbereiten

Modell: Opus. Läuft ohne den Lehrer: keine Rückfrage, Standdatei,
Commit je Teil, Fehlerregel je Teil. Ordner: mathe-nachhilfe.
In ../blattbau läuft keine Sitzung; du liest dort, schreibst dort
nichts.

## Ausgangslage

Der Chat vom 26.09. nachmittags hat fünf Urteile gefällt; ihr
Wortlaut steht in beschluss-2026-09-26.md (Datei 2 dieses
Auftrags, liegt in der Wurzel). Dieser Auftrag legt sie ab
(Teil 1), setzt die Abitur-Urteile um (Teil 2–4), stellt einen
Sollwert um (Teil 5), zieht einen Merkkasten nach (Teil 6) und
baut für die offenen Katalogbefunde Vorschlagsdateien, über die
der Chat morgen entscheidet (Teil 7–8). Du änderst keinen Prompt,
nichts unter blaetter/, keinen Katalogeintrag außer in Teil 4
(Sek-II-Typen) und Teil 6 (ein Merkkasten).

## Regeln

- Shell PowerShell: kein Heredoc, kein sed. Dateien schreiben mit
  [System.IO.File]::WriteAllText(pfad, text,
  (New-Object System.Text.UTF8Encoding($false))); Zeilenenden LF;
  nach dem Schreiben prüfen (keine BOM, kein CR).
- Python nur %LocalAppData%\Programs\Python\Python312\python.exe;
  git über die git.exe von GitHub Desktop, mit -c core.pager=cat;
  Commit-Nachrichten mit Umlaut über commit -F aus einer
  UTF-8-Datei, nie -m; kein Push.
- pdftotext und pdfinfo unter
  %LocalAppData%\Programs\MiKTeX\miktex\bin\x64. hefte/ ist lokal.
- Nichts löschen; verschieben nur mit git mv. Keine Handedits an
  CSV, die ein Bauskript schreibt.
- Grenzen sind Zählgrenzen, nie Zeit. Fehlerregel überall: ein
  Schritt, der zweimal scheitert, wird als „offen" mit Grund in
  Standdatei und Bericht eingetragen; der nächste Punkt folgt.
- Standdatei nacht-stand-2026-09-29.md in der Wurzel: je Teil eine
  Zeile „offen / läuft / erledigt" mit dem letzten fertigen Punkt
  und dem Commit; Uhrzeiten nur aus Get-Date; ein Neustart liest
  sie zuerst.
- Gegenproben: Der bekannte Wert steht mit seiner Belegdatei
  dabei. Weicht die Gegenprobe ab, schreib die Abweichung mit
  Erklärung in den Bericht und ändere das Skript nicht.
- README.md ist die Landkarte: jede neue Datei bekommt dort einen
  Satz, im selben Commit. faellig.md: erledigte Posten im selben
  Commit in § 2 streichen und mit Datum in § 4 eintragen; neue
  Posten eintragen statt sie im Bericht zu lassen.
- Skripte gehören mit allen Daten ins Repo. Hilfsagenten, die
  dieselben Dateien anfassen, laufen nacheinander.
- Urteil bleibt beim Chat: Wo dieser Auftrag „Vorschlag" sagt,
  schreibst du in die Vorschlagsdatei, nie ins Ziel.

## Teil 1: Beschlüsse ablegen

1. README-Zeile für beschluss-2026-09-26.md (Block Wurzel, neben
   befund-testlauf-2026-09-25.md).
2. befund-testlauf-2026-09-25.md: unter „Beschluss" Punkt 2 und
   unter „Prompt" Punkt 26 je eine Zeile „Nachtrag 26.09.:
   vertagt, siehe beschluss-2026-09-26.md Punkt 1" anhängen;
   sonst nichts an der Datei.
3. faellig.md: Posten „Übersichtsblatt: Form an den Prüfsteinen
   entscheiden" erledigt (§ 4, Ergebnis: vertagt); neuer Posten
   in § 2 nach beschluss-2026-09-26.md Punkt 1, Auslöser „nach
   dem Testlauf v4.4". Posten „einsortieren.py um die Sorte
   uebersicht erweitern" bekommt den Zusatz „ruht bis zum neuen
   Prüfstein".

Commit „beschluss: Urteile vom 26.09. nachmittags".

## Teil 2: Deutungsliste (f) und Posten Eichung 2017

beschluss-2026-09-26.md Punkt 2.

1. abitur/iqb.md § 7: Eintrag (f) an die Deutungsliste, Wortlaut
   aus Punkt 2 des Beschlusses, mit den fünf Belegen aus
   iqb-pruefungen.md § 4 (Zeilen um „Mindestanzahl oder
   Mindestumfang für eine Mindestwahrscheinlichkeit"); Kopf der
   Datei: Version hochzählen, Änderungszeile. Der zweite Kandidat
   („vom Text verlangte Fallunterscheidung ist amtlich II") wird
   nicht aufgenommen; iqb-pruefungen.md § 4 vermerkt an beiden
   Kandidaten den Stand.
2. Bestand prüfen: alle Poolzeilen in iqb-katalog.csv, auf die (f)
   zutrifft (Typ oder Aufgabentext: Mindestanzahl, Mindestumfang,
   „mindestens … Wahrscheinlichkeit", Gegenereignis mit
   Ungleichung für n). Liste mit id, Schätzung, amtlichem
   Bereich. Weicht eine Schätzung von (f) ab, wird sie über den
   Weg korrigiert, den iqb.md § 7 für Korrekturen vorsieht
   (bemerkung mit Grund), nicht von Hand in der CSV.
3. iqb-bau.py Selbstprüfung laufen lassen; Eichung Bestand vorher
   und nachher in den Bericht.
4. faellig.md: Posten „Eichung Pool 2017 grundlegend prüfen"
   erledigt, Ergebnis aus Punkt 2 des Beschlusses (ein Satz).

Gegenprobe Teil 2 (abitur/befund-eichung-2017-2026-09-28.md,
Abschnitt „Eichung je Pooljahr"): Bestand vorher 1526 von 1638
gewerteten Zeilen; iqb-pruefungen.md § 4: (f) hat fünf Poolfälle,
alle amtlich III.

Commit „abitur: Deutungsliste (f), Eichung 2017 geschlossen".

## Teil 3: Delta-Stapel 2018-ea-B (CAS) erfassen

beschluss-2026-09-26.md Punkt 2. Arbeitsstand unter
abitur/arbeitsstand/2018-ea-B-cas/ (schaetzungen.md, typwahl.md,
landesheft-abgleich.md, eichung.py).

1. Die 85 Schätzungen gegen (f) prüfen und nur dort ändern, wo (f)
   greift; Grund in bemerkung. Keine andere Schätzung ändern.
2. Eichung messen. Erreicht der Stapel die Schwelle (85 %, 73 von
   85): normal erfassen.
3. Erreicht er sie nicht: erfassen mit dokumentierter
   Unterschreitung. Die Schwelle bleibt 85 % für alle Stapel.
   Umsetzung: eine Liste in iqb-bau.py (etwa
   EICHUNG_UNTERSCHRITTEN), in der nur dieser Stapel steht, mit
   Wert und Verweis auf beschluss-2026-09-26.md; die Selbstprüfung
   meldet ihn als Warnung, nicht als Fehler. Begründung in
   iqb-pruefungen.md § 5 und iqb.md § 7 (ein Absatz: erfasst mit
   Unterschreitung, Beschluss vom 26.09., Schwelle unverändert).
   Das ist keine Wiedereinführung der Überschreibung je Stapel
   aus v1.4; sag das im Absatz.
4. Vormerkung schließen: 2018-bb-ea-cas-B3.1f auf „Dublette von:"
   bzw. „Abgewandelt von:" mit der Pool-id; die WTR-Zeilen
   2018-bb-ea-B3.1 a–f bekommen den Verweis auf
   2018MerhoehtBAGLAA2CAS1 (a, b, d, e wortgleich, c und f
   abgewandelt; c mit anderer Punktzahl „Dublette von:" mit
   BE-Vermerk nach abi.md § 7). Abgleichlauf abitur-abgleich.py,
   Selbstprüfung beider Bauskripte.
5. faellig.md: Posten „Pool-Vormerkung 2018 schließen" erledigt.

Gegenprobe Teil 3 (nacht-bericht-2026-09-28.md Teil 2,
befund-eichung-2017 Abschnitt 2018-ea-B): 85 Zeilen, erster Stand
57, nach Prüfung 67 von 85; danach grep „Poolaufgabe (nicht
erfasst)" über abitur/abi-katalog.csv: 0 Treffer; Typenzahl
vorher 1393 (Abgleichlauf 25).

Commit „abitur: Delta-Stapel 2018-ea-B (CAS) erfasst, Vormerkung
2018 geschlossen".

## Teil 4: Nachtrag Berliner CAS-Hefte 2017/2018

beschluss-2026-09-26.md Punkt 3; Messung und Art je Teilaufgabe in
abitur/befund-cas-berlin-2026-09-28.md; Nachtragsmodus abi-bau.py
(abi.md § 7). Hefte: 2017-be-gk-cas, 2017-be-lk-cas,
2018-be-gk-cas, 2018-be-lk-cas.

1. Eigene Zeile für jede abweichende Teilaufgabe mit der Art
   Werkzeug, Auftrag, Zuschnitt oder ganze Aufgabe (auch in
   Kombination mit Zahl oder BE).
2. Art nur BE oder nur Zahl (auch beides zusammen): Zeile mit
   „Dublette von:" auf die WTR-Zeile, mit BE- bzw. Zahlvermerk,
   wie abi.md § 7 es für abweichende Punktzahl vorsieht.
3. Teilaufgaben, die schon Zeile eines Brandenburger CAS-Hefts
   sind (Befund: 2017-be-lk-cas 9, 2018-be-lk-cas 13): keine neue
   Zeile, Verweis nach abi.md § 7.
4. Teilaufgaben der Berliner LK-Aufgaben, deren WTR-Fassung keine
   Zeile hat (2017-be-lk 1.1, 2.1, 3.1; 2018-be-lk 2.2, 3.1):
   nicht erfassen; neuer Posten in faellig.md § 2 („eigene
   Aufgaben der Berliner LK-Hefte 2017/2018, WTR und CAS").
5. abi.md § 7 und § 9: die Abgrenzung für die Berliner CAS-Hefte
   als entschieden eintragen (Regel aus Punkt 1–3, Verweis auf
   beschluss-2026-09-26.md); Version hochzählen.
6. Abgleichlauf abitur-abgleich.py (Typen), Selbstprüfung.
7. Sek-II-Einträge nachziehen für die neuen Zeilen dieses Teils
   und die aus Teil 3, Vorgehen wie Nacht 28.09. Teil 4 (je Zeile
   über themen.csv zum Eintrag, Typ in die passende Einheit,
   Original in „Prüfungsform" mit id; neue Einheit nur als
   Vorschlag in katalog/_vorschlaege-2026-09-29.md); danach
   katalog/_pruef_katalog.py.

Gegenprobe Teil 4 (abitur/befund-cas-berlin-2026-09-28.md,
Übersicht): abweichende Teilaufgaben je Heft 16, 19, 16, 16; davon
nur BE 5, 9, 2, 7; schon Zeile eines BB-CAS-Hefts 0, 9, 0, 13.
Neue eigene Zeilen je Heft in den Bericht. Kennzahl 5 vor dem Teil
28 (nacht-stand-2026-09-28.md, Teil 4); „Zeilensumme ≠ themen.csv"
danach 0 Einträge.

Scheitert ein Heft zweimal: offen mit Grund, nächstes Heft.

Commit je Heft „abitur: Nachtrag <papier>"; Commit „katalog:
Sek-II-Einträge auf den CAS-Nachtrag".

## Teil 5: marken-bau.py Sollwert kreis 1

beschluss-2026-09-26.md Punkt 4. GEGENPROBE-Zeile kreis 1 Typ
„Kreis mit gegebenem Radius oder Durchmesser zeichnen": Soll
„[OS 5–8, GYM 5–6]", Quelle im Skriptkopf (bericht-marken.md
Gegenprobe 4). Skript laufen lassen, `--probe` muss „nichts zu
ändern" melden. faellig.md: Posten „marken-bau-Gegenprobe
kreis 1" erledigt.

Gegenprobe Teil 5: alle GEGENPROBE-Zeilen melden „stimmt".

Commit „werkzeuge: marken-bau Sollwert kreis 1".

## Teil 6: Merkkasten quadratische-gleichungen

befund-testlauf-2026-09-25.md, Abschnitt „Katalog" Punkt 1:
Schreibform der Nullstellengleichung „0 = f(x)" – der Term bleibt,
wo er stand –, nicht „f(x) = 0 umgestellt". Nur die betroffenen
Zeilen im Merkkasten von katalog/quadratische-gleichungen.md und,
falls dort dieselbe Schreibweise steht, von
katalog/quadratische-funktionen.md. Änderungszeile im Kopf des
Eintrags. faellig.md: Posten erledigt.

Gegenprobe Teil 6: grep „f(x) = 0" in beiden Merkkästen vorher
und nachher, Zahlen in den Bericht; katalog/_pruef_katalog.py
ohne neuen Fehler.

Commit „katalog: Merkkasten Nullstellengleichung 0 = f(x)".

## Teil 7: Vorschläge Sprossenregel

befund-testlauf-2026-09-25.md, „Katalog" Punkt 2: Vorformen (der
Grundfall der zuerst gelernten Form) stehen vor dem
Universalverfahren; Abkürzungen (Satz vom Nullprodukt,
Ausklammern, fehlendes Absolutglied) stehen danach als Sprosse
„schneller, wenn …".

Prüfe jeden Sek-I-Eintrag unter katalog/ (Grenze: die Einträge,
die katalog/_klassen-belege.md als Sek I führt; höchstens diese).
Je Lerneinheit mit Sprossenkette: folgt sie der Regel? Wo nicht:
eine Zeile Eintrag · Einheit · jetzige Folge · vorgeschlagene
Folge · Grund. Datei katalog/_vorschlaege-sprossen-2026-09-29.md;
vorne eine Zählzeile (Einträge geprüft, Einheiten geprüft,
Vorschläge). Kein Eintrag wird geändert.

Gegenprobe Teil 7: quadratische-gleichungen muss einen Vorschlag
oder eine Bestätigung zu Wurzelziehen, p-q-Formel und Satz vom
Nullprodukt tragen (Befund Eingabe 7).

Commit „katalog: Vorschläge Sprossenregel".

## Teil 8: Vorschläge Katalogbefund 3–8

befund-testlauf-2026-09-25.md, „Katalog" Punkt 3–8. Je Punkt ein
Abschnitt in katalog/_vorschlaege-2026-09-29.md (dieselbe Datei
wie Teil 4 Punkt 7, eigener Abschnitt): was fehlt oder
widerspricht, im Wortlaut des Eintrags; der Vorschlag als fertige
Katalogzeile(n) im Format des Eintrags; Beleg je Zeile (Prüfungs-
id aus msa/fhr/abitur, Lehrwerksstelle aus _klassen-belege.md,
Rahmenlehrplan unter quellen/). Ohne Beleg: Zeile „kein Beleg
gefunden", kein Vorschlag. Punkt 9 (Skizzen) entfällt, er hängt am
vertagten Übersichtsblatt.

Gegenprobe Teil 8 (katalog/daten.md, Befund Punkt 5): die
Abweichung „Spannweite [OS 9]" gegen Einheitsmarke OS 6 muss mit
beiden Fundstellen aus _klassen-belege.md im Abschnitt stehen.

Commit „katalog: Vorschläge Katalogbefund 3–8".

## Abschluss

- faellig.md nachführen (neue Posten aus Teil 4 und 7–8: „Urteil
  im Chat" mit Verweis auf die Vorschlagsdateien).
- nacht-stand-2026-09-29.md und diesen Auftrag nach archiv/
  verschieben (git mv; bei Namensgleichheit „b" anhängen).
- Bericht nacht-bericht-2026-09-29.md in der Wurzel, README-Zeile.
  Commit „archiv: auftrag-nacht-2026-09-29, Bericht".

## Bericht

nacht-bericht-2026-09-29.md und im Chat. Erste Zeile das Modell.
Je Teil: was geändert ist (Dateien, Zahlen), die Gegenprobe im
Wortlaut mit Belegdatei, eigene Entscheidungen, offene Punkte mit
Grund. Teil 2: Zeilen, auf die (f) zutrifft, und Eichung Bestand
vorher/nachher. Teil 3: Eichung nach (f), erfasst normal oder mit
Unterschreitung, Typen vorher/nachher. Teil 4: je Heft neue eigene
Zeilen, Dubletten, Verweise, neue Typen; Kennzahl 5 vorher/
nachher. Teil 7 und 8: die Zählzeilen. Letzte Zeile: „Push origin
drücken".
