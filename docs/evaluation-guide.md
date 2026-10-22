# Evaluation guide

Do not construct a cross-paper leaderboard from unmatched experiments.

| Record | Why it matters |
|---|---|
| Model/revision; total and active parameters | Identifies the actual backbone and MoE storage |
| Agent harness/version; tools; context | Separates software capabilities from model changes |
| Dataset/split; contamination checks | Defines what generalization means |
| pass@1, pass@k, seeds and task count | Distinguishes reliability from repeated search |
| Tool-call validity and task success | Valid JSON does not imply a completed task |
| Token/action/retry/timeout budget | Avoids hidden inference scaling |
| Teacher role during data generation and inference | Exposes larger-model dependencies |
| Hardware/count; precision; memory semantics | Allows realistic deployment interpretation |
| End-to-end latency p50/p95 and total task cost | Captures retries and tools as well as generation |
| Training, memory-building, inference and tool costs | Prevents treating free weights as a free system |
| Out-of-domain and recovery results | Distinguishes specialization from robustness |
| Code/model/data availability and licenses | Availability does not establish reproducibility |

Cost per successful task = total cost of **all** evaluation attempts / successful tasks. Zero successes yields an undefined ratio; report total cost and zero successes explicitly. Amortize setup cost only with an explicit workload volume. Record energy measurement boundaries; GPU rail power is not wall-system power.

For every quantitative claim, record source version and page/table, denominator, baseline, setting, and whether the difference is percentage points or relative percent. Never infer performance from GPU name or combine unified memory with discrete VRAM.

A reproduction requires pinned code/model/data versions, hardware/software manifest, exact commands, seeds, raw outputs, task counts, metric computation, and deviations from the paper. No entry currently meets that bar in this repository.

## Repeated-trial metric notation

Original [τ-bench](https://arxiv.org/abs/2406.12045) uses **pass^k** to measure consistent success across repeated trials. This differs from **pass@k**, which measures finding a successful attempt within a set of attempts. Preserve the paper’s notation and estimator; do not use the two interchangeably.
