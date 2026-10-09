# Hedstok — Concept

## Purpose

Hedstok is an evidence-grounded interpretation tool for used musical-instrument listings.

Its purpose is to surface listings that may be worth a closer look by identifying meaningful details, relationships, and context in the information available.

Hedstok is not intended to make purchasing decisions, estimate market value, verify seller claims, or automatically recommend transactions. It helps a human notice something interesting and understand why it may deserve attention.

The guiding idea is:

> **“Hey. Look at this one.”**

## Core Principles

### Evidence before assumptions

Hedstok should distinguish what a listing actually says from what might be inferred from it.

Extracted information should remain grounded in the source. Claims should not silently become verified facts, and missing information should not be filled with invented details.

### Stories before specifications

Instrument specifications matter, but they are not the only reasons a listing may be interesting.

A listing may warrant attention because of its history, modifications, ownership context, unusual configuration, physical details, or relationship to a person's interests.

These details should be interpreted in context rather than reduced to specifications alone.

### Evidence before labels

A conclusion should be explainable through the evidence that supports it.

Labels such as _yes_, _maybe_, or _no_ are shorthand for an interpretation, not substitutes for the reasoning behind it.

### Concepts before implementation

Hedstok's conceptual distinctions should be understood before they are committed to permanent schemas, scoring systems, or architectural decisions.

Experimental results can inform implementation, but a successful experiment does not automatically justify a production feature.

### Evolution, not rewrite

Hedstok should develop incrementally. Existing evidence, working behavior, and useful distinctions should be preserved unless there is a demonstrated reason to change them.

## Conceptual Model

Hedstok separates three related activities.

### 1. Evidence extraction

Identify claims and details present in the listing.

Examples include:

- Instrument identity and configuration
- Modifications and included components
- Seller-reported history or provenance
- Physical condition and visible clues
- Transaction context
- Unknown, ambiguous, or potentially contradictory information

Extracted evidence should retain a connection to its source. Where practical, the original wording should remain available so that a human can inspect the basis for an interpretation.

Extraction does not establish whether a seller's claim is true.

### 2. Evidence interpretation

Consider what the extracted evidence means in context.

Interpretation may involve relationships among details, relevant uncertainty, unusual combinations, or reasons a listing deserves further investigation.

A meaningful interpretation should explain why the evidence matters rather than merely repeat the listing.

Not every listing needs a compelling story, and no single category of evidence is sufficient in every situation. A relatively ordinary instrument may still be interesting in the right context; a distinctive instrument may not warrant attention if its distinguishing details are irrelevant.

### 3. Human attention

Surface an observation that helps a person decide whether to look more closely.

A useful observation should be explainable, appropriately qualified, and grounded in the available evidence.

The purpose is to direct attention—not to decide what the person should buy.

## Evidence, Interpretation, and Uncertainty

These concepts should remain distinct:

- **Evidence:** What the source says or shows.
- **Interpretation:** Why some combination of evidence may be meaningful.
- **Uncertainty:** What remains unknown, ambiguous, or unsupported.
- **Attention judgment:** Whether the available evidence provides a reason to look more closely.

Uncertainty is not automatically a negative signal. It may itself be relevant when there is a specific, evidence-grounded reason to investigate further. However, missing information alone should not be treated as proof of an opportunity or a problem.

Interpretations should not overstate what the evidence establishes. Seller-reported history should remain attributed to the seller unless independently verified. An unusual configuration does not, by itself, establish rarity, value, authenticity, or provenance.

## Current Design Position

Early experiments suggest that reasons to examine a listing emerge from the interaction of evidence and context rather than from a single fixed category.

They also suggest that AI can help interpret structured evidence, but that interpretation quality remains imperfect. Common concerns include:

- Selecting too many supporting details
- Omitting relevant evidence
- Missing relationships among details
- Paraphrasing or overstating source claims
- Treating unsupported claims as established facts
- Expressing uncertainty inconsistently

Stable references to individual evidence items may improve traceability and make interpretations easier to audit. They do not, by themselves, guarantee better reasoning.

These are working conclusions from exploratory experiments, not proof that a particular production architecture is correct.

## Implementation Boundaries

The experiments conducted so far do not, by themselves, justify introducing:

- A permanent taxonomy of reasons for attention
- A numerical surface-worthiness score
- A confidence score or ranking algorithm
- Automated purchase recommendations
- Market valuation or authenticity judgments
- A fixed number of supporting evidence items

Such decisions should be made only when a clear requirement and sufficient evidence support them.

## Guiding Question

At each stage of development, ask:

> Does this help a person notice something meaningful in a listing, understand why it matters, and distinguish evidence from assumption?

If a proposed feature does not serve that purpose, its place in Hedstok should be reconsidered.
