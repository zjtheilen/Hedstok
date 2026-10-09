# Hedstok — Phase 4: Evidence Interpretation Experiments

## Purpose

Phase 4 investigates how Hedstok can interpret structured, source-grounded Signals to explain why a musical-instrument listing may deserve closer human attention.

Phase 3 established an experimental boundary between AI-assisted extraction and deterministic discovery. Phase 4 examines the next conceptual step: interpreting evidence in context rather than merely identifying patterns.

The central question is:

> Given the available evidence, can Hedstok produce a useful, explainable reason to look more closely at a listing without overstating what the evidence establishes?

The desired output is not a purchase recommendation, valuation, or claim of authenticity.

It is an observation that communicates:

> **“Hey. Look at this one.”**

This document preserves the experimental history and findings. Its conclusions should not be treated as automatic authorization for production changes.

### Phase 4.1 — Manual Opportunity Construction

#### Purpose

The first Phase 4 experiment will establish what a candidate acquisition opportunity looks like before introducing a formal opportunity model or implementation.

The experiment will use the existing Phase 3 evidence artifacts to manually construct candidate opportunities from structured Signals. The purpose is to determine whether opportunities can be described consistently while remaining useful, explainable, and constrained by the available evidence.

No new extraction calls or external market data will be used.

#### Core Question

> **Can candidate acquisition opportunities be constructed from existing Signals in a way that is useful, explainable, and disciplined by the available evidence?**

#### Inputs

The experiment will use:

- `experiment-0/input/listings.json`;
- `extraction2.json`;
- the experimental evidence-pattern detector results established during Phase 3; and
- the human investigation decisions established during Phase 3.

The experiment will not make new AI extraction or discovery calls.

#### Experimental Cases

The initial experiment will use five deliberately different listings:

| Listing | Purpose                                                             |
| ------- | ------------------------------------------------------------------- |
| 05      | Multi-Signal provenance                                             |
| 11      | Cross-source contradiction                                          |
| 09      | Seller/inventory opportunity                                        |
| 06      | Uncertain identity with additional clues                            |
| 01      | Potential opportunity without an existing evidence-pattern detector |

These cases are intended to test different relationships between evidence patterns and candidate opportunities rather than to represent a statistically complete evaluation.

#### Manual Candidate Structure

Each candidate opportunity will initially be described using:

- **listing** — the source listing associated with the candidate;
- **what appears worth investigating** — a concise description of the potential opportunity;
- **why** — the interpretation connecting the available evidence to the potential investigation;
- **supporting Signals** — the specific Signals supporting the candidate; and
- **uncertainty** — relevant claims, ambiguities, or limitations that remain unresolved.

This is an experimental description format rather than a proposed production data model.

#### Evaluation Boundaries

Each manually constructed candidate will be evaluated against the following questions:

1. **Investigation usefulness** — does the available evidence provide a reasonable basis for further investigation?
2. **Evidence grounding** — can the candidate and its explanation be traced to specific Signals?
3. **Interpretation discipline** — does the candidate avoid introducing significance or factual claims not established by the available evidence?
4. **Uncertainty preservation** — does the candidate preserve uncertain, attributed, or reported claims rather than presenting them as established facts?
5. **Pattern dependency** — does the candidate depend on an existing evidence pattern, or can a useful opportunity arise without one?
6. **Evidence composition** — can multiple Signals or multiple evidence patterns contribute to a single candidate opportunity?

The experiment will distinguish between the presence of evidence and the significance assigned to that evidence. A candidate may justify investigation without establishing that an instrument is authentic, valuable, rare, desirable, historically significant, or otherwise superior.

#### Expected Findings

The experiment will document:

- candidate opportunities that can be constructed directly from existing evidence patterns;
- candidates requiring combinations of multiple Signals;
- candidates that do not correspond to an existing evidence pattern;
- cases where uncertainty itself contributes to the reason for investigation;
- cases where the available evidence is insufficient to justify a candidate; and
- recurring constraints or structures that may inform a future opportunity representation.

False positives and rejected candidates are useful experimental results. They may identify boundaries where an apparent opportunity does not withstand evidence-grounded review.

#### Completion Criterion

Phase 4.1 will be considered complete when the five cases have been manually evaluated and the experiment has established:

1. whether candidate opportunities can be described consistently from existing evidence;
2. whether their explanations can remain grounded in specific Signals;
3. whether uncertainty can be preserved without weakening the usefulness of the candidate;
4. whether opportunities can arise without a pre-existing evidence pattern; and
5. what, if any, common structure appears justified for future implementation.

