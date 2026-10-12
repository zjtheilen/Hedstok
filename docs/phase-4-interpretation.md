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

## Phase 4.9 — Source Fidelity Audit

### Research question

Do AI-generated interpretations preserve the source's attribution, certainty, and meaning, or can an interpretation remain traceable to specific Signals while still overstating claims or omitting details that matter?

Phase 4.8 improved the ability to identify the evidence selected by the model. Phase 4.9 examines a separate question: whether the resulting interpretation represents that evidence faithfully.

Stable IDs make an interpretation easier to audit, but they do not guarantee that the interpretation preserves what the source actually says.

### Experimental approach

The audit reviewed the existing eight Phase 4.8 cases and outputs. It did not make new model calls or change the prompt, schema, or production implementation.

Each interpretation was examined against four criteria:

1. **Attribution fidelity** — does the interpretation preserve who made a claim or where the information came from?
2. **Certainty fidelity** — does it preserve the difference between a reported claim, an observed clue, an inference, and an established fact?
3. **Inference discipline** — does it avoid introducing claims or implications that the available evidence does not support?
4. **Meaning preservation** — does it retain the details necessary to understand why the evidence may matter, rather than compressing away important context?

The audit distinguishes substantive fidelity problems from stylistic preferences. Concise wording is not inherently a problem; it becomes a problem when compression changes the claim's status, removes a meaningful qualification, or loses context necessary to understand the interpretation.

### Case-level findings

#### interp-01 — Family provenance

The listing concerned a 1974 Gibson ES-335. The seller reported that their mother owned it and played in a church band. The case inscription contained the years 1974–79, and the seller reported inheriting the instrument in 1998.

The interpretation described the provenance as documented and speculated about modifications during church use.

**Attribution and certainty:** “Church band provenance documented” overstated what the evidence established. The reported family history and case inscription provided clues, but the inscription did not establish that this specific guitar was used by the church band. The claim about modifications during church use was unsupported.

**Meaning preservation:** The family ownership and church-band history were central to why the listing was interesting. Those details should not be removed merely to make the evidence selection shorter.

**Assessment:** The positive surface judgment remained defensible. The story was worth looking at without treating every part of it as verified history.

#### interp-02 — Ordinary Stratocaster

The listing described an ordinary 2018 Stratocaster. The seller reported good condition, working functionality, and a move as the reason for selling.

The interpretation described the listing as standard and lacking anomalies.

**Attribution and certainty:** The label “standard” was a reasonable concise description of the supplied case, but “lacking anomalies” risks treating the absence of identified anomalies as evidence that no potentially interesting detail exists.

**Meaning preservation:** The case did not provide a strong reason to surface. However, a negative judgment should not be justified by implying that the model exhaustively ruled out every possible point of interest.

**Assessment:** The negative judgment was defensible. The wording should not imply that missing evidence is equivalent to proof of absence.

#### interp-03 — Inherited Telecaster

The seller described a 1978 Telecaster that belonged to their father, who played at local bars and church events in the late 1970s and 1980s. A name appeared in the case, and the seller reported inheriting the instrument in 2012. The seller explicitly stated that they were not selling or trading it.

The interpretation described the history as documented and treated the instrument's unavailability as qualifying context.

**Attribution and certainty:** “Documented family history” slightly overstated the status of the reported history and the case inscription. The seller's account and the inscription were clues, not independent confirmation of the full history.

**Meaning preservation:** The personal story remained meaningful even though the instrument was not available for acquisition. The refusal to sell was explicit and should not be represented as merely uncertain availability.

**Assessment:** The negative surface judgment was defensible for the acquisition-oriented purpose. The case also demonstrates that a story can be worth preserving even when it does not lead to an acquisition opportunity. Whether Hedstok should surface such stories for a different reason remains an unresolved product-scope question.

#### interp-04 — Custom headless eight-string

The listing described a custom headless eight-string with a Strandberg-style layout. The seller reported buying it from a local musician two years earlier.

The interpretation recognized the unusual configuration and assigned a positive surface judgment.

**Attribution and certainty:** “Strandberg-style” describes a resemblance or layout; it does not establish that Strandberg manufactured the instrument. The interpretation did not need to claim a manufacturer to explain why the configuration was distinctive.

