# BAND-ANLEITUNG – Sammelbände aus den Originalseiten

Version 0.2 · 18.09.2026 · gilt für band-bau.py v0.4 und fhr-band-struktur.py v0.1 ·
anderes Projekt als die Erfassung (liest Katalog und Hefte, ändert nichts)

Änderung gegenüber 0.1 (Auftrag Korpus und OCR, Etappe 0, 18.09.2026): § 5 – band-bau.py
meldet die Reserve in freien Seiten, derselben Größe wie die Abbruchgrenze; die lineare
Jahrgangsschätzung ist gestrichen.

Diese Datei sagt, wie ein Band entsteht, wie ein neues Heft hineinkommt, was die
Strukturliste bedeutet und was die Seitenreserve leistet. Warum es den Band gibt,
steht in konzept.md § 2; wann er neu gebaut wird, in konzept.md § 7 (Schritt 10,
verweist hierher). Bisher gibt es einen Band: fhr (Fachhochschulreife Mathematik
Brandenburg, 16 Hefte 2019–2026). Die Dateien der Sammlung tragen den Familiennamen
`band-` (namensschema.md).

## 1 Was ein Band ist

Ein PDF je Prüfungsart aus den unveränderten Originalseiten der Hefte unter
hefte/<profil>/, in dieser Reihenfolge:

1. Titelblatt (Bandseite 1) mit Hinweisen zur Prüfung, Hinweisen zum Band, der
   Herkunftszeile (Repo, Commit, Stand der Arbeitskopie, Baudatum) und der
   Seitenkarte (Heft → Bandseiten, Offset).
2. Inhaltsverzeichnis (ab Bandseite 2): je Jahrgang die Hefte, je Heft die Abschnitte
   (Deckblatt, Aufgaben, Gutachtenbogen) mit Bandseite und der Seite des
   Erwartungshorizonts.
3. Register: Leitidee → Thema → Typ → Fundstellen „Heft Teilaufgabe: Aufgabenseite
   (EH Seite des Erwartungshorizonts)", kursiv = Vorkommen als Nebentyp. Es entsteht
   aus der Katalogdatei und der Typenliste (§ 6).
4. Reserveseiten (§ 5).
5. Die Hefte, vollständig und in Listenreihenfolge, jede Seite mit einem kleinen
   Aufdruck im oberen Rand: links Heft und Abschnitt, rechts die Marke „▲ Inhalt"
   (Link zum Inhaltsverzeichnis) und „Band S. n".

Bandseite = PDF-Seitenindex (Titelblatt = 1), die Seitenlabels sind entsprechend
gesetzt; die Zahlen aus Inhalt und Register gelten deshalb unmittelbar im Druckdialog.
Heftseite → Bandseite ist je Heft ein fester Offset. Seitenzahlen in gedecktem Blau
sind Sprungmarken (Links ohne Rahmen); Lesezeichen führen zu Titel, Inhalt, Register,
Jahrgängen, Heften und Abschnitten. Ein Rücksprung-Link ist im PDF nicht möglich;
zurück geht es im Betrachter (Acrobat, Edge/Chrome: Alt+Pfeil links; Vorschau: Cmd+ö).

Dazu legt band-bau.py je Heft ein Einzelheft unter baende/<profil>-einzeln/
<jahr>-<papier>.pdf ab – dieselben Seiten mit denselben Aufdrucken, die Seitenlabels
sind die Bandseiten, Lesezeichen je Abschnitt, ohne die Marke (ihr Ziel fehlt dort).
Ein herausgelöstes Heft passt so zum Register.

Alles unter baende/ liegt neben dem Repo und bleibt lokal (.gitignore): es enthält
die Hefte.

## 2 Wie ein Band entsteht

**Laufumgebung.** Python aus LibreOffice (`C:\Program Files\LibreOffice\program\python.exe`,
CLAUDE.md). Die Bibliotheken liegen nicht in der Python-Installation, sondern in einem
pip-Zielordner (`pip install --target <ordner> pypdf reportlab pypdfium2 pillow`), der
beim Lauf im `PYTHONPATH` stehen muss:

- pypdf (Zusammenführen, Lesezeichen, Links, Seitenlabels) – ab 6.19 empfohlen; mit
  6.18 schreibt band-bau.py die Linkziele selbst als Seitenreferenz, der Bau läuft auch.
