# ADR 0005: Published versions and page layout

## Status

Accepted. 2026-10-31.

Amended 2026-11-01: publish only the two-page cut, retain all cuts in CI artifacts, and use name-based PDFs with an unlabelled primary colophon; the public site serves PDF/HTML/JSON, with Markdown only in the CI artifact.

## Context

A two-page primary CV, a one-page and a full alternative share one factual source in this
[content-only repository](0004-content-only-repository.md). The owner chooses
coverage and readability over fitting by silently dropping whole roles.

## Decision

| Owner decision and rationale | Enforcement |
|---|---|
| One public version (`2-page`) in PDF/HTML/JSON, including the landing page, sitemap, llms.txt and `/resume.json`; one-page and full built and fully checked in CI, downloadable from the workflow run, not deployed | `variants.toml` order, `publish` and `formats`; `resume-checks.toml` explicitly checks all three; quality workflow builds `resume-all-versions/` and uploads `resume-all-versions`, while Pages uploads only `dist/` |
| PDFs use `Jacques-Thomazo-Resume.pdf` for the primary cut and `Jacques-Thomazo-Resume-One-Page.pdf` / `Jacques-Thomazo-Resume-Full.pdf` for the other cuts; old PDF URLs may break | Toolkit PDF naming and site-link tests; no redirects |
| Rename `short` to `2-page`; old `resume-short.*` links may break because little has been shared | No redirects; not mechanically enforced |
| One-page = 1 page, 2-page = 2, full unbounded, preserving a complete archive | `page_budget` per-variant table (full omitted) |
| Keep companies whole; if taller than a page, break between roles, never inside one, preserving reading context | `page_breaks` |
| Every PDF page repeats build stamp · latest-at link and page number; the public primary version has no version label, while all other cuts keep it. HTML and Markdown colophons follow the same rule; stamp shown as `YYYY-MM-DD · rev <hash>` | Toolkit build primary selection and shared theme footer (7.5pt default); toolkit PDF text, colophon and parity regression tests |
| One-page always includes education and languages, and every role starting on/after the master's degree end (Diplôme d'Ingénieur, 2010-06) has at least one bullet; earlier internships are exempt | `required_sections.one-page`; `role_highlights.one-page = { min = 1, since = "2010-06" }` |
| Compact typography only for one-page; alternatives retain the default look | `one-page.style`; exclusivity not mechanically enforced |
| Respect body ≥9pt, small text ≥7.5pt, leading ≥1.2, side margins ≥12 mm, bottom margin 15 mm; retain at least one body line of spare space | Toolkit [authoring floors](https://github.com/JayTeeBat/resume-toolkit/blob/fe8b62f6eebaa72ee6fcf17f7937ae691e560711/docs/development.md#per-variant-design-tokens); not mechanically enforced |
| Use “Skills” and print profile URL addresses for ATS readability | Toolkit theme defaults (addresses omit scheme and `www`); not a content check |
| Select content only with `x-tags`/`x-highlights`; never fork wording per version, avoiding factual drift | One `resume.json`, toolkit filtering; editorial policy not mechanically enforced |

## Consequences

[Toolkit checks](https://github.com/JayTeeBat/resume-toolkit/blob/fe8b62f6eebaa72ee6fcf17f7937ae691e560711/docs/checks.md)
enforce coverage and layout. Visual review still owns readability. Baseline sections
`basics`, `work`, `skills`, `education` are required in every checked cut, including the private one-page and full variants.
