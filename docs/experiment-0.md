# Experiment 0

## 1. Purpose

Experiment 0 tests the central premise of Hedstok before committing to a larger product architecture.

> **Can software discover interesting acquisition opportunities that a conventional search would not necessarily surface?**

The experiment is intentionally small. It focuses on whether Hedstok can produce useful discoveries from messy, incomplete, and inconsistent acquisition information.

Technical sophistication alone does not constitute success.

---

## 2. Hypothesis

A conventional search system primarily retrieves items based on explicit attributes such as:

- manufacturer;
- model;
- price;
- year;
- location;
- keywords.

Hedstok should attempt to identify opportunities based on relationships and signals that are less directly searchable, including:

- unusual provenance;
- uncertainty;
- contradictory information;
- unusual combinations of characteristics;
- potentially significant modifications;
- seller behavior or motivation;
- relationships between multiple pieces of information;
- information that warrants further investigation.

The experiment does not assume that these signals will produce useful results.

---

## 3. Input

Experiment 0 uses a small synthetic dataset of approximately 10–20 guitar listings and acquisition leads.

The dataset intentionally contains a mixture of:

- ordinary listings;
- incomplete descriptions;
- personal or private leads;
- provenance claims;
- unusual instruments;
- potentially interesting opportunities;
- misleading or contradictory information;
- cases that should not be considered interesting.

Each input contains the original human-style description as the information available to Hedstok.

The evaluation data is maintained separately and is not provided to the system during analysis.

---

## 4. Processing

Hedstok should attempt to:

1. ingest the raw listing or lead;
2. extract relevant claims and attributes;
3. preserve the original source information;
4. distinguish stated facts from uncertain claims;
5. identify potentially interesting signals;
6. determine whether the combination of signals warrants investigation;
7. explain why a candidate was surfaced;
8. identify what remains unknown or requires verification.

The system should not treat extracted information as automatically true.

---

## 5. Output

The experiment should produce a small set of candidates worth investigating.

For each surfaced candidate, Hedstok should provide:

### Why it surfaced

A concise explanation of the characteristics or relationships that attracted attention.

### Evidence

The source information supporting those observations.

### Uncertainty

Claims or details that remain unverified, ambiguous, or contradictory.

### Suggested investigation

The most useful next piece of information to obtain or verify.

The desired result is not:

> "Buy this guitar."

The desired result is:

> **"This is worth looking into. Here's why."**

---

## 6. Discovery vs. Value

Experiment 0 intentionally separates **interesting** from **valuable**.

A candidate may be worth investigating because it has:

- unusual provenance;
- an unresolved identification;
- contradictory information;
- an unusual combination of characteristics;
- potentially significant history;
- another reason to warrant human attention.

None of these automatically establish monetary value.

Hedstok should not claim that an instrument is valuable, rare, authentic, or a good deal unless the available evidence supports that conclusion.

---

## 7. Evidence Principle

Hedstok should preserve the distinction between:

**Claim**

What the source says.

**Evidence**

The information supporting the claim.

**Uncertainty**

What is unknown, ambiguous, or unverified.

**Interpretation**

What Hedstok believes may be worth investigating.

The system should not silently convert uncertain claims into established facts.

---

## 8. AI Principle

AI may be used to interpret messy natural-language information, but it is not the final authority.

Potential uses include:

- extracting structured information from descriptions;
- identifying claims;
- identifying provenance;
- recognizing uncertainty;
- comparing related pieces of information;
- identifying potentially contradictory information;
- generating evidence-grounded explanations.

AI output should remain traceable to the source material.

Hedstok should not use an LLM as an opaque "interestingness" oracle.

### AI Extraction Finding

Initial testing demonstrated that Gemini can convert unstructured listing text into structured observations containing:

- a signal type;

- a concise claim;

- source text supporting the claim.

