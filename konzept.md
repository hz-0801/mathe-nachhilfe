# KONZEPT – Arbeitsblätter aus alten Prüfungen
Stand 05.09.2026 · maßgebliche Grundlage; getroffene Entscheidungen werden ohne neuen Anlass nicht wieder aufgerollt

## 1 Ziel

Ein Nachhilfeschüler wird über Wochen gezielt auf die schriftliche Prüfung P10 Mathematik (Brandenburg, FOR-Niveau = MSA) vorbereitet. Grundlage sind die alten Prüfungen: Sie zeigen, welche Aufgabentypen vorkommen, in welcher Sprache und auf welcher Höhe. Aus ihnen entstehen immer wieder neue, druckfertige Arbeitsblätter zu einzelnen Typen oder Themen. Am Ende kann der Schüler eine vollständige Originalprüfung lösen.

Erfolgskriterium eines Blatts: Der Schüler löst danach Aufgaben dieses Typs auf Prüfungshöhe selbständig, und der Lehrer sieht am Blatt, an welcher Stufe er hängt.

## 2 Bausteine

    konzept.md             diese Datei
    katalog-prompt.md      Kern: Methode der Erfassung, prüfungsunabhängig
    msa.md                 Profil msa: alles, was an der P10 hängt (Quellen, Aufbau, Kürzel, Themenliste, Beispielzeilen)
    pruefungsprompt.md     Prüfungsprompt (bis v0.7 blatt-prompt.md): baut alle Prüfungen mit Katalog, heute Profil msa; Masterfassung hier, Projektanweisung ist Kopie (blatt-konzept.md §5)
    masterprompt.md        Masterprompt: baut alles ohne Katalog (Unterricht, Klassenarbeiten, Prüfungen ohne Katalog); Masterfassung hier, Projektanweisung ist Kopie
    CHANGELOG.md           Änderungshistorie der Prompts und der Vorlage
    mathblatt.sty          LaTeX-Vorlage (Version in Zeile 2); Anleitung_mathblatt.md gehört dazu – bis 2026-09-07 im Repo nachhilfe-arbeitsblatt-vorlage
    README.md              Landkarte: was im Repo liegt und wofür
    pruefungen.md          Heftliste mit Erfassungsstatus
    vorgaben.md            amtliche Vorgaben aus den Fachbriefen, Jahrescheck; gesonderter Baustein
    typen.csv              Typvokabular, wächst beim Erfassen
    katalog-basis.csv      Zeilen der Basisaufgaben
    katalog-kontext.csv    Zeilen der Kontextaufgaben
    typenbibliothek.md     abgeleitet aus dem Katalog, wird erzeugt, nie editiert (noch nicht vorhanden)
    pdf/                   Archiv der Hefte (noch nicht angelegt)

Alle Dateien liegen flach im Wurzelverzeichnis des Repos; das hält das Hochladen über die GitHub-Oberfläche einfach. Kommt ein zweites Profil, wird die Ordnung dann entschieden (eigenes Repo oder Präfixe).

Ablage: Repo hz-0801/mathe-nachhilfe (bis 2026-09-07 pruefungskatalog; öffentlich, damit curl ohne Anmeldung liest). Die Basis-URL steht in msa.md, im Prüfungsprompt (2.1, 4.6) und im Masterprompt (4.6) – vier Stellen, die bei anderer Ablage geändert werden. Claude liest per curl, der Lehrer lädt geänderte Dateien hoch. Geschrieben wird nur beim Aufbau und einmal im Jahr.

## 3 Entscheidungen

