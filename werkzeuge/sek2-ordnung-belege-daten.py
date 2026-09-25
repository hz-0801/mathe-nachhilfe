"""Zuordnungsdaten für werkzeuge/sek2-ordnung-belege.py – je Sek-II-Eintrag ein Abschnitt.

L(eintrag, einheit, quelle, zeile oder [zeilen], erm='') – Verzeichniszeile(n) eines Lehrwerks, die den Inhalt der
  Einheit nennen; quelle: 'BK' Bigalke/Köhler, 'FDM' Fundamente Sek II B, 'EDM' Elemente Sek II NRW, 'NW' Neue Wege
  Sek II Berlin 2011; zeile = Zeilennummer der Quelldatei unter quellen/ (das Skript prüft, dass dort eine
  Verzeichniszeile steht, und liest Band, Kapitel und Seite selbst). erm = Ermessen mit Grund (gilt der ersten Zeile).
K(eintrag, einheit, quelle, grund) – „keine Stelle“ mit eigenem Grund.
R(eintrag, einheit, plan, von, bis, zitat='…', erm='') – Planstelle ('BE', 'BB', 'FOS'), die nicht aus
  katalog/_kursart-belege.md oder dem FOS-Zitat des Eintrags kommt; zitat muss in den Zeilen stehen.
E(eintrag, einheit, text) – Ermessen für die ganze Einheit.
Zeilen Bigalke/Köhler: Band 11 GK 43–129, Band 11 LK 131–227, Band 12 GK 229–277, Band 12 LK 279–346,
Abiturvorbereitung 348–381. Stand 2026-09-26 (Auftrag Nacht, Teil 3).
"""

# ==== kurvenuntersuchung ====
L('kurvenuntersuchung', 1, 'BK', [65, 155])
L('kurvenuntersuchung', 1, 'EDM', 50)
L('kurvenuntersuchung', 1, 'NW', 39, erm='„Zusammenhänge zwischen Funktion und Ableitung“ als Monotonie über das Vorzeichen von f′ gelesen.')
L('kurvenuntersuchung', 2, 'BK', [67, 157])
L('kurvenuntersuchung', 2, 'EDM', 51)
L('kurvenuntersuchung', 2, 'NW', 39, erm='„Zusammenhänge zwischen Funktion und Ableitung“ als Extrempunkte über f′ gelesen.')
L('kurvenuntersuchung', 3, 'BK', [66, 68, 156, 158])
L('kurvenuntersuchung', 3, 'EDM', [52, 53])
L('kurvenuntersuchung', 3, 'NW', 39, erm='„Zusammenhänge zwischen Funktion und Ableitung“ als Krümmung und Wendepunkte gelesen.')
L('kurvenuntersuchung', 4, 'BK', [60, 150], erm='„Die Ableitungsfunktion“ als Ableitungsgraph zum Funktionsgraphen gelesen.')
L('kurvenuntersuchung', 4, 'FDM', 89)
L('kurvenuntersuchung', 4, 'EDM', 41)
L('kurvenuntersuchung', 4, 'NW', 39)
L('kurvenuntersuchung', 5, 'BK', [70, 161])
L('kurvenuntersuchung', 5, 'EDM', 55, erm='„Funktionen untersuchen“ als vollständige Kurvenuntersuchung gelesen; der Sachzusammenhang ist nicht genannt.')
L('kurvenuntersuchung', 5, 'NW', 46)

# ==== binomialverteilung ====
L('binomialverteilung', 1, 'BK', [122, 220])
L('binomialverteilung', 1, 'EDM', [137, 234])
L('binomialverteilung', 1, 'NW', 155)
L('binomialverteilung', 2, 'BK', [122, 220], erm='Die Bernoulli-Formel als Teil der „Bernoulli-Ketten“ gelesen.')
L('binomialverteilung', 2, 'EDM', [137, 138, 234])
L('binomialverteilung', 2, 'NW', 155)
L('binomialverteilung', 3, 'BK', [124, 222], erm='„Praxis der Binomialverteilung“ als kumulierte Wahrscheinlichkeiten gelesen.')
L('binomialverteilung', 3, 'EDM', [139, 235])
L('binomialverteilung', 3, 'NW', 155)
L('binomialverteilung', 4, 'BK', [124, 222], erm='„Praxis der Binomialverteilung“ auch als Umkehraufgaben (n, p, k gesucht) gelesen.')
L('binomialverteilung', 4, 'EDM', [140, 237])
L('binomialverteilung', 4, 'NW', 155)
L('binomialverteilung', 5, 'BK', [123, 221])
L('binomialverteilung', 5, 'EDM', [141, 238])
L('binomialverteilung', 5, 'NW', 155)

# ==== ebenen ====
L('ebenen', 1, 'BK', [250, 301])
L('ebenen', 1, 'EDM', [117, 207])
L('ebenen', 1, 'NW', 104)
L('ebenen', 2, 'BK', [251, 302])
L('ebenen', 2, 'EDM', [118, 208, 209])
L('ebenen', 2, 'NW', 104, erm='„Ebenen im Raum“ als Parameter- und Koordinatenform gelesen; der Normalenvektor braucht das Skalarprodukt aus Kapitel 3.')
L('ebenen', 3, 'BK', [252, 303])
L('ebenen', 3, 'EDM', [118, 208], erm='Koordinatenform als Ebenen in besonderer Lage zu den Achsen gelesen.')
L('ebenen', 3, 'NW', 104)
L('ebenen', 4, 'BK', [253, 304])
L('ebenen', 4, 'EDM', [119, 210], erm='Lagebeziehungen als parallele Ebenen gelesen; der GK-Band nennt nur Geraden und Ebenen.')
L('ebenen', 4, 'NW', 104)

