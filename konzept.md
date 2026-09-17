# KONZEPT – Arbeitsblätter aus alten Prüfungen
Stand 17.09.2026 · maßgebliche Grundlage; getroffene Entscheidungen werden ohne neuen Anlass nicht wieder aufgerollt

## 1 Ziel

Ein Nachhilfeschüler wird über Wochen gezielt auf die schriftliche Prüfung P10 Mathematik (Brandenburg, FOR-Niveau = MSA) vorbereitet. Grundlage sind die alten Prüfungen: Sie zeigen, welche Aufgabentypen vorkommen, in welcher Sprache und auf welcher Höhe. Aus ihnen entstehen immer wieder neue, druckfertige Arbeitsblätter zu einzelnen Typen oder Themen. Am Ende kann der Schüler eine vollständige Originalprüfung lösen.

Erfolgskriterium eines Blatts: Der Schüler löst danach Aufgaben dieses Typs auf Prüfungshöhe selbständig, und der Lehrer sieht am Blatt, an welcher Stufe er hängt.

## 2 Bausteine

    konzept.md             diese Datei
    katalog-prompt.md      Kern: Methode der Erfassung, prüfungsunabhängig
    msa.md                 Profil msa: alles, was an der P10 hängt (Quellen, Aufbau, Kürzel, Themenliste, Beispielzeilen)
    fhr.md, abi.md, iqb.md Profile fhr (Fachhochschulreife BB), abi (Zentralabitur BE/BB), iqb (Aufgabenpool des IQB);
                           Dateien je Profil mit Präfix: <kennung>-quellen.md, -pruefungen.md, -typen.csv, -katalog.csv, -bau.py;
                           iqb zusätzlich iqb-quellen.csv/.py (Kennungen)
    abitur-vokabular.md    gemeinsames Vokabular von abi und iqb (Sachgebiete, Themen, Geltung, Gegenstandsklassen, Regel Zeilenthema = Typthema), Entscheidungen 25 und 26
    abitur-typen.csv       gemeinsame Typenliste von abi und iqb (seit 15.09.2026, vorher abi-typen.csv und iqb-typen.csv)
    abi-<zielprüfung>-geltung.md  Geltung je Zielprüfung (be-gk, be-lk, bb-gk, bb-ea; seit 17.09.2026): Themen ja/nein, ausgeschlossene
                           Aufgabenformen, Rechnerfassung; das Profil nennt seine Zielprüfungen, die Bau-Skripte lesen die Dateien
    namensschema.md        Namensschema für Dateiarten und Kennungen (Vorschlag 17.09.2026, Auftrag D; Umbenennungen offen)
    abgleich.py            Abgleichlauf über die gemeinsame Typenliste und beide Kataloge (bis Lauf 11 iqb-abgleich.py)
    hefte/                 gescannte Verlagshefte (Stark) für abi ab 2019, lokal, per .gitignore nicht im Repo
    vorgaben.md, abi-vorgaben.md  amtliche Vorgaben mit Jahrescheck für msa bzw. abi/iqb
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
    <kennung>-typenbibliothek.md  abgeleitet aus dem Katalog, wird erzeugt, nie editiert; je Profil eine Datei
    <kennung>-typenbibliothek.py  erzeugt sie und hält die Zählweise als Code fest
                           für fhr vorhanden (12.09.2026), für msa noch nicht
    pdf/                   Archiv der Hefte (noch nicht angelegt)

Alle Dateien liegen flach im Wurzelverzeichnis des Repos; das hält das Hochladen über die GitHub-Oberfläche einfach. Kommt ein zweites Profil, wird die Ordnung dann entschieden (eigenes Repo oder Präfixe).

Ablage: Repo hz-0801/mathe-nachhilfe (bis 2026-09-07 pruefungskatalog; öffentlich, damit curl ohne Anmeldung liest). Die Basis-URL steht in msa.md, im Prüfungsprompt (2.1, 4.6) und im Masterprompt (4.6) – vier Stellen, die bei anderer Ablage geändert werden. Claude liest per curl, der Lehrer lädt geänderte Dateien hoch. Geschrieben wird nur beim Aufbau und einmal im Jahr.

## 3 Themenkatalog

Der Themenkatalog beschreibt den Stoff, nicht ein Blatt. Je Thema hält er fest, was
dazugehört und in welcher Reihenfolge man es lernt: Lerneinheiten, Voraussetzungen,
Grundvorstellung, typische Fehler, Merkkasten. Er wird einmal recherchiert und belegt
(Rahmenlehrplan, Lehrwerksgliederung, Förderliteratur, Prüfungsoriginale) und ist an
einer Stelle prüfbar und korrigierbar.

