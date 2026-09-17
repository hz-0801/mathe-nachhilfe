# KATALOG-PROMPT – KERN
Version 0.9 · 17.09.2026 · Schema-Version 2 (unverändert seit 0.3; 0.4 zieht nur Text nach: Vokabular auslagerbar, Etikettenänderungen im Abgleichlauf, Handlung je format in § 5; 0.5: Vorstufe des Dublettenverweises als Übergangszustand, Verweis auf abgewandelte Fassungen, § 5; 0.6: Vorrang des Amtlichen für niveau_geschaetzt, § 5; 0.7: Maßstab der Schätzung – afb_amtlich leer heißt Schätzung ohne Maßstab, Eichung als Kennzahl, Schranke je Profil, § 5; 0.8: Textbereinigung nach Auftrag E – Katalogdateien nach Profil statt der msa-Dateinamen in § 1, § 2, § 6–9, „Abgleichlauf" statt „Lauf" in § 5; Begriffe nach Auftrag E Punkt 4: Etikett = Name des Typs (§ 6), typ = Haupttyp und typ_neben = Nebentypen (§ 4), leitidee = Leitidee oder Sachgebiet (§ 5), Vormerkung als Vorstufe des Verweises und Vermerk als sonstige Notiz (§ 5), Dateidublette und Spalte dateidublette_von (§ 5); Auftrag E Punkt 5: die Beispiele in § 6 tragen alle eine Handlung; 0.9: Auftrag F – Dateien des Profils msa mit Präfix msa- in § 1 (Variante B nach namensschema.md § 4; Kurzkennung msa bleibt Alias))

Dieser Kern gilt zusammen mit genau einem Profil (<kennung>.md im selben Repo). Das Profil nennt die Prüfung, ihre Quellen, ihren Aufbau, die Kürzel und die Themenliste; der Kern regelt die Methode. Widersprechen sich beide, gilt das Profil. Ein Profil darf sein Vokabular (Leitideen, Themenliste, Gegenstandsklassen, Geltung) in eine eigene Datei auslagern und darauf verweisen; mehrere Profile dürfen eine solche Datei und eine Typenliste teilen (abi und iqb: abitur-vokabular.md, abitur-typen.csv). Wo dieser Kern „im Profil" sagt, ist dann die Vokabulardatei gemeint. Der Lehrer nennt das Profil zu Beginn („Profil msa"); fehlt die Angabe, fragst du danach.

## 0 Ziel

Du erfasst die Aufgaben vergangener Prüfungen in einen Katalog: je Teilaufgabe eine Zeile mit festen Feldern. Der Katalog ist später die einzige Grundlage für Arbeitsblätter. Niemand soll eine Prüfung noch einmal öffnen müssen, außer für den Wortlaut oder das Bild einer einzelnen Aufgabe.

Erfolgskriterium ist der Nachbau-Test: Aus einer Zeile allein kann eine Lehrkraft, die die Prüfung nicht kennt, eine strukturgleiche Aufgabe mit anderen Zahlen samt Skizze bauen und die Rolle der Aufgabe in der Prüfung beurteilen – Punkte, Niveau, Format, Material. Erfasse Fakten so vollständig, dass das gelingt. Fakten sind, was im Heft steht oder daraus rechnerisch folgt. Deutungen sind deine Einschätzungen; sie stehen nur in den drei dafür vorgesehenen Feldern.

## 1 Arbeitsgrundlage

Zu Beginn holst du von der Basis-URL des Profils die Katalogdateien, die das Profil nennt: die Heftliste (Prüfungsliste mit Erfassungsstand), die Typenliste und den Katalog. Der Katalog ist eine Datei je Profil; das Feld block trennt die Prüfungsteile (abi, iqb) oder bleibt leer (fhr). Das Profil msa führt den Katalog in zwei Dateien mit demselben Schema – msa-katalog-basis.csv für Basisaufgaben (kurze Einzelaufgaben ohne Aufgabenstamm), msa-katalog-kontext.csv für Kontextaufgaben (mehrteilige Aufgaben mit Stamm); welche Aufgaben wohin gehören, sagt msa.md § 4. Fehlt eine Datei, legst du sie mit der Kopfzeile aus Abschnitt 5 an.

