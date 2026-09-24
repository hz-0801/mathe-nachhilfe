# Übergabe 2026-09-25 – Werkstatt verbessereBlaetter

## 1 Ziel

Der bestmögliche Themenkatalog und die beiden Prompts, die aus
ihm Blätter bauen. Maßgeblich ist ziel.md in der Wurzel; jede
Entscheidung dient dem Blatt, das ein Schüler im ersten Lauf
bearbeiten kann.

## 2 Arbeitsgrundlage

- ziel.md – das Ziel; gilt vor jeder anderen Datei.
- blattbau/unterrichtsblatt.md v4.2 – läuft seit 23.09. als
  Projektanweisung in erzeugeUnterrichtsblatt(); noch kein Lauf
  mit v4.2. blattbau/pruefungsblatt.md v0.15 unverändert.
  blattbau/mathblatt.sty 2026-09-22h (Stufe 4).
- msa/ – Profil msa mit vier Papieren: OS (2014–2025), EBR und
  FOR (2026), GYM (Gymnasialhefte 2014–2025, eigene Datei
  msa-katalog-gym.csv, 248 Zeilen). Gemeinsame Typenliste
  msa-typen.csv, 264 Typen nach Abgleichlauf 24.09. Vergleiche:
  msa/gym-vergleich.md (Typen: 76 nur GYM, 91 nur OS/EBR/FOR,
  84 beide, als Haupttyp; Haupt+Neben 79/83/102),
  msa/ebr-vergleich.md (EBR 2026: 25 Zeilen, 0 eigene Typen,
  jede Aufgabe Teil einer FOR-Aufgabe). Berichte
  msa/gym-bericht-2026-09.md, msa/nacht-bericht-2026-09-24.md.
- katalog/_niveaustufen-belege.md, katalog/_kursart-belege.md –
  Stufe A–H bzw. Kursart je Einheit und Sprosse; Vorschlag,
  entscheidet nicht.
- quellen/ – Rahmenlehrplan, LISUM, Klett-Fahrplan LS-AA,
  Stoffverteilungspläne Elemente der Mathematik BB 2016 (Kl. 5–9)
  und Sekundo BB 2017 (Kl. 7–10); Inhaltsverzeichnisse der
  Landesausgaben BE/BB Kl. 7–10 als Text (Auftrag 25.09., DNB):
  Fundamente B 2024 (Gymnasium und Oberschule), Fundamente B 2017
  nur Kl. 9, Westermann Mathematik 2023 (Oberschule), Mathematik
  heute 2014 (Oberschule; BE/BB-Zuordnung über ISBN-Folge, nicht
  belegt), Elemente der Mathematik 2016 (Gymnasium, auch Kl. 10)
  und 2025 (Kl. 5–7), Sekundo 2017, Schnittpunkt 2017 (ISS).
  Lambacher Schweizer: keine BE/BB-Ausgabe, kein DNB-TOC.
  Fundliste quellen/lehrwerke-fundliste.md, Bericht
  quellen/lehrwerke-inhalt-bericht-2026-09.md, Skript
  werkzeuge/dnb-sru.py.
- fhr/fhr-vorgaben-pruefung-2026-09.md – Prüfung der fhr-Vorgaben:
  16 bestätigt, 1 abweichend, 3 nicht belegbar; Vorbehalt bleibt.
- blaetter/ – drei Blätter, Register blaetter/index.md;
  nullstellen/2026-09-22 ist Lauf 4 (nicht ausgewertet).
- katalog/ (73 Einträge), README.md als Landkarte.

## 3 Arbeitsstand

Abgeschlossen seit 23.09.:
- Gymnasialhefte P10 2014–2025 erfasst (Sonnet), Abgleichlauf der
  Typen (29 zusammengezogen, 32 umbenannt), Thema „Sinus- und
  Kosinussatz". Entscheidung 18 in konzept.md neu gefasst
  (Kippbedingung eingetreten: zentrale Klassenarbeit Gymnasium
  Kl. 10 seit 2025/26; Arbeit 2026 nicht veröffentlicht).
