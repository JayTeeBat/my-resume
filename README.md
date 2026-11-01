# my-resume

See the [standards register](docs/standards.md) for scope and enforcement.

**[View my CV →](https://jayteebat.github.io/my-resume/)**

## Overview

My CV, maintained as code. A single [JSON Resume](https://jsonresume.org/) file,
[`resume.json`](resume.json), renders to HTML, PDF, JSON and Markdown with
[resume-toolkit](https://github.com/JayTeeBat/resume-toolkit). Every change is
checked in CI for structure, style and length. Only the two-page version is
published; one-page and full copies are available from the workflow artifacts.

## Install

Requires Python 3.13+ and [uv](https://docs.astral.sh/uv/).

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

Editing, checks, publishing and toolkit upgrades are in
[docs/development.md](docs/development.md); contributor and agent rules are in
[AGENTS.md](AGENTS.md). Rendering and check rules are documented in the
[resume-toolkit docs](https://github.com/JayTeeBat/resume-toolkit/tree/9cd24f998df7d0c0d7a709cadc424d2c96723af1/docs).

## License

CV content (`resume.json` and everything rendered from it): © Jacques Thomazo,
all rights reserved. Repository configuration and workflow files: [MIT](LICENSE).
