# my-resume

My CV as data. [`resume.json`](resume.json) is the single source of truth — a standard
[JSON Resume](https://jsonresume.org/) document — and this toolchain renders it to styled PDF and
HTML.

```sh
uv sync
uv run playwright install chromium   # one-time, ~150MB

uv run resume build                  # -> dist/resume-{full,short}.{pdf,html}
```

## Commands

| Command | Does |
|---|---|
| `uv run resume validate` | Check `resume.json` against the schema |
| `uv run resume variants` | List the variants defined in `variants.toml` |
| `uv run resume build` | Render every variant to `dist/` |
| `uv run resume build -v short -f pdf` | Render one variant, one format |
| `uv run resume serve` | Browser preview, live-reloads on edit |

`serve` is the one to use while restyling: edit `themes/classic/style.css` and the page reloads.

## How it fits together

```
resume.json ──validate (schema)──> apply variant (x-tags) ──> Jinja2 + theme ──> HTML
                                                                                  │
                                                                     Chromium print-to-PDF
                                                                                  ↓
                                                                        dist/resume-*.pdf
```

- **Content** lives in `resume.json`. Nothing else should carry CV facts.
- **Styling** lives in `themes/classic/style.css`. The template carries structure only, so restyling
  never means touching HTML. The tokens at the top of the stylesheet (`--size-base`, `--leading`,
  `--section-gap`) are the fastest way to fit content onto one page.
- **Cuts** live in `variants.toml`.

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

*Known limitation:* `work[].highlights` is an array of plain strings per the schema, so individual
bullets can't be tagged — variant filtering is per-entry. Trimming bullets for the short cut would
need an `x-highlights` extension.

## Why these choices

- **Chromium, not WeasyPrint.** WeasyPrint needs MSYS2 + Pango installed by hand on Windows, which
  breaks clone-and-go. Playwright vendors its own browser.
- **Fonts are bundled** (`themes/classic/fonts/`, Source Sans 3, OFL). Relying on system fonts means
  different metrics — and so different pagination — between a local Windows build and Linux CI.
- **The schema is vendored and pinned** (`schema/`), so validation is hermetic and offline. See
  [`schema/SOURCE.md`](schema/SOURCE.md) for provenance and how to refresh it.
- **Format checking is on.** The schema declares `format` on 11 fields (`email` and 10 `uri`s), which
  `jsonschema` ignores unless asked; those are exactly the fields where a typo is invisible on the
  page but costly in life.

## CI

Every push validates `resume.json`, runs the tests, and builds all variants, uploading `dist/` as a
workflow artifact — so there is always a fresh PDF to download, and a broken resume fails loudly.

## Tests

```sh
uv run pytest              # all
uv run pytest -m 'not slow'   # skip the ones that drive a real browser
```
