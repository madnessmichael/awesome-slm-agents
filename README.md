# Awesome Small Language Model Agents

**Small Language Model Agents (SLM-Agents)** are AI systems that use a compact language model to decide what to do next while working toward a goal. The model can interpret a request, break it into steps, select tools, generate actions, and use feedback to continue, revise its approach, or stop. An agent may carry out several model calls and tool interactions before returning a result.

A typical interaction follows this loop:

**Goal → observe the current state → choose an action → execute a tool → inspect the result → continue or finish.**

For example, an agent asked to reconcile an invoice with a purchase order could retrieve the documents, call an extraction tool, use code to compare amounts, and investigate any mismatch. The language model chooses and coordinates the steps; software performs operations such as calculation, database access, and document retrieval. A small model can therefore contribute to a useful system without storing every fact or performing every operation itself.

The surrounding system matters as much as the backbone. Its main components can include:

- **Tools:** functions, APIs, search, code execution, or interface actions that let the agent retrieve information and act.
- **State and planning:** records of the current task, previous actions, and remaining steps or budget.
- **Memory:** relevant facts, past interactions, and reusable procedures retrieved when needed.
- **Feedback and recovery:** execution results, validation checks, and mechanisms for recognizing failed actions or stalled progress.
- **Coordination:** delegation to specialized agents or escalation to a stronger model when the system supports it.

There is **no universal parameter threshold** for an SLM. This collection focuses on dense backbones up to **10 billion parameters**, while including explicitly identified larger comparators and supporting work on memory or communication. For mixture-of-experts models, active parameters and total parameters describe different constraints. Small model size alone does not establish low total compute, a particular VRAM requirement, or fully local operation.

The aim is to complete useful tasks within practical limits on **cost, latency, memory, and reliability**. Smaller backbones can make specialized, frequently repeated agent decisions more economical and enable local deployment in suitable configurations. These benefits depend on the whole workflow: repeated failures, long contexts, tool calls, teacher-generated data, or a larger orchestrator can offset savings. Task success and **total cost per successful task** are therefore more informative than parameter count or price per token alone. The [SLM-agent position paper](https://arxiv.org/abs/2506.02153) motivates this direction, while [HAD](https://arxiv.org/abs/2610.02858) examines how the model learns to use the software around it.

This repository collects research on learning agent behavior, tool use, planning and recovery, memory, collaboration, and deployment with small language models.

<!-- CATALOG:START -->

## Surveys and Perspectives

- **[Small Language Models are the Future of Agentic AI](https://arxiv.org/abs/2506.02153)** (2025-06-02 · arXiv) — Argues that repeated specialized agent calls can use smaller models.

## Agent Training and Distillation

- **[Harness-Aware Distillation for Small Language Model Agents](https://arxiv.org/abs/2610.02858)** (2026-10-02 · arXiv) — Distills teacher actions conditioned on harness state and filters inconsistent preferences.
- **[From Passive Delegates to Strategic Negotiators: Reinforcing Social Reasoning in Small Language Models with SocialRL](https://arxiv.org/abs/2608.13787)** (2026-08-13 · arXiv) — Trains agents to represent a principal in negotiations with conflicting interests.
- **[AgentCPM-Explore: Realizing Long-Horizon Deep Exploration for Edge-Scale Agents](https://arxiv.org/abs/2602.06485)** (2026-02-06 · arXiv) — Combines model fusion, reward denoising, and context refinement for long-horizon exploration.

## Planning and Error Recovery

- **[Progress-Aware Distillation for Mitigating Stagnation in Small Language Model Agents](https://arxiv.org/abs/2610.19439)** (2026-10-14 · [NeurIPS 2026; accepted, author-reported](https://arxiv.org/abs/2610.19439)) — Detects stalled trajectories and uses an adaptive distillation penalty.
- **[PACE: Two-Timescale Self-Evolution for Small Language Model Agents](https://arxiv.org/abs/2605.23019)** (2026-05-21 · arXiv) — Separates prompt refinement from control-logic changes accepted through held-out validation.

## Memory and Context Management

- **[Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory](https://arxiv.org/abs/2608.07169)** (2026-08-07 · arXiv) — Transfers teacher experience into workflow, subtask, and function memories without student weight updates.
- **[Lightweight LLM Agent Memory with Small Language Models](https://arxiv.org/abs/2604.07798)** (2026-04-09 · [ACL 2026 Main Conference (Long Papers)](https://aclanthology.org/2026.acl-long.588/)) — Uses small models for modular memory retrieval, writing, and offline long-term consolidation.
- **[LightMem: Lightweight and Efficient Memory-Augmented Generation](https://arxiv.org/abs/2510.18866)** (2025-10-21 · [ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a05b72653ec5b473732129829ae04195-Abstract-Conference.html)) — Organizes memory into sensory, short-term, and long-term stages with offline consolidation.

## Multi-Agent Collaboration

- **[Reinforcement Learning of Communication in a Mesh of Small Language Models](https://arxiv.org/abs/2609.30578)** (2026-09-24 · arXiv) — Learns confidence-gated communication and decentralized revision.
- **[Can Small Agents Collaborate to Beat a Single Large Language Model?](https://arxiv.org/abs/2601.11327)** (2026-01-16 · [ICLR 2026 · MALGAI Workshop](https://openreview.net/pdf?id=RLHUTcvsA9)) — Studies a central orchestrator with specialized workers and restricted communication.
- **[Latent-Lens: Visual Perception in Small Language Models Through Latent Communication](https://neurips.cc/virtual/2026/loc/sydney/poster/155307)** ([NeurIPS 2026 Poster](https://neurips.cc/virtual/2026/loc/sydney/poster/155307)) — Connects a VLM and an SLM through a lightweight latent-state codec instead of text messages.

## On-Device and Edge Deployment

- **[Fara-7B: An Efficient Agentic Model for Computer Use](https://arxiv.org/abs/2511.19663)** (2025-11-24 · arXiv) — Trains a screenshot-based computer-use agent from filtered synthetic web trajectories.

## Benchmarks and Evaluation

- **[Rethinking Scale: Deployment Trade-offs of Small Language Models under Agent Paradigms](https://arxiv.org/abs/2604.19299)** (2026-04-21 · [ACL 2026 Industry Track](https://aclanthology.org/2026.acl-industry.123/)) — Compares base models, tool-equipped single agents, and multi-agent systems.

<!-- CATALOG:END -->

## Contributing

Suggestions and corrections are welcome. Read the [contribution guide](CONTRIBUTING.md). Paper metadata is maintained in [data/papers.yaml](data/papers.yaml).

## License

[CC BY 4.0 for original documentation; MIT for scripts](LICENSE). Third-party works retain their own licenses.