The experiment will not establish a permanent opportunity schema or require implementation. Its purpose is to determine whether the concept of a candidate acquisition opportunity is sufficiently coherent to justify further development.

### Phase 4.1 Findings

The five experimental cases demonstrated that candidate acquisition opportunities can be described consistently using a common descriptive structure while accommodating substantially different evidence configurations. The structure remained applicable to provenance, contradiction, seller/inventory context, uncertain identity, and opportunities arising directly from combinations of Signals without an existing evidence pattern.

The cases also demonstrated that candidate opportunity explanations can remain grounded in specific Signals across different opportunity types. In each case, the explanation could be traced to the evidence that motivated the investigation, including cases where an existing evidence pattern was present and cases where the opportunity arose directly from a combination of Signals. Evidence-pattern detection is therefore not required to maintain traceability between an opportunity and its supporting evidence.

The experiment demonstrated that uncertainty can be preserved within a candidate opportunity without eliminating its usefulness. Unverified provenance, conflicting identity evidence, unresolved identification, attributed claims, and incomplete seller context could remain explicitly uncertain while still providing a reasonable basis for further investigation. In some cases, particularly conflicting or unresolved identity evidence, the uncertainty itself was part of what made the candidate worth investigating. The experiment provides no evidence that a confidence value is necessary for the basic opportunity concept.

The Listing 01 case demonstrated that a candidate acquisition opportunity can arise from a combination of Signals without a pre-existing evidence-pattern classification. This indicates that evidence patterns can provide useful inputs to opportunity interpretation without being a required intermediate step for every candidate. Evidence patterns remain useful representations of recurring evidence structures, but they do not need to act as a mandatory gate between Signals and opportunities.

Across the five cases, a recurring conceptual structure emerged for candidate acquisition opportunities. A candidate identifies something potentially worth investigating, provides an explanation for why it appears worth investigating, references the supporting evidence, and preserves relevant uncertainty or limitations. Supporting evidence may consist of individual Signals, detected evidence patterns, or combinations of both.

This recurring structure is sufficient to describe the experimental cases, but the experiment does not establish that it should become a permanent production schema. Further experimentation may reveal additional requirements or distinctions.

### Phase 4.1 Completion Assessment

**This criterion has been met experimentally.**

The five cases demonstrated that candidate acquisition opportunities can be constructed from existing source-grounded evidence, described consistently, explained through specific supporting Signals, and kept useful without resolving underlying uncertainty. The experiment also demonstrated that opportunities can arise without a pre-existing evidence pattern and identified a recurring conceptual structure that can describe the cases.

These findings justify further investigation of candidate opportunity representation and interpretation. They do not yet establish a permanent opportunity schema, production architecture, or implementation approach.

**Multiple opportunities within one listing**: Edge case 08 demonstrated that a single listing can contain multiple distinct candidate acquisition opportunities. These may arise from different instruments, historical associations, seller/inventory context, or transaction circumstances. This suggests that candidate opportunities should not be assumed to have a one-to-one relationship with listings.

## Phase 4.2 — Story and Surface-Worthiness Boundary

### Purpose

Phase 4.2 investigates the boundary between an instrument having an interesting story and an instrument being worth surfacing to a person looking for instruments to potentially acquire.

The experiment is intended to test whether “story” alone is an adequate description of the desired Hedstok behavior, or whether additional characteristics determine whether a story or other evidence should result in:

> **“Hey. Look at this one.”**

The experiment uses manually constructed synthetic cases and human judgment. No new AI extraction calls, external market data, or implementation changes are used.

### Experimental Question

> **What makes an instrument's available evidence worth surfacing to a person looking for instruments to potentially acquire?**

The experiment specifically examines:

- whether a story must be unusual, unresolved, or historically significant to be worth surfacing;
- whether meaningful personal history can be sufficient;
- whether uncertainty is useful only when accompanied by additional clues or questions;
- whether unusual configuration or other non-narrative evidence can justify surfacing;
- whether a compelling story can still be unsuitable for surfacing when the instrument is explicitly unavailable;
- whether a story or evidence must be attached to a specific instrument rather than only to a person or collection;
- whether multiple ordinary pieces of evidence can combine into a meaningful reason to look closer;
- whether unsupported claims of rarity, fame, value, or significance should influence the decision.

### Experimental Findings

The boundary cases suggest that Hedstok is not simply looking for “good stories.”

An instrument may be worth surfacing because the available evidence creates a meaningful reason to stop and look closer. That reason may take several forms, including:

- meaningful personal or ownership history;
- a specific historical association or provenance claim;
- an unresolved identity or historical question;
- conflicting or unusual evidence;
- a meaningful relationship between an instrument and a person, event, or circumstance;
- a combination of individually ordinary Signals that produces a more compelling overall story;
- unusual characteristics that create a meaningful question or context.

The story does not need to be verified, famous, rare, or objectively important. A documented family history can be worth surfacing even when there is little unresolved uncertainty, while an unsupported claim of fame or rarity should not be treated as established significance.

Similarly, uncertainty by itself is not sufficient. An unknown instrument with no identifying clues does not necessarily provide a useful reason to look closer. Uncertainty becomes more useful when the available evidence provides a meaningful path, question, contradiction, or connection for further investigation.

The experiment also reinforced that unusualness alone is not sufficient. A strange specification, unexplained marking, or other unusual detail may be interesting without creating a reason to surface the instrument.

### Acquisition Context

The experiment clarified an important distinction in Hedstok's intended behavior.

Hedstok is concerned with instruments that a person might potentially acquire, but it is not intended to decide whether an instrument should be purchased.

The desired behavior is closer to:

> **“Hey. Look at this one.”**

rather than:

> **“You should buy this.”**

An interesting story therefore does not automatically justify surfacing an instrument. If the available evidence explicitly indicates that the instrument is not available and will not be sold, the story may remain interesting without being relevant to the acquisition-oriented purpose of Hedstok.

This does not mean Hedstok needs to establish that an instrument is definitely available before surfacing it. Rather, explicit evidence that an instrument is unavailable can provide a meaningful boundary against surfacing an otherwise compelling story.

### Evidence Discipline

The cases further reinforce the distinction between an interesting claim and evidence supporting that claim.

A seller's assertion that an instrument belonged to a famous musician, is rare, or represents an investment opportunity does not establish those characteristics merely because they appear in the listing.

Likewise, a handwritten note, photograph, family account, or other source can provide a reason to investigate without establishing that the underlying historical claim is true.

Hedstok should therefore preserve the distinction between:

> **“This evidence gives us a reason to look closer.”**

and:

> **“This claim has been established as true.”**

### Provisional Interpretation

The Phase 4.2 cases suggest a more useful working concept than simply “interesting story”:

> **Hedstok should identify instruments whose available evidence gives a person a meaningful reason to stop and look closer, in the context of finding instruments to potentially acquire.**

Stories and story potential appear to be major sources of those reasons, but they are not the only possible source. The relevant property is the relationship between the evidence, the specific instrument, and the reason a person might want to pay attention to it.

This remains a provisional interpretation rather than a formal definition or production rule.

The experiment does not establish a scoring model, ranking mechanism, permanent opportunity schema, or automated judgment process. Its purpose is to clarify the conceptual boundary that future experiments can test.

### Completion Assessment

**This criterion has been met experimentally.**

The Phase 4.2 cases demonstrated that:

- compelling stories are not necessarily sufficient by themselves;
- meaningful personal history can justify surfacing;
- uncertainty can contribute to a reason for investigation without being sufficient on its own;
- unusual characteristics do not automatically constitute a reason to surface;
- unsupported claims of significance should not be treated as evidence of significance;
- explicit unavailability can distinguish an interesting story from a relevant acquisition-oriented observation;
- a meaningful story or evidence relationship should generally be connected to a specific instrument;
- the desired behavior is better described as surfacing a reason for human attention than making an acquisition recommendation.

These findings provide a stronger conceptual boundary for future Phase 4 work while preserving the exploratory nature of the project.

## Phase 4.3 — Interpretation as a Derived Reason for Attention

### Research question

Can a reason to look more closely be understood as an interpretation derived from existing evidence, rather than as another type of evidence?

### Working conceptual pipeline

The experiment considered the following sequence:

1. Source listing
2. Extracted Signals
3. Evidence patterns and relationships
4. Interpretation — what is interesting here?
5. Acquisition context — is this relevant to what we are looking for?
6. Surface observation — “Hey. Look at this one.”

The purpose of this model was to distinguish the source information from the interpretation that emerges from it.

### Findings

**A reason for attention is derived, not extracted.**

A reason to investigate is an interpretation of existing evidence. It should not be treated as an independent Signal unless the source itself states something that qualifies as a Signal.

**Evidence composition can matter.**

Several Signals may combine to create a meaningful reason for attention. However, a single strong Signal may also be sufficient. A fixed requirement for multiple Signals would exclude potentially valid cases without justification.

