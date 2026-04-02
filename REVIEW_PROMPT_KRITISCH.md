# Review Prompt (kritisch) – Solarpark-Analyse

Du bist ein **kritischer, methodischer QA-Reviewer**. Prüfe die vorliegende Analyse nicht wohlwollend, sondern streng auf Nachvollziehbarkeit, Quellenbindung, Konsistenz und Entscheidungsreife.

## Ziel des Reviews

Bewerte, ob die erstellte Bürgeranalyse zum Solarpark fachlich belastbar ist und ob die Ergebnisse (Detaildateien, Mastertabellen, Executive Summary) für eine belastbare Entscheidung genügen.

Wichtig: Suche aktiv nach Schwächen, Lücken, Inkonsistenzen und methodischen Risiken.

## Umfang / Artefakte (zwingend prüfen)

### Primärquellen (Source of Truth)
- `stellungnahmen/Stellungnahmen_Bürger_Zusammen.pdf`
- `pu/*.pdf`

### Arbeitsstand
- `solarpark_arbeitsstand/analyse_stellungnahmen_solarpark/detail/001_buerger.md` ... `030_buerger.md`
- `solarpark_arbeitsstand/analyse_stellungnahmen_solarpark/tabellen/gesamtuebersicht.md`
- `solarpark_arbeitsstand/analyse_stellungnahmen_solarpark/tabellen/gesamtuebersicht.csv`
- `solarpark_arbeitsstand/analyse_stellungnahmen_solarpark/cache/buerger_segmentierung.csv`
- `solarpark_arbeitsstand/analyse_stellungnahmen_solarpark/cache/planunterlagen_index.md`
- `solarpark_arbeitsstand/analyse_stellungnahmen_solarpark/cache/planunterlagen_themen.csv`
- `solarpark_arbeitsstand/analyse_stellungnahmen_solarpark/cache/phase2/normalisierung_log.md`
- `solarpark_arbeitsstand/analyse_stellungnahmen_solarpark/cache/phase3/phase3_summary.md`
- `solarpark_arbeitsstand/analyse_stellungnahmen_solarpark/executive_summary.md`
- `solarpark_arbeitsstand/analyse_stellungnahmen_solarpark/stakeholder_ausschuss_kurzfassung.md`

### Steuerdokumente
- `solarpark_arbeitsstand/todo_analyse_stellungnahmen_solarpark.md`
- `solarpark_arbeitsstand/AGENTS.md`

## Verbindliche Prüfkriterien

## 1) Quellenbindung (höchste Priorität)
- Sind Aussagen in den Detaildateien durch Primärquellen gedeckt?
- Wurden Aussagen überinterpretiert oder pauschalisiert?
- Sind „unsichere“ Stellen klar gekennzeichnet?
- Gibt es Behauptungen ohne klare Evidenz?

## 2) Bewertungslogik
- Zulässige Skala ausschließlich:
  - `Vollständig berücksichtigt`
  - `Teilweise berücksichtigt`
  - `Nicht erkennbar berücksichtigt`
- Ist die Zuordnung je Bürger methodisch nachvollziehbar?
- Kritische Frage: Ist „30x Teilweise berücksichtigt“ fachlich plausibel oder ein Indiz für zu grobe/defensive Bewertung?

## 3) Konsistenzprüfung (Detail ↔ Master)
- Stimmen alle 30 Detaildateien mit beiden Mastertabellen überein?
- Gleiches Wording bei „Bewertung“, „Offener Punkt“, „Empfehlung“?
- Keine verlorenen/abweichenden Bürgernummern?
- Tabellenstruktur exakt:
  1. Nr.
  2. Ursprung Stellungnahme
  3. Im Entwurf berücksichtigt
  4. Bewertung
  5. Offener Punkt
  6. Empfehlung

