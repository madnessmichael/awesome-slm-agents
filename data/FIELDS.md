# Dataset conventions

`papers.yaml` is a JSON array using YAML 1.2-compatible syntax. Parse with Python `json.load` or a YAML 1.2 parser. Field semantics are specified in [the implementation plan](../docs/IMPLEMENTATION_PLAN_VI.md#5-dữ-liệu-và-schema).

Null or an empty list means **not established in the present review**, not absent in the original paper. All initial entries have metadata/abstract review only. `accepted_author_reported` is distinct from independently confirmed acceptance. `version_reviewed` identifies the landing-page version used for the abstract summary.

The validator currently checks core structure, dates, uniqueness, selected enums, review-note requirements and generated catalog consistency. It is not a comprehensive JSON Schema or factual verifier.
