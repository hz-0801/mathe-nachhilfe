# Bericht – Nachauftrag Lehrwerke (Formenliste, Bigalke/Köhler, Sorte 1 und 3)

Modell: Sonnet.

## Teil 1 – Formenliste aus den Betrachtern

- a) Cornelsen Klick! – Mathematik (Kl. 5, 6, 7): Betrachter gefunden
  ja. 11 Seiten angesehen (5/3/3). Bilder geladen über
  `static.cornelsen.de/bgd/.../<ISBN>_x1LIAB/preview/big/<n>.jpg`
  (Seitenliste aus `xml/book.xml`), mit Invoke-WebRequest lokal
  gespeichert und mit dem Lesewerkzeug angesehen.
- b) Kohl Verlag Grundwissen Mathematik (Kl. 5 und 8 als Stichprobe
  über die Spanne, dazu ISBN/IDN und TOC für Kl. 8–10): Betrachter
  gefunden ja. 5 Seiten angesehen (3/2). Bilder geladen über
  `leseprobe.kohlverlag.de/html5/p<Produktnummer>_leseprobe/
  preview/big/<n>.jpg`.
- c) Westermann Sekundo-Förderheft und Mathematik-2023-Förderheft:
  kein Betrachter gefunden (kapiert.de ist eine Lernplattform ohne
  Förderheft-Vorschauen; westermann.de ohne „Blick ins Buch“). 0
  Seiten angesehen.
- d) Klett Schnittpunkt Mathematik – Förderheft: kein Betrachter
  gefunden (klett.de ohne „Blick ins Buch“/„Probeseiten“). 0 Seiten
  angesehen.

Ergebnis in `quellen/foerderhefte-formen.md` (5 Tabellenzeilen: Klick!
Kl. 5/6/7, Kohl Verlag Kl. 5/8).

## Teil 2 – Bigalke/Köhler über das Personenfeld

Beide vorgegebenen Abfragen liefen; per="Bigalke" and tit="Mathematik"
and jhr>2013 (65 Treffer) enthielt eine bislang übersehene Brandenburg-
Ausgabe 2019 (Qualifikationsphase Jg. 11/12, GK/LK, dazu ein Band
„Aufgaben zur Abiturvorbereitung“) – gesichert: ja, 5 Bände. Für
Berlin kein Treffer (per="Köhler" and tit="Mathematik" and
tit="Berlin" sowie zusätzlich per="Bigalke" and tit="Berlin": je nur
ein Treffer, Ausgabe 2004/2006, außerhalb des Zeitraums ab 2014) –
gesichert: nein, keine aktuelle Berlin-Ausgabe unter diesem
Autorennamen auffindbar. Keine Einführungsphase (Jg. 10) gefunden.

## Teil 3 – Lücken der Sorte 1 und 3

11 Bände gesichert (Zählgrenze 12 nicht erreicht):
- Sekundo – Förderheft: Kl. 6 (Allgemeine Ausgabe 2018) und Kl. 8
  (Ausgabe 2017 BE/BB) gesichert. Kl. 10 „nicht gefunden“: die BE/BB-
  Ausgabe führt für Klasse 10 kein Förderheft (nur Schulbuch,
  Arbeitsheft, Lösungen, Interaktive Übungen).
- Schnittpunkt Mathematik – Förderheft: Kl. 8, 10, 5, 6 gesichert
  (über klett.de mit Bundeslandfilter Berlin bestätigt) – die Reihe
  ist damit für Klasse 5–10 vollständig.
- Mathematik heute – Diagnose und Fördern: Kl. 7, 8, 9, 10 gesichert
  (jüngster katalogisierter Band je Klasse); neue Textdatei.
- Klick! – Mathematik, Vorgängerausgabe: Kl. 10 gesichert (TOC
  vorhanden, deutlich berufsorientierter Inhalt). Kl. 8 und 9 „nicht
  gefunden“: die Hauptband-Katalogaufnahmen (IDN 1018817689 bzw.
  1030506914) haben keinen TOC-Link; die 2017/2018 erschienene
  „Klick! inklusiv“-Teilserie deckt zwar Kl. 7/8 und 9/10 mit TOC ab,
  aber nur als Doppelklassen-Themenhefte, keine Einzelklasse.