1. Die Einheit ist der Aufgabentyp, nicht die Aufgabe. Ein Typ ist eine Fertigkeit, die man als Einheit übt. Das Original ist Muster und Messlatte.
2. Auf dem Blatt gibt es drei Sorten Aufgaben: hinführende (leichter, eigene Struktur), die Originalfassung (Struktur und Wortlaut des Originals, neue Werte, leicht umformuliert) und weitere Varianten desselben Typs (gleiche Struktur, anderer Kontext). Struktur ändern nie – dann ist es ein anderer Typ. Auffüllende Aufgaben nach didaktischem Bedarf.
3. Decke ist das Original. Über das Prüfungsniveau geht kein Blatt hinaus.
4. Progression je Typ: hinführen, Anker, halten – nach dem Muster der Progressionsregeln aus dem Masterprompt (jede Hauptnummer beginnt leicht, endet auf Prüfungshöhe).
5. Keine Quellenangabe im Heft, auch nicht im Begleitteil; Herkunft (Jahr, Aufgabe) nur im Protokoll-Archiv (blatt-konzept.md v0.4).
6. Lösungen nach Aufgabensorte: Basis → Ergebnis; Kontext → Ergebnis mit Zwischenergebnissen; Original → knapper Lösungsweg mit Stichwort je Schritt, kein Text. Ergebnisse prüft das Skript, Lösungswege sind ungeprüft und deshalb knapp. Punkte stehen im Katalog (blatt-konzept.md v0.2).
7. Kein Log je Schüler. Wiederholung steuert der Lehrer; jedes Blatt hat neue Werte, eine ungeplante Wiederholung schadet nicht.
8. Keine Reserveprüfung. Für den Abschlusstest nimmt der Lehrer die Prüfung, die er am wenigsten verwendet hat.
9. Häufigkeit ist Auskunft, keine Priorität und kein Filter. Ein einziges Vorkommen ist ein vollwertiger Typ. Der Rahmenlehrplan setzt den Rahmen dessen, was kommen kann; er ist Hintergrund, keine Quelle für Typen.
10. Katalog vor Blatt: Alle Hefte werden einmal vollständig erfasst; Blätter entstehen nur aus dem Katalog. Die Hefte selbst holt der Blatt-Prompt nur für Wortlaut oder Bild einer Ankeraufgabe.
11. Der Katalog erfasst Fakten, nicht Nutzung: Zeile = kleinste Einheit mit eigener Punktangabe; Fakten getrennt von Deutung; Nachbau-Test als Erfolgskriterium; kein Volltext, sondern Verweis plus Strukturbeschreibung. Spätere Wünsche sind Umsortieren, im Ausnahmefall ein Nachtragslauf für ein Feld, nie ein Neustart.
12. Kern und Profil getrennt. Erstes Profil: msa (P10 Brandenburg, Niveau FOR). Zweites Profil abi (Abitur Brandenburg) folgt nach den MSA-Heften in eigenem Chat; Dateinamen mit Präfix abi-. Weitere Profile erst bei Bedarf; Vokabular und Häufigkeit gelten nie über Profile hinweg.
13. Vokabular in drei Ebenen: Leitidee und Thema fest im Profil (aus Rahmenlehrplan, Fachbrief-Inhaltsliste, Lehrwerkgliederung), Typ wächst aus den Heften in typen.csv, Abgleichlauf nach dem letzten Heft. Der Lehrer sieht die fertige Typenliste einmal durch; das ist optional.
14. Zwei Katalogdateien, Basis und Kontext, gleiches Schema; eine Typenliste.
15. Dateiform CSV mit Semikolon; Durchsicht über eine Prüftabelle im Chat, nicht in der Datei.
16. Ergebnisse sind eigene Rechnung, per Skript geprüft; Unsicheres trägt „?". Amtliche Lösungen gibt es im Profil msa nur für die Musteraufgaben 2028; für die FHR-Prüfung enthalten die veröffentlichten Lehrerhefte den Erwartungshorizont (2026-09-07).
17. Skizzen werden nicht übernommen, sondern aus dem Feld skizze mit der Vorlage neu gezeichnet; das Original-PDF ist Referenz. Foto und technische Zeichnung: Nachbau mit zeichenbarer Figur, Originalausschnitt nur als Notlösung.
18. Bestand: Oberschulhefte 2014–2026 und Musteraufgaben 2028. Gymnasialhefte nicht (seit 2025/26 keine P10 am Gymnasium).
19. Amtliche Vorgaben (Fachbriefe, Rundschreiben) werden gesondert in vorgaben.md geführt, mit einem jährlichen Check als eigenem Schritt. Der Katalog-Prompt liest sie nicht.
20. Die PDF-Pipeline aus dem Masterprompt (mathblatt.sty, xelatex, Skriptprüfung, Ausgabeblock) bleibt für die Blätter.
21. Versteckte Leistungen in einer Einheit bleiben eine Zeile; alle Leistungen werden in gesucht, ergebnis, format, typ und typ_neben erfasst; Punkte werden nicht geschätzt aufgeteilt.
22. Arbeitsweise Schritt für Schritt: Claude liefert Dateien mit Pfad und Namen, der Lehrer legt sie ab und meldet sich; dann nennt Claude den nächsten Schritt. Aufwendige Aktionen werden vorher angekündigt.

## 4 Verworfen

- Häufigkeitsschwelle und „Kerntypen": schließt aus, was die Prüfung trotzdem bringen kann.
- Reserveprüfung: Wiedererkennung bei neuen Werten klein, Bestand endlich.
- Log je Schüler: Schreibaufwand bei jeder Sitzung, Nutzen gering.
- Live-Analyse der Hefte je Blatt: langsam, teuer, jedes Mal anders kategorisiert.
- Virtuelle Unterzeilen mit geschätzten Punkten: Deutung im Faktenfeld.
- Volltext im Katalog: Kopie aller Hefte, sprengt Kontext und Projekt.
- Markdown-Tabelle als Katalog: bei 37 Feldern nicht lesbar.
- Ein Prompt für alle Prüfungen ohne Profil: verliert die konkreten Regeln, die Zeilen gut machen.
- Google Drive als Ablage: möglich, aber Dateien laufen bei jeder Sitzung durch den Kontext; Aktualisieren über den Konnektor ungetestet. Bleibt Alternative, falls das Hochladen zu lästig wird.

