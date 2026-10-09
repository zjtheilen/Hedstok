# Hedstok — Roadmap

## Purpose

This document tracks Hedstok's development, the status of its investigations, and the questions that remain open.

The roadmap is evidence-driven. Completing an experiment does not automatically authorize a production feature. Implementation decisions should follow from the findings and the project's actual needs.

## Guiding Principles

- Evidence before assumptions.
- Stories before specifications.
- Evidence before labels.
- Concepts before implementation.
- Evolution, not rewrite.

Hedstok exists to help a person notice a listing worth examining more closely and understand why it may be interesting. It is not intended to automate purchasing decisions, determine market value, or verify seller claims.

## Current Development Status

### Phase 1 — Initial Experiment

**Status: Completed**

Established an initial experimental foundation for working with musical-instrument listing descriptions and expected evidence.

The experiment provided a starting point for examining how listing information could be extracted and represented.

### Phase 2 — Evidence Extraction

**Status: Completed as an exploratory phase**

Investigated extracting structured evidence from listing descriptions.

The central design requirement is to preserve the distinction between a source claim and an independently established fact. Extracted information should remain traceable to the listing, with uncertainty preserved rather than silently resolved.

The resulting evidence representation serves as input to later interpretation experiments.

### Phase 3 — AI-Assisted Discovery

**Status: Exploratory findings documented**

Investigated AI-assisted discovery and extraction using representative listing examples.

The focus was on understanding how an AI model identifies potentially meaningful details and how those details can be represented as structured evidence.

Findings and limitations are preserved in `docs/phase-3-discovery.md`.

The results should not be treated as proof that discovery is complete, consistently reliable, or ready for unrestricted production use.

### Phase 4 — Evidence Interpretation

**Status: Exploratory investigation completed through Phase 4.8; design questions remain open**

Investigated whether structured evidence can support explainable interpretations of why a listing deserves closer attention.

The experiments examined:

- Whether a reason for attention is an interpretation rather than another evidence type
- Whether attention depends on a particular evidence category or on combinations of evidence and context
- Whether AI-generated interpretations agree with human judgments
- Whether targeted guidance improves interpretation quality
- Whether more selective evidence references improve interpretability
- Whether stable evidence IDs improve traceability and auditability

The detailed record is preserved in `docs/phase-4-interpretation.md`.

The experiments suggest that interpretation is possible, but quality remains uneven. Stable evidence references improve auditability, yet do not guarantee that the selected evidence is relevant, complete, or faithfully represented.

No permanent scoring model, confidence model, fixed reason taxonomy, or automated recommendation system has been justified by these experiments.

## Current Conceptual Pipeline

The working conceptual sequence is:

1. **Source listing** — the original listing information.
2. **Signals** — structured, source-grounded claims and details extracted from the listing.
3. **Evidence relationships** — relevant connections, tensions, and combinations among Signals.
4. **Interpretation** — an explanation of why the evidence may be interesting in context.
5. **Human attention** — a concise observation that invites closer inspection.

This is a conceptual model, not a commitment to a particular production schema or sequence of software components.

## Current Findings

The investigations so far support the following working conclusions:

- A listing may deserve attention for different reasons; no single evidence category explains every case.
- Interpretation should be derived from evidence rather than represented as an independent, unsupported claim.
- Context can change the significance of otherwise ordinary details.
- Uncertainty should be preserved and expressed where relevant.
- AI-generated interpretations can be useful, but may over-select evidence, omit important details, miss relationships, or overstate what a source establishes.
- Stable evidence IDs make interpretations easier to audit, but do not automatically improve reasoning quality.
- Small experimental samples and single model runs are insufficient to establish general reliability.

These findings remain provisional and should be revisited when new evidence warrants it.

## Open Questions

### Evidence quality

- How should Hedstok preserve source wording while still allowing concise, useful interpretation?
- How should conflicting, ambiguous, or redundant Signals be represented?
- What validation is needed to prevent unsupported claims from entering later stages?

### Interpretation quality

- How can interpretation select relevant evidence without omitting important context?
- How can uncertainty be represented without treating every unknown as an opportunity or a problem?
- What distinguishes a useful reason to investigate from a merely interesting detail?
- How should human disagreement with an AI interpretation be recorded and evaluated?

### Traceability and evaluation

- Are stable Signal IDs sufficient for the auditability Hedstok needs?
- What evaluation criteria should be applied consistently across experiments?
- What additional cases or repeated runs are necessary before drawing stronger conclusions?

### Production design

- Which experimental structures, if any, should become production interfaces or schemas?
- Is a fixed surface judgment useful, and if so, how should it be interpreted?
- What should remain deterministic, and what genuinely benefits from AI interpretation?

These questions should be resolved only when their answers affect a concrete implementation decision.

## Next Steps

1. **Preserve the experimental record.** Keep the detailed Phase 3 and Phase 4 findings separate from the current concept and roadmap.
2. **Review the interpretation boundary.** Ensure that evidence extraction, interpretation, uncertainty, and attention judgments remain distinct.
3. **Define evaluation criteria before further experiments.** Establish what counts as relevance, sufficiency, selectivity, fidelity, and defensible interpretation.
4. **Choose a focused follow-up experiment.** Target one unresolved question at a time rather than changing several variables simultaneously.
5. **Reassess production requirements after the evidence is stronger.** Avoid implementing a permanent scoring, confidence, or recommendation system merely because it is technically possible.

## Decision Rule

A proposed implementation change should have:

- A clearly stated problem or question
- Evidence that the change addresses that problem
- An evaluation method appropriate to the claim being made
- A documented account of limitations and unresolved uncertainty

Until those conditions are met, preserve the current behavior and treat new approaches as experiments.

## Status Summary

| Area                                   | Status                         | Position                                             |
| -------------------------------------- | ------------------------------ | ---------------------------------------------------- |
| Initial experiment                     | Completed                      | Exploratory foundation established                   |
| Evidence extraction                    | Explored                       | Preserve source-grounded claims                      |
| AI-assisted discovery                  | Investigated                   | Findings retained separately                         |
| Evidence interpretation                | Investigated through Phase 4.8 | Useful but imperfect                                 |
| Stable evidence references             | Experimentally evaluated       | Improves traceability; quality gains remain unproven |
| Production interpretation architecture | Open                           | No permanent design justified yet                    |
| Scoring and confidence models          | Deferred                       | Not justified by current evidence                    |
| Automated purchase recommendations     | Out of scope                   | Not Hedstok's purpose                                |
