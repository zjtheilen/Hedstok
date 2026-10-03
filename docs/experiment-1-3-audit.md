# Experiment 1.3 — Conceptual Classification Audit

## Purpose

This document records the human conceptual classification performed for Experiment 1.3.

The experiment evaluates whether the concepts identified during the Experiment 1.2 architectural review represent meaningfully different kinds of evidence structure.

The experiment uses representative examples from the existing frozen Experiment 1.2 evidence. It does not introduce new AI generation, external domain knowledge, implementation, or permanent schema decisions.

The purpose of the audit is to determine whether the provisional categories:

* Evidence Relationship
* Evidence Pattern
* Investigation Indicator
* None / Unsupported

provide a useful conceptual distinction.

## Audit Method

Representative fixtures were reviewed in plain language before applying the provisional category terminology.

For each fixture, the question was:

> What is the evidence doing?

The classification was then translated into the provisional conceptual categories.

The audit intentionally avoided the original five Experiment 1.2 relationship types during initial interpretation so that the categories could be evaluated independently of the earlier vocabulary.

## Fixture Findings

### Listing 05

**Primary category:** Evidence Relationship

The evidence connects the guitar to people, recordings, and claimed historical use.

The guitar's claimed connection to the seller's father/session-player history and recordings represents a relationship between the instrument and external people or historical works.

A separate relationship exists between the guitar and the claim that buckle scuffs are associated with Kirk Hammett.

These relationships are materially different despite both being instances of evidence relating the instrument to another entity or historical context.

**External knowledge required:** No to recognize the relationship; external evidence would be required to verify the claims.

**Investigation implication:** Potentially.

### Listing 06

**Primary category:** Evidence Pattern

The evidence contains multiple uncertain clues concerning the instrument's age and identity.

The clues may collectively narrow an unresolved possibility about what the instrument is, without establishing a specific identity.

The classification does not depend on determining what specific instrument the fixture was intended to evoke. The supplied evidence only supports an unresolved possibility concerning the instrument's age and identity.

**External knowledge required:** No to recognize that the clues may converge; external knowledge would be required to identify or verify the instrument.

**Investigation implication:** Potentially.

### Listing 14

**Primary category:** Investigation Indicator

The evidence describes a potentially unusual configuration: a Fender instrument described as combining Telecaster and Stratocaster characteristics.

The supplied evidence does not establish rarity, uniqueness, or market significance. It identifies a characteristic that may warrant further investigation.

**External knowledge required:** No to recognize the potentially unusual configuration from the supplied claims; external reference context would be required to establish rarity or distinctiveness relative to a population.

**Investigation implication:** Yes / inherently investigation-oriented.

### Listing 03

**Primary category:** None / Unsupported

The listing contains multiple ordinary descriptive and contextual signals, including the instrument, low-wattage amplifier, Christmas-gift context, storage history, and broken strings.

From a human perspective, these signals do not establish a meaningful relationship, evidence pattern, or investigation-worthy characteristic.

This fixture therefore functions as a control against treating the mere presence of multiple signals as meaningful structure.

**External knowledge required:** No.

**Investigation implication:** No.

### Listing 08

**Primary categories:** Evidence Relationship and Evidence Pattern

The evidence contains multiple distinct structures.

The statement that the instrument belonged to the seller's father establishes a provenance relationship between the instrument and a prior owner.

The combination of four thick strings, unusual length, and the seller's Fender/Precision claims forms an evidence pattern concerning a possible specific instrument identity.

The Ampeg B-15 is also associated with the listing as related equipment, creating a separate evidence relationship.

Determining the domain significance of the Ampeg B-15 would require external knowledge; its presence in the listing alone establishes the association but not what the equipment implies.

This fixture demonstrates that multiple conceptual categories can legitimately coexist within the same evidence set.

## Findings

### Conceptual Distinction

The audit found that the provisional categories can describe materially different kinds of evidence structure:

* **Evidence Relationship** describes a connection between the instrument and another entity, person, work, event, ownership history, or associated context.
* **Evidence Pattern** describes multiple pieces of evidence that collectively bear on an unresolved possibility.
* **Investigation Indicator** describes a characteristic or configuration that may warrant investigation without itself establishing rarity, significance, or desirability.
* **None / Unsupported** provides a control for evidence that does not establish meaningful structure.

These distinctions were understandable when examples were described in plain language before applying the terminology.

### Multiple Categories Can Coexist

