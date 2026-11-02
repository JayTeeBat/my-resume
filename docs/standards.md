# Standards register

| Standard | Version / pin | Scope (what it governs here) | Enforcement (rule / workflow / test, or "not enforced") | Decision (ADR link, if any) |
|---|---|---|---|---|
| JSON Resume | As declared by `$schema` in `resume.json`; toolkit pinned in `pyproject.toml` | CV interchange; toolkit uses its vendored schema | `resume validate`; `check-pins` hook for the toolkit docs link below | [Content only](adr/0004-content-only-repository.md) |
| en-GB spelling | `en-GB` | Editorial spelling consistency | `spelling` in `resume-checks.toml`, curated vocabulary | — |
| [BIPM SI Brochure](https://www.bipm.org/en/publications/si-brochure) | 9th edition (2019), via the toolkit's `unit_spacing` | Number–unit spacing in CV prose (`10 kWh`, `±3 %`) | `unit_spacing` in `resume-checks.toml` | — |
| ISO 8601 | `YYYY-MM` | Month-precision CV dates | `dates`, `date_format` | — |
| Owner format policy | ADR 0005, amended 2026-11-02 | One public cut, all cuts checked, pagination and typography | `variants.toml` publish flags and formats; `resume` workflow artifact; `required_sections`, `role_highlights`, `page_budget`, `page_breaks`; remaining policy as recorded in ADR | [Published versions](adr/0005-published-versions-and-page-layout.md) |
| Owner positioning policy | ADR 0006, 2026-11-02 | Backend positioning, evidenced skills and compact career coverage | `skill_evidence`, `role_highlights`; remaining policy as recorded in ADR | [Backend repositioning](adr/0006-backend-repositioning.md) |
| repo-standard-kit | v2.0.0, hygiene subset only | File hygiene, pinned actions and CI permissions | pre-commit (including `actionlint` and `zizmor`), quality workflow; no compliance profile | [Exemption](adr/0004-content-only-repository.md) |

## Toolkit documentation

Rendering, variants, check rules, tool behaviour and schema provenance are
documented in the [resume-toolkit docs at the pinned
ref](https://github.com/JayTeeBat/resume-toolkit/tree/v0.5.0/docs): its
`development.md` (commands, variants, design tokens), `checks.md` (every rule
and key) and `standards.md` (its register).

This is the only pinned toolkit link; every other file links here. The pin
may be a release tag or a full 40-character commit SHA while waiting for a
release. The `check-pins` pre-commit hook
([`scripts/check_pins.py`](../scripts/check_pins.py)) fails when this link's
ref differs from the `resume-toolkit` dependency in `pyproject.toml`, or when
another tracked file adds a pinned toolkit link.

## Deliberate deviations

- Exempt from compliance profiles: [ADR 0004](adr/0004-content-only-repository.md).
- Old short URLs may break, and typography floors are reviewed manually:
  [ADR 0005](adr/0005-published-versions-and-page-layout.md).