Beide Prompts lesen dieselbe Datei und nehmen daraus, was ihnen fehlt:

- Der Masterprompt bekommt die didaktische Struktur, die er sonst in jedem Lauf neu
  erfindet – Stoffauswahl, Reihenfolge, Niveau. Er erfindet dann nur noch Zahlen und
  Kontexte.
- Der Prüfungsprompt bekommt die Gliederung in Lerneinheiten, die der Prüfungskatalog
  nicht hat: Er kennt Typen und Originale, aber keine Lernreihenfolge.

Arbeitsteilung mit dem Prüfungskatalog: Der Themenkatalog sagt, **was** gelernt wird,
der Prüfungskatalog **wie hoch**. Die Decke einer Kette kommt immer aus dem
Prüfungskatalog der jeweiligen Prüfungsart; der Themenkatalog setzt keine Decke.

Daraus folgt, dass ein Eintrag prüfungsartübergreifend gilt. Die Lerneinheiten zu einem
Thema sind dieselben, ob der Schüler P10, FHR oder Abitur schreibt – verschieden ist nur
die oberste Sprosse. Ein Thema bekommt deshalb einen Eintrag, nicht einen je Profil.

Offen: Die vorhandenen Sek-I-Einträge führen Sprossen. Gemeint ist die Lernreihenfolge,
nicht die Teilaufgabenfolge eines Hefts – die baut der Prüfungsprompt aus den Originalen
(blatt-konzept.md §3). Ob die Trennung in der Praxis hält, entscheidet der erste
Testlauf: Bisher ist kein Blatt aus einem Katalogeintrag gebaut worden.

