# Phase 5 — Signal Fidelity Audit

**Status:** Audit Complete
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

**Follow-up — Dated instrument context boundary**

The detector previously accepted a year in any non-identity signal as dated instrument context. This allowed a market-context claim stating that a year was mentioned in the listing to support a dated configuration/modification pattern, even when the year did not establish the instrument's date.

The detector was narrowed to require explicit year-model context or a year directly associated with a recognized instrument identity. Regression coverage now verifies that a year mentioned only in market context does not establish dated instrument context. An arbitrary-number boundary test also verifies that a claim such as "Fender model 2001" is not sufficient.

**Validation:** 47 tests passed. The historical `extraction2.json` positive test remains intact.

**Conclusion:** The identified false-positive path is covered by regression tests. This does not establish general detector accuracy or validate the underlying listing claims.

### SF-03 — Ambiguity and seller-claim attribution

**Source:** `listing-05`

**Source evidence:** The seller claims that the guitar and the father's playing were featured on several late-1980s metal albums. The listing also attributes buckle scuffs to Kirk Hammett.

**Observed extraction:** The earlier extraction phrased the album association as the guitar being featured on the albums, narrowing the original statement's ambiguity. The revised extraction preserves both the guitar and the father's playing in the album claim. The buckle-scuff claim preserves the asserted origin in its wording but does not separately represent attribution.

**Assessment:** The observed loss of ambiguity in the earlier extraction is corrected in the revised artifact. The revised extraction preserves the seller's claim; it does not independently establish that the claimed recording history or Kirk Hammett association is true. Whether seller attribution should be represented explicitly and consistently remains an unresolved design question.

**Verification boundary:** This comparison evaluates extraction fidelity against the supplied source text. It does not validate the seller's claims or establish general attribution handling across other listings.

**Status:** Earlier album-claim ambiguity concern resolved in the revised extraction. Explicit seller-claim attribution remains a design question; no schema or prompt change is justified by this listing alone.

### SF-04 — Uncertain identity preservation

**Source:** `listing-06`

**Source evidence:** The seller describes a guitar as very old and says the name on it looks like “gibbons or gibson or something.”

**Observed extraction:**

- Identity: `"The top says 'gibbons' or 'gibson' or something similar."`
- Condition: `"The guitar is really old."`

**Assessment:** The extraction preserves uncertainty around the possible brand and retains the general age description without inventing a specific age or manufacture date.

**Downstream checks:** `detect_dated_configuration_modification_history`, `detect_cross_source_contradiction`, and `detect_provenance` returned no detections for this listing. These targeted checks did not demonstrate that the uncertain identity was treated as confirmed. This is limited evidence, not a guarantee for all downstream consumers.

**Status:** No extraction discrepancy observed. Targeted downstream checks completed; broader downstream behavior remains outside this verification.

### SF-05 — Conflicting text and image evidence

**Source:** `listing-11`

**Source evidence:** The text advertises a “1958 Les Paul,” while the accompanying image annotation describes a kid-size Stratocaster-style guitar.

**Observed extraction:** Both the textual identity claim and the conflicting image-derived description are retained as identity signals.

**Assessment:** Retaining both claims is appropriate; silently resolving the contradiction would not be.

**Verify:**

- Text-derived and image-derived evidence remain distinguishable in the extracted signals.
- Conflicting identity claims remain distinguishable.
- Downstream interpretation does not treat contradictory claims as mutually reinforcing evidence for a single identity.

**Mitigation implemented:** `detect_cross_source_contradiction()` now skips pairs of identity signals whose `source_text` values match after trimming surrounding whitespace. An adversarial same-source test confirms that identical source text does not trigger a contradiction; the text/image control test confirms that the existing listing-11-style contradiction is still detected.

**Validation:** Focused contradiction tests passed: **5 passed** (`pytest .\tests\test_detectors.py -k "cross_source_contradiction or same_source_identity_conflict"`).

**Status: Partially mitigated; provenance remains unresolved.** This is a provisional heuristic, not source-provenance tracking. Different excerpts may originate from the same source, and identical excerpts do not formally establish common provenance. The detector still identifies a specific Les Paul/Stratocaster wording pair rather than establishing that the underlying claims are genuinely contradictory. No schema redesign or broader detector changes were made.

### SF-06 — Promotional wording versus technical claims

**Source:** `listing-14`

**Source evidence:** The listing describes a Fender HotShot Telecaster as being in “AS NEW MINT” condition, calls it a “NEW Series,” and says “Tele and Strat in one guitar!”

**Observed extraction:** These statements are represented as condition or identity signals.

**Assessment:** The extraction preserves the seller's promotional claims. `detect_explicitly_unusual_configuration` matches the phrase “Tele and Strat in one guitar” and emits an `explicitly_unusual_configuration` pattern. This detects the presence of the claim; it does not verify the instrument's actual construction. The pattern name and evidence role could nevertheless be read as stronger than the underlying evidence supports. A targeted search of the `hedstok` Python files found no separate handling of “AS NEW MINT” or “NEW Series”; this does not establish how every downstream consumer may interpret these signals.

**Verification:**

- The detector's unit tests cover the promotional phrase and reject ordinary configuration and modification claims.
- The extraction-artifact test expects `listing-14` to be the only listing detected by this detector.
- No independent verification of the seller's configuration or condition claims is performed by this detector.
- The distinction between seller-reported condition and verified physical condition remains a broader semantic boundary, not something established by this detector review.

