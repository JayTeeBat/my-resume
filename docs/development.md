# Development

How the toolchain behind [the CV](../README.md) works, and how to work on it.

## Setup

```sh
uv sync
uv run playwright install chromium   # one-time, ~150MB
```

## Working on the CV

```sh
uv run resume serve                  # preview at localhost:8000, reloads as you edit
uv run resume build                  # -> dist/resume-{full,short}.{pdf,html,json,md}
```

`serve` is the one to use while writing or restyling: leave it running, edit
[`resume.json`](../resume.json) or `themes/classic/style.css`, and the browser reloads itself. Add
`-v short` to preview the short cut. Reach for `build` when you want the actual PDF in `dist/`.

## Commands

| Command | Does |
|---|---|
| `uv run resume validate` | Check `resume.json` against the schema |
| `uv run resume check` | Check prose, structure and layout using `resume-checks.toml` |
| `uv run resume check --fast` | Check without Chromium; `--strict` also fails on warnings |
| `uv run resume variants` | List the variants defined in `variants.toml` |
| `uv run resume build` | Render every variant to `dist/` |
| `uv run resume build -v short -f pdf` | Render one variant, one format |
| `uv run resume site` | Every variant **plus** the `index.html` landing page — what CI publishes |
| `uv run resume serve` | Browser preview, live-reloads on edit |

To see exactly what the published site will look like, `uv run resume site` and open
`dist/index.html`.

## How it fits together

```text
resume.json ──validate (schema)──> apply variant (x-tags) ──> Jinja2 + theme ──> HTML
                                                                                  │
                                                                     Chromium print-to-PDF
                                                                                  ↓
                                                                        dist/resume-*.pdf
```

- **Content** lives in `resume.json`. Nothing else should carry CV facts.
- **Styling** lives in `themes/classic/style.css`. The template carries structure only, so restyling
  never means touching HTML. The tokens at the top of the stylesheet (`--size-base`, `--leading`,
  `--section-gap`) are the fastest way to fit content into the page budget.
- **Cuts** live in `variants.toml`.
- **Quality policy** lives in `resume-checks.toml`; see [rule defaults and configuration](checks.md).

## Variants

One `resume.json`, several cuts of it. Tag any entry with `x-tags`:

```json
{ "name": "ACME Corp", "position": "Engineer", "x-tags": ["full"] }
```

- An entry with **no** `x-tags` is in **every** variant — so you only tag what you want to
  conditionally drop.
- A tagged entry survives only where one of its tags is in that variant's `include` list.
- `include = ["*"]` takes everything.

This works because the JSON Resume schema sets `additionalProperties: true` throughout: the tags ride
along inside a document that still validates as a standard JSON Resume and stays readable by every
other tool in the ecosystem. `x-tags` is stripped before rendering, so themes never see it.

Bullets are the one place the schema forbids that trick — `work[].highlights` items are plain
strings, so a tag can't ride inside one. The `x-highlights` extension covers it from the entry
level: a mapping from a substring of a bullet to that bullet's tags.

```json
{
  "highlights": ["Shipped X.", "Led Y."],
  "x-highlights": { "Led Y": ["full"] }
}
```

The substring must match exactly **one** bullet; the build fails loudly if an edit to the bullet
breaks the match, because a rule that silently stopped matching would silently republish the
bullet everywhere. Like `x-tags`, `x-highlights` is stripped before rendering.

## What gets published

The published JSON is not a copy of `resume.json`: it is the *variant-filtered* document — the same
entries and bullets the published PDF shows, with the variant machinery (`x-tags`, `x-highlights`)
stripped and build provenance stamped into `meta`. A parser and a reader can never disagree about
what the CV says. The same goes for the Markdown, which exists for the places styled output cannot
go: ATS web forms, plain-text email, LLM prompts.

Besides the variant artifacts, the published site carries three discovery files:
[`index.html`](../site/index.html.j2) (the human front door, with OpenGraph link previews and
schema.org Person markup for search engines),
[`/resume.json`](https://jayteebat.github.io/my-resume/resume.json) (the guessable canonical
machine address — an alias of the primary published cut), and
[`/llms.txt`](https://jayteebat.github.io/my-resume/llms.txt) (the note an AI agent reads first,
steering it to the canonical JSON instead of scraping the styled page).

## Contributing

This repository follows [repo-standard-kit v2.0.0](https://github.com/FP-DevTools/repo-standard-kit/tree/v2.0.0),
using the `python-single` profile. See [AGENTS.md](../AGENTS.md) for the exact gate chain
and contributor responsibilities.

## Why these choices

- **Chromium, not WeasyPrint.** WeasyPrint needs MSYS2 + Pango installed by hand on Windows, which
  breaks clone-and-go. Playwright vendors its own browser.
- **Fonts are bundled** (`themes/classic/fonts/`, Source Sans 3, OFL). Relying on system fonts means
  different metrics — and so different pagination — between a local Windows build and Linux CI.
- **The schema is vendored and pinned** (`schema/`), so validation is hermetic and offline. See
  [`schema/SOURCE.md`](../schema/SOURCE.md) for provenance and how to refresh it.
- **Format checking is on.** The schema declares `format` on 11 fields (`email` and 10 `uri`s), which
  `jsonschema` ignores unless asked; those are exactly the fields where a typo is invisible on the
  page but costly in life.

## CI and publishing

Every pull request into `main` validates `resume.json`, runs the tests and builds the site, so a
broken resume fails before it can merge; `quality` and `compliance` are required checks. `dist/` is
uploaded as a workflow artifact on each PR run, for checking a PR's output before it merges. Pushes
to `main` run the same job once more on the merged result and deploy to **GitHub Pages** at
[jayteebat.github.io/my-resume](https://jayteebat.github.io/my-resume/) — a stable public URL that
needs no GitHub login, which is what you actually share with people. Pushing a feature branch
without a PR runs nothing.

The landing page is `site/index.html.j2`. Card order follows `variants.toml`, so reordering that file
reorders the page.

> **One-time setup:** Settings → Pages → Source: **GitHub Actions**. Without it the deploy job fails.

## Tests

```sh
uv run pytest              # all
uv run pytest -m 'not slow'   # skip the ones that drive a real browser
```

## Pre-commit

```sh
uv tool install pre-commit && pre-commit install
```

The hook runs `resume check --fast` when content, policy, toolkit, templates or tests
change. It reports soft-limit warnings and skips Chromium; CI runs the full
`resume check` command on the CV as well as fixture-based toolkit tests.

The standard hooks also check formatting, lint, types, Markdown, file hygiene,
secrets, and repository compliance. Run `uv run pre-commit run --all-files`
to check the whole repository.
