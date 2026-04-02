# AGENTS.md

Arbeitsleitfaden für alle weiteren Bearbeitungsschritte im Projekt `planunterlagen`.

## 1) Projektziel

Abgleich von Bürger-Stellungnahmen zum Solarpark mit den neuen Planunterlagen:
- **Detailanalyse je Bürger** (eine Datei pro Bürger)
- **Konsolidierte Gesamttabelle** für Review/Entscheidung

## 2) Source of Truth (SoT)

### Primärquellen
- `stellungnahmen/Stellungnahmen_Bürger_Zusammen.pdf`
- `pu/*.pdf`

### Persistierte Arbeitsgrundlage
- `analyse_stellungnahmen_solarpark/cache/buerger_rohtext.md`
- `analyse_stellungnahmen_solarpark/cache/buerger_segmentierung.csv`
- `analyse_stellungnahmen_solarpark/cache/planunterlagen_raw/*.txt`
- `analyse_stellungnahmen_solarpark/cache/planunterlagen_index.md`
- `analyse_stellungnahmen_solarpark/cache/planunterlagen_themen.csv`

### Finale Ergebnisse
- `analyse_stellungnahmen_solarpark/detail/001_buerger.md` ... `030_buerger.md`
- `analyse_stellungnahmen_solarpark/tabellen/gesamtuebersicht.md`
- `analyse_stellungnahmen_solarpark/tabellen/gesamtuebersicht.csv`

## 3) Bewertungs- und Tabellenstandard

Erlaubte Werte für **Bewertung** (nur diese drei):
- `Vollständig berücksichtigt`
- `Teilweise berücksichtigt`
- `Nicht erkennbar berücksichtigt`

Pflichtspalten (exakte Reihenfolge):
1. `Nr.`
2. `Ursprung Stellungnahme`
3. `Im Entwurf berücksichtigt`
4. `Bewertung`
5. `Offener Punkt`
6. `Empfehlung`

Nummerierung in Mastertabellen: `1` bis `30` (ohne führende Null).

## 4) Arbeitsprinzipien

1. **Quellenbasiert arbeiten**
   - Keine erfundenen Fakten.
   - Bei Unsicherheit explizit markieren.

2. **Detail ↔ Tabelle synchron halten**
   - Änderungen zuerst in Detaildatei, dann in Mastertabelle nachziehen.

3. **Nachvollziehbarkeit sichern**
   - Größere Änderungen immer im Cache protokollieren (Batch-/Phase-Log).

4. **Normalisierung beachten**
   - Schreibweise und Format konsistent halten.
   - Referenz: `analyse_stellungnahmen_solarpark/cache/phase2/normalisierung_log.md`

## 5) Empfohlener Workflow für weitere Iterationen

1. Betroffene Bürger identifizieren
2. Detaildateien aktualisieren (mit Fundstellenbezug)
3. Batch- oder Änderungsprotokoll schreiben (`cache/phaseX/...`)
4. Mastertabellen neu konsolidieren
5. Vollständigkeit prüfen (30/30 Zeilen, gültige Bewertungsskala)

## 6) Qualitätssicherung (Kurzcheck)

- [ ] 30 Detaildateien vorhanden
- [ ] 30 Zeilen in `gesamtuebersicht.md` und `gesamtuebersicht.csv`
- [ ] Nur zulässige Bewertungswerte verwendet
- [ ] Keine uneinheitlichen Altformen (z. B. `beruecksichtigt`) in finalen Mastertabellen
- [ ] Offene Punkte/Empfehlungen inhaltlich konsistent mit Detaildateien

## 7) Offene nächste Aufgabe

Erstellung einer **Executive Summary** (1–2 Seiten):
- Hauptkonflikte
- priorisierte Empfehlungen
- Quick Wins vs. vertiefte Nacharbeit

## Active Technologies
- Python 3.11 (site build), Markdown + MkDocs 1.6+, Material for MkDocs 9+, GitHub Actions Pages actions (`configure-pages`, `upload-pages-artifact`, `deploy-pages`) (001-markdown-site-pages)
- N/A (static files in repository and generated static HTML artifacts) (001-markdown-site-pages)

## Recent Changes
- 001-markdown-site-pages: Added Python 3.11 (site build), Markdown + MkDocs 1.6+, Material for MkDocs 9+, GitHub Actions Pages actions (`configure-pages`, `upload-pages-artifact`, `deploy-pages`)
