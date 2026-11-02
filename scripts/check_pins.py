"""Check the one pinned toolkit-docs link against the pin in pyproject.toml.

Every other file links to that section instead, so a second pinned link fails.
"""

import re
import subprocess
import sys
import tomllib
from pathlib import Path

REGISTER = "docs/standards.md"
LINK = re.compile(r"resume-toolkit/(?:tree|blob)/([^/\s)]+)")


def toolkit_pin() -> str:
    deps = tomllib.loads(Path("pyproject.toml").read_text())["project"]["dependencies"]
    for dep in deps:
        name, _, url = dep.partition("@")
        if name.strip() == "resume-toolkit":
            return url.rpartition("@")[2].strip()
    sys.exit("pyproject.toml: no resume-toolkit dependency — add it with a pinned @<ref>")


def register_errors(pin: str) -> list[str]:
    refs = LINK.findall(Path(REGISTER).read_text())
    if len(refs) != 1:
        return [f"{REGISTER}: {len(refs)} pinned toolkit docs links — keep exactly one, at {pin}"]
    if refs[0] != pin:
        return [f"{REGISTER}: toolkit docs link uses {refs[0]}, pyproject.toml pins {pin} — update the link to {pin}"]
    return []


def duplicate_errors() -> list[str]:
    tracked = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True).stdout.splitlines()
    errors = []
    for path in tracked:
        try:
            text = Path(path).read_text()
        except (UnicodeDecodeError, FileNotFoundError):
            continue  # binary or deleted in the working tree
        if path != REGISTER and LINK.search(text):
            errors.append(f"{path}: pinned toolkit docs link — link to {REGISTER}#toolkit-documentation instead")
    return errors


if __name__ == "__main__":
    problems = register_errors(toolkit_pin()) + duplicate_errors()
    for problem in problems:
        print(problem)
    sys.exit(1 if problems else 0)