# ==== ableitung-und-aenderungsrate ====
L('ableitung-und-aenderungsrate', 1, 'BK', [58, 148])
L('ableitung-und-aenderungsrate', 1, 'FDM', 87)
L('ableitung-und-aenderungsrate', 1, 'EDM', 37)
L('ableitung-und-aenderungsrate', 1, 'NW', [31, 32])
L('ableitung-und-aenderungsrate', 2, 'BK', [59, 149])
L('ableitung-und-aenderungsrate', 2, 'FDM', 88)
L('ableitung-und-aenderungsrate', 2, 'EDM', [38, 39])
L('ableitung-und-aenderungsrate', 2, 'NW', 32)
L('ableitung-und-aenderungsrate', 3, 'BK', [59, 149], erm='„Die lokale Steigung einer Funktion“ als Grenzlage der Sekanten gelesen.')
L('ableitung-und-aenderungsrate', 3, 'FDM', 88)
L('ableitung-und-aenderungsrate', 3, 'EDM', 38)
L('ableitung-und-aenderungsrate', 3, 'NW', [32, 33])
L('ableitung-und-aenderungsrate', 4, 'BK', [60, 150, 70, 161], erm='Die Rate als Funktion: „Die Ableitungsfunktion“; ihre Extremwerte im Sachzusammenhang: „Kurvenuntersuchungen bei realen Prozessen“.')
L('ableitung-und-aenderungsrate', 4, 'FDM', 89)
L('ableitung-und-aenderungsrate', 4, 'EDM', 41)
L('ableitung-und-aenderungsrate', 4, 'NW', 33)

# ==== ableitungsregeln ====
L('ableitungsregeln', 1, 'BK', [61, 151])
L('ableitungsregeln', 1, 'FDM', [90, 91])
L('ableitungsregeln', 1, 'EDM', [42, 43])
L('ableitungsregeln', 1, 'NW', 38)
L('ableitungsregeln', 2, 'BK', [78, 169])
L('ableitungsregeln', 2, 'EDM', [105, 171], erm='GK-Band: „e-Funktionen ableiten“ als Kettenregel mit linearer innerer Funktion gelesen; der LK-Band nennt die Kettenregel.')
L('ableitungsregeln', 2, 'NW', 69)
L('ableitungsregeln', 3, 'BK', [78, 169])
L('ableitungsregeln', 3, 'EDM', [109, 171, 198])
L('ableitungsregeln', 3, 'NW', 69)

# ==== grenzwerte-und-verhalten-im-unendlichen ====
L('grenzwerte-und-verhalten-im-unendlichen', 1, 'BK', [57, 147, 55, 145], erm='„Grenzwerte von Funktionen“ und „Ganzrationale Funktionen“ als Verhalten im Unendlichen über den Leitterm gelesen.')
L('grenzwerte-und-verhalten-im-unendlichen', 1, 'FDM', 45, erm='„Ganzrationale Funktionen“ als Verhalten im Unendlichen gelesen.')
L('grenzwerte-und-verhalten-im-unendlichen', 1, 'EDM', 29, erm='„Ganzrationale Funktionen“ als Verhalten im Unendlichen gelesen.')
L('grenzwerte-und-verhalten-im-unendlichen', 1, 'NW', [56, 40])
L('grenzwerte-und-verhalten-im-unendlichen', 2, 'BK', [79, 170], erm='„Funktionsuntersuchungen“ im Kapitel Exponentialfunktionen als Grenzverhalten von Polynom mal e-Funktion gelesen.')
L('grenzwerte-und-verhalten-im-unendlichen', 2, 'EDM', [109, 198], erm='Produkte mit e-Funktionen als deren Grenzverhalten gelesen.')
L('grenzwerte-und-verhalten-im-unendlichen', 2, 'NW', 78, erm='„e-Funktionen in Realität und Mathematik“ als Grenzverhalten von e-Funktionstermen gelesen.')
L('grenzwerte-und-verhalten-im-unendlichen', 3, 'BK', [80, 171, 173], erm='Anwendungen von Exponentialfunktionen und Wachstumsprozesse als begrenztes Wachstum mit waagerechter Asymptote gelesen.')
L('grenzwerte-und-verhalten-im-unendlichen', 3, 'EDM', [107, 196])
L('grenzwerte-und-verhalten-im-unendlichen', 3, 'NW', 84)

# ==== gleichungen-loesen ====
L('gleichungen-loesen', 1, 'BK', [55, 145], erm='Ganzrationale Gleichungen als Nullstellen- und Schnittstellenbestimmung im Kapitel „Ganzrationale Funktionen“ gelesen.')
L('gleichungen-loesen', 1, 'FDM', 47)
L('gleichungen-loesen', 1, 'EDM', [31, 32])
L('gleichungen-loesen', 1, 'NW', 40, erm='„Ganzrationale Funktionen und ihre Graphen“ als ganzrationale Gleichungen gelesen.')
L('gleichungen-loesen', 2, 'BK', [77, 168, 176], erm='„Die natürliche Exponentialfunktion“ als Exponentialgleichung mit dem natürlichen Logarithmus gelesen; der LK-Band führt die Logarithmusfunktion eigens.')
L('gleichungen-loesen', 2, 'FDM', 56)
L('gleichungen-loesen', 2, 'EDM', [104, 200], erm='GK-Band: „Die e-Funktion“ als Gleichungen mit e und ln gelesen; der LK-Band nennt die Logarithmusfunktion.')
L('gleichungen-loesen', 2, 'NW', 77)
L('gleichungen-loesen', 3, 'NW', 57, erm='„Folgen und Gleichungen“ als numerisches Lösen gelesen.')
K('gleichungen-loesen', 3, 'BK', 'kein Kapitel zum Aufstellen und grafischen oder numerischen Lösen von Gleichungen')
K('gleichungen-loesen', 4, 'BK', 'kein Kapitel zu Ungleichungen')

# ==== umkehrfunktion ====
L('umkehrfunktion', 1, 'BK', [176, 177], erm='Logarithmus- und Wurzelfunktionen (nur LK-Band) als Umkehrfunktionen gelesen; das Verzeichnis nennt den Begriff nicht.')
L('umkehrfunktion', 1, 'EDM', [85, 169])
L('umkehrfunktion', 2, 'BK', [176, 177], erm='Wie Einheit 1: der Graph der Umkehrfunktion am Logarithmus und an der Wurzel.')
L('umkehrfunktion', 2, 'EDM', [85, 169])

