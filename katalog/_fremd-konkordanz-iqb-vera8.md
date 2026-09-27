# Fremd-Konkordanz IQB VERA-8

Stand 2026-09-27 · Fremdoriginale-Lauf (iqb-vera8), Web-Sitzung, Repo auf Commit e617aeb.
Modell: nicht eingetragen – die Sitzungsumgebung untersagt Modellkennungen in Repo-Dateien; genannt im Chat-Bericht des Laufs.

Quelle des Laufs: IQB (Berlin), VERA-8 Mathematik, https://www.iqb.hu-berlin.de/de/schule/aufgaben/seki/vera-8-mathematik/ – Didaktische Handreichungen 2022–2026 und, wenn frei abrufbar, die Archive „Alle Aufgaben der Leitidee 1–5“ (Aufgabenpool 2011–2017).

**Ergebnis: nichts gesichert, nichts zugeordnet.** Die Netzwerkrichtlinie der Web-Umgebung sperrt die IQB-Adresse (und den gefundenen Spiegel); keine Datei war abrufbar. Die Konkordanz unten ist leer; sie ist mit Beschaffung neu zu erzeugen (siehe „Nächster Lauf“).

## Zahlen

| Größe | Wert |
|---|---|
| Dateien gesichert (`quellen/quelle-fremd-iqb-vera8-*.txt`) | 0 |
| Aufgaben (Teilaufgaben) | 0 |
| Zeilen mit „Decke für“ | 0 |
| Zeilen mit „?“ | 0 |
| Dateiabrufe (Grenze 40) | 4, alle gescheitert |
| Websuchen (Grenze 8) | 1 |

Zuordnungen je Eintrag:

| Eintrag | Zeilen | davon „Decke für“ | davon „?“ |
|---|---|---|---|
| – (keine Zuordnung) | 0 | 0 | 0 |

## Nicht gesichert

| Datei | Adresse | Grund |
|---|---|---|
| Didaktische Handreichungen VERA-8 Mathematik 2022, 2023, 2024, 2025, 2026 | https://www.iqb.hu-berlin.de/de/schule/aufgaben/seki/vera-8-mathematik/ | Übersichtsseite nicht erreichbar: `curl` bricht mit „CONNECT tunnel failed, response 403“ ab (Egress-Proxy der Umgebung: connect_rejected), WebFetch meldet „EGRESS_BLOCKED … www.iqb.hu-berlin.de“. Ohne die Seite keine Dateiadressen. |
| „Alle Aufgaben der Leitidee 1–5“ (Aufgabenpool 2011–2017, laut Fundliste Word-Archive) | wie oben | wie oben; ob frei abrufbar, ist ungeprüft. |
| Didaktische Handreichung 2025 (Leitidee Funktionaler Zusammenhang), Spiegel bei QUA-LiS NRW | https://www.qua-lis.nrw.de/system/files/media/document/file/didaktische_handreichung_funktionaler_zusammenhang.PDF | Ersatzweg über das Landesinstitut NRW (Websuche); ebenfalls gesperrt: `curl` 403, WebFetch „EGRESS_BLOCKED … www.qua-lis.nrw.de“. |

Abrufe: (1) `curl` IQB-Seite, (2) WebFetch IQB-Seite, (3) `curl` QUA-LiS-PDF 2025, (4) WebFetch QUA-LiS-PDF 2025. Websuche: „VERA-8 Mathematik Didaktische Handreichung 2025 PDF“. Weitere Versuche unterlassen: Zwei Behördenadressen, je über beide Wege gesperrt, zeigen eine Sperre der Umgebung, keine Störung einer Seite.

Weitere Adressen aus der Websuche, nicht abgerufen (für den nächsten Lauf; Spiegel desselben IQB-Materials beim Landesinstitut NRW, Gleichheit mit den IQB-Dateien ungeprüft):
- 2024 (Leitidee Zahl): https://www.qua-lis.nrw.de/system/files/media/document/file/didaktische_handreichung_zahl_sekundarstufe.pdf
- 2023 (Leitidee Messen): https://www.qua-lis.nrw.de/system/files/media/document/file/didaktische_handreichung_messen.pdf

## Entscheidungen, die der Auftrag offenließ

