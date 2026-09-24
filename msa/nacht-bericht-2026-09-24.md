# Bericht Auftrag Nacht, 24.09.2026

Modell: Sonnet.

## Teil 1 – EBR-Heft 2026 erfassen, Vergleich EBR/FOR

Zeilen: 25 (10 Basis, 15 Kontext). Punktprüfung je Aufgabe (Soll/Ist):
Aufgabe 1: 10/10 · Aufgabe 2 (Turm): 5/5 · Aufgabe 3 (Viereck): 4/4 ·
Aufgabe 4 (Benzinpreise): 6/6 · Aufgabe 5 (Funktionen): 5/5 · Aufgabe 6
(Würfel): 5/5 · Aufgabe 7 (Mietkosten): 5/5. Gesamt 40/40. Selbstprüfung
(leeres ZEILEN) bestanden: 418 Katalogzeilen (136 Basis, 282 Kontext) plus
248 GYM-Zeilen, 264 Typen, alle verwendet.

Neue Typen: keine. Befund beim Bau: jede Aufgabe des EBR-Hefts 2026 ist
entweder wortgleich mit einer Aufgabe des Hefts 2026 FOR (Aufgabe 1,
Basisaufgaben a–j vollständig) oder deren erste ein bis zwei Teilaufgaben
desselben Kontexts (Turm, Viereck, Benzinpreise, Funktionen, Würfel,
Mietkosten – EBR lässt jeweils die letzte(n), schwerste(n) Teilaufgabe(n)
weg, die FOR zusätzlich hat). Dadurch reicht die vorhandene Typenliste
vollständig aus; jede Zeile trägt zur Nachvollziehbarkeit eine Bemerkung
„Wortgleich mit 2026-FOR-…“ (eigene Entscheidung, nicht im Schema
vorgesehen, aber als Besonderheit im Sinne von Kern § 5 sinnvoll).

„?“-Zeilen: keine.

Vergleich EBR/FOR (`msa/ebr-vergleich.md`, `werkzeuge/gym-vergleich.py
--gruppen`, Gruppe A = papier EBR, Gruppe B = papier FOR und OS): Typen
(Haupt) 0 nur EBR, 150 nur FOR/OS, 25 in beiden; Typen (Haupt+Neben) 0 nur
EBR, 156 nur FOR/OS, 29 in beiden; Themen 0 nur EBR, 15 nur FOR/OS, 17 in
beiden. Befund: EBR verwendet in diesem einen Heft keinen einzigen Typ und
kein einziges Thema, das nicht auch bei FOR/OS vorkommt – kein Beleg für
eine eigene Marke im Themenkatalog, aber auch keine Widerlegung (ein
einzelnes Heft ist keine tragfähige Grundlage; offene Entscheidung in
konzept.md § 6 mit Verweis auf weitere EBR-Jahrgänge, nächster 2027).

Ertrag (`werkzeuge/ertrag.py`): 25 Typen (alle 25 in diesem Heft als
Haupttyp verwendeten Typen) haben einen höheren Ertrag (mehr Punkte, mehr
Zeilen); die Jahreszahl `jahre_gesamt` bleibt für alle unverändert, weil das
Jahr 2026 durch das FOR-Heft bereits gezählt war. Die vier
typ_neben-Typen dieses Hefts (Kosten aus Menge und Preis berechnen,
Behauptung prüfen, Wahrscheinlichkeit mehrstufig unabhängig, Eigenschaften
eines Graphen beurteilen) ändern nur ihre Nebenzeilen-Zahl, nicht den
Ertrag. Gegenprobe des Skripts (Sollwerte aus einem früheren Auftrag, wird
laut Kopf des Skripts nicht angepasst): 4 von 5 Werten weichen jetzt ab
(erwartet, da das Skript ausdrücklich nicht an neue Katalogstände angepasst
wird, sondern die Abweichung selbst der Befund ist).

Nachgeführt: msa-pruefungen.md § 2/§ 3, msa-quellen.md § 2/§ 5,
konzept.md (Satz zur Zurückstellung ersetzt, Baustein 18 ergänzt, § 6 neue
offene Entscheidung), faellig.md § 1 msa. Commit „msa: Heft 2026 EBR
erfasst, 25 Zeilen; Vergleich EBR/FOR“.

## Teil 2 – Stoffverteilungspläne der Landesausgaben

Fundliste in Kurzform (vollständig: `quellen/lehrwerke-fundliste.md`):

- **Klett – Lambacher Schweizer**: bereits vorhanden (`quelle-klett-fahrplan-ls-aa-berlin-2024.txt`).
- **Klett – Schnittpunkt Mathematik**: nicht gefunden (nur Kompetenzraster Berlin/ISS Kl. 5–10 frei verlinkt, kein Stoffverteilungsplan).
- **Klett – Mathe live**: nicht gefunden (keine BE/BB-Landesausgabe).
- **Westermann – Elemente der Mathematik SI**: gefunden und gesichert, Kl. 5–9 (`quelle-westermann-elemente-der-mathematik-bb-2016.txt`).
- **Westermann – Mathematik Neue Wege**: nicht gefunden für Sek I (nur SII/Oberstufe-Ausgabe Berlin).
- **Westermann – Sekundo**: gefunden und gesichert, Kl. 7–10 (`quelle-westermann-sekundo-bb-2017.txt`).
- **Westermann – maßstab**: als „Mathematik – Ausgabe 2023 für BE/BB/ST/TH, 7.–10. Schuljahr“ fortgeführt; kein Stoffverteilungsplan verlinkt gefunden.
- **Cornelsen – Fundamente der Mathematik**: Synopsen Kl. 8/9/10 gefunden, aber nur über Warenkorb/Registrierung als Lehrkraft erhältlich (0 €, aber Login nötig) – nicht heruntergeladen (Auftragsregel „kein Login, keine Registrierung“).
- **Cornelsen – Fokus Mathematik**: keine BE/BB-Ausgabe gefunden.

