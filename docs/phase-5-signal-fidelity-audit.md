# Phase 5 — Signal Fidelity Audit

**Status:** Investigation in progress  
**Purpose:** Compare source listing text with extracted signals and downstream detector interpretation before making detector changes.

## Objective

Verify that extracted signals faithfully represent their source evidence and that downstream detectors do not infer more than the evidence supports.

The audit distinguishes three layers:

1. **Extraction fidelity:** Does the extracted signal preserve the source's meaning, uncertainty, attribution, and context?
2. **Signal semantics:** Does the signal's type and claim accurately describe the evidence without adding unsupported specificity?
3. **Detector interpretation:** Does the detector infer only what the selected evidence can establish?

These layers must be evaluated separately. A detector failure must not automatically be treated as an extraction failure, and extraction changes must not be used to conceal overreaching detector logic.

## Scope and constraints

- Use `experiment-0/input/listings.json` as the source text for the current fixtures.
- Use `extraction2.json` as the extracted-signal artifact under audit.
- Preserve seller claims as claims; do not independently validate them or infer instrument value.
- Preserve explicit uncertainty, attribution, and contradictions.
- Do not change extraction prompts, signal schemas, or detector logic until the relevant discrepancy has been classified.
- Record observations separately from confirmed defects.
- Limit this investigation to the cases below unless new evidence demonstrates that additional cases are necessary.

## Audit cases

### SF-01 — Explicit uncertainty preservation

**Source:** `listing-01`

**Source evidence:** The seller does not know the guitar's age or manufacturer, says it cannot be newer than 1970, describes it as acoustic, is unsure whether it has electronics, and thinks the manufacturer's name might start with M.

**Observed extraction:** The signals preserve the unknown age, the 1970 lower bound, uncertainty about electronics, and the tentative manufacturer initial.

**Assessment:** No obvious material loss of uncertainty in the current extraction.

**Verify:**

- A lower age bound is not interpreted as a confirmed manufacturing year.
- A possible manufacturer initial is not treated as a confirmed identity.
- Uncertainty remains available to downstream interpretation.

**Status:** No discrepancy confirmed; downstream behavior not yet audited.

### SF-02 — Configuration versus modification history

**Source:** `listing-02`

**Source evidence:** Off-brand active pickups are described as installed, original pickups are included, the guitar is set up for heavy-gauge strings, and a locking nut is described as installed.

**Observed extraction:** These details are represented as configuration signals.

**Assessment:** The extraction is broadly faithful. However, the presence of a configuration does not necessarily establish when it was introduced, who introduced it, or whether it represents a modification from an original state. Heavy-gauge strings in particular do not independently establish modification history.

**Verify:**

- Configuration evidence is not automatically treated as evidence of a modification.
- Claims of installation are not expanded into unsupported chronology or provenance.
- The dated-modification detector requires evidence sufficient to support the specific interpretation it returns.
- A dated instrument plus configuration evidence such as heavy-gauge strings must not automatically establish modification history.

**Status:** The detector initially accepted heavy-gauge strings as core modification evidence. After removing `"heavy gauge"` from `core_terms`, the negative boundary test passes, while the existing listing-02 positive test continues to pass. Focused and full test suites both pass (35 tests). The detector's other configuration-related terms have not yet been comprehensively audited.

### SF-03 — Ambiguity and seller-claim attribution

**Source:** `listing-05`

**Source evidence:** The seller claims that the guitar and the father's playing were featured on several late-1980s metal albums. The listing also attributes buckle scuffs to Kirk Hammett.

**Observed extraction:** The album claim is phrased as the guitar being featured on the albums, which may narrow the original ambiguity. The buckle-scuff claim preserves the asserted origin in its wording but does not separately represent attribution.

**Assessment:** Potential loss of ambiguity and unclear consistency in attribution handling.

**Verify:**

- Ambiguous source statements are not converted into more definite claims.
- Seller-provided claims remain distinguishable from independently established facts.
- Attribution is preserved consistently where a claim's origin matters to interpretation.

