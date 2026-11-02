# ADR 0006: Backend repositioning

## Status

Accepted. 2026-11-02.

## Context

[Issue #35](https://github.com/JayTeeBat/my-resume/issues/35) proposes a software-first
CV for battery-analytics, BMS-software, fleet-telematics and energy-storage
software employers. The owner approved the wording and the scope below.
This refines the coverage policy in [ADR 0005](0005-published-versions-and-page-layout.md).

## Decision

- Position as a backend software engineer with battery depth. Order skills for
  software readers, retain battery depth in one Domain line, and list only
  evidenced skills (`skill_evidence` checks the two-page and full cuts).
- Lead the two-sentence profile summary with backend work, then battery
  experience (not enforced: `lengths` and `summary_sentences = 1` govern
  work-entry summaries only).
- Keep separate pre-2020 roles and their summaries, with one highlight each in
  the two-page cut; retain all detail in full (`role_highlights` date bands).
- The one-page cut is retired (see the 2026-11-02 amendment to ADR 0005).
- Keep internships and CPGE in the private full cut: owner decision, deviating
  from issue #35. Keep SharePoint full-only.
- Deliberately add no Projects section: owner decision.
- The owner will update the LinkedIn headline/title to match; not enforced here.

## Consequences

The CV emphasises demonstrated backend delivery without adding unsupported
metrics or skills. Public coverage stays two pages, and full remains the
detailed archive.
LinkedIn and later issue #35 items remain open.
