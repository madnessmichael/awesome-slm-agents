# Dataset conventions

`papers.yaml` is a JSON array using YAML 1.2-compatible syntax. Parse with Python `json.load` or a YAML 1.2 parser. Field semantics are specified in [the implementation plan](../docs/IMPLEMENTATION_PLAN_VI.md#5-dữ-liệu-và-schema).

Null or an empty list means **not established in the present review**, not absent in the original paper. Five entries now include selected manuscript-section reviews and a note with an explicit version. All entries still have exhaustive full-text, human-review and reproduction flags set to false. `accepted_author_reported` is distinct from independently confirmed acceptance. `version_reviewed` identifies the landing-page version used for the abstract summary.

The checked-in [schema](papers.schema.json) specifies nested fields, types and required values. The standard-library validator enforces the keywords used by that schema, selected semantic invariants, review-note requirements and catalog synchronization. It rejects unsupported schema keywords; it is not a general JSON Schema engine or factual verifier. `note_version_reviewed` can differ from metadata `version_reviewed`, and `verification.sections_reviewed` identifies the narrower reading scope.