## 4 Entscheidungen

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
23. Eigenes Profil iqb für den Aufgabenpool des IQB (2026-09-13), nach dem Muster von fhr: gleicher Kern, eigenes Profil, eigene Katalogdatei, eigene Typenliste. Grund: Der Pool ist länderneutral und passt nicht in das abi-Kürzel Jahr-Land-Niveau. Der Pool liefert Typen und eicht über den Standardbezug die Niveauschätzung; die Landeshefte bleiben das Formatmodell. Zusammengeführt wird über die Typen, nicht über die Dateien. Reihenfolge: Prüfungsteil A vollständig, dann Teil B. Einheit des Laufs ist der Stapel (Prüfungsteil eines Pooljahrs auf einem Niveau); die Qualitätsschranke sitzt im Bau-Skript (Schwellenwerte für „?", neue Typen, fehlende Themen), nicht im Urteil des Lehrers, der keine Berichte liest. afb_amtlich trägt alle im Standardbezug vorkommenden Bereiche; die Eichung vergleicht mit dem höchsten.
24. Schnitt für Teil A des Pools: Thema × Gegenstandsklasse × Handlung (2026-09-13). Grund: Der Typ nach Kern § 6 ist für die Kurzaufgaben des Teils A so fein, dass fast jede Zeile ihr eigenes Etikett trägt (1,1 Zeilen je Typ nach sechs Stapeln, Wiederverwendung im Niveau 3–7 %); das Thema allein wirft Ungleiches zusammen (Matrizen: Verflechtung, Übergangsprozesse, Matrizenalgebra). Die Zwischenstufe trennt diese Fälle (Messung 13.09.2026: 114 Werte auf 197 Zeilen, Wiederverwendung im Niveau 38–47 %) und bündelt, was als Kette taugt. Umsetzung ohne neues Feld: Die Gegenstandsklasse steht als Präfix vor dem Doppelpunkt im Typnamen, die Klassenliste je Thema in iqb.md § 6; Themen, die selbst der Gegenstand sind, führen keine Unterklasse; die Handlung kommt aus format. Der Typ nach Kern § 6 bleibt als Feinetikett hinter dem Präfix; Umbenennungen und Zusammenziehungen laufen über iqb-abgleich.py (Kern § 9). Der Kern bleibt unverändert; für den Blattbau in Teil A zählt der Schnitt, nicht der Feintyp.
25. Gemeinsame Typenliste für abi und iqb, abi auf dem Typenschnitt nach Entscheidung 24 (2026-09-15). Grund: Die Messung (abi-iqb-typen.md) zeigte, dass 92 % der abi-Zeilen auf Schnittwerten liegen, die der Pool schon hat, und 36 % der abi-Typen ein inhaltsgleiches iqb-Gegenstück haben; die Landeshefte ab 2019 (Stark-Scans) nehmen Poolaufgaben auf. Umsetzung: abitur-vokabular.md als eine Quelle für Sachgebiete, Themenliste, Geltungstabelle, Gegenstandsklassen und Handlungen (abi.md und iqb.md verweisen darauf und führen nur Profilspezifisches); abitur-typen.csv als gemeinsame Typenliste mit beispiel_id in einem der beiden Kataloge; die Kataloge bleiben getrennt (abi-katalog.csv, iqb-katalog.csv); abgleich.py zieht beide Kataloge mit; abi-bau.py auf dem Stand von iqb-bau.py (Präfixregel, Schwellen, Eichung, Vollständigkeit). Pool-Teilaufgaben in Landesheften bekommen eine eigene abi-Zeile mit geteiltem Typ und dem Verweis „Dublette von: <iqb-id>" in bemerkung – kein bloßer Verweis ohne Zeile, kein neues Feld im Kern. Umstellungslauf 12: 938 → 875 Typen, 75 abi-Zeilen und 5 iqb-Zeilen umetikettiert (abi-pruefungen.md § 4). Der Kern bleibt unverändert; seine Sätze „Leitidee und Thema stehen im Profil" gelten über den Verweis des Profils.
26. Zeilenthema = Typthema für abi und iqb, Schnitt über das Thema des Typs (2026-09-16). Grund: 21 Zeilen (13 abi, 8 iqb) trugen ein anderes Thema als ihr Typ; der Schnitt des Gesamtbestands hing damit von der gezählten Spalte ab (189 gegen 183 Werte) – sechs Werte Unterschied bei einem Abbruchkriterium, dessen Schwelle bei fünf liegt. Tragen Zeile und Typ verschiedene Themen, ist eines von beiden falsch; der Schnittwert ist dann nicht definiert. Umsetzung: Lauf 13 von abgleich.py löst die 21 Fälle auf (18 Zeilen folgen dem Typ, drei Typen wechseln das Thema, ihre Zeilen folgen), beide Bau-Skripte erzwingen die Gleichheit für neue Zeilen und im Bestand, abgleich.py prüft sie nach jedem Lauf; die Regel steht in abitur-vokabular.md § 4. Die Teil-B-Reihen (grundlegend 7/3/2/2, erhöht 9/0/7/4/3) sind nachgerechnet und unverändert, keine Abbruchentscheidung kippt. Kern v0.4 zieht nur Text nach (Vokabulardatei vorgesehen, Etikettenänderungen im Abgleichlauf, Handlung je format in § 5, Markierungen in bemerkung); msa und fhr bleiben unberührt, fhr behält seine Regel Punkt-Schwerpunkt (fhr.md § 6).

## 5 Verworfen

- Häufigkeitsschwelle und „Kerntypen": schließt aus, was die Prüfung trotzdem bringen kann.
- Reserveprüfung: Wiedererkennung bei neuen Werten klein, Bestand endlich.
- Log je Schüler: Schreibaufwand bei jeder Sitzung, Nutzen gering.
- Live-Analyse der Hefte je Blatt: langsam, teuer, jedes Mal anders kategorisiert.
- Virtuelle Unterzeilen mit geschätzten Punkten: Deutung im Faktenfeld.
- Volltext im Katalog: Kopie aller Hefte, sprengt Kontext und Projekt.
- Markdown-Tabelle als Katalog: bei 37 Feldern nicht lesbar.
- Ein Prompt für alle Prüfungen ohne Profil: verliert die konkreten Regeln, die Zeilen gut machen.
- Google Drive als Ablage: möglich, aber Dateien laufen bei jeder Sitzung durch den Kontext; Aktualisieren über den Konnektor ungetestet. Bleibt Alternative, falls das Hochladen zu lästig wird.

## 6 Offen

- Ablageort bestätigen (Basis-URL im Profil).
- Prüfungsjahr des Schülers: Annahme 2027 (aktuelles Format). Bei 2028 rücken hilfsmittelfreier Teil und Musteraufgaben nach vorn.
- Blatt-Prompt: noch nicht begonnen; Entwurf nach dem Probelauf, damit er gegen echte Katalogzeilen geschrieben wird.
- PDF-Archiv anlegen.
- Profil abi: Schülerart am Oberstufenzentrum klären (berufliches Gymnasium oder Fachoberschule), Quellen und Erwartungshorizonte prüfen.

## 7 Ablauf

1. Entwurf: abgeschlossen (Kern, Profil, Dateien, Vorgaben). Ablage flach im Repo pruefungskatalog.
2. Probelauf: abgeschlossen (2025, 2026 FOR, 2024; 89 Zeilen). EBR-Hefte zurückgestellt: kein EBR-Schüler, Aufgaben weitgehend Dubletten der FOR-Hefte.
3. Typenliste nach drei Heften festgezogen (Typen-Check 05.09.2026, 83 Typen gültig); Blatt-Prompt v0.1; zwei, drei Testblätter aus dem Katalog. Fehlt ein Feld, wird es jetzt ergänzt.
4. Restliche MSA-Hefte 2023 bis 2014 erfasst; Abgleichlauf nach dem letzten Heft abgeschlossen (Typen-Check 05.09.2026, 185 Typen gültig). Offen: Muster 2028 FOR erfassen; Typenbibliothek ableiten.
4a. Profil abi in eigenem Chat.
4b. Profil iqb (2026-09-13): Prüfungsteil A in 22 Stapeln, dann Teil B; Abgleichlauf nach jedem Stapel.
5. Blatt-Prompt fertigstellen.
Jährlich: Vorgabencheck (vorgaben.md), neues Heft erfassen, Typenbibliothek neu ableiten.

## 8 Eine neue Prüfung aufnehmen

Reihenfolge für ein neues Profil (Beispiel in namensschema.md § 2:
Niedersachsen, Abitur, grundlegendes Niveau – Profil abi-ni). Stand
17.09.2026 (Auftrag D, Teil 4); die Erfahrung dahinter sind die vier Profile
msa, fhr, abi, iqb und ihre Prüfungslisten.

**Zuerst zu klären, in dieser Reihenfolge** – jede Antwort bestimmt eine
Kennung oder eine Regel des Profils:

1. **Träger (Land oder Institution).** Wer stellt die Prüfung, wer
   veröffentlicht Hefte, Lösungen und Vorgaben? Amtliches Länderkürzel als
   Träger-Baustein (namensschema.md § 2); ein länderübergreifender Pool ist
   ein Träger ohne Land (iqb). Ein gemeinsames Werk zweier Länder ist ein
   Profil mit beiden Kürzeln (bebb), auch wenn die Länder verschieden daraus
   zusammenstellen.
2. **Schulform.** Hängt der Inhalt von der Schulform ab (P10: Oberschule
   gegen Gymnasium; Fachoberschule)? Nur dann kommt die Schulform in die
   Kennung; sonst weggelassen (Entscheidung 18: msa nur Oberschule).
3. **Niveau.** Kennt die Prüfung Niveaus, und wie trägt das Heft sie – im
   selben Heft mit Kennzeichnung (msa bis 2025: Sternchen, Feld stern), in
   getrennten Heften (abi: gk/lk, Feld papier) oder gar nicht (fhr)? Das
   Niveau-Kürzel ist das des Trägers, nicht vereinheitlicht.
4. **Zielprüfung(en).** Für welche Prüfung(en) soll der Katalog Material
   liefern? Je Zielprüfung eine Geltungsdatei aus den amtlichen
   Schwerpunkten (Themen ja/nein, ausgeschlossene Aufgabenformen,
   Rechnerfassung; abitur-vokabular.md § 3, Teil 2 des Auftrags D). Gibt es
   keine Schwerpunkte (P10: „prüfungsrelevant ist der Rahmenlehrplan",
   vorgaben.md), gibt es keine Geltung – dann gilt die ganze Themenliste.
5. **Quellenlage.** Liegen die Hefte amtlich vor (Bildungsserver), nur im
   Verlag (STARK, lokal unter hefte/, nicht im Repo) oder gar nicht?
   Gibt es einen amtlichen Erwartungshorizont (fhr, iqb: Kern § 3 d
   „amtliche Lösung vorhanden", ergebnis mit „(amtlich)", afb_amtlich
   möglich) oder nicht (msa, abi: eigene Rechnung, Schätzung ohne Maßstab)?
   Das entscheidet die Ergebnisregel, die Eichung (Kern § 5: Kennzahl oder
   Schranke) und ob eine Quellenliste erzeugt werden muss (iqb-quellen.py).
6. **Rechnerfassung.** Gibt es Parallelfassungen (WTR/CAS/MMS)? Dann ist die
   Fassung ohne MMS der Hauptzweig und jede andere ein Delta, das je Niveau
   an einem Stapel gemessen wird (Entscheidung 27); Kürzel als Suffix
   (-cas, -mms).
7. **Aufbau der Hefte.** Teile (Feld block), Aufgabenstamm, Punktangaben
   je Buchstabe (Zeilenregel Kern § 4), Wahlaufgaben, Punktschlüssel je
   Jahrgang (abi.md § 11). Daraus folgen KONFIG des Bau-Skripts (soll je
   Aufgabe) und das id-Muster.
8. **Leitideen und Themenliste.** Aus Lehrplan, Schwerpunkten und
   Lehrwerksgliederung (Entscheidung 13). Gleiche Prüfungsart wie ein
   vorhandenes Profil → dessen Vokabular und Typenliste teilen (§ 9); andere
   Prüfungsart → eigene Listen, die vorhandenen als Muster (befund-typenlisten.md).

**Welche Dateien entstehen, in dieser Reihenfolge** (Namen nach
namensschema.md § 2; bis zur Entscheidung über die Umbenennungen dort mit
den heutigen Kurzkennungen):

1. `<profil>.md` – das Profil: Prüfung, Ablage und Quellen, Aufbau, Kürzel
   und Werte, Leitideen, Themenliste, Zeile „Zielprüfungen:", Besonderheiten
   beim Erfassen, Beispielzeilen (nach dem ersten Heft aus dem Katalog),
   Offenes. Vorlage: iqb.md (mit Erwartungshorizont) oder abi.md (ohne).
2. `<profil>-quellen.md` – Verzeichnis, Dateinamen, papier-Kürzel,
   Seitenzahlen, lokaler Heftordner; bei großen Quellen dazu
   `<profil>-quellen.csv` mit Erzeuger `<profil>-quellen.py`.
3. `<zielprüfung>-geltung.md` je Zielprüfung (Frage 4); jedes Thema der
   Liste braucht eine Zeile, die Bau-Skripte prüfen das.
4. `<profil>-vorgaben.md` – amtliche Vorgaben mit Jahrescheck (Entscheidung
   19); bei gleicher Prüfungsart in die Familiendatei (abi-vorgaben.md).
5. `<profil>-bau.py` – aus dem jüngsten Bau-Skript: alles unter „QUELLEN
   UND PRÜFUNG" übernehmen, Konstanten (KAT, TYP, VOKABULAR, PROFIL,
   GELTUNG_DATEI, ANDERE_KATALOGE) setzen, profilspezifische Prüfungen
   (id-Muster, Kürzel, Pflichtfelder) anpassen. Zuerst eine Feldprobe: ein
   Heft mit probe = True, nichts geschrieben (abi.md § 7, iqb.md § 7).
