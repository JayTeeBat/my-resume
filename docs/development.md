# Development

How to edit, check and publish [the CV](../README.md). Rendering, themes, the
schema and the check rules belong to
[resume-toolkit](https://github.com/JayTeeBat/resume-toolkit); its
[development guide][toolkit-dev] covers commands, variants and design choices.

## Editing the CV

[`resume.json`](../resume.json) holds every CV fact.
[`variants.toml`](../variants.toml) selects the cuts; only `publish = true`
variants reach the public site. All three cuts are published: `one-page`
(the primary cut, first on the site and served as `/resume.json`), `2-page`
and `full`. File order sets the site order. Tag entries with `x-tags` or
`x-highlights` as described in the toolkit's [variants
section][toolkit-variants]: `full` marks what only the complete CV keeps,
`2-page` what the two-page cut keeps but the one-page cut drops.

## Content checks

```sh
uv run resume validate        # schema
uv run resume check --fast    # prose and structure, no Chromium
uv run resume check           # also page budgets, contact header and page breaks
```

[`resume-checks.toml`](../resume-checks.toml) is this CV's editorial policy:
enabled rules, limits and owner decisions such as the gap allowlist. Rule
defaults and every key are documented in the toolkit's [checks
reference][toolkit-checks]. Hard violations fail CI. Soft warnings are
reported and need a justification in the pull request. The pre-commit hook
runs the fast check when content or policy changes.

## Previewing

```sh
uv run resume serve           # live preview at localhost:8000; -v one-page or -v 2-page
uv run resume site            # build exactly what Pages publishes into dist/
```

## Publishing

The `quality` workflow runs on every pull request and on `main`. It runs the
hygiene hooks, validation, the full check and the site build, then uploads
`dist/` as the `resume` artifact. Only `main` deploys to
[GitHub Pages](https://jayteebat.github.io/my-resume/). The checkout keeps
full history because the colophon dates the CV from the last commit that
touched `resume.json`.

## Upgrading the toolkit

1. Bump the tag in the `resume-toolkit` dependency in
   [`pyproject.toml`](../pyproject.toml), and in the toolkit documentation
   links (`git grep` the old tag).
2. Run `uv lock` and `uv sync`.
3. Run `uv run resume check` and compare the soft warnings with the previous
   tag; explain any new ones in the pull request.
4. Run `uv run resume site` and review the rendered PDF before merging.

[toolkit-dev]: https://github.com/JayTeeBat/resume-toolkit/blob/v0.2.0/docs/development.md
[toolkit-variants]: https://github.com/JayTeeBat/resume-toolkit/blob/v0.2.0/docs/development.md#variants
[toolkit-checks]: https://github.com/JayTeeBat/resume-toolkit/blob/v0.2.0/docs/checks.md