Listing 08 demonstrates that the categories are not necessarily mutually exclusive at the listing level.

A single evidence set can contain:

* a relationship,
* a pattern,
* and another relationship involving associated equipment.

This suggests that the categories describe **properties of evidence**, rather than exclusive classifications of an entire listing.

### Boundary Between Evidence and Domain Knowledge

The audit also reinforced a distinction between recognizing evidence structure and interpreting domain significance.

For example, the presence of an Ampeg B-15 can be represented as an association from the supplied evidence. Determining what that equipment implies about the instrument requires external domain knowledge.

Likewise, a configuration can be recognized as potentially unusual from the supplied claims without establishing that it is rare or unique.

This preserves the boundary between source-grounded evidence and later investigation or verification.

## Experiment Result

The Experiment 1.3 audit provides preliminary support for the hypothesis that the concepts identified during the Experiment 1.2 architectural review represent meaningfully different kinds of evidence structure.

The strongest evidence is that representative examples could be described naturally before applying terminology, and the resulting descriptions mapped consistently onto Evidence Relationship, Evidence Pattern, Investigation Indicator, or None / Unsupported.

The audit also exposed an important architectural property: these categories should not necessarily be treated as mutually exclusive types assigned to an entire listing. Multiple categories can coexist within the same evidence set.

This experiment does not establish:

* a permanent evidence model;
* a final relationship vocabulary;
* a production schema;
* deterministic classification rules;
* AI necessity;
* investigation scoring;
* rarity or market significance;
* or automatic discovery behavior.

The result supports retaining the conceptual distinction as a working model for subsequent investigation.

## Architectural Implication

The current evidence supports treating the three positive categories as different functional roles rather than forcing them into a single homogeneous relationship vocabulary:

```text
Evidence
   │
   ├── Evidence Relationships
   │      └── connections between entities/context
   │
   ├── Evidence Patterns
   │      └── multiple signals bearing on a possibility
   │
   └── Investigation Indicators
          └── characteristics that may warrant investigation
```

`None / Unsupported` remains useful as a control condition rather than an evidence structure.

No implementation decision is made by this experiment alone.

## Relationship Representation Test

The conceptual classification in Experiment 1.3 established that Evidence Relationships can be distinguished from Evidence Patterns and Investigation Indicators. A follow-up question is whether representing Evidence Relationships explicitly would provide a capability that the current signal model cannot represent cleanly.

Listing 05 provides a useful test case.

The current signal model can preserve evidence such as:

* the instrument belonged to the seller's father;
* the father was a session player;
* the instrument or playing associated with recordings including *Reign in Blood* and *Master of Puppets*;
* buckle scuffs were attributed to Kirk Hammett.

These signals preserve the underlying evidence, but the relationships between the instrument and the relevant people, recordings, and historical context exist only implicitly within the signal claims.

An explicit relationship representation would instead make those connections directly addressable. For example:

```text
Instrument → associated with → Dad
Instrument → associated with → Recording history
Instrument → associated with → Kirk Hammett
```

The immediate benefit is not additional factual information. The same source evidence is already present in the signals. The benefit is structural: Hedstok could identify and group the evidence supporting a particular connection rather than reconstructing that connection from the text of independent signals each time.

This would support operations such as:

* showing all evidence supporting an instrument's relationship with a particular person or context;
* distinguishing separate relationships involving the same instrument;
* treating a relationship as a unit of analysis rather than only as an interpretation of individual claims.

The comparison therefore identifies a potentially useful capability gap between independent evidence signals and explicitly represented Evidence Relationships.

However, this does not by itself justify implementation of a permanent relationship schema. The current experiment has not established that relationship-oriented operations are sufficiently important to require additional data structures, nor has it established the appropriate scope of such a structure. In particular, this finding does not justify introducing a generalized entity graph, entity-resolution system, or cross-listing identity model.

### Preliminary Finding

> **Explicit Evidence Relationships provide structural capabilities that independent signals do not represent cleanly, particularly the ability to group and address evidence supporting a specific connection. This is sufficient to justify continued architectural investigation, but not yet sufficient to justify implementation of a permanent relationship model.**

This remains an architectural investigation rather than an architectural decision.

## Next Step

The next investigation should determine what the smallest useful representation of an Evidence Relationship would need to support the capability identified above. This should focus on the structure required to represent a relationship and its supporting evidence without assuming a generalized entity graph, entity-resolution system, or broader domain model.
