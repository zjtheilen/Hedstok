# Experiment 1.2 — Candidate Relationship Derivation Audit

## Purpose

This document records the human audit of the first Experiment 1.2
candidate relationship derivation run.

The audit compares AI-proposed relationships against the existing
human relationship audit and evaluates evidence grounding, relationship
classification, missed relationships, and unsupported relationships.

The AI output is treated as experimental evidence. This document does
not modify the Experiment 1.2 hypothesis or relationship vocabulary
during the audit.

## Audit Method

For each fixture, evaluate:

1. **Supported** — Is the proposed relationship supported by the supplied signals?
2. **Type correctness** — Does the proposed relationship type match the defined relationship?
3. **Missed relationships** — Did the model fail to identify a relationship previously identified by the human audit?

Additional observations should be recorded without changing the experimental criteria retrospectively.

## Listing Audits

### Listing 01

- **Model proposed:** None
- **Supported:** N/A
- **Type correct:** N/A
- **Previously identified:** Historical Association
- **Missed:** Historical Association
- **Notes:** The model failed to recognize the multi-generational ownership and personal-significance evidence as a historical relationship.

### Listing 02

- **Model proposed:** Association
- **Supported:** Yes, partially
- **Type correct:** No
- **Previously identified:** No clean relationship
- **Missed:** None
- **Notes:** The model correctly recognized that the installed and retained pickups are meaningfully related. However, the proposed Association type does not match the experimental definition, which concerns a relationship between the instrument and another entity. The evidence instead describes configuration and modification history. This may indicate that the relationship vocabulary does not currently represent this type of evidence relationship.

### Listing 03

- **Model proposed:** None
- **Supported:** N/A
- **Type correct:** N/A
- **Previously identified:** No relationship; intentional non-discovery control
- **Missed:** None
- **Notes:** The model correctly returned no relationship for the control listing. This is consistent with the requirement that multiple signals alone should not produce a relationship.

### Listing 05

- **Model proposed:** Historical Association
- **Supported:** Yes, partially
- **Type correct:** Yes, for the proposed relationship
- **Previously identified:** Historical Association; Association
- **Missed:** Association
- **Notes:** The model correctly identified the recording-history evidence as a Historical Association, but it combined that evidence with the separate claim about Kirk Hammett's buckle scuffs. The model therefore recognized part of the relationship structure but collapsed two potentially distinct associations into one relationship. It also did not separately identify the claimed association between the instrument and Kirk Hammett.

### Listing 06

- **Model proposed:** None
- **Supported:** N/A
- **Type correct:** N/A
- **Previously identified:** Convergence; uncertain identification
- **Missed:** Convergence
- **Notes:** The model did not identify a relationship among the multiple clues bearing on the instrument's uncertain identity. The evidence does not establish a specific identity, but the combination of physical characteristics, age-related description, and uncertain manufacturer claim provides multiple pieces of evidence that could be investigated together.

### Listing 08

- **Model proposed:** Association
- **Supported:** Yes
- **Type correct:** Yes
- **Previously identified:** Association; Convergence
- **Missed:** Convergence
- **Notes:** The model correctly identified the association between the instrument and the available Ampeg B-15 amplifier. It did not identify the separate convergence among the instrument's physical description and identity clues, including the four thick strings, unusual length, and Fender/Precision claims.

### Listing 09

- **Model proposed:** None
- **Supported:** N/A
- **Type correct:** N/A
- **Previously identified:** Seller/collection-level opportunity
- **Missed:** Seller/collection-level relationship
- **Notes:** The model did not identify the seller's collection and business context as a potentially meaningful relationship. The evidence describes a collection with recurring instrument characteristics and a seller explicitly open to longer-term business arrangements. This does not map cleanly to the current experimental relationship vocabulary and may indicate that seller- or collection-level context is not adequately represented by the current relationship types.

### Listing 11

- **Model proposed:** Contradiction
- **Supported:** Yes
- **Type correct:** Yes
- **Previously identified:** Contradiction
- **Missed:** None
- **Notes:** The model correctly identified the contradiction between the textual identity claim and the image-based configuration evidence. The relationship is directly grounded in the supplied evidence, and the model did not attempt to determine which claim was correct.

### Listing 12

