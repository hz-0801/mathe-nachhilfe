# Fachhochschulreife Mathematik Brandenburg – Amtliche Vorgaben und ihre Änderungen
Stand 17.09.2026 · Profil fhr · gesonderter Baustein, unabhängig vom Katalog

Zweck: festhalten, was die Behörde zur Prüfung vorgibt und wann sich etwas
geändert hat, damit der Katalog richtig gelesen wird und Formatwechsel nicht
unbemerkt bleiben. Pendant zu msa-vorgaben.md (Profil msa) und abi-vorgaben.md
(abi, iqb); konzept.md Entscheidung 19. Diese Datei ist kein Teil der
Erfassung; der Katalog-Prompt und fhr-bau.py lesen sie nicht. Angelegt am
17.09.2026 (Auftrag G, Punkt 3) aus dem, was fhr.md § 1–7 und
fhr-pruefungen.md bereits festhalten; die Papiere selbst wurden dafür nicht
neu gelesen, der erste eigene Vorgabencheck (§ 4) steht aus.

## 1 Quellen

- Rechtsgrundlage: Fachoberschul- und Fachhochschulreifeverordnung (FOSFHRV);
  die Aufgaben werden nach § 31 Absatz 1 zentral festgelegt (fhr.md § 1).
- Rahmenlehrplan Mathematik für die Fachoberschule, in Kraft seit dem
  01.08.2019; konkretisiert durch die jährlichen Prüfungsschwerpunkte
  (fhr.md § 1).
