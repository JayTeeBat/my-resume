# AGENTS.md

See the [standards register](docs/standards.md) for scope and enforcement.

## Repository Purpose

Hold Jacques Thomazo’s CV as JSON Resume content and publish it as HTML, PDF,
JSON, Markdown and a GitHub Pages site, rendered and checked by
[resume-toolkit].

## Repository Context

- Repository name: `my-resume`; content only, no package code
- Content format: JSON Resume (`resume.json`) with TOML configuration
- Runtime/build system: `uv`, non-package project in `pyproject.toml` that
  depends on [resume-toolkit] at a pinned git tag
- Repository type: CV content and static site publishing
- Toolkit: rendering, themes, the schema, check rules and their tests live in
  [resume-toolkit]; change them there, not here
- Standards: hygiene subset of [repo-standard-kit]; see
  [ADR 0004](docs/adr/0004-content-only-repository.md)
- Key directories:
  - `docs/`: durable repository knowledge
  - `.github/`: the quality and Pages workflow, Dependabot, PR template

## Human And Agent Responsibilities

### Goal

Define clear decision boundaries between humans and agents so implementation
work can move quickly without ambiguity or accidental overreach.

### Human Responsibilities

Humans own:

- product scope and intent
- security exceptions and secret handling
- merge and release authority
- production access and production operations sign-off
- approval of breaking API, schema, or migration changes
- architectural exceptions to the documented standard

### Agent Responsibilities

Agents own:

- implementation within documented repository boundaries
- running the content checks and local verification
- documentation updates tied to behavior changes
- workflow, dependency and toolkit-version maintenance
- surfacing risks, missing decisions, and unclear contracts

### Shared Expectations

- Keep content, configuration, and docs aligned
- Prefer small, reviewable changes
- Make operational boundaries explicit
- Do not rely on undocumented local knowledge

### Agent Prohibitions

Agents must not:

- bypass documented quality gates
- weaken or disable content checks without explicit instruction
- invent, embellish, or infer CV facts
- make security, release, or breaking-change decisions alone
- modify out-of-scope systems without explicit approval

## Agent Operating Mode

Agent behaviour in this repository is calibrated, not left to model defaults.
Each dial runs from 1 to 5, where 5 is the maximum:

- **Verbosity:** 2 / 5
- **Precision, repeatability, determinism:** 4 / 5

Low verbosity means:

- Answer what was asked; do not restate the request or read the plan back
- Report outcomes, not a narration of the steps taken to reach them
- Prefer a diff, a command, or a `path:line` reference over prose describing it
- Open with the result; no preamble, and no recap the transcript already shows
- Spend words on decisions the reader must make, on risks, and on failures

High precision, repeatability, and determinism mean:

- Verify against the repository before asserting, and cite `path:line`
- Reuse the pattern already in the file rather than introducing a second one
- Make the smallest change that satisfies the requirement, and nothing beyond it
- Run the documented quality gates in order and report their real output
- Pin versions, ordering, and formatting rather than leaving them to chance
- State assumptions explicitly where the repository does not settle a choice
- The same task on the same input should reach the same result on a second run

The levels are policy values from [repo-standard-kit]; keep them unchanged.

## Single Source Of Truth

`resume.json` is the only home for CV facts. Never invent CV facts; ask the owner
when dates, claims, or wording need factual confirmation. `variants.toml` selects
cuts and `resume-checks.toml` holds editorial policy; neither carries CV facts.

Anything stated twice drifts, and the copy that drifts is the one nobody is
reading when it matters. Before writing, look for what already exists and
derive from it.

- **One home per fact.** A value, a command, a version, a path, a section
  order, a schema: declared in exactly one place, with every other use reading
  from that place
- **Derive, do not copy.** Where two artefacts must agree, generate one from
  the other or both from a shared source, and put the check that they still
  agree in the quality gates
- **Reference, do not restate.** Link to the document that owns a subject
  instead of summarising it somewhere it will go stale
- **Extend rather than parallel.** A second helper, constant, fixture, config
  key, or type that means what an existing one means is duplication even when
  the wording differs — change the original instead
- **Make unavoidable duplication fail loudly.** Where a copy cannot be removed,
  add a test or check that regenerates it and compares, so drift is a failure
  rather than a surprise
- **Deleting the stale copy is part of the change** that made it stale, not a
  follow-up

This applies to code, configuration, documentation, fixtures, and data alike.
When a change means editing the same fact in more than one file, treat that as
the defect to fix first.

## Workflow

### Default Model

Use trunk-based development with pull requests.

### Branching Rules

- `main` is the primary long-lived integration branch and is always releasable
- work happens on short-lived branches
- use one branch per objective
- branch prefixes:
  - `feat/`
  - `fix/`
  - `refactor/`
  - `docs/`
  - `chore/`

### Parallel Collaboration

- prefer small PRs over long-lived branches
- use stacked PRs when a larger change needs sequencing
- rebase private branches frequently to reduce drift
- avoid multiple concurrent branches changing the same subsystem without
  coordination

### History Rules

- rebasing private branches is allowed
- rewriting shared branches is not allowed
- merge through reviewed PRs only
- cut releases from `main` with tags

## Quality Gates

Install Chromium once with `uv run playwright install chromium`.
Preview edits with `uv run resume serve` (or `-v one-page`, `-v 2-page`); build what Pages
publishes with `uv run resume site`.

Run from repo root:

1. `uv sync --locked`
2. `uv run pre-commit run --all-files`
3. `uv run resume validate`
4. `uv run resume check`

`resume check` applies the rules from [resume-toolkit] with the policy in
`resume-checks.toml`; `--fast` skips Chromium and runs in pre-commit, CI runs
the full check. Hard violations fail. Soft warnings must not grow without a
justification in the pull request. Never auto-fix or silence a finding by
editing CV facts; ask the owner.

The quality job's effective permissions must be exactly `contents: read`, and
every remote action must be pinned to a full 40-character commit SHA. Keep
version comments and GitHub Actions Dependabot configuration so those pins
remain maintainable.

Branch protection must require the `quality` status check.

## Documentation Rules

- Keep `README.md` lean and visitor-facing; put editing, checks, publishing
  and upgrade detail in `docs/development.md`
- Link to the [resume-toolkit] docs for toolkit behavior instead of restating it
- Update `AGENTS.md` when operating rules change
- Add ADRs for significant repository decisions

## Repository Layout

- `resume.json`: all CV facts
- `variants.toml`: variant selection and publishing configuration
- `resume-checks.toml`: CV quality policy; rule defaults in the toolkit docs
- `docs/`: durable project knowledge
- `dist/`: generated outputs; never commit

## Change Control Notes

Preserve variant semantics and the published outputs. Upgrade the toolkit by
bumping its tag as described in `docs/development.md`, and compare soft
warnings and the rendered site before and after. Keep the full-history
checkout: the colophon dates content from git.
Only `main` deploys Pages; all branches upload preview artifacts. Open PRs against
`main`, or explicitly name and link the parent PR when stacking. Never merge
without owner authorization. Changes to CV facts require owner confirmation.
The MIT grant excludes CV content and its derived outputs; see [LICENSE](LICENSE).

[repo-standard-kit]: https://github.com/JayTeeBat/repo-standard-kit/tree/v2.0.0
[resume-toolkit]: https://github.com/JayTeeBat/resume-toolkit