1. **Ersatzwege.** Nach der Sperre von `curl` wurde WebFetch versucht, danach ein Spiegel beim Landesinstitut NRW (amtlich, dasselbe IQB-Material). Private Spiegel (docplayer.org u. ä.) nicht: keine amtliche Quelle, Gleichheit mit dem Original nicht prüfbar.
2. **Nichts aus zweiter Hand.** `katalog/_fremdoriginale-belege.md` nennt vier VERA-8-Aufgaben nur mit Titel und als „nicht gezählt“ (2023 „Krawatte“, 2024 „Vorteilhaft Rechnen“, 2025 „Tropfender Wasserhahn“, 2026 „Trapez“); Punkte, Ergebniszahl und Teilaufgaben fehlen dort. Daraus keine Zeilen – ohne Quelltext wäre jede Angabe geraten.
3. **Zählweise.** Jeder Abrufversuch zählt als Dateiabruf, auch ein gescheiterter; die Übersichtsseite zählt mit.
4. **Kennung** (für den nächsten Lauf festgelegt): `<land>` ist `iqb` (länderübergreifend, wie `iqb-vera8-<jahr>-kl8` in der Fundliste), `<sammlung>` `vera8`, `<nr>` zweistellig in Heftreihenfolge der Beispielaufgaben, `<teil>` Kleinbuchstabe der Teilaufgabe (Teilaufgabe 1, 2, 3 → a, b, c), z. B. `iqb-vera8-2025-03b`; Pool 2011–2017 mit der Poolkennung als `<nr>`.
5. **„Decke für“** (für den nächsten Lauf festgelegt): nur wenn die zugeordnete Sprosse selbst „kein P10-Original“ trägt, also die Prüfungshöhe einer Kette ohne P10-Original ist (22 solche Sprossen, `katalog/_niveaustufen-belege.md`).
6. **Landkarte.** Der Auftrag erlaubt nur diese Datei und `quellen/quelle-fremd-iqb-vera8-*.txt`; der nach CLAUDE.md § 3 fällige Eintrag in `README.md` unterbleibt deshalb und ist nachzuholen.
7. **Urheberrecht.** Die Fundliste legt Textfassungen fremder Tests bewusst nur lokal ab (`hefte/fremd/`, „das Urheberrecht liegt bei den Ländern“); der Auftrag verlangt sie unter `quellen/` im öffentlichen Repo. Nicht entschieden, weil nichts gesichert wurde – vor dem nächsten Lauf zu klären.

## Nächster Lauf

Voraussetzung: Netzwerkzugriff auf www.iqb.hu-berlin.de (Umgebungseinstellung „Network access“, Host in die erlaubten Domains) oder Lauf auf dem Rechner des Lehrers, wo die fünf Handreichungen bereits unter `hefte/fremd/iqb-vera8-<jahr>-kl8.pdf` liegen (Fundliste). Dann Schritte 1–3 des Auftrags unverändert.

## Gegenprobe

Skript (Aufruf aus der Repo-Wurzel, Python 3): prüft, dass jede Kennung genau einmal steht, jeder Eintrag als Datei unter `katalog/` existiert und jede Sprosse wortgleich im Eintrag steht (ohne führendes/abschließendes Anführungszeichen und ohne angehängtes „?“). Ergebnis dieses Laufs: `Zeilen: 0, Kennungen: 0, Fehler: 0` / „Gegenprobe bestanden.“ (leer, also ohne Aussagekraft).

```python
# Gegenprobe der Konkordanz; Aufruf aus der Repo-Wurzel:
#   python gegenprobe.py katalog/_fremd-konkordanz-iqb-vera8.md
import os, re, sys
pfad = sys.argv[1]
zeilen = open(pfad, encoding="utf-8").read().rsplit("\n## Konkordanz", 1)[1].splitlines()
fehler, gesehen, n = [], {}, 0
for z in zeilen:
    if not z.startswith("| ") or z.startswith("| Kennung") or z.startswith("|---"):
        continue
    f = [s.strip() for s in z.strip("|").split("|")]
    kennung, eintrag, sprosse = f[0], f[1], f[3]
    n += 1
    gesehen[kennung] = gesehen.get(kennung, 0) + 1
    datei = os.path.join("katalog", eintrag.strip("`").replace("katalog/", ""))
    if not os.path.isfile(datei):
        fehler.append(f"{kennung}: Eintrag {datei} fehlt")
        continue
    s = sprosse.rstrip(" ?").strip("„“")
    if s != "keine Sprosse" and s not in open(datei, encoding="utf-8").read():
        fehler.append(f"{kennung}: Sprosse nicht wortgleich in {datei}")
fehler += [f"{k}: {v}-mal" for k, v in gesehen.items() if v != 1]
print(f"Zeilen: {n}, Kennungen: {len(gesehen)}, Fehler: {len(fehler)}")
print("\n".join(fehler) or "Gegenprobe bestanden.")
sys.exit(1 if fehler else 0)
```

## Konkordanz

| Kennung | Eintrag | Einheit | Sprosse | Punkte | Hilfsmittel | Aufgabe | Ergebnis | Decke für |
|---|---|---|---|---|---|---|---|---|
