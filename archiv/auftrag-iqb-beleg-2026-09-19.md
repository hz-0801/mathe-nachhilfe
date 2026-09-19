# Auftrag: IQB-Regel belegen

## Ausgangslage

Drei Stellen im Repo führen die IQB-Regel ohne amtlichen Beleg:
`abitur/abi.md` § 11 (Zeile „ab Abitur 2026"), `fhr/fhr.md` § 9
und `fhr/fhr-vorgaben.md` § 1 („Kein IQB-Pool"). Die Werkstatt hat
am 19.09.2026 recherchiert. Ergebnis: Die Pools stehen den Ländern
seit 2017 amtlich zur Verfügung (KMK-Beschlüsse, Bildungsstandards
AHR); Brandenburgs Entnahme ist durch den MBJS-Fachbrief 7 und die
gemessene Poolquote belegt; ein amtlicher Satz für 2026 existiert
nicht, die Prüfungsschwerpunkte 2026 nennen nur die
IQB-Formelsammlung. Ein FHR-Pool ist nicht vorgesehen, weil die
Pools auf den Bildungsstandards AHR beruhen.

Quellen (in dieser Schreibweise übernehmen):

- [BS-IQB] Bildungsserver Berlin-Brandenburg, „Zentralabitur
  (Brandenburg)", Abschnitt IQB, redaktionell LIBRA:
  https://bildungsserver.berlin-brandenburg.de/unterricht/pruefungen/abitur-brandenburg
- [IQB-Pool] IQB, „Abituraufgabenpools":
  https://www.iqb.hu-berlin.de/de/schule/sekundarstufe-ii/abituraufgabenpools/
- [FB-BB-7] MBJS, Fachbrief Mathematik Brandenburg Nr. 7,
  August 2023:
  https://bildungsserver.berlin-brandenburg.de/fileadmin/bbb/unterricht/fachbriefe_brandenburg/Mathematik/Fachbrief_Mathematik_BB_07.pdf
- [PS-GK-2026] MBJS, Prüfungsschwerpunkte Mathematik Grundkurs
  2026, Abschnitt 3 Hilfsmittel.

## Schritte

1. `abitur/abi.md` § 11, Tabellenzeile „ab Abitur 2026": in der
   Spalte Quelle ergänzen:
   „; Pool amtlich: [BS-IQB], [IQB-Pool]; Entnahme durch
   Brandenburg: [FB-BB-7]; für 2026 kein amtlicher Wortlaut,
   [PS-GK-2026] nennt nur die IQB-Formelsammlung – Beleg ist die
   Poolquote (Lauf 19). Recherche 19.09.2026."
   Die Kurzkürzel am Ende von § 11 (oder wo abi.md seine Quellen
   auflöst) mit den vier URLs oben ergänzen; gibt es keine solche
   Liste, die vier Zeilen als Absatz „Quellen zur IQB-Regel
   (19.09.2026)" unter die Tabelle setzen.

2. `abitur/abi-vorgaben.md` § 1, Punkt „IQB, Abituraufgabenpools
   Mathematik": am Ende anfügen: „Amtliche Grundlage und Beleg der
   Entnahme: abi.md § 11, Zeile ab 2026."

3. `fhr/fhr.md` § 9: den Satz, der den fehlenden IQB-Pool nennt,
   so ändern, dass er belegt ist:
   „Ein IQB-Pool für die Fachhochschulreife existiert nicht: die
   Pools entstehen auf Grundlage der Bildungsstandards für die
   Allgemeine Hochschulreife [IQB-Pool], die FHR-Prüfung beruht auf
   FOSFHRV und FOS-Rahmenlehrplan (§ 4). Belegt 19.09.2026."
   Das Wort „nicht belegt" darf danach in § 9 nicht mehr auf den
   IQB-Pool bezogen stehen; die Aussage zu den Buchstaben A, B, C
   bleibt unverändert.

4. `fhr/fhr-vorgaben.md` § 1, Punkt „Kein IQB-Pool": ergänzen um
   „(Beleg: fhr.md § 9, IQB-Pool-Seite, 19.09.2026)".

5. Falls `abi.md` oder `fhr.md` ein Änderungslog führen: je eine
   Zeile „19.09.2026: IQB-Regel belegt (Auftrag iqb-beleg)".

6. Diese Auftragsdatei nach `archiv/auftrag-iqb-beleg-2026-09-19.md`
   verschieben (git mv).

7. Ein Commit: „IQB-Regel belegt (abi § 11, fhr § 9)".

## Prüfungen

- `grep -n "nicht belegt" fhr/fhr.md` zeigt keine Zeile mehr, die
  den IQB-Pool betrifft.
- Die vier URLs stehen wortgleich in `abi.md`.
- Keine Datei außer `abitur/abi.md`, `abitur/abi-vorgaben.md`,
  `fhr/fhr.md`, `fhr/fhr-vorgaben.md`, `archiv/` geändert; keine
  CSV berührt.

## Bericht (zurück in den Chat)

- Je Datei die geänderten Zeilennummern und den neuen Wortlaut.
- Ob abi.md eine Quellenliste hatte oder der Absatz neu ist.
- Commit-Hash.
- Letzte Zeile: „Push origin drücken".

## Regeln

- Nur Text ergänzen oder den einen Satz in fhr.md § 9 ersetzen;
  nichts umformulieren, was nicht genannt ist.
- Bei Unklarheit die einfachste Lesart wählen und im Bericht
  nennen, nicht rückfragen.
