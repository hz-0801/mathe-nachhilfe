# Auftrag: ziel.md anlegen, konzept.md § 1 darauf verweisen

Ausgangslage: Das Ziel des Blattbaus stand in konzept.md § 1 nur
für die P10. Es liegt jetzt als eigene Datei ziel.md in der Wurzel
(wortgleich mitgeliefert). konzept.md § 1 wird zum Verweis.

Schritte:
1. ziel.md liegt in der Wurzel (angelegt). Prüfen: beginnt mit
   „# Ziel – Blätter aus Prüfungen und Lehrplan".
2. In konzept.md den Block von der Zeile „## 1 Ziel" bis zur Zeile
   vor „## 2 Bausteine" ersetzen durch genau diese vier Zeilen
   (plus Leerzeile danach):
   ## 1 Ziel

   Das Ziel des Blattbaus steht in ziel.md: beide Blattsorten,
   die Leiter als Bauprinzip, gemeinsame Regeln, Offenes. Die
   frühere Fassung dieses Abschnitts (P10, 19.09.2026) ist durch
   sie ersetzt.
3. Zeile 2 von konzept.md: „Stand 19.09.2026" → „Stand 22.09.2026".
4. In konzept.md § 10 Änderungen als erste Zeile einfügen:
   - 2026-09-22: § 1 Ziel nach ziel.md ausgelagert und neu
     geschrieben (Chat verbessereBlätter 22.09.2026): beide
     Blattsorten, Leiter, gemeinsame Regeln, Kennzeichnung.
     blatt-konzept.md widerspricht ziel.md in § 2, § 5, § 6 und
     ist nachzuziehen (Befund § 3 in befund-inkonsistenzen).
5. In README.md, Abschnitt „Wo fange ich an", direkt nach der
   Zeile zu uebergabe.md eine Zeile einfügen:
   - `ziel.md` – das Ziel des Blattbaus: beide Blattsorten, Leiter, gemeinsame Regeln, Offenes. Ein neuer Chat liest sie nach uebergabe.md.
6. auftrag-ziel.md nach archiv/auftrag-ziel-2026-09-22.md
   verschieben.
7. Commit „ziel.md angelegt, konzept.md § 1 verweist".

Prüfungen: ziel.md vorhanden, LF, kein BOM; konzept.md enthält
genau einmal „## 1 Ziel" und „## 2 Bausteine", dazwischen die
vier Zeilen aus Schritt 2; § 2 bis § 9 byteidentisch mit HEAD;
README.md um genau eine Zeile länger; git status nach Commit
sauber; python werkzeuge/themen-pruef.py bestanden.

Bericht: erste Zeile das Modell, dann je Schritt ein Satz,
Prüfergebnisse, Abweichungen und Annahmen. Letzte Zeile: „Push
origin drücken".

Regeln: nichts löschen, keine andere Datei anfassen, kein
Katalogeintrag, kein Prüfskript.
