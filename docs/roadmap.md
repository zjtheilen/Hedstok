# Hedstok — Roadmap

## Purpose

This document tracks Hedstok's development, the status of its investigations, and the questions that remain open.

The roadmap is evidence-driven. Completing an experiment does not automatically authorize a production feature. Implementation decisions should follow from documented findings and a concrete need.

## Guiding Principles

- Evidence before assumptions.
- Stories before specifications.
- Evidence before labels.
- Concepts before implementation.
- Evolution, not rewrite.

Hedstok explores how software can help a person notice a musical-instrument listing or lead worth investigating and understand why it may be interesting.

It is not intended to automate purchasing decisions, establish market value, authenticate instruments, or independently verify seller claims.

## Current Status

**Active phase: Phase 5 — Signal Fidelity Audit**

Phases 1–4 established an experimental foundation for extracting structured evidence, detecting evidence patterns, and investigating evidence-grounded interpretation.

Phase 5 is auditing the boundary between source material, extracted Signals, and deterministic detector behavior. The purpose is to identify concrete fidelity and interpretation problems before making broader changes to prompts, schemas, or architecture.

The audit is in progress. Some targeted detector behaviors have been corrected or constrained, but several traceability and semantic questions remain unresolved.

See [`docs/phase-5-signal-fidelity-audit.md`](phase-5-signal-fidelity-audit.md) for the detailed record.

## Phase History

### Phase 1 — Initial Experiment

**Status: Completed**

Established the initial experimental foundation for working with used-instrument listings and potential acquisition leads.

The experiment tested the basic premise that a listing may be interesting for reasons that are not reducible to conventional specifications or keyword matching.

### Phase 2 — Evidence Extraction

**Status: Explored**

Investigated transforming unstructured listing descriptions into structured, source-grounded Signals.

The central boundary is that extraction represents what the available source says or shows. It does not independently establish whether a seller's claim is true, determine value, or decide that an instrument is worth acquiring.

The resulting evidence can support later discovery and interpretation, but extraction is not assumed to be complete or universally reliable.

### Phase 3 — Discovery Experiments

**Status: Exploratory findings documented**

Investigated whether structured Signals could support the discovery of potentially interesting acquisition leads.

The experiments found that deterministic evidence-pattern detection could identify some useful structures, including provenance claims, seller/inventory opportunities, and specific contradictory or unusual descriptions. Other cases required combinations of evidence or contextual interpretation.

The experiments also demonstrated that extracting source-grounded Signals does not guarantee that downstream explanations will remain source-grounded.

Findings are preserved in [`docs/phase-3-discovery.md`](phase-3-discovery.md).

The results do not establish a complete discovery architecture, a permanent evidence-pattern taxonomy, or general detector reliability.

### Phase 4 — Evidence Interpretation

**Status: Exploratory investigation closed; production design remains open**

Investigated how Hedstok could explain why a listing may deserve closer human attention.

The experiments examined evidence selection, contextual relevance, interpretation fidelity, source attribution, uncertainty, evidence references, and the relationship between an explanation and a surface judgment.

Several conclusions emerged:

- Interpretation is distinct from extraction.
- A useful reason for attention may arise from one Signal or from a combination of Signals and context.
- Evidence references improve auditability but do not guarantee faithful interpretation.
- An interpretation may include the expected label while still omitting important context or overstating what the evidence establishes.
- Shorter explanations are not automatically better explanations.
- Small samples and single model runs cannot establish general reliability.

The Phase 4.10 and Phase 4.11 prompt experiments produced mixed results. The added guidance did not demonstrate a consistent improvement sufficient to justify promoting it into production.

Findings are preserved in [`docs/phase-4-interpretation.md`](phase-4-interpretation.md).

Phase 4 is closed as an exploratory investigation, not as a claim that interpretation quality has been solved. Its results do not justify a permanent scoring, confidence, ranking, or recommendation system.

### Phase 5 — Signal Fidelity Audit

**Status: In progress**

Phase 5 investigates whether extracted Signals faithfully represent their source material and whether downstream detectors infer more than the evidence supports.

The audit separates three layers:

1. **Extraction fidelity:** Does the Signal preserve the source's meaning, uncertainty, attribution, and relevant context?
2. **Signal semantics:** Does the Signal's type and claim accurately represent the evidence?
3. **Detector interpretation:** Does the detector's output stay within what its input evidence supports?