**Context changes significance.**

A compelling family history may make an instrument interesting, but that history does not necessarily create an acquisition opportunity. For example, an instrument with a meaningful personal story may not be available for sale.

The interpretation and the acquisition context therefore need to remain conceptually distinct.

**Uncertainty can be relevant.**

An unresolved identification or unclear provenance may contribute to a reason for further investigation when there is additional evidence that makes the uncertainty meaningful.

Uncertainty alone should not automatically become an opportunity.

**A rigid taxonomy is not justified.**

The experiment did not establish that reasons for attention could be reduced to a permanent set of categories.

### Conclusion

The findings support treating a reason for attention as a derived interpretation grounded in evidence and context.

A provisional description is:

> A reason for attention is an interpretation of available evidence that explains why a listing may warrant closer human examination.

The terms _attention reason_, _surface observation_, _candidate_, and _opportunity_ remain provisional. This experiment did not justify a permanent schema, fixed field set, or naming decision.

No production change was warranted solely by this conceptual finding.

---

## Phase 4.4 — What Makes a Listing Worth Looking At?

### Research question

Does a listing become worth examining because of one particular evidence category, or can different configurations of evidence and context support that judgment?

### Experimental context

The experiment used examples drawn from Dan's instrument interests and acquisition context.

The examples included:

- A homemade EVH Frankenstein associated with a favorite artist
- A Mark Tremonti signature model connected to an exclusive event
- An Epiphone Lucille reportedly signed by B.B. King and purchased at a local casino where it was signed
- A headless eight-string Strandberg associated with a local artist who needed money
- Surf-style guitars
- A Gibson SG Bass
- A Mark Hoppus signature bass associated with a local church
- A customized Les Paul reportedly featured in _Hot Rod_, with a limited run of 150
- Visually distinctive rock and metal instruments
- Familiar Stratocaster, Telecaster, and Les Paul models

These examples were not intended to establish universal rules for which instruments are interesting. They provided contrasting cases for examining what might warrant attention.

### Controlled variation

The experiment varied the context around an ordinary Stratocaster example.

The variations included:

- An ordinary baseline listing
- Unusual custom appearance
- Association with a local musician
- A claim about historical use
- Transaction context
- A recognizable or relevant model
- A generic personal story
- Personal preference

The purpose was to see whether changing one aspect of the available information changed the reason to investigate.

### Findings

**There is no single threshold that explains all surface-worthy cases.**

Different combinations of evidence can produce different judgments.

**Distinctive appearance can be sufficient in some contexts.**

An unusual instrument or configuration may provide a reason to look more closely even without a compelling provenance story.

**Human and historical context can strengthen a case.**

A local musician association, reported history, or other contextual detail may make a listing more interesting than its specifications alone would suggest.

**Transaction context can affect borderline cases.**

Seller circumstances and the context of a transaction may matter, but they do not automatically establish that an instrument is a good deal or that the seller's claims are accurate.

**A distinctive model or identity may be enough.**

A recognizable or personally relevant model can warrant attention in the right context, without requiring multiple additional Signals.

**Personal preference is contextual rather than universally sufficient.**

A person's preferences can affect whether a listing deserves attention, but preference alone did not consistently produce a surface-worthy judgment across the examples.

**Ordinary instruments are not automatically excluded.**

A familiar Stratocaster, Telecaster, or Les Paul may still deserve attention when other evidence or context makes it meaningful.

### Conclusion

Surface-worthiness is not tied to one evidence category. A story may be important, but a story is not mandatory. A distinctive instrument may be interesting, but distinctiveness alone is not a universal rule.

The judgment emerges from evidence and context.

A provisional definition is:

> **Surface-worthiness is the presence of a meaningful, explainable reason for human attention arising from the available evidence and relevant context.**

This definition remains provisional. The experiment did not establish a numerical threshold, permanent reason taxonomy, or deterministic classification rule.

No production change was justified by this experiment alone.

---

## Phase 4.5 — Baseline AI Interpretation

### Research question

Can an AI model interpret structured, source-grounded Signals and produce a useful explanation of why a listing deserves attention?

### Experimental approach

The model was given structured Signals and asked to interpret them rather than independently discover evidence from an unstructured listing.

The experimental output included:

- **Observation:** The interpretation of the listing
- **Supporting Signals:** The evidence supporting that interpretation
- **Uncertainty:** What remained unknown or unresolved
- **Surface judgment:** Yes, maybe, or no

The model was not intended to verify external facts, estimate market value, or recommend a purchase.

