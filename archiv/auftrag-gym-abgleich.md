# Auftrag: Abgleichlauf nach der GYM-Erfassung

Stand 2026-09-24. Ordner mathe-nachhilfe. Modell Opus.

## Ausgangslage

Die GYM-Erfassung (archiv/auftrag-gym-erfassung.md, Bericht
msa/gym-bericht-2026-09.md) hat 248 Zeilen und 108 neue Typen
angelegt. Die Gegenlese des Lehrers am 24.09.2026 nach Kern § 6
(„Kontext, Zahlen und Format ändern den Typ nicht; trenne, wenn
der Lösungsweg ein anderer ist") ergibt: 29 der neuen Typen sind
Etiketten für eine Fertigkeit, die schon ein Typ trägt oder die
zwei neue Typen doppelt tragen; 32 weitere beschreiben eine
Aufgabe statt einer Fertigkeit und bekommen ein Etikett nach dem
Muster der Liste. Das Thema „Sinussatz" heißt künftig „Sinus- und
Kosinussatz", weil fünf GYM-Zeilen den Kosinussatz prüfen.

Das ist der Abgleichlauf nach Kern § 9: Etiketten vereinheitlichen
über ein Skript, das die Typenliste und alle Kataloge zugleich
umstellt; Fakten bleiben unverändert. Die Liste alt → neu steht in
msa/gym-abgleich.csv und ist entschieden – sie wird ausgeführt,
nicht neu bewertet.

## Regeln

- Python nur über %LocalAppData%\Programs\Python\Python312\
  python.exe; git über die git.exe von GitHub Desktop; PowerShell.
  git mit -c core.pager=cat, commit -m, nicht pushen.
- Nichts löschen. Keine Handedits an CSV; alles über das Skript.
- Gegenprobe vor und nach dem Lauf: Zeilenzahlen (basis 126,
  kontext 267, gym 248), Punktsumme je Katalog, Zahl der Typen
  vorher 293, nachher 264. Eine Abweichung ist ein Befund, kein
  Grund, das Skript oder die Liste anzupassen.
- Hefte werden nicht geöffnet (Kern § 9).

## Schritte

1. Referenz sichern: msa-bau.py mit leerem ZEILEN laufen lassen
   („Alle Prüfungen bestanden"), Zeilenzahlen und Punktsummen der
   drei Kataloge und die Typenzahl notieren.

2. Skript werkzeuge/typen-abgleich.py schreiben. Eingabe: eine
   Abgleichliste (alt;neu;thema_neu;art) und das Profil (msa).
   Für jede Zeile der Liste:
   a) In allen Katalogen des Profils (msa-katalog-basis.csv,
      -kontext.csv, -gym.csv) den Wert alt in typ und in jedem
      Glied von typ_neben durch neu ersetzen. Ist neu bereits
      ein Glied derselben typ_neben-Liste, Doppelung entfernen.
   b) Trägt eine Zeile nach dem Ersetzen in typ einen Typ, dessen
      Thema (Typenliste) nicht das Zeilenthema ist, Zeilenthema
      und leitidee auf die des Typs setzen (Kern § 6, Zeilenthema
      = Typthema).
   c) Typenliste: art „umbenennen" → Zeile mit typ alt bekommt
      typ neu, thema thema_neu (falls angegeben); art
      „zusammenziehen" → Zeile alt entfällt, neu muss vorhanden
      sein (in der Liste oder durch eine frühere Umbenennung
      derselben Liste); beispiel_id von neu bleibt.
   d) Ausgabe: Liste der geänderten Zeilen als id: alt → neu,
      dann die Zahl je Katalog.
   Das Skript ist idempotent (zweiter Lauf ändert nichts) und
   prüft vor dem Schreiben, dass jedes alt in der Typenliste
   vorkommt und jedes neu nach dem Lauf genau einmal.

3. Skript laufen lassen mit msa/gym-abgleich.csv. Ausgabe
   sichern (msa/gym-abgleich-log.md: Kopf mit Stand, dann die
   Liste id: alt → neu).

4. Thema umbenennen: „Sinussatz" → „Sinus- und Kosinussatz" in
   msa-typen.csv (Feld thema), allen msa-Katalogen (Feld thema),
   msa/msa.md § 6 (Themenliste) und in themen.csv (Zeile des
   msa-Themas; Kennung der Konkordanz beibehalten). Über das
   Skript (Option --thema alt neu) oder ein zweites kleines
   Skript, nicht von Hand.

5. Status: Alle Typen mit status „neu" auf „gültig" setzen
   (TYPEN_KORREKTUR ist dafür nicht gedacht; im Abgleichskript
   als Option --status-neu-gueltig). Grund: Die Gegenlese ist
   erfolgt.

6. werkzeuge/gym-vergleich.py ergänzen: Ein Typ zählt für eine
   Gruppe, wenn er dort als typ oder in typ_neben steht; die
   Ausgabe nennt je Typ beides getrennt („nur GYM" heißt: in
   OS/EBR/FOR weder Haupt- noch Nebentyp). Die Listen neu
   erzeugen (msa/gym-vergleich.md), ebenso msa-ertrag.csv über
   werkzeuge/ertrag.py.

7. Prüfungen: msa-bau.py Selbstprüfung „Alle Prüfungen
   bestanden"; Zeilenzahlen und Punktsummen wie in Schritt 1;
   Typenzahl 264; werkzeuge/themen-pruef.py Rückgabe 0; zweiter
   Lauf des Abgleichskripts ändert nichts.

8. Nachführen: msa/msa.md § 4 (Abgleichlauf 2026-09-24, ein
   Satz) und Änderungslog; msa/msa-pruefungen.md Änderungslog;
   README.md (typen-abgleich.py, gym-abgleich.csv,
   gym-abgleich-log.md je ein Satz); konzept.md Entscheidung 18
   um einen Satz (Abgleich erfolgt, Typenzahl). Commit
   „msa: Abgleichlauf GYM, 29 Typen zusammengezogen, 32
   umbenannt, Thema Sinus- und Kosinussatz".

9. Auftrag nach archiv/ verschieben (git mv), Commit „archiv:
   auftrag-gym-abgleich". gym-abgleich.csv bleibt in msa/.

## Bericht

Erste Zeile das Modell. Dann: Zahlen vorher/nachher je Katalog
(Zeilen, Punkte, Typen); Zahl der geänderten Zeilen je Katalog;
Zeilen, deren Thema durch Schritt 2 b wechselte, als Liste
id: alt → neu; die neuen Vergleichszahlen (nur GYM / nur
OS-EBR-FOR / beide, jeweils Haupt und Haupt+Neben); Befunde der
Gegenproben; eigene Entscheidungen. Letzte Zeile: „Push origin
drücken".
