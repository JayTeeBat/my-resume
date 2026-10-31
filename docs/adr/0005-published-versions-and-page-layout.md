# ADR 0005: Published versions and page layout

## Status

Accepted. 2026-10-31.

## Context

A two-page primary CV, a one-page and a full alternative share one factual source in this
[content-only repository](0004-content-only-repository.md). The owner chooses
coverage and readability over fitting by silently dropping whole roles.

## Decision

| Owner decision and rationale | Enforcement |
|---|---|
| Publish `2-page`, `one-page`, `full` in HTML/PDF/JSON/Markdown; 2-page first, primary for `/resume.json` and llms.txt, as the default read for 15+ years of experience; one-page for applications that ask for one page | `variants.toml` order and `publish`; toolkit site defaults; exact three-cut policy not mechanically enforced |
| Rename `short` to `2-page`; old `resume-short.*` links may break because little has been shared | No redirects; not mechanically enforced |
| One-page = 1 page, 2-page = 2, full unbounded, preserving a complete archive | `page_budget` per-variant table (full omitted) |
| Keep companies whole; if taller than a page, break between roles, never inside one, preserving reading context | `page_breaks` |
| Every PDF page repeats version · build stamp · latest-at link and page number, so detached pages remain identifiable. Footer identical across versions; only the version label and page count vary; stamp shown as `YYYY-MM-DD · rev <hash>` | Toolkit theme footer (7.5pt default; no `--size-footer` override in `variants.toml`); not a check |
| One-page always includes education and languages, and every role starting on/after the master's degree end (Diplôme d'Ingénieur, 2010-06) has at least one bullet; earlier internships are exempt | `required_sections.one-page`; `role_highlights.one-page = { min = 1, since = "2010-06" }` |
| Compact typography only for one-page; alternatives retain the default look | `one-page.style`; exclusivity not mechanically enforced |
| Respect body ≥9pt, small text ≥7.5pt, leading ≥1.2, side margins ≥12 mm, bottom margin 15 mm; retain at least one body line of spare space | Toolkit [authoring floors](https://github.com/JayTeeBat/resume-toolkit/blob/v0.2.0/docs/development.md#per-variant-design-tokens); not mechanically enforced |
| Use “Skills” and print profile URL addresses for ATS readability | Toolkit theme defaults (addresses omit scheme and `www`); not a content check |
| Select content only with `x-tags`/`x-highlights`; never fork wording per version, avoiding factual drift | One `resume.json`, toolkit filtering; editorial policy not mechanically enforced |

## Consequences

[Toolkit v0.2.0 checks](https://github.com/JayTeeBat/resume-toolkit/blob/v0.2.0/docs/checks.md)
enforce coverage and layout. Visual review still owns readability. Baseline sections
`basics`, `work`, `skills`, `education` are required in every published cut.
