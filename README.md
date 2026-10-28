# my-resume

**[View my CV →](https://jayteebat.github.io/my-resume/)**

## Overview

My CV, maintained as code. A single [JSON Resume](https://jsonresume.org/) file,
[`resume.json`](resume.json), renders to HTML, PDF, JSON and Markdown. Every change
is checked in CI for structure, style and length, then published automatically.

## Install

```sh
uv sync
uv run playwright install chromium
```

## Usage

```sh
uv run resume serve    # live preview at localhost:8000
uv run resume build    # render every variant to dist/
uv run resume check    # run the content checks
```

## Development

Toolchain internals (variants, theme, CI, design choices) are in
[docs/development.md](docs/development.md); content-check rules are in
[docs/checks.md](docs/checks.md); contributor and agent rules are in
[AGENTS.md](AGENTS.md). The repository follows
[repo-standard-kit v2.0.0](https://github.com/FP-DevTools/repo-standard-kit/tree/v2.0.0).

## License

Code: [MIT](LICENSE). CV content (`resume.json` and everything rendered from it):
© Jacques Thomazo, all rights reserved. Bundled fonts keep their own OFL license.