Gesichert: 2 Werke (9 Einzeldateien: 5 + 4 Klassen). README.md,
quellen/quellen.md nachgeführt. Commit „quellen: Stoffverteilungspläne
Landesausgaben BE/BB gesichert, Fundliste“.

## Teil 3 – Vorbehalt in fhr-vorgaben.md prüfen

20 Angaben aus § 1–3 geprüft: 16 bestätigt, 1 abweichend, 3 nicht belegbar,
1 nicht erneut geprüft (außerhalb der heute geholten Papiere). Vollständige
Tabelle mit Fundstellen: `fhr/fhr-vorgaben-pruefung-2026-09.md`.

Abweichung im Wortlaut: Die Angabe „Die Hefte 2019 und 2020 schreiben
Koordinaten als P(–1|–5) und benutzen den ASCII-Bindestrich als Minus“
(fhr.md § 4, wiederholt in fhr-vorgaben.md § 2) stimmt nicht mit den
geprüften Originalen überein: 2019-A, 2019-C und 2020-A verwenden im
PDF-Textlayer durchgehend das echte Minuszeichen U+2212 (z. B. 2020-A:
„Sx1(−1|0)“), an keiner Stelle einen ASCII-Bindestrich vor einer Ziffer.

Nicht belegbar (im Wortlaut): (1) „Coronabedingt gekürzte Vorgaben“ für
2021 und 2022 – die Prüfungsschwerpunkte dieser Jahrgänge sind auf dem
Bildungsserver nicht archiviert, nur die aktuellen Fassungen (2026/27,
2027/28) liegen vor, sodass sich die Kürzung nicht direkt belegen ließ.
(2) „Ab 2021 stehen die Hilfsmittel im Heft: Formelsammlung,
Nachschlagewerk Rechtschreibung, Taschenrechner ohne Programmierbarkeit,
Grafik, numerisches Differenzieren oder Integrieren und ohne automatisches
Gleichungslösen; nichtganzzahlige Ergebnisse auf zwei Dezimalstellen
gerundet“ – dieser Wortlaut steht in keinem der vier geprüften Lehrerhefte
(2019-A, 2021-B, 2022-B, 2023-C), sondern ist wortgleich mit Abschnitt 3
der Prüfungsschwerpunkte 2026/27 bzw. 2027/28; für 2021 liegt aber keine
Prüfungsschwerpunkte-Fassung vor, die eigentliche Quelle dieser Angabe ist
damit unklar.

Vorbehalt im Kopf von fhr-vorgaben.md bleibt bestehen (nicht alle Angaben
bestätigt). faellig.md § 2 nachgeführt: „Prüfung erfolgt 2026-09-24,
Abweichungen offen: 4“. Commit „fhr: Vorgaben gegen die Papiere geprüft“.

## Teile „offen“

Keiner der drei Teile ist offen geblieben. Ein Einzelschritt des
Abschlusses ließ sich nicht ausführen: `empty_zeilen.py` (im Auftrag als
„Hilfsskript aus dem Abgleichlauf, Repo-Wurzel“ genannt) existiert nicht im
Repo und ist auch in der gesamten Git-Historie nicht nachweisbar – nichts
zu verschieben.

## Eigene Entscheidungen (Zusammenfassung)

- Bemerkung „Wortgleich mit 2026-FOR-…“ als Vermerk in jeder wortgleichen
  EBR-Zeile eingeführt (Kern § 5 erlaubt freie Vermerke; für den
  angeforderten Vergleich EBR/FOR und künftigen Blattbau hilfreich).
- Für den Kreisanteil in 2026-EBR-B1b („grau markierte Fläche = 1/3“) die
  Bildvermessung selbst durchgeführt (Pixelanalyse der gerenderten Seite)
  statt sich nur auf den Vergleich mit der bereits erfassten FOR-Zeile zu
  verlassen; beide stimmen überein (Rechteck ≈ 1/6, Quadrat 1/4,
  Parallelogramm 1/2, Kreissektor 120° = 1/3).
- `werkzeuge/gym-vergleich.py` auf v0.3 gehoben (Option `--gruppen`) statt
  eines neuen Skripts, weil Zählregel und Ausgabeform identisch sind; der
  Standardlauf (ohne Option) wurde gegenprüft und ist bytegleich bis auf
  Versions- und HEAD-Zeile.
- Bei Schnittpunkt Mathematik (Klett) wurde ein „Kompetenzraster“ gefunden,
  aber nicht als Stoffverteilungsplan/Synopse gewertet und nicht gesichert
  (andere Dokumentart als angefordert).
- Cornelsen-Synopsen (Fundamente der Mathematik) trotz 0 €-Preis nicht
  heruntergeladen, weil der Bestellweg eine Registrierung als Lehrkraft
  voraussetzt (Auftragsregel „kein Login, keine Registrierung“).
- Bei der fhr-Prüfung wurden von sechzehn Heften sechs stichprobenartig im
  Volltext gegen die Vorgaben-Datei gehalten (2019-A, 2019-C, 2020-A,
  2021-B, 2022-B, 2023-C); die reinen Punktsummen und Prüfungstermine aller
  sechzehn Hefte wurden zusätzlich vollständig gegen `fhr-katalog.csv` und
  `fhr-pruefungen.md` geprüft (selbst aus dem Lesen der echten Hefte bei der
  Erfassung 12.09.2026). Methodik ausführlich in
  `fhr/fhr-vorgaben-pruefung-2026-09.md` begründet.

Push origin drücken.