**Meaning preservation:** The local-musician context was omitted. That detail could contribute to the listing's story, even if it did not establish provenance or instrument quality.

**Assessment:** The positive judgment was defensible based on the configuration alone. The omission illustrates that evidence selection can be concise and traceable while still losing meaningful context.

#### interp-05 — Studio-history Stratocaster

The seller reported buying a 2006 Stratocaster from a local studio that was closing. The studio's name appeared inside the case, and an original inventory tag was present. The seller did not know which musicians had used the guitar or how long it had been at the studio.

The interpretation treated the studio-related clues as a reason to investigate.

**Attribution and certainty:** “Studio provenance” can function as shorthand for the reported studio connection, but it risks implying established provenance if not qualified. The clues support a lead for investigation, not proof of which musicians used the instrument or how long it was there.

**Meaning preservation:** The studio name and inventory tag are specific, potentially useful clues. The uncertainty about musicians and duration is also relevant because it limits what can be concluded.

**Assessment:** A positive judgment was defensible as a reason to investigate the clues. The interpretation should preserve the distinction between evidence of a studio connection and verified instrument history.

#### interp-06 — Modified Telecaster

The listing concerned a 2012 Telecaster that belonged to the seller's uncle, who reportedly played locally for about twenty years. The Bigsby-style vibrato and bridge pickup had been changed around 2015. The original pickup was included, handwritten setup notes were present, and the seller reported inheriting the instrument three years earlier and selling it now.

The interpretation focused on the modifications, retained original component, and setup notes.

**Attribution and certainty:** “Documented musician modifications” overstated the attribution. The source described modifications and a family connection to a local musician, but did not establish that the uncle made the modifications.

**Meaning preservation:** The uncle's local playing history was omitted. That history may be an important part of the listing's story and should not automatically be discarded in favor of technical details.

**Assessment:** The positive judgment was defensible. A faithful interpretation should distinguish what changed on the instrument from who performed the work and preserve the relevant ownership and playing history.

#### interp-07 — Les Paul rarity and value claims

The seller described a 1979 Gibson Les Paul Custom as extremely rare, museum quality, and worth $8,000. The asking price was $2,500, with urgent need given as the reason for selling. The listing did not provide a serial number, provenance, or paperwork.

The interpretation described a significant valuation gap and retained some uncertainty.

**Attribution and certainty:** The phrase “significant valuation gap” implied that a meaningful market-value difference had been established. The supplied information contained seller claims and an asking price, not independent evidence of market value.

**Inference discipline:** The price difference and seller's stated circumstances do not establish that the instrument is authentic, rare, underpriced, or a bargain. They also do not establish fraud or bad intent.

**Meaning preservation:** The claimed rarity and value, urgent sale context, and missing documentation are all relevant, but their relevance comes from the questions they raise. None should be silently upgraded into a verified conclusion.

**Assessment:** A “maybe” judgment was defensible as a reason for investigation. The interpretation should preserve the claims as claims and make the missing evidence explicit without drawing a conclusion about value, authenticity, or seller intent.

#### interp-08 — Jazz Bass with local history

The seller reported that a 1991 Jazz Bass belonged to a local bassist who played clubs in the 1990s. The instrument was purchased from an estate and showed heavy wear. Handwritten notes were found in the cavity, but their author and meaning were unknown.

The interpretation described the local club history and treated the unexplained notes as a source of uncertainty.

**Attribution and certainty:** “Local club history” compressed the seller's account into a concise phrase, but the account should remain attributed to the seller. The notes could be interesting, but their presence did not establish who wrote them or what they meant.

**Meaning preservation:** The wear, local-history claim, and unexplained notes form a potentially meaningful combination. The word “mysterious” is mildly stylized, but the more important concern is whether the interpretation preserves the uncertainty around the notes.

**Assessment:** The positive judgment was defensible. The interpretation should retain attribution for the history and avoid implying that the notes reveal anything specific.

### Cross-case findings

**Traceability does not guarantee fidelity.**

Stable IDs make it easier to identify which Signals were selected. They do not prevent the interpretation from overstating what those Signals establish.

**Attribution can be lost during compression.**

Phrases such as “documented family history,” “studio provenance,” and “local club history” may be convenient summaries, but they can imply a stronger evidentiary status than the original source supports.

**Meaningful details can be lost through over-selectivity.**