**Validation:** Focused detector tests passed: **4 passed** (`pytest .\tests\test_detectors.py -k "explicitly_unusual_configuration"`).

**Status:** Detector behavior reviewed; no code change justified by the current evidence. The detector identifies promotional wording, but its output terminology could imply more certainty than the source supports.

## Cross-case observations

The current sample raises four recurring questions:

1. **Uncertainty:** Is uncertainty preserved through the full path from source text to detector result?
2. **Attribution:** Can downstream logic distinguish seller assertions from other forms of evidence?
3. **Specificity:** Does normalization introduce unsupported details, such as interpreting a bare year as a confirmed model year?
4. **Category semantics:** Are signal types sufficiently consistent for the assumptions made by downstream detectors?

These are investigation questions, not confirmed schema defects.

## Confirmed cross-case findings

### CF-01 — Image evidence context loss (listing-03)

The source describes a bad camera angle and fuzzy image quality alongside the observation that two strings are broken. The extracted signal's `source_text` retains only the broken-strings statement.

**Classification:** Source traceability and context preservation discrepancy. The observation is retained, but the image-quality caveat is lost.

### CF-02 — Claim/source-text mismatch (listing-12)

The first identity claim includes model `H954`, but its associated `source_text` contains only the instrument description. The model number appears elsewhere in the original listing, but not in the cited source span for that claim.

**Classification:** Signal traceability discrepancy. The claim is supported by the overall listing, but its associated source text does not independently support the full claim.

**Status:** Confirmed in the audited `extraction2.json` artifact; corrected in `extraction3.json`. The original listing explicitly includes model H954, but the earlier signal's `source_text` did not. The revised artifact's source span includes the model number and supports the full claim. No downstream detector failure was demonstrated during this review.

**Disposition:** Historical extraction traceability discrepancy, corrected in the revised artifact. No additional prompt, schema, or detector change is justified by this case.

### CF-03 — Transaction-context category mismatch

The instrument-transaction detector requires at least one `seller_context` signal alongside instrument evidence. It does not recognize `market_context` signals as transaction evidence. Consequently, explicit sale/trade wording in listing-04 and “make an offer” in listing-08 do not satisfy its transaction-context condition. Conversely, generic seller-context wording in listing-06 and promotional wording in listing-12 can satisfy that condition without an explicit transaction offer.

**Classification:** Confirmed detector-logic limitation interacting with signal semantics. Explicit transaction language in `market_context` signals is missed, while generic or promotional `seller_context` signals can satisfy the detector without an explicit offer.

**Disposition:** Record as a known limitation. Do not broaden detection to all `market_context` signals, because price-only context is insufficient. A future change should define and test the semantic conditions for transaction evidence separately from signal category. No code change is justified within this audit.

### CF-04 — Configuration claim categorized as identity (listing-14)

In `extraction2.json`, “Tele and Strat in one guitar” is categorized as `identity`, although it describes a configuration. The unusual-configuration detector recognizes the claim through text matching without checking the signal type.

In `extraction3.json`, the claim is categorized as `configuration`, correcting the observed signal-semantics inconsistency.

**Classification:** Signal-semantics inconsistency in the historical extraction artifact.

**Status:** Corrected in `extraction3.json`. The detector's existing behavior remains compatible with the revised signal.

**Disposition:** No detector or schema change is justified. The historical artifact-level test remains tied to `extraction2.json`, while a separate regression test verifies the revised `extraction3.json` classification and detector behavior.

## Year normalization — cross-case review

The revised extraction handles years differently depending on context, but ambiguity remains. Listing-01 preserves the statement that the guitar cannot be newer than 1970, rather than assigning an exact date. Listing-02 combines `1992` with the Fender SSH Strat identity claim, supported by its source span. Listing-05 keeps the 1986 album dates within a story signal rather than treating them as the guitar's date.

However, listing-04 still identifies the instrument as a “2006 Rickenbacker 12-string,” even though the source only says “rickenbacker 12-string. 2006.” Listing-10 similarly identifies a “2025 Squier Sonic Stratocaster” without the source explicitly stating that 2025 is a manufacture or model year.

**Classification:** Remaining extraction-semantic ambiguity. The source spans are traceable, but the claims assign an interpretation to years whose precise meaning is not explicit.

**Disposition:** Do not assume that every year adjacent to an instrument description is a confirmed manufacture or model year. Record listings 04 and 10 as bounded ambiguities; do not broaden detector logic or redesign the schema on this evidence alone.

**Status:** Classified for this audit. No code change is required to close Phase 5.

## Exit criteria

This audit is ready to close when:

- Each listed case has been checked against its source text.
- Relevant downstream detector behavior has been inspected.
- Each discrepancy is classified as extraction fidelity, signal semantics, detector logic, or an unresolved interaction between layers.
- Any proposed code or schema change is justified by a documented finding.
- No redesign is undertaken solely on the basis of a hypothetical concern.

Closing this audit does not itself authorize a scoring-model change, a schema redesign, or broader project scope.

## Current conclusion

The reviewed cases have been assessed across extraction fidelity, Signal semantics, and downstream detector behavior. The audit identified bounded context and traceability discrepancies, a transaction-context detector limitation, a corrected configuration categorization, and remaining ambiguity in year interpretation.

The findings do not justify broad extraction, detector, or schema changes. Known limitations and unresolved ambiguities are documented with their dispositions. Any future changes should be driven by concrete evidence and evaluated against the intended semantics, with regression coverage where applicable.

**Status:** Audit complete. Findings classified; no additional code or schema changes are required to close Phase 5.