The experiment used eight interpretation cases.

### Findings

The initial run produced the expected output structure for all eight cases, but structural completion did not guarantee interpretation quality.

The human comparison found several recurring weaknesses:

- Too many Signals were selected as supporting evidence.
- Relationships among Signals were sometimes missed.
- Uncertainty was not consistently expressed in a useful way.
- Some interpretations treated rarity or value claims and an asking-price discrepancy as an acquisition opportunity without adequate support.
- Some judgments were more conservative than the human target.

Surface-judgment agreement with the human targets was **4/8**.

### Conclusion

The experiment showed that an AI model could produce structured interpretations from extracted evidence, but the baseline was not sufficiently consistent to justify relying on it as the sole authority for surfacing listings.

The most promising role was an interpretive component operating after structured evidence extraction—not an unrestricted model asked to decide what is interesting from scratch.

This was an exploratory baseline, not a production-quality benchmark.

---

## Phase 4.6 — Targeted Interpretation Guidance

### Research question

Can targeted prompt guidance improve the model's interpretation of relationships among Signals, its handling of uncertainty, and its surface judgments?

### Experimental approach

The experiment retained the same eight cases, model, input structure, output schema, and general constraints used in Phase 4.5.

The prompt added more targeted guidance about:

- Relationships among Signals
- Uncertainty relevant to the interpretation
- The distinction between evidence and acquisition implications

The purpose was to test the effect of the additional guidance without intentionally changing the rest of the experimental setup.

### Surface-judgment comparison

| Case      | Human target | Phase 4.5 | Phase 4.6 |
| --------- | ------------ | --------- | --------- |
| interp-01 | Yes          | Maybe     | Yes       |
| interp-02 | No           | No        | No        |
| interp-03 | No           | No        | No        |
| interp-04 | Yes          | Maybe     | Maybe     |
| interp-05 | Yes          | Maybe     | Yes       |
| interp-06 | Yes          | Yes       | Yes       |
| interp-07 | Maybe        | Yes       | Maybe     |
| interp-08 | Yes          | Yes       | Yes       |

Agreement increased from **4/8 in Phase 4.5 to 6/8 in Phase 4.6**.

This improvement was limited to the tested cases. It does not establish general reliability.

### Findings

The targeted guidance improved some surface judgments, particularly cases where the baseline was too conservative or treated an uncertain acquisition implication too strongly.

However, several weaknesses remained:

- The model continued to select too many supporting Signals.
- Relationships among Signals were not consistently interpreted well.
- Uncertainty was not always relevant, precise, or sufficiently qualified.

Improved label agreement did not necessarily mean that the model had selected better evidence or produced a more faithful explanation.

### Conclusion

Targeted interpretation guidance showed promise, but it did not resolve the evidence-selection and uncertainty problems.

The experiment did not justify a production change. The next investigation needed to examine supporting-evidence selection more directly rather than focusing primarily on the surface label.

---

## Phase 4.7 — Supporting-Evidence Selection

### Research question

Can targeted guidance improve the model's selection of supporting Signals by encouraging it to:

- Select evidence directly relevant to the interpretation
- Omit incidental information
- Prefer relevant evidence over indiscriminate inclusion
- Retain enough evidence to support the interpretation
- Preserve the source's meaning and wording faithfully

### Experimental approach

The experiment used the same eight cases, model, input, and general output structure.

The prompt explicitly requested supporting evidence that was directly relevant to the interpretation. It instructed the model to exclude incidental details, preserve original wording, and avoid imposing an arbitrary limit on the number of supporting Signals.

The run initially encountered a temporary Gemini 503 error, then completed successfully using `gemini-3.5-flash-lite`.

### Results

Surface-judgment agreement was **5/8**, compared with:

- Phase 4.5: 4/8
- Phase 4.6: 6/8
- Phase 4.7: 5/8

The number of supporting Signal selections fell from **66 in Phase 4.6 to 36 in Phase 4.7**, a reduction of approximately 45%.

The reduction demonstrated a change in selection behavior. It did not, by itself, prove that the selected evidence was better.

### Case-level findings

#### interp-01 — Family provenance

The model omitted important family-ownership context, including the mother's ownership and church-band history.

This weakened the coverage of the provenance story. Selectivity cannot be considered an improvement when it removes evidence necessary to understand why the listing matters.

#### interp-02 — Ordinary Stratocaster

The model continued to include incidental details about finish, neck, condition, and functionality.

This suggested that explicit guidance did not reliably distinguish evidence relevant to the interpretation from information that merely described the instrument.

