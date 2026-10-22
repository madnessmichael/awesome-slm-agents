# AMD — focused manuscript note

Source: [2608.07169v1](https://arxiv.org/html/2608.07169v1). Checked 2026-10-22. AI-assisted, **selected sections reviewed**: Section 3, Section 4.1, Tables 1–3, Appendix B.3–B.4. This is not an exhaustive full-manuscript audit, human review, or reproduction.

## Mechanism and conditions

Workflow/subtask memories arrive proactively; function memory is retrieved after tool errors (§3). GPT-5-mini constructs teacher experience; retrieval uses text-embedding-3-small (§4.1).

## Anchored result

Table 1: Qwen3-4B AppWorld success increases from **14.88%** to **49.40%** on **168 test_normal tasks**; the main table averages two runs. Appendix B.3 separately studies disjoint memory construction and evaluation, so do not present the main table as that stricter protocol.

## Limitations

Training-free refers to student weight updates. Teacher trajectories, embeddings, retrieval, and longer context still incur costs. Hardware and complete cost per successful task remain unestablished here.

## Editorial next step

Measure amortized memory-building cost and performance after API-schema changes. Reproduction: not run.