**Status:** Potential extraction or representation issue; schema implications not yet determined.

### SF-04 — Uncertain identity preservation

**Source:** `listing-06`

**Source evidence:** The seller describes a guitar as very old and says the name on it looks like “gibbons or gibson or something.”

**Observed extraction:** The signal preserves the uncertain wording in the identity claim.

**Assessment:** The extraction appears appropriately cautious.

**Verify:**

- Downstream logic does not treat the uncertain brand reference as a confirmed manufacturer.
- General descriptive language such as “really old” is not silently converted into a specific age or date.

**Status:** No extraction discrepancy observed; downstream behavior not yet audited.

### SF-05 — Conflicting text and image evidence

**Source:** `listing-11`

**Source evidence:** The text advertises a “1958 Les Paul,” while the accompanying image annotation describes a kid-size Stratocaster-style guitar.

**Observed extraction:** Both the textual identity claim and the conflicting image-derived description are retained as identity signals.

**Assessment:** Retaining both claims is appropriate; silently resolving the contradiction would not be.

**Verify:**

- Text-derived and image-derived evidence retain their provenance.
- Conflicting identity claims remain distinguishable.
- Downstream interpretation does not treat contradictory claims as mutually reinforcing evidence for a single identity.

**Status:** Contradiction preserved in extraction; downstream handling not yet audited.

### SF-06 — Promotional wording versus technical claims

**Source:** `listing-14`

**Source evidence:** The listing describes a Fender HotShot Telecaster as being in “AS NEW MINT” condition, calls it a “NEW Series,” and says “Tele and Strat in one guitar!”

**Observed extraction:** These statements are represented as condition or identity signals.

**Assessment:** The extraction preserves the listing's claims. The concern is whether downstream logic assigns them a stronger technical meaning than the source warrants.

**Verify:**

- Promotional wording is not treated as independent technical verification.
- “Tele and Strat in one guitar” remains a seller claim unless supported by evidence appropriate to the intended interpretation.
- Condition language is distinguished from verified physical condition where that distinction matters.

**Status:** Downstream semantic boundary to be investigated.

## Cross-case observations

The current sample raises four recurring questions:

1. **Uncertainty:** Is uncertainty preserved through the full path from source text to detector result?
2. **Attribution:** Can downstream logic distinguish seller assertions from other forms of evidence?
3. **Specificity:** Does normalization introduce unsupported details, such as interpreting a bare year as a confirmed model year?
4. **Category semantics:** Are signal types sufficiently consistent for the assumptions made by downstream detectors?

These are investigation questions, not confirmed schema defects.

## Known limitation: year normalization

Listings 02, 04, and 10 normalize bare years into claims such as “1992 year model,” “2006 year model,” and “2025 year model.” Listing-01 correctly preserves a lower-bound statement rather than converting it into a manufacturing year. Listing-05 also contains years in the context of album releases.

The audit must determine whether year normalization consistently respects source context. A four-digit year alone must not be assumed to describe the instrument's manufacture date.

**Status:** Cross-case question; requires targeted source-to-signal and downstream review.

## Exit criteria

This audit is ready to close when:

- Each listed case has been checked against its source text.
- Relevant downstream detector behavior has been inspected.
- Each discrepancy is classified as extraction fidelity, signal semantics, detector logic, or an unresolved interaction between layers.
- Any proposed code or schema change is justified by a documented finding.
- No redesign is undertaken solely on the basis of a hypothetical concern.

Closing this audit does not itself authorize a scoring-model change, a schema redesign, or broader project scope.

## Current conclusion

The sampled extraction is generally faithful, and several cases preserve uncertainty or contradictory evidence appropriately. Potential issues remain around ambiguity, attribution, year normalization, and the boundary between configuration and modification history.

No broad extraction or detector changes are justified by this audit alone. The next step is to inspect downstream interpretation for the documented cases and classify concrete discrepancies before implementing fixes.