## 5 Offen

- Ablageort bestätigen (Basis-URL im Profil).
- Prüfungsjahr des Schülers: Annahme 2027 (aktuelles Format). Bei 2028 rücken hilfsmittelfreier Teil und Musteraufgaben nach vorn.
- Blatt-Prompt: noch nicht begonnen; Entwurf nach dem Probelauf, damit er gegen echte Katalogzeilen geschrieben wird.
- PDF-Archiv anlegen.
- Profil abi: Schülerart am Oberstufenzentrum klären (berufliches Gymnasium oder Fachoberschule), Quellen und Erwartungshorizonte prüfen.

## 6 Ablauf

1. Entwurf: abgeschlossen (Kern, Profil, Dateien, Vorgaben). Ablage flach im Repo pruefungskatalog.
2. Probelauf: abgeschlossen (2025, 2026 FOR, 2024; 89 Zeilen). EBR-Hefte zurückgestellt: kein EBR-Schüler, Aufgaben weitgehend Dubletten der FOR-Hefte.
3. Typenliste nach drei Heften festgezogen (Typen-Check 05.09.2026, 83 Typen gültig); Blatt-Prompt v0.1; zwei, drei Testblätter aus dem Katalog. Fehlt ein Feld, wird es jetzt ergänzt.
4. Restliche MSA-Hefte 2023 bis 2014 erfasst; Abgleichlauf nach dem letzten Heft abgeschlossen (Typen-Check 05.09.2026, 185 Typen gültig). Offen: Muster 2028 FOR erfassen; Typenbibliothek ableiten.
4a. Profil abi in eigenem Chat.
5. Blatt-Prompt fertigstellen.
Jährlich: Vorgabencheck (vorgaben.md), neues Heft erfassen, Typenbibliothek neu ableiten.

## 7 Änderungen

