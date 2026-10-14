# Hedstok — Concept

## Purpose

Hedstok is an evidence-grounded discovery and interpretation project for used musical-instrument listings and acquisition leads.

Its purpose is to help a person notice listings that may be worth a closer look by identifying meaningful details, relationships, and context in the available information.

A listing may be interesting because of its specifications, but it may also contain a personal history, an unresolved identity, an unusual configuration, a provenance claim, conflicting evidence, or a connection that becomes meaningful only when several details are considered together.

Hedstok's guiding expression is:

> **"Hey. Look at this one."**

Hedstok is intended to direct human attention, not make purchasing decisions. It does not independently verify seller claims, establish authenticity, estimate market value, or determine whether an instrument should be acquired.

An observation that warrants investigation is not proof that an instrument is valuable, rare, authentic, or historically significant.

## Core Principles

### Evidence before assumptions

Hedstok should distinguish what a source says or shows from what might be inferred from it.

Extracted information should remain grounded in its source. Seller claims should not silently become established facts, and missing information should not be filled with invented details.

When attribution, uncertainty, or context affects the meaning of a claim, that information should remain available to later stages of analysis.

### Stories before specifications

Instrument specifications matter, but they are not the only reasons a listing may be interesting.

Personal history, reported provenance, ownership context, unusual characteristics, unresolved identification, and relationships among otherwise ordinary details may all provide reasons to investigate.

These details should be considered in context rather than reduced to specifications alone.

A story does not need to be famous or independently verified to warrant attention. Its relevance must nevertheless be grounded in the available evidence.

### Evidence before labels

A judgment should be explainable through the evidence that supports it.

Labels such as _yes_, _maybe_, or _no_ may be useful shorthand for an experimental attention judgment, but they are not substitutes for the reasoning behind it.

A label does not prove that the selected evidence is relevant, that the explanation is faithful, or that the underlying claims are true.

### Concepts before implementation

Hedstok's conceptual distinctions should be understood before they are committed to permanent schemas, scoring systems, or architectural decisions.

Experiments can identify useful behavior, reveal failure modes, and inform implementation. A successful experiment does not automatically justify a production feature.

Implementation decisions should follow from demonstrated needs rather than from the availability of a technical approach.

### Evolution, not rewrite

Hedstok should develop incrementally.

Existing evidence, working behavior, useful distinctions, and experimental findings should be preserved unless there is a demonstrated reason to change them.

Corrections should address observed problems as narrowly as practical, with evaluation appropriate to the intended improvement.

## Conceptual Model

Hedstok separates several related activities. The distinctions matter even if a future implementation combines some of them.

### 1. Source material

The source is the original information available for a listing or lead.

It may include listing text, manually supplied information, image-derived observations, or other relevant material.

Source material is the basis for extraction. Its existence does not guarantee that it is complete, accurate, or independently verified.

Where different sources or modalities contribute information, their origin should remain distinguishable when that distinction matters to interpretation.

### 2. Signal extraction

A **Signal** is a structured representation of a source-grounded claim or observation.

Signals may represent:

- Instrument identity and configuration
- Modifications and included components
- Seller-reported history or provenance
- Physical condition and visible characteristics
- Seller, market, or transaction context
- Unknown, ambiguous, or potentially conflicting information

A Signal should preserve the meaning of the source rather than encode a conclusion about what that information means for acquisition.

The connection between a Signal and its source is important. Its supporting source text should substantiate the claim associated with it, and relevant qualifications should not be lost merely because the extracted claim is concise.

A Signal's category is a description of the evidence, not proof that the evidence has been categorized correctly. Downstream logic must not assume that a category label guarantees semantic precision.

**Extraction does not independently establish whether a claim is true.**

### 3. Evidence relationships and patterns

Individual Signals may become more meaningful when considered together.

Their relationships may include:

- Converging clues about an uncertain identity
- Connections between an instrument and a reported history
- Configuration details alongside evidence of modification
- Relationships between instrument information and transaction context
- Tensions or contradictions among claims
- Combinations of otherwise ordinary details that create a reason to investigate

Some recurring structures may be explicit enough for deterministic detection. Others require contextual interpretation.

An evidence pattern identifies a particular structure in the available Signals. Detecting that structure does not, by itself, establish that it is significant, correctly interpreted, or worth surfacing.

Pattern detection should remain limited to what its evidence and rules can support.

A string match is not automatically semantic understanding. Different claims are not automatically contradictory, and a reported association is not automatically verified provenance.

