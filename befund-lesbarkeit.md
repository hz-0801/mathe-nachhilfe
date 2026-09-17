# BEFUND – Lesbarkeit von Kern und Profilen für ein anderes Sprachmodell
Stand 17.09.2026 (Auftrag D „Namensschema, Erweiterbarkeit, Begründungen",
Teil 6). Durchgesehen: katalog-prompt.md v0.7, msa.md v0.3, fhr.md v1.6,
abi.md v0.23, iqb.md v1.10; für die Begriffe zusätzlich abitur-vokabular.md
v1.5, CLAUDE.md und konzept.md. Stellen benannt, nichts umgeschrieben.

Maßstab für § 1: Ein Leser, der nur die Dateien im Repo hat und kein früheres
Gespräch kennt, muss jede Regel als Anweisung vorfinden. Vier Arten von
Stellen fallen durch:

- **A – Regel nur als Verweis:** die Regel steht nicht da, sondern nur ihr
  Anlass (Auftragstitel, „Entscheidung des Lehrers", Laufnummer).
- **B – überholte Aussage im Präsens:** steht als geltend da, ist aber durch
  den Bestand oder eine spätere Regel überholt; der Leser kann das nicht
  erkennen.
- **C – Umgebungswissen:** setzt eine Arbeitsumgebung oder einen Ablauf
  voraus, der nur in früheren Gesprächen bestand (Sandbox, Upload, Chat).
- **D – Begriff ohne Einführung:** ein Wort wird gebraucht, bevor oder ohne
  dass es erklärt wird.

Nicht gezählt: die Änderungshistorien im Kopf von abi.md (80 Zeilen) und
iqb.md (86 Zeilen) mit Auftragstiteln wie „Weg A umsetzen" – sie sind
Geschichte, keine Regel; ein Leser überspringt sie. Ebenso die rund 40
Einschübe „(Entscheidung des Lehrers, DD.MM.2026)": sie sind Zuschreibung,
die Regel steht jeweils daneben; dass es kein Protokoll dazu gibt, ist eine
Eigenschaft des Repos, nicht der Formulierung.

## 1 Stellen, die frühere Gespräche voraussetzen

| Datei | Stelle | Befund | Art |
|---|---|---|---|
| katalog-prompt.md | § 1 „Zu Beginn holst du … die vier Katalogdateien (Heftliste, Typenliste, Basis- und Kontextkatalog) … ohne Angabe pruefungen.md, typen.csv, katalog-basis.csv, katalog-kontext.csv … Der Katalog liegt in zwei Dateien" | Gilt nur für msa. fhr, abi und iqb haben eine Katalogdatei mit Feld block (fhr.md § 4, abi.md § 2); die Ausnahme steht nur in den Profilen. Ein Leser, der mit abi beginnt, liest im Kern eine Anweisung, die dort nicht gilt. | B |
| katalog-prompt.md | § 2 „Zahl der Typen in typen.csv"; § 7 „Jeder typ steht in typen.csv"; § 8 „katalog-basis.csv und katalog-kontext.csv … typen.csv … pruefungen.md"; § 9 „Alle Zeilen beider Dateien" | Dateinamen und Zwei-Dateien-Modell von msa im prüfungsunabhängigen Kern; § 1 sagt zwar „sie heißen so, wie das Profil sie angibt", § 7–9 nennen dann doch die msa-Namen. | B |
| katalog-prompt.md | § 5 „Lauf 22 hat die Hefte bis 2018 nachgezogen"; § 5 „(abi: „Poolaufgabe (nicht erfasst): <id>.")" | „Lauf 22" ohne Erklärung, dass Abgleichläufe nummeriert sind und wo sie stehen (abgleich.py); die Regel selbst ist vollständig, der Verweis ist Geschichte in der Regel. | D |
| katalog-prompt.md | § 6 „benannt als Gegenstand plus Handlung: Grundwert berechnen; Pythagoras Hypotenuse; Wahrscheinlichkeit zweistufig unabhängig; Scheitelpunkt ablesen" | Zwei der vier Beispiele haben keine Handlung; die Regel und ihre Beispiele widersprechen sich (befund-typenlisten.md § 2, Abweichung 2). | B |
| katalog-prompt.md | Kopfzeile „gilt zusammen mit genau einem Profil"; msa.md und fhr.md „gilt mit Kern v0.3" | Der Kern ist v0.7; welche Kernregeln seit v0.4 (Vokabulardatei, Markierungen, Vorrang des Amtlichen „gilt für alle Profile", Maßstab der Schätzung) für msa und fhr gelten, sagt keine Datei – der Leser muss raten, ob „alle Profile" msa einschließt. | B |
| msa.md | § 2 „die Domain … ist aus der Sandbox erreichbar, Hefte werden mit curl geholt" | „Sandbox" ist die Umgebung eines früheren Chats; heute läuft die Erfassung auf dem Rechner des Lehrers (CLAUDE.md Kopf). | C |
| msa.md | § 6 „Stand v0.2, im Probelauf zu prüfen; Ergänzungen nur über den Bericht" | Der Probelauf ist seit dem 05.09.2026 abgeschlossen (konzept.md § 7); der Satz liest sich als offene Anweisung. | B |
| msa.md | § 3 „Ein Sternchen vor dem Buchstaben kennzeichnet Einheiten, die nur FOR-Schüler lösen müssen" | Vollständig – zum Vergleich: so muss eine Regel aussehen. | – |
| fhr.md | § 2 „Ein Upload durch den Lehrer ist nicht nötig" | Setzt den Ablauf „Claude liefert Dateien, der Lehrer lädt sie hoch" voraus (konzept.md Entscheidung 22), der nicht mehr gilt. | C |
| fhr.md | § 9 Offene Punkte: „Die frühere Regel „Decke ist immer ein Original ab 2023" ist aufgehoben. Für die Decke gilt …"; „Zweiter Abgleichlauf am 12.09.2026 …"; „Beim Abgleichlauf am 12.09.2026 bewusst nicht geändert: …"; „Zwei Vorschläge für den nächsten Abgleichlauf, hier nicht ausgeführt" | Geltende Regeln (Decke, Stufenzahl im Typnamen, Vierfeldertafel unter Unabhängigkeit) stehen als Erzählung einer Änderung unter „Offene Punkte", nicht als Anweisung in § 6/§ 7; der Leser muss die Regel aus der Geschichte herauslesen und erkennt nicht, was noch offen ist. | A |
| fhr.md | § 9 „msa.md schreibt Koordinaten mit „|" … Vorschlag zur Nachbesserung an msa.md, hier nicht ausgeführt" | Ein Vorschlag an eine andere Datei, geparkt im Profil; seit dem 13.09.2026 unbearbeitet. | A |
| fhr.md | § 5 „Im Probelauf bestätigt durch 2026-C-3b" | „Probelauf" ohne Erklärung (erstes Heft vor dem vollständigen Bestand); Befund, keine Regel. | D |
| abi.md | § 1 „Bestand: Die Hefte laut abi-quellen.md § 2, zunächst 2017 und 2018." | Überholt: 16 Hefte 2017–2026 erfasst (abi-pruefungen.md § 2). | B |
| abi.md | § 3 „Zwei Formate. Die erfassten Hefte 2017/2018 und die heutige Prüfung sind verschieden gebaut. Der Katalog nimmt 2017/2018 als Typenquelle; die Blattstruktur richtet sich nach dem heutigen Format." | Überholt und im Widerspruch zu § 11 (Struktur je Jahrgang 2019–2026 aus den Heften, Zuordnung für die Simulation). | B |
| abi.md | § 4 afb_amtlich: „(bis 2018 seit Lauf 22, 17.09.2026; vorher blieb das Feld dort leer und der Bereich stand nur in bemerkung) … die frühere Beschreibung „eine angekreuzte Spalte je Anforderungsbereich" war falsch" | Regel und Geschichte in einem Absatz; die geltende Regel („gefüllt genau bei Dubletten, aus der Poolzeile") ist da, aber in drei Rückblicken versteckt. | D |
| abi.md | § 6 „Bekannte Lücken … Stand nach 2018-be-gk: 33 der 46 damaligen Themen belegt." | Überholt (Stand nach dem dritten von 16 Heften; Themenliste hat 49). | B |
| abi.md | § 7 „Umfang. … Ob verfahren und schritte diesen Umfang tragen, ist in der Feldprobe zu prüfen, bevor ein ganzes Heft erfasst wird." | Anweisung für einen Schritt, der am 12.09.2026 stattfand; für den Leser ein Auftrag, der nicht mehr besteht. „Feldprobe" ohne Erklärung. | B, D |
| abi.md | § 7 „Entschieden: typen.csv markiert das nicht." | Dateiname überholt (abitur-typen.csv seit 15.09.2026); „Entschieden" ohne Datum und ohne Ort. | B |
| abi.md | § 7 „CAS als Nachtrag, und nur für Aufgaben mit „CAS:"-Präfix." | Setzt den Plan voraus, die CAS-Hefte 2017/2018 später zu erfassen (abi-pruefungen.md § 2 „zurückgestellt – Nachtrag nach WTR"); als Regel unvollständig (was ist ein Nachtrag, wann?). | A |
| abi.md | § 8 „Drei Zeilen aus der Feldprobe an 2018-bb-ea" | Beispielzeilen aus der Zeit vor v0.9: afb_amtlich leer bei Dubletten, keine Markierungen – ein Leser hält sie für die geltende Form. | B |
| abi.md | § 9 Offen: „Werden die Themenlücken aus § 6 durch neue Themen geschlossen oder durch eine Lockerung der Regel …?"; „Beantwortet (13.09.2026) …"; „Beantwortet: Brandenburg hat eine eigene zentrale Prüfung …" | Erste Frage durch abitur-vokabular.md § 2 beantwortet (Lücken im Pool aufgelöst), steht aber offen; beantwortete Punkte stehen unter „Offen". | B |
| abi.md | § 11 Kopf „Quelle, wo nichts anderes steht: STARK-Bände zum Abitur 2027, Vorspann S. I–III … (Angabe des Lehrers)" | Vollständig mit Quelle – so muss ein Befund aussehen. | – |
| iqb.md | § 1 „Stand nach dem Delta-Stapel 2026-ea-B-mms: 1061 Zeilen, 792 Typen (nach Abgleichlauf 11), 180 Schnittwerte in 29 Stapeln" | Überholt (1443 Zeilen, 1323 Typen, 37 Stapel, 17.09.2026). | B |
| iqb.md | § 1 „Zusammengeführt werden abi und iqb später über die Typen" | Überholt: seit Entscheidung 25 (15.09.2026) zusammengeführt. | B |
| iqb.md | § 4 id „2026MgrundlegendBAnalysisWTR1-2a (vorläufig, wird vor Teil B bestätigt)"; papier „Zusatz -mms … vorläufig"; aufgabe „Teil B (vorläufig)" | Dreimal „vorläufig" in geltenden Kürzelregeln; § 9 sagt „benutzt und bewährt", Teil B ist abgeschlossen. Widerspruch innerhalb der Datei. | B |
| iqb.md | § 7 „Die Werte sind vorerst Schätzung … nach drei Stapeln werden Schwellenwerte vorgeschlagen"; § 9 „Schwellenwerte in § 7 sind Vorschläge des ersten Laufs; nach drei Stapeln prüfen" | Nach 37 Stapeln; die Schwellen sind gesetzt und mehrfach geändert (Eichung 85 %, neue Typen deaktiviert). | B |
| iqb.md | § 7 „Neue Typen: Schranke deaktiviert (13.09.2026) … eine neue Schranke wird erst gesetzt, wenn der Typenschnitt für Teil A entschieden ist" | Der Typenschnitt ist am selben Tag entschieden worden (Entscheidung 24); die Bedingung ist erfüllt, die Folge nie gezogen. | B |
| iqb.md | § 7 Deutungsliste: nach der Regel (a)–(e) rund 40 Zeilen Messgeschichte („Messung, die zur engen Fassung geführt hat … Mit der Liste v0.5 … v0.6 … v0.7 rückwirkend …") | Die Regel ist vollständig; die Geschichte dahinter ist länger als die Regel und steht im selben Absatz. Für die Erfassung braucht der Leser nur (a)–(e), das Prinzip und die Nullfall-Regel. | D |
| iqb.md | § 8 erste Beispielzeile beginnt mit einem unsichtbaren Zeichen (U+FEFF vor „    id = 2026MgrundlegendAAnalysis11-a") | Zeichenfehler (Zeile 663); ein Skript, das Beispielzeilen einliest, stolpert darüber. | Fehler |
| iqb.md | § 9 „Teil B: Kürzel … im Probestapel 2026-ga-B benutzt und bewährt … Teil B ist zeilenweise erfasst und abgeschlossen"; „Zusammenführung mit abi über die Typen: entschieden"; „Eichung: … Erst ab mehreren Stapeln entscheiden, ob die Schätzregel … nachjustiert werden muss" | Erledigte Punkte unter „Offene Punkte"; die Eichungsfrage ist nach 37 Stapeln (94 %) faktisch beantwortet, ohne dass es dasteht. | B |
| iqb.md | § 6 Abbruchkriterium: „Stand 15.09.2026: grundlegend ausgereizt (7 → 3 → 2 → 2 …) … Beide Niveaus des WTR-Zweigs in Teil B sind damit ausgereizt." | Vollständig: Regel, Maß, Stand, Konsequenz. | – |

Zählung: Kern 5 Stellen (davon 4 überholt), msa 2, fhr 3, abi 9, iqb 8;
Arten: A 3, B 18, C 2, D 5, 1 Zeichenfehler (Mehrfachnennung möglich). Die überholten
Aussagen (B) häufen sich in den Abschnitten § 1 Prüfung, § 6/§ 7 Lücken und
§ 9 Offen der beiden Abitur-Profile; sie sind seit der ersten Fassung nicht
nachgeführt worden, während die Regelabschnitte (§ 4, § 7) mit jeder Version
mitgezogen sind.

## 2 Begriffe – wo dieselbe Sache verschieden heißt

Gezählt per Skript über Kern, vier Profile, abitur-vokabular.md, CLAUDE.md
und konzept.md (Scratchpad begriffe.py).

| Begriff | Verwendung | Abweichung | Vorschlag (nicht ausgeführt) |
|---|---|---|---|
| **Typ** | Kern § 6 definiert: Fertigkeit, Etikett aus der Typenliste, Feld typ. Überall so gebraucht. | – | – |
| **Etikett** | Kern § 6 („Verwende ein vorhandenes Etikett"), CLAUDE.md § 3 („Etikettenfragen"), iqb.md § 7 („Etiketten des Stapels vereinheitlichen") | Synonym zu Typ bzw. Typname, nie definiert; in „Etikettenfragen" meint es die Zuordnung, in „Etiketten vereinheitlichen" die Namen. | Etikett = Name des Typs (das Wort in der Spalte typ); Typ = die Fertigkeit dahinter. Ein Satz im Kern § 6. |
| **Feinetikett / Feintyp** | abitur-vokabular.md § 4, abi.md § 6, konzept.md Entscheidung 24: „der Typ nach Kern § 6 bleibt als Feinetikett"; konzept.md Entscheidung 24 letzter Satz: „nicht der Feintyp" | Zwei Wörter für dasselbe (der Typ im Gegensatz zum Schnittwert). | Feinetikett; „Feintyp" an der einen Stelle ersetzen. |
| **Haupttyp / Nebentyp** | abi.md § 7 „Haupttyp", abitur-vokabular.md § 4 „Haupttyps", fhr.md § 6 „Nebentyp"; Kern § 4 sagt nur „typ ist die erste Leistung, typ_neben die weiteren" | Die Felder heißen typ und typ_neben, die Wörter Haupttyp/Nebentyp kommen im Kern nicht vor. | Im Kern § 4 einmal einführen: „typ (Haupttyp) … typ_neben (Nebentypen)". |
| **Schnitt / Schnittwert / Typenschnitt / Zwischenstufe** | Kern § 5 „Schnitt Thema × Gegenstandsklasse × Handlung"; iqb.md § 6 „Schnittwerte" (die Werte des Schnitts); abi.md § 6 „Typenschnitt nach Entscheidung 24"; konzept.md und iqb-pruefungen.md „Zwischenstufe" (historischer Name der Messung) | Schnitt (das Raster) und Schnittwert (eine Zelle) sind sauber getrennt; „Typenschnitt" ist ein drittes Wort für den Schnitt, „Zwischenstufe" ein viertes. | Schnitt und Schnittwert; „Typenschnitt" in abi.md § 6 und konzept.md streichen, „Zwischenstufe" nur mit Zusatz „(Messung vom 13.09.2026)". |
| **Gegenstandsklasse / Klasse / Unterklasse / Klassenliste** | abitur-vokabular.md § 4: „Gegenstandsklassen" (5), „Klassen" (7), „Klasse" (5), „Unterklassen" (1); konzept.md Entscheidung 24 „Unterklasse", „Klassenliste"; CLAUDE.md „Präfix „Klasse: "" | Gegenstandsklasse und ihre Kurzform Klasse sind eingeführt; „Unterklasse" (Vokabular § 4, konzept E24) ist ein drittes Wort ohne Einführung. | Gegenstandsklasse, kurz Klasse; „Unterklasse" an beiden Stellen durch „Klasse" ersetzen. |
| **Stapel** | iqb.md § 7 definiert (Prüfungsteil × Pooljahr × Niveau [× Rechnerfassung]); CLAUDE.md § 4; in abi.md nur als Verweis auf Reserve-Stapel | – | – |
| **Heft** | Kern und abi/fhr/msa: die Prüfung als Dokument; iqb.md: Landesheft im Gegensatz zur Pooldatei; daneben „Band" (STARK-Verlagsband), „Scan" (Bilddatei des Bands), „Datei" (Pool) | Konsistent; „Heft" meint nie eine Pooldatei. | – |
| **Lauf** | Heftlauf, Stapellauf, Abgleichlauf, Umstellungslauf, Nachtragslauf, Probelauf, Testlauf; „Lauf 23" allein (Kern § 5, abi.md § 4, § 7, iqb.md § 7) meint immer einen nummerierten Abgleichlauf, sagt es aber nicht | Die nummerierten Läufe sind nur in abgleich.py erklärt; im Kern steht „Lauf 22" ohne das Wort Abgleichlauf. | Erste Nennung je Datei als „Abgleichlauf 22 (abgleich.py)"; danach „Lauf 22". |
| **Vormerkung / Vorstufe / Vermerk / vorgemerkt / offener Posten / Übergangszustand** | Kern § 5: „Vorstufe des Verweises … ein Übergangszustand – ein offener Posten"; abi.md § 7: „Vorstufe" (4), „Vormerkung" (3), „Vermerk" (2), „vorgemerkt"; iqb.md § 7: „Vermerk" (4), „Vormerkung" (2), „Vorstufe" (1); CLAUDE.md: „Vermerk", „Vorstufe" | Drei Wörter für die Markierung „Poolaufgabe (nicht erfasst …)"; „Vermerk" zugleich das allgemeine Wort für jede Notiz in bemerkung („Vermerk in bemerkung", „Befund im Vermerk"). „Offener Posten" und „Übergangszustand" beschreiben ihren Status, nicht die Sache. | Vormerkung = die Markierung „Poolaufgabe (nicht erfasst …)"; Verweis = „Dublette von:" und „Abgewandelt von:"; Vermerk = jede andere Notiz in bemerkung; „Vorstufe" nur einmal erklärend („Vormerkung, die Vorstufe des Verweises"). |
| **Dublette** | (a) Landeszeile mit „Dublette von: <iqb-id>" (abi.md § 7, Kern § 5); (b) Pooldatei, die wortgleich mit einer anderen ist – Spalte dublette_von in iqb-quellen.csv, keine Zeile (iqb.md § 7); (c) wortgleiche nummerierte Aufgabe in zwei Dateien desselben Stapels, keine Zeile (iqb.md § 7 „Dubletten unterhalb der Dateiebene") | Drei Sachverhalte unter einem Wort; Kern, abi.md und iqb.md warnen an drei Stellen ausdrücklich, dass (b) „etwas anderes" ist als (a) – ein Zeichen, dass das Wort überladen ist. | (a) Dublette; (b) Dateidublette; (c) Aufgabendublette. Spalte dublette_von in iqb-quellen.csv umbenennen wäre Teil einer Umbenennung (namensschema.md § 4), sonst nur im Text. |
| **Zwilling** | abi.md § 7 „Wortgleiche Zwillinge des anderen Landes" (Heft zu Heft, keine Zeile); iqb.md § 7 „WTR-Zwilling" (WTR-Datei zur MMS-Datei); iqb-pruefungen.md „Zwillingsnachweis" | Zweimal ein Paar wortgleicher Dokumente, einmal Landeshefte, einmal Rechnerfassungen. | „Zwilling" nur für Landesheft-Paare; die WTR-Datei zur MMS-Datei „WTR-Fassung". |
| **wortgleich / abgewandelt** | Kern § 5, abi.md § 7, iqb.md § 7 einheitlich: wortgleich → Dublette, sonst abgewandelt; Toleranz in Lauf 23 (Gesamtoberfläche/Oberfläche als wortgleich) | Die Grenze „wortgleich" ist nirgends definiert (Zahlen, Aufträge, BE gleich? Artikel? Synonyme?); die Praxis steht in den Befunden (abi-pruefungen.md § 4). | Definition in abi.md § 7: wortgleich = Zahlen, Aufträge, Reihenfolge und BE gleich; Artikel und Synonyme ohne Bedeutungsänderung zulässig. |
| **Schätzung übernommen / geerbt** | Kern § 5 „übernommene Schätzung" (Poolzeile aus der Landeszeile); abi.md § 7 „geerbte Schätzungen der Dubletten" (Landeszeile aus der Poolzeile) | Zwei Richtungen, zwei Wörter – brauchbar, aber nirgends gegenübergestellt. | Ein Satz in abi.md § 7: übernommen = vom Land in den Pool, geerbt = vom Pool ins Land. |
| **Niveau** | (a) Anforderungsniveau der Prüfung: grundlegend/erhöht, gk/lk/ga/ea (abi.md § 4, iqb.md § 4, Zielprüfungen); (b) Feld niveau_geschaetzt: geschätzter Anforderungsbereich I–III (Kern § 5) | Ein Wort für zwei Achsen; „Niveau" in „Wiederverwendung im Niveau" meint (a), in „Niveauschätzung" (b). | Für (b) „Anforderungsbereich (geschätzt)" oder „AB-Schätzung" im Text; das Feld heißt weiter niveau_geschaetzt. |
| **Leitidee / Sachgebiet** | Feld leitidee; Kern § 5 „leitidee (genau eine aus dem Profil)"; msa/fhr nennen es Leitidee, abi/iqb Sachgebiet (abitur-vokabular.md § 1 begründet) | Ein Feld, zwei Wörter je Profil – begründet, aber im Kern nicht erwähnt. | Im Kern § 5 ein Halbsatz: „leitidee (Leitidee oder Sachgebiet, wie das Profil es nennt)". |
| **Zielprüfung / Profil / Prüfungsart / Familie** | Zielprüfung: abitur-vokabular.md § 3, Geltungsdateien; Profil: Kern; Prüfungsart, Familie: namensschema.md § 2 | Konsistent; Prüfungsart und Familie sind neu (Auftrag D) und nur in namensschema.md und konzept.md § 8 eingeführt. | – |
| **Eichung / enge Fassung / Maßstab / Schranke / Kennzahl** | Kern § 5 v0.7 definiert Eichung, Maßstab, Kennzahl, Schranke; iqb.md § 7 „enge Fassung" (Deutungsliste) | Konsistent seit v0.7. | – |

Befund: Von sechzehn Begriffen sind sieben einheitlich gebraucht (Typ,
Stapel, Heft, wortgleich/abgewandelt im Gebrauch, Zielprüfung, Eichung,
Schätzung übernommen/geerbt), sechs haben zwei bis vier Wörter für dieselbe
Sache (Etikett/Feinetikett/Feintyp, Schnitt/Typenschnitt/Zwischenstufe,
Gegenstandsklasse/Unterklasse, Vormerkung/Vorstufe/Vermerk, Lauf,
Haupttyp/Nebentyp), drei tragen ein Wort für mehrere Sachen (Dublette,
Zwilling, Niveau). Die Vorschläge in der letzten Spalte sind Textänderungen
an Kern und Profilen ohne Skript- oder Katalogänderung, mit einer
Ausnahme (Spalte dublette_von).
