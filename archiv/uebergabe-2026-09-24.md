# Übergabe – Werkstatt verbessereBlaetter

Stand 2026-09-24, 19 Uhr. Nächster Chat beginnt mit „Start."

## 1. Ziel

Bestmöglicher Themenkatalog und bestmögliche Prompts für
Unterrichts- und Prüfungsblatt (ziel.md). Diese Phase: den
Unterrichtsblatt-Prompt auf v4.3 umbauen – neue Steuerung
(Bildschirm, drei Leiterstellungen, Blatt-0-Schalter) und
„schwach" als Form statt als Kürzung.

## 2. Arbeitsgrundlage

- ziel.md – Maßstab jeder Auswertung.
- blattbau/unterrichtsblatt.md v4.2 – der Prompt, der umgebaut
  wird; liegt seit 23.09. wortgleich in erzeugeUnterrichtsblatt().
- blaetter/prozentrechnung/2026-09-24/ – das Prüfstein-Blatt:
  Eingabe „prozentsatz 7 schwach", v4.2, Opus; Fokus Prozentsatz
  mit Blatt 0, 16 Hauptnummern, 4 Seiten.
- befund-schwach-blatt-2026-09-24.md – Auswertung dieses Blatts
  gegen MSK P A; befund-foerderhefte-2026-09-24.md – Befund aus
  den Förderheft-Seiten (älter, teils überholt durch den Blatt-
  Befund).
- quellen/foerderformen-fundliste.md (42 Zeilen, Formen und
  Dichte), quellen/foerderhefte-formen.md (Klick!, Kohl).
- MSK-Baustein P „Verständiges Prozentrechnen" (DZLM, CC BY-NC-SA):
  https://mathe-sicher-koennen.dzlm.de/mskfiles/uploads/Dokumente/
  msk_df_p_abc-verstaendig-prozentrechnen_260311.pdf, lokal unter
  hefte/foerderformen/. Der Katalog zitiert ihn schon (MSK P A).
- katalog/prozentrechnung.md, Abschnitt „Für schwache Schüler".

## 3. Arbeitsstand

Abgeschlossen am 24.09.:
- Sek II gesichert (quellen/lehrwerke-fundliste.md, Tabelle
  Sek II): Fundamente Einführungsphase BE/BB; Bigalke/Köhler
  Brandenburg 2019, Qualifikationsphase GK und LK, 5 Bände;
  Elemente SII nur NRW, Neue Wege nur Berlin 2011 (Gegenproben).
  Lambacher Schweizer Oberstufe hat keine Landesausgabe;
  Fundamente Qualifikationsphase B nicht erschienen. Fundamente B
  2017 und Mathematik heute bestätigt.
- Förderhefte: 25 Bände Inhaltsverzeichnisse (Sekundo 6–9,
  Schnittpunkt 5–10, Mathematik 2023, Kohl 5–10, Klick! 5–7 und
  Vorgänger 10, Mathematik heute Diagnose und Fördern 7–10);
  quellen/foerderhefte-fundliste.md.
- Formen: 42 freie Quellen (DZLM 8 Bausteine, Stark 3, Persen/
  Auer 13, Grundwissen Bayern 8, Brückenkurse 5, Rechenschwäche
  5); Zahlen in der Fundliste. Ergebnis in Kürze: Boden (DZLM,
  Klick!) = 1–3 Aufgaben je Seite, Diagnose zuerst, Streifen als
  Methode, Lücken; Kl. 7–10 (Auer Inklusion) = 1–2 je Seite,
  Lücke und Raster statt Beispiel; Grundwissen (Bayern, Stark) =
  Regel, Beispiel, eine Aufgabe, dicht – Vorbild für
  Auffrischen, nicht für schwach.
- MSK P A gelesen und gegen Katalog und Blatt gehalten; Befund
  in befund-schwach-blatt-2026-09-24.md.
- Prüfstein-Blatt gebaut und abgelegt.

