# Konkordanz fremder Originalaufgaben – Hamburg und Schleswig-Holstein (ESA, MSA)

## Kopf

- Datum: 2026-09-27 (Web-Sitzung, Repo auf Commit e617aeb).
- Modell: Claude in Claude Code (Web-Sitzung); die Modellkennung steht nach der Vorgabe der Umgebung nicht im Repo, sondern im Chatbericht dieses Laufs.
- Auftrag: Fremdoriginale-Lauf hh-sh – freie amtliche ESA- und MSA-Prüfungen Mathematik aus Hamburg und Schleswig-Holstein, jüngste fünf Jahrgänge mit Lösungen, beschaffen, als Text unter `quellen/quelle-fremd-hh-sh-<sammlung>-<jahr>.txt` sichern und je Teilaufgabe einem Katalogeintrag und einer Sprosse zuordnen. Grundlage gelesen: `ziel.md`, `quellen/fremdsammlungen-fundliste.md`, `katalog/_fremdoriginale-belege.md`.
- **Ergebnis: nichts gesichert.** Die Netzrichtlinie der Sitzungsumgebung sperrt jeden Quellhost (Proxy-Antwort 403 auf CONNECT, WebFetch „EGRESS_BLOCKED“); die Sperre trifft auch `www.isb.bayern.de`, die Quelle des Vorlaufs, liegt also an der Umgebung und nicht an den Ländern.

| Kennzahl | Wert |
|---|---|
| gesicherte Dateien | 0 |
| Aufgaben (Teilaufgaben) | 0 |
| Konkordanzzeilen | 0 |
| „Decke für“ | 0 |
| „?“ | 0 |
| Dateiabrufe (Verbindungsversuche) | 14 von 40, keiner lieferte eine Datei |
| Websuchen | 5 von 8 |

Zuordnungen je Eintrag:

| Eintrag (`katalog/`) | Zuordnungen | davon „Decke für“ | davon „?“ |
|---|---|---|---|
| – (keine Zuordnung, nichts gesichert) | 0 | 0 | 0 |
| Summe | 0 | 0 | 0 |

### Entscheidungen, die der Auftrag offenließ

1. **Gesperrter Zugang ist „nicht gesichert“, kein Abbruch.** Die Konkordanz wird trotzdem angelegt und committet: Sie hält fest, was versucht wurde, welche Adressen die Suchen geliefert haben und was ein Nachlauf braucht. Keine Textdatei unter `quellen/` – ohne Abruf gibt es keinen Text; Aufgabentexte aus Suchausschnitten, Drittseiten (serlo.org, Verlagsmuster, Schulseiten) oder aus dem Gedächtnis sind keine amtliche Quelle und wurden nicht verwendet.
2. **Zählweise der Abrufe:** Jeder Verbindungsversuch zu einem Quellhost zählt als Abruf, auch ein gescheiterter und ein reiner Erreichbarkeitsversuch (Kopfanfrage). Zwei Probeanfragen an Entwicklerhosts (github.com, pypi.org), nur zur Unterscheidung „Host gesperrt“ gegen „Netz tot“, sind nicht gezählt.
3. **Suchen nach dem Sperrbefund nicht aufgebraucht.** Drei der fünf Suchen dienten nur noch dazu, die Adressen für den Nachlauf festzuhalten; drei Suchen sind übrig und wurden nicht verbraucht, weil sie nichts sichern konnten.
4. **Modellkennung** nicht im Repo (Vorgabe der Umgebung), sondern im Chat.
5. **`README.md` und `faellig.md` nicht nachgeführt**, weil der Auftrag nur diese Datei und die Quellentexte zum Schreiben freigibt. Nachzutragen: die neue Datei in `README.md` (Block `katalog/`, Anlass: Konkordanz der Fremdoriginale Hamburg/Schleswig-Holstein) und der Nachlauf (unten) als Posten in `faellig.md`.
6. **Ablage der Quellentexte:** Der Auftrag legt sie nach `quellen/`, also ins Repo. Der Vorlauf hat Fremdtexte bewusst nur lokal unter `hefte/fremd/` abgelegt (`.gitignore`, „das Urheberrecht liegt bei den Ländern“, `quellen/fremdsammlungen-fundliste.md`). Dieser Lauf hat nichts abgelegt, die Frage bleibt für den Nachlauf offen: Volltexte ganzer Prüfungshefte im Repo sind eine Veröffentlichung, sobald das Repo öffentlich ist; der Lizenzvermerk je Datei entscheidet, ob das trägt.

## Beschaffung

### Gesichert

keine

### Nicht gesichert

