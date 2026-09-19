# Projekt Prüfungssammlung – Archivbefund

Projekt: `erstellePrüfungssammlung()` · Zeitraum: 18.09.2026 – 19.09.2026 ·
Chats: 1 · Durchsicht: 19.09.2026

Eingefroren. Beschreibt den Stand seines Datums und wird nicht fortgeschrieben.

## 1 Anlass und Status

**Ziel**, ausdrücklich im Startauftrag § 1: alle greifbaren
Mathe-Abschlussprüfungen in durchsuchbare Sammlungen überführen – je
Prüfungsart ein PDF-Sammelband mit Inhaltsverzeichnis, Register und
durchlaufender Seitenzahl, aus dem sich gezielt von Seite bis Seite drucken
lässt, dazu ein Markdown-Korpus zum Nachschlagen. Vier Prüfungsarten nach den
Profilen des Katalogprojekts (msa, fhr, abi, iqb). Nur für den eigenen
Gebrauch; Verlagsmaterial bleibt lokal.

**Anlass**: nicht ausdrücklich genannt, aus dem Startauftrag ableitbar. § 3
hält fest, dass das Material mit Auftrag N des Katalogprojekts am 18.09.2026
vollständig gesichert und geordnet war – 784 Dateien, 929,8 MB. Das Projekt
setzt an dieser Stelle an: Der Bestand war vollständig, aber nicht
adressierbar. Der Katalog nennt je Teilaufgabe nur die Fundstelle (Heft,
Seite); was fehlte, war ein Träger, auf dem diese Fundstelle eine feste,
druckbare Seite hat, und ein Volltext, den der Katalog nicht hält.

**Status: teilweise erreicht.** Letzter Chat 19.09.2026.

Erreicht:

- Musterband fhr gebaut (18.09.2026): `band-bau.py`, `fhr-band-struktur.py`,
  `fhr-band.csv`, `band-anleitung.md`; Ausgabe `baende/` lokal. Bis v0.4
  nachgebessert (Vorspann 13 Seiten, Vorrat acht Jahrgänge, Reservemeldung in
  freien Reserveseiten).
- Markdown-Korpus über `korpus-bau.py`, rein maschinell: Etappe 1 (msa und
  fhr, 52 Dateien), Etappe 2 (abi amtlich 2011–2018, 44 Dateien) und Etappe 4
  (iqb, 624 von 624 echten Kennungen) vollständig.
- Die Arbeit ist in die Jahresroutine des Katalogprojekts eingegangen
  (konzept.md § 7 Schritt 10: erst erfassen, dann bauen).

Nicht erreicht:

- Bände für msa, abi und iqb: nicht gebaut. Nur fhr hat einen.
- OCR (Etappe 3, die acht Bildscan-Verlagshefte abi 2022–2025, 664,5 MB):
  blockiert, weil Tesseract und Ghostscript ohne Administratorrechte nicht
  installierbar sind. Damit bleibt der einzige Teil des Bestands ohne
  Textebene weiter ohne Textebene – das Ziel „durchsuchbar" ist für die
  abi-Verlagsbände nicht erfüllt.

**Ablösung:** keine. Das Projekt wurde nicht von einem anderen abgelöst,
sondern in Claude Code ausgeführt und im Hauptrepo dokumentiert (Ordner
`werkzeuge/`, konzept.md § 2 als Baustein, § 7 Schritt 10, README).

## 2 Was in den Chats steht und im Repo fehlt

Drei Funde, alle aus dem Chat vom 19.09.2026.

**2-up gehört nicht in den Band** (19.09.2026). Zwei A5-Seiten auf ein
A4-Blatt zu legen ist Druckeinstellung, nicht Bandeigenschaft, und wird nicht
eingebaut. Grund: Es halbiert die Auflösung des Druckfensters – zwei Aufgaben
teilen sich dann eine Bandseite – und legt auf eine Druckform fest, die bei
Abbildungen und Koordinatensystemen unerwünscht sein kann. Die Papierersparnis
ist dadurch nicht verloren; sie macht der Druckertreiber. Der Startauftrag § 5
führte 2-up noch als Argument für Originalseiten; das ist damit entkoppelt.

**Neusatz verworfen** (19.09.2026). Der Band übernimmt die Heftseiten
unverändert. Zwei Gründe, die im Repo nur als Ergebnis, nicht als Abwägung
stehen: Erstens ist Heftseite → Bandseite bei Originalseiten ein fester Offset
je Heft, das Register fällt damit per Addition aus dem Katalog heraus; bei
Neusatz verschiebt sich jeder Umbruch, die Katalogseiten werden wertlos, und
die Registerseiten müssten aus dem Satzlauf zurückgemeldet werden – der
Katalog hinge dann am Satzprozess, obwohl die Bände ihn nur lesen. Zweitens
wäre „Inhalt identisch" bei Neusatz eine Behauptung, die eine Sichtprüfung
jeder Aufgabe verlangt: Formeln, Vektoren und Abbildungen zerfallen bei der
Textextraktion, und ein verlorener Exponent ist in einer Prüfungsaufgabe ein
sachlicher Fehler, den beim Durchsehen von 253 Zeilen niemand zuverlässig
findet.

**Drei offene Punkte des Startauftrags sind nie aufgegriffen worden**
(Startauftrag § 5, 18.09.2026; im einzigen Chat des Projekts nicht behandelt):
was ein Band umfasst, wenn es mehr als eine Prüfungsart gibt (abi gk und lk
getrennt oder zusammen; iqb nach Jahrgang, Prüfungsteil oder Sachgebiet);
CAS/MMS als eigene Bände, Anhang oder weggelassen; und die Gliederungstiefe
des Druckfensters. Alle drei stellen sich erst beim zweiten Band. Einschränkung:
`band-anleitung.md` konnte bei dieser Durchsicht nicht gelesen werden (siehe
§ 3); dass die Punkte dort beantwortet sind, ist nicht ausgeschlossen.

## 3 Vollständigkeit

Nachzutragen sind die beiden Begründungen aus § 2 – 2-up als Druckeinstellung
und die Abwägung gegen Neusatz –, am besten in `werkzeuge/band-anleitung.md`,
die drei offenen Punkte in konzept.md § 6; im Übrigen bildet das Repo diesen
Projektstand ab. Vorbehalt: Die Arbeit lief über Claude Code, dessen Sitzungen
keine Chats dieses Projekts sind und bei dieser Durchsicht nicht durchsucht
wurden, und `band-anleitung.md` war nicht abrufbar – was dort steht und was in
den Code-Sitzungen besprochen wurde, ist in dieser Durchsicht nicht enthalten.
