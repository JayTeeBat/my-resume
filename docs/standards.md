# Standards register

| Standard | Version / pin | Scope (what it governs here) | Enforcement (rule / workflow / test, or "not enforced") | Decision (ADR link, if any) |
|---|---|---|---|---|
| JSON Resume | `$schema` v1.0.0; toolkit v0.3.0 | CV interchange; toolkit uses its vendored schema | `resume validate`; quality pin-drift step | [Content only](adr/0004-content-only-repository.md) |
| en-GB spelling | `en-GB` | Editorial spelling consistency | `spelling` in `resume-checks.toml`, curated vocabulary | — |
| [BIPM SI Brochure](https://www.bipm.org/en/publications/si-brochure) | 9th edition (2019), via the toolkit's `unit_spacing` | Number–unit spacing in CV prose (`10 kWh`, `±3 %`) | `unit_spacing` in `resume-checks.toml` | — |
| ISO 8601 | `YYYY-MM` | Month-precision CV dates | `dates`, `date_format` | — |
| Owner format policy | ADR 0005, amended 2026-11-01 | One public cut, all cuts checked, pagination and typography | `variants.toml` publish flags; separate workflow artifacts; `required_sections`, `role_highlights`, `page_budget`, `page_breaks`; remaining policy as recorded in ADR | [Published versions](adr/0005-published-versions-and-page-layout.md) |
| repo-standard-kit | v2.0.0, hygiene subset only | File hygiene, pinned actions and CI permissions | pre-commit, quality workflow; no compliance profile | [Exemption](adr/0004-content-only-repository.md) |

Tool behavior and schema provenance: [toolkit register](https://github.com/JayTeeBat/resume-toolkit/blob/v0.3.0/docs/standards.md).

The toolkit pin may be a release tag or a full 40-character commit SHA while
waiting for a release. The JSON Resume row and every toolkit documentation
link must match the dependency in `pyproject.toml`; the quality workflow checks
both forms. Re-pin to v0.3.0 after the toolkit PR merges and the tag exists.

## Deliberate deviations

- Exempt from compliance profiles: [ADR 0004](adr/0004-content-only-repository.md).
- Old short URLs may break, and compact floors are reviewed manually:
  [ADR 0005](adr/0005-published-versions-and-page-layout.md).
