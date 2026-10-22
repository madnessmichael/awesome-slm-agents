# HAD — focused manuscript note

Source: [2610.02858v1](https://arxiv.org/html/2610.02858v1). Checked 2026-10-22. AI-assisted, **selected sections reviewed**: Section 3, Sections 4.1–4.5, Tables 2–4 and 8, Appendix B.1–B.2. This is not an exhaustive full-manuscript audit, human review, or reproduction.

## Mechanism and conditions

HAD contrasts teacher actions with/without harness information under student reasoning, then filters invalid preferences (§3). The harness reports state and stalls; it does not select actions.

## Anchored result

Table 2: ALFWorld unseen success is **63.43% with harness**, **40.30% without**. Table 8 specifies **134 unseen tasks**, a **30-step limit**, temperature **0.4**, and Qwen3-1.7B student/8B teacher. WebShop and ScienceWorld use 0.6B students with a 30B-A3B teacher.

## Limitations

Deployment retains harness dependencies; teacher size and training calls belong in cost accounting. Hardware and cost per successful task are not established by this note.

## Editorial next step

Evaluate stale or corrupted harness state before transferring conclusions to production. Reproduction: not run.