The local-musician context in interp-04 and the uncle's playing history in interp-06 were not necessary to support the most immediate technical observations, but they contributed to the listings' stories. Evidence selection should not optimize for the fewest references at the expense of meaning.

**Uncertainty can be a reason to investigate, not just a warning.**

The studio clues, inscriptions, seller claims, and unexplained notes can justify attention precisely because they create questions. The correct response is to preserve those questions rather than resolve them without evidence.

**A faithful interpretation need not be verbose.**

The goal is not to repeat every Signal. It is to compress the evidence without changing its attribution, certainty, or relevant meaning.

**Stylistic concerns should remain distinct from substantive failures.**

A phrase may be slightly dramatic or less elegant than preferred without materially changing the evidence. The more serious failures are unsupported claims of verification, lost source attribution, and conclusions that go beyond what the evidence supports.

### Limitations

This was a manual audit of eight existing cases and one set of Phase 4.8 outputs.

It did not measure inter-reviewer agreement, repeated-run consistency, or general reliability across different models or datasets. The findings identify concrete fidelity risks in the reviewed outputs but do not establish how frequently those risks occur in broader use.

### Conclusion

Phase 4.9 found that stable evidence references improve auditability without ensuring faithful interpretation.

The model could identify its selected Signals and still overstate provenance, blur the distinction between a reported claim and an established fact, or omit details that helped explain why a listing was interesting.

The central principle is:

> **Preserve the story without upgrading it into established fact; preserve uncertainty without treating it only as a negative; and compress the evidence without discarding the details that give it meaning.**

The audit does not justify a production change by itself. It clarifies what future interpretation experiments need to evaluate: not only whether evidence can be traced, but whether the resulting explanation remains faithful to its source.

---

## Phase 4.10 — Fidelity-Focused Interpretation Experiment

**Status:** Evaluation in progress

### Purpose

Evaluate whether a narrowly revised interpretation instruction improves source attribution, certainty, inference discipline, and preservation of meaningful context compared with the Phase 4.8 baseline.

### Method

- Reused the eight Phase 4.8 interpretation cases.
- Ran the copied Phase 4.10 runner with the revised faithful-compression instructions.
- Compared Phase 4.10 outputs with the corresponding Phase 4.8 outputs.
- Made no changes to the underlying Signals or interpretation output schema.
- No additional model calls were made for this evaluation.

This is a qualitative comparison of one batch run. It does not establish repeatability or general model reliability.

### Evaluation criteria

1. **Attribution fidelity:** Does the interpretation preserve who made a claim and whether it is seller-reported?
2. **Certainty fidelity:** Does it preserve uncertainty without presenting unverified claims as established facts?
3. **Inference discipline:** Does it avoid adding relationships, history, or conclusions unsupported by the supplied Signals?
4. **Meaning preservation:** Does it retain the context that materially explains why the listing may deserve attention?

### Case-by-case audit

