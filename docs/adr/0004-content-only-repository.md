# ADR 0004: Content-only repository after toolkit extraction

## Status

Accepted. Supersedes [ADR 0002](0002-adopt-repo-standard.md).

## Context

The renderer, checks, theme, site template, schema and tests moved to
[resume-toolkit](https://github.com/JayTeeBat/resume-toolkit), which this
repository now installs from a git tag. Their decision record, formerly
ADR 0003 here, moved with them. What remains is CV content, its editorial
policy, documentation and the workflow that publishes the site.

[repo-standard-kit v2.0.0](https://github.com/JayTeeBat/repo-standard-kit/tree/v2.0.0)
only defines profiles for code projects. Its `python-single` profile expects
Python sources, tests, lint, type checks and a package build, none of which
exist here any more. The standard has no profile for a repository whose job
is to hold content and publish a static site, so no profile describes this
repository honestly.

## Decision

Stop claiming compliance: remove `[tool.repo-standard]`, the compliance
workflow and the `repo-check` pre-commit hook rather than add empty Python
scaffolding to satisfy a profile that does not apply.

Keep the standard's hygiene that still applies:

- pre-commit file hooks: check-yaml, check-toml, check-json,
  trailing-whitespace, end-of-file-fixer, check-merge-conflict,
  detect-private-key, detect-secrets, check-added-large-files and Markdown lint
- every remote action pinned to a full 40-character commit SHA with a version
  comment, kept current by Dependabot for GitHub Actions
- the `quality` job limited to `contents: read`, with Pages write permissions
  confined to the deploy job
- `quality` as a required status check on `main`

## Consequences

The `compliance` status check no longer reports and must be removed from the
`main` ruleset's required checks. `repo-check` reports failures against
`python-single`; they are expected and not tracked as defects.

If the standard gains a content or static-site profile, adopt it and restore
the compliance workflow and hook with full compliance.
