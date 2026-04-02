# Task Context Bundle: Phase 2 – Bürgerweiser Abgleich

Session ID: 2026-04-02-stellungnahmen-phase2
Created: 2026-04-02
Status: in_progress

## Auftrag
Für jede Bürger-Stellungnahme den Abgleich mit den neuen Planunterlagen erstellen und in zwei Ebenen persistieren:
1) Detaildatei je Bürger in `analyse_stellungnahmen_solarpark/detail/`
2) Gesamttabelle in `analyse_stellungnahmen_solarpark/tabellen/`

## Kontextdateien (Standards)
- /home/rico/.config/opencode/context/core/standards/documentation.md
- /home/rico/.config/opencode/context/core/standards/code-analysis.md
- /home/rico/.config/opencode/context/core/workflows/task-delegation-basics.md
- /home/rico/.config/opencode/context/core/task-management/standards/task-schema.md

## Referenzdateien (Source)
- analyse_stellungnahmen_solarpark/cache/buerger_rohtext.md
- analyse_stellungnahmen_solarpark/cache/buerger_segmentierung.csv
- analyse_stellungnahmen_solarpark/cache/planunterlagen_index.md
- analyse_stellungnahmen_solarpark/cache/planunterlagen_themen.csv
- analyse_stellungnahmen_solarpark/cache/planunterlagen_raw/*.txt

## Bewertungs-Skala
- Vollständig berücksichtigt
- Teilweise berücksichtigt
- Nicht erkennbar berücksichtigt

## Ausgabeformat Detaildatei
Pfad: `analyse_stellungnahmen_solarpark/detail/{NNN}_buerger.md`

Abschnitte:
1. Nr. / Bürger
2. Ursprung Stellungnahme (Kurzfassung)
3. Im Entwurf berücksichtigt (mit Evidenz/Fundstellen)
4. Bewertung
5. Offener Punkt
6. Empfehlung
7. Unsicherheiten

## Tabellenstruktur (Pflichtspalten)
- Nr.
- Ursprung Stellungnahme
- Im Entwurf berücksichtigt
- Bewertung
- Offener Punkt
- Empfehlung

## Qualitätsregeln
- Nur quellenbasiert, keine erfundenen Fakten.
- Unsichere Zuordnungen explizit markieren.
- Knapp, präzise, vergleichbar zwischen Bürgern.
