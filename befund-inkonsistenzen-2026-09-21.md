# BEFUND – Inkonsistenzen vor dem Promptumbau

Stand 21.09.2026 · erhoben im Chat verbessereBlätter() gegen
blatt-konzept.md v0.8, uebergabe.md 2026-09-20, katalog/,
katalog/_tragfaehigkeit.md und die Kopfabschnitte von
unterrichtsblatt.md v3.35 und pruefungsblatt.md v0.15 ·
nichts entschieden, nichts geändert

**Reichweite.** Geprüft wurde Konzept gegen Konzept und Konzept
gegen die Kopfabschnitte der beiden Prompte. Nicht geprüft: die
beiden Prompte im Volltext (112 KB) gegen die Konzepte und gegen
den Katalog. Dort sind weitere Befunde zu erwarten.

## 1 Zwei Dinge heißen „Katalog", und der Themenkatalog hat keinen Abnehmer

pruefungsblatt.md v0.15 § 2.1 holt msa-typen.csv,
msa-katalog-basis.csv und msa-katalog-kontext.csv – den
Prüfungskatalog. unterrichtsblatt.md v3.35 enthält das Wort
„Katalog" genau einmal, in der Kopfzeile, und zwar um sich als
Werkzeug für Themen *ohne* Katalog zu bestimmen; themen.csv und
katalog/*.md kommen darin nicht vor. Die 73 Einträge mit
Lerneinheiten, Merkkästen und Voraussetzungen werden von keinem
der beiden Prompte gelesen. Alles Weitere hängt daran.

## 2 Die Architekturregel „Trennung nach Quelle" ist überholt

blatt-konzept.md § 5 (07.09.2026): Der Prüfungsblatt-Prompt baut
alles mit Katalog, der Unterrichtsblatt-Prompt alles ohne – „er
wird nicht abgelöst, weil der Unterricht nie einen Katalog hat".
Seit dem Themenkatalog stimmt der Halbsatz nicht mehr. Solange die
Regel steht, ist jeder Umbau, der den Unterrichtsblatt-Prompt aus
katalog/ lesen lässt, ein Bruch mit einer schriftlichen
Festlegung. Zu entscheiden: Trennlinie neu ziehen oder die Regel
ausdrücklich aufheben.

## 3 Die maßgebliche Datei steht auf dem Stand vom 12.09.

blatt-konzept.md trägt den Satz „Für die Heft-Phase gilt bei
Widerspruch diese Datei", kennt aber nichts aus den Gesprächen vom
19.09. Die vier Konzepte (Blatt 0, Überspringbarkeit, Kurztest,
Stundenanker) existieren nur in der Übergabe und als Kurzposten in
faellig.md § 2. Ein dauerhafter Ort fehlt.

## 4 Diskussionsstand als Entscheidung abgelegt

Die Übergabe 2026-09-20 führt die vier Konzepte unter
„Verbindliche Entscheidungen und Rahmenbedingungen" und nennt sie
im selben Satz „Diskussionsstand, Umsetzung steht aus". Wer die
Übergabe liest, hält sie für beschlossen. Berichtigt in der
Übergabe 2026-09-21 § 4.

## 5 Kurztest gegen „Kein eigener Test"

blatt-konzept.md § 6: „Kein eigener Test: Die Generalprobe ist die
Originalprüfung" (konzept.md Nr. 8). Der Stand vom 19.09. macht
den Kurztest zum festen Schlussabschnitt jedes Blatts (10 Minuten,
3 Aufgaben, Ankreuzfußzeile). Möglich, dass sich das über die
Blattsorte auflöst – gesagt ist es nicht.

## 6 Stundenanker gegen „Kein Übersichtskasten in keinem Heft"

blatt-konzept.md § 6 schließt Kästen aus, mit der Begründung, die
Prüfung erlaube die Formelsammlung und der Schüler solle mit ihr
üben. Entscheidung 36 füllt die Sek-II-Einträge gerade mit
Merkkästen, und der Stundenanker will sie in Kurzform an den
Blattanfang setzen. Dieselbe Begründung trägt im Unterricht nicht,
weil dort keine Formelsammlung die Rolle des Kastens übernimmt.

## 7 Blatt 0 gegen die Heftsorte „Vorbereitung"

Drei Punkte auf einmal:

(a) blatt-konzept.md § 2 kennt die Heftsorte „Vorbereitung"
(Auslöser: Zuruf). Blatt 0 ist inhaltlich dasselbe, aber
Standardbestandteil ohne Bestellparameter. Zwei Namen, zwei
Auslöser.

(b) § 7 führt „Vorbereitung ohne Zuruf bei bekannten
Vorwissenslücken" ausdrücklich als *vom Lehrer unbestätigt*. Im
Stand vom 19.09. ist daraus ein Standardbestandteil geworden, ohne
dass die Bestätigung nachgeholt wurde.

(c) § 6: „Katalogfeld voraussetzungen ist Hinweis, keine Liste –
die Fertigkeiten leitet der Prompt aus den Rechenschritten ab".
Die Katalogeinträge liefern inzwischen einen eigenen Abschnitt
„Voraussetzungen (Blatt 0)" mit benannten Fertigkeiten und
Dateiverweisen. Die Quelle hat sich bewegt, die Regel nicht.

## 8 Überspringbarkeit gegen die Kette

blatt-konzept.md § 4 baut rückwärts von der Decke: eine Sprosse je
Merkmal, aufeinander aufbauend, Original am Ende. Das Bauprinzip
Überspringbarkeit verlangt unabhängige Aufgaben in beschrifteten
Fertigkeitsgruppen. Das sind zwei Bauprinzipien, kein
Formulierungsunterschied. Vermutung, nicht geprüft: Die Kette
gehört zum Prüfungsblatt, die Überspringbarkeit zum
Unterrichtsblatt – dann wäre § 4 profilabhängig zu fassen.

## 9 Formlücke im Katalog – am 21.09. weitgehend geschlossen

Bei der Erhebung nannten 22 von 73 Einträgen ihre
Blatt-0-Voraussetzungen nur in Wortform, ohne Dateiverweis. Die
spätere Messung (Kennzahl 9) zeigte den wahren Umfang: 93 von 463
Fertigkeitszeilen in 23 Einträgen ohne Ziel. Die Läufe cfa4723,
f6e5fc5 und 795ca0a haben 182 Zuordnungen nachgetragen; offen
sind noch 24 Zeilen, und die sind kein Formproblem mehr: 20 zeigen
unter den Katalog, 3 sind Rechnerbedienung, 1 ist ein Grenzfall.
Für den Umbau heißt das: Blatt 0 ist maschinell auflösbar, wo ein
Katalogthema existiert – und wo keins existiert, sagt der Katalog
das künftig ausdrücklich, sobald über den Boden entschieden ist.