| Sammlung | Land, Herausgeber | Befund | Adressen (aus den Suchen, nicht abgerufen) | Abrufe |
|---|---|---|---|---|
| ESA Mathematik, zentrale schriftliche Prüfung – `hh-esa-<jahr>` | Hamburg, Behörde für Schule, Familie und Berufsbildung (BSFB), Institut für Bildungsmonitoring/Landesinstitut | nicht gesichert: Host gesperrt (403). Laut Suchtreffern veröffentlicht Hamburg „Hinweise und Beispiele“ und „Lösungen, Hinweise und Beispiele für zentrale Prüfungsaufgaben“ – ob die Originalprüfungen der Jahrgänge 2021–2025 frei stehen, ist nicht geprüft (Annahme: eher nicht, siehe MSA). | https://www.hamburg.de/resource/blob/133198/51edbfa5ee45a80b58026f6684d4be71/hinweise-und-beispiele-zu-den-zentralen-pruefungsaufgaben-im-fach-mathematik-data.pdf; https://www.hamburg.de/resource/blob/133272/f2091f792939adfc9e183a2ef20741e4/mathematik-loesungen-hinweise-und-beispiele-fuer-zentrale-pruefungsaufgaben-data.pdf; https://www.hamburg.de/resource/blob/133120/37596dff5af8a07d8b68b52bf399a612/regelungen-fuer-die-zentralen-schriftlichen-pruefungsaufgaben-esa-2024-data.pdf; Themenseite https://bildungsserver.hamburg.de/schulfaecher/mint/mathematik/mathematik-themen-sek-i/mathematik-abschlusspruefungen-sek-i | 2 (bildungsserver.hamburg.de, li.hamburg.de) |
| MSA Mathematik, zentrale schriftliche Prüfung – `hh-msa-<jahr>` | Hamburg, BSFB | nicht gesichert: Host gesperrt (403). Laut Suchtreffern: Handreichung „Hinweise und Beispiele“ (nach Titelzeile „überarbeitete Aufgaben aus früheren Prüfungen“), ein Lösungsheft „Lösungen zu den zentralen schriftlichen Prüfungsaufgaben“ als Pflichtexemplar auf dem Publikationsserver der SUB Hamburg (2024), Regelungshefte je Jahr; dazu eine FragDenStaat-Anfrage nach den MSA-Aufgaben 2023 – ein Hinweis (nicht geprüft), dass Hamburg die Originalaufgaben nicht frei veröffentlicht. Die Reform der ESA- und MSA-Prüfungen (Seite der BSFB) ist nicht gelesen. | https://www.hamburg.de/politik-und-verwaltung/behoerden/bsfb/themen/zentrale-pruefungen/msa-2026-935302; https://dokumente.hamburg.de/resource/blob/119936/41789503891c24cc54ccad34a503789b/msa-hinweise-und-beispiele-zu-den-zentralen-schriftlichen-pruefungsaufgaben-mathematik-data.pdf; https://www.hamburg.de/resource/blob/119990/ad0ed4c7a085a9ba05fd91624d587127/mathematik-loesungen-hinweise-und-beispiele-zu-zentralen-pruefungsaufgaben-msa-data.pdf; https://epub.sub.uni-hamburg.de/epub/volltexte/2024/164312/; https://fragdenstaat.de/en/request/mittlerer-schulabschluss-aufgaben-im-fach-mathematik-im-jahr-2023-in-hamburg/; https://www.hamburg.de/politik-und-verwaltung/behoerden/bsfb/reform-der-esa-und-msa-pruefungen-1063444 | 7 (Themenseite MSA 2026 per curl und per WebFetch, dokumente.hamburg.de zweimal, epub.sub.uni-hamburg.de zweimal – Titelseite und Wurzel –, edoc.sub.uni-hamburg.de) |
| ESA Mathematik, Zentrale Abschlussarbeit – `sh-esa-<jahr>` | Schleswig-Holstein, Ministerium für Allgemeine und Berufliche Bildung / IQSH (Portal Zentrale Abschlussarbeiten) | nicht gesichert: Host gesperrt (403). Laut Suchtreffern führt das Portal je Jahr die Abschlussarbeit in zwei Heften und eine Korrekturanweisung (Treffertitel „Zentrale Abschlussarbeit 2024 Mathematik Heft 2“), dazu Übungshefte; das IQSH-Fachportal hat eine Seite „Lernhilfen für den ESA“. | https://za.schleswig-holstein.de/?view=100&path=3+ESA%7C5+Abschlussarbeiten; https://za.schleswig-holstein.de/?dHash=eb40181b950f860d4bdad7f22324c6b0&path=3+ESA%7C5+Abschlussarbeiten&view=101; https://fachportal.lernnetz.de/sh/faecher/mathematik/materialien-und-links/vorbereitung-auf-esa-und-msa/lernhilfen-f%C3%BCr-den-ESA.html | 2 (fachportal.lernnetz.de, www.schleswig-holstein.de) |
| MSA Mathematik, Zentrale Abschlussarbeit – `sh-msa-<jahr>` | Schleswig-Holstein, wie ESA | nicht gesichert: Host gesperrt (403). Laut Suchtreffer stehen für 2025 „Schülerheft1“, „Schülerheft2“ und die Korrekturanweisung auf dem Portal. | https://za.schleswig-holstein.de/?view=100&path=2+MSA%7C5+Abschlussarbeiten; https://za.schleswig-holstein.de/?view=2&path=2+MSA | 1 |

