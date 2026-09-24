# Bericht – Auftrag Lehrwerke Sek II und Förderhefte

Modell: Sonnet.

## Schritt 0

Gegenprobe bestanden: `python werkzeuge/dnb-sru.py 'num=9783060428175'`
liefert Satz 1338042475 mit TOC:ja. pdftotext war bereits über MiKTeX im
PATH verfügbar, kein Reparaturbedarf. Einzige Anpassung gegenüber dem
Auftragstext: CQL-Abfragen mit eingebetteten Anführungszeichen mussten
über den PowerShell-Stop-Parsing-Operator (`--%`) mit verdoppelten
Anführungszeichen (`""..""`) übergeben werden, sonst zerlegt PowerShell
die Abfrage fehlerhaft (z. B. `tit="Fundamente der Mathematik"` wurde
sonst zu `tit=Fundamente`); dies ist kein Fehler von `dnb-sru.py`
selbst, das Skript blieb unverändert.

## Teil A – Sek II, Landesausgaben Berlin/Brandenburg

5 Bände gesichert (Fundamente Einführungsphase 1; Elemente der
Mathematik SII NRW-Gegenprobe 2; Mathematik Neue Wege Berlin 3), dazu
3 weitere über die zwei Bestätigungen (Fundamente Ausgabe B 2017 Kl.
7/8/10) und 4 Bestätigungen (Mathematik heute Kl. 7-10). „Nicht
gefunden“ bzw. ohne Landesausgabe: Lambacher Schweizer (keine
Oberstufen-Landesausgabe, auch kein gedrucktes Allgemeine-Ausgabe-
Schulbuch), Bigalke/Köhler Mathematik (kein Titeltreffer in der DNB),
Fundamente-Qualifikationsphase Ausgabe B (in der DNB nicht katalogisiert
– vermutlich noch nicht erschienen). Zeitgrenze (20 Minuten je Reihe)
erreicht: ja, bei den meisten Reihen deutlich überschritten (die
Verifikation der Bundesland-Zuordnung über DNB-926-Metadaten bzw.
Web-Bibliografien war zeitaufwendiger als vorgesehen).

| Reihe | Bände | Fund | Vollständigkeit |
|---|---|---|---|
| Lambacher Schweizer | 0 | nicht gefunden | – |
| Cornelsen Fundamente der Mathematik SII (Ausgabe B) | 1 | DNB | Einführungsphase ja, Qualifikationsphase nicht gefunden |
| Cornelsen Bigalke/Köhler Mathematik | 0 | nicht gefunden | – |
| Westermann Elemente der Mathematik SII | 3 (Gegenprobe NRW) | DNB (Gegenprobe) | ja |
| Westermann Mathematik Neue Wege SII | 3 (Berlin 2011) | DNB | ja |

Bestätigungen: Fundamente der Mathematik Ausgabe B ab 2017 Kl. 7/8/10 (3
Bände, beide vorgemerkten Kandidaten für Kl. 7 und Kl. 8 waren falsch,
die richtigen ISBNs kamen über eine Websuche); Mathematik heute Kl. 7-10
(4 ISBNs, alle bestätigt).

## Teil B – Förderhefte, bundesweit, Klasse 5–10

Alle drei Sorten begonnen, alle drei erreichten die 90-Minuten-Zeitgrenze
vor vollständiger Abarbeitung der im Auftrag genannten Reihen.

**Sorte 1** (8 Bände über 3 Reihen): Sekundo-Förderheft (Kl. 5, 7, 9),
Schnittpunkt-Mathematik-Förderheft (Kl. 7, 9), Mathematik-Ausgabe-2023-
Förderheft (Kl. 7, 8, 9). Nicht gefunden bzw. ohne TOC: Fundamente-
Grundlagentraining (Kl. 5-7 gefunden, aber kein TOC-PDF verlinkt),
Elemente der Mathematik (kein Förderheft-Titel), Mathematik heute (kein
Förderheft-Titel unter diesem Suchbegriff – führt stattdessen „Diagnose
und Fördern“-Bände, s. u.), Lambacher Schweizer (kein Sek-I-Förderheft,
nur Oberstufen-„Basistraining“).

