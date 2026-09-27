# Konkordanz fremder Prüfungsaufgaben – Niedersachsen und Baden-Württemberg

## Kopf

- Datum: 2026-09-27, Web-Sitzung (Claude Code, Cloud-Container), Katalog auf Commit e617aeb.
- Modell: in Repo-Dateien nicht geführt (Vorgabe der Umgebung); steht im Chatbericht des Laufs.
- Dateien gesichert: 0. Aufgaben: 0. Zuordnungen: 0. „Decke für“: 0. „?“: 0.
- Abrufe: 0 von 40 erfolgreich (2 Datei-/Seitenversuche per WebFetch und 7 Verbindungsprüfungen per curl, alle von der Netzsperre abgewiesen). Websuchen: 4 von 8.

Ergebnis: Kein Heft gesichert. Die Netzwerkrichtlinie der Cloud-Umgebung dieses Laufs weist jede Verbindung zu den Quellservern ab (curl: „CONNECT tunnel failed, response 403“; WebFetch: „EGRESS_BLOCKED … blocked by the network egress proxy“). Betroffen: `www.nibis.de`, `cuvo.nibis.de`, `aba-aufgaben.nibis.de`, `bildungsportal-niedersachsen.de`, `www.schule-bw.de`; zur Gegenprobe ebenso `www.isb.bayern.de` und `de.serlo.org` – die Sperre gilt allgemein, nicht einzelnen Ländern. Nur die Websuche lief; ihre Treffer stehen unten als Adressen für den nächsten Lauf.

### Zuordnungen je Eintrag

| Eintrag (katalog/) | Zuordnungen | davon „Decke für“ | davon „?“ |
|---|---|---|---|
| – | 0 | 0 | 0 |
| Summe | 0 | 0 | 0 |

### Entscheidungen, die der Auftrag offenließ

1. Netzsperre statt Zählgrenze: Der Auftrag regelt „nicht gesichert“ nur für die Zählgrenze. Angewandt auf die Sperre: jede Sammlung steht unten als „nicht gesichert“ mit Grund; kein Ersatz aus Drittquellen (Serlo, Verlagsleseproben, Schul-Websites), weil der Auftrag amtliche Quellen der Länder verlangt und Drittquellen ebenso gesperrt waren.
2. Commit trotz leerem Ergebnis: Die Datei hält fest, was gesucht, was gefunden und was gesperrt war, damit der nächste Lauf nicht von vorn sucht. Der nächste Lauf überschreibt sie.
3. Kein Abruf über Umwege: Die Sperre ist eine Einstellung der Umgebung, kein Fehler; sie wurde nicht umgangen.
4. Zählweise: Websuchen gezählt (4). Die Verbindungsprüfungen per curl sind nicht als Dateiabrufe gezählt, weil keine Datei ankam; die beiden WebFetch-Versuche sind gezählt.
5. Offener Widerspruch für den nächsten Lauf (nicht entschieden, weil hier nichts zu sichern war): `quellen/fremdsammlungen-fundliste.md` legt die Texte fremder Hefte bewusst nur lokal unter `hefte/fremd/` ab („das Urheberrecht liegt bei den Ländern“); dieser Auftrag verlangt sie im Repo unter `quellen/quelle-fremd-ni-bw-*.txt`. Wer die Texte ins Repo legt, sollte vorher wissen, ob das Repo öffentlich ist.

### Gegenprobe

Skript (im Repo-Wurzelverzeichnis ausführen; hier nicht als Datei abgelegt, weil der Auftrag nur diese Datei zulässt):

```python
import re, pathlib, collections
t = pathlib.Path("katalog/_fremd-konkordanz-ni-bw.md").read_text(encoding="utf-8")
rows = [r for r in t.splitlines() if re.match(r"\| (ni|bw)-", r)]
ids = [r.split("|")[1].strip() for r in rows]
dup = [k for k, n in collections.Counter(ids).items() if n > 1]
bad = []
for r in rows:
    c = [x.strip() for x in r.split("|")[1:-1]]
    eintrag, sprosse = c[1], c[3]
    p = pathlib.Path("katalog") / eintrag
    if not p.exists():
        bad.append((c[0], "Eintrag fehlt", eintrag)); continue
    if sprosse != "keine Sprosse" and sprosse.rstrip(" ?") not in p.read_text(encoding="utf-8"):
        bad.append((c[0], "Sprosse nicht wortgleich", sprosse))
print(len(ids), "Kennungen;", "doppelt:", dup or "keine;", "Fehler:", bad or "keine")
```