The extraction prompt explicitly requires claims to remain source-grounded and prohibits fact-checking, inference, valuation, or other interpretation.

Testing also showed that unconstrained extraction can introduce interpretation beyond the source, such as attempting to fact-check claims or characterize them as unsupported. The extraction boundary was therefore tightened so that verification and interpretation remain outside the AI extraction step.

A full extraction run was then performed against all 14 Experiment 0 listings in a single request. The resulting observations were generally source-grounded and preserved important distinctions such as uncertain identification, provenance claims, seller context, image-derived observations, and potentially conflicting information.

The extraction did not reproduce every signal represented in the separate evaluation dataset, and signal categories were sometimes broad or inconsistent. These results do not currently justify expanding the extraction schema. The extraction layer's purpose is to establish a faithful observation layer; it should not encode the discovery logic itself.

The full run demonstrated that potentially interesting cases can be represented as combinations or relationships between extracted observations. Examples include:

- conflicting text and image descriptions;
- provenance combined with unusual historical claims;
- uncertain identification combined with ownership history;
- seller context combined with instrument characteristics.

This establishes the current architectural boundary:

> **AI extracts. Software reasons. Human evaluates.**

The frozen extraction output was considered sufficient to proceed to deterministic discovery analysis. Evaluation of that output identified both discovery failures and limitations in the organization of extracted observations. These findings motivated a targeted revision of the extraction schema rather than an attempt to make the AI independently determine what is "interesting."

The original extraction baseline remains preserved as an experimental reference point. The revised schema represents the next extraction iteration and should be evaluated against the discovery failures identified during Experiment 0 rather than treated as an assumption that the revised categories are universally correct.

### Semantic Extraction Schema Finding

The initial extraction vocabulary used several narrowly defined categories, including separate categories for brand, ownership history, recording history, electronics, and miscellaneous information.

The evaluation showed that these categories were inconsistent in granularity. Some represented semantic domains, while others represented specific attributes or implementation details. This made it difficult to reason consistently about relationships between observations.

The extraction schema was therefore revised to use a smaller set of semantic evidence categories:

- `identity` — manufacturer, model, instrument type, or other evidence about what the instrument is or may be;
- `configuration` — physical, electronic, hardware, construction, or unusual configuration characteristics;
- `story` — human history, ownership, personal significance, previous players, recordings, use, or other narrative associated with the instrument;
- `associated_equipment` — amplifiers, accessories, or other equipment connected to the listing or instrument;
- `seller_context` — seller inventory, collection, selling or trading motivation, or business context;
- `condition` — physical condition, damage, wear, or originality;
- `market_context` — price, date, trade terms, or other listing or market context.

Uncertainty is treated as a property of an observation rather than as a separate semantic category.

This creates a deliberate distinction between **what an observation is about** and **how that observation relates to other observations**.

For example:

> `identity + configuration`

is a relationship that can be evaluated by the deterministic discovery layer. It is not itself an extraction category.

Similarly, contradiction and convergence are relationships between observations rather than properties that the extraction model must independently classify.

The revised schema intentionally does not introduce subtypes beneath categories such as `story`. For example, ownership history and recording history are both represented as `story` observations rather than creating a premature taxonomy of story types.

This creates a temporary limitation for existing discovery rules that depended on those distinctions. That limitation is intentional. The experiment should not expand the extraction taxonomy solely to preserve previously implemented rules.

The schema should become more specific only when an observed discovery failure demonstrates that the additional distinction is necessary.

The resulting architectural boundary is:

> **AI classifies evidence semantically. Discovery reasons about relationships between evidence.**

This preserves the principle:

> **AI extracts. Software reasons. Human evaluates.**

### Deterministic Discovery Finding

The initial deterministic discovery layer successfully surfaced several distinct relationship types from the frozen extraction baseline:

- ownership history combined with uncertain identification;
- ownership history combined with recording-history claims;
- multiple modification or specialized-configuration signals;
- conflicting instrument identification and image-based observations.

