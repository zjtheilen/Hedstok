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

### Endpoint Representation

The relationship representation test raises a further question: whether relationship endpoints require independently represented entities, or whether they can remain references to information already present in the evidence.

Listing 05 does not require a separately represented `Dad` entity to express the relationship:

```text
Instrument → belonged to → Dad
```

The evidence already identifies the endpoint as the seller's father. Similarly, Listing 08 can express the relationship:

```text
Instrument → associated with → Ampeg B-15
```

without requiring an independently represented equipment entity.

This suggests that an Evidence Relationship can initially identify its endpoints from the evidence without establishing persistent entity identity. The relationship provides explicit structure between the endpoints, while the supporting signals preserve the evidence from which those endpoints are identified.

Independently represented entities would become necessary if Hedstok needs persistent identity, reuse, or resolution of the same endpoint across multiple pieces of evidence or listings. That requirement has not yet been established.

### Supporting Evidence Reference

The endpoint representation investigation identifies a further constraint. While an Evidence Relationship can identify its endpoints without requiring independently represented entities, the relationship must also be able to identify the evidence supporting it if that evidence is to remain directly addressable.

The current `Signal` model does not provide a stable identifier for individual signals. Signals are currently contained within a listing extraction and are represented by their type, claim, and source text.

For example, Listing 05 contains evidence from which the following relationship can be identified:

```text
Instrument → belonged to → Dad
```

The existing signal preserves the evidence needed to establish that relationship, but there is currently no stable signal reference that a relationship could use to identify that specific supporting evidence.

The same constraint appears in Listing 08:

```text
Instrument → associated with → Ampeg B-15
```

The relationship can be identified from the existing evidence without introducing an independently represented equipment entity, but a relationship would require some reliable reference to the supporting signal if the evidence is to be explicitly associated with that relationship.

This suggests that the smallest missing capability is not an entity model, but a mechanism for reliably referencing individual evidence signals.

This investigation does not determine what form such a reference should take. It does not establish that a specific identifier scheme, relationship schema, or implementation is required.

### Evidence Continuity Across Extractions

The supporting evidence reference investigation raises a further question: whether individual evidence signals must retain their identity across multiple extractions of the same listing, or whether listing changes can be detected by comparing the existing evidence content.

The current signal model already preserves three pieces of structured information:

* `type`, which categorizes the signal;
* `claim`, which represents the extracted semantic statement;
* `source_text`, which preserves the source wording.

For detecting changes to the observed listing, `source_text` provides the primary basis for comparison because it preserves what the source actually stated.

For example, if two extractions contain the same source text:

```text
Extraction A
story
source_text: "my dad's guitar."

Extraction B
story
source_text: "my dad's guitar."
```

the evidence can be recognized as unchanged without requiring the same signal identifier to persist across extractions.

If the later extraction instead contains:

```text
story
source_text: "my dad's guitar. bought in 1988."
```

the source evidence has changed.

Similarly, newly appearing or disappearing source statements can indicate added or removed evidence.

This comparison does not require relationships themselves to persist across extractions. An Evidence Relationship can remain scoped to the extraction from which it was derived, while the underlying evidence can be compared across observations of the same listing.

The distinction between source evidence and extraction representation is also important. A change to `claim` or `type` while `source_text` remains unchanged may represent a change in Hedstok's extraction rather than a change to the listing itself.

This establishes two separate concerns:

```text
Source change
    ↓
Compare source evidence

Extraction change
    ↓
Compare structured representation
```

Content comparison does not establish persistent identity for an individual evidence item. Identical source text appearing in two extractions can be treated as corresponding evidence for change-detection purposes without establishing that the two signal instances are definitively the same persistent object.

The current investigation has not demonstrated a requirement for that stronger form of cross-extraction identity. Introducing persistent signal identity would therefore add architectural complexity without a demonstrated capability need.

### Preliminary Finding

> **Evidence Relationships require reliable references to supporting signals within their extraction scope, but those references do not currently need to persist across extractions. Hedstok can initially detect listing evidence changes by comparing existing source evidence, with `source_text` as the primary comparison basis and `claim` and `type` providing structured extraction context. Persistent cross-extraction signal identity is not currently justified.**

This remains an architectural investigation rather than an architectural decision.

### Minimum Signal-Reference Requirements

The evidence continuity investigation established that supporting signal references need to be reliable within the scope of the extraction from which a relationship is derived.

A reliable reference must distinguish one signal from another without depending on the signal's position in the extraction. It must resolve unambiguously to the specific signal so that the signal's `type`, `claim`, and `source_text` can be recovered. The reference must also have a defined scope.

The investigation does not establish a requirement for the reference to remain valid across separate extractions of the same listing. Cross-extraction evidence comparison remains a separate concern.

The reference should identify the evidence signal itself rather than encode the meaning of the relationship or identify an independently modeled domain entity.

### Multiple Supporting Signals

A relationship can legitimately be supported by multiple evidence signals.

For example, a relationship may depend on several independently extracted pieces of evidence rather than a single signal. The relationship therefore cannot assume a one-to-one correspondence between a relationship and its supporting evidence.

The distinction is between the relationship's endpoints and its supporting evidence:

```text
Evidence Relationship
├── endpoint A
├── endpoint B
└── supporting signals
      ├── signal reference
      ├── signal reference
      └── signal reference
```

Each reference identifies one individual signal, while a relationship may contain one or more supporting signal references.

