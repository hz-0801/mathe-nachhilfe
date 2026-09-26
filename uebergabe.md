# Übergabe verbessereBlaetter – 2026-09-26 (Chat vom 26.09.)

Vorherige Übergabe: archiv/uebergabe-2026-09-25-abends.md.

## 1 Ziel

Der bestmögliche Themenkatalog und die beiden Prompts, damit
erzeugeUnterrichtsblatt() und erzeugePrüfungsblatt() aus wenigen
Wörtern druckfertige Blätter bauen. Maßstab ist ziel.md
(Stand 25.09.2026).

## 2 Arbeitsgrundlage

- ziel.md (25.09.2026), unverändert.
- befund-testlauf-2026-09-25.md (Wurzel, seit Nacht 28.09. Teil 1):
  alle Befunde des Testlaufs v4.3 – Lesebefunde des Lehrers an
  Eingabe 7 (Fokus, ganz) und Eingabe 3 (schwach, S. 1–6), dazu
  die aus Bericht und Lesezettel –, sortiert nach Ziel: Prompt
  (26 Punkte → v4.4), Vorlage (Stufe 6/7), Katalog (9), Werkzeug
  (4), Beschluss (6). Das ist die Quelle für v4.4; nichts davon
  wird hier wiederholt.
- blattbau: unterrichtsblatt.md v4.3 (512ae78; Projektanweisung
  ist v4.3); mathblatt.sty Stufe 6, Version 2026-09-28a (cad91ae)
  mit Anleitung_mathblatt.md und referenz/probeblatt.pdf (154
  Bausteine, 12 Seiten; referenz/probeblatt-pruef.py). Berichte
  bericht-vorlage-stufe5-2026-09-27.md und -stufe6-2026-09-28.md.
  Neue Namen, die v4.4 nennt: \zweigzeile, \verzeichniszeile mit
  \verz, abhakseite mit \abhak/\abhakgruppe/\abhakauto,
  \einheitenkopf[ziel][kurzform]{…}, \verfahren, \anweisung,
  \rechenplatz{n} (12 mm je Zeile, [halb]), Umgebung beispiel,
  \streifenleer[0], \streifenfeld, \swz/\swa/\swb/\swfrage.
- Katalog: Marken-Zeilen in allen Einträgen (273 Zeilen, 262
  Typklammern; Belegskripte seit 27.09. auf potenz 5, daten 7 und
  die Klassen-Typen umgestellt, FHR-Wort an einheiten 1/3/4 und
  daten 1/4); Vorrat-Verweise auf gost-*/fos-* umgestellt;
  katalog/_vorschlaege-2026-09-27.md (312 Zeilen, vier
  Abschnitte: Ausbau potenz 5 und daten 7, Niveaustufe G,
  2025-GYM-K5d, 28 Namensabweichungen) – Vorschläge, nicht
  entschieden.
- Abitur: Stapel 2017-ea-B WTR und CAS erfasst, Abgleichlauf 25,
  Typen 1393 (Zahlen in nacht-bericht-2026-09-28.md Teil 2).
  2018-ea-B CAS nicht erfasst (Eichschwelle zweimal verfehlt);
  Arbeitsstand unter abitur/arbeitsstand/2018-ea-B-cas/; eine
  Vormerkung bleibt (2018-bb-ea-cas-B3.1f).
- Befunde zum Urteil: abitur/befund-cas-berlin-2026-09-28.md
  (abweichende Teilaufgaben je Heft 16, 19, 16, 16),
  abitur/befund-eichung-2017-2026-09-28.md, Übersichtsblatt-
  Prüfsteine blaetter/uebersicht/quadratische-funktionen/ und
  /prozentrechnung/ (je 1 Seite, PNG neben dem PDF).
- Berichte: nacht-bericht-2026-09-27.md (zehn Teile),
  nacht-bericht-2026-09-28.md (sieben Teile, sechs fertig; im Chat
  gelesen, Urteile offen).
- Testlauf: blaetter/testlauf-2026-09-25/ (eingefroren),
  bericht-testlauf-2026-09-25.md, werkzeuge/testlauf-auftrag.md
  (Vorlage für den nächsten Lauf: nacheinander, Get-Date,
  Regelweg claude -p zuerst), werkzeuge/testlauf-eingaben.csv.
- Weiter gültig: katalog/_klassen-belege.md,
  _pruefungswort-belege.md, _sek2-ordnung-belege.md,
  _klassen-ermessen.md, bericht-marken.md; werkzeuge/blatt-pruef.py
  (v0.4, zählt Schwach-Bausteine, Kennzahlen 13–17 für Stufe 6).
- Katalog Sek II: alle Katalogzeilen vom 27./28.09. zugeordnet
  (39 Einträge, 74 neue Typen); Kennzahl 5 = 28 (Rest msa/fhr).

## 3 Arbeitsstand

