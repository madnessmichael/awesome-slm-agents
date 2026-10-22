# Detailed paper catalog

[Back to the list](../README.md) · [Structured metadata](../data/papers.yaml)

AI-assisted summaries based on primary metadata and abstracts. Evidence below is author-reported; no full-text review or reproduction is claimed. Dates are first-publication dates. `core`, `supporting`, and `background` describe scope, not quality.

## Surveys and Perspectives

Why use small models in agents?

### SLM agent position paper

**[Small Language Models are the Future of Agentic AI](https://arxiv.org/abs/2506.02153)** — Peter Belcak et al.; 2025-06-02. `background`

- **Models:** Conceptual; heterogeneous sizes.
- **Contribution:** Argues that repeated specialized agent calls can use smaller models.
- **Evidence:** A position paper motivated by capabilities, architecture, and deployment economics.
- **Limitation:** An architectural argument is not a universal empirical demonstration of cheaper successful tasks.
- **Status:** arXiv.
- **Source review:** v3; metadata and abstract, checked 2026-10-22.

## Agent Training and Distillation

Which agent capabilities should be learned?

### HAD

**[Harness-Aware Distillation for Small Language Model Agents](https://arxiv.org/abs/2610.02858)** — Moonseok Choi et al.; 2026-10-02. `core`

- **Models:** Not established from abstract.
- **Contribution:** Distills teacher actions conditioned on harness state and filters inconsistent preferences.
- **Evidence:** Authors compare long-horizon agents with a fixed harness and report fewer unproductive loops.
- **Limitation:** Model sizes, benchmark-level results, and teacher costs require full-text review.
- **Status:** arXiv.
- **Source review:** v1; metadata and abstract, checked 2026-10-22.

### SocialRL

**[From Passive Delegates to Strategic Negotiators: Reinforcing Social Reasoning in Small Language Models with SocialRL](https://arxiv.org/abs/2608.13787)** — Wenyue Hua et al.; 2026-08-13. `core`

- **Models:** 4B.
- **Contribution:** Trains agents to represent a principal in negotiations with conflicting interests.
- **Evidence:** The abstract describes six domains and cross-domain policy evaluation.
- **Limitation:** Controlled negotiation outcomes do not establish real-world delegation reliability.
- **Status:** arXiv.
- **Source review:** v1; metadata and abstract, checked 2026-10-22.

### AgentCPM-Explore

**[AgentCPM-Explore: Realizing Long-Horizon Deep Exploration for Edge-Scale Agents](https://arxiv.org/abs/2602.06485)** — Haotian Chen et al.; 2026-02-06. `core`

- **Models:** 4B.
- **Contribution:** Combines model fusion, reward denoising, and context refinement for long-horizon exploration.
- **Evidence:** The abstract reports benchmark comparisons and a GAIA text result under pass@64.
- **Limitation:** pass@64 is not single-run reliability; local model size does not imply local tools or cheap training.
- **Status:** arXiv.
- **Source review:** v1; metadata and abstract, checked 2026-10-22.

## Planning and Error Recovery

How do agents detect failure and resume progress?

### ProD

**[Progress-Aware Distillation for Mitigating Stagnation in Small Language Model Agents](https://arxiv.org/abs/2610.19439)** — Yuanpu Cao et al.; 2026-10-14. `core`

- **Models:** 0.6–8B.
- **Contribution:** Detects stalled trajectories and uses an adaptive distillation penalty.
- **Evidence:** Authors evaluate eight small models on in-domain and out-of-domain tasks.
- **Limitation:** Abstract review cannot establish fair total compute or robustness in production.
- **Status:** [NeurIPS 2026; accepted, author-reported](https://arxiv.org/abs/2610.19439).
- **Source review:** v2; metadata and abstract, checked 2026-10-22.

### PACE

**[PACE: Two-Timescale Self-Evolution for Small Language Model Agents](https://arxiv.org/abs/2605.23019)** — Chen Ling et al.; 2026-05-21. `core`

- **Models:** 4–14B; includes models above scope threshold.
- **Contribution:** Separates prompt refinement from control-logic changes accepted through held-out validation.
- **Evidence:** Authors use three frozen backbones, controlled tasks, and a tau-bench case study.
- **Limitation:** Some models exceed 10B; validation costs and domain transfer need deeper review.
- **Status:** arXiv.
- **Source review:** v1; metadata and abstract, checked 2026-10-22.

## Memory and Context Management

What belongs in weights, context, or external memory?

### AMD

**[Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory](https://arxiv.org/abs/2608.07169)** — Taeil Kim et al.; 2026-08-07. `core`

- **Models:** 4–8B.
- **Contribution:** Transfers teacher experience into workflow, subtask, and function memories without student weight updates.
- **Evidence:** Authors evaluate AppWorld, BFCL V3, and ToolSandbox using four small students.
- **Limitation:** Teacher-generated memory has construction cost; training-free does not mean cost-free.
- **Status:** arXiv.
- **Source review:** v1; metadata and abstract, checked 2026-10-22.

### LightMem (ACL 2026)

**[Lightweight LLM Agent Memory with Small Language Models](https://arxiv.org/abs/2604.07798)** — Jiaquan Zhang et al.; 2026-04-09. `core`

- **Models:** Small models for memory operations; sizes not established from abstract.
- **Contribution:** Uses small models for modular memory retrieval, writing, and offline long-term consolidation.
- **Evidence:** Authors report LoCoMo F1 and retrieval/end-to-end latency under a fixed retrieval budget.
- **Limitation:** Small memory-operation models do not establish that the full answering agent or every deployment component is small.
- **Status:** [ACL 2026 Main Conference (Long Papers)](https://aclanthology.org/2026.acl-long.588/).
- **Source review:** v3; metadata and abstract, checked 2026-10-22.

### LightMem (ICLR 2026)

**[LightMem: Lightweight and Efficient Memory-Augmented Generation](https://arxiv.org/abs/2510.18866)** — Jizhan Fang et al.; 2025-10-21. `supporting`

- **Models:** GPT and Qwen backbones; not restricted to small models.
- **Contribution:** Organizes memory into sensory, short-term, and long-term stages with offline consolidation.
- **Evidence:** Authors evaluate memory accuracy and token, API-call, and runtime costs on LongMemEval.
- **Limitation:** Efficient memory augmentation is supporting architecture evidence, not proof of an entirely small-model agent.
- **Status:** [ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a05b72653ec5b473732129829ae04195-Abstract-Conference.html).
- **Source review:** v4; metadata and abstract, checked 2026-10-22.

## Multi-Agent Collaboration

When does communication justify its overhead?

### TalkMesh

**[Reinforcement Learning of Communication in a Mesh of Small Language Models](https://arxiv.org/abs/2609.30578)** — Mehmet Kerem Turkcan; 2026-09-24. `core`

- **Models:** Includes 0.8B and 3B.
- **Contribution:** Learns confidence-gated communication and decentralized revision.
- **Evidence:** The abstract compares communication against independent sampling and studies corrupted messages.
- **Limitation:** Agent count and communication costs must accompany any accuracy comparison.
- **Status:** arXiv.
- **Source review:** v1; metadata and abstract, checked 2026-10-22.

### Small-agent collaboration

**[Can Small Agents Collaborate to Beat a Single Large Language Model?](https://arxiv.org/abs/2601.11327)** — Agata Żywot et al.; 2026-01-16. `supporting`

- **Models:** Not established from reviewed abstract.
- **Contribution:** Studies a central orchestrator with specialized workers and restricted communication.
- **Evidence:** Authors find that reasoning at the orchestrator matters more than at workers.
- **Limitation:** Inspect orchestrator size and matched inference budgets before crediting small workers.
- **Status:** [ICLR 2026 · MALGAI Workshop](https://openreview.net/pdf?id=RLHUTcvsA9).
- **Source review:** v2; metadata and abstract, checked 2026-10-22.

### Latent-Lens

**[Latent-Lens: Visual Perception in Small Language Models Through Latent Communication](https://neurips.cc/virtual/2026/loc/sydney/poster/155307)** — Mo Shahdloo et al.; first-publication date unverified. `supporting`

- **Models:** TinyLlama-1.1B and InternVL2-1B example pairing; 1.6M trainable codec parameters.
- **Contribution:** Connects a VLM and an SLM through a lightweight latent-state codec instead of text messages.
- **Evidence:** The official abstract reports visual question answering and image captioning comparisons against text communication.
- **Limitation:** Perception and communication results do not establish long-horizon agent task completion; first-publication date is not verified.
- **Status:** [NeurIPS 2026 Poster](https://neurips.cc/virtual/2026/loc/sydney/poster/155307).
- **Source review:** Official NeurIPS 2026 poster page; metadata and abstract, checked 2026-10-22.

## On-Device and Edge Deployment

What can run locally under actual hardware limits?

### Fara-7B

**[Fara-7B: An Efficient Agentic Model for Computer Use](https://arxiv.org/abs/2511.19663)** — Ahmed Awadallah et al.; 2025-11-24. `core`

- **Models:** 7B.
- **Contribution:** Trains a screenshot-based computer-use agent from filtered synthetic web trajectories.
- **Evidence:** Authors evaluate WebVoyager, Online-Mind2Web, and WebTailBench.
- **Limitation:** An on-device-capable model does not establish offline operation or fit on any specific GPU.
- **Status:** arXiv.
- **Source review:** v1; metadata and abstract, checked 2026-10-22.

## Benchmarks and Evaluation

What is the cost of completing a task correctly?

### Rethinking Scale

**[Rethinking Scale: Deployment Trade-offs of Small Language Models under Agent Paradigms](https://arxiv.org/abs/2604.19299)** — Xinlin Wang et al.; 2026-04-21. `core`

- **Models:** <10B.
- **Contribution:** Compares base models, tool-equipped single agents, and multi-agent systems.
- **Evidence:** Authors report the best performance–cost balance for the single-agent setup studied.
- **Limitation:** A setting-specific negative finding does not establish that collaboration never helps.
- **Status:** [ACL 2026 Industry Track](https://aclanthology.org/2026.acl-industry.123/).
- **Source review:** v1; metadata and abstract, checked 2026-10-22.