This establishes a one-to-many capability for supporting evidence without requiring independently modeled entities or persistent signal identity across extractions.

### Signal-Level Reference vs. Span-Level Reference

The investigation also considered whether a supporting evidence reference must identify a specific occurrence or span within a signal rather than the signal itself.

Listing 05 provides a useful test because individual signals can contain multiple related claims. A single story signal can preserve the instrument's connection to the seller's father, the father's session-player history, and recording claims within the same source statement.

A relationship can reference that complete signal while preserving the original source wording through `source_text`. The relationship's meaning identifies the connection being represented; the supporting signal reference identifies the evidence from which that connection is derived.

The investigation did not identify a demonstrated capability that requires Hedstok to address a specific span within a signal independently of the signal as a whole.

This suggests that the signal is currently a sufficient unit of supporting evidence. Span-level provenance would introduce a finer-grained evidence model without a demonstrated requirement.

### Preliminary Finding

> **Evidence Relationships require reliable references to supporting signals within their extraction scope. A relationship may reference one or more complete signals, and the same signal may support multiple relationships. The current evidence does not establish a need for span-level references or persistent cross-extraction signal identity.**

This remains an architectural investigation rather than an architectural decision.

### Minimum Relationship Representation

The investigation then examined the minimum information required for an Evidence Relationship itself.

Listing 05 provides three representative cases:

```text
Instrument → belonged to → Dad

Instrument → associated with → Recording history

Instrument → associated with → Kirk Hammett
```

Each can be represented using the same conceptual structure:

```text
Endpoint A
    ↓
Relationship meaning
    ↓
Endpoint B
    ↓
Supporting signal references
```

The endpoints identify the two things connected by the relationship. The relationship meaning communicates what connection is being represented. Supporting signal references preserve the evidence grounding that connection.

The investigation did not identify a demonstrated need for additional relationship-level information such as confidence, scoring, timestamps, persistent endpoint identity, or relationship-specific explanations.

### Binary Relationship Boundary

The investigation also tested whether Evidence Relationships require more than two endpoints.

Listing 05 contains compound evidence involving the instrument, the seller's father, and recordings. However, the evidence can be represented as separate binary relationships while preserving the original compound source claim in the supporting signal.

For example:

```text
Instrument → associated with → Reign in Blood

Dad → associated with → Reign in Blood
```

The source evidence can support both relationships without requiring a single relationship containing the instrument, Dad, and the recording as simultaneous endpoints.

No encountered example has demonstrated a requirement for a relationship with more than two endpoints.

This suggests that a binary relationship is sufficient for the current evidence model. This is a representation boundary established by the current investigation, not a decision to implement a generalized graph structure.

### Relationship vs. Descriptive Evidence

Listing 08 provides an adversarial test for distinguishing Evidence Relationships from ordinary descriptive or configuration evidence.

The listing contains evidence such as:

```text
Instrument → belonged to → Dad

Instrument → associated with → Ampeg B-15
```

These can be represented as Evidence Relationships.

Other evidence describes the instrument itself:

```text
four thick strings
kind of long
Fender
Precision
```

These signals may collectively form an Evidence Pattern or provide identity/configuration evidence. The fact that they can be expressed grammatically as connections to the instrument does not by itself make them Evidence Relationships.

This establishes an important boundary:

> **Not every connection between extracted information constitutes an Evidence Relationship.**

Evidence Relationships should represent meaningful connections that provide a distinct structural capability rather than converting every descriptive or configuration signal into a graph edge.

### Relationship Meaning and Normalization

The minimum relationship representation requires the relationship to communicate its meaning, but the investigation has not yet established whether that meaning should use a controlled vocabulary or remain unnormalized.

A controlled vocabulary could improve consistency for operations such as querying, aggregation, and comparison by relationship type. However, defining such a vocabulary would introduce semantic commitments and could force early assumptions about domain relationships that the current evidence does not yet justify.

Free-form relationship meaning would preserve flexibility and avoid premature vocabulary design, but could make future semantic querying or aggregation more difficult if differently worded relationships represent the same concept.

At the current stage, Hedstok has demonstrated a need to represent, display, and trace Evidence Relationships. Querying, aggregation, and comparison by normalized semantic type would make a controlled vocabulary more useful, but those capabilities have not been demonstrated as requirements for the current architecture.

Therefore, a controlled relationship vocabulary is not currently justified.

This does not establish that free-form relationship meanings are the permanent design. It establishes only that normalization has not yet been demonstrated as a required capability.

### Current Architectural Finding

The investigation now provides a provisional minimum representation for Evidence Relationships:

```text
Evidence Relationship
├── endpoint A
├── relationship meaning
├── endpoint B
└── one or more supporting signal references
```

The current evidence also supports the following boundaries:

* endpoints do not require independently modeled entities;
* supporting references identify complete signals rather than spans;
* supporting evidence may contain multiple signal references;
* a signal may support multiple relationships;
* relationships are currently adequately represented as binary connections;
* descriptive or configuration evidence should not automatically become relationships;
* persistent cross-extraction relationship or signal identity has not been established as a requirement;
* a controlled relationship vocabulary has not yet been justified.

These findings remain provisional architectural investigation results. They do not establish a production schema or require immediate implementation.

## Next Step

The next investigation should determine whether the provisional Evidence Relationship representation provides enough structure for the capabilities Hedstok has actually demonstrated a need for, without introducing additional entity, identity, or normalization machinery.