Abgeschlossen: Nacht 27.09. (alle zehn Teile: Belegskripte,
FHR-Wort, potenz 1 ohne Vorrat, Kleinposten, Vorrat-Verweise,
cosh gesichert, Vorschläge, Prüfskript v0.3, CAS-Nachträge bb-ea,
Stapel 2017 und 2017-be-gk mit Abgleichlauf 24); Vorlage Stufe 5
und Stufe 6; Auswertung des Testlaufs an zwei Blättern mit dem
Lehrer, Befunde als Datei; Beschluss „270 Paare ohne
Gegenrichtung" geschlossen (kein Bedarf).

Abgeschlossen außerdem: Nacht 28.09. (Befund abgelegt, Stapel
2017-ea-B, Befund Berliner CAS-Hefte, Sek-II-Einträge
nachgezogen, Prüfskript v0.4, marken-bau-Sollwerte, Befund
Eichung 2017, Prüfsteine Übersichtsblatt); Projektanweisung
Stand 27.09.b (Modellwechsel ansagen, Web-Sitzungen).

Nicht begonnen: v4.4; Testlauf mit v4.4; Blatt-Chat; Urteile zu
_vorschlaege-2026-09-27.md.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Aus früheren Übergaben gelten weiter: Marke = Klasse je Schulform
aus den Lehrwerken; Klasse und Schulform ordnen, filtern nicht;
Zweigzeile Fertigkeit · Zeitmarke · Prüfungswort; Prüfungswort-
Schwelle 7 von 13; Ich-kann-Titel; schwach ändert die Form;
Bestellung „nur das Neue / mit Wiederholung / mit Ausblick";
Regel A und B der Marken; Testlauf ist der Regeltest je Version,
ein Blatt-Chat je Version danach; Zwei Sitzungen im selben
Ordner: nur eine schreibt; Cloud-Sitzungen nur für Repo-und-Netz.

