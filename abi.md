# PROFIL ABI – Zentrale schriftliche Abiturprüfung, Mathematik, Berlin/Brandenburg
Version 0.2 · 12.09.2026 · Kennung abi · gilt mit Kern v0.3 (Schema-Version 2)
Änderungen gegenüber 0.1: § 4 punkte und seite präzisiert, § 6 Themenlücken, § 7 um
vier Befunde der Feldprobe ergänzt, § 8 mit Beispielzeilen gefüllt, § 9 fortgeschrieben.

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
            Liegt die zugehörige Abbildung in einer Anlage auf einer anderen
            Seite, werden beide genannt (5|6).
    punkte: Bewertungseinheiten (BE) laut der Tabelle am Ende jeder Aufgabe.
            Im hilfsmittelfreien Teil steht keine Tabelle an den einzelnen
            Aufgaben; die BE aller drei Sachgebiete stehen gesammelt auf der
            letzten Seite von Teil 1, nach Teilgebiet und Buchstabe gegliedert
            (2018: Analysis 2 + 3, Geometrie 2 + 3, Stochastik 3 + 2 = 15).
            Die Herkunft der BE gehört in diesen Fällen nach bemerkung.

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

**Bekannte Lücken** (Feldprobe 2018-bb-ea 2.1). Zwei Fertigkeiten treten in
Analysisaufgaben auf, ohne dass die Analysis-Liste ein Thema dafür hätte:
die relative Abweichung zweier Funktionswerte in Prozent (2.1 f) und eine
elementargeometrische Nebenrechnung, hier der Flächeninhalt eines regelmäßigen
Sechsecks (2.1 i). Ursache ist die Regel, dass leitidee das Sachgebiet der
Aufgabenstellung trägt: „Flächeninhalt und Volumen im Raum“ würde passen, liegt
aber unter Analytischer Geometrie. Bis zur Entscheidung wird das nächstliegende
Thema gewählt und der Fall in bemerkung vermerkt. Erst nach mehreren Heften
entscheiden, ob die Liste ergänzt oder die Regel gelockert wird.

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
- **Mehrere Leistungen je Einheit sind der Normalfall.** Kern § 4 hält sie in
  einer Zeile: typ trägt die erste Leistung, typ_neben die weiteren. In der
  Feldprobe entfielen zehn von 21 Typen allein auf typ_neben. Das Feld thema ist
  dabei einwertig, obwohl die Einheit oft zwei Themen berührt (2.1 a: Nullstellen
  einer Schar und Grenzverhalten); ein zweites Thema ist nur mittelbar über
  typ_neben sichtbar. Folge für die Heft-Phase: ein Typ, der nur als Nebenleistung
  vorkommt, hat keine Ankeraufgabe, die als Decke taugt. Offen, ob typen.csv das
  markiert oder die Ankeraufgabe auf die Teilleistung zugeschnitten wird.
- **schritte trägt hier wenig.** Bei Deutungsaufgaben ohne Rechnung steht 0
  (2.1 h), bei langen Ketten ist der Wert eine Schätzung, weil Ableiten,
  Gleichsetzen, Fallunterscheidung und Randvergleich keine natürliche
  Schrittzahl haben. Das Feld wird gefüllt, aber nicht ausgewertet.
- **skizze meint Material, nicht Lösung.** Verlangt eine Aufgabe selbst eine
  Skizze (2.1 i: „mit Hilfe einer Skizze und einer Gleichung“), beschreibt das
  Feld ausnahmsweise die zu erstellende Skizze; der Fall wird in bemerkung
  kenntlich gemacht.
- **Kontrollangaben** in eckigen Klammern stehen in gegeben der Teilaufgabe, in
  der sie abgedruckt sind, und werden durch eigene Rechnung bestätigt; die
  Bestätigung wird in bemerkung vermerkt.
- **Kein Volltext.** Beschreibung statt Wortlaut, auch bei den langen
  Aufgabenstämmen. Das Original wird nur für Wortlaut und Bild der Ankeraufgabe
  herangezogen.

## 8 Beispielzeilen

