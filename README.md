# Awesome Small Language Model Agents

A research reading resource on small language models for agentic systems: training, tools, recovery, memory, collaboration, evaluation, and deployment.

**Initial release:** 11 selected papers (10 recent method/application studies plus one foundational perspective). Primary-source metadata and abstracts checked on **2026-10-22**. Entries are **AI-assisted editorial summaries**, not full-text peer reviews or reproductions. This is a selective snapshot, not an exhaustive or automatically current bibliography.

## Start here

- [Scope and inclusion policy](docs/scope.md) · [Taxonomy](docs/taxonomy.md)
- [Reading guide](docs/reading-guide.md) · [Applications and outlook](docs/applications-and-outlook.md)
- [Evaluation guide](docs/evaluation-guide.md) · [Structured paper data](data/papers.yaml)
- [Detailed implementation plan, milestones and estimates — Vietnamese](docs/IMPLEMENTATION_PLAN_VI.md)
- [Contributing](CONTRIBUTING.md) · [Review-note template](notes/TEMPLATE.md)

## What counts as an SLM agent?

An agent observes state, chooses tools or actions, uses feedback, and continues or stops. We focus on dense backbones up to **10B parameters**, with labeled exceptions for mixed-size studies. Report total and active parameters separately for MoE. Small parameter count does not establish low total compute, a specific VRAM requirement, offline operation, or absence of a larger teacher.

The practical objective is reliable task completion under a budget. Evaluate **cost per successful task**, latency, recovery and tool validity alongside accuracy. Software, context and memory are part of the system being evaluated.

## How to read this list

Each paper has a contribution, author-reported evidence, and editorial limitation. Dates refer to first publication; revisions are stored separately. `Core`, `supporting`, and `background` express scope, not quality. Null fields mean not established in this review. Published resources are not labeled reproduced. There is no cross-paper leaderboard.

## Paper catalog

<!-- CATALOG:START -->

### Surveys and Perspectives

Why use small models in agents?