# ==== tangente-normale-schnittwinkel ====
L('tangente-normale-schnittwinkel', 1, 'BK', [62, 152], erm='„Erste Anwendungen der Ableitung“ als Tangentengleichung gelesen.')
L('tangente-normale-schnittwinkel', 1, 'FDM', 92)
L('tangente-normale-schnittwinkel', 1, 'EDM', 44)
L('tangente-normale-schnittwinkel', 2, 'BK', [62, 152], erm='„Erste Anwendungen der Ableitung“ als Berührbedingung gelesen.')
L('tangente-normale-schnittwinkel', 2, 'FDM', 92)
L('tangente-normale-schnittwinkel', 2, 'EDM', 44)
L('tangente-normale-schnittwinkel', 3, 'BK', [62, 152], erm='„Erste Anwendungen der Ableitung“ als Normale gelesen; das Verzeichnis nennt sie nicht.')
L('tangente-normale-schnittwinkel', 3, 'EDM', 44)
L('tangente-normale-schnittwinkel', 4, 'FDM', 92)
L('tangente-normale-schnittwinkel', 4, 'BK', [62, 152], erm='„Erste Anwendungen der Ableitung“ als Steigungswinkel gelesen; das Verzeichnis nennt Winkel nicht.')
L('tangente-normale-schnittwinkel', 5, 'BK', [62, 152], erm='„Erste Anwendungen der Ableitung“ als Figuren aus Tangente und Achsen gelesen.')
L('tangente-normale-schnittwinkel', 5, 'FDM', 92, erm='„Tangente, Steigungs- und Schnittwinkel“ als Achsendreiecke der Tangente gelesen.')
L('tangente-normale-schnittwinkel', 5, 'EDM', 44, erm='„Tangenten und Normalen“ als Figuren aus Tangente, Normale und Achsen gelesen.')

# ==== extremalprobleme ====
for n in (1, 2, 3):
    L('extremalprobleme', n, 'BK', [71, 162])
    L('extremalprobleme', n, 'EDM', [80, 163])
    L('extremalprobleme', n, 'NW', 41)

# ==== funktionsklassen-und-eigenschaften ====
L('funktionsklassen-und-eigenschaften', 1, 'BK', [53, 143])
L('funktionsklassen-und-eigenschaften', 1, 'EDM', 26)
L('funktionsklassen-und-eigenschaften', 2, 'BK', [55, 145], erm='Nullstellen als Teil von „Ganzrationale Funktionen“ gelesen.')
L('funktionsklassen-und-eigenschaften', 2, 'FDM', 47)
L('funktionsklassen-und-eigenschaften', 2, 'EDM', [31, 32])
L('funktionsklassen-und-eigenschaften', 2, 'NW', 40, erm='„Ganzrationale Funktionen und ihre Graphen“ als Nullstellenverfahren gelesen.')
L('funktionsklassen-und-eigenschaften', 3, 'BK', [53, 143], erm='„Reelle Funktionen“ als Definitionsbereich und Wertemenge gelesen.')
L('funktionsklassen-und-eigenschaften', 3, 'EDM', 26, erm='„Funktionen und ihre Darstellungen“ als Definitions- und Wertebereich gelesen.')
L('funktionsklassen-und-eigenschaften', 4, 'BK', [55, 145], erm='Symmetrie als Teil von „Ganzrationale Funktionen“ gelesen.')
L('funktionsklassen-und-eigenschaften', 4, 'EDM', 30)
L('funktionsklassen-und-eigenschaften', 4, 'NW', 40, erm='„Muster in der Vielfalt“ als Symmetrie der Graphen gelesen.')
L('funktionsklassen-und-eigenschaften', 5, 'BK', [84, 180], erm='„Modifikationen von sin x und cos x“ als Transformationen gelesen; allgemeine Transformationen nennt das Verzeichnis nicht.')
L('funktionsklassen-und-eigenschaften', 5, 'FDM', [77, 78])
L('funktionsklassen-und-eigenschaften', 5, 'EDM', 28)
L('funktionsklassen-und-eigenschaften', 6, 'BK', [69, 159], erm='„Funktionsuntersuchung“ als Graph zeichnen und Graph zum Term zuordnen gelesen.')
L('funktionsklassen-und-eigenschaften', 6, 'FDM', 45, erm='„Ganzrationale Funktionen“ als Graph und Term gelesen.')
L('funktionsklassen-und-eigenschaften', 6, 'EDM', [54, 55])
L('funktionsklassen-und-eigenschaften', 6, 'NW', 40)

# ==== funktionsscharen-und-ortskurven ====
for n in (1, 2, 3, 4):
    L('funktionsscharen-und-ortskurven', n, 'BK', [160, 172, 184])
    L('funktionsscharen-und-ortskurven', n, 'EDM', [84, 168])
    L('funktionsscharen-und-ortskurven', n, 'NW', 70)
L('funktionsscharen-und-ortskurven', 5, 'BK', [160, 172], erm='„Funktionenscharen“ auch als Ortskurven gelesen; das Verzeichnis nennt sie nicht.')
L('funktionsscharen-und-ortskurven', 5, 'EDM', 168, erm='„Funktionenscharen“ (LK) als Ortskurven und Kurvenvergleich gelesen.')
L('funktionsscharen-und-ortskurven', 5, 'NW', 70)
E('funktionsscharen-und-ortskurven', 1, 'Elemente NRW führt „Funktionen mit einem Parameter“ auch im GK-Band (Z. 84); Bigalke/Köhler nur in den LK-Bänden.')

# ==== rekonstruktion-von-funktionsgleichungen ====
for n in (1, 2):
    L('rekonstruktion-von-funktionsgleichungen', n, 'BK', [72, 163])
    L('rekonstruktion-von-funktionsgleichungen', n, 'EDM', [83, 166])
    L('rekonstruktion-von-funktionsgleichungen', n, 'NW', 48)
L('rekonstruktion-von-funktionsgleichungen', 3, 'BK', [87, 183], erm='„Funktionsuntersuchungen und Modellierungen“ (trigonometrische Funktionen) als Sinusansatz gelesen.')
L('rekonstruktion-von-funktionsgleichungen', 3, 'FDM', 80)
L('rekonstruktion-von-funktionsgleichungen', 3, 'EDM', 172, erm='„Allgemeine Sinusfunktion“ (LK) als Sinusansatz aus Extremstellen gelesen.')