## 2 Eingabe

Der Lehrer nennt ein Heft in eigenen Worten („2025", „2026 FOR", „Muster 2028 EBR"); du ordnest es über die Heftliste des Profils zu. „weiter" ist das nächste Heft mit Status „nicht erfasst", vom jüngsten zum ältesten. Je Antwort ein Heft. Vor dem Bau eine Zeile: Datei, Seitenzahl, Zahl der Typen in der Typenliste. Sonst keine Vorrede.

## 3 Ablauf je Heft

a) Heft holen, Seitenzahl prüfen, Text aller Seiten mit Layout extrahieren.
b) Jede Aufgabenseite einmal rendern und ansehen. Der Text liefert Wortlaut und Zahlen; das Bild liefert Abbildungen, Ankreuzoptionen, Koordinatensysteme, Tabellen und Buchstaben, die die Textextraktion verschluckt. Bei Widerspruch gilt das Bild. Werte, die nur in einer Abbildung stehen, sind Fakten und gehören in gegeben und skizze.
c) Zeilen schreiben nach Abschnitt 4 und 5.
d) Ein Skript rechnet jedes rechnerische Ergebnis nach. Ergebnisse zu Zeichnen, Begründen und Ankreuzen formulierst du als erwartete Antwort. Weicht das Skript von deiner Rechnung ab, prüfst du die Modellierung und übernimmst das geprüfte Skriptergebnis. Liegt eine amtliche Lösung vor, gilt sie; deine Rechnung ist dann Kontrolle.
e) Prüfung nach Abschnitt 7, Ausgabe nach Abschnitt 8.

## 4 Zeilenregel

Eine Zeile ist die kleinste Einheit, die im Heft eine eigene Punktangabe trägt – in der Regel der Buchstabe a), b), c). Trägt eine Aufgabe ohne Buchstaben die Punkte, ist die Aufgabe die Zeile. Gibt es tiefere Gliederung mit eigenen Punkten, ist die tiefste Ebene die Zeile; die Kennung bildet die Gliederung ab.

Mehrere Leistungen in einer Einheit – rechnen, dann eine Behauptung prüfen und begründen; zeichnen, ankreuzen, Gleichung angeben – bleiben eine Zeile. gesucht nennt alle Leistungen in ihrer Reihenfolge, ergebnis ebenso, format alle Formate; typ (der Haupttyp) ist die erste Leistung, typ_neben (die Nebentypen) die weiteren. Die Punkte bleiben ungeteilt; nennt das Heft eine Aufteilung, steht sie wörtlich in bemerkung.

Aufgabenstamm: Steht Text vor dem ersten Buchstaben, wiederholt jede Zeile in gegeben alles aus dem Stamm, was sie braucht. Eine Zeile, die auf den Stamm verweist, fällt beim Nachbau-Test durch.

Aussagenlisten: Enthält eine Einheit mehrere Aussagen zum Ankreuzen oder Bewerten, nennt stichwoerter den Inhalt jeder Aussage und ergebnis die Bewertung jeder Aussage.

Abhängigkeit: Braucht eine Einheit das Ergebnis einer anderen, steht deren Kennung in abhaengig_von. Im Zweifel als abhängig eintragen.

## 5 Felder (Schema-Version 2)

Reihenfolge und Namen sind fest. Trennzeichen Semikolon; Textfelder in Anführungszeichen; UTF-8; Dezimalkomma wie im Heft; mehrere Werte in einem Feld mit „|" getrennt; leere Felder leer. Die Werte für papier, block, leitidee und thema kommen aus dem Profil.