The discovery layer deliberately operates on extracted observations rather than attempting to determine whether individual claims are true.

Initial adversarial testing also identified a false-positive path in the modification rule. The rule initially treated unrelated uses of terms such as "pickup" and "setup" as evidence of modification. The rule was tightened to require stronger modification-oriented language, and the resulting behavior passed six targeted tests covering positive cases and plausible false positives.

This establishes an important boundary for the discovery layer:

> **Discovery rules must identify relationships between observations, not merely the presence of interesting-sounding words.**

The current rules are intentionally narrow and experiment-specific. Generalization will be driven by observed failures rather than by attempting to anticipate a complete discovery taxonomy.

### Discovery Schema Boundary

The revised extraction schema changes the appropriate unit of deterministic discovery from individual signal keywords or narrowly defined signal types toward relationships between semantic evidence categories.

The first relationship implemented under this model is **identity + configuration convergence**.

The rule does not require knowledge of specific manufacturers, models, instrument types, or configuration terminology. It only requires the presence of both identity evidence and configuration evidence. The rule therefore tests whether semantic classification by the extraction layer can enable deterministic relationship analysis without transferring the judgment of "interestingness" to the AI.

This approach also exposes a boundary in the existing discovery rules. Some earlier rules depended on distinctions that are no longer represented as separate extraction categories. For example, the previous provenance rule distinguished ownership history from recording history, while both are now represented as `story`.

Rather than restoring those distinctions as subtypes, such rules should be considered candidates for redesign or deferral. Their future implementation should be driven by an observed need for the distinction, not by a requirement to preserve the original rule structure.

This establishes a broader design principle:

> **Discovery rules should operate on relationships that the evidence schema can express meaningfully. The extraction schema should not grow solely to accommodate a pre-existing rule.**

The identity/configuration convergence rule passed four targeted tests covering:

- positive identity + configuration convergence;
- identity without configuration;
- configuration without identity;
- identity combined with unrelated evidence.

This demonstrates the relationship in isolation without yet establishing that the relationship itself represents a useful acquisition opportunity. Human evaluation remains responsible for that determination.

### Schema Decision

Experiment 0 will treat signal categories as **semantic evidence domains**, not as a taxonomy of every possible fact that may appear in a listing.

The current categories are:

- `identity`
- `configuration`
- `story`
- `associated_equipment`
- `seller_context`
- `condition`
- `market_context`

Discovery rules may combine these categories to identify relationships worth presenting for human evaluation.

The experiment will not introduce additional signal subtypes solely to preserve an existing discovery rule. If a discovery failure demonstrates that a distinction within one category is necessary, that need will be documented as an observed requirement and evaluated before expanding the schema.

This means that some earlier discovery rules may be retired, redesigned, or deferred when their original distinctions cannot be expressed meaningfully by the revised evidence model.

This is intentional.

> **The evidence schema should describe what the system observed. Discovery rules should describe relationships the system can reason about.**

### Discovery Rule Audit

The original deterministic discovery rules were reviewed against the revised semantic evidence schema. The audit distinguishes between discovery concepts that remain useful, rules that require redesign, and rules that should be deferred rather than preserved solely for compatibility with the previous schema.

