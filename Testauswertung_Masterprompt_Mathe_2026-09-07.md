# Testauswertung – Masterprompt und Prüfungsprompt

Gilt für Protokoll-Archive aus dem Masterprompt-Projekt (`[Thema]_[Typ]_[Datum]_protokoll.zip`, ab v3.28) und aus dem Aufgaben-Projekt (Prüfungsprompt ab v0.8). Maßgeblich ist je Prompt die höchste Versionsnummer im Repo mathe-nachhilfe. Die erste Zeile von `protokoll.txt` sagt, welcher Prompt und welches Profil gebaut hat; danach richtet sich, welche Punkte gelten.

Ziel der Auswertung: gleiche Qualität, weniger Korrekturrunden. Jede Korrekturrunde bekommt eine Klasse (Schritt 4); nur die ersten drei Klassen führen zu Änderungen, die letzten beiden sind Messwerte.

Testauftrag: Zu jeder Prompt-Lieferung nennt die Werkstatt Thema und Eingabe wortgleich, so gewählt, dass die geänderten Stellen im Archiv sichtbar werden (Stern, Hilfe-Seite, Grafik, Kasten – je nachdem, was sich geändert hat). Ein Bau je Prompt-Version; ein zweiter nur, wenn eine Änderung sonst nicht sichtbar wird. Für den Prüfungsprompt ist Prozentrechnung ohne Zusatz („prozent") die Vergleichseingabe; Messbasis neu ab v0.12. Das Start-PDF wird nur geprüft, wenn „start" ausdrücklich Testgegenstand ist (Aufgabe 1–2 wortgleich mit dem Heft). Für den Masterprompt zwei Themen je Lieferung, wenn eine Änderung an Übung, Vorstufe oder Kette geprüft wird – die Fertigkeiten darunter müssen sich unterscheiden.

Ablauf bei Upload eines Archivs: entpacken und in dieser Reihenfolge prüfen.

1. `protokoll.txt`
   - Kopfzeilen: Prompt-Version gegen den Repo-Stand; Vorlagenversion gegen Zeile 2 der mitgelieferten `mathblatt.sty` und gegen das Repo. Weicht die Vorlage vom Repo ab, ist das ein Befund für den Prompt (Abruf), nicht für die Vorlage.
   - Zählung gegen das PDF nachzählen (Hauptnummern, Grafiken, Seiten vor dem Begleitteil); geplante gegen gezählte Zahlen.
   - Masterprompt: Budget 6/2/4 und Schnitt gegen die Regel „so wenige Teile wie möglich" und gegen frühere Läufe desselben Themas: gleiche Teilzahl, gleiche Zuordnung der Typen. Prüfungsprompt: Typenliste gegen den Katalog (jeder Typ eine Hauptnummer, jede Hauptnummer ihre Decke), Katalog-ids der Originale stimmen.
   - Messzeile: Korrekturrunden, Sekunden, Anteil – gegen die vorigen Läufe. Planungszeit gegen die vorigen Läufe.

2. `chat.txt`
   - Deutungszeile gegen 1.2: Blattbezeichnung wortgleich, nur Ergänztes und Abgeleitetes.
   - Rückfragen gegen 1.1 und 1.4: nur die vorgesehenen, keine Erklärsätze davor, Buttonbeschriftungen nach Muster.
   - Ausgabeblock gegen 6.3; übergebene Dateinamen gegen 4.6.

3. PDF
   - Je Hauptnummer: leichter Einstieg; Masterprompt bis Kl. 10: Vorstufe (2.2 b, vier bis fünf) bei jedem Verfahren mit Erkennungsschritt, mit Antwortfeld; Grundfall in Teil 1 vier- bis fünfmal; die ersten sechs Teilaufgaben ohne die Sprossen ab der Mitte lösbar (zählen, nicht schätzen). Kette mit genau einem Merkmal je Schritt, keine Zahlenwiederholung, genau eine Teilaufgabe auf Prüfungshöhe am Ende (Masterprompt: geschätzt; Prüfungsprompt: verfremdetes Original mit Stern).
   - Masterprompt Aufgabe 1 (Übung): je Fertigkeit zwei leichte, eine mittlere, je Fallstrick eine; höchstens zwölf; Hinrichtung prüfen – jeder Fallstrick aus Aufgabe 1 kommt an einer Stelle des Blatts wieder, sonst wurde Ungebrauchtes geübt (P). Zuordnung im Begleitteil, keine Fokus-Zeile.
   - Masterprompt: Kasten in fester Zeilenform (3.1): je Zeile eine Regel, Varianten zusammen, höchstens fünf Zeilen, nichts aus der Vorstufe. Bis Kl. 10 `\weit` im .tex nach `\blattkopf` (4.6), Hilfe-Seite nur auf „mit hilfe" (4.2). Beide: Kopfzeile mit Blattbezeichnung, Legende in der Fußzeile nur bei Sternen (4.1), Hilfe-Seite nur wo vorgesehen und ohne Ergebnisse oder Zwischenwerte aus Teilaufgaben (4.2).
   - Ergebnisse stichprobenartig nachrechnen, mindestens drei je Blatt, bevorzugt Umkehrungen und Rundungsfälle; `pruef_out.txt` muss null Abweichungen zeigen. Ergebnisse ohne Senkrechtstrich (3.4); kein unerklärter Buchstabe, keine doppelt belegten Labels (3.6).

4. `.log`, `.tex`, `mathblatt.sty`, Anleitung
   - Jede Korrekturrunde aus dem Protokoll im .tex und .log nachvollziehen und einer Klasse zuordnen:
     V  Vorlagenfehler – das Makro tut nicht, was die Anleitung sagt → Repo (.sty).
     A  Makro falsch aufgerufen – die Anleitung war unklar oder ohne Beispiel → Repo (Anleitung).
     P  Inhalts- oder Regelfehler – Skript-Abweichung, Kette, Hilfe-Seite → Prompt.
     L  Layoutentscheidung – Achsenbereich, Umbruch, Seitenfüllung → Messwert; erst bei Wiederholung über Läufe hinweg ein Vorlagen-Befund (z. B. Achsenbereich aus den Punkten ableiten).
     F  Flüchtigkeit – Tippfehler, vergessene Umgebung → Messwert.
   - Layout: kurze Ketten (mehr als vier Teilaufgaben, Term plus Feld unter halber Satzbreite) in `teilezwei`, sonst Klasse A; Felder nicht allein in der nächsten Zeile (ab Vorlage 2026-09-07c Vorlagenfehler V).
   - Zeile „Vorlage: fehlende Bausteine · eigener TikZ · Warnungen": fehlende Bausteine in die Stufe-4-Liste der Anleitung; eigener TikZ prüfen, ob ein vorhandenes Makro gereicht hätte (dann Klasse A); Overfull- und mathblatt-Warnungen zuordnen.
   - Vorlagenänderungen werden in der Werkstatt gegen das .tex dieses Archivs und gegen alle gesammelten .tex früherer Archive kompiliert, bevor sie geliefert werden. Die gesammelten .tex bleiben in der Werkstatt, nicht im Repo.

Nicht im Archiv enthalten: wie Buttons und Rückfragen im Chat dargestellt wurden. Dafür Screenshots anfordern, wenn sie fehlen.

Ergebnis der Auswertung: Befunde sortiert nach Prompt, Vorlage, Anleitung und nicht beurteilbar; daraus gezielte Ersetzungen im betroffenen Prompt, je Änderung nur der betroffene Abschnitt, und geänderte .sty oder Anleitung mit Versionszeile. Quellenunabhängige Prompt-Änderungen (Abschnitte 3–6) in beiden Prompts (blatt-konzept §5). Keine Neustrukturierung. Budgetzahlen des Masterprompts (6 Hauptnummern, 2 Grafiken, 4 Seiten) erst ändern, wenn mehrere Läufe je Thema vorliegen.
