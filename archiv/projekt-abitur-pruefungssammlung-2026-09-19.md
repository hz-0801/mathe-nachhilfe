# Projekt: Abitur-Prüfungssammlung Berlin/Brandenburg

Projektname: Abitur-Prüfungssammlung (Chattitel „Sammlung von Abitur-Mathematikprüfungen Brandenburg"; ein Projektname war nicht auslesbar, der Dateiname ist daraus gebildet)
Zeitraum: 07.09.2026 (ein Tag)
Zahl der Chats: 1
Datum der Durchsicht: 19.09.2026
Gegengelesen gegen: README.md, konzept.md, blatt-konzept.md, abitur/abi-quellen.md (v0.8, 18.09.2026), abitur/iqb-quellen.md (v0.5, 17.09.2026) sowie die übrigen Profildateien des Repos, Stand 19.09.2026

## 1 Warum dieses Projekt entstand

Eine ausdrückliche Motivation steht nirgends. Sie ist nur aus dem ersten Auftrag
ableitbar: Gesucht war eine Sammlung aller frei zugänglichen Original-Abiturprüfungen
Mathematik der letzten fünfzehn Jahre in Brandenburg/Berlin, als ZIP, getrennt nach
Grundkurs und Leistungskurs, beschränkt auf Prüfungen an Gymnasien. Wozu die Sammlung
dienen sollte – Nachhilfe, Katalogaufbau, Archiv – sagt der Chat nicht. Der zweite
Teil des Auftrags war ausdrücklich, vorher die Probleme zu benennen.

Status: **teilweise erreicht.** Geliefert wurden 44 Original-Klausuren 2011–2018 als
ZIP mit README. Der verlangte Zeitraum bis 2026 wurde nicht erreicht, weil es ab
Prüfungsjahr 2019 keine geschlossenen Originalklausuren mehr gibt, sondern nur den
IQB-Aufgabenpool aus Einzeldateien – und weil die Domain iqb.hu-berlin.de aus der
damaligen Ausführungsumgebung nicht erreichbar war (im Repo seit dem 13.09.2026 anders:
`iqb-quellen.md` § 1 hält fest, dass die Domain mit curl erreichbar ist). Der Chat
endet am 07.09.2026 mit zwei offenen Fragen an den Lehrer, die nie beantwortet wurden;
abgebrochen wurde er nicht ausdrücklich.

Abgelöst wurde das Projekt (Annahme aus der Aktenlage, im Chat nicht gesagt) vom Repo
`hz-0801/mathe-nachhilfe`, konkret von den Profilen `abi` und `iqb`: Dort ist die
Quellenfrage ab dem 12./13.09.2026 anders beantwortet – Landeshefte ab 2019 über
Verlagsbände unter `hefte/` (lokal, nicht im Repo), der Pool über `iqb-quellen.py`
mit 624 Kennungen statt über einen Sammel-Download (konzept.md, Entscheidung 23).

## 2 Was in den Chats steht und im Repo fehlt

**07.09.2026 – Befund: die Hefte 2011–2013 liegen auf einem anderen Basis-Pfad.**
Die Jahrgänge ab 2014 liegen unter `.../abitur_bb/Zabi_Mathematik`, die Jahrgänge
2011, 2012 und 2013 je unter einem eigenen Verzeichnis
`.../gemeinsames_Abitur_Be_BB/Abituraufgaben/Abituraufgaben_<Jahr>`. `abi-quellen.md`
nennt in § 1 nur das erste Verzeichnis und regelt „Vollständige URL = Verzeichnis aus
§ 1 + Serverdatei" – für die zwölf Dateien 2011–2013 in § 8 trifft das nicht zu. Wer
sie erneut holen will, kommt mit der dort angegebenen Regel nicht ans Ziel.

**07.09.2026 – Offene Frage: Lizenz und Weitergabe des Materials.** Das IQB stellt die
Pooldateien frei zum Download bereit; ob eine gebündelte Weitergabe an Dritte zulässig
ist, wurde ausdrücklich nicht geprüft und nie nachgeholt. Für die
Bildungsserver-Hefte 2011–2018 wurde die Frage gar nicht gestellt. Das Repo regelt die
Lizenzfrage nur für die Quellentexte unter `quellen/` und schließt `hefte/` wegen der
Verlagsausgaben aus; in keiner Profildatei steht etwas zur Lizenz von Pool und
amtlichen Heften. Entschärft, solange das Material lokal bleibt – offen, sobald etwas
weitergegeben wird.

Erledigt durch die Profildateien und deshalb hier gestrichen: der Befund zu den
amtlich veröffentlichten Klausuren 2011–2018 (steht vollständig in `abi-quellen.md`
§ 3 und § 8, alle 44 Dateien mit Servernamen, Seitenzahl, gemeinsamen Heften bebb
2011–2013 und den zweiteiligen BB-Dateien 2016); der verworfene Sammel-Download aus
der Sandbox (von `iqb-quellen.md` § 1 und § 4 widerlegt); die offene Frage nach der
Beschaffung 2019–2026 (entschieden in `abi-quellen.md` § 5 und `iqb-quellen.md` § 4);
der Schulform-Filter (gegenstandslos, seit alle 44 amtlichen Hefte und alle 624
Pooldateien erfasst sind).

## 3 Vollständigkeit des Repos

Nachzutragen wären die abweichenden Basis-Pfade der Jahrgänge 2011–2013 in
`abitur/abi-quellen.md` § 1 und der ungeklärte Lizenzstand von Pool und amtlichen
Heften in `abitur/iqb-quellen.md`.