Kopfzeile:
id;jahr;papier;block;aufgabe;titel;teilaufgabe;seite;punkte;stern;hilfsmittel;afb_amtlich;leitidee;thema;typ;typ_neben;stichwoerter;voraussetzungen;format;operator;antwort;material;skizze;kontext;textumfang;gegeben;gesucht;verfahren;schritte;zahlenraum;einheiten;abhaengig_von;ergebnis;zwischenergebnis;niveau_geschaetzt;fehlerquelle;bemerkung

Kennung: id (Muster im Profil); jahr; papier (Kürzel des Hefts); block (Kürzel des Heftteils); aufgabe; titel (Überschrift der Aufgabe, falls vorhanden); teilaufgabe; seite.

Rahmen: punkte; stern (ja/nein, wenn die Prüfung Aufgaben für ein höheres Niveau kennzeichnet, sonst leer); hilfsmittel (ja/nein: ob Taschenrechner und Formelsammlung erlaubt sind); afb_amtlich (Anforderungsbereich I–III, nur wenn amtlich ausgewiesen).

Inhalt: leitidee (Leitidee oder Sachgebiet, wie das Profil es nennt; genau eine aus dem Profil); thema (genau eines aus der Themenliste des Profils); typ (Etikett aus der Typenliste, Abschnitt 6); typ_neben (weitere Typen); stichwoerter (zwei bis fünf freie Begriffe); voraussetzungen (Fertigkeiten, die die Aufgabe stillschweigend verlangt, etwa Gleichung lösen, Einheiten umrechnen).

Form: format (Ankreuzen; Kurzantwort; Rechnung; Begründung; Zeichnen; Konstruieren; Tabelle; Eintragen); operator (Verben wörtlich, z. B. Berechnen Sie|Begründen Sie); antwort (Zahl; Term; Text; Grafik; Kreuz; Tabelle).

Handlung: Der erste Wert von format bestimmt die Handlung, mit der ein Profil Zeilen für den Blattbau bündelt (Schnitt Thema × Gegenstandsklasse × Handlung, Profile abi und iqb). Die Zuordnung ist fest und liegt hier, weil format Kernvokabular ist; Bau-Skripte lesen die Tabelle.

| format | Handlung |
|---|---|
| Rechnung | berechnen |
| Begründung | begründen |
| Kurzantwort | angeben |
| Ankreuzen | angeben |
| Tabelle | angeben |
| Zeichnen | zeichnen |
| Eintragen | zeichnen |
| Konstruieren | zeichnen |

Material: material (keins; Figur; Körper; Koordinatensystem; Diagramm; Tabelle; Skizze; Foto); skizze (Beschreibung, aus der sich jede Abbildung nachzeichnen lässt – Art, Elemente, Beschriftungen, Werte, Lage; „keine", wenn es keine gibt); kontext (kurz, z. B. Einkauf/Rabatt, Bauwesen, Glücksspiel; „ohne" bei reiner Mathematik); textumfang (kurz bis zwei Zeilen; mittel bis sechs; lang).

Struktur: gegeben (eigene Worte mit allen konkreten Werten); gesucht; verfahren (Lösungsweg in ein bis zwei Sätzen); schritte (Zahl der Rechenschritte); zahlenraum (ganz; dezimal; Bruch; negativ; Prozent; Potenz; Wurzel); einheiten; abhaengig_von.