- 2026-09-05: angelegt.
- 2026-09-05: Probelauf abgeschlossen. EBR zurückgestellt, Profil abi vorgemerkt (Entscheidung 12 ergänzt). Typen-Check: drei Bruchteil-Typen zusammengelegt, Flächen-/Umfangsterm → „Term zu Figur zuordnen“, „Wahrscheinlichkeit zweistufig“ in unabhängig/ohne Zurücklegen getrennt, Mittelpunktswinkel als Baustein vermerkt; alle Typen auf „gültig“. Kern §1: Dateinamen nach Profil.
- 2026-09-05: Typen-Check nach Heften 2023–2019: 147 → 141 Typen, alle „gültig“. Zusammengelegt: Winkel im Trapez/Parallelogramm → „Winkel im Viereck berechnen“; Wahrscheinlichkeit zwei-/dreistufig → „… mehrstufig unabhängig“ und „… mehrstufig ohne Zurücklegen“ (Stufenzahl in gegeben/schritte); Flächenformel Dreieck/Rechteck angeben + Term zu Figur zuordnen → „Term zu Figur angeben“ (Leistung in format); Flächeninhalt Dreieck über Höhe → „Flächeninhalt Dreieck berechnen“ (Vorarbeit in typ_neben). Umbenannt: Lineare Kostenfunktion aufstellen → „Lineare Funktion aus Sachverhalt aufstellen“ (gegen „Lineare Gleichung aus Sachverhalt aufstellen“ abgegrenzt); Endwert linearer Zunahme → „… Veränderung“; Bruch in Prozent umwandeln → „Prozent und Anteil umwandeln“; Zehnerpotenz Exponent bestimmen → „Zehnerpotenzschreibweise umwandeln“; Säulendiagramm ergänzen → „Säulen- oder Balkendiagramm ergänzen“. Definitionen erweitert: Gleichung im Sachzusammenhang deuten (Bestandteile benennen), Term zu Sachtext zuordnen (auch Gleichungen), Proportionale Zuordnung Dreisatz (Abgrenzung zu Zeit aus Weg und Geschwindigkeit), Zufallsgerät entwerfen (Thema jetzt Wahrscheinlichkeit einstufig). Lösung durch Einsetzen prüfen: Thema Lineare Gleichungen. Getrennt gelassen: Gleichung/Graph zu Tarif zuordnen, Geradengleichung zu Graph zuordnen, Graph nach Eigenschaft auswählen (vier verschiedene Richtungen); Nullstelle berechnen vs. am Graphen ablesen. Zwei „?“ in gesucht (2026-FOR-K5b, 2024-OS-K3c) umformuliert.
- 2026-09-05: Typen-Check nach Heften 2018–2014 (Abgleichlauf): 193 → 185 Typen, alle „gültig“, typen.csv nach Leitidee (Lehrplanreihenfolge), Thema, Typ sortiert. Zusammengelegt: Zeit aus Weg und Geschwindigkeit + Dauer aus Menge und Durchsatz → „Dauer aus Menge und Rate berechnen“ (Gegenrichtung „Geschwindigkeit aus Weg und Zeit berechnen“ bleibt: andere Formelrichtung, wie bei Fläche/Seite); Verdopplungszeit am Graphen + Halbwertszeit aus Tabelle → „Verdopplungs- oder Halbwertszeit bestimmen“; Teilstrecke berechnen + Weglänge aus Teilstrecken → „Strecke aus Teilstrecken berechnen“; Körper zu Netz zuordnen + Körper im Schrägbild benennen → „Körper aus Netz oder Schrägbild benennen“; Jahreszinsen berechnen → „Prozentwert berechnen“, Zinssatz berechnen → „Prozentsatz berechnen“ (Zinsvokabular ist Kontext, Thema Zinsrechnung behält Guthabentabelle und Zinseszins). Gelöscht (Leistung steht in format bzw. bemerkung): „Lösungsweg beschreiben“ (2015-OS-K5d jetzt Flächeninhalt Dreieck berechnen, format Begründung – wie Mantellinie 2018-OS-K6d) und „Ergebnis sinnvoll runden“ (Konvention: Vermerk in bemerkung, kein Typ). Umbenannt: Teilwinkel berechnen → „Winkel aus Teilwinkeln berechnen“; Term zu Sachtext zuordnen → „Term zu Sachtext angeben“ (Angeben, Auswählen, Richtig/Falsch in format; 2016-OS-B1b hierher, Abgrenzung zu Lineare Gleichung aus Sachverhalt); Volumenterm zu Körper prüfen → „Term zu Körper angeben“ (parallel zu Term zu Figur angeben); Zahl zu Ungleichung angeben → „Zahl zu Bedingung angeben“ (auch „zwischen“, Abgrenzung zu Mitte zweier Zahlen); Masse aus Volumen berechnen → „Masse aus Volumen und Dichte berechnen“ (Gegenrichtung zu Volumen aus Masse und Dichte, getrennt wie bei Fläche/Seite). Definitionen erweitert: Wachstumstabelle ergänzen (Abnahme, fehlende Zeitangabe, Abgrenzung Guthabentabelle), Zufallsgerät entwerfen (Anzahl berechnen ohne Zeichnung), Graph zu Tarif zuordnen (lineare Tarife), Parabel verschieben (nur Scheitel), Wert aus Diagramm ablesen (Funktionsgraph im Sachzusammenhang), Flächeninhalt Dreieck (Rechenweg beschreiben), Proportionale Zuordnung Dreisatz (Abgrenzung Rate). Thema geändert: Mantelfläche Prisma berechnen → Volumen und Oberfläche (wie Mantelfläche Zylinder/Kegel). Belassen: Restfläche/Restvolumen, Mantellinie Kegel unter Pythagoras, Große Zahl mit Zehnerpotenz multiplizieren, Parabelgleichung zu Graph zuordnen, Zeitpunkt für Schwellenwert (schrittweise, anders als Ablesen). Typ_neben „Flächeninhalt Rechteck berechnen“ an 2018-OS-K6a und 2017-OS-K3b ergänzt. Prozessnotizen in bemerkung von neun Zeilen bereinigt, Fakten unverändert. 37 Katalogzeilen umetikettiert.
- 2026-09-06: Entscheidung 6 (Lösungen) an blatt-konzept.md v0.2 angeglichen.
- 2026-09-06: Basis-URL steht auch im Blatt-Prompt (§2). blatt-prompt.md v0.1 angelegt.
- 2026-09-06: Nr. 5 Herkunft → Protokoll; §2 blatt-prompt nur als Projektanweisung.
- 2026-09-07: §2 Prüfungsprompt (`pruefungsprompt.md`, vorher blatt-prompt) und Masterprompt mit Masterfassung im Repo, CHANGELOG.md; Aufteilung nach Quelle (blatt-konzept.md §5). Entscheidung 16 ergänzt: FHR-Lehrerhefte enthalten den Erwartungshorizont. Repo umbenannt in mathe-nachhilfe; Vorlage und Anleitung aus dem Vorlagen-Repo hierher, ein Repo für alles; Basis-URL an vier Stellen umgestellt.
