# Rethinking Scale — focused manuscript note

Source: [2604.19299v1](https://arxiv.org/html/2604.19299v1). Checked 2026-10-22. AI-assisted, **selected sections reviewed**: Sections 3–5, Tables 1–2, Appendix E. This is not an exhaustive full-manuscript audit, human review, or reproduction.

## Conditions

The study compares direct inference, single-agent ReAct, and supervisor/worker ReAct on financial tasks. Table 1 includes **SOLAR 10.7B**, despite the abstract’s under-10B framing. Section 3.4 reports **H100 80GB**, vLLM, and a **five-turn cap**.

## Anchored result

Table 2 reports **8,039.75 tokens/sample** for single-agent versus **14,618.22** for multi-agent. Its completion rate measures execution stability, not universal answer correctness. Architecture-level aggregates are not an individual-model ranking.

## Limitations

The task domain, fixed coordination, and short horizon constrain generalization (§5.3). Energy per token alone cannot establish total energy per successful task.

## Editorial next step

Repeat comparisons with longer horizons and matched task budgets. Reproduction: not run.
