# Auftrag: Lösungen und Hinweise Kurvendiskussion FHR

Stand 18.10.2026 (Chat FHR 2; plan.md § 7 D, § 10 18.10. a, b).

## Ziel

Je FHR-Heft eine Datendatei `fhr/loesung/daten/<jahr>-<heft>.txt`
mit allen Teilaufgaben der Art Kurvendiskussion, Stufe kern
(`zuordnung-kurvendiskussion.csv`, profil fhr). Daraus setzt
`setzer.py` zwei PDFs: `loesung-<jahr>-<heft>.pdf` und
`hinweise-<jahr>-<heft>.pdf`. Rand-Teilaufgaben (*) bleiben weg.

Muster: `daten/2026-C-1.txt` mit `pilot-2026-C-1.pdf` und
`hinweise-2026-C-1.pdf`. Erst lesen, dann schreiben. Die Syntax
steht im Kopf von `setzer.py`.

## Quelle

- Heft mit curl: Dateiname aus `fhr/fhr-pruefungen.md`, Verzeichnis
  aus `fhr/fhr-quellen.md`. Text mit `pdftotext -layout`; jede Seite
  mit Abbildung rendern und ansehen.
- Der amtliche Erwartungshorizont hinten im Heft prüft die
  Ergebnisse. Er ist nicht fehlerfrei: 2026 C 1f nennt f(−0,93) ≈
  −75,83, richtig ist das nur für die ungerundete Stelle.

## Form (Warum – Beispiel – Grenze)

- Frage mit „?“. Warum: Der Schüler sieht, was jede Zeile
  beantwortet. Beispiel: „Welche Abbildung zeigt G_f?“, darunter
  Unterfragen. Grenze: Die Hauptfrage nimmt die Aufgabe auf; eine
  Unterfrage nur, wo ein eigener Schritt beginnt.
- Ansatz in allgemeiner Form aus `ansaetze-kurvendiskussion.tex`.
  Warum: Gleiche Fragen sehen gleich aus; das Hinweisblatt besteht
  nur aus Fragen und Ansätzen. Beispiel: „$f''(x_W)=0$ und
  $f'''(x_W)\neq0$“. Grenze: Die Sammlung leitet, sie zwingt nicht;
  passt ein Ansatz nicht, den passenden nehmen (Grenze → Ersatz in
  der Sammlung). Eine zweite Ansatzzeile nur, wo der Weg die Hürde
  ist (Nullstelle raten, dann dividieren).
- Zeilen „Rechnung ⇒ Schluss“. Warum: Der Lehrer prüft je Zeile in
  Sekunden. Beispiel: eine Stelle je Zeile, „f″(…) … ; f(…) ⇒
  Tiefpunkt T(…)“. Grenze: nur Zwischenergebnisse, keine
  Rechenwege, keine Sätze; nichts doppelt (Verweis grau „aus e“);
  Ergebnisse fett; nur ⇒, nie ⇔.
- Gerundete Stellen. Warum: Wer mit dem gerundeten Wert nachrechnet,
  bekommt sonst etwas anderes. Beispiel: $f(x_{W2})\approx-75{,}83$
  statt $f(-0{,}93)$. Grenze: Wo Rundung nichts ändert, die Zahl.
- Logik in Schlussrichtung. Warum: 2026 C 1b (I) stand umgekehrt
  („nur ungerade ⇒ punktsymmetrisch“ zum Nachweis von „nicht“).
  Beispiel: „ein gerader Exponent ⇒ nicht punktsymmetrisch“.
- Skizze am Anfang (@-Zeile). Warum: Der Schüler sieht, ob die
  Ergebnisse zusammenpassen; der Lehrer prüft die Aufgabe auf einen
  Blick. Beispiel: Fenster so, dass alle Punkte sichtbar sind, Punkte
  mit Namen. Grenze: „| aufgabe“ nur, wenn das Heft selbst einen
  Graphen von f zeigt (dann steht er auch auf dem Hinweisblatt).
- Teilaufgaben aus Aufgabe 2 (Sachaufgaben) in dieselbe Datei, mit
  eigenem Kopf „# 2 <Titel> | FHR <jahr> <heft> · Lösung“ und
  f-Zeile; Buchstaben wie im Heft.

## Prüfen

- Jede Zahl mit sympy nachrechnen (Skript im Scratchpad, nicht ins
  Repo); Abweichung vom Erwartungshorizont im Bericht nennen.
- `python setzer.py daten/X.txt <ziel>.tex` und mit `--hinweise`;
  xelatex ohne Fehler; jede Seite als PNG ansehen (nichts läuft aus
  dem Rand, keine Zeile bricht mitten im Schluss um).

## Grenzen

- Nur `fhr/loesung/daten/`, `loesung-*.pdf`, `hinweise-*.pdf`.
  setzer.py, Sammlung, plan.md nicht ändern; fehlt dem Setzer
  etwas, im Bericht.
- Eigener Klon; je Heft ein Commit („Lösung Kurvendiskussion FHR
  <jahr> <heft> (Auftrag Kurvendiskussion)“), vorher
  `git pull --rebase`.

## Bericht (je Heft eine Zeile, höchstens 15 Zeilen)

Teilaufgaben gesetzt / ausgelassen mit Grund; Abweichungen zum
Erwartungshorizont; wo ein Ansatz der Sammlung nicht passte und
welcher Ersatz; was dem Setzer fehlte; Wanduhr je Heft.