- Prüfungsschwerpunkte je Schuljahr und Fach: Ordner `Pruefungsschwerpunkte/`
  neben den Heften auf dem Bildungsserver Berlin-Brandenburg
  (https://bildungsserver.berlin-brandenburg.de/fileadmin/bbb/unterricht/pruefungen/Fachoberschule_BB/).
  Dort liegen nur die Fassungen 2026/27 (Prüfung 2027) und 2027/28 (Prüfung
  2028); für die erfassten Jahrgänge 2019–2026 fehlen sie (fhr-pruefungen.md,
  Umfang).
- Rundschreiben des MBJS zu Terminen und Fristen: Ordner `Pruefungstermine/`,
  zuletzt `MBJS_RS_07-26.pdf` vom 25.06.2026 (nennt die Ersatzaufgabe nach
  § 31 Absatz 1 FOSFHRV; fhr.md § 4).
- Hefte: Übersichtsseite https://bildungsserver.berlin-brandenburg.de/pruefungen-fos-bb;
  Verzeichnis und Dateinamen in fhr-pruefungen.md.
- Kein IQB-Pool: die Aufgabenpools des IQB gelten nur für die Allgemeine
  Hochschulreife (fhr.md § 9).

## 2 Vorgaben-Historie

Aufbau aus den Heften (fhr.md § 3): drei voneinander unabhängige Aufgaben mit
Überschrift – zweimal Differential- und Integralrechnung, einmal Stochastik;
laut Prüfungsschwerpunkten sind auch vier möglich, im Bestand kommen nur drei
vor. 70 Bewertungseinheiten (meist 30 + 20 + 20), 180 Minuten, alle Aufgaben
Pflicht, ein Niveau, keine Anforderungsbereiche im Heft. Die Lehrerhefte
enthalten den Erwartungshorizont mit verbindlicher Punkteverteilung, ab 2021
meist einen Gutachtenbogen. Je Prüfungstermin zwei gleichwertige
Aufgabenvorschläge zur Wahl der Lehrkraft (Buchstaben A, B, C) und ein weiterer
Vorschlag für den Nachschreibetermin, der nicht veröffentlicht wird
(Prüfungsschwerpunkte § 2.1; fhr.md § 4).

| Prüfungsjahr | Quelle | Vorgabe / Änderung |
|---|---|---|
| 2019 | Hefte 2019 A/C, fhr.md § 4 und § 7 | Prüfung 10.05.2019, vor dem Rahmenlehrplan vom 01.08.2019. Die Hefte nennen keine Hilfsmittel (hilfsmittel „ja" aus den Vorgaben); Koordinaten im Heft als P(–1|–5) mit ASCII-Bindestrich als Minus. |
| 2020 | Hefte 2020 A/C | Prüfung 03.06.2020, erster Jahrgang unter dem heutigen Rahmenlehrplan, vor den Kürzungen. Hilfsmittel im Heft nicht genannt; Punkte 28 + 21 + 21 (A) und 29 + 21 + 20 (C). |
| 2021 | Hefte 2021 A/B, fhr.md § 3 und § 7 | Coronabedingt gekürzte Vorgaben. Ab 2021 stehen die Hilfsmittel im Heft: Formelsammlung, Nachschlagewerk Rechtschreibung, Taschenrechner ohne Programmierbarkeit, Grafik, numerisches Differenzieren oder Integrieren und ohne automatisches Gleichungslösen; nichtganzzahlige Ergebnisse auf zwei Dezimalstellen gerundet. Ab 2021 meist Gutachtenbogen (fehlt 2021 B und 2023 C). Punkte 2021 B 32 + 18 + 20. |
| 2022 | Hefte 2022 B/C | Coronabedingt gekürzte Vorgaben; Prüfung 06.05.2022. Aufbau sonst unverändert. |
| 2023–2026 | Hefte | Aufbau unverändert (drei Aufgaben, 70 BE, 180 min); Prüfungen 05.05.2023, 08.05.2024, 28.05.2025, 05.06.2026; 2026 C mit 27 + 23 + 20. Prüfungsschwerpunkte dieser Jahrgänge liegen nicht auf dem Server. |
| 2027 | Prüfungsschwerpunkte 2026/27 (gelesen bei Anlage des Profils, 12./13.09.2026) | Zwei gleichwertige Aufgabensätze zum Prüfungstermin plus Nachschreibevorschlag (§ 2.1); Hilfsmittel ohne CAS; Kompetenzen ausdrücklich nicht auf Themengebiete beschränkt (fhr.md § 5). Inhalte nur 2027 (Markierung 27 in fhr.md § 6): Extremwertaufgaben, Rotationsvolumen um die x-Achse, Kombinatorische Abzählverfahren; Funktionsgleichung bestimmen bis zum zweiten Grad. |
| 2028 | Prüfungsschwerpunkte 2027/28 | Neu gegenüber 2027 (Markierung 28): Normale, Körpervolumen aus Grundfläche und Länge, Unabhängigkeit von Ereignissen; Funktionsgleichung bestimmen bis zum vierten Grad (dritter und vierter nur über Symmetrie). Die Inhalte mit Markierung 27 entfallen. |

Folgen für die Deutung des Katalogs: Der Vorgabenstand eines Jahrgangs ist
kein Katalogfeld. Gefiltert wird über die Schwerpunktmarkierung der Themenliste
(fhr.md § 6); für die Decke einer Kette bleibt der Vorgabenstand Information im
Protokoll (fhr.md § 7). Eine Geltungsdatei entfällt, weil ein Träger, eine
Schulform und ein Niveau vorliegen (konzept.md § 8, Frage 4).

## 3 Was die Schwerpunkte nicht als Inhalt führen

- Geometrie, Trigonometrie und Gleichungslehre kommen nur als Werkzeug vor
  (fhr.md § 1); die Themenliste führt sie unter der Leitidee Grundlagen, einer
  Zutat des Profils (fhr.md § 5).
- Einstufige Laplace-Versuche stehen nicht in den Schwerpunkten, die Hefte
  verlangen sie aber (2023-C-3b); Thema Laplace-Wahrscheinlichkeit ohne
  Schwerpunktmarkierung (fhr.md § 6).

## 4 Jährlicher Vorgabencheck (eigener Schritt, einmal im Jahr, wenn die Prüfungsschwerpunkte des nächsten Schuljahrs erscheinen)

1. Prüfungsschwerpunkte des neuen Schuljahrs aus `Pruefungsschwerpunkte/`
   laden, dazu das Rundschreiben aus `Pruefungstermine/` (§ 1).
2. Alles zu Aufbau, Zeit, BE, Aufgabenzahl, Hilfsmitteln, Inhalten und
   Terminen als Zeile in § 2 eintragen, Änderungen gegen das Vorjahr benennen.
3. Themenliste fhr.md § 6: Markierungen auf den neuen Stand bringen (neuer
   Jahrgang dazu, ausgelaufener weg); neue oder gestrichene Inhalte nur über
   den Bericht. fhr-bau.py und fhr-typenbibliothek.py führen die Themenliste
   als Code (THEMEN) und ziehen mit.
4. Danach die neuen Hefte in fhr-pruefungen.md eintragen und erfassen.
5. Wenn sich Aufbau oder Hilfsmittel ändern: prüfen, ob das Profil (Felder,
   Kürzel, soll in KONFIG von fhr-bau.py) mitziehen muss.

## 5 Änderungen an dieser Datei

- 2026-09-17: angelegt (Auftrag G, Punkt 3) als fhr-Pendant zu msa-vorgaben.md
  und abi-vorgaben.md, aus fhr.md v1.8 § 1–7 und fhr-pruefungen.md
  zusammengetragen; kein eigener Vorgabencheck, die Papiere nicht neu gelesen.
