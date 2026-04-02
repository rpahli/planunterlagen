# TODO – Analyse Stellungnahmen Solarpark (Bürger einzeln)

Status: Phase 1–3 abgeschlossen, Finalisierung/Review laufend.
Ziel: Stellungnahmen je Bürger gegen neue Planunterlagen (`pu/`) bewerten und nachvollziehbar dokumentieren.

## Phase 0 – Setup & Struktur
- [x] Arbeitsstruktur anlegen:
  - [x] `analyse_stellungnahmen_solarpark/`
  - [x] `analyse_stellungnahmen_solarpark/detail/`
  - [x] `analyse_stellungnahmen_solarpark/tabellen/`
  - [x] `analyse_stellungnahmen_solarpark/cache/`
- [x] Persistenzkonzept umsetzen:
  - [x] Roh-Extrakte aus PDFs im `cache/` speichern
  - [x] Bürger-Mapping (Nr. ↔ Stellungnahme) im `cache/` speichern
  - [x] Abgleichsnotizen je Planunterlage im `cache/` speichern

## Phase 1 – Quellen erfassen
- [x] `stellungnahmen/Stellungnahmen_Bürger_Zusammen.pdf` vollständig extrahieren
- [x] Bürgerweise segmentieren und nummerieren (laufende Nr.; 30 Einträge)
- [x] Planunterlagen aus `pu/` inhaltlich indexieren (Themen/Fundstellen; 7 PDFs)
- [x] Prüfmaßstab anwenden:
  - [x] Vollständig berücksichtigt
  - [x] Teilweise berücksichtigt
  - [x] Nicht erkennbar berücksichtigt

## Phase 2 – Parallelisierte Detailanalyse (Subagent-first)
- [x] Analyse-Batches bilden (001–010, 011–020, 021–030)
- [x] Je Batch Subagent(s) parallel ausführen
- [x] Pro Bürger Ergebnisdatei erzeugen in `detail/`:
  - [x] Ursprung Stellungnahme
  - [x] Im Entwurf berücksichtigt (mit Nachweis)
  - [x] Bewertung
  - [x] Offener Punkt
  - [x] Empfehlung
- [x] Zwischenstände persistieren (Batch-Logs, Evidenz, offene Fragen)

## Phase 3 – Gesamttabelle erzeugen
- [x] Mastertabelle in `tabellen/gesamtuebersicht.md` mit Spalten:
  - [x] Nr.
  - [x] Ursprung Stellungnahme
  - [x] Im Entwurf berücksichtigt
  - [x] Bewertung
  - [x] Offener Punkt
  - [x] Empfehlung
- [x] Tabelle als `tabellen/gesamtuebersicht.csv` exportieren
- [x] Normalisierungspass durchführen (Schreibweise + Nummernformat)
- [x] Normalisierungs-Log dokumentieren (`cache/phase2/normalisierung_log.md`)

## Phase 4 – Qualitätssicherung
- [x] Vollständigkeit prüfen (jeder Bürger genau einmal; 30/30)
- [x] Konsistenzprüfung der Bewertungen über alle Bürger
- [x] Nachweise/Fundstellen-Check je Zeile (Batch-QA Phase 3)
- [x] Offene Punkte und Empfehlungen schärfen

## Phase 5 – Review-Paket
- [x] Kurze Leseanleitung (`analyse_stellungnahmen_solarpark/README.md`) vorhanden
- [x] Änderungs-/Erkenntnisprotokolle angelegt (Phase1/2/3 + Normalisierungs-Log)
- [x] Übergabe für Review vorbereiten (Executive Summary für Entscheidungsvorlage)

---

## Offene nächste Schritte
- [x] Executive Summary (1–2 Seiten): Kernkonflikte, priorisierte Empfehlungen, Quick Wins vs. vertiefte Nacharbeit
- [ ] Optional: Zusätzliche Vereinheitlichung der historischen Batch-Dateien im Cache (nicht finalitätskritisch)
- [x] Optional: Stakeholder-/Ausschussversion mit gekürzten Formulierungen für Präsentation

## Persistente Hauptartefakte (aktueller Stand)
- Detail: `analyse_stellungnahmen_solarpark/detail/001_buerger.md` ... `030_buerger.md`
- Tabelle: `analyse_stellungnahmen_solarpark/tabellen/gesamtuebersicht.md`
- Tabelle: `analyse_stellungnahmen_solarpark/tabellen/gesamtuebersicht.csv`
- QA: `analyse_stellungnahmen_solarpark/cache/phase3/phase3_summary.md`
- Normalisierung: `analyse_stellungnahmen_solarpark/cache/phase2/normalisierung_log.md`
- Executive Summary: `analyse_stellungnahmen_solarpark/executive_summary.md`
- Stakeholder-Kurzfassung: `analyse_stellungnahmen_solarpark/stakeholder_ausschuss_kurzfassung.md`
