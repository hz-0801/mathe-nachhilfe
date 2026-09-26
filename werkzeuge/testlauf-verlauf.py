#!/usr/bin/env python3
r"""testlauf-verlauf.py – Sitzungsprotokoll einer Blattsitzung auswerten (v0.1, 26.09.2026)

Auftrag: auftrag-testlauf.md (26.09.2026), Teil 2: „Zusätzlich zur Aufrufzahl aus protokoll.txt zählst
du die tatsächlichen Werkzeugaufrufe der Sitzung aus ihrer Ausgabe oder dem Sitzungsprotokoll (Spalte
„Aufrufe (Umgebung)“)“.

  python werkzeuge/testlauf-verlauf.py <verlauf.jsonl> <zielordner>

<verlauf.jsonl> ist das Sitzungsprotokoll des Sub-Agenten (Ersatzweg), wie Claude Code es unter
%USERPROFILE%\.claude\projects\<projekt>\<sitzung>\subagents\agent-<id>.jsonl ablegt (die
Ausgabedatei tasks\<id>.output bleibt leer). Schreibt in den Zielordner:
  sitzung.txt   alle Textblöcke der Sitzung in Reihenfolge; der letzte ist die Schlussnachricht (auch
                wenn sie als Aufruf „SubagentHandback“ übergeben wurde – der zählt als Werkzeugaufruf mit,
                wie in der Meldung der Laufzeitumgebung „tool_uses“)
  aufrufe.txt   je Werkzeugaufruf eine Zeile „n · Werkzeug · Kurzform der Eingabe“, am Ende die Zahl
                (Spalte „Aufrufe (Umgebung)“), erster und letzter Zeitstempel, Modell
Gezählt wird jeder Block „tool_use“ in einer Nachricht des Assistenten, einmal je Block-id (der
Verlauf kann eine Nachricht in mehreren Zeilen wiederholen).
"""

import json
import sys
from pathlib import Path


def kurz(eingabe):
    for k in ('description', 'command', 'file_path', 'pattern', 'path', 'url', 'prompt'):
        if k in eingabe:
            s = ' '.join(str(eingabe[k]).split())
            return s[:160] + ('…' if len(s) > 160 else '')
    return json.dumps(eingabe, ensure_ascii=False)[:160]


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    verlauf, ziel = Path(sys.argv[1]), Path(sys.argv[2])
    texte, aufrufe, gesehen, zeiten, modelle = [], [], set(), [], []
    for roh in verlauf.read_text(encoding='utf-8', errors='replace').split('\n'):
        roh = roh.strip()
        if not roh:
            continue
        try:
            ev = json.loads(roh)
        except json.JSONDecodeError:
            continue
        if ev.get('timestamp'):
            zeiten.append(ev['timestamp'])
        m = ev.get('message')
        if ev.get('type') != 'assistant' or not isinstance(m, dict):
            continue
        if m.get('model') and m['model'] not in modelle:
            modelle.append(m['model'])
        for teil in m.get('content') or []:
            if not isinstance(teil, dict):
                continue
            if teil.get('type') == 'text' and teil.get('text', '').strip():
                texte.append(teil['text'].strip())
            elif teil.get('type') == 'tool_use' and teil.get('id') not in gesehen:
                gesehen.add(teil.get('id'))
                if teil.get('name') == 'SubagentHandback':
                    # Schlussnachricht als Übergabeaufruf; zählt wie in der Meldung der Umgebung mit
                    texte.append(str((teil.get('input') or {}).get('message', '')).strip())
                aufrufe.append((teil.get('name'), kurz(teil.get('input') or {})))
    with open(ziel / 'sitzung.txt', 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n\n'.join(texte) + '\n')
    z = [f'{n} · {name} · {k}' for n, (name, k) in enumerate(aufrufe, 1)]
    z += ['', f'Werkzeugaufrufe (Umgebung): {len(aufrufe)}',
          f'Zeitstempel: {zeiten[0] if zeiten else "–"} bis {zeiten[-1] if zeiten else "–"}',
          f'Modell: {", ".join(modelle) or "–"}', f'Quelle: {verlauf.name}']
    with open(ziel / 'aufrufe.txt', 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(z) + '\n')
    print(f'Werkzeugaufrufe (Umgebung): {len(aufrufe)} · Textblöcke {len(texte)} · Modell {", ".join(modelle)}')


if __name__ == '__main__':
    main()