# ==== stammfunktion-und-hauptsatz ====
L('stammfunktion-und-hauptsatz', 1, 'BK', [91, 188])
L('stammfunktion-und-hauptsatz', 1, 'EDM', [94, 180], erm='Die Stammfunktion steht im Kapitel „Hauptsatz“; eine eigene Zeile nennt das Verzeichnis nicht.')
L('stammfunktion-und-hauptsatz', 1, 'NW', 63)
L('stammfunktion-und-hauptsatz', 2, 'BK', [92, 189])
L('stammfunktion-und-hauptsatz', 2, 'EDM', [94, 180])
L('stammfunktion-und-hauptsatz', 2, 'NW', 63)
L('stammfunktion-und-hauptsatz', 3, 'BK', [90, 187, 91, 188], erm='„Die Flächeninhaltsfunktion“ und „Stammfunktion“ als Graphenblick F′ = f gelesen.')
L('stammfunktion-und-hauptsatz', 3, 'EDM', [95, 181], erm='„Integralfunktion“ als Graphenblick F′ = f gelesen.')
L('stammfunktion-und-hauptsatz', 3, 'NW', 63)
L('stammfunktion-und-hauptsatz', 4, 'BK', [90, 187], erm='„Die Flächeninhaltsfunktion“ als Integralfunktion gelesen.')
L('stammfunktion-und-hauptsatz', 4, 'EDM', [95, 181])
L('stammfunktion-und-hauptsatz', 4, 'NW', 63)

# ==== integrationsregeln ====
L('integrationsregeln', 1, 'BK', [91, 188], erm='„Stammfunktion und unbestimmtes Integral“ als Regelsatz gelesen.')
L('integrationsregeln', 1, 'NW', 63, erm='„Integralfunktion, Stammfunktion und Hauptsatz“ als Regelsatz gelesen.')
L('integrationsregeln', 2, 'BK', [98, 195], erm='„Flächen unter nichtganzrationalen Funktionen“ als Integrieren mit vorgegebener Regel gelesen.')

# ==== flaecheninhalt-durch-integration ====
L('flaecheninhalt-durch-integration', 1, 'BK', [95, 96, 192, 193])
L('flaecheninhalt-durch-integration', 1, 'EDM', [97, 183])
L('flaecheninhalt-durch-integration', 1, 'NW', 64)
L('flaecheninhalt-durch-integration', 2, 'BK', [97, 194])
L('flaecheninhalt-durch-integration', 2, 'EDM', [98, 184])
L('flaecheninhalt-durch-integration', 2, 'NW', 64)
L('flaecheninhalt-durch-integration', 3, 'BK', [96, 193, 314], erm='Zusammengesetzte Flächen als „Flächen unter Funktionsgraphen“; das Körpervolumen aus Querschnitt und Länge als „Allgemeine Volumenformeln“ (nur LK 12).')
L('flaecheninhalt-durch-integration', 3, 'EDM', [97, 183], erm='Zusammengesetzte Flächen als Fläche zwischen Graph und x-Achse gelesen.')
L('flaecheninhalt-durch-integration', 3, 'NW', 64)
L('flaecheninhalt-durch-integration', 4, 'BK', [103, 201], erm='„Randkurvenprobleme“ als Flächenbedingungen gelesen.')
L('flaecheninhalt-durch-integration', 4, 'NW', 64)
L('flaecheninhalt-durch-integration', 5, 'BK', [95, 192])
L('flaecheninhalt-durch-integration', 5, 'EDM', [93, 179], erm='„Integral als Grenzwert“ als orientierter Flächeninhalt gelesen.')
L('flaecheninhalt-durch-integration', 5, 'NW', 62, erm='„Von der Änderungs- zur Bestandsfunktion“ als Flächenbilanz gelesen.')

# ==== rekonstruktion-von-bestaenden ====
for n in (1, 2, 3):
    L('rekonstruktion-von-bestaenden', n, 'BK', [99, 197])
    L('rekonstruktion-von-bestaenden', n, 'EDM', [92, 178])
    L('rekonstruktion-von-bestaenden', n, 'NW', 62)
L('rekonstruktion-von-bestaenden', 2, 'BK', [104, 202], erm='„Beschreibung von Prozessen“ als Rate und Bestand im Paar gelesen.')

# ==== rotationsvolumen ====
for n in (1, 2):
    L('rotationsvolumen', n, 'BK', 313)
    L('rotationsvolumen', n, 'EDM', 186)
L('rotationsvolumen', 1, 'NW', 64, erm='„Anwendungen der Integralrechnung“ als Rotationsvolumen gelesen; das Verzeichnis nennt es nicht.')

# ==== uneigentliche-integrale ====
for n in (1, 2):
    L('uneigentliche-integrale', n, 'BK', 196)
    L('uneigentliche-integrale', n, 'EDM', 185)

# ==== punkte-und-strecken-im-koordinatensystem ====
L('punkte-und-strecken-im-koordinatensystem', 1, 'BK', [233, 283])
L('punkte-und-strecken-im-koordinatensystem', 1, 'EDM', 60)
L('punkte-und-strecken-im-koordinatensystem', 1, 'NW', 97)
L('punkte-und-strecken-im-koordinatensystem', 2, 'BK', [235, 285], erm='Streckenlänge als Betrag im Kapitel „Rechnen mit Vektoren“ gelesen.')
L('punkte-und-strecken-im-koordinatensystem', 2, 'EDM', 61, erm='„Verschiebungen im Raum – Vektoren“ als Verbindungsvektor und Streckenlänge gelesen.')
L('punkte-und-strecken-im-koordinatensystem', 2, 'NW', 98, erm='„Bewegen im Raum – Vektoren“ als Streckenlänge und Teilpunkte gelesen.')
L('punkte-und-strecken-im-koordinatensystem', 3, 'BK', [240, 290])
L('punkte-und-strecken-im-koordinatensystem', 3, 'EDM', [115, 205], erm='Rechte Winkel am Dreieck über „Orthogonalität – Skalarprodukt“ gelesen.')
L('punkte-und-strecken-im-koordinatensystem', 3, 'NW', 109, erm='„Skalarprodukt und Winkel“ als Dreiecksnachweis gelesen.')
L('punkte-und-strecken-im-koordinatensystem', 4, 'BK', [240, 290])
L('punkte-und-strecken-im-koordinatensystem', 5, 'BK', [233, 283, 258, 310], erm='Körper im Koordinatensystem als „Punkte im Koordinatensystem“ und „Untersuchung geometrischer Objekte im Raum“ gelesen.')
L('punkte-und-strecken-im-koordinatensystem', 5, 'EDM', 60)
L('punkte-und-strecken-im-koordinatensystem', 5, 'NW', 97)