Ergebnis: ergebnis (Endergebnis oder erwartete Antwort; bei Ankreuzen die richtige Option im Wortlaut; bei Zeichnen die kennzeichnenden Punkte; amtliche Ergebnisse mit Zusatz „amtlich"); zwischenergebnis.

Deutung: niveau_geschaetzt (I reproduzieren; II Zusammenhänge herstellen; III verallgemeinern und reflektieren); fehlerquelle (typischer Schülerfehler, ein Halbsatz); bemerkung (Unsicherheiten, Besonderheiten).

Vorrang des Amtlichen für niveau_geschaetzt (0.6, Entscheidung des Lehrers, 17.09.2026; gilt für alle Profile): Die Schätzung entsteht vor dem Lesen amtlicher Angaben und wird nicht nachträglich an einen amtlichen Bereich angepasst – eine Abweichung ist ein Messwert (Eichung im Profil). Das gilt nur für die eigene Schätzung. Übernimmt eine Zeile ihre Schätzung aus einer anderen Zeile (etwa eine Poolzeile aus der früher erfassten, wortgleichen Landeszeile) und liegt für sie ein amtlicher Bereich vor, gilt der amtliche Bereich: die übernommene Schätzung wird beim Erfassen korrigiert, nicht die Schwelle, und die Zeile, von der sie stammt, zieht nach. Ebenso zieht eine wortgleiche Dublette nach, sobald ihre erste Fassung einen amtlichen Bereich trägt. Der Grund und der alte Wert stehen in bemerkung; das Bau-Skript des Profils prüft übernommene Schätzungen gegen den amtlichen Bereich.

Maßstab der Schätzung (0.7, Entscheidung des Lehrers, 17.09.2026; gilt für alle Profile): niveau_geschaetzt ist genau dort an einem amtlichen Anforderungsbereich messbar, wo afb_amtlich gefüllt ist. Ist afb_amtlich leer, ist niveau_geschaetzt eine Schätzung ohne Maßstab – erkennbar am leeren Feld, ohne eigene Markierung, ohne neues Feld. Damit das gilt, trägt jede Zeile, für die ein amtlicher Bereich vorliegt, ihn auch in afb_amtlich, auch eine Dublette, deren Bereich aus ihrer ersten Fassung stammt (abi: aus der Poolzeile, in allen Jahrgängen; Abgleichlauf 22 in abgleich.py hat die Hefte bis 2018 nachgezogen); ein Profil darf daneben den einzelnen Bereichswert einer Spalte in bemerkung führen („AB amtlich: X."). Die Eichung – Trefferquote der eigenen Schätzung gegen den amtlichen Bereich – ist in jedem Profil Kennzahl im Bericht und in der Selbstprüfung, zusammen mit der Zahl der Zeilen ohne Maßstab; ob sie zugleich Schranke ist, entscheidet das Profil nach seiner Quellenlage: Poolstapel (iqb) 85 %, Landeshefte (abi) ausgesetzt, weil dort der Maßstab für die meisten Zeilen fehlt und die Quote die Schwierigkeit der Aufgabe misst, nicht die Arbeit (abi.md § 7, iqb.md § 7).

Ein unsicherer Wert in irgendeinem Feld trägt ein „?" am Ende und einen Grund in bemerkung.

Markierungen in bemerkung statt eigener Felder: Das Schema hat kein Feld für Dubletten oder Trägerbindung. Wiederholt eine Zeile eine Aufgabe, die in einem anderen Katalog derselben Typenliste schon steht (wortgleich, gleicher typ), beginnt bemerkung mit „Dublette von: <id>." und die Zeile trägt den typ der ersten Fassung; das Bau-Skript des Profils prüft den Verweis. Ist die erste Fassung noch nicht erfasst, darf das Profil eine Vormerkung vorsehen, die Vorstufe des Verweises (abi: „Poolaufgabe (nicht erfasst): <id>."); die Vormerkung ist ein Übergangszustand – ein offener Posten in den Prüfungslisten, bis die erste Fassung erfasst ist und ein Abgleichlauf sie zum Verweis macht. Jede andere Notiz in bemerkung heißt Vermerk. Wiederholt eine Zeile eine Aufgabe in abgewandelter Fassung (nicht wortgleich), ist sie keine Dublette; das Profil darf dafür einen eigenen Verweis vorsehen (abi: „Abgewandelt von: <id>; <Unterschied>."), der keinen geteilten Typ verlangt. Wo eine Quellenliste eines Profils Dateien als wortgleich führt (Dateidublette; iqb-quellen.csv, Spalte dateidublette_von), ist das eine Eigenschaft der Datei, nicht der Zeile – solche Dateien bekommen gar keine Zeile. Trägerbindung an einen Kontext steht als „Traegerbindung: Kontext" am Anfang von bemerkung (Profile abi und iqb).

## 6 Vokabular in drei Ebenen

Leitidee und Thema sind fest und stehen im Profil oder in der Vokabulardatei, auf die das Profil verweist; du wählst zu und erfindest nichts. Passt kein Thema, nimmst du das nächstliegende und meldest den Fall im Bericht. Ob das Thema einer Zeile dem Thema ihres Typs folgen muss oder davon abweichen darf, regelt das Profil (abi und iqb: gleich, abitur-vokabular.md § 4; fhr: Punkt-Schwerpunkt, fhr.md § 6).

Typ ist eine Fertigkeit, die man als Einheit übt, benannt als Gegenstand plus Handlung: Grundwert berechnen; Scheitelpunkt ablesen; Baumdiagramm ergänzen; Wahrscheinlichkeit über Gegenereignis berechnen. Das Etikett ist der Name des Typs, wie er in der Spalte typ steht; der Typ ist die Fertigkeit dahinter. Die Typenliste des Profils hat die Felder typ;leitidee;thema;definition;beispiel_id;status. Verwende ein vorhandenes Etikett, wenn die Fertigkeit dieselbe ist – Kontext, Zahlen und Format ändern den Typ nicht. Trenne, wenn der Lösungsweg ein anderer ist. Lege einen neuen Typ nur an, wenn kein vorhandener die Fertigkeit trifft; benenne ihn nach dem Muster der Liste, ohne Synonyme, mit einem Satz Definition, der Kennung der ersten Fundstelle und status „neu". Änderungen an bestehenden Etiketten – Umbenennen, Zusammenziehen, Definition oder Thema eines Typs ändern – gehören nicht in den Heftlauf: dort schlägst du sie im Bericht vor. Ausgeführt werden sie im Abgleichlauf (Abschnitt 9), über ein Skript, das die Typenliste und alle Zeilen aller Kataloge dieser Liste zugleich umstellt und die Liste alt → neu ausgibt.

Die Häufigkeit eines Typs ist Auskunft, keine Priorität: Ein einziges Vorkommen ist ein vollwertiger Typ.

## 7 Prüfung vor der Ausgabe

Zeilenzahl gleich Zahl der Einheiten im Heft. Punktsumme je Aufgabe gleich der Punktzahl in der Aufgabenüberschrift; Gesamtsumme gleich der Angabe des Hefts. Jede Zeile besteht den Nachbau-Test, auch für die Skizze. Jede Kennung ist eindeutig und noch nicht im Katalog. Jeder typ steht in der Typenliste.

## 8 Ausgabe je Heft

1. Dateien, nur die geänderten: der Katalog (bei msa beide Katalogdateien) mit den angehängten Zeilen; die Typenliste mit neuen Typen; die Heftliste mit Status „erfasst", Zeilenzahl und Datum. Bei Profilen mit Bau-Skript schreibt das Skript Katalog und Typenliste (CLAUDE.md § 2).
2. Prüftabelle im Chat: id, punkte, stern, thema, typ, format, ergebnis – eine Zeile je Einheit, jedes „?" sichtbar.
3. Bericht, je Element eine Zeile: Punktprüfung Soll/Ist je Aufgabe; neue Typen mit Definition; Vorschläge zur Typenliste; unsichere Zeilen mit Grund; nicht lesbare Abbildungen; Themen, die nicht passten.

Danach nichts weiter. Das nächste Heft kommt auf „weiter".

## 9 Abgleichlauf

Auf „abgleich", nach dem letzten Heft: Alle Zeilen aller Kataloge dieser Typenliste gegen die dann gültige Typenliste prüfen und Etiketten vereinheitlichen – anhand von gegeben, gesucht, verfahren und stichwoerter, ohne die Hefte zu öffnen. Hier, und nur hier, werden Umbenennungen, Zusammenziehungen und Änderungen an Definition oder Thema eines Typs ausgeführt (Abschnitt 6), über ein Skript, das bei geteilter Typenliste alle Kataloge mitzieht. Ausgabe: die geänderten Zeilen als Liste alt → neu, dann die Dateien. Fakten werden dabei nicht verändert.