Nicht begonnen (aus der Übergabe vom Vormittag, weiter offen):
(a) Gymnasialdecke Kl. 10 gegen die drei Gymnasial-Reihen plus
Fundamente Einführungsphase; (b) Katalogrevision „Klasse filtert
in Sek I nur, wo die Bücher es zeigen" (Beleg liegt jetzt in den
Inhaltsverzeichnissen); (c) Verortung Sek II an Bigalke/Köhler
und Fundamente EP. Alle drei Fable.

## 4. Verbindliche Entscheidungen und Rahmenbedingungen

Neu am 24.09. (Lehrer):
- Jedes Blatt beginnt mit einem Bildschirm: Thema, Klasse
  (Katalog, wenn nicht genannt), Zahl der Einheiten, die
  Leiterstellungen als nummerierte Zeilen mit je einer Zeile
  Wirkung, Vorschlag markiert (2 statt 1, wenn das Thema in
  blaetter/ liegt), Zusatzzeile mit den Zurufen. Antwort: eine
  Nummer; „weiter" nimmt den Vorschlag. Wer Thema, Klasse und
  Wort in einer Zeile tippt, überspringt den Bildschirm. Zweck
  ohne Thema → eine Zeile Rückfrage „Thema, Klasse?".
- Klasse ist Pflichtzahl im Zuruf; schwach, oberschule,
  Einheitsname (= Fokus) sind Zurufe, keine Fragen. Schulform
  filtert bis Kl. 10 nur GYM-Sprossen (Beschluss 23.09. bleibt).
- Fokus läuft über den Einheitsnamen; am Blatt vom 24.09.
  bestätigt („prozentsatz" → Fokus Einheit 2).
- Revision „schwach" vorgemerkt („superidee"), zu entscheiden
  am Prüfstein: schwach ändert die Form, nicht die Länge. Der
  Prüfstein liegt jetzt; die Entscheidung fällt zu Beginn des
  Umbaus.
- Claude-Code-Aufträge: Zählgrenzen (Abfragen, Bände, Seiten)
  statt Zeitgrenzen – Claude Code misst keine Zeit und meldet
  jede Zeitgrenze als erreicht. CQL mit Anführungszeichen an
  dnb-sru.py über --% und verdoppelte Anführungszeichen. Eine
  Formenzeile braucht keine gesicherte Datei; Ansehen im
  Betrachter genügt.

Vorgelegt, unwidersprochen, im neuen Chat mit einem Satz zu
bestätigen (nicht neu herleiten):
- Drei Stellungen der Leiter, disjunkt nach dem Kriterium
  „welcher Teil wird bearbeitet": ganze Leiter (jede Sprosse
  einmal), unten (untere Sprossen mehrfach), oben (obere
  Sprossen mehrfach). Blatt 0 ist ein eigener Schalter: voll,
  kurz, nur, ohne – Vorgabe je Stellung: ganz → voll (kurz, wenn
  das Thema in blaetter/ liegt), unten → voll, oben → ohne.
  „knapp" als Zuruf = ganze Leiter mit einer Aufgabe je Typ.
- Schnitt unten/oben: vor der ersten Sprosse, bei der der
  Schüler deuten muss (Sachtext, Umkehrung, Verknüpfung,
  Begründung); ohne solche Sprosse: Prüfungshöhe plus die
  davor. Der Prompt setzt ihn, die Deutungszeile zeigt ihn;
  Katalogmarke erst, wenn ein Lauf falsch schneidet.
- Klasse, Schulform, schwach ändern die Leiter (Stoffstand,
  GYM-Sprossen, F/Vorrat-Sprossen), die Stellung wählt daraus.
  schwach + oben = die höchsten verbliebenen Sprossen.
- Der Lehrer will die Wörter nicht lernen; die Wortliste dient
  dem Prompt (Freitext lesen), nicht ihm.

Rahmen aus früheren Übergaben, unverändert: Leiterprinzip;
Erkennungsschritte als Vorstufe; Schulform per Zuruf; Titel
„Kurzname – Formwort"; Ausgabeblock; Regel „erst Exemplar, dann
Regel"; nach jedem Blatt-Chat Protokoll-Archiv einsortieren.

## 5. Offene Punkte und verworfene Ansätze