# ==== vektoren-und-rechenoperationen ====
L('vektoren-und-rechenoperationen', 1, 'BK', [234, 235, 284, 285])
L('vektoren-und-rechenoperationen', 1, 'EDM', [61, 62, 63])
L('vektoren-und-rechenoperationen', 1, 'NW', 98)
L('vektoren-und-rechenoperationen', 2, 'BK', [235, 285])
L('vektoren-und-rechenoperationen', 2, 'EDM', [62, 63])
L('vektoren-und-rechenoperationen', 2, 'NW', 98)
L('vektoren-und-rechenoperationen', 3, 'BK', [238, 288], erm='„Die Definition des Skalarproduktes“ als Skalarprodukt im Sachzusammenhang gelesen.')
L('vektoren-und-rechenoperationen', 3, 'EDM', [115, 205], erm='Das Skalarprodukt steht nur geometrisch („Orthogonalität – Skalarprodukt“).')
L('vektoren-und-rechenoperationen', 3, 'NW', 116, erm='„Von Tabellen zu Matrizen – Matrizen in Anwendungen“ als Mengen- mal Preisvektor gelesen.')

# ==== linearkombination-und-lineare-abhaengigkeit ====
L('linearkombination-und-lineare-abhaengigkeit', 1, 'BK', [235, 285], erm='Kollinearität und Linearkombination als Teil von „Rechnen mit Vektoren“ gelesen.')
L('linearkombination-und-lineare-abhaengigkeit', 1, 'EDM', 63, erm='„Vektoren vervielfachen“ als Kollinearität gelesen.')
L('linearkombination-und-lineare-abhaengigkeit', 1, 'NW', [98, 125], erm='„Vektorräume“ als lineare Abhängigkeit gelesen.')
L('linearkombination-und-lineare-abhaengigkeit', 2, 'BK', [235, 285], erm='Linearkombination als Teil von „Rechnen mit Vektoren“ gelesen.')
L('linearkombination-und-lineare-abhaengigkeit', 2, 'NW', 98)

# ==== geraden ====
L('geraden', 1, 'BK', [244, 294])
L('geraden', 1, 'EDM', 65)
L('geraden', 1, 'NW', 103)
L('geraden', 2, 'BK', [244, 294])
L('geraden', 2, 'EDM', 65)
L('geraden', 2, 'NW', 103)
L('geraden', 3, 'BK', [245, 295])
L('geraden', 3, 'EDM', 66)
L('geraden', 3, 'NW', 103)
L('geraden', 4, 'BK', [247, 297], erm='„Spurpunkte mit Anwendungen“ als Sachgeraden gelesen.')
L('geraden', 4, 'EDM', 64, erm='„Bewegungen auf dem Wasser“ als Sachgerade gelesen.')
L('geraden', 4, 'NW', 103)

# ==== lagebeziehungen ====
for n in (1, 2, 3):
    L('lagebeziehungen', n, 'BK', [253, 304])
    L('lagebeziehungen', n, 'EDM', [119, 210])
    L('lagebeziehungen', n, 'NW', 104)
L('lagebeziehungen', 4, 'BK', [247, 297], erm='„Spurpunkte mit Anwendungen“ als Schattenpunkt und Durchstoßpunkt gelesen.')
L('lagebeziehungen', 4, 'EDM', [120, 211])
L('lagebeziehungen', 4, 'NW', 104)

# ==== schnittmengen ====
L('schnittmengen', 1, 'BK', [253, 304])
L('schnittmengen', 1, 'EDM', [119, 210])
L('schnittmengen', 1, 'NW', 104)
L('schnittmengen', 2, 'BK', [245, 295])
L('schnittmengen', 2, 'EDM', 66)
L('schnittmengen', 2, 'NW', 103)
L('schnittmengen', 3, 'BK', [247, 252, 297, 303])
L('schnittmengen', 3, 'EDM', [119, 210], erm='Lagebeziehungen als Schnittgeraden gelesen; Spuren nennt das Verzeichnis nicht.')
L('schnittmengen', 3, 'NW', 104)

# ==== skalarprodukt-und-winkel ====
L('skalarprodukt-und-winkel', 1, 'BK', [238, 288])
L('skalarprodukt-und-winkel', 1, 'EDM', [115, 205])
L('skalarprodukt-und-winkel', 1, 'NW', 109)
L('skalarprodukt-und-winkel', 2, 'BK', [239, 246, 289, 296])
L('skalarprodukt-und-winkel', 2, 'EDM', [116, 206])
L('skalarprodukt-und-winkel', 2, 'NW', 109)
for n in (3, 4):
    L('skalarprodukt-und-winkel', n, 'BK', [256, 308])
    L('skalarprodukt-und-winkel', n, 'EDM', [121, 212])
    L('skalarprodukt-und-winkel', n, 'NW', 110)

# ==== orthogonalitaet ====
for n in (1, 2):
    L('orthogonalitaet', n, 'BK', [240, 290], erm='„Untersuchung von Figuren und Körpern“ als rechte Winkel über das Skalarprodukt gelesen.')
    L('orthogonalitaet', n, 'EDM', [115, 205])
    L('orthogonalitaet', n, 'NW', 109)