- reportlab (Titelblatt, Inhalt, Register, Aufdruck; bettet Arial aus
  `C:\Windows\Fonts` ein, sonst Helvetica).
- pypdfium2 und Pillow (Randprüfung: jede Heftseite wird gerendert, bevor der Aufdruck
  gesetzt wird).
- git (für die Herkunftszeile; im PATH oder aus GitHub Desktop, sonst „unbekannt").

Am 18.09.2026 lagen pypdf, pypdfium2 und Pillow im Scratchpad-Ordner der Erfassung
(`…\scratchpad\pylib`), reportlab im Scratchpad-Ordner der Band-Sitzung. **Für einen
späteren Lauf müssen beide Ordner im PYTHONPATH stehen oder die Pakete neu installiert
werden** (`pip install --target`); Scratchpad-Ordner sind nicht dauerhaft.

**Schritte** (Aufruf neben den Quelldateien im Repo):

1. `python fhr-band-struktur.py` – schreibt fhr-band.csv (§ 4). Liest fhr-pruefungen.md
   (Heftliste: Jahr, Buchstabe, Datei, Prüfungsdatum, Seiten, BE), fhr-katalog.csv
   (Startseite und Titel je Aufgabe) und den Seitentext der Hefte unter hefte/fhr/
   (Deckblatt, Aufgabe, Erwartungshorizont, Gutachtenbogen). Prüft: Seitenzahl der Datei
   gegen die Heftliste, Startseite jeder Aufgabe laut Katalog gegen den Seitentext, Zahl
   der Aufgaben im Heft gegen den Katalog; bei Abweichung bricht es ab. Jahrgangs- und
   Heftzeilen einer vorhandenen Liste bleiben erhalten, Abschnittszeilen werden neu
   erzeugt, neue Hefte aus der Heftliste angehängt. Meldungen (etwa Prüfungsdatum vom
   Deckblatt statt aus der Heftliste) stehen am Ende der Ausgabe.
2. `python band-bau.py fhr` – baut baende/fhr-band.pdf und die Einzelhefte. Ausgabe:
   Zahl der Hefte und Heftseiten, Ergebnis der Randprüfung, Seiten von Inhalt und
   Register, Reserve, Zahl der Links und Marken, Seitenkarte, Registerzahlen (Leitideen,
   Themen, Typen, Fundstellen) sowie Katalogzeilen ohne Heft im Band und Typen, die nicht
   in der Typenliste stehen. Das Skript bricht ab, wenn eine Heftdatei fehlt, die Liste
   nicht zur Datei passt, ein Heft nicht A4 hoch ist, der Vorspann nicht reicht (§ 5)
   oder die Seitenkarte nicht mehr auf das Titelblatt passt; nach dem Schreiben liest es
   den Band zurück und vergleicht die Seitenzahl.
3. Ansehen: Titelblatt, eine Inhaltsseite, eine Registerseite, eine Heftseite mit
   Aufdruck; ein Link aus dem Register anklicken. Was zu prüfen ist: Bandseite im
   Aufdruck = Seitenzahl im Betrachter; Registereintrag führt auf die Aufgabenseite;
   Herkunftszeile nennt den Commit, aus dem gebaut wurde.

Der Bau ist kein Commit-Gegenstand: im Repo liegen Skripte, Strukturliste und diese
Anleitung; der Band selbst nicht. Wird nach einem Commit gebaut, nennt die
Herkunftszeile diesen Commit ohne Änderungen – so ist ein Ausdruck später dem Stand
zuzuordnen.

## 3 Wie ein neues Heft hineinkommt

Reihenfolge immer: erst erfassen, dann bauen (§ 6). Für ein neues fhr-Heft:

1. Heft nach hefte/fhr/<jahr>-<papier>.pdf legen (fhr-quellen.md § 5), Zeile in der
   Heftliste fhr-pruefungen.md (Jahr, Buchstabe, Datei, Prüfungsdatum, Seiten, BE), Heft
   mit fhr-bau.py erfassen, Abgleichlauf, Selbstprüfung, Commit – die Jahresroutine in
   konzept.md § 7 bis Schritt 9.
2. `python fhr-band-struktur.py`: das neue Heft wird aus der Heftliste angehängt, hinter
   das letzte Heft seines Jahrgangs (ein neuer Jahrgang bekommt eine neue Ebene-1-Zeile
   am Ende), die Abschnitte kommen aus Katalog und Seitentext. Die Hinweiszeile (Ebene 2,
   Spalte hinweis) wird aus Prüfungsdatum und BE-Verteilung gebildet und danach nicht
   mehr überschrieben.
3. `python band-bau.py fhr`. Ein Jahrgang, der hinten angehängt wird, verschiebt keine
   Bandseite der vorhandenen Hefte: die Hefte beginnen fest bei Vorspann + 1, das
   wachsende Inhaltsverzeichnis und Register füllen die Reserve (§ 5). Nur Register und
   Inhalt sind neu zu drucken, die alten Heftseiten und Einzelhefte bleiben gültig.

Ausnahme: ein Heft eines **älteren** Jahrgangs (etwa ein später gefundener
Nachschreibevorschlag) würde nach der Sortierung mitten in den Band rücken und alle
folgenden Bandseiten verschieben. Wer die gedruckten Seiten behalten will, setzt die
Ebene-2-Zeile des Hefts von Hand ans Ende der Liste (Ebenen 1 und 2 dürfen von Hand
geordnet werden) und vermerkt das in der Hinweiszeile; band-bau.py nimmt die Reihenfolge
der Liste.

Ein Heft, das im Band steht, aber nicht erfasst ist, hat keine Katalogzeilen und
erscheint deshalb nicht im Register (§ 6); band-bau.py verlangt keine Katalogzeilen.
fhr-band-struktur.py dagegen bricht bei einem Heft der Heftliste ohne Katalogzeilen ab,
weil es die Aufgabenabschnitte aus dem Katalog bildet – ein zweiter Grund für die
Reihenfolge erst erfassen, dann bauen.

## 4 Die Strukturliste <profil>-band.csv

Semikolon, alles gequotet, UTF-8, LF – wie die Kataloge. Kopfzeile
`ebene;kennung;titel;datei;von;bis;hinweis`. Seiten sind Heftseiten ab 1, keine
Bandseiten; Ausgabeformat und Seitenzählung des Bands stehen nicht in der Liste, sondern
in KONFIG von band-bau.py.

| Spalte | Ebene 1 Jahrgang | Ebene 2 Heft | Ebene 3 Abschnitt |
|---|---|---|---|
| ebene | 1 | 2 | 3 |
| kennung | `<jahr>` (2019) | `<jahr>-<papier>` (2019-A); Präfix aller Katalog-ids des Hefts | `<heft>-deckblatt`, `<heft>-<aufgabe>` (2019-A-1; Präfix der ids seiner Teilaufgaben), `<heft>-<aufgabe>-eh` (Erwartungshorizont), `<heft>-gutachten` |
| titel | Überschrift im Inhalt und Lesezeichen („Prüfung 2019") | Überschrift („Aufgabenvorschlag A") | Abschnittstitel; bei Aufgaben „Aufgabe n: <titel aus dem Katalog>" |
| datei | leer | Pfad der Heftdatei (hefte/fhr/2019-a.pdf) | leer |
| von, bis | leer | 1 und Seitenzahl der Datei (band-bau.py prüft beides) | erste und letzte Heftseite des Abschnitts |
| hinweis | leer | eine Zeile unter der Heftüberschrift im Inhalt: Prüfungsdatum, Zeit, BE-Verteilung, Hilfsmittel | leer |

Ebenen 1 und 2 sind Hand- und Skriptgut: Reihenfolge, Titel und Hinweiszeile bleiben beim
Neuerzeugen erhalten und dürfen geändert werden. Ebene 3 ist nur Skriptgut: sie wird bei
jedem Lauf von <profil>-band-struktur.py aus Katalog und Seitentext neu erzeugt und
nicht von Hand gepflegt. band-bau.py nutzt die Kennungen: die Aufgabenkennung ist Präfix
der Katalog-ids ihrer Teilaufgaben (2019-A-1 → 2019-A-1a), der Erwartungshorizont einer
Aufgabe heißt `<aufgabe>-eh` und steht im Inhalt auf der Aufgabenzeile.

## 5 Die Seitenreserve

Der Vorspann hat eine feste Länge (KONFIG `vorspann_seiten`, fhr: 13). Titelblatt,
Inhalt und Register füllen ihn von vorn, der Rest sind Reserveseiten mit einem Vermerk;
die Hefte beginnen immer bei Vorspann + 1. Wächst Inhalt oder Register mit einem neuen
Jahrgang, füllt es die Reserve, und die Bandseiten der Hefte bleiben, wie sie gedruckt
sind.

Bemessung (Messung vom 18.09.2026 mit duplizierten Jahrgängen, Typenliste um 30 % je acht
Jahrgänge wachsend): 8 Jahrgänge brauchen 1 + 3 + 4 = 8 Seiten, 16 Jahrgänge 1 + 5 + 7 =
13, 24 Jahrgänge 17. Mit 13 Vorspannseiten sind heute 5 Reserveseiten frei; der Vorrat
trägt acht weitere Jahrgänge (Entscheidung des Lehrers, 18.09.2026: acht statt sechzehn,
fünf Leerseiten statt zwölf). band-bau.py meldet bei jedem Bau, wie viele Seiten Inhalt
und Register brauchen und wie viele Reserveseiten frei sind – dieselbe Größe, an der es
abbricht (Abbruch, sobald keine Seite mehr frei ist). Wie viele Jahrgänge die freien
Seiten tragen, sagt nur die Messung oben; eine lineare Umrechnung im Skript gab es bis
v0.3 und ist gestrichen, weil sie mit „etwa 5 weitere Jahrgänge" der gemessenen acht
widersprach (Seitenrundung und sublineares Wachstum des Registers).

Reicht die Reserve nicht mehr, bricht band-bau.py ab: „Inhalt (n) und Register (m)
brauchen … Seiten, Vorspann hat 13 – KONFIG vorspann_seiten erhöhen (verschiebt alle
Bandseiten)." Dann ist zu entscheiden: `vorspann_seiten` erhöhen – alle Bandseiten der
Hefte verschieben sich um die Differenz, gedruckte Register, Inhalte und Einzelhefte sind
danach veraltet und neu zu drucken; die Seitenkarte auf dem Titelblatt und die Seitenlabels
der Einzelhefte zieht das Skript mit. Ein zweiter Ausweg wäre, den Band zu teilen (ein
Band je Zeitraum), jeder mit eigenem Vorspann. Die Seitenkarte auf dem Titelblatt schaltet
bei mehr Heften auf drei und vier Spalten; passt sie nicht mehr, bricht das Skript ebenfalls
ab (geprüft bis 48 Hefte).

## 6 Regel: Zuordnung in der Erfassung, Register aus der Katalogdatei

Die Zuordnung zu Themen und Typen geschieht in der Erfassung, nicht beim Bandbau. Das
Register entsteht aus der Katalogdatei (<profil>-katalog.csv: id, aufgabe, teilaufgabe,
seite, typ, typ_neben) und der Typenliste (<profil>-typen.csv: Leitidee und Thema je Typ;
band-bau.py ordnet jede Fundstelle nach dem Thema ihres Typs, nicht nach dem Zeilenthema).
band-bau.py erfindet keine Zuordnung, ergänzt keine Fundstelle und legt keinen Typ an;
Typen, die im Katalog stehen, aber nicht in der Typenliste, meldet es und führt sie unter
Leitidee und Thema der Zeile. Ein Heft, das nicht erfasst ist, steht im Band, aber nicht
im Register – seine Seiten sind erreichbar über Inhalt und Lesezeichen, nicht über
Leitidee, Thema oder Typ. Ändert der Abgleichlauf Etiketten, ändert sich das Register erst
beim nächsten Bau. Reihenfolge deshalb immer: erst erfassen (Heft, Abgleichlauf,
Selbstprüfung, Commit), dann Strukturliste erzeugen, dann bauen.

## 7 Änderungen an dieser Datei

- 2026-09-18: angelegt (Nachtrag zum Musterband, Punkt 1); die Regel aus konzept.md § 7
  Schritt 10 steht hier in voller Länge, § 7 verweist hierher.
