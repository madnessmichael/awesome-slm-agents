# Reading guide

These routes are editorial suggestions. Five [focused manuscript notes](../notes/README.md) add selected methods/results evidence; other entries use primary abstracts. No exhaustive full-text audit or reproduction is implied.

## Understand the motivation

1. [SLM agent position paper](https://arxiv.org/abs/2506.02153): read the economic argument as a hypothesis.
2. [Rethinking Scale](https://arxiv.org/abs/2604.19299): look for conditions where tools help and collaboration adds overhead.
3. [Small-agent collaboration](https://arxiv.org/abs/2601.11327): contrast orchestrator capacity with worker capacity.

## Build a system

1. [Fara-7B](https://arxiv.org/abs/2511.19663): inspect screenshot actions and trajectory generation.
2. [AMD](https://arxiv.org/abs/2608.07169): investigate memory as a channel for teacher experience.
3. [HAD](https://arxiv.org/abs/2610.02858): separate capabilities supplied by the model from those supplied by software.
4. Use the [evaluation guide](evaluation-guide.md) before choosing a backbone.

## Develop a research question

Read [AgentCPM-Explore](https://arxiv.org/abs/2602.06485), [ProD](https://arxiv.org/abs/2610.19439), and [PACE](https://arxiv.org/abs/2605.23019) together. Ask whether a small agent can detect stalled progress and choose among memory retrieval, strategy changes, and escalation under a fixed budget. Compare against single-agent tools, random escalation, and a strong-model-only baseline. This is a proposed experiment, not a result.

For communication, pair [TalkMesh](https://arxiv.org/abs/2609.30578) with the contrasting collaboration studies. For delegation, inspect [SocialRL](https://arxiv.org/abs/2608.13787), particularly the distinction between controlled games and operational safety.

## Tools and routing

Read [TinyAgent](../notes/tinyagent.md) for bounded tool planning, then [ToolACE](https://arxiv.org/abs/2409.00920) for data synthesis. For escalation, compare [R2V-Agent](https://arxiv.org/abs/2605.16604) and [AgentRouter](https://arxiv.org/abs/2609.22951): record the stronger model role and cost boundaries before interpreting small-model savings.

## Check the evaluation itself

Use [ToolSandbox](https://arxiv.org/abs/2408.04682) and [τ-bench](https://arxiv.org/abs/2406.12045) as supporting methodology. The [BFCL conference paper](https://proceedings.mlr.press/v267/patil25a.html) documents function-call evaluation; specify the benchmark version rather than copying a current leaderboard score into an older paper comparison.
