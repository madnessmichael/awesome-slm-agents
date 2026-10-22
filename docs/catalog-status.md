# Catalog and implementation status

Snapshot: 2026-10-22. This document reports delivered artifacts, not an automatically maintained literature survey.

## Current coverage

| Category | Entries |
|---|---:|
| Surveys and Perspectives | 1 |
| Agent Training and Distillation | 5 |
| Tool Use and Structured Actions | 4 |
| Planning and Error Recovery | 2 |
| Memory and Context Management | 1 |
| Multi-Agent Collaboration | 2 |
| Hybrid Systems and Routing | 2 |
| On-Device and Edge Deployment | 4 |
| Benchmarks and Evaluation | 4 |
| **Total** | **25** |

Five [focused notes](../notes/README.md) inspect primary manuscript methods/results and selected appendices. All five preserve `full_text_reviewed=false`, `human_reviewed=false`, and `reproduced=false`. `manuscript_sections_reviewed=true` records the narrower work actually done. TinyAgent's note uses v1 while catalog metadata tracks v3; the two version fields are separate.

## Milestones

| Milestone | Status | Evidence / remaining work |
|---|---|---|
| M0: repository and editorial policies | Delivered | Scope, taxonomy, licenses, contribution process |
| M1: primary-source seed catalog | Delivered | Initial 11 records, expanded to 25 |
| M2: 20–30 selected entries | Count target delivered | 25 entries; discovery did not claim an exhaustive 40–60-candidate screening |
| M3: 5–8 exhaustive full-text notes | Partial | Five focused notes delivered; exhaustive manuscript/appendix audits and human review remain open |
| M4: metadata and publication tooling | Implemented | Nested schema, semantic invariants, renderer, basic Markdown/local-link checks, pinned Actions, bounded link retries |
| M5: final editorial release | Open | Review unresolved metadata, deepen notes, complete publication/resource checks |

The candidate decision log is a small recorded set of decisions, not an assertion that every relevant paper was screened. The schema keyword validator intentionally supports the keywords used by the checked-in schema; it rejects unsupported keywords rather than silently ignoring them. It is not a general JSON Schema implementation.

## Corrections discovered during manuscript reading

- Rethinking Scale's under-10B framing has a Table 1 exception: SOLAR 10.7B. Its completion metric must not be read as answer accuracy.
- HAD uses a 30B-A3B teacher for two environments; small students do not imply small training dependencies.
- AMD's main results and disjoint-memory protocols are distinct; memory construction is not cost-free.
- TinyAgent's graph-plan success and planner latency do not establish unrestricted task completion or total system memory.
- Original τ-bench uses **pass^k** for consistency across repeated trials; this differs from best-of-k **pass@k**.

These are source-specific reading observations, not new experimental findings. See the linked catalog entries and notes for the primary sources.

## Next editorial work

1. Finish full manuscript reviews, including limits, additional experiments and resource appendices, before promoting review flags.
2. Verify model/weights/data URLs and licensing, with pinned revisions for reproduction candidates.
3. Review routing papers under matched attempts and tool budgets; do not merge their headline scores.
4. Resolve OR-Toolformer's source-reported submission date versus identifier-month discrepancy; preserve both without silently guessing.
5. Add independently reviewed corrections and a changelog for revised scientific annotations.

No paid API usage or GPU experiment is needed for these catalog tasks. No reproduction has been started.