| Case        | Attribution fidelity                                                                                                                                      | Certainty fidelity                                                                                                                                     | Inference discipline                                                                                                                                         | Meaning preservation                                                                                                                                                   | Overall                                   |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| `interp-01` | Phase 4.10 avoids calling the case inscription documented provenance, but omits the seller's reported inheritance in 1998 and continued family ownership. | Both versions present substantial family history; Phase 4.10 does not clearly distinguish the seller's account from independently established history. | Neither version establishes a verified chain of ownership.                                                                                                   | Phase 4.10 preserves the church connection and case inscription but loses meaningful ownership history.                                                                | Mixed                                     |
| `interp-02` | Both versions preserve the seller's reason for selling.                                                                                                   | Phase 4.10 retains the reported condition claims without materially overstating them.                                                                  | No significant new inference is apparent.                                                                                                                    | Both versions capture the ordinary nature of the listing; Phase 4.10 preserves the finish and neck details.                                                            | Neutral                                   |
| `interp-03` | Phase 4.10 preserves the family relationship but drops the explicit refusal to sell or trade.                                                             | Neither version materially overstates the family history.                                                                                              | Phase 4.10 does not invent a new historical claim, but its statement that the guitar remains in the family is less precise than the explicit seller context. | Omitting the refusal to sell removes the most consequential acquisition-related fact.                                                                                  | Regression                                |
| `interp-04` | Both versions omit attribution details that are not necessary to describe the configuration.                                                              | Phase 4.10 preserves the seller's good-condition claim as a reported statement, but does not include it in the observation.                            | The description remains consistent with the supplied configuration Signals.                                                                                  | Phase 4.10 adds the seller's reason for selling but omits the condition claim and asking price. Its change from `yes` to `maybe` is not justified by the output alone. | Mixed                                     |
| `interp-05` | Phase 4.10 avoids the stronger label "studio provenance" and describes the physical clues directly.                                                       | Both versions acknowledge that the users and duration of studio use are unknown.                                                                       | Phase 4.10 avoids treating the inventory tag and inscription as proof of the guitar's complete history.                                                      | It omits the seller's reported direct purchase from the studio when it closed in 2019, weakening the acquisition story.                                                | Mixed                                     |
| `interp-06` | Both versions attribute the modifications to the uncle, as explicitly stated in the input Signals.                                                        | Phase 4.10 omits the baseline's uncertainty about wear and installation quality.                                                                       | The attribution is supported; however, dropping uncertainty may imply more is known about the modifications' condition than the Signals establish.           | Phase 4.10 preserves the modification details, original pickup, and setup notes, and adds the approximate date.                                                        | Mixed                                     |
| `interp-07` | Phase 4.10 explicitly frames rarity, investment value, and museum quality as seller claims.                                                               | This is a clear improvement: unsupported promotional claims are not presented as established properties.                                               | Phase 4.10 avoids asserting that a genuine market-value gap exists, although it omits the actual claimed value and asking price.                             | It preserves the unsupported-claims issue and missing documentation, but drops the $8,000-versus-$2,500 contrast and the seller's stated urgency.                      | Improvement in attribution; mixed overall |
| `interp-08` | Both versions avoid assigning the notes to a known author.                                                                                                | Both preserve uncertainty about the notes' origin and meaning.                                                                                         | Phase 4.10 does not turn the notes into evidence of verified history.                                                                                        | Both preserve the bass's identity, heavy wear, and unexplained notes; Phase 4.10 is more direct.                                                                       | Neutral to positive                       |

### Findings

1. **Attribution improved most clearly in `interp-07`.** The revised wording treats rarity, investment value, and museum quality as seller claims rather than verified facts. It also avoids asserting a genuine market-value gap based solely on the seller's valuation and asking price.

2. **Meaning preservation remains inconsistent.** `interp-03` omits the explicit refusal to sell or trade. `interp-05` omits the seller's account of buying the guitar directly from the studio when it closed. `interp-01` drops the reported inheritance date and continued family ownership. These omissions matter even though the resulting interpretations remain concise.

3. **Certainty and attribution are separate concerns.** `interp-01` avoids the stronger phrase "documented provenance," but still summarizes a seller-reported family history without clearly identifying it as reported. Conversely, `interp-06` retains a supported attribution to the uncle but drops uncertainty about the condition of the wear and installation work.

4. **Uncertainty should not automatically suppress surface relevance.** `interp-04` describes an unusual extended-range instrument, yet changes the surface assessment from `yes` to `maybe`. The output does not explain why uncertainty about the maker should outweigh the distinctive configuration. The result warrants review against the existing surface criteria, not an automatic change to those criteria.

5. **The experiment does not establish a general improvement.** It consists of one batch run over eight cases, and the outputs show both improvements and regressions. There is no repeated-run evidence to establish consistency.

### Conclusion

Phase 4.10 provides a promising but mixed exploratory result. The revised instruction appears helpful for preventing unsupported seller claims from being presented as established facts, particularly in `interp-07`. It does not consistently preserve all context relevant to interpretation or acquisition decisions.

No production prompt, scoring, surface-classification, or schema changes are justified by this experiment alone. Future work should distinguish source attribution from completeness of meaning and should evaluate surface judgments against the existing criteria. Any further prompt experiment should test a clearly isolated change and retain the same input cases for comparison.

---

### Phase 4.11 — Decision-Relevant Context Under Compression

**Status:** Completed — mixed/inconclusive
**Purpose:** Determine whether an additional prompt instruction could preserve decision-relevant context without making interpretations longer or less selective.

**Intervention**