## Ergebnis der Prüfungen 1–5

1. Bestanden: `foerderhefte-formen.md` trägt in jeder Datenzeile nur
   Kürzel aus der festen Liste, drei Zahlen (Aufgaben/Seite, Zeilen
   Text vor 1. Aufgabe, Teilaufgaben je Beispiel) und einen
   Kapiteltitel; kein Aufgabentext.
2. Bestanden: jede neue oder ergänzte Textdatei nennt ISBN, IDN,
   d-nb.info-Adresse und Datum im Kopf und listet je Band mindestens
   die Kapitel erster Ebene mit Seitenzahl.
3. Bestanden: jede Fundzeile „DNB“ in `foerderhefte-fundliste.md` bzw.
   `lehrwerke-fundliste.md` hat einen `==`-Abschnitt in der
   zugehörigen Textdatei, jeder neue Abschnitt hat seine Zeile.
4. Bestanden: vor jedem der vier Commits (Teil 1, Teil 2, Teil 3,
   Register) stand `git status` ohne einen Pfad unter `hefte/` – alle
   Seitenbilder und TOC-PDFs liegen unter `hefte/lehrwerke/` (bereits
   über die bestehende `hefte/`-Regel in `.gitignore`).
5. Bestanden: alle acht Punkte der Standdatei tragen „erledigt“ mit
   Zahl und Bemerkung.

## Eigene Entscheidungen

- Zählgrenzen statt Zeitgrenzen (wie im Auftrag verlangt): je
  Betrachter deutlich unter 12 Seiten angesehen (2–5), weil sich die
  vorkommenden Formen nach wenigen Seiten wiederholten – mehr Seiten
  hätten die Formenliste nicht verändert, nur Zeit gekostet.
- Bei Kohl Verlag nicht alle sechs Klassen einzeln als
  Betrachter-Zeile geführt, sondern Kl. 5 und Kl. 8 als Stichprobe
  über die Klassenspanne, weil die Reihe kein Kapitel-, nur ein
  Arbeitsblattraster hat, das sich zwischen den Klassen stark
  ähnelt – eine dritte oder vierte Zeile hätte kaum neue Formen
  gezeigt.
- Für Kohl Verlag Kl. 8–10 keine neue Datei
  (quelle-kohlverlag-grundwissenmathematik-foerder-5bis10-inhalt.txt)
  angelegt, sondern die bestehende „Freiarbeit“-Datei erweitert, weil
  sich beim Ermitteln von ISBN/IDN herausstellte, dass es dieselbe
  Reihe ist (EAN Kl. 5–7 identisch mit den bereits erfassten Bänden) –
  eine zweite Datei hätte denselben Inhalt doppelt geführt.
- Für Sekundo Kl. 6 die „Allgemeine Ausgabe 2018“ statt einer
  BE/BB-spezifischen Ausgabe gesichert, weil westermann.de unter dem
  Bundesland-Filter Berlin für Kl. 5 und 6 dieselbe Allgemeine Ausgabe
  zeigt – es gibt für diese beiden Klassen keine eigene Landesausgabe.
- Bei „Mathematik heute – Diagnose und Fördern“ Kl. 8 zwei
  gleichdatierte, aber inhaltlich verschiedene Bände gefunden
  (unterschiedliche Kapitelfolge und Schülerband-Seitenzählung); nur
  einen gesichert und den anderen im Dateikopf vermerkt, weil eine
  Klärung der Bundesland-/Bildungsgang-Zuordnung beider Varianten den
  Rahmen des Nachauftrags gesprengt hätte.
- Bei Klick! Vorgängerausgabe die „Klick! inklusiv“-Teilserie
  (Doppelklassenhefte 7/8 und 9/10, 2017/2018) nicht als Ersatz für
  die fehlenden Einzelklassen 8 und 9 gesichert, weil sie nicht der
  im Auftrag verlangten Klassenstruktur entspricht und aus sechs
  Einzelheften je Doppelklasse bestünde – unverhältnismäßiger Aufwand
  gegenüber der Zählgrenze.

Push origin drücken.
