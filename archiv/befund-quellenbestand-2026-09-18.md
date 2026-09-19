# Quellenbestand – Originaldateien unter hefte/ je Profil, Abgleich mit Quellenlisten und Servern
Befund, einmalig und eingefroren (namensschema.md § 2: befund-<gegenstand>-<datum>); Stand 18.09.2026 nach Auftrag N. Der Ordner hefte/ liegt neben dem Repo und bleibt außerhalb (.gitignore). Nichts wurde gelöscht; byteidentische Zweitstücke liegen in hefte/dubletten/ (Liste dubletten.md dort), den Ordner löscht der Lehrer selbst.

## 1 Was vor dem Auftrag da war

| Profil | Ort | Bestand | Befund |
|---|---|---|---|
| abi | hefte/ (flach) | 17 PDF (13 Verlagsdateien, 4 amtliche Berliner Grundkurshefte 2016/2017 WTR/CAS), 4 Textauszüge, 5 abgeschriebene Verlagstexte; 675,3 MB | wie abi-quellen.md § 8 (Auftrag M) |
| abi | OneDrive\Desktop\abi prüfunn (Download-Ordner des Lehrers) | 68 PDF, GK.zip (15 PDF), 749,7 MB: amtliche Hefte 2011–2018 (41 von 44 des Bildungsservers, dazu 17_Ma_GK_CAS doppelt), die 13 Verlagsdateien im Rohnamen (2022.pdf, 2022-bebb-lk.pdf, 2026-bebb-gk.pdf …), STARK-Band Berlin GK 2016–2022 mit Textebene (11710-nn-xx-JJJJ-00-pruefungsaufgaben.pdf), Prüfungsschwerpunkte 2026–2028, RLP GOST, Bildungsstandards, LISUM-Aufgaben | alle 83 Stücke (68 lose, 15 im Zip) sind nach dem Auftrag byteidentisch unter hefte/ vorhanden; nichts wurde von dort verschoben oder gelöscht |
| iqb | Scratchpad\pdf (Cache von iqb-quellen.py) | 624 PDF, 140,7 MB, dazu 22 Textauszüge; Teilmengen in Scratchpad\pool1718, pool19–25 (143 PDF) und Prüfungsschwerpunkte 2027 in ps/, ps2027/ | vollständig; die Teilmengen sind byteidentische Kopien |
| msa | – | keine Datei auf der Platte (Download-Ordner, Scratchpad, Temp durchsucht) | die zwölf Hefte wurden am 05.09.2026 in einer Chat-Sandbox geholt und nicht aufbewahrt |
| fhr | – | keine Datei; im Explorer-Verlauf ein Ordner OneDrive\Desktop\fos, der nicht mehr existiert | die sechzehn Hefte wurden am 12.09.2026 in einer Chat-Sandbox geholt und nicht aufbewahrt |

Bilddateien in hefte/ gab es keine; die „drei nicht zuzuordnenden Bilddateien" des letzten Laufs waren ein Zwischenergebnis der Auftrag-M-Zählung in hefte-md/ (Zählfehler, im Befund heftkorpus berichtigt: alle 94 Abbildungen sind verlinkt). Seitenbilder und Ausschnitte der Erfassungsläufe (heft_*, pool*r, kopf, montage, seiten im Scratchpad) sind abgeleitet, keine Originale, und blieben liegen.

## 2 Ordnung nach dem Auftrag