### 4. Evidence interpretation

Interpretation considers what the available evidence may mean in context.

It connects relevant details and relationships to explain why a listing may deserve closer attention.

A useful interpretation should do more than repeat the listing. It should provide a defensible explanation of why the selected evidence matters while preserving relevant attribution, uncertainty, and limitations.

Interpretation must distinguish between two separate responsibilities:

- **Evidence selection:** identifying which information is relevant enough to include.
- **Evidence representation:** expressing the selected information without distorting its meaning.

An interpretation may select appropriate evidence but misrepresent it. It may also describe the selected evidence accurately while omitting context that materially changes its meaning.

Evidence references can help a person inspect the basis for an interpretation, but a reference alone does not establish that the evidence supports the exact claim being made.

The goal is not to reproduce every Signal. It is to preserve the evidence necessary to understand the reason for attention.

### 5. Human attention

Hedstok's intended output is an explainable observation that helps a person decide whether to investigate further.

The observation should be:

- Grounded in available evidence
- Clear about relevant uncertainty and reported claims
- Selective without losing necessary context
- Explicit about the reason for attention
- Careful not to imply conclusions the evidence does not establish

An observation may justify further investigation without establishing a final answer.

The human remains responsible for deciding whether the lead merits further attention and what, if anything, should happen next.

## Evidence, Interpretation, and Uncertainty

These concepts should remain distinct:

- **Source material:** What the available source says or shows.
- **Signal:** A structured, source-grounded representation of a claim or observation.
- **Evidence relationship or pattern:** A connection or recurring structure among Signals.
- **Interpretation:** An explanation of why some combination of evidence may be meaningful.
- **Uncertainty:** What remains unknown, ambiguous, attributed, conflicting, or unsupported.
- **Attention judgment:** Whether the available evidence provides a reason to look more closely.

These concepts are related, but they are not interchangeable.

A seller's account of an instrument's history remains a seller-reported claim unless independently established. An unusual configuration does not, by itself, establish rarity, value, authenticity, or provenance. A conflicting description does not establish which description is correct.

Uncertainty is not automatically a negative signal. It may be relevant when the available evidence provides a meaningful question, clue, contradiction, or path for investigation.

Missing information alone should not be treated as proof of an opportunity or a problem.

Likewise, a detector's output should not imply more certainty than the underlying evidence supports. The name of a pattern, the role assigned to a Signal, and the wording of an interpretation can all communicate unintended certainty even when the underlying source claim has been preserved.

## Current Design Position

The experiments so far support investigating discovery through structured, source-grounded evidence, explicit evidence relationships, and contextual interpretation.

They do not establish that any one extraction prompt, Signal taxonomy, detector set, or interpretation architecture is sufficient for reliable production use.

Several distinctions remain especially important:

- Faithful extraction and faithful interpretation are separate requirements.
- Source traceability and semantic support are separate requirements.
- Signal categories must be sufficiently consistent for the assumptions made by downstream consumers.
- Deterministic detection can recognize specific evidence structures without independently validating the meaning or truth of the claims.
- Interpretation quality depends on both selecting relevant evidence and preserving its meaning.
- Small experimental samples are useful for revealing failure modes but cannot establish general reliability.

These are working conclusions from exploratory research, not proof that a particular production design is correct.

Detailed experimental results and unresolved cases belong in the relevant phase documents and audit records.

## Implementation Boundaries

The current experiments do not, by themselves, justify introducing:

- A permanent taxonomy of reasons for attention
- A numerical surface-worthiness score
- A confidence score or ranking algorithm
- A universal rule for how many Signals must support an interpretation
- Automated purchase recommendations
- Market valuation or authenticity judgments
- A general-purpose contradiction or provenance system based on narrow pattern matches

Such decisions should be made only when a concrete requirement and sufficient evidence support them.

This does not prohibit future implementation. It establishes that the implementation must earn its place through demonstrated need and appropriate evaluation.

## Guiding Question

At each stage of development, ask:

> **Does this help a person notice something meaningful in a listing, understand why it matters, and distinguish evidence from assumption?**

A proposed change should also answer:

- What demonstrated problem does it address?
- Which layer of the system is responsible for that problem?
- How will the intended improvement be evaluated?
- What could the change break or leave unresolved?

If a proposed feature cannot demonstrate a meaningful contribution to Hedstok's purpose, its place in the design should be reconsidered.