| Original rule                             | Decision | Rationale                                                                                                                                                                                                                                                                       |
| ----------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `find_provenance_clusters`                | Defer    | The rule depended on distinguishing ownership history from recording history. Both are now represented as `story`, and the experiment has not demonstrated that story subtypes are necessary.                                                                                   |
| `find_uncertain_identification`           | Redesign | Uncertain instrument identity remains an observed investigation signal, but ownership history is not inherently required for the relationship. The revised rule should operate on uncertain `identity` evidence.                                                                |
| `find_modification_cluster`               | Defer    | The original implementation relies on keyword matching across heterogeneous signal types. The revised schema represents these observations as `configuration`, but the experiment has not established a sufficiently general `configuration + configuration` relationship.      |
| `find_identity_configuration_convergence` | Keep     | This is the first discovery rule implemented directly against the revised semantic schema. It demonstrates a relationship between `identity` and `configuration` evidence without requiring domain-specific vocabulary in the deterministic layer.                              |
| `find_seller_motivation`                  | Defer    | The evaluation of listing-04 identified an extraction omission rather than a demonstrated discovery failure. Seller motivation is now represented as `seller_context`, but a useful relationship involving seller context has not yet been established.                         |
| `find_contradictions`                     | Redesign | Contradiction remains a meaningful discovery relationship, but the current implementation is tied to listing-specific terminology and implicit image-source conventions. Contradiction should remain a relationship between evidence rather than become an extraction category. |

The audit establishes that previously implemented discovery rules are experimental hypotheses, not architectural commitments. A rule may be retired, redesigned, or deferred when the revised evidence model no longer expresses its original assumptions meaningfully.

The active discovery layer should therefore remain small and evidence-driven. New rules should be introduced when observed evaluation failures establish a useful relationship that can be expressed by the current evidence model.

> **Do not preserve a discovery rule merely because it already exists. Preserve the discovery concept only when the evidence supports the relationship.**

---

## 9. Evaluation

Experiment 0 will be evaluated using the separate evaluation dataset.

Evaluation should consider:

### Discovery

Did Hedstok surface candidates that are genuinely worth investigating?

### Relevance

Were the surfaced candidates interesting for reasons supported by the available information?

### Evidence

Can each important observation be traced back to source material?

### Uncertainty

Did Hedstok preserve uncertainty rather than presenting assumptions as facts?

### False positives

Did Hedstok surface ordinary or weak cases merely because they contained interesting-sounding words?

### False negatives

Did Hedstok overlook cases containing meaningful signals?

### Explanation quality

Does the explanation describe _why_ the candidate was surfaced rather than simply restating the listing?

### Hallucination

Did Hedstok introduce information that was not present in the source material?

---

## 10. Success Criteria

Experiment 0 is considered promising if Hedstok can surface at least one candidate that:

1. is genuinely worth investigating;
2. contains a meaningful signal or relationship;
3. would not necessarily be obvious from a conventional keyword/attribute search;
4. can be explained using the available evidence;
5. preserves uncertainty where appropriate.

A technically impressive implementation that does not produce useful discoveries is not considered a successful experiment.

---

## 11. Sample Listing Evaluations

[Samples](../experiment-0/output/extraction-baseline.json)

1. listing-03
    - Classification: intentional non-discovery
    - Reason: Signals describe an ordinary beginner-oriented package with minor condition issues, but do not indicate an acquisition opportunity worth investigating.
    - Implication: Unusual or negative condition signals should not automatically become discoveries. Discovery requires a meaningful acquisition relationship, not merely something notable about a listing.

2. listing-04
    - Classification: extraction failure
    - Reason: The source listing includes a specific seller trade motivation (tube/high-gain amplifiers) that was not preserved in the frozen extraction. The extracted signals identify a Rickenbacker 12-string, its 2006 date, an all-original claim, and new strings, but do not preserve the seller's motivation.
    - Implication: Potential discoveries can be lost when extraction omits contextual signals that become meaningful only in combination with instrument characteristics and seller intent.

3. listing-07
    - Classification: domain-context candidate
    - Reason: The extraction identifies a 3/4-size KAY acoustic, but the potential acquisition significance depends on information not contained in the listing itself, including the historical context of the KAY brand and the relative rarity or utility of the 3/4-size configuration.
    - Implication: Some potentially interesting opportunities cannot be identified from listing evidence alone and may require external domain knowledge. This should remain distinct from extraction failure and deterministic discovery failure.