#### interp-03 — Inherited Telecaster

The model retained the core information about identity, family history, inheritance, and refusal to sell.

Some historical context was omitted. The negative surface judgment remained defensible because the instrument was not available for acquisition.

This case illustrates why personal significance and acquisition relevance must remain distinct.

#### interp-04 — Custom headless eight-string

The model selected configuration details but still described the instrument as ordinary and assigned a negative surface judgment.

The case exposed tension between selecting relevant evidence and interpreting its significance. The presence of a distinctive configuration did not reliably translate into an appropriate interpretation.

#### interp-05 — Studio-history Stratocaster

The model selected the reported studio history, case inscription, inventory tag, and uncertainty.

Its surface judgment changed from _yes_ to _maybe_. The additional evidence selection did not clearly establish that the new judgment was more accurate.

The case illustrates the distinction between clues that justify investigation and evidence that establishes provenance.

#### interp-06 — Modified Telecaster

The model produced a comparatively coherent selection of modification-related information, original-pickup details, and notes.

This was a stronger example of selecting evidence that supported a consistent interpretation.

#### interp-07 — Les Paul rarity and value claims

The model changed its judgment from _maybe_ to _yes_ despite the combination of rarity or value claims and missing documentation.

The result raised concerns about whether claims that appear commercially significant were being treated as sufficient evidence of an opportunity.

Missing documentation and seller claims should inform uncertainty, not automatically validate an acquisition implication.

#### interp-08 — Jazz Bass with local history

The model selected relevant local-history details, physical wear, and unexplained notes.

It reasonably omitted some transaction details, including estate-purchase and willingness-to-sell context, along with price information.

This suggested that some incidental details could be excluded without undermining the central interpretation.

### Assessment against the five criteria

**Direct relevance:** Partially improved. Some cases had more focused selections, while others retained incidental details or lost important context.

**Omission:** Unresolved. The model still omitted meaningful information in some cases.

**Selectivity:** Improved in some cases. The reduction in selected Signals was substantial, but fewer selections did not consistently mean better selections.

**Sufficiency:** Generally maintained, but with exceptions where omitted evidence weakened the explanation.

**Fidelity:** Unresolved. The model still paraphrased, combined, or abbreviated source material in ways that could change meaning or reduce traceability.

### Conclusion

Targeted evidence-selection guidance changed the model's behavior, but it did not consistently improve interpretation quality.

The experiment reinforced that evidence selection must balance relevance, completeness, and fidelity. Minimizing the number of Signals is not itself a valid objective.

No production change was justified.

A useful next step was to improve the traceability of selected evidence so that individual selections could be audited against their sources.

---

## Phase 4.8 — Stable Signal IDs and Auditable Interpretation

### Research question

Do stable IDs for individual Signals improve traceability and auditability while preserving relevance, sufficiency, fidelity, and interpretation quality?

### Input preparation

The source dataset was:

`experiment-phase-4/interpretation-cases.json`

It contained eight interpretation cases and 66 Signals in total. The original individual Signals did not have stable IDs.

A preparation script, `prepare_phase_4_8_input.py`, assigned deterministic IDs in the form:

`interp-01-S01`

The derived input was:

`interpretation-cases-phase-4-8.json`

The preparation process preserved the original Signal fields, including `type`, `claim`, and `source_text`.

A validation script checked that:

- All eight cases remained present.
- Listing and Signal counts were preserved.
- Original Signal fields were preserved.
- IDs were assigned deterministically.

This created an auditable input representation without intentionally changing the underlying evidence.

### Interpretation output

The interpreter script was:

`interpret_with_ai_phase_4_8.py`

The model was `gemini-3.5-flash-lite`.

The output was written to:

`interpretation-results-phase-4-8.json`

The output structure included:

- `listing_id`
- `observation`
- `supporting_evidence_ids`
- `qualifying_or_contradictory_evidence_ids`
- `uncertainty`
- `surface`

The model referenced Signals by their stable IDs instead of reproducing their text as the primary means of identifying evidence.

### Structural validation

The run completed and produced eight interpretations.

Validation checked that:

- Exactly one interpretation existed for each listing.
- IDs were unique and belonged to the appropriate listing.
- No Signal ID was duplicated within a reference list.
- Supporting and qualifying/contradictory reference lists did not overlap.

These checks established structural validity and reference integrity. They did not establish that the interpretation itself was correct.

### Surface-judgment results