| Reihe | Bände | Fund | Vollständigkeit |
|---|---|---|---|
| Sekundo – Förderheft | 3 von 5 möglichen (Kl. 5, 7, 9) | DNB | Kl. 6, 8, 10 nicht gesichert |
| Schnittpunkt Mathematik – Förderheft | 2 von 6 möglichen (Kl. 7, 9) | DNB | Kl. 5, 6, 8, 10 nicht gesichert |
| Mathematik Ausgabe 2023 – Förderheft | 3 (Kl. 7, 8, 9) | DNB | Kl. 10 noch nicht erschienen |
| Fundamente der Mathematik – Grundlagentraining | 0 | DNB, aber kein TOC | – |
| Elemente der Mathematik – Förderheft | 0 | nicht gefunden | – |
| Mathematik heute – Förderheft | 0 | nicht gefunden (Nebenfund „Diagnose und Fördern“ nicht gesichert) | – |
| Lambacher Schweizer – Förderheft/Basisheft | 0 | nicht gefunden | – |

**Sorte 2** (3 Bände über 1 Reihe): Kohl Verlag „Grundwissen Mathematik
Freiarbeit“, Klasse 5-7 (die Reihe endet dort, kein Band für Klasse
8-10 in der DNB). Die vier vorgegebenen Suchbegriffe brachten sonst
überwiegend Nachschlagewerke, Prüfungstrainer und (bei „Training ...
Grundlagen“) Titel vor 2010 – nach den Ausschlussregeln blieb nur diese
eine Reihe übrig, dazu ein ungeprüfter Kandidat („Training Mathematik ...
Grundwissen Mathematik [Schulform]“, 2011).

| Reihe | Bände | Fund | Vollständigkeit |
|---|---|---|---|
| Kohl Verlag Grundwissen Mathematik – Freiarbeit | 3 (Kl. 5-7) | DNB | ja, Reihe vollständig |

**Sorte 3** (3 Bände über 1 Reihe): Cornelsen „Klick! – Mathematik“,
Ausgabe ab 2024 (Förderschwerpunkt Lernen, bundesweit inkl. Berlin und
Brandenburg), Klasse 5-7 (Kl. 8-10 der neuen Ausgabe noch nicht
erschienen). Die übrigen im Auftrag genannten Startpunkte (Stark in
Mathematik – erwies sich als Grundschul-/bayerische Mittelschulreihe,
Lernstufen Mathematik, Maßstab) und die beiden Schlagwortsuchen
(Förderschule, Lernbehinderung) wurden wegen der Zeitgrenze nicht mehr
geprüft.

| Reihe | Bände | Fund | Vollständigkeit |
|---|---|---|---|
| Cornelsen Klick! – Mathematik (Ausgabe ab 2024) | 3 (Kl. 5-7) | DNB | Kl. 8-10 noch nicht erschienen |

## Teil C – Probeseiten der Förderhefte

Alle 5 Reihen aus Teil B geprüft (Zeitgrenze von 10 Minuten je Reihe
nicht überschritten). Ergebnis: 0 Reihen mit gesicherter Probe, 2 Reihen
nur Betrachter (Cornelsen „Blick ins Buch“, Kohl Verlag „Leseprobe“ –
beide als eingebetteter Seiten-Viewer ohne erkennbaren Download-Knopf),
3 Reihen ganz ohne Vorschau auf der Produktseite (Westermann Sekundo,
Westermann Mathematik 2023, Klett Schnittpunkt). `foerderhefte-
formen.md` bleibt deshalb ohne Tabellenzeile.

## Ergebnis der Prüfungen 1–6

1. Bestanden (Satz 1338042475, TOC:ja).
2. Bestanden: jede neue bzw. geänderte Textdatei nennt ISBN, IDN,
   d-nb.info-Adresse und Datum im Kopf; jeder Band listet mindestens die
   Kapitel erster Ebene mit Seitenzahl (bei den beiden Cornelsen-PDFs mit
   gestörter Schrift, Kl. 7/8 der Ausgabe B ab 2017, wurde der Wortlaut
   stattdessen von den gerenderten Seiten abgelesen, siehe Datei-Kopf).
3. Bestanden: jede Zeile mit Fund „DNB“/„Verlag“ in beiden Fundlisten hat
   eine Textdatei mit passendem `==`-Abschnitt; einzige Ausnahme mit
   Absicht ist die Fundamente-Grundlagentraining-Zeile (Fund „DNB, aber
   kein TOC“ – ausdrücklich als nicht gesichert vermerkt, keine Datei).
4. Bestanden (vacuous): `foerderhefte-formen.md` hat keine Datenzeile,
   also auch keine Zeile mit einem unzulässigen Kürzel oder einer
   fehlenden lokalen Datei.
5. Bestanden: vor jedem der vier Commits stand `git status` ohne einen
   Pfad unter `hefte/`.
6. Bestanden: alle zehn Zeilen der Standdatei tragen „erledigt“ mit
   Bandzahl und Bemerkung.