4. listing-08
    - Classification: discovery failure
    - Reason: The extracted signals contain enough information to identify a potentially interesting instrument relationship: an uncertain Fender/Precision identification is supported by physical characteristics consistent with a bass, while an Ampeg B-15 is also available. The discovery layer does not currently connect these signals.
    - Implication: Discovery may require relationships between instrument-identification clues, physical characteristics, provenance, and associated equipment. Basses are currently treated as part of Hedstok's guitar acquisition domain.

5. listing-09
    - Classification: discovery failure
    - Reason: The extracted signals describe a seller with a collection spanning late-1960s through early-1990s instruments, including multiple pickup configurations. These signals provide enough evidence to identify a potentially interesting collection-level opportunity, but the discovery layer does not currently reason about seller inventory or historical concentration.
    - Implication: Opportunities may exist at the seller or collection level rather than within a single instrument. Seller inventory characteristics and relationship context can be relevant discovery signals.

6. listing-10
    - Classification: external-context-dependent candidate
    - Reason: The listing identifies a recent Squier Sonic Stratocaster at $250. Domain knowledge suggests the asking price may be substantially above the instrument's typical market level, but the listing itself does not provide enough evidence to establish that.
    - Implication: Price anomalies may be useful acquisition signals, but identifying them requires external market context rather than listing evidence alone.

7. listing-12
    - Classification: discovery failure
    - Reason: The extracted signals provide a detailed identification of a 1950s Harmony Broadway H954, including its U.S. manufacture, original pickguard, period-correct strap, original chipboard case, and specific binding details. This combination provides substantial evidence of a historically specific and potentially desirable instrument, but the discovery layer does not currently recognize dense vintage-identification and originality relationships.
    - Implication: Detailed combinations of model identification, manufacturing history, original or period-appropriate accessories, and construction details may represent acquisition opportunities even when no single extracted signal is sufficient on its own.

8. listing-13
    - Classification: investigation candidate
    - Reason: The listing provides specific construction details, including a solid spruce top and mahogany back, sides, and neck, but does not identify a manufacturer. Combined with the $150 asking price, the incomplete manufacturer information creates enough uncertainty to warrant further investigation.
    - Implication: Missing identity information can itself be useful when a listing contains unusually specific characteristics that may justify verifying the instrument's manufacturer, construction, and market context.

9. listing-14
    - Classification: investigation candidate
    - Reason: The listing describes an unusual Telecaster/Stratocaster hybrid configuration and specifically characterizes the instrument as combining elements of both designs. The unusual configuration alone makes the listing worth investigating, while the lack of date information leaves an important identification detail unresolved.
    - Implication: Unusual instrument configurations can be acquisition signals in their own right. Identification gaps may increase the value of investigating an otherwise well-described instrument.

### Evaluation Finding

The sample audit identified multiple distinct sources of acquisition interest:

- relationships between extracted observations;
- contradictions or unresolved identification;
- seller and collection context;
- unusual instrument configurations;
- domain knowledge not contained in the listing;
- external market context;
- information that warrants investigation without yet establishing a specific discovery rule.

These findings indicate that "interesting" cannot yet be represented as a single deterministic signal or score. The next discovery iteration should address observed failure modes selectively rather than attempting to define a complete taxonomy of acquisition opportunities.

---

## 12. Non-Goals

Experiment 0 will not attempt to build:

- autonomous purchasing or bidding;
- universal marketplace scraping;
- a complete marketplace;
- continuous monitoring;
- notifications;
- authoritative guitar valuation;
- a general-purpose chatbot;
- a trained machine-learning model;
- sophisticated entity resolution;
- full computer-vision analysis;
- production authentication or authorization;
- a production deployment architecture.

These may be considered only if the experiment demonstrates that the underlying concept is useful.

---

## 13. Guiding Principle

> **The experiment should earn the right to become a product.**

Implementation choices should follow what is learned from the experiment rather than assuming the architecture of the eventual system in advance.