6. `<profil>-katalog.csv`, `<familie>-typen.csv` (neu oder geteilt) und
   `<profil>-pruefungen.md` (Heftliste, Kennzahlen, Befunde, Änderungslog)
   entstehen mit dem ersten Heft; Selbstprüfung und byteidentischer Rerun
   aus dem HEAD-Stand vor dem Commit (CLAUDE.md § 3).
7. Abgleichlauf über `<familie>-abgleich.py` nach dem letzten Heft bzw.
   nach jedem Stapel (Kern § 9); bei geteilter Liste zieht er alle Kataloge
   der Familie mit.
8. Nachführen: CLAUDE.md § 1 (Regelwerk und Arbeitsdateien), konzept.md
   § 2 (Baustein) und § 4 (Entscheidung mit Grund), README.md.

**Was aus dem Bestand wiederverwendbar ist:**

- Der Kern (katalog-prompt.md) vollständig: Zeilenregel, 37 Felder,
  Formvokabular, Markierungen, Prüfung, Abgleichlauf. Er ist
  prüfungsunabhängig; ein Profil darf ihm widersprechen, ändert ihn aber
  nicht.
- Die Typenliste weitgehend, wenn die Prüfungsart dieselbe ist: ein neues
  Abiturprofil teilt abitur-typen.csv und abitur-vokabular.md (Entscheidung
  25; die Bildungsstandards sind dieselben, Länderunterschiede liegen in der
  Geltung, nicht in den Typen). Bei anderer Prüfungsart eigene Liste, aber
  die vorhandenen als Muster für Namen und Definitionen: 16 von 26
  Fertigkeiten, die in zwei der drei heutigen Listen vorkommen, sind gleich
  geschnitten (befund-typenlisten.md § 4).