Weitere gezählte Abrufe: de.serlo.org (1, Erreichbarkeit; Drittseite, wäre ohnehin keine amtliche Quelle), www.isb.bayern.de (1, Gegenprobe gegen den Vorlauf: ebenfalls gesperrt). Summe 14 (2 + 7 + 2 + 1 + 2).

Websuchen (5): „Hamburg Abschlussprüfung MSA Mathematik Aufgaben Lösungen PDF li.hamburg.de“; „Schleswig-Holstein Zentrale Abschlussprüfung MSA Mathematik Aufgaben Lösungen PDF 2025“; „hamburg.de ESA MSA Mathematik zentrale Prüfungsaufgaben 2024 2025 Aufgaben Lösungen veröffentlicht Download“; „za.schleswig-holstein.de ESA Mathematik Abschlussarbeiten Schülerheft Lösungen“; „epub.sub.uni-hamburg.de Schriftliche Prüfung mittlerer Schulabschluss Mathematik zentrale schriftliche Prüfungsaufgaben“.

### Nachlauf

Der Lauf ist nachzuholen, wo die Hosts erreichbar sind – auf dem Rechner des Lehrers (wie der Vorlauf, `hefte/fremd/`) oder in einer Web-Umgebung, deren Netzfreigabe diese Hosts enthält: `za.schleswig-holstein.de`, `fachportal.lernnetz.de`, `www.hamburg.de`, `dokumente.hamburg.de`, `bildungsserver.hamburg.de`, `epub.sub.uni-hamburg.de`. Reihenfolge nach den Suchbefunden: Schleswig-Holstein zuerst (Abschlussarbeiten mit Korrekturanweisung sind dort offenbar frei), Hamburg danach mit der Vorfrage, ob die Originalprüfungen überhaupt frei stehen oder nur überarbeitete Beispiele (die wären als Decke schwächer: kein Prüfungsjahr, keine unveränderte Aufgabe).

## Konkordanz

Spalten: Kennung `<land>-<sammlung>-<jahr>-<nr><teil>` · Eintrag (`katalog/<name>.md`) · Einheit · Sprosse (wortgleich aus „Sprossen je Verfahrenstyp“ oder „keine Sprosse“) · Punkte · Hilfsmittel · Aufgabe (ein Satz) · Ergebnis · Decke.

| Kennung | Eintrag | Einheit | Sprosse | Punkte | Hilfsmittel | Aufgabe | Ergebnis | Decke |
|---|---|---|---|---|---|---|---|---|

Keine Zeile: keine Datei gesichert.

## Gegenprobe

Skript (aus dem Repo-Wurzelverzeichnis, `python3`); es liest die Konkordanztabelle oben und prüft: jede Kennung genau einmal, jeder Eintrag als Datei unter `katalog/`, jede Sprosse wortgleich im Eintrag (außer „keine Sprosse“; ein angehängtes „?“ mit Grund wird vor dem Vergleich abgetrennt, die Sprosse steht in „…“).

```python
import re, pathlib, collections
t = pathlib.Path("katalog/_fremd-konkordanz-hh-sh.md").read_text(encoding="utf-8")
zeilen = [z for z in t.split("## Konkordanz", 1)[1].split("## Gegenprobe", 1)[0].splitlines()
          if re.match(r"\| (hh|sh)-", z)]
fehler, n = [], collections.Counter()
for z in zeilen:
    f = [s.strip() for s in z.strip("|").split("|")]
    kennung, eintrag, sprosse = f[0], f[1].strip("`"), f[3]
    n[kennung] += 1
    datei = pathlib.Path("katalog") / eintrag
    if not datei.is_file():
        fehler.append(f"{kennung}: Eintrag {eintrag} fehlt")
    elif sprosse != "keine Sprosse":
        m = re.search(r"„(.+?)“", sprosse)
        s = m.group(1) if m else sprosse
        if s not in datei.read_text(encoding="utf-8"):
            fehler.append(f"{kennung}: Sprosse nicht wortgleich in {eintrag}")
fehler += [f"{k}: {v}-mal" for k, v in n.items() if v != 1]
print(f"{len(zeilen)} Zeilen, {len(n)} Kennungen, {len(fehler)} Fehler")
print("\n".join(fehler))
```

Ergebnis am 2026-09-27: „0 Zeilen, 0 Kennungen, 0 Fehler“ – die Gegenprobe ist leer bestanden, weil es nichts zu prüfen gibt.
