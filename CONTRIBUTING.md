# Contributing

1. Search existing IDs and versions. Propose primary sources, not aggregator summaries.
2. Explain core/supporting/background fit and choose one category.
3. Add an entry to `data/papers.yaml` (JSON syntax, a YAML 1.2 subset; standard-library parsing).
4. Supply contribution, evidence and limitation; distinguish author claims from reviewer interpretation.
5. Preserve first-publication date; a revision does not make a paper newly published.
6. Set verification flags truthfully. Identify human reviewers only with their consent. Never mark reproduced based on code availability.
7. Run the renderer to update the README catalog. The CI validator checks metadata structure and generated content; it does not validate scientific claims.

Use null for information not established. Add source page/table and version for numerical claims. Link resources only when verified; do not guess GitHub URLs. Corrections and negative findings are welcome. Do not upload publisher PDFs, private corpus snapshots, credentials, reviewer identities, or copied full abstracts.

AI assistance is permitted with disclosure, primary-source comparison, and accurate review labels. Maintainers remain responsible for acceptance. Do not present an AI-only review as human reading. A maintainer must inspect changes before merge; repository protection settings are not assumed to enforce this.

Useful commands: `python3 scripts/render.py`, `python3 scripts/validate.py`, `python3 scripts/check_markdown.py`. A focused manuscript note must list reviewed sections, version and source locators; it does not qualify as an exhaustive full-text review. Link checking is a separate, non-blocking scheduled/manual job; temporary failures are review alerts, never automatic deletion.