| Case      | Human target | Phase 4.7          | Phase 4.8 |
| --------- | ------------ | ------------------ | --------- |
| interp-01 | Yes          | Not specified here | Yes       |
| interp-02 | No           | Not specified here | No        |
| interp-03 | No           | Not specified here | No        |
| interp-04 | Yes          | Not specified here | Yes       |
| interp-05 | Yes          | Not specified here | Yes       |
| interp-06 | Yes          | Not specified here | Yes       |
| interp-07 | Maybe        | Not specified here | Maybe     |
| interp-08 | Yes          | Not specified here | Yes       |

Phase 4.8 matched the human target labels in **8/8 cases**, compared with **5/8 in Phase 4.7**.

This result is encouraging but must be interpreted cautiously. One run across eight cases cannot establish that stable IDs caused the improvement or that the result will reproduce across different runs, datasets, or models.

### Evidence-reference totals

The output contained:

- **44 supporting evidence references**
- **4 qualifying or contradictory evidence references**
- **48 total references**

The total number of references should not be interpreted as a quality score. Relevance, sufficiency, omissions, and fidelity still require human review.

### Case-level output and human audit

#### interp-01 — Family provenance

**Output selection:** Signals S01–S06 were selected as supporting evidence.

**Interpretation:** The model provided better coverage of the family history and made the selected evidence easier to inspect.

**Audit findings:** The wording “provenance documented” overstated what the source established. The statement about modifications during church use was speculative.

**Assessment:** Traceability improved, but source fidelity and uncertainty handling remained imperfect. The positive surface judgment was defensible.

#### interp-02 — Ordinary Stratocaster

**Output selection:** All six Signals were selected as supporting evidence.

**Interpretation:** The model assigned a negative surface judgment.

**Audit findings:** The evidence selection remained overinclusive. S02 was incidental. S03 and S04 described condition or functionality that might matter to an ordinary listing description but did not support the central negative judgment. S05 concerned moving, and S06 concerned price; neither was clearly relevant to the core reason for the judgment.

**Assessment:** The negative label was defensible, but the model had not demonstrated reliable selectivity.

#### interp-03 — Inherited Telecaster

**Output selection:** Signals S01–S06 were selected as supporting evidence; S07, the refusal to sell, was selected as qualifying evidence.

**Interpretation:** The model separated the personal history from the acquisition limitation.

**Audit findings:** The phrase “documented family history” overstated the evidentiary status of the source. S06 was redundant.

**Assessment:** The separation between personal significance and availability was useful and auditable. The negative surface judgment was defensible.

#### interp-04 — Custom headless eight-string

**Output selection:** Signals S01–S05 were selected as supporting evidence.

**Interpretation:** The model recognized the unusual configuration and produced a positive surface judgment, correcting the earlier tension in Phase 4.7.

**Audit findings:** Some incidental details remained. The wording “Strandberg-style” did not confirm that the instrument was manufactured by Strandberg.

**Assessment:** The positive judgment was defensible because of the unusual configuration, but the interpretation still needed careful attribution and source fidelity.

#### interp-05 — Studio-history Stratocaster

**Output selection:** Signals S01, S03, S04, S05, and S06 were selected as supporting evidence. S07, concerning the unknown musician or duration, was selected as qualifying evidence.

**Interpretation:** The model treated the available studio-related clues as a reason to investigate.

**Audit findings:** The clues offered a lead but did not verify provenance. The phrase “accompanied by studio provenance” overstated what the evidence established.

**Assessment:** A positive or maybe judgment could be defensible depending on whether the question is whether to investigate the clues or whether the claimed history has been established. The experiment did not resolve that distinction.

#### interp-06 — Modified Telecaster

**Output selection:** Signals S01, S04, S05, S06, and S07 were selected as supporting evidence.

**Interpretation:** The model recognized a coherent combination of modification-related details, retained components, and setup notes.

**Audit findings:** The phrase “documented musician modifications” overstated the attribution. The model also introduced concerns that were not grounded in the source.

**Assessment:** The evidence combination was useful, but the interpretation needed to distinguish documented modifications from claims about who made them.

#### interp-07 — Les Paul rarity and value claims

**Output selection:** Signals S01–S06 were selected as supporting evidence. S09, concerning the lack of documentation, was selected as qualifying evidence.

**Interpretation:** The model assigned a _maybe_ judgment.

**Audit findings:** The model correctly retained uncertainty around the claims, but omitted S08, the seller's condition claim, as a qualification. The phrase “significant valuation gap” implied market significance that the evidence did not establish.

