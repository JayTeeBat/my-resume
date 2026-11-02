# ADR 0005: Published versions and page layout

## Status

Accepted. 2026-10-31.

Amended 2026-11-01: publish only the two-page cut, retain all cuts in CI artifacts, and use name-based PDFs with an unlabelled primary colophon; the public site serves PDF/HTML/JSON, with Markdown only in the CI artifact.

Amended 2026-11-02: the one-page cut is retired for now. It was private, and its budget fought every content change; the two-page cut is the CV. Its rows below are removed, and the 2-page include no longer needs a `2-page` tag; per-role coverage is set by the `role_highlights` bands in [ADR 0006](0006-backend-repositioning.md).

Amended 2026-11-02 (toolkit 0.5.0): the primary cut publishes at the unsuffixed `resume.html` and `resume.json`; the former `resume-2-page.*` URLs break, without redirects.

## Context

A two-page primary CV and a full alternative share one factual source in this
[content-only repository](0004-content-only-repository.md). The owner chooses
coverage and readability over fitting by silently dropping whole roles.

## Decision

| Owner decision and rationale | Enforcement |
|---|---|
| One public version (`2-page`) in PDF/HTML/JSON, including the landing page, sitemap, llms.txt, `/resume.html` and `/resume.json`; full built and fully checked in CI, downloadable from the workflow run, not deployed | `variants.toml` order, `publish` and `formats`; `resume-checks.toml` explicitly checks both; quality workflow builds `resume-all-versions/` and uploads `resume-all-versions`, while Pages uploads only `dist/` |
| PDFs use `Jacques-Thomazo-Resume.pdf` for the primary cut and `Jacques-Thomazo-Resume-Full.pdf` for the full cut; old PDF URLs may break | Toolkit PDF naming and site-link tests; no redirects |
| Rename `short` to `2-page`; old `resume-short.*` links may break because little has been shared | No redirects; not mechanically enforced |
| 2-page = 2 pages, full unbounded, preserving a complete archive | `page_budget` per-variant table (full omitted) |
| Keep companies whole; if taller than a page, break between roles, never inside one, preserving reading context | `page_breaks` |
| Every PDF page repeats build stamp · latest-at link and page number; the public primary version has no version label, while all other cuts keep it. HTML and Markdown colophons follow the same rule; stamp shown as `YYYY-MM-DD · rev <hash>` | Toolkit build primary selection and shared theme footer (7.5pt default); toolkit PDF text, colophon and parity regression tests |
| Respect body ≥9pt, small text ≥7.5pt, leading ≥1.2, side margins ≥12 mm, bottom margin 15 mm; retain at least one body line of spare space | Toolkit [authoring floors](https://github.com/JayTeeBat/resume-toolkit/blob/d9cdc1cf5d8c1bc959db157b33244fbb2d4e0513/docs/development.md#per-variant-design-tokens); not mechanically enforced |
| Use “Skills” and print profile URL addresses for ATS readability | Toolkit theme defaults (addresses omit scheme and `www`); not a content check |
| Select content only with `x-tags`/`x-highlights`; never fork wording per version, avoiding factual drift | One `resume.json`, toolkit filtering; editorial policy not mechanically enforced |

## Consequences

[Toolkit checks](https://github.com/JayTeeBat/resume-toolkit/blob/d9cdc1cf5d8c1bc959db157b33244fbb2d4e0513/docs/checks.md)
enforce coverage and layout. Visual review still owns readability. Baseline sections
`basics`, `work`, `skills`, `education` are required in every checked cut, including the private full variant.