These layers must be assessed separately. A source-to-Signal mismatch does not automatically establish a detector defect, and a detector defect should not be hidden by changing extraction wording.

#### Audited signal-fidelity cases

| Case  | Focus                                       | Current assessment                                                                                                                                                                                         |
| ----- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SF-01 | Explicit uncertainty                        | The extraction preserves the sampled uncertainty and lower-bound language. Downstream behavior has not been fully audited.                                                                                 |
| SF-02 | Configuration versus modification history   | The heavy-gauge-string false-positive path was addressed, and dated-instrument context was narrowed and tested. Other configuration-related detector terms have not been comprehensively audited.          |
| SF-03 | Ambiguity and seller-claim attribution      | The revised extraction preserves ambiguity around the album claim. Consistent explicit representation of attribution remains an open design question.                                                      |
| SF-04 | Uncertain identity                          | The extraction preserves the uncertain possible brand. Targeted downstream checks produced no detections, but broader behavior is not established.                                                         |
| SF-05 | Conflicting text and image evidence         | A same-source guard partially mitigates the observed contradiction false-positive path. This is a heuristic, not general provenance tracking or semantic contradiction analysis.                           |
| SF-06 | Promotional wording versus technical claims | The detector recognizes the seller's unusual-configuration wording, but its output terminology may imply more than the source establishes. No broader code change has been justified by the reviewed case. |

The detailed case records and limitations are maintained in `docs/phase-5-signal-fidelity-audit.md`.

#### Confirmed cross-case findings

The audit has also documented four recurring discrepancies:

- **CF-01 — Image context loss:** A source caveat about a poor camera angle and fuzzy image quality is omitted from the associated extracted evidence.
- **CF-02 — Claim/source-text mismatch:** A claim includes a model identifier that its associated `source_text` does not itself contain, even though the identifier appears elsewhere in the listing.
- **CF-03 — Transaction-context category mismatch:** The instrument-transaction detector relies on `seller_context` Signals, while explicit transaction language can appear under another Signal category. Generic seller context can also satisfy the detector without explicit transaction wording.
- **CF-04 — Configuration claim categorized as identity:** A claim describing a combined configuration is represented as `identity`, even though the unusual-configuration detector recognizes it from its text.

These are observed discrepancies, but their appropriate remedies differ. Each requires a decision based on intended semantics and downstream behavior rather than an automatic schema change.

#### Remaining cross-case question: year normalization

The audit also identified normalized claims in which bare years become statements such as "1992 year model." A year may refer to an instrument, a model, a market context, an album release, or something else.

The presence of a four-digit year is not sufficient to establish a manufacturing date. The source-to-Signal relationship and downstream use of year information require targeted review.

#### Phase 5 exit criteria

Phase 5 is ready to close when:

- Each documented case has been checked against its source material.
- Relevant downstream detector behavior has been inspected.
- Each discrepancy is classified as extraction fidelity, Signal semantics, detector logic, or an unresolved interaction between layers.
- Any proposed code or schema change is justified by a concrete finding and an appropriate evaluation.
- Targeted corrections have regression coverage where applicable.
- The audit records what remains unresolved and avoids claims broader than the evidence supports.

Closing Phase 5 will not automatically authorize a schema redesign, a new scoring system, or a new production feature.

## Current Conceptual Pipeline

The current conceptual sequence is:

1. **Source material** — a public listing, a manually supplied lead, or other relevant source information.
2. **Signals** — structured, source-grounded claims and observations.
3. **Evidence relationships and patterns** — relevant connections, combinations, and tensions among Signals.
4. **Interpretation** — an explanation of why the evidence may be meaningful in context.
5. **Human attention** — an explainable reason to consider further investigation.

This is a conceptual model, not a commitment to a particular production schema or sequence of software components.

Not every listing needs to pass through every stage in the same way. Deterministic detection may identify recognizable structures, while interpretation may be needed to establish why those structures matter. Neither should claim more than the available evidence supports.

## Working Findings

The investigations so far support the following provisional conclusions:

- A useful investigation lead may arise from an individual detail, a combination of Signals, or the context connecting them.
- Source-grounded extraction is necessary but does not guarantee source-grounded downstream reasoning.
- Seller-reported history should remain distinguishable from independently established fact.
- Unknown, ambiguous, or contradictory information should not be silently resolved.
- Signal categories are useful only to the extent that their meanings are sufficiently consistent for downstream consumers.
- Source references improve traceability, but they do not guarantee that a claim is fully supported by its cited text or that an interpretation preserves its meaning.
- Deterministic detectors can identify specific recurring structures, but narrow string-matching rules do not establish general semantic understanding.
- Small, deliberately constructed samples are useful for finding failure modes, but they do not establish broad reliability.

These findings should be revisited when new evidence warrants it.

## Open Questions

### Extraction and traceability

- How should Signals preserve concise claims while retaining the source context needed to understand them?
- What must `source_text` establish for a claim to be considered traceable?
- How should evidence originating from different modalities or passages preserve its source identity?
- How should seller attribution and uncertainty remain visible to downstream consumers?

### Signal semantics

- Are current Signal types sufficiently distinct and consistently applied?
- How should configuration, identity, history, condition, seller context, and market context be distinguished?
- Where a claim spans multiple concepts, should it be represented differently or handled by downstream interpretation?
- Which normalization rules preserve source meaning without introducing unsupported specificity?

### Detection and interpretation

- Which evidence relationships are sufficiently explicit for deterministic detection?
- Which cases require contextual interpretation rather than a pattern match?
- How should a detector express what a source claims without implying independent verification?
- How should contradictions be identified without assuming that different claims are necessarily incompatible?
- What evaluation method would justify a broader claim about detector or interpretation reliability?

### Product and architecture

- Which experimental structures, if any, should become permanent production interfaces or schemas?
- What should remain deterministic, and where does AI add demonstrated value?
- How should a useful observation guide human attention without being mistaken for a valuation, authenticity judgment, or purchase recommendation?

These questions should be pursued when answering them could affect a concrete design decision, not simply because they are technically interesting.

## Next Steps

1. **Continue the Phase 5 audit.** Work through CF-01 through CF-04, checking the source-to-Signal relationship and the relevant downstream consumer for each finding.
2. **Reconcile year normalization.** Confirm how the source context is represented and whether downstream logic receives an appropriately qualified date or year claim.
3. **Classify each discrepancy before changing code.** Distinguish a source-traceability problem from a Signal-category problem or a detector rule that exceeds its intended boundary.
4. **Make only justified, testable corrections.** Add focused regression coverage when a confirmed behavior should change. Do not broaden unrelated logic as part of a local correction.
5. **Close Phase 5 against its exit criteria.** Record resolved issues, partial mitigations, and unresolved limitations in the audit.
6. **Choose any follow-up investigation deliberately.** After the audit, select a specific unanswered question only if it is important enough to warrant a defined evaluation.

The next phase is not predetermined. Phase 5 findings should inform that decision.

## Decision Rule

Before implementing a change, establish:

- **The problem:** What observed behavior or unmet requirement needs attention?
- **The boundary:** Is the problem in extraction fidelity, Signal semantics, detector logic, or interpretation?
- **The evidence:** What source material, test case, or evaluation demonstrates the problem?
- **The intervention:** What is the smallest change that addresses it?
- **The evaluation:** How will the intended improvement and possible regressions be checked?
- **The limitation:** What will remain unproven after the change?

Prefer narrow, reversible changes with relevant regression coverage. Preserve useful existing behavior unless evidence supports changing it.

A completed experiment is a source of evidence, not automatic authorization for a feature.

## Status Summary

| Area                                           | Status                   | Current position                                                      |
| ---------------------------------------------- | ------------------------ | --------------------------------------------------------------------- |
| Initial experiment                             | Completed                | Foundational premise explored                                         |
| Evidence extraction                            | Explored                 | Source-grounded structure established; fidelity is still under audit  |
| Discovery experiments                          | Documented               | Deterministic patterns are useful but incomplete                      |
| Evidence interpretation                        | Exploratory phase closed | Concept established; quality limitations remain                       |
| Phase 5 signal fidelity audit                  | In progress              | Six cases documented; targeted fixes and partial mitigations recorded |
| Cross-case traceability and semantics          | Open                     | Four confirmed findings require disposition                           |
| Year normalization                             | Open                     | Source context and downstream use need reconciliation                 |
| Production architecture                        | Open                     | Must follow from demonstrated needs                                   |
| Permanent scoring or confidence model          | Deferred                 | Not justified by current evidence                                     |
| Automated purchase recommendation or valuation | Out of scope             | Not Hedstok's purpose                                                 |