**Assessment:** The _maybe_ judgment was defensible as a reason to investigate, provided that the rarity and value claims remained unverified rather than being treated as evidence of actual market value.

#### interp-08 — Jazz Bass with local history

**Output selection:** Signals S01–S05 were selected as supporting evidence. S06, concerning unknown notes, was selected as qualifying evidence.

**Interpretation:** The model separated local-history clues from uncertainty about the unexplained notes.

**Audit findings:** The local history was seller-reported and should have remained explicitly attributed to the seller.

**Assessment:** The positive judgment was defensible, but the source attribution still needed improvement.

### Cross-case assessment

**Traceability improved.**

Stable Signal IDs made it possible to identify exactly which pieces of evidence the model selected. This made the output easier to inspect, compare, and audit.

**Selectivity remained inconsistent.**

The model sometimes selected all available Signals, even when several were incidental to the interpretation.

**Omissions remained possible.**

Stable references did not prevent the model from overlooking meaningful evidence or failing to include a relevant qualification.

**Fidelity remained imperfect.**

The model could still overstate source claims, imply verification that had not occurred, or introduce interpretations that were not adequately supported.

**Interpretation quality remained mixed.**

The surface labels matched the human targets in all eight cases, but the supporting explanations still contained weaknesses. A correct label did not guarantee that the reasoning was complete, faithful, or appropriately qualified.

### Conclusion

Phase 4.8 demonstrated that stable evidence IDs can improve the traceability and auditability of AI-generated interpretations.

The experiment did **not** establish that stable IDs universally improve reasoning quality. The increase from 5/8 to 8/8 surface-label agreement is a result from a small, single-run experiment and cannot establish causation.

The key distinction is:

> **Stable IDs make interpretation easier to audit; they do not make an interpretation correct.**

No production change was justified solely by this experiment.

---

## Overall Phase 4 Findings

Across Phases 4.3–4.8, several conclusions emerged.

### 1. Interpretation is distinct from extraction

A reason for attention is derived from evidence and context. It should not be treated as another independent Signal.

### 2. Surface-worthiness is contextual

No single evidence category or fixed number of Signals explains all cases. Distinctive configurations, personal history, provenance claims, transaction context, and combinations of details may each contribute in different situations.

### 3. Evidence selection is a multi-part problem

Useful interpretation requires balancing:

- Relevance
- Selectivity
- Sufficiency
- Fidelity
- Appropriate uncertainty
- Defensible surface judgments

Optimizing only one of these can make another worse. Fewer selected Signals do not necessarily mean a better explanation.

### 4. Label agreement is not enough

A model may select the expected _yes_, _maybe_, or _no_ label while still overstating evidence or producing a weak explanation.

Evaluation should therefore examine the reasoning and its source grounding, not only the final label.

### 5. Stable IDs improve auditability

Stable Signal references provide a clearer way to trace an interpretation to its evidence. They improve inspection and validation but do not guarantee relevance, completeness, or correctness.

### 6. Source fidelity remains a concern

Seller-reported claims should remain attributed to the seller. Unknown provenance should not become established provenance, and distinctive characteristics should not silently establish rarity, authenticity, manufacturer, or value.

### 7. The experiments do not justify a permanent scoring architecture

The work does not establish a numerical surface-worthiness threshold, confidence model, ranking system, permanent reason taxonomy, or automated purchase recommendation.

## Current Design Position

The Phase 4 experiments support continuing to investigate evidence-grounded interpretation, while keeping its limits explicit.

The current conceptual sequence remains:

1. Extract source-grounded Signals.
2. Identify relevant evidence relationships.
3. Interpret the evidence in context.
4. Preserve uncertainty and source attribution.
5. Present an explainable reason for human attention.
6. Allow the human to decide whether further investigation is worthwhile.

This sequence does not prescribe a final production implementation.

## Suggested Follow-Up Investigations

Further experiments should target specific unresolved problems rather than changing multiple aspects of the system at once.

Potential directions include:

- Testing whether stable IDs improve auditability across repeated runs.
- Evaluating supporting-evidence relevance, sufficiency, and omission separately.
- Establishing explicit checks for unsupported paraphrasing and claims of verification.
- Testing whether interpretations distinguish a reason to investigate from a verified story or acquisition opportunity.
- Expanding the evaluation set before making broader claims about reliability.

These are possible investigations, not commitments to implement all of them.

## Final Principle

> **Evidence should support interpretation, interpretation should explain attention, and neither should claim more than the source establishes.**

Phase 4 provides a basis for continued investigation, not proof that interpretation quality has been solved.