- Die Bau-Skripte im Kern (Laden, Schreiben, Zeilenprüfung, Typenprüfung,
  Selbstprüfung, Kennzahlen), die Regeln der Selbstprüfung und des Reruns,
  die Struktur der Prüfungslisten (§ 2 Liste, § 4 Befunde, § 5 Log).
- Der Themenkatalog (§ 3), weil er prüfungsartübergreifend ist.
- Die Werkzeuge außerhalb des Repos (repo-bestand.md § 3) als Muster; sie
  werden je Sitzung neu geschrieben.
- **Gar nicht: die Geltung.** Sie hängt am Träger und am Niveau; auch bei
  gleicher Prüfungsart und gleicher Themenliste sind die ja/nein-Werte neu
  aus den Schwerpunkten des Trägers zu lesen. Ebenso wenig: Vorgaben
  (landeseigen), Quellenverzeichnis, Prüfungsstruktur und Bewertungsschlüssel
  (abi.md § 11), Kürzel und id-Muster.

**Woran man merkt, dass ein neues Profil nötig ist** statt eines neuen
Jahrgangs im vorhandenen:

- Anderer Träger bei gleicher Prüfungsart (Niedersachsen neben
  Berlin/Brandenburg): eigene Zielprüfungen, eigene Quellen, eigenes
  Kürzel im papier – Profil.
