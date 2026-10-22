# ProD — focused manuscript note

Source: [2610.19439v2](https://arxiv.org/html/2610.19439v2). Checked 2026-10-22. AI-assisted, **selected sections reviewed**: Sections 2–4, Table 3, Appendix B, NeurIPS checklist: statistical significance. This is not an exhaustive full-manuscript audit, human review, or reproduction.

## Mechanism and conditions

Stagnation gaps adjust a trajectory preference margin alongside SFT. CodeAct students use greedy decoding and a ten-turn horizon (§§3–4). GPT-4.1 supplies successful demonstrations.

## Anchored result

Table 3: Qwen3-4B HotpotQA accuracy rises from **66.6% (SFT)** to **70.8% (ProD)**; §4.1 specifies **500 hard questions**. This is +4.2 percentage points, not a 4.2% relative gain.

## Compute and limitations

Appendix B reports single A100 80GB and H200 “140GB” devices; retain the paper’s wording without silently replacing it with product specifications. Task/device assignment and whole-study device-hours remain unestablished here. The checklist acknowledges missing error bars.

## Editorial next step

Compare against progress signals based on environment state under matched rollout and teacher budgets. Reproduction: not run.
