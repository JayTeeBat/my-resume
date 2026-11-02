# Development

How to edit, check and publish [the CV](../README.md). Rendering, themes, the
schema and the check rules belong to
[resume-toolkit](https://github.com/JayTeeBat/resume-toolkit); its
[development guide][toolkit-dev] covers commands, variants and design choices.

## Editing the CV

[`resume.json`](../resume.json) holds every CV fact.
[`variants.toml`](../variants.toml) selects the cuts; only `publish = true`
variants reach the public site. Only `2-page` is public, the primary cut served
at the unsuffixed `/resume.html` and `/resume.json`. Its `formats` selects PDF/HTML/JSON for the public site;
Markdown remains in the private CI artifact. The `full` cut is built and fully checked
in CI, downloadable from the workflow run, and never deployed. Tag entries with `x-tags` or
`x-highlights` as described in the toolkit's [variants
section][toolkit-variants]: `full` marks what only the complete CV keeps;
untagged content appears in both cuts.

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
uv run resume serve           # live preview at localhost:8000; -v 2-page or -v full
uv run resume site            # build exactly what Pages publishes into dist/
```

## Publishing

The `quality` workflow runs on every pull request and on `main`. It runs the
hygiene hooks, validation, the full check and the site build, then uploads
`dist/` as the `resume` artifact. A separate `resume build --out resume-all-versions`
builds every cut in all four formats for the `resume-all-versions` artifact,
outside `dist/`. Only `main` deploys `dist/` to
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

[toolkit-dev]: https://github.com/JayTeeBat/resume-toolkit/blob/d9cdc1cf5d8c1bc959db157b33244fbb2d4e0513/docs/development.md
[toolkit-variants]: https://github.com/JayTeeBat/resume-toolkit/blob/d9cdc1cf5d8c1bc959db157b33244fbb2d4e0513/docs/development.md#variants
[toolkit-checks]: https://github.com/JayTeeBat/resume-toolkit/blob/d9cdc1cf5d8c1bc959db157b33244fbb2d4e0513/docs/checks.md
