# Auftrag: Prompts umbenennen

Die beiden Prompts bekommen neue Namen, die überall gelten – Projekte, Dateien, Text.
Du arbeitest im Clone von `mathe-nachhilfe`; das Repo `blattbau` liegt daneben unter
`../blattbau` (sonst abbrechen und melden). Beide werden geändert, je ein Commit.

| bisher | neu |
|---|---|
| `masterprompt.md` | `unterrichtsblatt.md` |
| `pruefungsprompt.md` | `pruefungsblatt.md` |
| Wort „Masterprompt" | „Unterrichtsblatt-Prompt" |
| Wort „Prüfungsprompt" | „Prüfungsblatt-Prompt" |

## Schritte in blattbau

1. `git status` sauber, sonst abbrechen.
2. `git mv masterprompt.md unterrichtsblatt.md`, `git mv pruefungsprompt.md pruefungsblatt.md`.
3. In `unterrichtsblatt.md`: Kopfzeile `# MASTERPROMPT v3.35 – …` wird
   `# UNTERRICHTSBLATT v3.35 – PROMPT FÜR ARBEITSBLÄTTER ZUM LAUFENDEN STOFF`.
   Nach der Versionszeile eine Zeile einfügen:
   `Umbenannt 19.09.2026, vorher masterprompt.md; Inhalt unverändert.`
   In `pruefungsblatt.md`: Kopfzeile `# PRÜFUNGSPROMPT v0.15 – …` wird
   `# PRÜFUNGSBLATT v0.15 – PROMPT FÜR ÜBUNGSBLÄTTER UND PROBEPRÜFUNGEN AUS DEM PRÜFUNGSKATALOG (PROFIL MSA)`,
   gleiche Zusatzzeile mit `pruefungsprompt.md`.
4. Textersetzung nach der Tabelle in: `unterrichtsblatt.md`, `pruefungsblatt.md`,
   `README.md`, `mathblatt.sty`. Groß-/Kleinschreibung beachten (`masterprompt.md` klein,
   „Masterprompt" groß). Auch „Master-Prompt", „Prüfungs-Prompt", „Prüfungsprompt" mit
   ü und mit ue.
5. `CHANGELOG.md`: nur den Kopf (Titel, erste Zeilen) anpassen und oben einen Eintrag
   `- 19.09.2026: masterprompt.md → unterrichtsblatt.md, pruefungsprompt.md → pruefungsblatt.md (Umbenennung, Inhalt unverändert)` einfügen.
   Die Versionseinträge darunter bleiben, wie sie sind – sie beschreiben Fassungen unter
   altem Namen.
6. `Bewertung_*.md` und `Testauswertung_*.md`: nicht anfassen, nicht umbenennen
   (eingefroren).
7. Commit: `Prompts umbenannt: unterrichtsblatt.md, pruefungsblatt.md`. Push versuchen.

## Schritte in mathe-nachhilfe

8. `git status` sauber, sonst abbrechen.
9. Textersetzung nach der Tabelle in allen `.md`-Dateien außer unter `archiv/`:
   Wurzel (`README.md`, `konzept.md`, `blatt-konzept.md`, `faellig.md`, `uebergabe.md`,
   `CLAUDE.md`, `katalog-prompt.md`), alle Profildateien, alle Dateien unter `katalog/`.
   Vorher `grep -rniE "masterprompt|pruefungsprompt|prüfungsprompt|master-prompt|prüfungs-prompt" --include=*.md . | grep -v archiv/ | wc -l`
   notieren; nachher muss der Zähler 0 sein, sonst die Reste einzeln melden.
10. In `README.md`, Abschnitt „Repo blattbau": die Dateiliste auf die neuen Namen.
11. Commit: `Prompt-Namen nachgezogen: unterrichtsblatt.md, pruefungsblatt.md`. Push versuchen.

## Bericht

Je Repo: Commit-Hash, Zahl der geänderten Dateien, Zahl der Ersetzungen, Reste (wenn
der Zähler nicht 0 ist). Am Ende „Push origin drücken – in beiden Repos", falls nötig.
Diese Auftragsdatei nach `archiv/` in mathe-nachhilfe.

## Regeln

- Nur Namen. Kein Satz im Inhalt eines Prompts oder Eintrags ändert sich außer durch
  die Ersetzung.
- `archiv/` in beiden Repos unangetastet.
- Wenn eine Ersetzung ein Wort trifft, das nicht den Prompt meint (etwa „Master" in
  anderem Sinn), die Stelle nicht ersetzen und melden.