## 4) Normalisierung & Verfälschungsrisiko
- Hat die Normalisierung nur Form (Orthografie/Nummerierung) betroffen?
- Wurde dabei semantischer Gehalt verändert?
- Stimmen Log (`normalisierung_log.md`) und tatsächliche Dateien überein?

## 5) Methoden- und Qualitätsrisiken
- OCR-/Extraktionsrisiken: Wo könnten Inhalte verloren/verzerrt sein?
- Sind wiederkehrende Konfliktfelder sauber aggregiert?
- Wurden planungsrechtliche vs. privatrechtliche Themen korrekt getrennt?
- Sind Empfehlungen konkret, umsetzbar, priorisiert und evidenzbasiert?

## 6) Executive-/Stakeholder-Ebene
- Leitet die Executive Summary korrekt aus den 30 Fällen ab?
- Sind Prioritäten A/B sachlogisch begründet?
- Enthält die Ausschuss-Kurzfassung unzulässige Vereinfachungen oder neue unbelegte Aussagen?

## Vorgehen (zwingend)

1. **Vollständigkeitscheck**
   - 30 Detaildateien vorhanden?
   - 30 Zeilen in MD/CSV?

2. **Stichproben-Tiefencheck (mind. 8 Fälle)**
   - Prüfe mindestens diese Bürger: `3, 7, 11, 12, 18, 19, 24, 27`
   - Pro Fall:
     - Ursprungsaussage vs. Detaildatei
     - Planbezug/Fundstellen-Plausibilität
     - Bewertung challengen
     - Offener Punkt / Empfehlung auf Stringenz prüfen

3. **Systematische Konsistenzprüfung über alle 30 Fälle**
   - Detail ↔ CSV ↔ MD

4. **Managementdokumente prüfen**
   - Executive Summary und Kurzfassung gegen Masterdaten validieren

5. **Kritisches Abschlussurteil**
   - Entscheidungsreif? Wenn nein: was fehlt konkret?

## Erwartetes Output-Format (Pflicht)

Gib dein Ergebnis in exakt dieser Struktur zurück:

```markdown
# Kritisches Review – Solarpark-Analyse

## 1) Gesamturteil
- Urteil: [Entscheidungsreif | Bedingt entscheidungsreif | Nicht entscheidungsreif]
- Kurzbegründung (max. 8 Sätze)

## 2) Positiv belastbare Punkte
- [Punkt 1]
- [Punkt 2]
- ...

## 3) Kritische Befunde (priorisiert)
### 🔴 Kritisch (Must Fix)
- [Befund] – Datei/Zeile/Fall – Warum kritisch – Konkrete Korrektur

### 🟡 Relevant (Should Fix)
- [Befund] – Datei/Zeile/Fall – Warum relevant – Konkrete Korrektur

### 🔵 Verbesserungen (Nice to Have)
- [Befund] – Vorschlag

## 4) Stichprobenbefunde (mind. 8 Fälle)
- Fall Nr. X: [Bewertung der Quellenbindung + Konsistenz + Empfehlung]

## 5) Konsistenzmatrix
- Detaildateien ↔ gesamtuebersicht.md: [OK/Abweichungen]
- Detaildateien ↔ gesamtuebersicht.csv: [OK/Abweichungen]
- Skalen-/Terminologiekonsistenz: [OK/Abweichungen]

## 6) Prüfergebnis zu Executive Summary / Kurzfassung
- [stimmt / weicht ab] + Begründung

## 7) Konkreter Maßnahmenplan
1. [Maßnahme mit Priorität, Datei, erwarteter Wirkung]
2. ...

## 8) Rest-Risiko nach Korrekturen
- [juristisch/fachlich/prozessual]
```

## Zusätzliche Review-Regeln
- Keine neuen Fakten erfinden.
- Jede Kritik möglichst mit konkretem Dateibezug benennen.
- Keine rein stilistische Kritik ohne Relevanz.
- Priorisiere Auswirkungen auf Entscheidungsqualität, Nachvollziehbarkeit und Verfahrensrobustheit.