Phase 4.11 added a _Decision-relevant context under compression_ instruction to the Phase 4.10 prompt. It directed the model to prioritize consequential context, compress supporting details rather than dropping the point they establish, select only the details needed to preserve meaning, and maintain attribution and uncertainty.

The experiment reused the same eight cases, model, input, and output schema. Phase 4.10 served as the control; Phase 4.11 was the treatment.

**Results**

| Measure                           | Phase 4.10 | Phase 4.11 |
| --------------------------------- | ---------: | ---------: |
| Interpretations evaluated         |          8 |          8 |
| Total observation words           |        183 |        158 |
| Total length change               |          — |     −13.7% |
| Median per-case percentage change |          — |      −9.8% |
| Surface classification changes    |          — |          0 |

The added instruction did not produce consistently better preservation of decision-relevant meaning.

**Observed improvements**

- `interp-03`: Explicitly preserved the seller's refusal to sell, correcting a meaningful omission in Phase 4.10.
- `interp-08`: Added estate provenance while retaining the instrument's heavy wear and unexplained handwritten notes.

**Observed limitations and regressions**

- `interp-01`: Retained family and church context but omitted the reported 1998 inheritance.
- `interp-02`: Preserved the asking price but introduced the unnecessary characterization “standard” and dropped the reported working condition.
- `interp-04`: Retained the unusual guitar configuration but omitted the seller's reason for selling.
- `interp-05`: Still incomplete. Omits the seller-reported account that the guitar was purchased directly from the studio when it closed in 2019. Evidence-role assignment does not consistently reflect the relationship between the Signals and the observation.
- `interp-06`: Retained modifications and included components but lost attribution to the seller's uncle and the approximate date of the modifications.
- `interp-07`: Restored the asking-price context but omitted the concrete $2,500 asking price, the seller's claimed $8,000 valuation, and the reported urgency to sell. Its framing risked implying a market-value gap from an unsupported seller valuation; it also introduced speculative possibilities about hidden modifications or condition issues.

Evidence-ID coverage did not necessarily mean that the corresponding observation preserved the evidence's specific meaning.

**Conclusion**

The treatment reduced overall observation length by 13.7%, with a median per-case change of approximately −9.8%. It therefore met the experiment's length constraint. However, shorter output did not reliably preserve all decision-relevant context, and the experiment produced both localized improvements and meaningful omissions.

No surface classifications changed across the eight cases.

Phase 4.11 does not justify promoting the new instruction into the production prompt. The result is **mixed/inconclusive**, not evidence that the approach is ineffective in every case. This was a single eight-case comparison and does not establish repeatability or general model reliability.

**Evaluation Rubric — Eight-Case Audit**

**Status:** Initial criteria applied to the existing Phase 4.10 and Phase 4.11 outputs. No new model calls or prompt changes.

**Purpose**

Establish a consistent way to evaluate whether an interpretation preserves source-grounded meaning, rather than judging quality by brevity, evidence-ID coverage, or surface classification alone.

**Governing rule**

Judge omissions by whether they materially affect a person's interpretation of the listing. Preserve source-grounded meaning; do not judge authenticity, value, or purchase merit. Not every Signal needs to appear in the observation.

**Evaluation criteria**

1. **Selection failure:** Consequential evidence or context is omitted. An omission is not automatically a failure; it must materially affect the reader's understanding of the listing, its history, the seller's claims or circumstances, or a relevant constraint.

2. **Representation failure:** Selected evidence is paraphrased in a way that loses or distorts its meaning, attribution, chronology, uncertainty, or constraints, or introduces an implication that the source does not establish. This includes treating seller-reported information as verified fact and implying conclusions about authenticity or value that the evidence does not support.

3. **Evidence-reference/role mismatch:** Evidence IDs are missing or do not support the specific observation they accompany, or evidence is assigned a supporting versus qualifying/contradictory role that does not match its actual relationship to the observation. Assess evidence references independently from prose fidelity.

A single interpretation may exhibit multiple failure types. Record meaningful improvements and regressions separately rather than collapsing the result into one score.

**Materiality and paraphrase**

Evaluate omissions against the observation's stated reason for attention and the source context needed to understand it. Do not require every potentially relevant Signal to appear. Treat an omission or paraphrase as a failure when it materially changes the reader's understanding, removes a necessary qualification, or introduces an unsupported implication—not merely because a different wording or additional detail was possible.