Lauf 2026-09-27: `0 Kennungen; doppelt: keine; Fehler: keine` – trivial bestanden, weil keine Zeile vorliegt.

## Sammlungen

| Sammlung | Land, Herausgeber | Stand | Grund | Adresse (aus der Websuche, nicht aufgerufen) |
|---|---|---|---|---|
| Abschlussarbeit Mathematik Realschule (Kl. 10) – `ni-rs` | Niedersachsen, Kultusministerium / NLQ | nicht gesichert | Netzsperre der Umgebung. Laut Suchtreffer führen die Jahresseiten des Bildungsportals die Arbeiten (2024: „Realschule 10 … Mathematik“, „Mathematik-Formelsammlung“); Aufbau Hauptteil 1 ohne Hilfsmittel, Hauptteil 2 und Wahlteil mit Hilfsmitteln. Ob Aufgaben und Lösungen dort frei liegen, ist ungeprüft. | https://bildungsportal-niedersachsen.de/allgemeinbildung/zentrale-arbeiten/abschlusspruefungen/2025 (ebenso …/2024, …/2023); https://www.nibis.de/abschlusspruefungen_1590 |
| Abschlussarbeit Mathematik Hauptschule (Kl. 9/10) – `ni-hs` | Niedersachsen, Kultusministerium / NLQ | nicht gesichert | wie `ni-rs`. Die Aufgaben früherer Jahre stellt das Land laut Hinweisschrift unter aba-aufgaben.nibis.de „zur Vorbereitung“ bereit; ob dort eine Schulanmeldung nötig ist, ist ungeprüft (Annahme: ja, weil die Plattform auch der Aufgabenübermittlung an Schulen dient). | https://aba-aufgaben.nibis.de; Hinweise zur Abschlussprüfung Mathematik: https://bildungsportal-niedersachsen.de/index.php?eID=dumpFile&t=f&f=14328&token=c714eb51232ae70a35f0e5c9439d866987337180 |
| Realschulabschlussprüfung Mathematik – `bw-rsa` | Baden-Württemberg, Kultusministerium / ZSL | nicht gesichert | Netzsperre der Umgebung. Laut Suchtreffern bietet der Landesbildungsserver zur Prüfung nur Vorbereitungsmaterial (Lernvideos, Checklisten, „Problem des Monats“ mit Lösungen), die Originalprüfungen erscheinen bei Verlagen (Stark, Freiburger Verlag, abschluss-bw.de, pruefungshefte.de). Vermutlich nicht frei – ungeprüft. | https://www.schule-bw.de/faecher-und-schularten/mathematisch-naturwissenschaftliche-faecher/mathematik/bildungsplan_pruefungen-und-wettbewerbe/abschluss_rs/mathe_rs_pruefung |
| Hauptschulabschlussprüfung Mathematik – `bw-hsa` | Baden-Württemberg, Kultusministerium / ZSL | nicht gesichert | wie `bw-rsa`; Seite „Vorbereitung auf die Hauptschulabschlussprüfung – digital“, Originale laut Treffern bei Verlagen. Vermutlich nicht frei – ungeprüft. | https://www.schule-bw.de/faecher-und-schularten/mathematisch-naturwissenschaftliche-faecher/mathematik/bildungsplan_pruefungen-und-wettbewerbe/mathe_hs_pruefung |

Websuchen: „nibis Abschlussarbeiten Mathematik Realschule Aufgaben Lösungen PDF 2024“; „schule-bw.de Realschulabschlussprüfung Mathematik Aufgaben Lösungen PDF“; „aba-aufgaben.nibis.de Abschlussarbeiten Mathematik Hauptschule Realschule frei zugänglich Anmeldung“; „Hauptschulabschlussprüfung Mathematik Baden-Württemberg Aufgaben Lösungen Landesbildungsserver frei PDF“.

Für den nächsten Lauf: In der Umgebung die Domains `nibis.de` (mit Subdomains), `bildungsportal-niedersachsen.de` und `schule-bw.de` freigeben oder den Lauf lokal ausführen. Baden-Württemberg lohnt nach den Suchtreffern wenig; Niedersachsen (Bildungsportal-Jahresseiten 2021–2025) ist die aussichtsreichere Hälfte.

## Konkordanz

Kennung · Eintrag · Einheit · Sprosse · Punkte · Hilfsmittel · Aufgabe · Ergebnis · Decke

(keine Zeilen – keine Datei gesichert)
