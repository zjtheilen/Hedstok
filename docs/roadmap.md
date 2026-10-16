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

**Current milestone: Phase 5 complete — audit closed.**

Phases 1–4 established an experimental foundation for extracting structured evidence, detecting evidence patterns, and investigating evidence-grounded interpretation.

Phase 5 audited the boundary between source material, extracted Signals, and deterministic detector behavior. The audit identified bounded extraction-fidelity and traceability discrepancies, a transaction-context detector limitation, a corrected configuration categorization, and remaining ambiguity in year interpretation.

The findings have been classified and documented. Targeted regression coverage has been added where applicable. The audit did not justify broad extraction, detector, schema, or architectural changes.

Phase 5 is closed. Its unresolved limitations remain documented findings, not blockers to audit closure.

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

**Status: Complete — audit closed**

Phase 5 investigated whether extracted Signals faithfully represent their source material and whether downstream detectors infer more than the evidence supports.

The audit separated three layers:

1. **Extraction fidelity:** Does the Signal preserve the source's meaning, uncertainty, attribution, and relevant context?
2. **Signal semantics:** Does the Signal's type and claim accurately represent the evidence?
3. **Detector interpretation:** Does the detector's output stay within what its input evidence supports?

These layers were assessed separately. A source-to-Signal mismatch does not automatically establish a detector defect, and a detector defect should not be hidden by changing extraction wording.

#### Audited signal-fidelity cases

| Case  | Focus                                       | Final assessment                                                                                                                                                                               |
| ----- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SF-01 | Explicit uncertainty                        | The sampled extraction preserves uncertainty and lower-bound language. No broader reliability claim is established.                                                                            |
| SF-02 | Configuration versus modification history   | The heavy-gauge-string false-positive path was addressed, and dated-instrument context was narrowed and tested. The audit did not establish a need for a comprehensive detector-term redesign. |
| SF-03 | Ambiguity and seller-claim attribution      | The revised extraction preserves ambiguity around the album claim. Consistent explicit representation of attribution remains a broader design question.                                        |
| SF-04 | Uncertain identity                          | The extraction preserves the uncertain possible brand. Targeted downstream checks produced no detections; broader behavior remains unproven.                                                   |
| SF-05 | Conflicting text and image evidence         | A same-source guard partially mitigates the observed contradiction false-positive path. It is a heuristic, not general provenance tracking or semantic contradiction analysis.                 |
| SF-06 | Promotional wording versus technical claims | The detector recognizes the seller's unusual-configuration wording, but its terminology may imply more than the source establishes. No broader code change was justified by the reviewed case. |

The detailed case records and limitations are maintained in `docs/phase-5-signal-fidelity-audit.md`.

#### Confirmed cross-case findings

The audit documented four recurring discrepancies and their dispositions:

- **CF-01 — Image context loss:** The source caveat about a poor camera angle and fuzzy image quality is omitted from the associated extracted evidence. This is a bounded context-fidelity inconsistency. A broader downstream detector failure was not established, so no general provenance redesign was justified.
- **CF-02 — Claim/source-text mismatch:** The historical extraction included a model identifier in a claim that its associated `source_text` did not contain, although the identifier appeared elsewhere in the listing. The revised extraction includes the identifier in the supporting source text, correcting the documented traceability mismatch.
- **CF-03 — Transaction-context category mismatch:** The transaction detector relies on `seller_context` Signals, while explicit transaction language can appear under another Signal category. Generic seller context can also satisfy the detector without explicit transaction wording. This remains a detector-logic limitation interacting with Signal semantics. Broader detection changes require explicit semantic criteria and targeted evaluation.
- **CF-04 — Configuration claim categorized as identity:** The historical extraction categorized a combined Tele/Strat configuration claim as `identity`. The revised extraction categorizes it as `configuration`. The existing unusual-configuration detector recognizes the claim text, and regression coverage now verifies the revised classification and detector behavior.

These findings have been dispositioned according to their demonstrated scope. They do not collectively justify automatic schema changes or a broad redesign.

#### Remaining cross-case question: year normalization

The audit reviewed cases in which bare years were normalized into claims assigning a year to an instrument. The source context varies: listing-01 expresses a lower bound, listing-02 associates a year with a Fender SSH Strat, listing-05 mentions an album-release year, and listings 04 and 10 leave room for ambiguity about whether the year refers to the instrument.

The remaining ambiguity in listings 04 and 10 does not justify broad changes to year normalization. A four-digit year alone is insufficient to establish a manufacturing date, and future changes should be based on concrete source-context requirements and downstream use.

#### Phase 5 closure

The audit's exit criteria have been met:

- Documented cases were checked against their source material.
- Relevant downstream detector behavior was inspected.
- Findings were classified across extraction fidelity, Signal semantics, detector logic, and interactions between those layers.
- Proposed changes were evaluated against concrete findings rather than hypothetical concerns.
- Targeted regression coverage was added where applicable.
- Resolved discrepancies, partial mitigations, and unresolved limitations were recorded.

**Closure decision:** Phase 5 is complete. No additional code or schema changes are required to close the audit.

This closure does not authorize a schema redesign, a new scoring system, or a new production feature.

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

The questions below remain available for future investigation. They are not outstanding Phase 5 closure requirements.

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

Phase 5 no longer has outstanding work. The next phase is deliberately undecided.

1. **Choose a concrete question.** Select an unresolved issue only if its answer could materially affect Hedstok's design or usefulness.
2. **Define the evaluation before implementation.** Identify the evidence, expected behavior, and criteria that would support a decision.
3. **Keep the scope narrow.** Prefer a focused experiment or targeted correction over a generalized redesign.
4. **Preserve the findings.** Document what the experiment demonstrates, what it fails to establish, and whether any follow-up is warranted.
5. **Defer production commitments.** Do not promote experimental patterns, schemas, scoring, or interpretation approaches into permanent product behavior without sufficient evidence.

No specific next phase is prescribed by the completion of Phase 5.

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

| Area                                           | Status                              | Current position                                                                         |
| ---------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------- |
| Initial experiment                             | Completed                           | Foundational premise explored                                                            |
| Evidence extraction                            | Explored                            | Source-grounded structure established; fidelity limitations documented                   |
| Discovery experiments                          | Documented                          | Deterministic patterns are useful but incomplete                                         |
| Evidence interpretation                        | Exploratory phase closed            | Concept established; quality limitations remain                                          |
| Phase 5 signal fidelity audit                  | Complete — audit closed             | Cases reviewed, findings classified, targeted regression coverage added where applicable |
| Cross-case traceability and semantics          | Findings dispositioned              | CF-01 through CF-04 documented with bounded conclusions                                  |
| Year normalization                             | Reviewed; bounded ambiguity remains | Listings 04 and 10 retain ambiguity; no broad change justified                           |
| Production architecture                        | Open                                | Must follow from demonstrated needs                                                      |
| Permanent scoring or confidence model          | Deferred                            | Not justified by current evidence                                                        |
| Automated purchase recommendation or valuation | Out of scope                        | Not Hedstok's purpose                                                                    |