Drei Zeilen aus der Feldprobe an 2018-bb-ea, zur Lesbarkeit als Feld = Wert; in
abi-katalog.csv stehen dieselben Werte als eine Zeile in der Reihenfolge der
Kopfzeile. Gewählt sind eine Zeile aus dem hilfsmittelfreien Teil und zwei aus
der Analysisaufgabe, darunter die mit der zu erstellenden Skizze.

    id = 2018-bb-ea-A1.2b · jahr = 2018 · papier = 2018-bb-ea · block = A · aufgabe = 1.2 ·
      titel = Analytische Geometrie · teilaufgabe = b · seite = 2
    punkte = 3 · stern =  · hilfsmittel = nein · afb_amtlich =
    leitidee = Analytische Geometrie · thema = Orthogonalität · typ = Eckpunkt eines Quadrates
      nachweisen · typ_neben = Schnittpunkt Gerade Koordinatenebene berechnen|Streckenlänge im
      Raum berechnen · stichwoerter =
      Quadrat|Diagonalenschnittpunkt|Halbdiagonalen|Skalarprodukt · voraussetzungen =
      Vektorlänge berechnen|Skalarprodukt bilden|Eigenschaften der Quadratdiagonalen kennen
    format = Begründung · operator = Zeigen Sie · antwort = Text
    material = keins · skizze = keine · kontext = ohne · textumfang = kurz
    gegeben = Quadrat mit Eckpunkt P(0 | 1 | 5) in der y-z-Ebene; die Gerade g mit x = (5 | 4 |
      1) + t · (1 | 0 | 0) verläuft orthogonal zur Trägerebene. Der Schnittpunkt der beiden
      Diagonalen des Quadrates liegt auf g. Der Punkt Q(0 | 8 | 4) liegt in der y-z-Ebene. ·
      gesucht = Nachweis, dass Q einer der beiden zu P benachbarten Eckpunkte des Quadrates ist
      · verfahren = Diagonalenschnittpunkt M als Schnittpunkt von g mit der y-z-Ebene bestimmen
      (x-Koordinate 0 setzen). Dann die Halbdiagonalen MP und MQ vergleichen: gleiche Länge
      zeigt, dass Q Eckpunkt ist, Skalarprodukt 0 zeigt, dass Q nicht der zu P
      gegenüberliegende, sondern ein benachbarter Eckpunkt ist. · schritte = 4 · zahlenraum =
      ganz · einheiten =  · abhaengig_von = 2018-bb-ea-A1.2a
    ergebnis = M(0 | 4 | 1). Mit MP = (0 | −3 | 4) und MQ = (0 | 4 | 3) ist |MP| = |MQ| = 5 und
      MP · MQ = −12 + 12 = 0. Im Quadrat sind die vier Halbdiagonalen gleich lang und die
      Diagonalen orthogonal, also ist Q ein zu P benachbarter Eckpunkt. · zwischenergebnis = M(0
      | 4 | 1)|MP = (0 | −3 | 4)|MQ = (0 | 4 | 3)|Seitenlänge |PQ| = 5·√2
    niveau_geschaetzt = II · fehlerquelle = gleiche Länge der Halbdiagonalen allein als Nachweis
      nehmen und den gegenüberliegenden Eckpunkt nicht ausschließen · bemerkung = BE aus der
      gesammelten Tabelle am Ende von Teil 1 (Teilgebiet Geometrie, b) 3 BE). Eigene Rechnung.

    id = 2018-bb-ea-B2.1a · jahr = 2018 · papier = 2018-bb-ea · block = B · aufgabe = 2.1 ·
      titel = Vase · teilaufgabe = a · seite = 5
    punkte = 8 · stern =  · hilfsmittel = ja · afb_amtlich =
    leitidee = Analysis · thema = Funktionsscharen und Ortskurven · typ = Nullstellen einer
      Funktionenschar mit Fallunterscheidung ermitteln · typ_neben = Grenzverhalten einer
      Exponentialfunktion untersuchen · stichwoerter =
      Funktionenschar|Nullstellen|Fallunterscheidung|Grenzwert · voraussetzungen = Satz vom
      Nullprodukt|quadratische Gleichung lösen|Vorzeichen der Exponentialfunktion kennen
    format = Rechnung|Begründung · operator = Ermitteln Sie|Untersuchen Sie · antwort =
      Term|Text
    material = keins · skizze = keine · kontext = ohne · textumfang = kurz
    gegeben = Funktionenschar f_a mit f_a(x) = (x² + a) · e^(0,5 − x), a ∈ IR; die Graphen der
      Schar sind G_a. · gesucht = Anzahl der Nullstellen von f_a in Abhängigkeit von a;
      Verhalten der Funktionswerte für x → ∞ und für x → −∞ · verfahren = Der Faktor e^(0,5 − x)
      ist stets positiv, also nur x² + a = 0 lösen: x² = −a mit Fallunterscheidung a < 0, a = 0,
      a > 0. Für x → ∞ dominiert der fallende Exponentialfaktor, für x → −∞ wachsen beide
      Faktoren unbeschränkt. · schritte = 5 · zahlenraum = ganz|Wurzel|Potenz · einheiten =  ·
      abhaengig_von =
    ergebnis = a < 0: zwei Nullstellen x = ±√(−a); a = 0: eine Nullstelle x = 0; a > 0: keine
      Nullstelle. Für x → ∞ gilt f_a(x) → 0, für x → −∞ gilt f_a(x) → +∞. · zwischenergebnis =
    niveau_geschaetzt = II · fehlerquelle = den Exponentialfaktor als möglichen Nullfaktor
      behandeln oder die Fallunterscheidung auf a < 0 und a > 0 verkürzen · bemerkung = Zwei
      Themen in einer Einheit: Nullstellen der Schar und Grenzverhalten. Das Feld thema ist
      einwertig, das zweite Thema (Grenzwerte und Verhalten im Unendlichen) erscheint nur über
      typ_neben. Eigene Rechnung.

    id = 2018-bb-ea-B2.1i · jahr = 2018 · papier = 2018-bb-ea · block = B · aufgabe = 2.1 ·
      titel = Vase · teilaufgabe = i · seite = 6
    punkte = 7 · stern =  · hilfsmittel = ja · afb_amtlich =
    leitidee = Analysis · thema = Rotationsvolumen · typ = Umbeschriebenes Prisma zu einem
      Rotationskörper bestimmen · typ_neben = Flächeninhalt eines regelmäßigen Sechsecks aus dem
      Inkreisradius berechnen|Sachzusammenhang durch Skizze und Gleichung darstellen ·
      stichwoerter = regelmäßiges Sechseck|Inkreisradius|Prisma|Mindestvolumen · voraussetzungen
      = regelmäßiges Sechseck in Dreiecke zerlegen|Inkreisradius und Seitenlänge
      umrechnen|Einheiten dm³ in cm³ umrechnen
    format = Zeichnen|Rechnung · operator = Stellen Sie dar|Ermitteln Sie · antwort =
      Grafik|Zahl
    material = keins · skizze = Im Heft ist keine Abbildung vorgegeben; die Skizze ist Teil der
      Lösung. Gefordert ist eine Draufsicht auf das regelmäßige Sechseck der Grundfläche mit
      eingezeichnetem Inkreis vom Radius r (maximaler Vasenradius), dem Inkreisradius als
      Abstand vom Mittelpunkt zur Seitenmitte und der Seitenlänge s. · kontext = Verpackung /
      Vase · textumfang = mittel
    gegeben = Die Vase hat die Länge 3 dm und einen maximalen Radius von ca. 1,07 dm. Sie soll
      stehend in einem Karton verpackt werden, der die Form eines regelmäßigen sechsseitigen
      Prismas besitzt. · gesucht = Zusammenhang zwischen dem maximalen Radius der Vase und der
      Grundfläche des Kartons als Skizze und Gleichung; Mindestvolumen des Kartons in cm³ ·
      verfahren = Der maximale Radius ist der Inkreisradius r des regelmäßigen Sechsecks. Aus s
      = 2r / √3 folgt für die Grundfläche A = 6 · (s · r / 2) = 2√3 · r². Die Prismenhöhe ist
      die Vasenlänge 3 dm, also V = 2√3 · r² · 3; Ergebnis in cm³ umrechnen. · schritte = 5 ·
      zahlenraum = dezimal|Wurzel · einheiten = dm|cm³ · abhaengig_von = 2018-bb-ea-B2.1g
    ergebnis = A = 2√3 · r² ≈ 3,98 dm² und V = 6√3 · r² ≈ 11,9 dm³, also muss der Karton
      mindestens etwa 11 900 cm³ Volumen haben. · zwischenergebnis = s = 2r / √3 ≈ 1,237 dm|A ≈
      3,98 dm²|V ≈ 11,94 dm³
    niveau_geschaetzt = III · fehlerquelle = den Umkreisradius statt des Inkreisradius mit dem
      Vasenradius gleichsetzen, oder dm³ nicht in cm³ umrechnen · bemerkung = Mit r = 0,65 · √e
      ≈ 1,0717 dm ergibt sich V ≈ 11 935 cm³, mit dem gerundeten r = 1,07 dm ≈ 11 898 cm³;
      beides rundet auf 11 900 cm³. Das Feld skizze beschreibt hier eine vom Prüfling zu
      erstellende Skizze, nicht vorhandenes Aufgabenmaterial. Die Teilaufgabe ist
      elementargeometrisch; die Themenliste Analysis führt dafür kein passendes Thema,
      ersatzweise Rotationsvolumen. Eigene Rechnung.

## 9 Offen

- Welches Land und welches Niveau schreibt der Schüler? Davon hängt die
  Erfassungsreihenfolge ab, nicht die Methode. Bis zur Antwort gilt die Annahme
  Brandenburg, erhöhtes Niveau, also bb-ea als Leitfassung.
- Bekommen Typen, die nur als typ_neben auftreten, eine eigene Markierung in
  typen.csv? Entscheidung nach dem ersten vollständigen Heft, da die Liste
  profilübergreifend ist und msa wie fhr mitbetroffen wären.
- Werden die Themenlücken aus § 6 durch neue Themen geschlossen oder durch eine
  Lockerung der Regel, dass leitidee das Sachgebiet der Aufgabenstellung trägt?
- Existiert in Brandenburg eine eigene Prüfung auf grundlegendem Niveau?
- Auf welcher Vereinbarung beruht das gemeinsame Aufgabenwerk, und welche Länder
  gehören dazu?
- Ab wann genau gilt in Berlin Teil A/Teil B, und seit wann in Brandenburg? Belegt
  ist: Brandenburg hatte den hilfsmittelfreien Teil bereits 2017, Berlin nach den
  Fachbriefen ab 2019.