hefte/abi/, hefte/msa/, hefte/fhr/, hefte/iqb/, je mit sonstiges/; hefte/dubletten/. Dateiname = Kennung des Katalogs: abi papier-Kürzel (abi.md § 4; Zusätze -stark für die Verlagsfassung eines amtlich vorhandenen Hefts, -teil1/-teil2 für die zweiteiligen Brandenburger Dateien 2016), msa und fhr `<jahr>-<papier>` klein (namensschema.md § 2), iqb die Kennung aus iqb-quellen.csv (Cache-Name von iqb-quellen.py: `python iqb-quellen.py hefte/iqb`). Ohne Kennung und deshalb unter Servernamen in sonstiges/: die gemeinsamen Hefte 2011–2013 (Kürzel bebb oder bbbe offen), die Gymnasialhefte P10 (kein papier-Wert in msa.md), die Verlagsfassung Berlin GK 2022 (Kopfzeile „Berlin", Katalog führt 2022-bebb-gk), Vorgabendokumente, Textauszüge, Verlagstexte. Kein Fall für hefte/unklar/.

Gesamt: 784 Dateien, 929,8 MB unter hefte/ ohne dubletten/; dazu 144 Zweitstücke in dubletten/ (32,6 MB).

## 3 Profil abi – hefte/abi/ (85 Dateien, 736,6 MB)

Server: Jahresseite abituraufgaben-2011 mit 44 PDF-Links, Jahrgänge 2011–2018 (2011–2013 unter gemeinsames_Abitur_Be_BB, 2014–2018 unter Zabi_Mathematik), keine Erwartungshorizonte; alle 44 geholt, 0 nicht holbar. Vier davon lagen schon vor und sind byteidentisch mit dem Server (2016-be-gk, 2016-be-gk-cas, 2017-be-gk, 2017-be-gk-cas).

| Datei | Herkunft | Seiten | Textebene | Größe | Auftrag N | Katalog |
|---|---|---|---|---|---|---|
| 2014-bb-ea-cas.pdf | BB_14_Ma_L_CAS_Aufgaben.pdf (Bildungsserver) | 8 | ja | 1,1 MB | neu geholt | nicht im Katalog |
| 2014-bb-ea.pdf | BB_14_Ma_L_Aufgaben.pdf (Bildungsserver) | 9 | ja | 1,3 MB | neu geholt | nicht im Katalog |
| 2014-be-gk-cas.pdf | 14_Ma_GK_CAS_Aufgaben.pdf (Bildungsserver) | 8 | ja | 3,7 MB | neu geholt | nicht im Katalog |
| 2014-be-gk.pdf | 14_Ma_GK_Aufgaben.pdf (Bildungsserver) | 10 | ja | 5,1 MB | neu geholt | nicht im Katalog |
| 2014-be-lk-cas.pdf | BE_14_CMa_LK_Aufgaben.pdf (Bildungsserver) | 8 | ja | 0,9 MB | neu geholt | nicht im Katalog |
| 2014-be-lk.pdf | BE_14_Ma_LK_Aufgaben.pdf (Bildungsserver) | 9 | ja | 1,0 MB | neu geholt | nicht im Katalog |
| 2015-bb-ea-cas.pdf | BB_15_Ma_CAS_Aufgaben.pdf (Bildungsserver) | 9 | ja | 1,1 MB | neu geholt | nicht im Katalog |
| 2015-bb-ea.pdf | BB_15_Ma_Aufgaben.pdf (Bildungsserver) | 9 | ja | 1,2 MB | neu geholt | nicht im Katalog |
| 2015-be-gk-cas.pdf | BE_15_Ma_GK_Aufgaben_CAS.pdf (Bildungsserver) | 11 | ja | 0,9 MB | neu geholt | nicht im Katalog |
| 2015-be-gk.pdf | BE_15_Ma_GK_Aufgaben.pdf (Bildungsserver) | 12 | ja | 1,0 MB | neu geholt | nicht im Katalog |
| 2015-be-lk-cas.pdf | BE_15_Ma_LK_Aufgaben_CAS.pdf (Bildungsserver) | 8 | ja | 1,3 MB | neu geholt | nicht im Katalog |
| 2015-be-lk.pdf | BE_15_Ma_LK_Aufgaben.pdf (Bildungsserver) | 11 | ja | 1,7 MB | neu geholt | nicht im Katalog |
| 2016-bb-ea-cas-teil1.pdf | BB_16_Ma_CAS_Aufgaben_1.pdf (Bildungsserver) | 3 | ja | 0,8 MB | neu geholt | nicht im Katalog |
| 2016-bb-ea-cas-teil2.pdf | BB_16_Ma_CAS_Aufgaben_2.pdf (Bildungsserver) | 5 | ja | 0,9 MB | neu geholt | nicht im Katalog |
| 2016-bb-ea-teil1.pdf | BB_16_Ma_Aufgaben_1.pdf (Bildungsserver) | 3 | ja | 0,8 MB | neu geholt | nicht im Katalog |
| 2016-bb-ea-teil2.pdf | BB_16_Ma_Aufgaben_2.pdf (Bildungsserver) | 6 | ja | 1,0 MB | neu geholt | nicht im Katalog |
| 2016-be-gk-cas.pdf | 16_Ma_GK_CAS_Aufgaben.pdf (Bildungsserver) | 8 | ja | 1,1 MB | vorhanden | nicht im Katalog |
| 2016-be-gk-stark.pdf | 11710-nn-xx-2016-00-pruefungsaufgaben.pdf, STARK-Band Berlin (Download-Ordner) | 40 | ja | 1,0 MB | vorhanden | nicht im Katalog |
| 2016-be-gk.pdf | 16_Ma_GK_Aufgaben.pdf (Bildungsserver) | 9 | ja | 1,1 MB | vorhanden | nicht im Katalog |
| 2016-be-lk-cas.pdf | 16_Ma_LK_CAS_Aufgaben.pdf (Bildungsserver) | 7 | ja | 1,0 MB | neu geholt | nicht im Katalog |
| 2016-be-lk.pdf | 16_Ma_LK_Aufgaben.pdf (Bildungsserver) | 8 | ja | 1,2 MB | neu geholt | nicht im Katalog |
| 2017-bb-ea-cas.pdf | BB_17_Ma_CAS_Aufgaben.pdf (Bildungsserver) | 10 | ja | 1,1 MB | neu geholt | nicht im Katalog |
| 2017-bb-ea.pdf | BB_17_Ma_Aufgaben.pdf (Bildungsserver) | 10 | ja | 1,0 MB | neu geholt | erfasst |
| 2017-be-gk-cas.pdf | 17_Ma_GK_CAS_Aufgaben.pdf (Bildungsserver) | 8 | ja | 1,5 MB | vorhanden | nicht im Katalog |
| 2017-be-gk-stark.pdf | 11710-nn-xx-2017-00-pruefungsaufgaben.pdf, STARK-Band Berlin (Download-Ordner) | 39 | ja | 1,4 MB | vorhanden | nicht im Katalog |
| 2017-be-gk.pdf | 17_Ma_GK_Aufgaben.pdf (Bildungsserver) | 8 | ja | 1,4 MB | vorhanden | nicht im Katalog |
| 2017-be-lk-cas.pdf | 17_Ma_LK_CAS_Aufgaben_neu.pdf (Bildungsserver) | 9 | ja | 1,3 MB | neu geholt | nicht im Katalog |
| 2017-be-lk.pdf | 17_Ma_LK_Aufgaben_neu.pdf (Bildungsserver) | 10 | ja | 1,1 MB | neu geholt | nicht im Katalog |
| 2018-bb-ea-cas.pdf | BB_18_Ma_CAS_Aufgaben.pdf (Bildungsserver) | 12 | ja | 1,9 MB | neu geholt | nicht im Katalog |
| 2018-bb-ea.pdf | BB_18_Ma_Aufgaben.pdf (Bildungsserver) | 13 | ja | 2,0 MB | neu geholt | erfasst |
| 2018-be-gk-cas.pdf | 18_Ma_GK_CAS_Aufgaben.pdf (Bildungsserver) | 10 | ja | 2,2 MB | neu geholt | nicht im Katalog |
| 2018-be-gk-stark.pdf | 11710-nn-xx-2018-00-pruefungsaufgaben.pdf, STARK-Band Berlin (Download-Ordner) | 38 | ja | 1,1 MB | vorhanden | nicht im Katalog |
| 2018-be-gk.pdf | 18_Ma_GK_Aufgaben.pdf (Bildungsserver) | 11 | ja | 3,1 MB | neu geholt | erfasst |
| 2018-be-lk-cas.pdf | 18_Ma_LK_CAS_Aufgaben.pdf (Bildungsserver) | 9 | ja | 1,7 MB | neu geholt | nicht im Katalog |
| 2018-be-lk.pdf | 18_Ma_LK_Aufgaben.pdf (Bildungsserver) | 11 | ja | 1,9 MB | neu geholt | nicht im Katalog |
| 2019-be-gk.pdf | STARK-Band, PDF (Download-Ordner des Lehrers) | 46 | ja | 1,4 MB | vorhanden | erfasst |
| 2020-be-gk.pdf | STARK-Band, PDF (Download-Ordner des Lehrers) | 49 | ja | 1,2 MB | vorhanden | erfasst |
| 2021-be-gk.pdf | STARK-Band, PDF (Download-Ordner des Lehrers) | 45 | ja | 1,0 MB | vorhanden | erfasst |
| 2022-bebb-gk.pdf | STARK-Band, Scan (Download-Ordner des Lehrers) | 12 | nein | 78,0 MB | vorhanden | erfasst |
| 2022-bebb-lk.pdf | STARK-Band, Scan (Download-Ordner des Lehrers) | 15 | nein | 99,4 MB | vorhanden | erfasst |
| 2023-bebb-gk.pdf | STARK-Band, Scan (Download-Ordner des Lehrers) | 14 | nein | 90,1 MB | vorhanden | erfasst |
| 2023-bebb-lk.pdf | STARK-Band, Scan (Download-Ordner des Lehrers) | 14 | nein | 93,1 MB | vorhanden | erfasst |
| 2024-bebb-gk.pdf | STARK-Band, Scan (Download-Ordner des Lehrers) | 10 | nein | 80,5 MB | vorhanden | erfasst |
| 2024-bebb-lk.pdf | STARK-Band, Scan (Download-Ordner des Lehrers) | 13 | nein | 85,6 MB | vorhanden | erfasst |
| 2025-bebb-gk.pdf | STARK-Band, Scan (Download-Ordner des Lehrers) | 8 | nein | 68,2 MB | vorhanden | erfasst |
| 2025-bebb-lk.pdf | STARK-Band, Scan (Download-Ordner des Lehrers) | 11 | nein | 69,6 MB | vorhanden | erfasst |
| 2026-bb-ea.pdf | STARK-Band, PDF (Download-Ordner des Lehrers) | 47 | ja | 1,1 MB | vorhanden | erfasst |
| 2026-bb-gk.pdf | STARK-Band, PDF (Download-Ordner des Lehrers) | 36 | ja | 0,9 MB | vorhanden | erfasst |

sonstiges/ (37 Dateien):

| Datei | Umfang | Größe | Auftrag N |
|---|---|---|---|
| 11710-nn-xx-2022-00-pruefungsaufgaben.pdf | 47 S., Textebene ja | 0,9 MB | vorhanden |
| 11_Ma_Aufgaben_GK.pdf | 10 S., Textebene ja | 1,0 MB | neu geholt |
| 11_Ma_Aufgaben_GK_CAS.pdf | 9 S., Textebene ja | 0,8 MB | neu geholt |
| 11_Ma_Aufgaben_LK.pdf | 12 S., Textebene ja | 1,1 MB | neu geholt |
| 11_Ma_Aufgaben_LK_CAS.pdf | 9 S., Textebene ja | 0,8 MB | neu geholt |
| 12_Ma_Aufgaben_G_.pdf | 8 S., Textebene ja | 0,4 MB | neu geholt |
| 12_Ma_Aufgaben_G_CAS_.pdf | 8 S., Textebene ja | 0,3 MB | neu geholt |
| 12_Ma_Aufgaben_L_.pdf | 11 S., Textebene ja | 0,5 MB | neu geholt |
| 12_Ma_Aufgaben_L_CAS.pdf | 8 S., Textebene ja | 0,5 MB | neu geholt |
| 13_Ma_GK_Aufgaben.pdf | 8 S., Textebene ja | 0,7 MB | neu geholt |
| 13_Ma_GK_CAS_Aufgaben.pdf | 8 S., Textebene ja | 1,0 MB | neu geholt |
| 13_Ma_LK_Aufgaben.pdf | 10 S., Textebene ja | 0,8 MB | neu geholt |
| 13_Ma_LK_CAS_Aufgaben.pdf | 7 S., Textebene ja | 0,7 MB | neu geholt |
| 2012_10_18-Bildungsstandards-Mathe-Abi.pdf | 73 S., Textebene ja | 1,6 MB | vorhanden |
| 2016-be-gk-cas.txt | – | 17,2 KB | vorhanden |
| 2016-be-gk.txt | – | 20,1 KB | vorhanden |
| 2017-be-gk-cas.txt | – | 16,3 KB | vorhanden |
| 2017-be-gk.txt | – | 19,1 KB | vorhanden |
| PSP_Mathematik_GK_BB_2026_aktualisiert.pdf | 6 S., Textebene ja | 0,2 MB | vorhanden |
| PSP_Mathematik_LK_BB_2026_aktualisiert.pdf | 7 S., Textebene ja | 0,2 MB | vorhanden |
| PS_Mathematik_GK_2027.pdf | 6 S., Textebene ja | 0,2 MB | vorhanden |
| PS_Mathematik_GK_2027.txt | – | 18,9 KB | vorhanden |
| PS_Mathematik_GK_2028_formal_aktualisiert.pdf | 6 S., Textebene ja | 0,2 MB | vorhanden |
| PS_Mathematik_LK_2027.pdf | 7 S., Textebene ja | 0,2 MB | vorhanden |
| PS_Mathematik_LK_2027.txt | – | 20,2 KB | vorhanden |
| PS_Mathematik_LK_2028_formal_aktualisiert.pdf | 7 S., Textebene ja | 0,2 MB | vorhanden |
| Teil_C_RLP_GOST_2022_Mathematik.pdf | 32 S., Textebene ja | 0,6 MB | vorhanden |
| hinweise-2021-be-gk.md | – | 3,2 KB | vorhanden |
| hinweise-2027-bebb.md | – | 6,9 KB | vorhanden |
| oHiMi-2013_04_22.pdf | 44 S., Textebene ja | 0,5 MB | vorhanden |
| ps_mathematik_2027_gk.pdf | 7 S., Textebene ja | 0,4 MB | vorhanden |
| ps_mathematik_2027_gk.txt | – | 20,5 KB | vorhanden |
| ps_mathematik_2027_lk.pdf | 8 S., Textebene ja | 0,4 MB | vorhanden |
| ps_mathematik_2027_lk.txt | – | 22,4 KB | vorhanden |
| stichwort-2021-be-gk.md | – | 6,4 KB | vorhanden |
| stichwort-2027-bebb-gk.md | – | 8,6 KB | vorhanden |
| stichwort-2027-bebb-lk.md | – | 9,5 KB | vorhanden |

Abgleich: Katalog 16 Hefte, alle mit Datei (2017-bb-ea, 2018-bb-ea, 2018-be-gk neu geholt – bis heute wurden sie je Lauf vom Server geholt). Datei ohne Katalogeintrag: 32 (alle amtlichen Hefte außer den drei Leitfassungen, drei -stark-Fassungen). Zweite Fassungen desselben Inhalts, keine Dubletten: 2016/2017/2018-be-gk amtlich neben -stark (Verlag, mit Tipps und Lösungen); 2022-bebb-gk Bildscan neben sonstiges/11710-nn-xx-2022 (Verlagsfassung Berlin, Textebene, Aufgabengleichheit nicht geprüft); die Prüfungsschwerpunkte 2027 je Land als PDF und Textauszug. Auf keiner Quelle beschaffbar: Landeshefte ab 2019 amtlich (nur Verlag), Berlin 2026 (kein Band, keine Veröffentlichung), CAS-Fassungen 2018–2021 (abi-quellen.md § 5).

## 4 Profil msa – hefte/msa/ (33 Dateien, 39,7 MB)

Server: Seite pruefungsaufgaben-mathematik mit 33 PDF-Links, **Spanne 2014–2026** – je Jahrgang das Oberschulheft (ab 2026 getrennt EBR/FOR) und die Gymnasialhefte (bis 2025); keine Lösungen, keine Erwartungshorizonte, keine Vorgabendokumente auf der Seite. Alle 33 geholt, 0 nicht holbar.

| Datei | Herkunft | Seiten | Textebene | Größe | Auftrag N | Katalog |
|---|---|---|---|---|---|---|
| 2014-os.pdf | 14_P10_Ma_Set2_A.pdf (Bildungsserver) | 9 | ja | 0,5 MB | neu geholt | erfasst |
| 2015-os.pdf | 15_P10_Ma_A.pdf (Bildungsserver) | 9 | ja | 0,9 MB | neu geholt | erfasst |
| 2016-os.pdf | 16_P10_Ma_A.pdf (Bildungsserver) | 9 | ja | 0,9 MB | neu geholt | erfasst |
| 2017-os.pdf | 17_P10_Ma_A.pdf (Bildungsserver) | 15 | ja | 1,4 MB | neu geholt | erfasst |
| 2018-os.pdf | 18_P10_Ma_A.pdf (Bildungsserver) | 15 | ja | 2,8 MB | neu geholt | erfasst |
| 2019-os.pdf | 19_P10_Ma_A.pdf (Bildungsserver) | 15 | ja | 1,4 MB | neu geholt | erfasst |
| 2020-os.pdf | 20_P10_Ma_A.pdf (Bildungsserver) | 15 | ja | 1,3 MB | neu geholt | erfasst |
| 2021-os.pdf | 21_P10_Ma_A.pdf (Bildungsserver) | 15 | ja | 1,3 MB | neu geholt | erfasst |
| 2022-os.pdf | 22_P10_Ma_EBR_FOR.pdf (Bildungsserver) | 13 | ja | 1,2 MB | neu geholt | erfasst |
| 2023-os.pdf | 23_P10_Ma_A.pdf (Bildungsserver) | 12 | ja | 1,3 MB | neu geholt | erfasst |
| 2024-os.pdf | 24_P10_Ma_A.pdf (Bildungsserver) | 14 | ja | 1,5 MB | neu geholt | erfasst |
| 2025-os.pdf | 25_P10_Ma_A.pdf (Bildungsserver) | 15 | ja | 1,4 MB | neu geholt | erfasst |
| 2026-ebr.pdf | 26_P10_Ma_EBR_A.pdf (Bildungsserver) | 10 | ja | 1,3 MB | neu geholt | nicht im Katalog |
| 2026-for.pdf | 26_P10_Ma_FOR_A.pdf (Bildungsserver) | 15 | ja | 1,6 MB | neu geholt | erfasst |

sonstiges/ – 19 Gymnasialhefte 2014–2025 (kein papier-Wert im Profil, nicht Bestand: Entscheidung 18), alle mit Textebene:

| Datei | Umfang | Größe | Auftrag N |
|---|---|---|---|
| 14_P10_Gym_Ma_A_Set1.pdf | 7 S., Textebene ja | 0,5 MB | neu geholt |
| 15_P10_Ma_Gym_A.pdf | 7 S., Textebene ja | 1,0 MB | neu geholt |
| 16_P10_Gym_Ma_A.pdf | 11 S., Textebene ja | 1,3 MB | neu geholt |
| 17_P10_Ma_Gym_A.pdf | 11 S., Textebene ja | 1,4 MB | neu geholt |
| 18_P10_Ma_Gym_A.pdf | 11 S., Textebene ja | 2,4 MB | neu geholt |
| 19_P10_Ma_Gym_A_1.pdf | 3 S., Textebene ja | 0,8 MB | neu geholt |
| 19_P10_Ma_Gym_A_2.pdf | 9 S., Textebene ja | 1,1 MB | neu geholt |
| 20_P10_Ma_Gym_A_1.pdf | 3 S., Textebene ja | 0,8 MB | neu geholt |
| 20_P10_Ma_Gym_A_2.pdf | 9 S., Textebene ja | 1,2 MB | neu geholt |
| 21_P10_Ma_Gym_A1.pdf | 3 S., Textebene ja | 0,7 MB | neu geholt |
| 21_P10_Ma_Gym_A2.pdf | 9 S., Textebene ja | 1,1 MB | neu geholt |
| 22_P10_Ma_Gym_Aufgaben_1_und_2.pdf | 3 S., Textebene ja | 0,8 MB | neu geholt |
| 22_P10_Ma_Gym_Aufgaben_3_bis_6.pdf | 9 S., Textebene ja | 1,2 MB | neu geholt |
| 23_P10_Ma_Gym_A1.pdf | 3 S., Textebene ja | 1,0 MB | neu geholt |
| 23_P10_Ma_Gym_A2.pdf | 9 S., Textebene ja | 1,4 MB | neu geholt |
| 24_P10_Ma_Gym_A1.pdf | 3 S., Textebene ja | 0,8 MB | neu geholt |
| 24_P10_Ma_Gym_A2.pdf | 9 S., Textebene ja | 1,4 MB | neu geholt |
| 25_P10_Ma_Gym_A1.pdf | 3 S., Textebene ja | 0,9 MB | neu geholt |
| 25_P10_Ma_Gym_A2.pdf | 8 S., Textebene ja | 1,2 MB | neu geholt |

Abgleich: Katalog 13 Hefte (2014–2025 OS, 2026 FOR), alle mit Datei; Datei ohne Katalogeintrag: 2026-ebr.pdf (zurückgestellt, msa-pruefungen.md § 2). Die Musteraufgaben 2028 (Fachbrief 10) liegen nicht auf dieser Seite und wurden nicht gesucht.

## 5 Profil fhr – hefte/fhr/ (19 Dateien, 12,8 MB)

Server: Seite pruefungen-fos-bb mit 27 PDF-Links; Aufgabenhefte **Spanne 2019–2026**, je Jahrgang zwei Lehrerhefte (mit Erwartungshorizont), dazu die Prüfungsschwerpunkte Mathematik 2026/27 und 2027/28 und das Rundschreiben MBJS_RS_07-26 (mitgenommen), Deutsch/Englisch-Dokumente (acht, nicht Mathematik, nicht geholt). Alle 19 geholt, 0 nicht holbar.

| Datei | Herkunft | Seiten | Textebene | Größe | Auftrag N | Katalog |
|---|---|---|---|---|---|---|
| 2019-a.pdf | 19_Mathematik_FOS_Lehrer_A.pdf (Bildungsserver) | 10 | ja | 0,8 MB | neu geholt | erfasst |
| 2019-c.pdf | 19_Mathematik_FOS_Lehrer_C.pdf (Bildungsserver) | 9 | ja | 0,8 MB | neu geholt | erfasst |
| 2020-a.pdf | 20_FOS_Ma_EH_A.pdf (Bildungsserver) | 9 | ja | 0,7 MB | neu geholt | erfasst |
| 2020-c.pdf | 20_FOS_Ma_EH_C.pdf (Bildungsserver) | 9 | ja | 0,8 MB | neu geholt | erfasst |
| 2021-a.pdf | 21_FOS_Ma_LH_A.pdf (Bildungsserver) | 9 | ja | 0,8 MB | neu geholt | erfasst |
| 2021-b.pdf | 21_FOS_Ma_LH_B.pdf (Bildungsserver) | 8 | ja | 1,4 MB | neu geholt | erfasst |
| 2022-b.pdf | 22_FOS_Ma_B_LH.pdf (Bildungsserver) | 10 | ja | 0,5 MB | neu geholt | erfasst |
| 2022-c.pdf | 22_FOS_Ma_C_LH.pdf (Bildungsserver) | 10 | ja | 0,6 MB | neu geholt | erfasst |
| 2023-a.pdf | 23_FOS_Ma_A_LH.pdf (Bildungsserver) | 10 | ja | 0,3 MB | neu geholt | erfasst |
| 2023-c.pdf | 23_FOS_Ma_C_LH.pdf (Bildungsserver) | 8 | ja | 0,4 MB | neu geholt | erfasst |
| 2024-b.pdf | 24_FOS_Ma_B_LH.pdf (Bildungsserver) | 10 | ja | 1,0 MB | neu geholt | erfasst |
| 2024-c.pdf | 24_FOS_Ma_C_LH.pdf (Bildungsserver) | 10 | ja | 1,0 MB | neu geholt | erfasst |
| 2025-a.pdf | 25_FOS_Ma_LH_A.pdf (Bildungsserver) | 9 | ja | 0,8 MB | neu geholt | erfasst |
| 2025-c.pdf | 25_FOS_Ma_LH_C.pdf (Bildungsserver) | 10 | ja | 1,0 MB | neu geholt | erfasst |
| 2026-b.pdf | 26_FOS_Ma_LH_B.pdf (Bildungsserver) | 10 | ja | 0,8 MB | neu geholt | erfasst |
| 2026-c.pdf | 26_FOS_Ma_LH_C.pdf (Bildungsserver) | 10 | ja | 0,6 MB | neu geholt | erfasst |

sonstiges/:

| Datei | Umfang | Größe | Auftrag N |
|---|---|---|---|
| MBJS_RS_07-26.pdf | 7 S., Textebene ja | 0,2 MB | neu geholt |
| Pruefungsschwerpunkte_Mathematik_2026-2027.pdf | 2 S., Textebene ja | 0,1 MB | neu geholt |
| Pruefungsschwerpunkte_Mathematik_2027-2028.pdf | 2 S., Textebene ja | 92,4 KB | neu geholt |

Abgleich: Katalog 16 Hefte, alle mit Datei; keine Datei ohne Katalogeintrag. Die Nachschreibevorschläge liegen nicht auf dem Server (fhr-pruefungen.md).

## 6 Profil iqb – hefte/iqb/ (647 Dateien, 140,7 MB)

Server: IQB-Übersicht (52 Seiten, Stand 13.09.2026 in iqb-quellen.csv). Alle 624 Kennungen aus iqb-quellen.csv liegen als `<Kennung>.pdf` vor (624 Dateien, davon 624 mit Textebene, 0 ohne), 0 fehlend, 0 neu geholt (der Cache war vollständig). Erfasst (mindestens eine Katalogzeile): 404 Kennungen; Dateidubletten ohne Zeile (Spalte dateidublette_von): 35; nicht erfasst (Reserve-Stapel und Beispielaufgaben): 185. sonstiges/: 22 Textauszüge 2023 grundlegend und eine 153-Byte-Fehlantwort (404) unter dem Namen 2025MerhoehtBAnalysisMMS3.pdf – keine Kennung, kein PDF; ihr Zweitstück 2025MgrundlegendBAnalysisMMS3.pdf liegt in dubletten/. Ob die Übersicht des IQB heute mehr als 624 Kennungen führt, wurde nicht neu gescannt (iqb-quellen.py schreibt iqb-quellen.csv).

## 7 Dubletten (Punkt 3)

Vergleich über SHA-256 aller Dateien unter hefte/ und im Download-Ordner. In hefte/dubletten/: 144 Stücke – 143 Kopien von Pool-Dateien aus den Scratchpad-Teilmengen und die Fehlantwort oben; je Zeile das Original in dubletten.md. Innerhalb von hefte/ sonst keine byteidentischen Zweitstücke (verschiedene Kennungen tragen verschiedene Bytes). Der Download-Ordner des Lehrers hält 83 byteidentische Zweitstücke zu Dateien unter hefte/ und nichts, was dort fehlt; er wurde nicht angerührt (Löschen ist Sache des Lehrers). Keine Dubletten sind: die amtlichen und die Verlagsfassungen 2016–2018 Berlin GK (andere Fassung), Bildscan und Berlin-Verlagsfassung 2022 GK, Prüfungsschwerpunkte als PDF und als Textauszug.

## 8 Textebene

Alle amtlichen Dateien (abi 44, msa 33, fhr 19, iqb 624), die Verlagsfassungen 2016–2022 Berlin GK und die Bände 2019–2021 und 2026 haben eine Textebene. Ohne Textebene sind nur die acht Bildscans 2022–2025 (bebb gk/lk, 664,5 MB); eine Umwandlung (OCR) beträfe genau diese acht.
