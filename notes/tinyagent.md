# TinyAgent — focused manuscript note

Source: [2409.00608v1](https://arxiv.org/html/2409.00608v1). Checked 2026-10-22. AI-assisted, **selected sections reviewed**: Sections 3–4, Tables 1–2. This is not an exhaustive full-manuscript audit, human review, or reproduction.

## Mechanism and conditions

TinyAgent generates dependency-aware function plans; Tool RAG selects relevant functions. Section 3.2 defines **16 Mac tools**, **80K training**, **1K validation**, and **1K test examples**. The metric matches generated function-plan graphs, not unrestricted real-world completion.

## Anchored result

Table 1: TinyAgent-1.1B scores **80.06%** with the learned retriever versus **78.89%** with all tools. Table 2 reports **80.35%**, **2.9 seconds**, and **0.68 GB model size** after four-bit quantization. Model size is not peak working memory; latency covers the planner.

## Limitations

Data synthesis uses GPT-4-Turbo. The MacBook demo does not establish arbitrary-tool generalization.

## Editorial next step

Test held-out functions, retrieval misses, and execution-state correctness. Reproduction: not run. This note reviews v1; catalog metadata tracks v3 separately.