Neu (26.09.), Wortlaut in befund-testlauf-2026-09-25.md Abschnitt
„Beschluss": Blatt liefert Aufgaben, Platz und Reihenfolge –
Erklären, Beispiel und Gerüst sind Sache des Lehrers (kein
gedrucktes Beispiel, kein gedrucktes Gerüst; Rechenplatz 12 mm;
„mit beispiel" auf Zuruf); Übersichtsblatt je Thema für den
Lehrer aus den Merkkästen, Bestellwort „mit übersicht", Prüfstein
in Nacht 28.09.; „Das kennst du schon" bleibt, Nummern laufen
durch; Struktur Einheit → Verfahrensüberschrift → Hauptnummer,
keine Verzeichnisseite; Zone prüft Fertigkeiten in der Form, die
das Blatt braucht (Klammer auflösen + zusammenfassen bleibt eine
Aufgabe).

Weitere Festlegungen 26.09.:
- Vorlage: die Namen der Stufe 5/6 sind fest; v4.4 nennt sie, statt
  Bausteine je Lauf bauen zu lassen. Jede Stufe muss das
  Probeblatt kompilieren und erweitern.
- marken-bau.py: die Gegenprobe-Sollwerte vom 26.09. waren falsch;
  die Belegwerte gelten (lineare-funktionen 4 „P10", quadratische-
  gleichungen 2 „GYM Kl. 8–9"); Nacht 28.09. Teil 5 stellt sie um.
- CAS-Vormerkungen werden nach der Delta-Regel geschlossen
  (Delta-Stapel aus den nicht wortgleichen CAS-Dateien; Muster
  2026-ea-B-mms), nicht durch eine neue Vormerkungsform.
- Sek II im Prompt: das Halbjahr ordnet; „kennst du seit Q1" ist
  Zeitmarke, kein Zweig fällt in die Zone (Befund Prompt 20).
- Sprossenregel für den Katalog: Vorformen vor dem Universal-
  verfahren, Abkürzungen danach (Befund Katalog 2); Prüfung je
  Eintrag beim nächsten Katalogauftrag.
- Ein Nachtauftrag darf in das Nachbar-Repo schreiben, wenn dort
  keine zweite Sitzung läuft; „nur lesen" gilt nur bei parallelen
  Sitzungen. Je Nachricht ein Auftrag.

## 5 Offene Punkte und verworfene Ansätze

Offen (Urteil im Chat, Material liegt oder kommt):
- Aus nacht-bericht-2026-09-28.md fünf Urteile: Form des
  Übersichtsblatts (zwei Prüfsteine); 2018-ea-B CAS (dokumentiert
  unter Schwelle erfassen, Schwelle begründet ändern, Deutungs-
  liste erweitern oder Vormerkung stehen lassen); Abgrenzung der
  Berliner CAS-Hefte; Eichung Pool 2017 (erste Läufe aller
  2017/2018-Stapel bei 62–70 %: eher Jahrgangseigenheit als
  Fehler); Sollwert „kreis 1 Typ" in marken-bau.py.
- _vorschlaege-2026-09-27.md: vier Abschnitte entscheiden; danach
  Katalogauftrag (Einträge potenz 5, daten 7; Niveaustufe G;
  GYM-K5d; Namensabweichungen; Merkkasten quadratische-gleichungen
  „0 = f(x)"; Befund Katalog 3–8; Skizzenbeschreibung im
  Merkkasten).
- Prompt-Punkte, die v4.4 nicht trägt, weil der Katalog fehlt:
  Skizzen (Katalog hält keine Abbildung).
- Vorlage Stufe 7 (Posten faellig.md).
- Fundamente B Qualifikationsphase: DNB fand nichts; Quelle beim
  Lehrer oder Verlag.
- Testlauf-Auftrag: Regelweg claude -p noch nie gelaufen; erster
  Lauf mit v4.4 zeigt, ob der Ersatzweg (Sub-Agenten) bleibt.
- Prüfungsheft: Umbau nach v4.4-Muster, Schwelle „selten";
  Verschmelzung der Prompte danach prüfen.
- Förderhefte (Prüfstein-Befund, wenn gekauft); Fotos der
  Inhaltsverzeichnisse (etwa 10.10.); Berlin 2026 be-gk/lk.
- Übersichtsblatt braucht einsortieren.py-Sorte „uebersicht"
  (Posten aus Nacht 28.09.).

Verworfen (mit Grund):
- Gedrucktes Gerüst und gedrucktes Beispiel im Regelfall: der
  Lehrer schreibt das Gerüst selbst, er macht es besser.
- Fettdruck der Fertigkeit im Titel: Fett in jedem Titel ist
  Rauschen; die eigene Zeile hebt hervor.
- Verzeichnisseite: kostet eine Seite für sieben Zeilen; die
  Verzeichniszeile leistet es.
- Feste Gliederung gegeben/gesucht/Lösung im Beispiel: passt nicht
  zu Rechenverfahren, kostet Platz; Beispiel in Teilaufgaben-
  Gestalt stattdessen.
- Merkkasten oder Übersicht auf dem Fokus: Fokus setzt die
  Einheit voraus; Übersicht ist eigenes Produkt je Thema.
- Eigene Nummerierung der Zone (Z1, 1–7 doppelt): Nummer ist
  Adresse.
- Übersichtsblatt nur für Objektthemen: der Lehrer will die
  Übersicht für sich bei jedem Thema; ob der Schüler sie sieht,
  entscheidet er.
- Zwei getrennte Nachtaufträge in zwei Ordnern gleichzeitig: ein
  Auftrag mit Teilen, die ins Nachbar-Repo schreiben, ist
  einfacher; getrennt nur, wenn zwei Sitzungen laufen sollen.

## 6 Nächster Arbeitsschritt

Modell: Fable (Prompt-Umbau Abschnitt 0–2 mit Folgen; Urteile aus
dem Nachtbericht).

1. Übersichtsblatt-Prüfsteine mit dem Lehrer ansehen (PNG unter
   blaetter/uebersicht/…/pdf/) und die Form festlegen; danach die
   vier Abitur-Urteile aus § 5 knapp fällen (Befunddateien liegen);
   Ergebnisse in den Katalogauftrag (Punkt 3) oder als Posten.
2. v4.4 bauen aus befund-testlauf-2026-09-25.md Abschnitt „Prompt"
   (26 Punkte) und den Vorlagennamen der Stufe 5/6: Abschnitt 0–2
   (Bestellwörter „mit beispiel", „mit übersicht"; Sek-II-Regel;
   Fokus-Kopf; Anweisung und Fragewort; Rechenplatz statt
   Beispiel; Verfahrensüberschrift; Kastenzahlen-Sperre enger;
   Vorstufe ohne Ergebnis) und Abschnitt 3–6 (Bausteine nennen,
   Aufrufplan 2.7 neu, Deutungszeile, Ausgabeblock, zeiten.txt).
   Jede Regel aus einem Befund, keine aus Vermutung. Ausgabe:
   Auftrag an blattbau mit dem vollständigen Text als Datei 2,
   CHANGELOG-Zeile; dazu der Chat-Block für die Projektanweisung.
3. Katalogauftrag aus den Urteilen (Punkt 1) und
   _vorschlaege-2026-09-27.md (Opus): Einträge potenz 5, daten 7
   ausbauen; Niveaustufe G; GYM-K5d; Namensabweichungen;
   Merkkasten quadratische-gleichungen „0 = f(x)"; Befund Katalog
   3–8.
4. Testlauf mit v4.4 über werkzeuge/testlauf-auftrag.md (Nacht),
   Ergebnisse neben die vom 25.09.; danach der Blatt-Chat
   „quadratische gleichungen 9 oberschule".
