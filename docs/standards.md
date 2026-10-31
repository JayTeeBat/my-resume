# Standards register

| Standard | Version / pin | Scope (what it governs here) | Enforcement (rule / workflow / test, or "not enforced") | Decision (ADR link, if any) |
|---|---|---|---|---|
| JSON Resume | `$schema` v1.0.0; toolkit v0.2.0 (temporary 40-character PR SHA) | CV interchange; toolkit uses its vendored schema | `resume validate`; quality pin-drift step | [Content only](adr/0004-content-only-repository.md) |
| en-GB spelling | `en-GB` | Editorial spelling consistency | `spelling` in `resume-checks.toml`, curated vocabulary | — |
| BIPM SI Brochure | SI unit spacing convention | Supported units in CV prose | `unit_spacing` in `resume-checks.toml` | — |
| ISO 8601 | `YYYY-MM` | Month-precision CV dates | `dates`, `date_format` | — |
| Owner format policy | ADR 0005, 2026-10-31 | Published cuts, coverage, pagination and typography | `required_sections`, `role_highlights`, `page_budget`, `page_breaks`; remaining policy as recorded in ADR | [Published versions](adr/0005-published-versions-and-page-layout.md) |
| repo-standard-kit | v2.0.0, hygiene subset only | File hygiene, pinned actions and CI permissions | pre-commit, quality workflow; no compliance profile | [Exemption](adr/0004-content-only-repository.md) |

Tool behavior and schema provenance: [toolkit register](https://github.com/JayTeeBat/resume-toolkit/blob/v0.2.0/docs/standards.md).

## Deliberate deviations

- Exempt from compliance profiles: [ADR 0004](adr/0004-content-only-repository.md).
- Old short URLs may break, and compact floors are reviewed manually:
  [ADR 0005](adr/0005-published-versions-and-page-layout.md).