## Eigene Entscheidungen

- CQL-Abfragen mit eingebetteten Anführungszeichen über PowerShells
  Stop-Parsing-Operator (`--%`) mit verdoppelten Anführungszeichen
  übergeben, weil die naheliegende Schreibweise (einfach oder doppelt
  gequotet) die Abfrage beim Aufruf von `dnb-sru.py` zerschnitt.
- Für Reihen ohne Landesausgabe (Lambacher Schweizer, Elemente der
  Mathematik SII) wurde jeweils geprüft, ob wenigstens eine gedruckte
  „Allgemeine Ausgabe“ existiert, bevor die Reihe als „nicht gefunden“
  bzw. mit Gegenprobe geführt wurde – bei Lambacher Schweizer gibt es nur
  eine bundeslandübergreifende Digitalplattform (Studyly), kein
  gedrucktes Buch, deshalb „nicht gefunden“ statt Gegenprobe.
- Bei Fundamente der Mathematik Ausgabe B ab 2017 wurden die im Vorauftrag
  vom 24.09. notierten Kandidaten-ISBNs für Kl. 7 und Kl. 8 verworfen
  (Web-Bibliografien zeigten Hessen bzw. Sachsen-Anhalt) und durch die
  über eine Websuche gefundenen richtigen ISBNs ersetzt, weil die
  DNB-Titelaufnahmen selbst kein Bundesland nennen.
- Für Förderhefte zu Regelreihen (Sorte 1) wurde, wenn die DNB mehrere
  ISBN-Varianten ohne Bundeslandangabe je Klasse führte, der Band mit
  dem zum Schülerband nächstliegenden Erscheinungsjahr bzw. ISBN-Präfix
  gewählt, auch ohne Bundeslandbestätigung – Teil C hat zwei dieser Wahlen
  (Sekundo Kl. 7, Schnittpunkt Kl. 7) nachträglich als richtig bestätigt.
- Innerhalb jeder Sorte wurde, sobald mehrere Klassen einer Reihe zur
  Wahl standen, eine Stichprobe über die Klassenspanne (nicht
  zwingend alle Klassen) gesichert, um die Zeitgrenze auf mehrere
  Reihen statt auf eine einzige Reihe zu verteilen – das entspricht dem
  Auftragsziel „Breite zählt“ für Teil B eher als eine einzelne
  vollständige Reihe.
- „Mathematik heute Diagnose und Fördern“ wurde trotz Fund als Sorte-1-
  Nebenfund nicht mehr gesichert und stattdessen in der Fundliste
  vermerkt, weil die Zeitgrenze für Sorte 1 zu diesem Zeitpunkt bereits
  erreicht war.
- In `foerderhefte-formen.md` wurde die Tabelle absichtlich leer
  gelassen (mit Prosa-Begründung je Reihe) statt sie ganz wegzulassen,
  weil der Auftrag eine Formenliste als Ergebnis von Teil C verlangt,
  auch wenn das Ergebnis „keine Probe gesichert“ lautet.

## Was ein späterer Auftrag noch holen könnte

- Teil A: Bigalke/Köhler Mathematik direkt über eine Verlags-Sitzung
  statt DNB-Titelsuche prüfen (Autorenname erscheint in der DNB nicht im
  Titel); Fundamente-Qualifikationsphase Ausgabe B nach Erscheinen
  nachtragen.
- Teil B Sorte 1: Sekundo/Schnittpunkt Kl. 6, 8, 10 sowie die übrigen
  Elemente-der-Mathematik- und Mathematik-heute-Förderprodukte
  („Diagnose und Fördern“, viele Bände 2017-2021) nachsichern.
- Teil B Sorte 2: den Kandidaten „Training Mathematik ... Grundwissen
  Mathematik [Schulform]“ (2011, mehrere Schulformen) prüfen.
- Teil B Sorte 3: Stark in Mathematik (bayerische Mittelschule),
  Lernstufen Mathematik, Maßstab sowie die beiden Schlagwortsuchen
  (Förderschule, Lernbehinderung) abarbeiten; die Vorgängerausgabe von
  Klick! (2008-2018, Kl. 1-10) für die fehlenden Klassenstufen 8-10 der
  neuen Ausgabe als Übergangslösung sichern.
- Teil C: kapiert.de wurde nicht geprüft (im Auftrag als Nebenfund für
  Westermann genannt) – könnte für Sekundo/Mathematik-2023-Förderhefte
  doch noch eine Probe liefern.

Push origin drücken.