- **[Small Language Models are the Future of Agentic AI](https://arxiv.org/abs/2506.02153)** — Peter Belcak et al.; first published 2025-06-02. `background`
  - Models: Conceptual; heterogeneous sizes. Reviewed source: v3; metadata + abstract only.
  - Contribution: Argues that repeated specialized agent calls can use smaller models.
  - Evidence: A position paper motivated by capabilities, architecture, and deployment economics.
  - Limitation: An architectural argument is not a universal empirical demonstration of cheaper successful tasks.
  - Status: preprint. Checked 2026-10-22.

### Agent Training and Distillation

Which agent capabilities should be learned?

- **[Harness-Aware Distillation for Small Language Model Agents](https://arxiv.org/abs/2610.02858)** — Moonseok Choi et al.; first published 2026-10-02. `core`
  - Models: Not established from abstract. Reviewed source: v1; metadata + abstract only.
  - Contribution: Distills teacher actions conditioned on harness state and filters inconsistent preferences.
  - Evidence: Authors compare long-horizon agents with a fixed harness and report fewer unproductive loops.
  - Limitation: Model sizes, benchmark-level results, and teacher costs require full-text review.
  - Status: preprint. Checked 2026-10-22.

- **[From Passive Delegates to Strategic Negotiators: Reinforcing Social Reasoning in Small Language Models with SocialRL](https://arxiv.org/abs/2608.13787)** — Wenyue Hua et al.; first published 2026-08-13. `core`
  - Models: 4B. Reviewed source: v1; metadata + abstract only.
  - Contribution: Trains agents to represent a principal in negotiations with conflicting interests.
  - Evidence: The abstract describes six domains and cross-domain policy evaluation.
  - Limitation: Controlled negotiation outcomes do not establish real-world delegation reliability.
  - Status: preprint. Checked 2026-10-22.

- **[AgentCPM-Explore: Realizing Long-Horizon Deep Exploration for Edge-Scale Agents](https://arxiv.org/abs/2602.06485)** — Haotian Chen et al.; first published 2026-02-06. `core`
  - Models: 4B. Reviewed source: v1; metadata + abstract only.
  - Contribution: Combines model fusion, reward denoising, and context refinement for long-horizon exploration.
  - Evidence: The abstract reports benchmark comparisons and a GAIA text result under pass@64.
  - Limitation: pass@64 is not single-run reliability; local model size does not imply local tools or cheap training.
  - Status: preprint. Checked 2026-10-22.

### Tool Use and Structured Actions

How do agents select tools and valid arguments?

No entries selected yet; contributions with primary evidence are welcome.

### Planning and Error Recovery

How do agents detect failure and resume progress?

- **[Progress-Aware Distillation for Mitigating Stagnation in Small Language Model Agents](https://arxiv.org/abs/2610.19439)** — Yuanpu Cao et al.; first published 2026-10-14. `core`
  - Models: 0.6–8B. Reviewed source: v2; metadata + abstract only.
  - Contribution: Detects stalled trajectories and uses an adaptive distillation penalty.
  - Evidence: Authors evaluate eight small models on in-domain and out-of-domain tasks.
  - Limitation: Abstract review cannot establish fair total compute or robustness in production.
  - Status: NeurIPS 2026 (arXiv author comment; proceedings not independently checked). Checked 2026-10-22.

- **[PACE: Two-Timescale Self-Evolution for Small Language Model Agents](https://arxiv.org/abs/2605.23019)** — Chen Ling et al.; first published 2026-05-21. `core`
  - Models: 4–14B; includes models above scope threshold. Reviewed source: v1; metadata + abstract only.
  - Contribution: Separates prompt refinement from control-logic changes accepted through held-out validation.
  - Evidence: Authors use three frozen backbones, controlled tasks, and a tau-bench case study.
  - Limitation: Some models exceed 10B; validation costs and domain transfer need deeper review.
  - Status: preprint. Checked 2026-10-22.

### Memory and Context Management

What belongs in weights, context, or external memory?

- **[Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory](https://arxiv.org/abs/2608.07169)** — Taeil Kim et al.; first published 2026-08-07. `core`
  - Models: 4–8B. Reviewed source: v1; metadata + abstract only.
  - Contribution: Transfers teacher experience into workflow, subtask, and function memories without student weight updates.
  - Evidence: Authors evaluate AppWorld, BFCL V3, and ToolSandbox using four small students.
  - Limitation: Teacher-generated memory has construction cost; training-free does not mean cost-free.
  - Status: preprint. Checked 2026-10-22.

### Multi-Agent Collaboration

When does communication justify its overhead?

- **[Reinforcement Learning of Communication in a Mesh of Small Language Models](https://arxiv.org/abs/2609.30578)** — Mehmet Kerem Turkcan; first published 2026-09-24. `core`
  - Models: Includes 0.8B and 3B. Reviewed source: v1; metadata + abstract only.
  - Contribution: Learns confidence-gated communication and decentralized revision.
  - Evidence: The abstract compares communication against independent sampling and studies corrupted messages.
  - Limitation: Agent count and communication costs must accompany any accuracy comparison.
  - Status: preprint. Checked 2026-10-22.

- **[Can Small Agents Collaborate to Beat a Single Large Language Model?](https://arxiv.org/abs/2601.11327)** — Agata Żywot et al.; first published 2026-01-16. `supporting`
  - Models: Not established from reviewed abstract. Reviewed source: v2; metadata + abstract only.
  - Contribution: Studies a central orchestrator with specialized workers and restricted communication.
  - Evidence: Authors find that reasoning at the orchestrator matters more than at workers.
  - Limitation: Inspect orchestrator size and matched inference budgets before crediting small workers.
  - Status: preprint. Checked 2026-10-22.

### Hybrid Systems and Routing

When should a small agent escalate?

No entries selected yet; contributions with primary evidence are welcome.

### On-Device and Edge Deployment

What can run locally under actual hardware limits?

- **[Fara-7B: An Efficient Agentic Model for Computer Use](https://arxiv.org/abs/2511.19663)** — Ahmed Awadallah et al.; first published 2025-11-24. `core`
  - Models: 7B. Reviewed source: v1; metadata + abstract only.
  - Contribution: Trains a screenshot-based computer-use agent from filtered synthetic web trajectories.
  - Evidence: Authors evaluate WebVoyager, Online-Mind2Web, and WebTailBench.
  - Limitation: An on-device-capable model does not establish offline operation or fit on any specific GPU.
  - Status: preprint. Checked 2026-10-22.

### Benchmarks and Evaluation

What is the cost of completing a task correctly?

- **[Rethinking Scale: Deployment Trade-offs of Small Language Models under Agent Paradigms](https://arxiv.org/abs/2604.19299)** — Xinlin Wang et al.; first published 2026-04-21. `core`
  - Models: <10B. Reviewed source: v1; metadata + abstract only.
  - Contribution: Compares base models, tool-equipped single agents, and multi-agent systems.
  - Evidence: Authors report the best performance–cost balance for the single-agent setup studied.
  - Limitation: A setting-specific negative finding does not establish that collaboration never helps.
  - Status: preprint. Checked 2026-10-22.

<!-- CATALOG:END -->

## Contrasting and negative findings

Read Rethinking Scale alongside the collaboration and TalkMesh studies. Their settings differ: an improvement from communication in one setup does not establish that adding workers is economical in another. Inspect the orchestrator, tools, attempts, and total cost before comparing conclusions.

## Coverage gaps and next milestones

Dedicated tool-use and routing entries, older foundational agent work, detailed hardware profiles, and full-text evaluation-condition notes need further curation. The next milestone targets 20–30 entries and 5–8 full-text notes, subject to primary-source review. No automatic ongoing monitoring is currently running.

## Maintenance and provenance

Metadata is the source of truth; the catalog is generated with `python3 scripts/render.py`. CI checks structure and catalog synchronization. Scheduled link checks report reachability only; they do not verify claims or update review dates. AI assistance is disclosed; no human-review status or central Awesome-list affiliation is claimed.

Original editorial content: CC BY 4.0; scripts: MIT. Third-party works retain their own licenses. See [LICENSE](LICENSE).