**Independent evaluation dimensions**

Assess selection, representation, and evidence-reference/role alignment independently. Within evidence-reference/role alignment, distinguish reference accuracy from role accuracy. Evaluate surface classification separately; agreement with a label does not establish that the observation is faithful, and a faithful observation does not by itself establish that the label is justified.

**Eight-case comparison**

| Case        | Phase 4.11 comparison with Phase 4.10                                                                                                                                                                                                               |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `interp-01` | Mixed. Family and church context remains, but the inheritance timeline is omitted. The wording risks implying a stronger connection between the instrument and the church band than the Signals establish.                                          |
| `interp-02` | Mixed. Adds price and seller motivation but drops reported condition and working status, and introduces the unsupported descriptor “standard.”                                                                                                      |
| `interp-03` | Improved on a consequential constraint. Restores the explicit refusal to sell or trade, but omits the inheritance date and the father's playing history.                                                                                            |
| `interp-04` | Weaker on seller context. Drops the reason for selling and adds the finish description instead.                                                                                                                                                     |
| `interp-05` | Still incomplete. Omits the seller-reported account that the guitar was purchased directly from the studio when it closed in 2019. Evidence-role assignment does not consistently reflect the relationship between the Signals and the observation. |
| `interp-06` | Weaker on historical fidelity. Loses attribution of the modifications to the uncle and their approximate date; ownership Signals are incorrectly assigned a qualifying/contradictory role.                                                          |
| `interp-07` | Mixed. Makes the asking-price context more prominent but risks implying a genuine value gap from an unsupported seller valuation and introduces speculative possibilities about hidden modifications or condition issues.                           |
| `interp-08` | Improved contextual coverage. Restores the reported estate acquisition, but “estate provenance” risks overstating the strength of the seller's account.                                                                                             |

Both phases also contain evidence-reference mismatches, including observations with uncited supporting details. The table summarizes the principal differences; it is not an exhaustive inventory of every individual reference error.

**Audit findings**

- **Consequentiality requires judgment.** The explicit not-for-sale constraint in `interp-03` materially affects interpretation. By contrast, omitting a descriptive detail such as finish color is not inherently a failure.
- **Faithful wording is not sufficient by itself.** An observation may accurately repeat individual facts while implying a relationship those facts do not establish, as seen in `interp-01` and `interp-07`.
- **Traceability is not fidelity.** Evidence IDs can be present while the observation loses attribution or chronology, or while evidence is assigned an inappropriate role.
- **Compression involves tradeoffs.** Phase 4.11 corrected a consequential omission in `interp-03` and restored context in `interp-08`, but introduced or retained meaningful omissions and representation problems elsewhere.
- **The audit is exploratory.** These judgments were developed using the same eight cases and outputs already examined. They have not been independently or blindly validated and do not establish general model reliability.

**Next step**

Review these criteria for consistency and ambiguity before deciding whether another experiment is warranted. Any future comparison should assess selection, representation, and evidence-reference/role alignment separately, recording improvements and regressions at the case level.

Do not promote the Phase 4.11 instruction or run another experiment solely on the strength of this audit. No production prompt, scoring, surface-classification, or schema changes are justified by these findings alone.

---

## Overall Phase 4 Findings

Across Phases 4.3–4.9, several conclusions emerged.

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

### 7. Traceability does not guarantee faithful interpretation

The Phase 4.9 audit demonstrated that an interpretation can reference the correct Signals while still overstating their certainty, losing source attribution, or omitting context that gives the evidence meaning.

Evaluation must therefore consider both the traceability of selected evidence and the fidelity of the explanation derived from it.

### 8. Faithful interpretation requires meaningful compression

The goal is not to repeat every Signal or minimize the number selected. A useful interpretation should preserve the evidence necessary to understand the reason for attention, including relevant qualifications, relationships, and source-reported context.

### 9. The experiments do not justify a permanent scoring architecture

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
- Evaluating whether meaningful source context survives concise interpretation.
- Expanding the evaluation set before making broader claims about reliability.

These are possible investigations, not commitments to implement all of them.

## Final Principle

> **Evidence should support interpretation, interpretation should explain attention, and neither should claim more than the source establishes.**

Phase 4 provides a basis for continued investigation, not proof that interpretation quality has been solved.
