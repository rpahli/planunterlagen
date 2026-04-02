# Review-Fix-Log – Phase 4

Datum: 2026-04-02
Anlass: Kritisches Re-Review auf Basis von `REVIEW_PROMPT_KRITISCH.md` mit parallelem Subagent-Review und anschliessendem Fix-Batch.

## 1) Vorgehen

- Review-Kontext geladen (`code-review.md`, `task-delegation-basics.md`, `documentation.md`, `AGENTS.md`, `REVIEW_PROMPT_KRITISCH.md`)
- Paralleles Tiefenreview mit Subagents fuer:
  - Faelle `001-010`
  - Faelle `011-020`
  - Faelle `021-030`
  - globale Konsistenz `detail -> gesamtuebersicht.md -> gesamtuebersicht.csv`
  - `executive_summary.md` und `stakeholder_ausschuss_kurzfassung.md`
- Relevante Befunde anschliessend quellengebunden nachgeschaerft

## 2) Wichtige Befunde aus dem Review

### Fachlich nachgeschaerft
- **001**: Ursprung/Offener Punkt um Hitze- und Niederschlagswasser-Vorbehalte ergaenzt
- **002**: Naturschutzrechtliche vs. agrarwirtschaftliche Kompensation klarer getrennt
- **004**: Zu weite Ableitung von "beruecksichtigt" reduziert; offene Punkte praezisiert
- **007**: OCR-/Zuordnungsunsicherheit frueher und deutlicher kenntlich gemacht; Haftung/Sicherung expliziter als offen markiert
- **012**: offene Teilaspekte zu Kumulation, Grundwasser-, Schutzgebiets- und Artkonflikten deutlicher markiert
- **014**: Artenschutzformulierung verallgemeinert; spezifischer Wolf-Bezug nicht mehr als explizit belegt dargestellt
- **015**: Alternativstandorte in Ursprung, Evidenz und Empfehlung nachgezogen
- **018**: fehlende Nachweisbarkeit der Teilflaechen-Herausnahme klarer formuliert; raeumliche Unsicherheit expliziter markiert
- **019**: Detailpunkte (Zisternen, Widmung, Wege, Experimentierklausel) granularer als nur teilweise beantwortet ausgewiesen
- **022**: artspezifische Evidenz enger gefasst; Kranichbezug nicht auf alle Arten ueberdehnt
- **023**: Verdichtungscharakter und Bedarf an Punkt-fuer-Punkt-Synopse deutlicher gemacht
- **024**: allgemeiner Waldbezug vom objektspezifischen Nachweis getrennt

### Managementdokumente nachgeschaerft
- `executive_summary.md`
  - Trennung von **Evidenz** und **Synthese** eingefuehrt
  - zu starke Gesamtbewertung abgeschwaecht
  - methodischen Hinweis zu Detail-/OCR-Grenzen ergaenzt
  - prognostische Schlussformulierung vorsichtiger gefasst
- `stakeholder_ausschuss_kurzfassung.md`
  - Trennung von **Evidenz**, **Einordnung** und **Methodik** eingefuehrt
  - Wirkungsversprechen abgeschwaecht (`duerfte`, `kann`, `koennte` statt faktischer Zusicherung)

### Konsistenz / Normalisierung
- Bewertungszeilen in Detaildateien `011-030` auf die kanonische Skala `Teilweise berücksichtigt` vereinheitlicht
- betroffene Zeilen in `gesamtuebersicht.md` und `gesamtuebersicht.csv` an die nachgeschaerften Detaildateien angepasst

## 3) Geaenderte Dateien

### Detaildateien
- `analyse_stellungnahmen_solarpark/detail/001_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/002_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/004_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/007_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/011_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/012_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/013_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/014_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/015_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/016_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/017_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/018_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/019_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/020_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/021_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/022_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/023_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/024_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/025_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/026_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/027_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/028_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/029_buerger.md`
- `analyse_stellungnahmen_solarpark/detail/030_buerger.md`

### Tabellen / Management
- `analyse_stellungnahmen_solarpark/tabellen/gesamtuebersicht.md`
- `analyse_stellungnahmen_solarpark/tabellen/gesamtuebersicht.csv`
- `analyse_stellungnahmen_solarpark/executive_summary.md`
- `analyse_stellungnahmen_solarpark/stakeholder_ausschuss_kurzfassung.md`

## 4) Verworfen / nicht uebernommen

- Der Review-Hinweis auf eine vermeintlich falsche Zuordnung ab Fall 21 wurde **nicht pauschal uebernommen**.
- Gegenpruefung in `cache/buerger_segmentierung.csv` zeigt: `21 -> Buerger 20B` ist projektintern konsistent dokumentiert.
- Daher wurde **keine** Umnummerierung von Fall 21 vorgenommen.

## 5) Nicht veraendert

- Primaerquellen (`stellungnahmen/*.pdf`, `pu/*.pdf`)
- Roh-/Cache-Extrakte als Source of Truth
- Inhaltliche Dreierskala der Bewertung (`Vollständig berücksichtigt` / `Teilweise berücksichtigt` / `Nicht erkennbar berücksichtigt`)

## 6) Offene Rest-Risiken nach dem Fix-Batch

- OCR-/Anlagenrisiken bleiben in einzelnen Faellen bestehen (insb. 007, 018, 019, 022)
- Das Gesamtbild `30/30 = Teilweise berücksichtigt` bleibt methodisch erklaerungsbeduerftig, auch wenn mehrere Faelle jetzt schaerfer abgegrenzt sind
- Fuer einige Konfliktfelder fehlen weiterhin standort- oder objektspezifische Zusatznachweise; diese wurden als offene Punkte/Empfehlungen belassen, nicht erfunden