L('orthogonalitaet', 3, 'BK', [251, 302], erm='„Normalen- und Koordinatengleichung der Ebene“ als senkrecht zu Ebenen gelesen.')
L('orthogonalitaet', 3, 'EDM', [115, 205])
L('orthogonalitaet', 3, 'NW', 110, erm='„Winkel zwischen Geraden und Ebenen“ als Orthogonalität von Gerade und Ebene gelesen.')
L('orthogonalitaet', 4, 'BK', [257, 309], erm='„Abstandsberechnungen“ als Lotbedingung gelesen.')
L('orthogonalitaet', 4, 'EDM', 214, erm='„Abstände zu Geraden“ (LK) als Lotbedingung gelesen.')
L('orthogonalitaet', 4, 'NW', 111)

# ==== abstaende ====
L('abstaende', 1, 'BK', [235, 285], erm='Abstand zweier Punkte als Betrag im Kapitel „Rechnen mit Vektoren“ gelesen.')
L('abstaende', 1, 'NW', 98, erm='„Bewegen im Raum – Vektoren“ als Betrag gelesen.')
L('abstaende', 2, 'BK', [257, 309])
L('abstaende', 2, 'EDM', 213)
L('abstaende', 2, 'NW', 111)
L('abstaende', 3, 'BK', [257, 309], erm='„Abstandsberechnungen“ auch als Abstand Punkt–Gerade gelesen; der GK-Band führt das Kapitel ebenso.')
L('abstaende', 3, 'EDM', 214)
L('abstaende', 3, 'NW', 111)
L('abstaende', 4, 'BK', [257, 258, 309, 310])
L('abstaende', 4, 'NW', 111)

# ==== spiegelung ====
for n in (1, 2, 3):
    L('spiegelung', n, 'BK', [258, 310], erm='„Untersuchung geometrischer Objekte im Raum“ als Spiegelung und Symmetrie gelesen; das Verzeichnis nennt sie nicht.')
for n in (1, 2):
    L('spiegelung', n, 'NW', 118, erm='„Geometrische Abbildungen“ (Kapitel Matrizen) als Spiegelung gelesen.')

# ==== scharen-von-geraden-und-ebenen ====
for n in (1, 2):
    L('scharen-von-geraden-und-ebenen', n, 'BK', [298, 305])
L('scharen-von-geraden-und-ebenen', 3, 'BK', [298, 305], erm='Geraden- und Ebenenscharen auch mit Maßbedingungen gelesen.')
L('scharen-von-geraden-und-ebenen', 4, 'BK', 305, erm='„Ebenenscharen“ als Scharen am Körper gelesen.')

# ==== flaecheninhalt-und-volumen-im-raum ====
L('flaecheninhalt-und-volumen-im-raum', 1, 'BK', [239, 289])
L('flaecheninhalt-und-volumen-im-raum', 1, 'EDM', 209, erm='„Vektorprodukt“ (LK) als Dreiecksfläche gelesen.')
L('flaecheninhalt-und-volumen-im-raum', 2, 'BK', [239, 289, 240, 290])
L('flaecheninhalt-und-volumen-im-raum', 3, 'BK', [240, 290, 258, 310], erm='„Untersuchung von Figuren und Körpern“ und „Untersuchung geometrischer Objekte im Raum“ als Volumen und Oberfläche gelesen.')
L('flaecheninhalt-und-volumen-im-raum', 4, 'BK', [258, 310], erm='„Untersuchung geometrischer Objekte im Raum“ als zusammengesetzte Körper gelesen.')

# ==== matrizen-und-uebergangsprozesse ====
L('matrizen-und-uebergangsprozesse', 1, 'BK', 367, erm='Nur im Band Abiturvorbereitung; die Bände 11 und 12 führen keine Matrizen.')
L('matrizen-und-uebergangsprozesse', 1, 'NW', 116)
L('matrizen-und-uebergangsprozesse', 2, 'BK', 367, erm='Nur im Band Abiturvorbereitung.')
L('matrizen-und-uebergangsprozesse', 2, 'NW', [117, 118], erm='Fixvektoren als Teil von Übergangsprozessen und geometrischen Abbildungen gelesen.')
L('matrizen-und-uebergangsprozesse', 3, 'BK', 367, erm='Nur im Band Abiturvorbereitung; Verflechtung als Matrizenanwendung gelesen.')
L('matrizen-und-uebergangsprozesse', 3, 'NW', 116, erm='„Matrizen in Anwendungen“ als mehrstufige Produktion gelesen.')
for n in (4, 5):
    L('matrizen-und-uebergangsprozesse', n, 'BK', 368, erm='Nur im Band Abiturvorbereitung.')
    L('matrizen-und-uebergangsprozesse', n, 'NW', 117)

# ==== vierfeldertafel ====
for n in (1, 2):
    L('vierfeldertafel', n, 'BK', [119, 217])
    L('vierfeldertafel', n, 'EDM', [130, 226])
L('vierfeldertafel', 1, 'NW', 145, erm='„Bedingte Wahrscheinlichkeit“ als Vierfeldertafel gelesen; das Verzeichnis nennt sie nicht.')
L('vierfeldertafel', 2, 'NW', 143, erm='„Rechnen mit Ereigniswahrscheinlichkeiten“ als Additionssatz an der Tafel gelesen.')

# ==== bedingte-wahrscheinlichkeit-und-bayes ====
for n in (1, 2, 3):
    L('bedingte-wahrscheinlichkeit-und-bayes', n, 'BK', [118, 216])
    L('bedingte-wahrscheinlichkeit-und-bayes', n, 'EDM', [129, 225])
    L('bedingte-wahrscheinlichkeit-und-bayes', n, 'NW', 145)
L('bedingte-wahrscheinlichkeit-und-bayes', 2, 'EDM', 227)

# ==== unabhaengigkeit ====
for n in (1, 2):
    L('unabhaengigkeit', n, 'BK', [118, 216])
    L('unabhaengigkeit', n, 'EDM', [129, 225])
    L('unabhaengigkeit', n, 'NW', 145, erm='„Bedingte Wahrscheinlichkeit“ als Unabhängigkeit gelesen; das Verzeichnis nennt sie nicht.')
