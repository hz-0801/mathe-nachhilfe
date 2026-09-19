# Nachlese Voraussetzungsfeld – Vorabprobe 2026-09-11d

Zweck: entscheiden, ob die Gegenlese-Blöcke eins bis acht nachzulesen sind. Sie haben ihre Nebenleistungsbestände über `typ_neben` erhoben; der 11d-Befund zeigt, dass das Feld `voraussetzungen` weitere Originale nennt.

Methode: handgepflegte Stichwortliste je Datei (18 Dateien, 54 Muster), Suche im Feld `voraussetzungen` aller 393 Originale, Treffer nur gezählt, wenn die id in der getroffenen Datei **nicht** vorkommt. Bewusst konservativ.

**Zwei Grenzen der Methode, ohne die das Ergebnis falsch gelesen wird:**
1. Das Raster kennt nur von Hand eingetragene Begriffe – es findet nur, was vorher erraten wurde. Die wirkliche Zahl kann höher liegen.
2. Nur **182 der 393 Originale** haben überhaupt ein gefülltes Feld `voraussetzungen`. Bei der anderen Hälfte greift die Methode nicht. Sie ersetzt die Verfahrenssuche nicht, sie ergänzt sie.

**Ergebnis: 29 Rohtreffer, davon rund ein Dutzend Fehlalarme** (das Muster „umrechnen“ für `einheiten.md` fängt auch „Bruch in Prozent umrechnen“ und „Anteil in Anzahl umrechnen“). Belastbar bleiben etwa siebzehn Fälle in fünf Dateien, alle bereits abgenommen:

- `einheiten.md` (sieben): 2014-OS-K4c, 2021-OS-K7a (Cent in Euro) · 2014-OS-K5d (m² und cm) · 2021-OS-K4a (cm³ in dm³) · 2022-OS-K2b, 2023-OS-K5b (1 cm³ = 1 ml) · 2023-OS-K5c (Meter in Zentimeter)
- `lineare-gleichungen.md` (fünf): 2022-OS-K2d, 2023-OS-K5d, 2024-OS-K6d, 2025-OS-K4c, 2026-FOR-K4c – jeweils das Umstellen einer Formel nach einer Größe
- `potenzen-wurzeln.md` (drei): 2026-FOR-K2c, 2026-FOR-K4a (Wurzel ziehen) · 2025-OS-K7b (Potenzen mit dem Taschenrechner)
- `prozentrechnung.md` (zwei): 2018-OS-B1j, 2019-OS-K4c (Prozentwert berechnen)
- `pythagoras.md` (einer, grenzwertig): 2026-FOR-K4c – „Gleichung nach der Hypotenuse umstellen“ ist eher ein Umstellfall als ein Pythagoras-Fall

**Bewertung:** Keiner dieser Fälle kippt eine Kennzahl. Kennzahl 5 und 6 prüfen die Nennung eines Originals im Eintrag seines CSV-Themas, und die ist überall erfüllt. Es geht um die Vollständigkeit der Nebenbestände, nicht um Fehler. Siebzehn Nachträge in fünf Dateien rechtfertigen keine Unterbrechung des Fahrplans; die Nachlese gehört als **Mechanik-Chat ans Ende von Schritt 5**, zusammen mit der breiten A4-Fassung und C4, falls der Lehrer sie will.

---

## Rohausgabe der Probe