- EBR-Heft 2026 erfasst, Vergleich EBR/FOR.
- fhr-Vorgaben gegen die Papiere geprüft.
- Quelle gefunden: Die Deutsche Nationalbibliothek führt zu fast
  jedem Schulbuch das Inhaltsverzeichnis als PDF
  (d-nb.info/<IDN>/04, SRU-Schnittstelle). Fundamente der
  Mathematik Ausgabe B ab 2024 (Berlin/Brandenburg, Gymnasium
  und Oberschule zugleich) Kl. 7–10 liegen vor; Kl. 10 endet mit
  ganzrationalen Funktionen, Polynomdivision, Ableitung.

- Inhaltsverzeichnisse von sieben Reihen gesichert (Sonnet,
  25.09.): 27 Bände, Text unter quellen/. Schwachstelle: Mathematik
  heute ist als BE/BB-Ausgabe angesetzt, nicht belegt; Kl. 7 mit
  Zeichenfehlern.

Läuft: nichts.

Nicht geschehen: Lauf 5 mit v4.2; Auswertung Lauf 4.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Neu am 23.–25.09.:
- Schulform bis Klasse 10: Zuruf statt Frage. Der Prompt fragt
  nicht nach der Schulform; „oberschule" und „schwach" lassen
  GYM- und Vorrat-Sprossen weg, ohne Zuruf bleibt alles auf dem
  Blatt (Leiterprinzip; fehlender Stoff ist der schlimmere
  Fehler als Überschuss). Ersetzt „Gefragt wird in v4.3".
- GYM-Marke im Themenkatalog kommt aus drei Belegen zusammen:
  Rahmenlehrplan H, LISUM nur-Gymnasium, Typ nur in
  Gymnasialheften; ein P10-Original hebt sie immer auf. „Nur
  GYM" im Vergleich allein ist kein Gymnasialstoff (Kreisumfang,
  binomische Formel stehen dort).
- EBR: keine eigene Marke; EBR ist FOR ohne die oberen Sprossen,
  also die Option „schwach" (Beleg: ein Heft, 2026; zweites
  2027).
- Sek II: ohne Zuruf Grundkurs, keine Kursartfrage.
- Berlin: MSA-Prüfung Mathematik seit 2011 gemeinsam mit
  Brandenburg (FOR-Hefte = Berliner MSA); Gymnasium Berlin ohne
  MSA-Prüfung seit 2023/24, ohne Ersatz. Die Gymnasialhefte
  sind für Berlin Maßstab der Leiterhöhe, Prüfungsart nur für
  Brandenburg.
- Modelle: Sonnet reicht für Hefte erfassen und Mechanik, wenn
  danach ein Abgleichlauf der Etiketten mit Opus oder im Chat
  folgt (Sonnet-Messlauf 24.09.: Mechanik fehlerfrei, 108 neue
  Typen für 248 Zeilen). Urteil bleibt Fable/Chat.
- Unbeaufsichtigte Aufträge: keine Rückfrage, Standdatei je
  Teil, ein Commit je Teil, Fehlerfall mit Regel, Berechtigungen
  der Code-Sitzung auf automatisch. Der Kopf jedes Blocks sagt
  „keine Rückfragen".
- Quellen: sammeln breit (DNB ist billig), auswerten nur, was
  ein Blatt ändert. Fotos der Schülerbücher: nicht ablegen,
  im Chat lesen und als Zeile eintragen (Schule, Klasse, Werk,
  Kapitelstand, Datum).
- Beschlüsse vom 22.09. und 23.09. gelten weiter (archiv/
  uebergabe-2026-09-23.md § 4), soweit oben nicht ersetzt.

Rahmen: wie 23.09. (PowerShell, git.exe, Python-Pfad, MiKTeX;
Modellwähler vor jedem Auftrag prüfen; eigenes Modell nachsehen).
Zusätzlich: Schwelle „selten" muss je Papier zählen –
msa-ertrag.csv trägt jetzt GYM- und EBR-Zeilen mit.