L('unabhaengigkeit', 3, 'BK', [118, 216], erm='Die Ausgleichs-Fehlvorstellung als Anwendung der Unabhängigkeit gelesen.')
L('unabhaengigkeit', 3, 'NW', 138, erm='„Empirisches Gesetz der großen Zahlen“ als Widerlegung des Ausgleichs gelesen.')

# ==== zufallsgroessen-und-verteilungen ====
for n in (1, 2):
    L('zufallsgroessen-und-verteilungen', n, 'BK', [121, 219])
    L('zufallsgroessen-und-verteilungen', n, 'EDM', [131, 228], erm='„Erwartungswert einer Zufallsgröße“ als Verteilung einer Zufallsgröße gelesen; eine eigene Zeile fehlt.')
    L('zufallsgroessen-und-verteilungen', n, 'NW', 154)

# ==== hypergeometrische-verteilung ====
L('hypergeometrische-verteilung', 1, 'BK', [117, 215], erm='„Kombinatorische Abzählverfahren“ als Quotient von Binomialkoeffizienten gelesen; die hypergeometrische Verteilung nennt das Verzeichnis nicht.')
L('hypergeometrische-verteilung', 1, 'FDM', [66, 67])
L('hypergeometrische-verteilung', 1, 'EDM', 223, erm='„Zählstrategien“ (LK) als Ziehen ohne Zurücklegen gelesen.')
L('hypergeometrische-verteilung', 1, 'NW', 144)
L('hypergeometrische-verteilung', 2, 'BK', [117, 215], erm='Wie Einheit 1.')
L('hypergeometrische-verteilung', 2, 'FDM', 67, erm='Ziehen ohne Reihenfolge als Kumulieren hypergeometrischer Wahrscheinlichkeiten gelesen.')
L('hypergeometrische-verteilung', 2, 'NW', 144)

# ==== kenngroessen-von-verteilungen ====
for n in (1, 2):
    L('kenngroessen-von-verteilungen', n, 'BK', [121, 219], erm='„Zufallsgrößen und Wahrscheinlichkeitsverteilung“ als Erwartungswert gelesen.')
    L('kenngroessen-von-verteilungen', n, 'EDM', [131, 228])
    L('kenngroessen-von-verteilungen', n, 'NW', 154)
L('kenngroessen-von-verteilungen', 3, 'BK', [123, 221], erm='„Eigenschaften von Binomialverteilungen“ als Standardabweichung gelesen; die allgemeine Varianz nennt das Verzeichnis nicht.')
L('kenngroessen-von-verteilungen', 3, 'EDM', [132, 229, 141, 238])
L('kenngroessen-von-verteilungen', 3, 'NW', [154, 155])
L('kenngroessen-von-verteilungen', 4, 'BK', [123, 221])
L('kenngroessen-von-verteilungen', 4, 'EDM', [141, 142, 238])
L('kenngroessen-von-verteilungen', 4, 'NW', 155)

# ==== normalverteilung-und-sigma-regeln ====
L('normalverteilung-und-sigma-regeln', 1, 'BK', [324, 328])
L('normalverteilung-und-sigma-regeln', 1, 'EDM', [247, 249])
L('normalverteilung-und-sigma-regeln', 1, 'NW', 156)
L('normalverteilung-und-sigma-regeln', 2, 'BK', [326, 328, 317, 262], erm='Die Sigma-Regeln stehen in beiden Band-12-Kapiteln „Prognose- und Konfidenzintervalle“ (GK Z. 262, LK Z. 317) für die Binomialverteilung; die Normalverteilung nur im LK-Band.')
L('normalverteilung-und-sigma-regeln', 2, 'EDM', [249, 244, 142])
L('normalverteilung-und-sigma-regeln', 2, 'NW', 156)
L('normalverteilung-und-sigma-regeln', 3, 'BK', 328, erm='„Die Normalverteilung bei stetigen Zufallsgrößen“ als Umkehraufgaben gelesen.')
L('normalverteilung-und-sigma-regeln', 3, 'EDM', 249)
L('normalverteilung-und-sigma-regeln', 3, 'NW', 156)

# ==== hypothesentests ====
for n in (1, 2):
    L('hypothesentests', n, 'BK', 333)
    L('hypothesentests', n, 'NW', 161)
L('hypothesentests', 3, 'BK', [332, 333])
L('hypothesentests', 3, 'NW', 161)
for n in (1, 2, 3):
    K('hypothesentests', n, 'EDM', 'die NRW-Ausgabe 2024/2025 führt keine Hypothesentests (Kapitel 7 endet bei der Normalverteilung)')

# ==== konfidenzintervalle ====
L('konfidenzintervalle', 1, 'BK', [264, 265, 319, 320])
L('konfidenzintervalle', 1, 'EDM', 245)
L('konfidenzintervalle', 1, 'NW', 160)
L('konfidenzintervalle', 2, 'BK', [265, 320])
L('konfidenzintervalle', 2, 'EDM', 245)
L('konfidenzintervalle', 2, 'NW', 160)
L('konfidenzintervalle', 3, 'BK', [266, 321])
L('konfidenzintervalle', 3, 'EDM', 246)
L('konfidenzintervalle', 3, 'NW', 160)

