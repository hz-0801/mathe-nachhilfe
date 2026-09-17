# GELTUNG – Zielprüfung be-gk (Abitur Berlin, grundlegendes Anforderungsniveau – Grundkurs)
Version 1.0 · 17.09.2026 · Familie abi (Profile abi und iqb) · erzeugt aus abitur-vokabular.md v1.4 § 3 (Auftrag D „Namensschema, Erweiterbarkeit, Begründungen", Teil 2), Inhalt unverändert; Vollform der Kennung nach namensschema.md § 2: abi-be-gk

Zielprüfung: be-gk · Prüfungsart: Abitur · Träger: Berlin (Senatsverwaltung für Bildung, Jugend und Familie) · Niveau: grundlegend (Grundkurs)
Quelle der Themen: Prüfungsschwerpunkte 2027, ps_mathematik_2027_gk.pdf (berlin.de), gelesen am 13.09.2026 (Ablage abi-vorgaben.md § 1). ja = in den Schwerpunkten genannt, nein = nicht genannt; Geltung ist eine Eigenschaft des Themas, nicht der Zeile.
Themenliste: abitur-vokabular.md § 2 – jedes Thema der Liste hat in § 1 genau eine Zeile; abi-bau.py und iqb-bau.py lesen § 1 und prüfen das. Anmerkungen zu einzelnen Themen, zur Rechnerfassung und zur Ausschlussliste, die Regel „Geltung eines Hefts" und die Zwei-Spalten-Regel für gemeinsame Hefte: abitur-vokabular.md § 3.
Gebraucht von: abi-bau.py (Geltung je Heft, abi.md § 6), iqb-bau.py (Poolzeilen gegen alle Zielprüfungen des Profils abi, iqb.md § 6), Abbruchkriterium der Erfassung (iqb.md § 6), Blattbau (Filter über das Thema nach § 1, dann über die Zeile nach § 2).

## 1 Themen

39 von 48 Themen gelten.

| Thema | gilt |
|---|---|
| Gleichungen lösen | ja |
| Lineare Gleichungssysteme | ja |
| Funktionsklassen und Eigenschaften | ja |
| Umkehrfunktion | ja |
| Grenzwerte und Verhalten im Unendlichen | ja |
| Ableitung und Änderungsrate | ja |
| Ableitungsregeln | ja |
| Tangente, Normale, Schnittwinkel | ja |
| Kurvenuntersuchung | ja |
| Ableitungsgraph und Funktionsgraph | ja |
| Funktionsscharen und Ortskurven | nein |
| Rekonstruktion von Funktionsgleichungen | ja |
| Extremalprobleme | ja |
| Stammfunktion und Hauptsatz | ja |
| Integrationsregeln | ja |
| Flächeninhalt durch Integration | ja |
| Rekonstruktion von Beständen | ja |
| Uneigentliche Integrale | nein |
| Rotationsvolumen | nein |
| Punkte und Strecken im Koordinatensystem | ja |
| Vektoren und Rechenoperationen | ja |
| Linearkombination und lineare Abhängigkeit | ja |
| Geraden | ja |
| Ebenen | ja |
| Lagebeziehungen | ja |
| Schnittmengen | ja |
| Skalarprodukt und Winkel | ja |
| Orthogonalität | ja |
| Abstände | ja |
| Flächeninhalt und Volumen im Raum | ja |
| Scharen von Geraden und Ebenen | nein |
| Spiegelung | ja |
| Matrizen und Übergangsprozesse | nein |
| Ereignisse und Mengenoperationen | ja |
| Zufallsexperimente und Urnenmodelle | ja |
| Kombinatorik | ja |
| Baumdiagramm und Pfadregeln | ja |
| Vierfeldertafel | ja |
| Bedingte Wahrscheinlichkeit und Bayes | ja |
| Unabhängigkeit | ja |
| Lage- und Streumaße einer Stichprobe | ja |
| Zufallsgrößen und Verteilungen | ja |
| Binomialverteilung | ja |
| Kenngrößen von Verteilungen | ja |
| Hypergeometrische Verteilung | nein |
| Normalverteilung und Sigma-Regeln | nein |
| Hypothesentests | nein |
| Konfidenzintervalle | nein |

## 2 Ausgeschlossene Aufgabenformen

Die Einträge sind Aufgabenformen oder Lösungswege, keine Themen: sie schränken Zeilen innerhalb gültiger Themen ein und ändern keine Zeile von § 1 (abitur-vokabular.md § 3, Auftrag B Teil 5; Quelle STARK-Bände zum Abitur 2027, Vorspann S. I–III, Angabe des Lehrers – Verlagsdarstellung der amtlichen Vorgaben). Kein Feld und kein Skriptfilter; der Blattbau filtert damit über operator, verfahren und gegeben. Befund im Bestand vom 17.09.2026 (794 abi- und 1258 iqb-Zeilen).

| Ausschluss | Art | Befund im Bestand |
|---|---|---|
| Beweise erläutern oder entwickeln | Aufgabenform (Operator) | keine Zeile verlangt einen Beweis; „Weisen Sie nach"/„Zeigen Sie" sind Nachweise an konkreten Termen und bleiben zulässig |
| Simulationen | Aufgabenform | keine Zeile |
| Grenzwerte bei der Bestimmung von Ableitung oder Integral (h-Methode, Ober-/Untersumme, Streifenmethode) | Lösungsweg | 0 Zeilen in beiden Katalogen, die einen solchen Weg verlangen (das Wort „Obersumme" kommt nur als Fehlerquelle in 2025-bebb-lk 2.1 g vor); Differenzenquotienten im Bestand sind mittlere Änderungsraten, „Grenzwerte und Verhalten im Unendlichen" bleibt gültig |

## 3 Rechnerfassung

Fakt aus den Prüfungsschwerpunkten 2027, Abschnitt 3 „Hilfsmittel" (gelesen 15.09.2026; Erläuterung und zugelassene MMS-Funktionen in abitur-vokabular.md § 3). Regelfall ist der Taschenrechner ohne MMS (WTR-Fassung des Pools); Kurse mit MMS erhalten die MMS-Aufgaben. Die Wahl ist eine des Kurses, nicht der Prüfung.

| WTR | MMS | CAS | Fundstelle |
|---|---|---|---|
| zugelassen, Regelfall (Taschenrechner nach Abschnitt 3) | zugelassen für Kurse mit Prüfungsfach „Mathematik mit MMS (CAS)", dann MMS-Aufgaben | keine eigene Fassung, in Berlin „MMS (CAS)" | ps_mathematik_2027_gk.pdf, Abschnitt 3 (S. 6 mit Fußnote 1, S. 7), Abschnitt 2.2 (S. 2) |
