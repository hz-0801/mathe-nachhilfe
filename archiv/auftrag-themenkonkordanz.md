# Auftrag: Themenkonkordanz einspielen und prüfen

## Ausgangslage

`themen.csv` liegt neben diesem Auftrag in der Repo-Wurzel. Sie ist die
Themenkonkordanz der Werkstatt (Stufe 0): jede Zeile ordnet ein Thema eines
Prüfungskatalogs einem kanonischen Thema zu. Die Zuordnung ist im Chat
entschieden; dieser Auftrag prüft die Datei gegen die Kataloge, legt das
Prüfskript ab und committet. Die Zuordnung selbst wird nicht verändert.

Aufbau von `themen.csv` (Trennzeichen `;`, alle Felder in Anführungszeichen):

- `kanonisch` – Schlüssel des Themas. Für Sek I der Dateiname in `katalog/`
  ohne `.md`; für Sek II der Themenname aus `abitur/abitur-vokabular.md` als
  Kleinschreibung mit Bindestrichen. Zwei Sek-I-Schlüssel haben keine
  Katalogdatei: `funktionen-allgemein`, `kombinatorik` (Bemerkung nennt es).
- `stufe` – I, II oder I+II.
- `profil` – msa, fhr, abi, iqb; leer bei kanonischen Themen ohne Fundstelle.
- `leitidee`, `thema` – wortgleich wie im Katalog.
- `zeilen`, `typen` – Zahlen aus `werkzeuge/themen-inventar.md`.
- `bemerkung` – frei.

Die Datei wurde aus dem Inventar gebaut, nicht aus den Katalogen. Deshalb
die Prüfung.

## Schritte

1. Lege `werkzeuge/themen-pruef.py` an. Läuft aus der Repo-Wurzel, liest
   `themen.csv` und die fünf Katalogdateien (`msa/msa-katalog-basis.csv`,
   `msa/msa-katalog-kontext.csv`, `fhr/fhr-katalog.csv`,
   `abitur/abi-katalog.csv`, `abitur/iqb-katalog.csv`; msa-Basis und
   msa-Kontext zusammen ein Profil), ändert keine Datei und prüft:
   - Jedes Paar (leitidee, thema) jedes Profils steht genau einmal in
     `themen.csv`, und jede Profilzeile in `themen.csv` hat ein Gegenstück im
     Katalog.
   - `zeilen` und `typen` stimmen mit der Zählung aus dem Katalog überein
     (Typen = verschiedene Werte in `typ`).
   - Jede Datei `katalog/*.md` ohne führenden Unterstrich und ohne `index.md`
     kommt als `kanonisch` vor, und jeder `kanonisch` mit Stufe I hat eine
     Katalogdatei, außer `funktionen-allgemein` und `kombinatorik`.
   - Jeder `kanonisch` mit Stufe II ist ein Thema aus
     `abitur/abitur-vokabular.md` (gleiche Umschrift wie oben) oder hat eine
     abi/iqb-Zeile mit diesem Thema.
   Ausgabe: je Prüfung bestanden oder die Abweichungen, Rückgabewert 0 nur
   wenn alles besteht.

2. Führe das Skript aus. Besteht eine Prüfung nicht, ändere `themen.csv`
   nicht; berichte die Abweichungen wörtlich.

3. Trage in `README.md` ein: unter „Wo fange ich an" eine Zeile für
   `themen.csv` (Themenkonkordanz: kanonisches Thema je Katalogthema, alle vier
   Profile; nach jeder Katalogänderung `python werkzeuge/themen-pruef.py`),
   unter `werkzeuge/` eine Zeile für `themen-pruef.py`.

4. Ergänze in `konzept.md` § 3 am Ende einen Absatz: Die Themenkonkordanz
   `themen.csv` verbindet die Themennamen der vier Prüfungskataloge mit den
   Einträgen des Themenkatalogs. Regel: Ein Sek-I-Thema ist kanonisch, wenn
   Sek II denselben Stoff fortführt (Daten, Wahrscheinlichkeit, LGS); ein
   Sek-II-Thema bleibt eigen, wenn es ein neues Konzept einführt. Sonst nichts
   ändern.

## Prüfungen

`git status` zeigt nur `themen.csv`, `werkzeuge/themen-pruef.py`, `README.md`,
`konzept.md` und die Verschiebung des Auftrags. Kataloge, Typenlisten,
Profildateien und `werkzeuge/themen-inventar.*` unverändert.

## Abschluss

Verschiebe diese Auftragsdatei nach `archiv/auftrag-themenkonkordanz.md` und
committe alles in einem Commit.

## Regeln

- Ändere `themen.csv` nicht, auch nicht bei Abweichungen.
- Ändere keine Katalog-, Typen- oder Profildatei.
- Lösche nichts; Verschieben statt Löschen.
- Rate nicht bei Unklarheiten: brich ab und berichte.

## Bericht

Kurz: Ergebnis je Prüfung; bei Abweichungen die Zeilen wörtlich; geänderte
Dateien; Commit.

Letzte Zeile des Berichts: Push origin drücken
