# Normalisierungs-Log – Phase 2

Datum: 2026-04-02
Zweck: Nachvollziehbare Dokumentation rein formaler Vereinheitlichungen ohne inhaltliche Änderung.

## Geltungsbereich

- `analyse_stellungnahmen_solarpark/tabellen/gesamtuebersicht.md`
- `analyse_stellungnahmen_solarpark/tabellen/gesamtuebersicht.csv`
- `analyse_stellungnahmen_solarpark/cache/phase2/phase2_summary.md`

## Durchgeführte Normalisierungen

### 1) Bewertungsschreibweise vereinheitlicht

- Feld: `Bewertung`
- Alt: `Teilweise beruecksichtigt`
- Neu: `Teilweise berücksichtigt`
- Änderungstyp: Orthografie/Encoding (Umlaut)
- Inhaltliche Wirkung: Keine

### 2) Nummernformat vereinheitlicht

- Feld: `Nr.`
- Alt: `021`–`030`
- Neu: `21`–`30`
- Änderungstyp: Formatierung (führende Null entfernt)
- Inhaltliche Wirkung: Keine

### 3) Summary-Konsistenz aktualisiert

- Datei: `phase2_summary.md`
- Alt: getrennte Zählung nach zwei Schreibweisen (`beruecksichtigt` vs `berücksichtigt`)
- Neu: einheitliche Zählung `Teilweise berücksichtigt: 30`
- Änderungstyp: Konsolidierung nach Normalisierung
- Inhaltliche Wirkung: Keine

## Nicht verändert

- Originalquellen (`stellungnahmen/*.pdf`, `pu/*.pdf`)
- Quellnahe Roh-/Cache-Extrakte aus Phase 1
- Inhaltliche Bewertungen/Empfehlungen (nur formale Schreib- und Formatvereinheitlichung)

## Prüfhilfe

Zur Verifikation kann in den Gesamttabellen nach Altformen gesucht werden:

- `beruecksichtigt`
- `021`, `022`, ..., `030` (im Feld `Nr.`)

Im normalisierten Zustand sollten diese Altformen in den finalen Gesamttabellen nicht mehr vorkommen.
