# Bewertung Masterprompt v3.34 – Mathe-Nachhilfe-Aufgabengenerator

Stand: 2026-09-08

## Kernbefund

Der Prompt ist handwerklich stark, verlangt vom Modell aber Reproduzierbarkeit und Selbstkontrolle, die ein Sprachmodell nicht liefert. Rechnen, Kompilat und Layout sind abgesichert; die eigentliche Qualitätsbehauptung – die didaktische Kette – prüft nur das Modell selbst.

## Was der Prompt will

Aus einem Wort („kreis") ein druckfertiges, im ersten Lauf einsetzbares Nachhilfeblatt als PDF – mit fester Progression je Aufgabe (Vorstufe → Grundfall → je Merkmal eine Sprosse → Prüfungsniveau), Pflichtelementen, LaTeX-Vorlage, Nachrechen-Skript und Protokoll-Archiv. Messlatte ist das Leitziel: „Ein Blatt, das nachgebessert werden muss, ist ein verlorenes Blatt."

## Wird er das erreichen?

Teilweise.

**Sicher gut abgedeckt:** Rechenfehler (Skript), Kompilierfehler, abgeschnittene Grafiken, Vollständigkeit der Typen.

**Unsicher:** Ob die Kette wirklich stimmt, ob ein Anfänger die ersten sechs Teilaufgaben schafft, ob der Schnitt sinnvoll ist. Das sind genau die Punkte, an denen ein Blatt im Unterricht scheitert – und genau die, für die 5.1 b) nur „prüfst du" sagt. Selbstprüfung durch dasselbe Modell, das den Fehler gemacht hat, fängt wenig.

## Was auffällt

1. **Der Prompt verletzt sein eigenes Budget.** „Höchstens sechs Hauptnummern; Übung, Fehler-finden, Begründen zählen mit." Das Beispiel Lineare Funktionen Teil 1 listet sieben Typen, dazu Aufgabe 1, dazu die Pflicht-Fehler-finden- und Begründungsaufgabe – neun bis zehn. Rechnet man ehrlich, bleiben je Teil drei Typen, und „typisch 2–3 Teile" wird zu 4–5. Entweder Budget oder Beispiel ist falsch.

2. **Reproduzierbarkeit wird behauptet, nicht hergestellt.** „So wenige Teile, wie das Budget erlaubt – nie mehr, damit dasselbe Thema bei jedem Lauf gleich geschnitten wird." Ein LLM schneidet nicht zweimal gleich. Enthält Teil 2 vom Vormonat andere Typen als Teil 2 von heute, bricht das Konzept „weiter". Abhilfe: ein Schnittkatalog im Repo für die häufigsten Themen, nicht eine Regel.

3. **„Maßstab ist die Erzeugungszeit"** – die kann das Modell vor dem Bau nicht kennen. Faktisch gelten die Zählgrenzen; der Satz stiftet nur Verwirrung.

4. **Unabhängigkeit des Prüfskripts ist Fiktion.** Aufgabe, Lösung und Skript stammen vom selben Modell im selben Lauf. Rechenschlampigkeit fängt es; ein systematischer Modellierungsfehler reproduziert sich. Trotzdem sinnvoll – nur nicht „unabhängig".

5. **Eingefrorene Fakten.** „Am Gymnasium seit 2025/26 keine P10", „seit 2026 getrennte Hefte EBR/FOR", FHR-Details. Ungeprüft; der Prompt sagt „recherchiere nur bei konkretem Zweifel" – also nie. Ändert sich etwas, erben alle Blätter den Fehler stillschweigend. Stand-Datum an diese Passage.

6. **Versionsdrift.** Kopf sagt v3.34, `protokoll.txt` soll „Masterprompt v3.33" schreiben.

7. **Zwei „erste" Werkzeugaufrufe.** 4.6 (Vorlage holen zu Beginn) und 6.3 (`date` allein als erster Aufruf).

8. **Patch-Akkretion.** 34 Versionen sieht man: viele Sätze sind erkennbar Reaktionen auf einen konkreten Fehllauf („das Sternzeichen tippst du nie", „nie aus dem Kontext abgetippt"). Jede Regel kostet Aufmerksamkeit, die beim LaTeX-Schreiben fehlt; Regelverstöße im Detail werden dadurch wahrscheinlicher, nicht seltener. Der Prompt ist an der Grenze, wo er selbst zur Fehlerquelle wird.

## Kritisch – das schwächste Glied

Die Kette (2.2 b) ist Herzstück und zugleich das einzige Element ohne externes Prüfsignal.

**Vorschlag 1:** Das Modell schreibt je Hauptnummer eine Tabelle ins Protokoll – Teilaufgabe, neues Merkmal, Vorgänger-Teilaufgabe. Was sich nicht in eine Zeile fassen lässt, ist keine Sprosse. Das zwingt zur Explizitheit statt Absichtserklärung und erlaubt einen Audit in 30 Sekunden, ohne das PDF durchzuarbeiten.

**Vorschlag 2:** Pflichtelemente vom Hauptnummern-Budget entkoppeln (Fehler-finden und Begründen als Teilaufgaben einer bestehenden Nummer zulassen), sonst frisst die Form die Typen.

## Was stimmt

Rangfolge, Rückwärtsplanung von der Prüfungsstufe, Merkmal statt Stückzahl, Verbot der Beispielzahlen und die Trennung Stoffstand/Anspruchslage sind sauber gedacht und besser als das meiste, was an Aufgabengenerator-Prompts kursiert.
