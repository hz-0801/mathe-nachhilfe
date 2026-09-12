# Quellentexte – Übersicht

Textfassungen der drei Quellen, die für alle Katalogeinträge gebraucht werden.
Abgelegt, damit sie nicht in jedem Chat neu geholt und durchsucht werden müssen –
und weil ihre Erreichbarkeit nicht gesichert ist: Alle drei sind LISUM- bzw.
Bildungsserver-Erzeugnisse, und das LISUM wurde zum 31.12.2024 aufgelöst
(Nachfolger: LIBRA in Brandenburg, BLiQ in Berlin).

Erzeugt am 12.09.2026 mit `pdftotext -layout`.

## quelle-rlp-teil-c-mathematik-2023.txt  [RLP]

Rahmenlehrplan 1–10 Berlin-Brandenburg, Teil C Mathematik, Fassung 14.08.2023.
66 Seiten. Ab dem Schuljahr 2025/2026 gültig für die Jahrgangsstufen 1 bis 10.
Herausgeber: Senatsverwaltung für Bildung, Jugend und Familie Berlin und
Ministerium für Bildung, Jugend und Sport des Landes Brandenburg 2023.

Quelle: https://bildungsserver.berlin-brandenburg.de/fileadmin/bbb/unterricht/rahmenlehrplaene/Rahmenlehrplanprojekt/amtliche_Fassung/Teil_C_Mathematik_2015_10_13_Ma_14.08.2023_Berlin_23_11.pdf

## quelle-klett-fahrplan-ls-aa-berlin-2024.txt  [LS-AA]

Lambacher Schweizer Allgemeine Ausgabe, Klett: „Fahrplan Studyly Allgemeine
Ausgabe für Berlin“, Stand Oktober 2024. 43 Seiten. Kapitel und Lerneinheiten
Kl. 5–10 sowie Einführungs- und Qualifikationsphase, mit Zuordnung zum
RLP 1–10 BB 2023 (Niveaustufen D–H) und zum RLP GOST Berlin 2014.
© Klett – Gliederung als Beleg, keine Aufgaben.

Achtung: Die Textfassung ist mehrspaltig gesetzt; Kapitel stehen nicht in
Lesereihenfolge untereinander. Beim Suchen die Kapitelüberschrift verwenden,
nicht die Zeilenfolge.

Quelle: https://www.klett.de/inhalt/media_fast_path/145/Fahrplan_Lambacher_Schweizer_Studyly_AA_Berlin.pdf

## quelle-lisum-planungshilfen-7bis10.txt  [LISUM-PH]

LISUM, „Planungshilfen für einen kompetenzorientierten Mathematikunterricht,
Jahrgangsstufen 7 bis 10“, Gesamtdatei vom 02.09.2024, 21 Reihen.
Lizenz CC BY-SA 4.0 (LISUM 2023) – Text darf mit Quellenzeile übernommen werden.
Unverändert aus der Lieferung 2026-09-11j übernommen.

Achtung: zweispaltig; Wörter sind am Zeilenende getrennt und die Fortsetzung
steht nicht in der Folgezeile. Für Nulltreffer-Protokolle `katalog/_suche_quelle.py`
benutzen. Reihenliste finden mit:

    grep -n "^ \+Jahrgangsstufe .*Mathematik: " quelle-lisum-planungshilfen-7bis10.txt

Quelle: https://bildungsserver.berlin-brandenburg.de/fileadmin/bbb/unterricht/faecher/naturwissenschaften/mathematik/Planungshilfen_kompetenzorientierter_Unterricht/Sekundarstufe_I/Mathematik_PH_gesamt_7bis10_2024-09-02.pdf
Einzeldateien je Reihe im übergeordneten Ordner, z. B. `PH_Ma_Jg07_Zuordnungen.pdf`.

## Noch nicht abgelegt

- [MzDuF] LISUM, „Material zur Diagnose und Förderung im Mathematikunterricht“,
  je Leitidee eine PDF-Gesamtdatei (Seitenzahlen bis über 650). Lizenz wie die
  Planungshilfen: LISUM 2023, CC BY-SA 4.0. Downloadadresse noch nicht gefunden.
- [FS] Formelsammlung: Das P10-Formelblatt ist nicht öffentlich. Für die
  Sekundarstufe II gilt ab Abitur 2025 die IQB-Formelsammlung
  (iqb.hu-berlin.de/media/documents/N_Mathematisch-naturwissenschaftliche_Formelsammlung.pdf,
  Stand 14.02.2024, Mathematikteil S. 3–8).
