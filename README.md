# Awesome Small Language Model Agents

A research reading resource on small language models for agentic systems: training, tools, recovery, memory, collaboration, evaluation, and deployment.

**Catalog snapshot:** 25 selected papers, with five [focused manuscript notes](notes/README.md). Primary sources checked on **2026-10-22**. Entries are **AI-assisted editorial summaries**. Five notes inspect named methods/results/appendix sections; none claims exhaustive full-text review, human review, or reproduction. This is a selective snapshot, not an exhaustive or automatically current bibliography.

## Start here

- [Catalog coverage and review status](docs/catalog-status.md) · [Candidate decisions](data/candidate-decisions.json)
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
  - Status: [preprint](https://arxiv.org/abs/2506.02153). Checked 2026-10-22.

### Agent Training and Distillation

Which agent capabilities should be learned?

- **[Harness-Aware Distillation for Small Language Model Agents](https://arxiv.org/abs/2610.02858)** — Moonseok Choi et al.; first published 2026-10-02. `core`
  - Models: Qwen3 students 0.6B/1.7B; teachers 8B and 30B-A3B; Gemma cross-family study. Reviewed source: v1; selected manuscript sections.
  - Contribution: Distills teacher actions conditioned on harness state and filters inconsistent preferences.
  - Evidence: Authors compare long-horizon agents with a fixed harness and report fewer unproductive loops.
  - Limitation: Model sizes, benchmark-level results, and teacher costs require full-text review.
  - Status: [preprint](https://arxiv.org/abs/2610.02858). Checked 2026-10-22.
  - [Focused note](notes/had.md) (manuscript v1; selected sections, not exhaustive audit).

- **[From Passive Delegates to Strategic Negotiators: Reinforcing Social Reasoning in Small Language Models with SocialRL](https://arxiv.org/abs/2608.13787)** — Wenyue Hua et al.; first published 2026-08-13. `core`
  - Models: 4B. Reviewed source: v1; metadata + abstract only.
  - Contribution: Trains agents to represent a principal in negotiations with conflicting interests.
  - Evidence: The abstract describes six domains and cross-domain policy evaluation.
  - Limitation: Controlled negotiation outcomes do not establish real-world delegation reliability.
  - Status: [preprint](https://arxiv.org/abs/2608.13787). Checked 2026-10-22.

- **[AgentCPM-Explore: Realizing Long-Horizon Deep Exploration for Edge-Scale Agents](https://arxiv.org/abs/2602.06485)** — Haotian Chen et al.; first published 2026-02-06. `core`
  - Models: 4B. Reviewed source: v1; metadata + abstract only.
  - Contribution: Combines model fusion, reward denoising, and context refinement for long-horizon exploration.
  - Evidence: The abstract reports benchmark comparisons and a GAIA text result under pass@64.
  - Limitation: pass@64 is not single-run reliability; local model size does not imply local tools or cheap training.
  - Status: [preprint](https://arxiv.org/abs/2602.06485). Checked 2026-10-22.

- **[Agent-FLAN: Designing Data and Methods of Effective Agent Tuning for Large Language Models](https://arxiv.org/abs/2403.12881)** — Zehui Chen et al.; first published 2024-03-19. `core`
  - Models: Includes Llama2-7B; mixed-size study. Reviewed source: v1; metadata + abstract only.
  - Contribution: Separates training concerns and adds negative examples for agent tuning.
  - Evidence: Authors evaluate agent tasks and hallucinated actions with a 7B model.
  - Limitation: Training improvements need separate accounting for synthetic data and generalization.
  - Status: [Findings of ACL 2024](https://aclanthology.org/2024.findings-acl.557/). Checked 2026-10-22.
  - [Code](https://github.com/InternLM/Agent-FLAN) (availability checked; not reproduced).

- **[AgentTuning: Enabling Generalized Agent Abilities for LLMs](https://arxiv.org/abs/2310.12823)** — Aohan Zeng et al.; first published 2023-10-19. `core`
  - Models: 7B, 13B, 70B; mixed-size study. Reviewed source: v2; metadata + abstract only.
  - Contribution: Mixes agent trajectories with general instruction data.
  - Evidence: Authors release AgentLM variants and evaluate unseen agent tasks.
  - Limitation: The abstract comparison against GPT-3.5 concerns 70B, not the 7B variant.
  - Status: [Findings of ACL 2024](https://aclanthology.org/2024.findings-acl.181/). Checked 2026-10-22.
  - [Code](https://github.com/THUDM/AgentTuning) (availability checked; not reproduced).

### Tool Use and Structured Actions

How do agents select tools and valid arguments?

- **[OR-Toolformer: Modeling and Solving Operations Research Problems with Tool Augmented Large Language Models](https://arxiv.org/abs/2510.01253)** — Jianzhang Zhang et al.; first published 2025-09-24. `core`
  - Models: Llama-3.1-8B-Instruct. Reviewed source: v1; metadata + abstract only.
  - Contribution: Fine-tunes a small model to formulate operations-research tasks with external solvers.
  - Evidence: Authors evaluate execution accuracy and two unseen problem types.
  - Limitation: Solver dependence and problem-type coverage limit claims about general agent planning.
  - Status: [preprint](https://arxiv.org/abs/2510.01253). Checked 2026-10-22.

- **[ToolACE: Winning the Points of LLM Function Calling](https://arxiv.org/abs/2409.00920)** — Weiwen Liu et al.; first published 2024-09-02. `core`
  - Models: Includes 8B. Reviewed source: v2; metadata + abstract only.
  - Contribution: Synthesizes diverse function-calling data with rule and model verification.
  - Evidence: Authors report an 8B model on the Berkeley Function-Calling Leaderboard.
  - Limitation: Function-call scores do not establish long-horizon completion or cheap data generation.
  - Status: [preprint](https://arxiv.org/abs/2409.00920). Checked 2026-10-22.

- **[TinyAgent: Function Calling at the Edge](https://arxiv.org/abs/2409.00608)** — Lutfi Eren Erdogan et al.; first published 2024-09-01. `core`
  - Models: 1.1B and 7B. Reviewed source: v3; selected manuscript sections.
  - Contribution: Specializes small planners for function dependencies and retrieves relevant tools.
  - Evidence: Authors demonstrate a MacBook assistant and compare function-plan success.
  - Limitation: A fixed tool inventory and synthetic plan metric do not establish open-ended agent reliability.
  - Status: [EMNLP 2024 System Demonstrations](https://aclanthology.org/2024.emnlp-demo.9/). Checked 2026-10-22.
  - [Focused note](notes/tinyagent.md) (manuscript v1; selected sections, not exhaustive audit).
  - [Code](https://github.com/SqueezeAILab/TinyAgent) (availability checked; not reproduced).

- **[Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)** — Timo Schick et al.; first published 2023-02-09. `background`
  - Models: Not established from reviewed abstract. Reviewed source: v1; metadata + abstract only.
  - Contribution: Learns API insertion from a few demonstrations and self-supervision.
  - Evidence: Authors evaluate several tools and downstream zero-shot tasks.
  - Limitation: Foundational tool-use work; not evidence of reliable long-horizon interactive agents.
  - Status: [preprint](https://arxiv.org/abs/2302.04761). Checked 2026-10-22.

### Planning and Error Recovery

How do agents detect failure and resume progress?

- **[Progress-Aware Distillation for Mitigating Stagnation in Small Language Model Agents](https://arxiv.org/abs/2610.19439)** — Yuanpu Cao et al.; first published 2026-10-14. `core`
  - Models: 0.6–8B. Reviewed source: v2; selected manuscript sections.
  - Contribution: Detects stalled trajectories and uses an adaptive distillation penalty.
  - Evidence: Authors evaluate eight small models on in-domain and out-of-domain tasks.
  - Limitation: Abstract review cannot establish fair total compute or robustness in production.
  - Status: [NeurIPS 2026 (arXiv author comment; proceedings not independently checked)](https://arxiv.org/abs/2610.19439). Checked 2026-10-22.
  - [Focused note](notes/prod.md) (manuscript v2; selected sections, not exhaustive audit).
  - [Code](https://github.com/CaoYuanpu/ProD) (availability checked; not reproduced).

- **[PACE: Two-Timescale Self-Evolution for Small Language Model Agents](https://arxiv.org/abs/2605.23019)** — Chen Ling et al.; first published 2026-05-21. `core`
  - Models: 4–14B; includes models above scope threshold. Reviewed source: v1; metadata + abstract only.
  - Contribution: Separates prompt refinement from control-logic changes accepted through held-out validation.
  - Evidence: Authors use three frozen backbones, controlled tasks, and a tau-bench case study.
  - Limitation: Some models exceed 10B; validation costs and domain transfer need deeper review.
  - Status: [preprint](https://arxiv.org/abs/2605.23019). Checked 2026-10-22.

### Memory and Context Management

What belongs in weights, context, or external memory?

- **[Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory](https://arxiv.org/abs/2608.07169)** — Taeil Kim et al.; first published 2026-08-07. `core`
  - Models: 4–8B. Reviewed source: v1; selected manuscript sections.
  - Contribution: Transfers teacher experience into workflow, subtask, and function memories without student weight updates.
  - Evidence: Authors evaluate AppWorld, BFCL V3, and ToolSandbox using four small students.
  - Limitation: Teacher-generated memory has construction cost; training-free does not mean cost-free.
  - Status: [preprint](https://arxiv.org/abs/2608.07169). Checked 2026-10-22.
  - [Focused note](notes/amd.md) (manuscript v1; selected sections, not exhaustive audit).

### Multi-Agent Collaboration

When does communication justify its overhead?

- **[Reinforcement Learning of Communication in a Mesh of Small Language Models](https://arxiv.org/abs/2609.30578)** — Mehmet Kerem Turkcan; first published 2026-09-24. `core`
  - Models: Includes 0.8B and 3B. Reviewed source: v1; metadata + abstract only.
  - Contribution: Learns confidence-gated communication and decentralized revision.
  - Evidence: The abstract compares communication against independent sampling and studies corrupted messages.
  - Limitation: Agent count and communication costs must accompany any accuracy comparison.
  - Status: [preprint](https://arxiv.org/abs/2609.30578). Checked 2026-10-22.

- **[Can Small Agents Collaborate to Beat a Single Large Language Model?](https://arxiv.org/abs/2601.11327)** — Agata Żywot et al.; first published 2026-01-16. `supporting`
  - Models: Not established from reviewed abstract. Reviewed source: v2; metadata + abstract only.
  - Contribution: Studies a central orchestrator with specialized workers and restricted communication.
  - Evidence: Authors find that reasoning at the orchestrator matters more than at workers.
  - Limitation: Inspect orchestrator size and matched inference budgets before crediting small workers.
  - Status: [preprint](https://arxiv.org/abs/2601.11327). Checked 2026-10-22.

### Hybrid Systems and Routing

When should a small agent escalate?

- **[AgentRouter: Heterogeneous Model Routing for Cost-Optimal Multi-Step Agentic Workflows](https://arxiv.org/abs/2609.22951)** — Rudrendu Kumar Paul et al.; first published 2026-09-19. `core`
  - Models: 12M router; four backend tiers including a 7B example. Reviewed source: v1; metadata + abstract only.
  - Contribution: Assigns trajectory steps to heterogeneous model tiers.
  - Evidence: Authors compare step-level routing with frontier-only and query-routing baselines.
  - Limitation: The router is not the agent backbone; quality retention and costs require benchmark-specific scrutiny.
  - Status: [AgenticUQ Workshop, ICML 2026 (arXiv author comment; workshop acceptance not independently checked)](https://arxiv.org/abs/2609.22951). Checked 2026-10-22.

- **[R2V Agent: Teaching SLMs When to Ask for Help](https://arxiv.org/abs/2605.16604)** — Raghu Vamshi Hemadri et al.; first published 2026-05-15. `core`
  - Models: Four SLM backbones; sizes not established from abstract. Reviewed source: v1; metadata + abstract only.
  - Contribution: Routes individual decisions using a calibrated verifier after small-policy training.
  - Evidence: Authors evaluate HumanEval+, TextWorld, and TerminalBench with stronger-model escalation.
  - Limitation: System success includes teacher intervention; escalation fraction alone is not total cost.
  - Status: [preprint](https://arxiv.org/abs/2605.16604). Checked 2026-10-22.

### On-Device and Edge Deployment

What can run locally under actual hardware limits?

- **[MolmoWeb: Open Visual Web Agent and Open Data for the Open Web](https://arxiv.org/abs/2604.08516)** — Tanmay Gupta et al.; first published 2026-04-09. `core`
  - Models: 4B and 8B. Reviewed source: v1; metadata + abstract only.
  - Contribution: Builds visual browser policies with synthetic and human demonstration data.
  - Evidence: Authors report WebVoyager, Online-Mind2Web, and DeepShop evaluations.
  - Limitation: Parallel rollouts and best-of-N selection must be separated from single-run success.
  - Status: [preprint](https://arxiv.org/abs/2604.08516). Checked 2026-10-22.

- **[Fara-7B: An Efficient Agentic Model for Computer Use](https://arxiv.org/abs/2511.19663)** — Ahmed Awadallah et al.; first published 2025-11-24. `core`
  - Models: 7B. Reviewed source: v1; metadata + abstract only.
  - Contribution: Trains a screenshot-based computer-use agent from filtered synthetic web trajectories.
  - Evidence: Authors evaluate WebVoyager, Online-Mind2Web, and WebTailBench.
  - Limitation: An on-device-capable model does not establish offline operation or fit on any specific GPU.
  - Status: [preprint](https://arxiv.org/abs/2511.19663). Checked 2026-10-22.

- **[UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326)** — Yujia Qin et al.; first published 2025-01-21. `supporting`
  - Models: Mixed-size family; per-result sizes need full-text review. Reviewed source: v1; metadata + abstract only.
  - Contribution: Learns screenshot-conditioned actions with reasoning and iterative training.
  - Evidence: Authors evaluate perception, grounding, and GUI execution benchmarks.
  - Limitation: Do not assign headline results to a small variant without checking model size and step budget.
  - Status: [preprint](https://arxiv.org/abs/2501.12326). Checked 2026-10-22.

- **[Octopus v2: On-device language model for super agent](https://arxiv.org/abs/2404.01744)** — Wei Chen et al.; first published 2024-04-02. `core`
  - Models: 2B. Reviewed source: v7; metadata + abstract only.
  - Contribution: Targets low-latency function calling with an on-device model.
  - Evidence: The abstract reports comparisons with GPT-4 and a retrieval-based Llama baseline.
  - Limitation: Inspect the tool inventory and matched hardware before generalizing latency claims.
  - Status: [preprint](https://arxiv.org/abs/2404.01744). Checked 2026-10-22.

### Benchmarks and Evaluation

What is the cost of completing a task correctly?

- **[Rethinking Scale: Deployment Trade-offs of Small Language Models under Agent Paradigms](https://arxiv.org/abs/2604.19299)** — Xinlin Wang et al.; first published 2026-04-21. `core`
  - Models: 27 models; Table 1 includes SOLAR 10.7B despite abstract framing <10B. Reviewed source: v1; selected manuscript sections.
  - Contribution: Compares base models, tool-equipped single agents, and multi-agent systems.
  - Evidence: Authors report the best performance–cost balance for the single-agent setup studied.
  - Limitation: Financial tasks, fixed ReAct designs and a five-turn cap constrain transfer; Table 1 includes a 10.7B model.
  - Status: [preprint](https://arxiv.org/abs/2604.19299). Checked 2026-10-22.
  - [Focused note](notes/rethinking-scale.md) (manuscript v1; selected sections, not exhaustive audit).

- **[ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities](https://arxiv.org/abs/2408.04682)** — Jiarui Lu et al.; first published 2024-08-08. `supporting`
  - Models: Benchmark; multiple model sizes. Reviewed source: v2; metadata + abstract only.
  - Contribution: Evaluates state dependencies and intermediate milestones in interactive tool use.
  - Evidence: Authors use stateful execution and a simulated conversational user.
  - Limitation: A benchmark for SLM-agent studies, not a small-agent training method; simulator behavior affects results.
  - Status: [Findings of NAACL 2025](https://aclanthology.org/2025.findings-naacl.65/). Checked 2026-10-22.

- **[τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045)** — Shunyu Yao et al.; first published 2024-06-17. `supporting`
  - Models: Benchmark; multiple model sizes. Reviewed source: v1; metadata + abstract only.
  - Contribution: Measures policy-following task completion using final database states.
  - Evidence: Authors study repeated-trial reliability using pass^k.
  - Limitation: pass^k requires consistent success across trials; it is not best-of-k pass@k.
  - Status: [preprint](https://arxiv.org/abs/2406.12045). Checked 2026-10-22.

- **[AgentGym: Evolving Large Language Model-based Agents across Diverse Environments](https://arxiv.org/abs/2406.04151)** — Zhiheng Xi et al.; first published 2024-06-06. `supporting`
  - Models: Not established from reviewed abstract. Reviewed source: v1; metadata + abstract only.
  - Contribution: Combines environments, trajectories, and an agent-evolution method.
  - Evidence: Authors describe cross-environment agent learning and an evaluation suite.
  - Limitation: Useful evaluation infrastructure; abstract-level review does not establish the small-model subset.
  - Status: [preprint](https://arxiv.org/abs/2406.04151). Checked 2026-10-22.

<!-- CATALOG:END -->

## Contrasting and negative findings

Read Rethinking Scale alongside the collaboration and TalkMesh studies. Their settings differ: an improvement from communication in one setup does not establish that adding workers is economical in another. Inspect the orchestrator, tools, attempts, and total cost before comparing conclusions.

## Coverage gaps and next milestones

All nine categories now have entries. Tool use and routing include direct SLM-agent studies; general benchmarks are labeled supporting resources. Five focused notes cover ProD, HAD, AMD, Rethinking Scale, and TinyAgent. The 20–30-entry catalog milestone is met; the original target of 5–8 exhaustive full-text notes remains open. Next: deepen manuscript reviews, verify hardware/costs, add missing resource links, and compare evaluation conditions without inventing a common leaderboard.

No automatic literature discovery or human-review process is running. The scheduled job checks link reachability only. See [the milestone status](docs/catalog-status.md).

## Maintenance and provenance

Metadata is the source of truth; the catalog is generated with `python3 scripts/render.py`. CI checks structure and catalog synchronization. Scheduled link checks report reachability only; they do not verify claims or update review dates. AI assistance is disclosed; no human-review status or central Awesome-list affiliation is claimed.

Original editorial content: CC BY 4.0; scripts: MIT. Third-party works retain their own licenses. See [LICENSE](LICENSE).