Modellwahl nächste Phase: Fable für die drei Auswertungen (§ 6)
und für Lauf-Auswertungen; Opus für Aufträge und Berichte;
Sonnet für Sammelaufträge; Blatt-Chats Opus.

## 5 Offene Punkte und verworfene Ansätze

Zur Entscheidung vorgelegt (Lehrer entscheidet):
- Revision „Klasse filtert in der Sek I keine Sprosse": mit
  mehreren Landesausgaben je Klasse gilt stattdessen – in
  Richtung Klassenarbeit endet die Leiter beim Stoff der Klasse,
  wo die Bücher einig sind; in Richtung Prüfung am
  Prüfungsniveau; bei Streuung Leiterprinzip. Beleg entsteht im
  laufenden Auftrag.

Offen, in dieser Reihenfolge:
1. Sammelauftrag DNB Sek II (Einführungs- und Q-Phase, beide
   Länder, GK und LK) und Förder-/Arbeitshefte (bundesweit) –
   Sonnet, nachts. Darin: Fundamente B 2017 Kl. 7/8/10 und
   Mathematik heute per Verlagsseite bestätigen.
2. Drei Auswertungen (Fable), jede mit einem Blatt als
   Prüfstein: (a) Gymnasialdecke Kl. 10 aus Fundamente/Elemente –
   welche Ketten oben länger werden, Verortung der Sek-II-
   Einträge, die in Kl. 10 Gymnasium liegen; (b) Kapitel, die
   Oberschulreihen weglassen → GYM-Marke; (c) Kapiteltitel als
   Wortform für Katalogtitel und Zuruf.
3. Katalogauftrag: Prüfungsform (GYM) je Kette in den 29 Sek-I-
   Einträgen, GYM-Marke nach der Drei-Belege-Regel; die drei
   Stufenfehler (trigonometrie G, lineare-funktionen E4 G,
   wahrscheinlichkeit Baumdiagramm G); msa.md § 1 Satz zu Berlin.
4. Lauf 5 mit v4.2, „nullstellen kl. 10" – misst die Umfangsfrage.
5. v4.3: Umfangsfrage auch bei Test-Richtung; Zuruf oberschule/
   schwach filtert GYM und Vorrat; Klassenfilter nach der
   Revision oben, falls beschlossen; Schwelle „selten" je Papier.
6. Lauf 4 auswerten (Fable); v4.2 von Fable gegenlesen.
7. Weiter wie 23.09.: schwach mit Lückenbeispielen, ziel.md § 5
   bereinigen, Befunde-Skript, Prompt kürzen, Prüfungsblatt-
   Prompt, Katalogpflege (Gegenlese Sek II, Boden unter Kl. 8,
   README-Lücken, \liniendia Overfull).
8. Cornelsen-Synopsen: nur für Lehrkräfte; Weg entfällt.
   Elemente Kl. 10 und Mathematik 2023 BB liegen (DNB).

Verworfen:
- Schulformfrage im Prompt mit Auslöser „Stoff auf H" – zu grob
  in beide Richtungen (Begründungen liegen auf H, P10-Stoff
  würde gestrichen; GYM-Sprossen ohne H blieben unerkannt).
- Eigenes Profil für die Gymnasialhefte – gemeinsame Typenliste
  ist nötig für den Vergleich je Typ.
- Berlin als eigene Prüfungsquelle – gemeinsame Prüfung.
- Leseproben und Warenkorb als Weg zu Inhaltsverzeichnissen –
  DNB ist vollständiger und frei.
- Fotos der Schülerbücher ablegen – im Chat lesen genügt.
- Verworfenes vom 22./23.09. gilt weiter.

## 6 Nächster Arbeitsschritt

Sammelauftrag für Sek II (Einführungs- und Q-Phase, Berlin und
Brandenburg, GK und LK, alle drei Verlage) und für Förder- und
Arbeitshefte (bundesweit) über die DNB schreiben (Sonnet,
unbeaufsichtigt, Muster archiv/auftrag-lehrwerke-inhalt.md).
Danach die Auswertung (a) Gymnasialdecke Kl. 10 auf Fable, mit
einem Blatt als Prüfstein.
