# MVP-0 Source Coverage & Precedence Audit
## International Basketball Historical Analytics (2005–2025)

---

## 1. Source Capabilities & Ingested Volume

| Source ID | Source Name | Type | Ingested Games | Hash Protocol |
| :--- | :--- | :--- | :---: | :---: |
| `SRC_WIKI_ARCHIVE` | Wikipedia Match Archives | Secondary Structured | 559 | SHA-256 Immutability |
| `SRC_FIBA_ARCHIVE` | FIBA Official Registry | Official Historical | 19 editions | SHA-256 Immutability |

---

## 2. Precedence & Conflict Policy
- Primary source values are never overwritten silently. Discrepancies are logged to `fact_validation_issue`.