- **Model proposed:** Association
- **Supported:** Yes
- **Type correct:** Yes
- **Previously identified:** Association
- **Missed:** None
- **Notes:** The model correctly identified the association between the instrument and its original chipboard case and period-correct strap. The relationship is supported by the supplied evidence, although it is relatively direct and adds limited structure beyond the underlying extraction. This is recorded as an observation rather than a failure under the current evaluation criteria.

### Listing 14

- **Model proposed:** Convergence
- **Supported:** Yes, partially
- **Type correct:** No
- **Previously identified:** Distinctiveness
- **Missed:** Distinctiveness
- **Notes:** The model recognized that the identity and configuration signals are related, but classified the relationship as Convergence. The evidence instead describes a potentially distinctive configuration: the instrument is identified as a Fender HotShot Telecaster and is explicitly described as combining Tele and Strat characteristics. The signals do not independently converge on an uncertain underlying possibility; they describe the same claimed unusual configuration.

## Audit Findings

The first candidate relationship derivation run produced useful relationship proposals, but performance varied by relationship type and by the structure of the underlying evidence.

### Relationship Detection

The model successfully identified several relationships that were also supported by the human audit, including:

- Historical Association in listing 05
- Association with associated equipment in listings 08 and 12
- Contradiction in listing 11

The model also recognized meaningful connections in listings 02 and 14, but classified those relationships incorrectly.

The model missed previously identified relationships in listings 01, 06, 08, and 09. These misses included historical association, convergence, and seller/collection-level context.

The intentional non-discovery control in listing 03 produced no relationship, which supports the model's ability to refrain from creating a relationship solely because multiple signals are present.

### Relationship Classification

The run demonstrated that recognizing that evidence is related does not necessarily mean the model will classify the relationship according to the experimental vocabulary.

In listing 02, the model recognized a relationship between installed and retained pickups but classified it as Association even though the evidence described configuration and modification history.

In listing 14, the model recognized a relationship between identity and configuration evidence but classified it as Convergence rather than Distinctiveness.

These cases suggest that relationship detection and relationship classification should be treated as separate evaluation concerns.

### Relationship Decomposition

In listings 05 and 08, the model identified a valid relationship but failed to separate multiple relationships supported by the same evidence set.

Listing 05 contained both a claimed historical association with recording activity and a separate claimed association with Kirk Hammett.

Listing 08 contained an association with the Ampeg B-15 as well as a separate convergence among identity and configuration clues.

This indicates that the model may recognize some relationship structure without reliably representing all of the distinct relationships present.

### Relationship Vocabulary Observations

Two fixtures exposed evidence structures that do not map cleanly to the current vocabulary.

Listing 02 contains configuration and modification history that the current relationship types do not represent directly.

Listing 09 contains seller- and collection-level context that may itself form a useful investigative unit, but does not clearly fit the current instrument-centered relationship vocabulary.

These observations do not justify changing the vocabulary during this experiment. They instead identify areas for later evaluation.

### Evidence Grounding

The model generally based its relationship descriptions on the supplied signals and did not introduce outside knowledge or make acquisition judgments.

However, the output did not consistently satisfy the prompt requirement that `supporting_signals` exactly match the supplied signal claims. The model sometimes added signal-type prefixes to the returned values.

This means the semantic relationship proposals were partially grounded in the supplied evidence, but the current output format does not provide sufficiently reliable deterministic traceability for downstream use.

## Experiment Result

The experiment provides evidence that AI can propose source-grounded candidate relationships between extracted signals using a constrained relationship vocabulary.

The strongest evidence is the successful identification of multiple relationship types, particularly the contradiction in listing 11, while preserving the unresolved nature of the conflicting claims.

However, the experiment also demonstrated limitations in detection, classification, decomposition, and deterministic evidence traceability. Several missed relationships and misclassified relationships occurred even when the relevant evidence was present in the supplied signals.

The experiment therefore does **not** establish that AI relationship derivation is sufficiently reliable to serve as an automatic relationship layer.

It does establish that constrained AI relationship derivation is useful as an **experimental proposal mechanism** for further human evaluation.

The current evidence supports retaining the experimental flow:

```text
frozen extracted signals
        ↓
AI candidate relationship proposals
        ↓
human audit
        ↓
accepted / rejected / revised relationship understanding
```

No permanent relationship schema, deterministic validation layer, or automatic discovery behavior is established by this experiment alone.