- Andere Prüfungsart oder andere Schulform mit anderem Inhalt (P10 Gymnasium
  neben Oberschule): eigene Themenliste – Profil.
- Andere Quellenlage mit anderer Ergebnisregel (amtlicher
  Erwartungshorizont vorhanden oder nicht): andere Regeln für ergebnis,
  afb_amtlich, Eichung – Profil. Das war der Grund für das Profil iqb neben
  abi (Entscheidung 23): länderneutral, mit Erwartungshorizont, eigenes
  Kennungsmuster.
- Dagegen bleibt es ein Jahrgang im vorhandenen Profil, wenn nur der Aufbau
  wechselt (Corona-Aufbau 2021–2023, Bewertungsschlüssel 2024/2025,
  Strukturbruch 2018/2019: alles in abi über papier, KONFIG und abi.md
  § 11), wenn das Land-Kürzel im selben Aufgabenwerk wechselt (bebb →
  bb/be 2026) oder wenn eine Rechnerfassung hinzukommt (Suffix, Delta).
- Probe: Braucht die neue Sache eine eigene Geltungsdatei, ein eigenes
  id-Muster oder eine andere Ergebnisregel? Dann Profil. Braucht sie nur
  neue Zeilen in der Heftliste und ein neues soll in KONFIG? Dann
  Jahrgang.

## 9 Andere Zielprüfung bei gleichem Bestand

Fall: der Schüler zieht in ein anderes Bundesland oder wechselt den
Schultyp, die Prüfungsart bleibt (Abitur). Der Bestand – Kataloge,
Typenliste, Vokabular – ist eine Sammlung von Fakten über Hefte und
Poolaufgaben und ändert sich dadurch nicht. Was sich ändert, ist die
Geltung.

1. **Typenkatalog bleibt.** abi-katalog.csv, iqb-katalog.csv,
   abitur-typen.csv, abitur-vokabular.md § 1, § 2, § 4 unverändert; kein
   Abgleichlauf nötig.
2. **Geltungsdateien neu anlegen:** je neuer Zielprüfung eine
   `<zielprüfung>-geltung.md` (etwa abi-ni-ga-geltung.md) aus den
   Schwerpunkten des neuen Trägers – § 1 Themen ja/nein für jedes Thema der
   Liste, § 2 ausgeschlossene Aufgabenformen, § 3 Rechnerfassung. Nennen die
   Schwerpunkte ein Thema, das die Liste nicht hat, kommt es nach
   abitur-vokabular.md § 2 und bekommt in jeder Geltungsdatei aller
   Zielprüfungen eine Zeile (die Bau-Skripte verlangen Vollständigkeit);
   die alten Dateien tragen dort „nein".
3. **Profile verweisen auf die neuen Dateien:** die Zeile „Zielprüfungen:"
   in abi.md § 6 und iqb.md § 6 nennt die neuen Zielprüfungen – zusätzlich
   oder statt der alten. Die Bau-Skripte lesen die Zeile; die Kennzahl
   „außerhalb der Geltung" und das Abbruchkriterium (neue Schnittwerte
   innerhalb der Geltung, iqb.md § 6) rechnen dann gegen die neue Geltung.
   Reserve-Stapel, die für die alte Geltung ausgereizt waren, können für
   die neue wieder Neues liefern – die Reihe ist gegen die neue Zielprüfung
   nachzurechnen, bevor die Reserve geschlossen bleibt.
4. **Der Blattbau filtert nach der neuen Geltung** (Thema nach § 1,
   Zeile nach § 2); die Eichung ist unberührt, sie hängt am Pool.
5. **Was neu erfasst werden muss:** die Landeshefte des neuen Trägers, wenn
   sie als Formatmodell und Typenquelle gebraucht werden – das ist ein neues
   Profil nach § 8 (abi-ni), das die Typenliste teilt; der Pool (iqb) gilt
   für jedes Land. Die alten Landeshefte (abi) bleiben Typenquelle, sind
   aber kein Formatmodell der neuen Prüfung mehr.
6. **Was nicht mitzieht:** Prüfungsstruktur und Bewertungsschlüssel (abi.md
   § 11), Vorgaben (abi-vorgaben.md), Quellenverzeichnis – alles
   trägergebunden; die alten Geltungsdateien bleiben liegen, solange die
   alte Zielprüfung noch gebraucht wird, sonst werden sie aus der Zeile
   „Zielprüfungen:" gestrichen und können gelöscht werden.