# ==== zufallsexperimente-und-pfadregeln ====
L('zufallsexperimente-und-pfadregeln', 1, 'BK', [111, 209])
L('zufallsexperimente-und-pfadregeln', 1, 'NW', [142, 143])
L('zufallsexperimente-und-pfadregeln', 2, 'BK', [112, 210], erm='„Relative Häufigkeit und Wahrscheinlichkeit“ als Laplace-Experimente gelesen.')
L('zufallsexperimente-und-pfadregeln', 2, 'NW', 142, erm='„Grundbegriffe stochastischer Modelle“ als Laplace-Modell gelesen.')
L('zufallsexperimente-und-pfadregeln', 3, 'BK', [113, 211])
L('zufallsexperimente-und-pfadregeln', 3, 'FDM', [64, 65])
L('zufallsexperimente-und-pfadregeln', 3, 'EDM', [128, 222])
L('zufallsexperimente-und-pfadregeln', 3, 'NW', 143, erm='„Rechnen mit Ereigniswahrscheinlichkeiten“ als Pfadregeln gelesen.')
L('zufallsexperimente-und-pfadregeln', 4, 'BK', [113, 211])
L('zufallsexperimente-und-pfadregeln', 4, 'FDM', 66)
L('zufallsexperimente-und-pfadregeln', 4, 'EDM', [128, 222], erm='„Mehrstufige Zufallsexperimente“ als Ziehen ohne Zurücklegen gelesen.')
L('zufallsexperimente-und-pfadregeln', 4, 'NW', 144, erm='„Zählen und Wahrscheinlichkeiten“ als Ziehen ohne Zurücklegen gelesen.')
L('zufallsexperimente-und-pfadregeln', 5, 'BK', [117, 215], erm='„Kombinatorische Abzählverfahren“ als Pfad mal Anzahl der Reihenfolgen gelesen.')
L('zufallsexperimente-und-pfadregeln', 5, 'FDM', 67)
L('zufallsexperimente-und-pfadregeln', 5, 'EDM', 223, erm='„Zählstrategien“ (LK) als Anzahl der Reihenfolgen gelesen.')
L('zufallsexperimente-und-pfadregeln', 5, 'NW', 144)
L('zufallsexperimente-und-pfadregeln', 6, 'BK', [113, 211, 118, 216], erm='Situationsbäume als Baumdiagramme mit bedingten Angaben gelesen.')
L('zufallsexperimente-und-pfadregeln', 6, 'FDM', 65, erm='„Sinnvoller Umgang mit Baumdiagrammen“ als Situationsbaum gelesen.')
L('zufallsexperimente-und-pfadregeln', 6, 'EDM', [129, 225], erm='„Bedingte Wahrscheinlichkeit“ als Situationsbaum mit totaler Wahrscheinlichkeit gelesen.')
L('zufallsexperimente-und-pfadregeln', 6, 'NW', 145)
L('zufallsexperimente-und-pfadregeln', 7, 'BK', [113, 211], erm='Terme lesen und aufstellen als Teil von „Mehrstufige Zufallsversuche/Baumdiagramme“ gelesen.')
L('zufallsexperimente-und-pfadregeln', 7, 'FDM', 65, erm='„Sinnvoller Umgang mit Baumdiagrammen“ als Term und Ereignis gelesen.')
L('zufallsexperimente-und-pfadregeln', 7, 'NW', 143, erm='„Rechnen mit Ereigniswahrscheinlichkeiten“ als Wahrscheinlichkeitsterme gelesen.')
L('zufallsexperimente-und-pfadregeln', 8, 'BK', [113, 211], erm='Rückwärtsaufgaben am Baum als Teil von „Mehrstufige Zufallsversuche/Baumdiagramme“ gelesen.')
L('zufallsexperimente-und-pfadregeln', 8, 'FDM', 65, erm='„Sinnvoller Umgang mit Baumdiagrammen“ als Rückwärtsaufgaben gelesen.')

# ==== kombinatorik ====
L('kombinatorik', 1, 'BK', [117, 215])
L('kombinatorik', 1, 'EDM', 223)
L('kombinatorik', 1, 'NW', 144)
L('kombinatorik', 2, 'BK', [117, 215])
L('kombinatorik', 2, 'FDM', 67)
L('kombinatorik', 2, 'EDM', [138, 223, 224])
L('kombinatorik', 2, 'NW', 144)
L('kombinatorik', 3, 'BK', [117, 215])
L('kombinatorik', 3, 'EDM', 223)
L('kombinatorik', 3, 'NW', 144)

# ==== lineare-gleichungssysteme (Sek-II-Einheit 5) ====
R('lineare-gleichungssysteme', 5, 'BE', 1054, 1055, zitat='ein algorithmisches Lösungsverfahren für lineare Gleichungssysteme erläutern',
  erm='Die Einheit fehlt in _kursart-belege.md (Sek-I-Eintrag); Stelle neu zugeordnet.')
R('lineare-gleichungssysteme', 5, 'BB', 894, 895, zitat='Gauß-Verfahren zur Lösung linearer',
  erm='Brandenburg führt lineare Gleichungssysteme zweimal: Q1 (Gauß-Verfahren, Lösbarkeit) und Q3 (bis zu drei Variablen, Schnittmengen).')
R('lineare-gleichungssysteme', 5, 'BB', 1204, 1205, zitat='lineare Gleichungssysteme mit bis zu drei')
L('lineare-gleichungssysteme', 5, 'BK', [47, 48, 49, 135, 136, 137, 138])
L('lineare-gleichungssysteme', 5, 'EDM', [82, 165])
L('lineare-gleichungssysteme', 5, 'NW', 47)

# ==== daten (Sek-II-Einheit 6) ====
R('daten', 6, 'BE', 1093, 1093, zitat='Lage- und Streumaße einer Stichprobe bestimmen und deuten,',
  erm='Die Einheit fehlt in _kursart-belege.md (Sek-I-Eintrag); Stelle neu zugeordnet.')
R('daten', 6, 'BB', 1059, 1060, zitat='Lage- und Streumaße einer Stichprobe')
L('daten', 6, 'BK', [107, 108, 205, 206])
L('daten', 6, 'FDM', [29, 30, 31])
L('daten', 6, 'EDM', [126, 219, 220])
L('daten', 6, 'NW', 149)

# ==== FOS-Zitate, die der Plantext so nicht führt ====
R('ableitungsregeln', 1, 'FOS', 1086, 1088, zitat='Ableitungsregeln: Konstanten-, Faktor-, Sum-',
  erm='Das FOS-Zitat des Eintrags („Konstanten-, Potenz-, Faktor-, Summenregel“) stellt die Regeln um; der Plantext Z. 1086–1088 lautet „Ableitungsregeln: Konstanten-, Faktor-, Summen- und Potenzregel (auch mit negativen Exponenten)“.')
R('kombinatorik', 1, 'FOS', 1194, 1194, zitat='Permutationen, Kombinationen, Variationen',
  erm='Das FOS-Zitat des Eintrags („Permutationen, Variationen“) kürzt die Plantextzeile „Permutationen, Kombinationen, Variationen“.')