Offen:
- Bezeichnungen der drei Leiterstellungen: Der Lehrer fand
  „Einstieg/Wiederholung/Sondierung/Vertiefung/Sicherheit" nicht
  treffend; Vorschlag „Ganze Leiter · Unten · Oben" mit je einer
  Zeile Wirkung; endgültig entscheidet er am Bildschirm-Entwurf.
- Stil-Befund am Blatt vom 24.09. (Lehrer, mit Fotos):
  Zwischenanweisungen wiederholen die Teilaufgabe („Färbe bei c)
  und d) selbst." – dann „c) Färbe die Hälfte."; „Kürze bei c)
  zuerst, dann erweitere." – dann „c) … gekürzt: … erweitert";
  „Bei e) steht das Ganze nicht im Text. Kreuze an …" – dann
  e) mit Kreuzen). Regel für v4.3, Abschnitt 3: Eine Anweisung
  steht einmal, entweder als Zwischenzeile oder im Teil.
- \streifenfeld (Streifen mit Antwortfeld rechts) fehlt in
  mathblatt.sty; der Prompt hat ihn als Baustein gebaut
  (Protokoll, Schritt 12). Auftrag an blattbau.
- Nach der Stunde ein Satz (Thema, wo der Schüler hing, was
  half): Der Lehrer denkt nach; Frage wieder stellen, wenn das
  erste v4.3-Blatt am Tisch war. Posten in faellig.md.
- Empfehlung: zwei bis drei Förderhefte kaufen (Sekundo
  Förderheft 7/8, Schnittpunkt Förderheft 8); Verlage zeigen
  keine Seiten, Händler nur Deckel.
- cosh-Katalog: in quellen.md geführt, Datei fehlt (faellig.md).
- Nebenfund: LISUM-Diagnosematerial (quellen/quelle-lisum-
  diagnose-foerderung-zahlen-operationen.txt) löst die Fundlücke
  [MzDuF] auf; Katalogeinträge, die sie zitieren, prüfen.

Verworfen (nicht wieder aufnehmen):
- Niveau-Achse (schwach/mittel/stark) als Filter: widerspricht
  dem Leiterprinzip; nur „schwach" bleibt, als Form.
- Fünf Zweckwörter als Zeilen des Bildschirms: mischten
  Leiterteil und Blatt 0; ersetzt durch drei Stellungen plus
  Schalter.
- „?"-Hilfeliste: ersetzt durch den Bildschirm bei jedem Blatt.
- Zwischensprossen für schwach: Die Seiten zeigen Takt und
  Dichte, keine zusätzlichen Stufen.
- Zeitgrenzen in Code-Aufträgen (siehe oben).
- Bundesweite Förderreihen ohne Zweck suchen: Zweck ist jetzt
  benannt (Form), Suche erledigt.

## 6. Nächster Arbeitsschritt

Modell Fable. Zuerst in einem Satz bestätigen lassen: drei
Stellungen plus Blatt-0-Schalter und die Revision „schwach als
Form" (Befund liegt). Dann v4.3 von unterrichtsblatt.md bauen,
Abschnitt 0–2: Bildschirm (Aufbau oben), Eingabedeutung (Thema,
Zahl unter 20 = Klasse, Einheitsname = Fokus, Zurufe), drei
Stellungen mit Schnittregel, Blatt-0-Schalter mit Vorgaben,
„schwach" als Form (zwei bis drei Aufgaben je Seite, Streifen
bzw. Darstellung neben jeder Aufgabe bis zur Prüfungshöhe,
Raster mit einer Zeile je Schritt, Päckchen mit einem variierten
Merkmal und Erklärzeile, Fachwort erst in der Sprosse, die es
braucht, Merkkasten ans Ende). Abschnitt 3: Anweisung nur einmal.
Testmaterial: das Blatt vom 24.09. gegen MSK P A – v4.3 muss die
fünf Abweichungen aus befund-schwach-blatt-2026-09-24.md
schließen. Ausgabe: vollständiger Prompt als Chat-Block mit
Holger-Zeile für erzeugeUnterrichtsblatt(), dazu Auftrag an
blattbau (Datei, \streifenfeld). Danach Opus: Lauf „prozent 7
schwach" und „prozent 7" mit v4.3, einsortieren, auswerten.