## 10 Änderungen

- 2026-09-17 (Auftrag D, Teil 4): § 8 Eine neue Prüfung aufnehmen (Fragen,
  Dateien in Reihenfolge, Wiederverwendbares, Profil oder Jahrgang) und § 9
  Andere Zielprüfung bei gleichem Bestand; Änderungen sind jetzt § 10.
- 2026-09-15: Entscheidung 25 – gemeinsame Typenliste abitur-typen.csv und
  gemeinsames Vokabular abitur-vokabular.md für abi und iqb, abgleich.py über
  beide Kataloge, Umstellungslauf 12 (938 → 875 Typen). §2 Bausteine ergänzt.
- 2026-09-13: Entscheidung 24 – Schnitt Thema × Gegenstandsklasse × Handlung für
  Teil A des Pools, Gegenstandsklasse als Präfix im Typnamen, Abgleichlauf über
  iqb-abgleich.py (183 → 174 Typen).
- 2026-09-13: Entscheidung 23 – Profil iqb für den IQB-Aufgabenpool, Stapel als
  Laufeinheit, Qualitätsschranke im Skript. §2 Bausteine um die Profile fhr, abi, iqb
  und abi-vorgaben.md ergänzt. Ablauf §7: 4b Profil iqb, Teil A zuerst.
- 2026-09-12: §3 Themenkatalog aufgenommen – Zweck, Leser, Arbeitsteilung mit dem
  Prüfungskatalog, Geltung über die Prüfungsarten hinweg. Bis dahin war der Themenkatalog
  im Repo nirgends beschrieben. Folgeabschnitte umnummeriert (3–7 → 4–8).
- 2026-09-12: Baustein Typenbibliothek je Profil (Ausgabe und erzeugendes Skript); für fhr angelegt,
  nachdem dessen Katalog vollständig war. Die Deckenwahl darin ist als vorläufige Rechnung gekennzeichnet,
  solange die Merkmalsfrage offen ist (blatt-konzept.md § 7).
