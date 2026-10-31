# Changelog

## [Unreleased]

### Added

- [ADR 0005](docs/adr/0005-published-versions-and-page-layout.md) records owner
  format policy, enforced by `required_sections` and `role_highlights` coverage.
- Standards register and CI pin-drift check.

- Publish three cuts: `one-page` (new, primary), `2-page` and `full`. The
  one-page cut is selected with `x-tags`/`x-highlights` only (tag `2-page`).
  Depends on resume-toolkit v0.2.0 (pagination, running footer, per-variant
  page budgets and styles).

- Config-driven `resume check` with actionable text/JSON diagnostics, fast and
  strict modes, and fixture-based rule tests ahead of toolkit extraction.

- Adopt repo-standard-kit v2.0.0 with the python-single profile, pinned
  compliance checking, local hooks, type checking, and an audited secrets baseline.
- Document contributor gates, the adoption decision, and MIT code licensing
  with CV content and derived outputs reserved to Jacques Thomazo.

### Changed

- Rename the published `short` cut to `2-page`; `resume-short.*` URLs no
  longer exist after deploy.
- Depend on resume-toolkit 0.2.0: per-variant page budgets, the
  `page_breaks` check, running PDF footer with page numbers, full profile
  addresses and a "Skills" heading.
- The PDF footer is identical on every cut (theme default 7.5pt, no one-page
  override) and shows the build as `2026-10-31 · rev 39140c4`.

- Rename the build workflow to quality, add standard gates, and pin actions
  while preserving Chromium tests, artifacts, and main-only Pages deployment.
- Format and lint Python code without changing CV rendering behavior.
- Depend on resume-toolkit v0.1.0 from its git tag as a non-package uv project.
- Quality workflow drops Python lint, type, test and package steps, keeps
  hygiene hooks, validation, the full content check, the site artifact and
  main-only Pages deploy, and pins every action to its latest release.
- Rewrite the development guide, README and AGENTS.md for the content-only
  setup; LICENSE separates reserved CV content from MIT configuration.

### Removed

- Toolkit code, theme, site template, schema, tests and their docs, now in
  [resume-toolkit](https://github.com/JayTeeBat/resume-toolkit).
- Compliance workflow, `repo-check` hook and `[tool.repo-standard]`: the
  repository is content only and fits no repo-standard-kit profile
  (ADR 0004).
