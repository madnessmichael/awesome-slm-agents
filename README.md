# Awesome Small Language Model Agents

A collection of papers on small language models for agentic systems: training, planning, memory, collaboration, and deployment.

Focus: models up to **10B parameters**, with labeled exceptions. **11 papers** · Metadata and abstracts checked **2026-10-22** · AI-assisted summaries; no reproductions.

## Contents

- [Surveys and Perspectives](#surveys-and-perspectives)
- [Agent Training and Distillation](#agent-training-and-distillation)
- [Planning and Error Recovery](#planning-and-error-recovery)
- [Memory and Context Management](#memory-and-context-management)
- [Multi-Agent Collaboration](#multi-agent-collaboration)
- [On-Device and Edge Deployment](#on-device-and-edge-deployment)
- [Benchmarks and Evaluation](#benchmarks-and-evaluation)
- [Reading Guides](#reading-guides)
- [Contributing](#contributing)

## Papers

Newest first within each category. Dates refer to first publication. See the [detailed catalog](docs/paper-catalog.md) for model sizes, evidence, limitations, and publication status.

<!-- CATALOG:START -->

### Surveys and Perspectives

- **[Small Language Models are the Future of Agentic AI](https://arxiv.org/abs/2506.02153)** (2025-06-02) — Argues that repeated specialized agent calls can use smaller models.

### Agent Training and Distillation

- **[Harness-Aware Distillation for Small Language Model Agents](https://arxiv.org/abs/2610.02858)** (2026-10-02) — Distills teacher actions conditioned on harness state and filters inconsistent preferences.
- **[From Passive Delegates to Strategic Negotiators: Reinforcing Social Reasoning in Small Language Models with SocialRL](https://arxiv.org/abs/2608.13787)** (2026-08-13) — Trains agents to represent a principal in negotiations with conflicting interests.
- **[AgentCPM-Explore: Realizing Long-Horizon Deep Exploration for Edge-Scale Agents](https://arxiv.org/abs/2602.06485)** (2026-02-06) — Combines model fusion, reward denoising, and context refinement for long-horizon exploration.

### Planning and Error Recovery

- **[Progress-Aware Distillation for Mitigating Stagnation in Small Language Model Agents](https://arxiv.org/abs/2610.19439)** (2026-10-14) — Detects stalled trajectories and uses an adaptive distillation penalty.
- **[PACE: Two-Timescale Self-Evolution for Small Language Model Agents](https://arxiv.org/abs/2605.23019)** (2026-05-21) — Separates prompt refinement from control-logic changes accepted through held-out validation.

### Memory and Context Management

- **[Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory](https://arxiv.org/abs/2608.07169)** (2026-08-07) — Transfers teacher experience into workflow, subtask, and function memories without student weight updates.

### Multi-Agent Collaboration

- **[Reinforcement Learning of Communication in a Mesh of Small Language Models](https://arxiv.org/abs/2609.30578)** (2026-09-24) — Learns confidence-gated communication and decentralized revision.
- **[Can Small Agents Collaborate to Beat a Single Large Language Model?](https://arxiv.org/abs/2601.11327)** (2026-01-16) — Studies a central orchestrator with specialized workers and restricted communication.

### On-Device and Edge Deployment

- **[Fara-7B: An Efficient Agentic Model for Computer Use](https://arxiv.org/abs/2511.19663)** (2025-11-24) — Trains a screenshot-based computer-use agent from filtered synthetic web trajectories.

### Benchmarks and Evaluation

- **[Rethinking Scale: Deployment Trade-offs of Small Language Models under Agent Paradigms](https://arxiv.org/abs/2604.19299)** (2026-04-21) — Compares base models, tool-equipped single agents, and multi-agent systems.

<!-- CATALOG:END -->

## Reading Guides

- [Where to start](docs/reading-guide.md)
- [How to evaluate SLM agents](docs/evaluation-guide.md)
- [Applications and research directions](docs/applications-and-outlook.md)
- [Scope and selection criteria](docs/scope.md)

## Contributing

Suggestions and corrections are welcome. Read the [contribution guide](CONTRIBUTING.md). Paper metadata is maintained in [data/papers.yaml](data/papers.yaml).

## License

[CC BY 4.0 for original documentation; MIT for scripts](LICENSE). Third-party works retain their own licenses.