- 2026-09-05: angelegt.
- 2026-09-05: Probelauf abgeschlossen. EBR zurückgestellt, Profil abi vorgemerkt (Entscheidung 12 ergänzt). Typen-Check: drei Bruchteil-Typen zusammengelegt, Flächen-/Umfangsterm → „Term zu Figur zuordnen“, „Wahrscheinlichkeit zweistufig“ in unabhängig/ohne Zurücklegen getrennt, Mittelpunktswinkel als Baustein vermerkt; alle Typen auf „gültig“. Kern §1: Dateinamen nach Profil.
- 2026-09-05: Typen-Check nach Heften 2023–2019: 147 → 141 Typen, alle „gültig“. Zusammengelegt: Winkel im Trapez/Parallelogramm → „Winkel im Viereck berechnen“; Wahrscheinlichkeit zwei-/dreistufig → „… mehrstufig unabhängig“ und „… mehrstufig ohne Zurücklegen“ (Stufenzahl in gegeben/schritte); Flächenformel Dreieck/Rechteck angeben + Term zu Figur zuordnen → „Term zu Figur angeben“ (Leistung in format); Flächeninhalt Dreieck über Höhe → „Flächeninhalt Dreieck berechnen“ (Vorarbeit in typ_neben). Umbenannt: Lineare Kostenfunktion aufstellen → „Lineare Funktion aus Sachverhalt aufstellen“ (gegen „Lineare Gleichung aus Sachverhalt aufstellen“ abgegrenzt); Endwert linearer Zunahme → „… Veränderung“; Bruch in Prozent umwandeln → „Prozent und Anteil umwandeln“; Zehnerpotenz Exponent bestimmen → „Zehnerpotenzschreibweise umwandeln“; Säulendiagramm ergänzen → „Säulen- oder Balkendiagramm ergänzen“. Definitionen erweitert: Gleichung im Sachzusammenhang deuten (Bestandteile benennen), Term zu Sachtext zuordnen (auch Gleichungen), Proportionale Zuordnung Dreisatz (Abgrenzung zu Zeit aus Weg und Geschwindigkeit), Zufallsgerät entwerfen (Thema jetzt Wahrscheinlichkeit einstufig). Lösung durch Einsetzen prüfen: Thema Lineare Gleichungen. Getrennt gelassen: Gleichung/Graph zu Tarif zuordnen, Geradengleichung zu Graph zuordnen, Graph nach Eigenschaft auswählen (vier verschiedene Richtungen); Nullstelle berechnen vs. am Graphen ablesen. Zwei „?“ in gesucht (2026-FOR-K5b, 2024-OS-K3c) umformuliert.
- 2026-09-05: Typen-Check nach Heften 2018–2014 (Abgleichlauf): 193 → 185 Typen, alle „gültig“, typen.csv nach Leitidee (Lehrplanreihenfolge), Thema, Typ sortiert. Zusammengelegt: Zeit aus Weg und Geschwindigkeit + Dauer aus Menge und Durchsatz → „Dauer aus Menge und Rate berechnen“ (Gegenrichtung „Geschwindigkeit aus Weg und Zeit berechnen“ bleibt: andere Formelrichtung, wie bei Fläche/Seite); Verdopplungszeit am Graphen + Halbwertszeit aus Tabelle → „Verdopplungs- oder Halbwertszeit bestimmen“; Teilstrecke berechnen + Weglänge aus Teilstrecken → „Strecke aus Teilstrecken berechnen“; Körper zu Netz zuordnen + Körper im Schrägbild benennen → „Körper aus Netz oder Schrägbild benennen“; Jahreszinsen berechnen → „Prozentwert berechnen“, Zinssatz berechnen → „Prozentsatz berechnen“ (Zinsvokabular ist Kontext, Thema Zinsrechnung behält Guthabentabelle und Zinseszins). Gelöscht (Leistung steht in format bzw. bemerkung): „Lösungsweg beschreiben“ (2015-OS-K5d jetzt Flächeninhalt Dreieck berechnen, format Begründung – wie Mantellinie 2018-OS-K6d) und „Ergebnis sinnvoll runden“ (Konvention: Vermerk in bemerkung, kein Typ). Umbenannt: Teilwinkel berechnen → „Winkel aus Teilwinkeln berechnen“; Term zu Sachtext zuordnen → „Term zu Sachtext angeben“ (Angeben, Auswählen, Richtig/Falsch in format; 2016-OS-B1b hierher, Abgrenzung zu Lineare Gleichung aus Sachverhalt); Volumenterm zu Körper prüfen → „Term zu Körper angeben“ (parallel zu Term zu Figur angeben); Zahl zu Ungleichung angeben → „Zahl zu Bedingung angeben“ (auch „zwischen“, Abgrenzung zu Mitte zweier Zahlen); Masse aus Volumen berechnen → „Masse aus Volumen und Dichte berechnen“ (Gegenrichtung zu Volumen aus Masse und Dichte, getrennt wie bei Fläche/Seite). Definitionen erweitert: Wachstumstabelle ergänzen (Abnahme, fehlende Zeitangabe, Abgrenzung Guthabentabelle), Zufallsgerät entwerfen (Anzahl berechnen ohne Zeichnung), Graph zu Tarif zuordnen (lineare Tarife), Parabel verschieben (nur Scheitel), Wert aus Diagramm ablesen (Funktionsgraph im Sachzusammenhang), Flächeninhalt Dreieck (Rechenweg beschreiben), Proportionale Zuordnung Dreisatz (Abgrenzung Rate). Thema geändert: Mantelfläche Prisma berechnen → Volumen und Oberfläche (wie Mantelfläche Zylinder/Kegel). Belassen: Restfläche/Restvolumen, Mantellinie Kegel unter Pythagoras, Große Zahl mit Zehnerpotenz multiplizieren, Parabelgleichung zu Graph zuordnen, Zeitpunkt für Schwellenwert (schrittweise, anders als Ablesen). Typ_neben „Flächeninhalt Rechteck berechnen“ an 2018-OS-K6a und 2017-OS-K3b ergänzt. Prozessnotizen in bemerkung von neun Zeilen bereinigt, Fakten unverändert. 37 Katalogzeilen umetikettiert.
- 2026-09-06: Entscheidung 6 (Lösungen) an blatt-konzept.md v0.2 angeglichen.
- 2026-09-06: Basis-URL steht auch im Blatt-Prompt (§2). blatt-prompt.md v0.1 angelegt.
- 2026-09-06: Nr. 5 Herkunft → Protokoll; §2 blatt-prompt nur als Projektanweisung.
- 2026-09-07: §2 Prüfungsprompt (`pruefungsprompt.md`, vorher blatt-prompt) und Masterprompt mit Masterfassung im Repo, CHANGELOG.md; Aufteilung nach Quelle (blatt-konzept.md §5). Entscheidung 16 ergänzt: FHR-Lehrerhefte enthalten den Erwartungshorizont. Repo umbenannt in mathe-nachhilfe; Vorlage und Anleitung aus dem Vorlagen-Repo hierher, ein Repo für alles; Basis-URL an vier Stellen umgestellt.
