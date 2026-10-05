# Hedstok Concept

## 1. Problem

Used-instrument acquisition often depends on finding things that are not obvious from a conventional search.

Relevant information may be:

* incomplete;
* inconsistent;
* poorly structured;
* qualitative;
* distributed across different sources;
* buried in seller descriptions or personal leads;
* uncertain or contradictory.

A useful acquisition tool should therefore do more than retrieve instruments matching a search query.

## 2. Core Question

> **Can software discover interesting acquisition opportunities that a conventional search would not necessarily surface?**

This is the central question of Hedstok.

The project should not assume that the answer is yes. Early development exists to test the premise.

## 3. Core Behavior

Given a collection of guitar listings or acquisition leads, Hedstok should attempt to:

1. understand the available information;
2. identify potentially interesting characteristics or relationships;
3. surface candidates worth investigating;
4. explain why each candidate was surfaced;
5. preserve the evidence supporting those explanations;
6. distinguish known information from uncertainty or inference.

The desired outcome is not a definitive purchasing recommendation.

It is:

> **"This is worth looking into. Here's why."**

## 4. Evidence Principle

Hedstok should not treat extracted or inferred information as unquestioned truth.

Where practical, claims should remain traceable to their source.

Uncertainty should be preserved rather than silently converted into certainty.

## 5. AI Principle

AI may be useful for understanding messy, unstructured information.

Potential uses include:

* extracting structured information from natural-language listings;
* identifying claims and provenance;
* comparing descriptions;
* detecting potentially contradictory information;
* identifying information that warrants further investigation.

AI should not be treated as the final authority.

Deterministic analysis, source evidence, uncertainty, and human judgment remain part of the system.

## 6. Initial Experiment

The first experiment should remain deliberately small.

### Input

Approximately 10–20 guitar listings or acquisition leads containing realistic, imperfect information.

### Output

Hedstok should surface approximately 1–3 candidates it considers worth investigating.

For each candidate, Hedstok should provide:

* what caught its attention;
* the evidence supporting that observation;
* what remains uncertain;
* where the relevant information came from.

### Human Evaluation

The initial evaluation question is:

> **Would I actually investigate this?**

A later evaluation question may be:

> **Would Dan actually investigate this?**

The purpose of the experiment is to learn whether Hedstok can produce useful discoveries, not merely technically plausible output.

## 7. Experiment Success

The experiment should be considered promising if Hedstok surfaces at least one candidate that is interesting specifically because it identified a relationship, anomaly, uncertainty, provenance detail, or combination of information that would not have been obvious from simply searching for a known guitar.

Technical sophistication alone does not constitute success.

## 8. Current Non-Goals

The initial experiment will not attempt to build:

* autonomous purchasing or bidding;
* universal marketplace scraping;
* a general-purpose chatbot;
* an authoritative guitar valuation system;
* a full image-recognition system;
* a trained machine-learning model;
* a sophisticated entity-resolution platform;
* notifications or continuous monitoring;
* a complete marketplace;
* the eventual production architecture.

These may be considered later if the core concept proves useful.

## 9. Guiding Principle

> **The experiment should earn the right to become a product.**

Architecture, technology choices, and larger features should follow what is learned from the experiment rather than being assumed in advance.

## Phase 2 — Evidence Pipeline

### Goal

Turn the initial extraction vertical slice into a repeatable workflow for processing listings and producing reliable, source-grounded structured evidence.

Phase 2 should establish the minimum input, output, and evaluation conventions needed to determine whether the core extraction capability is useful enough to support further development.

### Scope

Phase 2 will focus on:

* **Multiple-listing input**

  * Establish a simple input format for processing a collection of listings rather than a single hard-coded listing.

* **Repeatable extraction**

  * Run the existing extraction capability across multiple listings and produce structured extraction artifacts.

* **Source preservation**

  * Maintain a direct connection between each extracted Signal and the source text from which it was derived.

* **Extraction evaluation**

  * Bring the useful evaluation principles from Experiment 0 into the working pipeline so extraction quality can be measured rather than assumed.

* **Uncertainty preservation**

  * Preserve the distinction between what a listing claims and what is actually established.
  * The extraction process must not silently convert uncertain or attributed claims into facts.

### Evaluation Findings

#### Source-text grounding

The structural evaluator identified a source-text fidelity failure in listing-11. The extracted contradiction signal combined two non-contiguous portions of the listing while omitting the intervening price:

`1958 les paul $4000 [image is of a kid-size stratocaster style guitar]`

The extraction returned:

`1958 les paul [image is of a kid-size stratocaster style guitar]`

Under the current extraction contract, `source_text` must be copied exactly from the source listing, so this was correctly classified as a grounding failure.

The batch extraction subsequently represented the two pieces of evidence as separate signals with exact source text. This demonstrates that the underlying evidence can be extracted correctly without requiring a combined source span.

The earlier failure also raises a potential future design question: whether a signal should be able to reference multiple source spans when a claim depends on non-contiguous evidence. No schema change is made at this stage.

#### Semantic extraction

Semantic review of the batch extraction showed that fewer signals do not necessarily indicate lower extraction quality. Related evidence was sometimes consolidated into fewer signals while preserving the substantive information required by the evaluation criteria.

The review also showed that the current Experiment 0 expected-signal fixture contains several different kinds of evaluation criteria:

* directly extractable source evidence;
* interpretations or conclusions derived from source evidence;
* absence-based observations.

These categories should not necessarily be treated as equivalent extraction requirements.

For example, a listing may provide the evidence needed to identify a potential contradiction or investigation opportunity without the extraction layer itself needing to assert that interpretation.

The current batch extraction captured the substantive evidence for most of the applicable evaluation criteria reviewed.

These findings support continuing to treat the extraction layer as an evidence-preservation step rather than requiring it to perform higher-level interpretation.

No extraction schema change is made at this stage.

#### Batch extraction

The 14-listing batch extraction was compared with independent extraction of each listing.

The batch extraction produced fewer Signals primarily by consolidating related evidence into broader Signals. Review of the two outputs found no meaningful loss of substantive evidence required by the evaluation criteria.

In some cases, the batch extraction produced cleaner source-grounded evidence than the independent extraction. In listing-11, for example, the independent extraction combined non-contiguous source text into a single invalid source reference, while the batch extraction represented the relevant evidence as separate Signals with exact source text.

Within the scope of this experiment, batch extraction therefore appears viable for repeatable multi-listing processing without a demonstrated loss of useful evidence.

This does not establish that batch extraction is universally equivalent to independent extraction. The finding is limited to the current evaluation set and should be revisited if larger or materially different inputs produce different behavior.

### Out of Scope

Phase 2 does not currently include:

* Evidence Relationship implementation
* entity resolution or persistent entity modeling
* database implementation
* web UI
* recommendation or ranking systems
* marketplace integrations or automated web scraping
* pricing intelligence
* authentication or deployment infrastructure
* generalized AI orchestration
* graph architecture

These capabilities may become appropriate in later phases, but Phase 2 should not assume that they are required.

### Phase 2 Completion Criterion

Phase 2 is complete when Hedstok can repeatedly process a collection of listings and produce structured, source-grounded evidence with enough evaluation support to determine whether the extraction capability is reliable and useful enough to justify further development.

> **Phase 2 is intended to establish whether the core evidence pipeline works well enough to earn the next capability.**
