## Buerger-Extraktion

### Extraction quality notes
- Quelle: `stellungnahmen/Stellungnahmen_Buerger_Zusammen.pdf`
- Volltext primaer per `pdftotext -layout` nach `analyse_stellungnahmen_solarpark/cache/buerger_rohtext.md` extrahiert.
- OCR/Textqualitaet insgesamt gut, aber mit typischen Artefakten (z. B. "8" statt "\u00a7", einzelne Zeichensatz-/Zeilenumbruchsfehler).
- Eine Stellungnahme (Buerger 7) lag im PDF als bildbasierte Seite vor; diese wurde als unsicherer OCR-Nachtrag in `buerger_rohtext.md` markiert.

### Ambiguities
- Buerger 7: Seitenzuordnung auf Basis des PDF-Ablaufs als "vermutlich S. 9" gekennzeichnet.
- Buerger 22: umfasst einen sehr langen Block mit mehreren thematischen Untereinwendungen (S. 35-56), aber ohne neue Buerger-Kennung; als ein Eintrag segmentiert.
- Einzelne redaktionelle Schwaerzungen/fehlende Textteile in bildbasierten Bereichen sind im Rohtext als unsicher markiert.

### Count of segmented entries
- Segmentierte Eintraege gesamt: **30**
- Davon eindeutig per Kennung im Haupttext: **29**
- Zusaetzlich bildbasierter OCR-Eintrag: **1** (Buerger 7, unsicher)

## Planunterlagen-Index

### Quality notes
- Quelle: lokale TXT-Extrakte aus `analyse_stellungnahmen_solarpark/cache/planunterlagen_raw/*.txt`.
- Alle 7 vorhandenen Dokumente im Ordner wurden gesichtet und im Index (`planunterlagen_index.md`) sowie als Themen-CSV (`planunterlagen_themen.csv`) strukturiert erfasst.
- Inhaltliche Aussagen wurden nur aus lesbaren Textpassagen abgeleitet; unsichere Ableitungen sind explizit markiert.

### Uncertainties
- `260204_Waltersdorf_Anlage2.txt` ist stark karten-/layoutdominiert; OCR liefert nur fragmentarische Legenden- und Kartenbeschriftungen.
- `251219_Waltersdorf_Anlage4.txt` enthaelt im TXT faktisch nur das Deckblatt der FFH-Vorpruefung; detaillierte Inhalte sind aus dem Extract nicht belastbar ableitbar.
- `251219_Waltersdorf_PlanteilD.txt` und Teile von `251219_Waltersdorf_PlanteilAB.txt` sind durch Planlayout nur eingeschraenkt textlich auswertbar.

### Count of indexed documents
- Indexierte Dokumente gesamt: **7**
