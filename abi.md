# PROFIL ABI – Zentrale schriftliche Abiturprüfung, Mathematik, Berlin/Brandenburg
Version 0.1 · 12.09.2026 · Kennung abi · gilt mit Kern v0.3 (Schema-Version 2)

## 1 Prüfung

Zentrale schriftliche Abiturprüfung im Fach Mathematik. Berlin und Brandenburg
prüfen beide zentral, auf grundlegendem Anforderungsniveau (Grundkurs) und auf
erhöhtem Anforderungsniveau (Leistungskurs; in Brandenburg „Kurs auf erhöhtem
Anforderungsniveau"). In Brandenburg ist Mathematik nur dann Pflichtprüfungsfach,
wenn es als Leistungskurs belegt wird.

Die Aufgaben entstehen gemeinsam: Die Hefte für das erhöhte Niveau tragen im Kopf
sowohl das Ministerium für Bildung, Jugend und Sport als auch die Senatsverwaltung
für Bildung, Jugend und Familie, und ein erheblicher Teil der Aufgaben ist in
beiden Ländern wortgleich (Nachweis in abi-aufbau.md § 4). Die Länder stellen aus
diesem Werk verschieden zusammen. Auf grundlegendem Niveau tragen die
veröffentlichten Hefte nur die Berliner Behörde.

Bestand: Die Hefte laut abi-quellen.md § 2, zunächst 2017 und 2018.
Sagt der Lehrer Abi, Abitur, GK oder LK, ist dieses Profil gemeint.

## 2 Ablage und Quellen

Basis-URL der Katalogdateien: https://raw.githubusercontent.com/hz-0801/mathe-nachhilfe/main/
(alle Dateien flach in der Wurzel; bei anderer Ablage nur diese Zeile ändern).
Katalogdateien dieses Profils: abi-quellen.md, abi-pruefungen.md, abi-typen.csv,
abi-katalog.csv. Eine Katalogdatei, kein zweiter Block wie beim Profil msa – der
hilfsmittelfreie Teil hat zu wenige Zeilen, um eine eigene Datei zu rechtfertigen;
er wird über das Feld `block` unterschieden.

Hefte: abi-quellen.md nennt Verzeichnis, Dateinamen und papier-Kürzel; geholt wird
mit curl. Veröffentlicht sind nur 2011–2018.

Amtliche Lösungen: für die Landesaufgaben 2017/2018 keine. Der Erwartungshorizont
mit verbindlicher Verteilung der Bewertungseinheiten geht nur an die Schulen. Für
diese Hefte gilt Kern § 3 d in der Fassung „eigene Rechnung"; Unsicherheiten nach
`bemerkung`. Für Poolaufgaben des IQB ab Prüfungsjahr 2019 liegt der
Erwartungshorizont öffentlich vor; dort gilt die Fassung „amtliche Lösung
vorhanden" wie im Profil fhr, mit dem Zusatz „amtlich" in `ergebnis`.

Amtliche Vorgaben: die Prüfungsschwerpunkte des jeweiligen Prüfungsjahrs,
getrennt nach Land und Niveau. Brandenburg unter
.../fileadmin/bbb/unterricht/pruefungen/abitur_bb/RS_ZA_JJJJ/PS_Mathematik_LK_JJJJ.pdf
(entsprechend _GK_), Berlin unter berlin.de, ps_mathematik_JJJJ_lk.pdf bzw. _gk.pdf.
Sie gehören nach vorgaben.md und werden jährlich geprüft.

## 3 Aufbau der Hefte

**Zwei Formate.** Die erfassten Hefte 2017/2018 und die heutige Prüfung sind
verschieden gebaut. Der Katalog nimmt 2017/2018 als Typenquelle; die Blattstruktur
richtet sich nach dem heutigen Format.

**Format bis 2018 (papier be-gk, be-lk, bb-ea).** Drei Aufgabenstellungen, je eine
von zwei Aufgaben zur Wahl: 1 Analysis, 2 Analytische Geometrie, 3 Stochastik.
Berlin GK 210 Minuten, 40 + 20 + 20 = 80 BE; Berlin LK 270 Minuten,
50 + 25 + 25 = 100 BE. Brandenburg auf erhöhtem Niveau hat zusätzlich
Aufgabenstellung 1 als hilfsmittelfreien Teil ohne Wahl (drei Aufgaben zu je zwei
Teilaufgaben, 15 BE, Abgabe spätestens nach 40 Minuten); die Sachgebiete
verschieben sich dadurch auf 2, 3 und 4, und die Wahl in 3 und 4 ist gekoppelt –
wer 3.1 nimmt, muss 4.1 nehmen. 270 Minuten, 15 + 50 + 35 = 100 BE. Berlin hat in
diesen Jahren keinen hilfsmittelfreien Teil. Hilfsmittel: Nachschlagewerk zur
Rechtschreibung, an der Schule eingeführte Formelsammlung, nicht programmierbarer
und nicht grafikfähiger Taschenrechner.

**Format ab Prüfungsjahr 2019 (Berlin) bzw. bereits vorher (Brandenburg).** Jeder
Aufgabenvorschlag besteht aus Prüfungsteil A (hilfsmittelfrei) und Prüfungsteil B
(mit Hilfsmitteln). Teil A enthält mehrere kurze, nicht zusammenhängende Aufgaben
in zwei Gruppen: Gruppe 1 in den Anforderungsbereichen I und II, Gruppe 2 mit
mindestens einer Teilaufgabe im Anforderungsbereich III. Brandenburg LK 2027: vier
Pflichtaufgaben aus Gruppe 1, dazu zwei aus sechs angebotenen der Gruppe 2; GK:
je drei Aufgaben beider Gruppen zur Auswahl, aus jeder Gruppe eine. Teil B enthält
komplexe Aufgaben, mindestens eine aus der Analysis, dazu Analytische Geometrie
und Stochastik, teils Pflicht, teils Wahl. Arbeitszeit Brandenburg LK 2027
330 Minuten inklusive Auswahlzeit. Hilfsmittel: Nachschlagewerk zur
Rechtschreibung, Formelsammlung des IQB (nicht in Teil A), Taschenrechner (nicht
in Teil A), Standard-Zeichenwerkzeuge.

**WTR, CAS und MMS.** Zu jedem Heft gibt es eine vollständige Parallelfassung für
Rechner mit Computeralgebra. Brandenburg nennt sie ab 2027 „modulares
Mathematiksystem" (MMS); Berlin schreibt „MMS (CAS)". Die Fassungen tragen
dieselben Kontexte; der Eingriff sitzt in einzelnen Teilaufgaben. In den
Brandenburger CAS-Heften trägt jede geänderte Aufgabe das Präfix „CAS:" im Titel;
fehlt es, ist die Aufgabe unverändert aus dem WTR-Heft übernommen. Die Berliner
CAS-Hefte sind durchgehend eigene Fassungen.

## 4 Kürzel und Werte

    papier: Jahr-Land-Niveau[-cas], klein und ohne Umlaute
            2017-be-gk · 2017-be-gk-cas · 2017-be-lk · 2017-be-lk-cas
            2017-bb-ea · 2017-bb-ea-cas · entsprechend 2018
            Die Werte stehen in abi-quellen.md § 2 und sind zugleich die
            Dateinamen des Korpus.
    block:  A (hilfsmittelfreier Teil; bis 2018 Aufgabenstellung 1 der
            bb-ea-Hefte) · B (Sachgebietsaufgaben)
    id:     Jahr-papier-BlockkürzelAufgabeTeilaufgabe, Aufgabe zweistufig
            2018-bb-ea-B2.1c · 2018-bb-ea-A1.2a · 2018-be-gk-B3.2e
    aufgabe: die Nummer wie im Heft, mit Punkt (2.1). Nicht umnummerieren –
            die Nummer ist der Rückweg ins Original.
    titel:  der Aufgabentitel des Hefts ohne das CAS-Präfix (Vase, Museum,
            Gartenteich); im hilfsmittelfreien Teil das Sachgebiet.
    stern:  leer. Es gibt keine Sternaufgaben; Niveauunterschiede stehen im
            papier-Kürzel.
    hilfsmittel: nein in block A, sonst ja.
    afb_amtlich: leer für 2017/2018 – diese Hefte weisen keine
            Anforderungsbereiche aus. Ab Erfassung von Poolaufgaben aus dem
            Erwartungshorizont zu füllen.
    seite:  Seite im PDF. Die Brandenburger Dateien sind Zusammenschnitte mit
            eigener Seitenzählung je Teil; die gedruckte Angabe weicht ab.
    punkte: Bewertungseinheiten (BE) laut der Tabelle am Ende jeder Aufgabe.

## 5 Sachgebiete

Feld `leitidee` trägt das Sachgebiet: **Analysis · Analytische Geometrie ·
Stochastik**.

Abweichung vom Profil msa, bewusst: Die Bildungsstandards der KMK kennen für die
Oberstufe fünf Leitideen (Algorithmus und Zahl, Messen, Raum und Form,
Funktionaler Zusammenhang, Daten und Zufall), und der Rahmenlehrplan weist sie
jeder Kompetenz zu. Sie sind aber quer zu den Sachgebieten – „Messen" tritt in
Analysis, Geometrie und Stochastik auf – und damit für die Zuordnung einer
Teilaufgabe nicht trennscharf. Die Prüfung selbst, die Kurshalbjahre und die
Prüfungsschwerpunkte sind nach Sachgebieten gegliedert. Lineare Algebra ist kein
eigener Wert: Die Prüfungsschwerpunkte führen Gleichungssysteme unter Analysis,
Vektoren unter Analytischer Geometrie.

## 6 Themenliste

Feste Ebene zwischen Sachgebiet und Typ. Abgeleitet aus den Prüfungsschwerpunkten
Brandenburg 2027 (LK und GK) und dem Rahmenlehrplan GOST Teil C Mathematik, gültig
ab 01.08.2022 (inhaltlich die Kapitel 2–4 des Brandenburger RLP vom 01.08.2018).
Stand v0.1, in der Feldprobe zu prüfen; Ergänzungen nur über den Bericht.

**Analysis:** Gleichungen lösen · Lineare Gleichungssysteme · Funktionsklassen und
Eigenschaften · Umkehrfunktion · Grenzwerte und Verhalten im Unendlichen ·
Ableitung und Änderungsrate · Ableitungsregeln · Tangente, Normale, Schnittwinkel ·
Kurvenuntersuchung · Ableitungsgraph und Funktionsgraph · Funktionsscharen und
Ortskurven · Rekonstruktion von Funktionsgleichungen · Extremalprobleme ·
Stammfunktion und Hauptsatz · Integrationsregeln · Flächeninhalt durch Integration ·
Rekonstruktion von Beständen · Uneigentliche Integrale · Rotationsvolumen

**Analytische Geometrie:** Punkte und Strecken im Koordinatensystem · Vektoren und
Rechenoperationen · Linearkombination und lineare Abhängigkeit · Geraden · Ebenen ·
Lagebeziehungen · Schnittmengen · Skalarprodukt und Winkel · Orthogonalität ·
Abstände · Flächeninhalt und Volumen im Raum · Scharen von Geraden und Ebenen ·
Spiegelung

**Stochastik:** Ereignisse und Mengenoperationen · Zufallsexperimente und
Urnenmodelle · Kombinatorik · Baumdiagramm und Pfadregeln · Vierfeldertafel ·
Bedingte Wahrscheinlichkeit und Bayes · Unabhängigkeit · Lage- und Streumaße einer
Stichprobe · Zufallsgrößen und Verteilungen · Binomialverteilung · Kenngrößen von
Verteilungen · Hypergeometrische Verteilung · Normalverteilung und Sigma-Regeln ·
Hypothesentests

Nur auf erhöhtem Niveau: Uneigentliche Integrale, Rotationsvolumen, Funktionsscharen
und Ortskurven, Scharen von Geraden und Ebenen, Normalverteilung und Sigma-Regeln,
Hypothesentests, goniometrische Gleichungen und Wurzelgleichungen innerhalb von
„Gleichungen lösen".

Nicht Prüfungsgegenstand (Prüfungsschwerpunkte 2027): Beweise erläutern oder
entwickeln (K1); Simulationen (L5). Aufgaben dieser Art erscheinen im Katalog
nicht, auch wenn der Rahmenlehrplan sie führt.

## 7 Besonderheiten beim Erfassen

- **Eine Leitfassung je Jahr und Niveau.** Auf erhöhtem Niveau bb-ea, weil sie den
  hilfsmittelfreien Teil enthält; auf grundlegendem be-gk, weil Brandenburg dort
  nichts veröffentlicht. Wortgleiche Zwillinge des anderen Landes werden nicht als
  Zeile erfasst, sondern in abi-pruefungen.md notiert. Eigene Zeile nur bei
  abweichender Teilung; Erkennungsregel ist der Vergleich der BE-Vektoren
  (abi-aufbau.md § 4).
- **CAS als Nachtrag**, und nur für Aufgaben mit „CAS:"-Präfix. Der Eingriff ist
  punktuell und sitzt in `gegeben`, `gesucht`, `punkte` und teils `verfahren`;
  typisch wird ein im WTR-Heft vorgegebener Kontrollwert in der CAS-Fassung selbst
  bestimmt.
- **Wahl ist keine Eigenschaft der Teilaufgabe.** Dass 2.1 und 2.2 zur Wahl stehen
  und dass 3.x und 4.x in bb-ea gekoppelt sind, steht in diesem Profil und in
  abi-pruefungen.md, nicht im Katalog.
- **Aufbauende Teilaufgaben.** Oberstufenaufgaben sind Ketten: Teilaufgabe d) nutzt
  das Ergebnis aus b). Feld `abhaengig_von` wird deutlich häufiger belegt als beim
  MSA. Kontrollangaben in eckigen Klammern („Zur Kontrolle: …") gehören nach
  `gegeben` der folgenden Teilaufgabe.
- **Umfang.** Eine Analysisaufgabe hat bis zu zehn Teilaufgaben und 50 BE. Ob
  `verfahren` und `schritte` diesen Umfang tragen, ist in der Feldprobe zu prüfen,
  bevor ein ganzes Heft erfasst wird.
- **Kein Volltext.** Beschreibung statt Wortlaut, auch bei den langen
  Aufgabenstämmen. Das Original wird nur für Wortlaut und Bild der Ankeraufgabe
  herangezogen.

## 8 Beispielzeilen

Folgen aus der Feldprobe an 2018-bb-ea; bis dahin gilt das Muster von msa.md § 8.

## 9 Offen

- Welches Land und welches Niveau schreibt der Schüler? Davon hängt die
  Erfassungsreihenfolge ab, nicht die Methode.
- Existiert in Brandenburg eine eigene Prüfung auf grundlegendem Niveau?
- Auf welcher Vereinbarung beruht das gemeinsame Aufgabenwerk, und welche Länder
  gehören dazu?
- Ab wann genau gilt in Berlin Teil A/Teil B, und seit wann in Brandenburg? Belegt
  ist: Brandenburg hatte den hilfsmittelfreien Teil bereits 2017, Berlin nach den
  Fachbriefen ab 2019.