```
PROBE Stichwortlisten: 18 Dateien | 54 Muster
PROBE Gegentest (muss >0 sein): 'Winkelsumme' in winkel-dreiecke.md: True

=== Originale, deren Voraussetzungsfeld auf eine Datei zeigt, in der die id NICHT steht: 29 ===
  einheiten.md: 16
  lineare-gleichungen.md: 5
  prozentrechnung.md: 4
  potenzen-wurzeln.md: 3
  pythagoras.md: 1

einheiten.md                 <- 2014-OS-K4c [Zuordnungen proportional und antiproportional]  :: Cent in Euro umrechnen
einheiten.md                 <- 2014-OS-K5d [Flächeninhalt und Umfang]  :: m² und cm umrechnen
einheiten.md                 <- 2018-OS-K3c [Daten darstellen]  :: Werte aus Säulendiagramm ablesen; Prozent in Länge umrechnen
einheiten.md                 <- 2018-OS-K3d [Diagramme lesen und beurteilen]  :: Anteil „jede 15.“ in Prozent umrechnen
einheiten.md                 <- 2019-OS-B1g [Wahrscheinlichkeit einstufig]  :: Anteil in Anzahl umrechnen
einheiten.md                 <- 2019-OS-K5b [Prozentrechnung]  :: Bruch in Prozent umrechnen
einheiten.md                 <- 2019-OS-K6b [Wahrscheinlichkeit mehrstufig]  :: Nenner nach jedem Zug anpassen; Bruch in Prozent umrechnen
einheiten.md                 <- 2019-OS-K7a [Exponentialfunktionen und Wachstum]  :: Prozentsatz in Wachstumsfaktor umrechnen
einheiten.md                 <- 2021-OS-K4a [Volumen und Oberfläche]  :: cm³ in dm³ umrechnen
einheiten.md                 <- 2021-OS-K4c [Maßstab]  :: Durchmesser aus Radius; Maßstab wählen und umrechnen; Kreis mit Zirkel
einheiten.md                 <- 2021-OS-K7a [Lineare Funktionen]  :: Cent in Euro umrechnen
einheiten.md                 <- 2022-OS-K2b [Volumen und Oberfläche]  :: 1 cm³ = 1 ml (im Heft angegeben)
einheiten.md                 <- 2023-OS-K5b [Volumen und Oberfläche]  :: 1 cm³ = 1 ml (im Heft angegeben)
einheiten.md                 <- 2023-OS-K5c [Flächeninhalt und Umfang]  :: Meter in Zentimeter umrechnen|Anzahl abrunden
einheiten.md                 <- 2025-OS-K6b [Daten darstellen]  :: Prozentsatz in Winkel umrechnen|Winkel mit Geodreieck abtragen
einheiten.md                 <- 2026-FOR-K7a [Exponentialfunktionen und Wachstum]  :: Prozentsatz in Wachstumsfaktor umrechnen
lineare-gleichungen.md       <- 2022-OS-K2d [Volumen und Oberfläche]  :: Formel nach r umstellen|Wurzel ziehen
lineare-gleichungen.md       <- 2023-OS-K5d [Volumen und Oberfläche]  :: 1 l = 1000 cm³|Formel nach h umstellen
lineare-gleichungen.md       <- 2024-OS-K6d [Sinussatz]  :: Winkelsumme im Dreieck|Gleichung umstellen
lineare-gleichungen.md       <- 2025-OS-K4c [Sinussatz]  :: Winkelsumme im Dreieck|Gleichung nach y umstellen
lineare-gleichungen.md       <- 2026-FOR-K4c [Trigonometrie im rechtwinkligen Dreieck]  :: Gleichung nach der Hypotenuse umstellen
potenzen-wurzeln.md          <- 2025-OS-K7b [Exponentialfunktionen und Wachstum]  :: Potenzen mit dem Taschenrechner
potenzen-wurzeln.md          <- 2026-FOR-K2c [Satz des Pythagoras]  :: Wurzel ziehen|rechtwinkliges Dreieck im Kegel erkennen
potenzen-wurzeln.md          <- 2026-FOR-K4a [Satz des Pythagoras]  :: Wurzel ziehen
prozentrechnung.md           <- 2018-OS-B1j [Wahrscheinlichkeit einstufig]  :: Prozentwert berechnen
prozentrechnung.md           <- 2019-OS-K4c [Volumen und Oberfläche]  :: Prozentwert berechnen; Volumen in Masse umrechnen
prozentrechnung.md           <- 2019-OS-K7a [Exponentialfunktionen und Wachstum]  :: Prozentsatz in Wachstumsfaktor umrechnen
prozentrechnung.md           <- 2026-FOR-K7a [Exponentialfunktionen und Wachstum]  :: Prozentsatz in Wachstumsfaktor umrechnen
pythagoras.md                <- 2026-FOR-K4c [Trigonometrie im rechtwinkligen Dreieck]  :: Gleichung nach der Hypotenuse umstellen
```

## Nachtrag 2026-09-11e (zehnter Block, `pythagoras.md`)

Zwei Ergebnisse der Gegenlese betreffen diese Liste.

**Ein Fall fällt weg.** Der hier geführte Eintrag `pythagoras.md <- 2026-FOR-K4c [Trigonometrie im rechtwinkligen Dreieck] :: Gleichung nach der Hypotenuse umstellen` ist ein Fehlalarm. Das Original rechnet AC = 29,24 : sin 22° im Parallelogramm; die umzustellende Gleichung ist eine Winkelfunktionsgleichung, und „Hypotenuse“ ist dort nur der Name der gesuchten Seite. Kein Pythagoras-Verfahren, keine Nebenleistung dieses Eintrags. Damit sinkt die Schätzung der belastbaren Fälle von etwa siebzehn auf etwa sechzehn und `pythagoras.md` fällt als Datei aus der Liste heraus; es bleiben vier Dateien – `einheiten.md` (sieben), `lineare-gleichungen.md` (fünf), `potenzen-wurzeln.md` (drei), `prozentrechnung.md` (zwei). Das bestätigt die in der Methode genannte Grenze: das Raster kennt nur die von Hand eingetragenen Begriffe und unterscheidet nicht, in welcher Rolle sie stehen.

**Ein Fall kommt hinzu, außerhalb der Blöcke eins bis acht.** `winkel-dreiecke.md` führt seit 11d als Nebenmarke der Einheit 3 das Erkennen des rechtwinkligen Teildreiecks in drei Teilaufgaben zweier Stämme (2022-OS-K5a, 2022-OS-K5d, 2023-OS-K7b). Die Verfahrenssuche des zehnten Blocks zeigt einen **vierten Fall derselben Sorte: 2017-OS-K4b** (Niveau II, zwei Punkte, CSV-Thema Trigonometrie im rechtwinkligen Dreieck, geführt von trigonometrie.md), dessen Voraussetzungsfeld „rechtwinkliges Dreieck P–B–Wandkopf erkennen“ nennt. Kein Fehler von `pythagoras.md` – das Erkennen ist kein Pythagoras-Verfahren – und keine Kennzahl hängt daran; es fehlt eine Zeile im Nebenbestand von `winkel-dreiecke.md`.

**Folgerung für den Zuschnitt des Mechanik-Chats:** Die Nachlese war bisher als Nachlese der Blöcke eins bis acht geplant, weil der neunte Block die Zwei-Felder-Regel schon anwandte. Der Fall 2017-OS-K4b zeigt, dass auch ein Block, der die Regel anwendet, einen Einzelfall übersehen kann – die Suche lief dort über die Winkelverfahren, nicht über das Erkennen des rechtwinkligen Dreiecks. Der Mechanik-Chat sollte `winkel-dreiecke.md` deshalb mitnehmen, aber nur für diesen einen Nachtrag.
