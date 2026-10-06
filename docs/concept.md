# Hedstok Concept

## 1. Problem

Used-instrument acquisition often depends on finding things that are not obvious from a conventional search.

Relevant information may be:

- incomplete;
- inconsistent;
- poorly structured;
- qualitative;
- distributed across different sources;
- buried in seller descriptions or personal leads;
- uncertain or contradictory.

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

- extracting structured information from natural-language listings;
- identifying claims and provenance;
- comparing descriptions;
- detecting potentially contradictory information;
- identifying information that warrants further investigation.

AI should not be treated as the final authority.

Deterministic analysis, source evidence, uncertainty, and human judgment remain part of the system.

## 6. Initial Experiment

The first experiment should remain deliberately small.

### Input

Approximately 10–20 guitar listings or acquisition leads containing realistic, imperfect information.

### Output

Hedstok should surface approximately 1–3 candidates it considers worth investigating.

For each candidate, Hedstok should provide:

- what caught its attention;
- the evidence supporting that observation;
- what remains uncertain;
- where the relevant information came from.

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

- autonomous purchasing or bidding;
- universal marketplace scraping;
- a general-purpose chatbot;
- an authoritative guitar valuation system;
- a full image-recognition system;
- a trained machine-learning model;
- a sophisticated entity-resolution platform;
- notifications or continuous monitoring;
- a complete marketplace;
- the eventual production architecture.

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

- **Multiple-listing input**
    - Establish a simple input format for processing a collection of listings rather than a single hard-coded listing.

- **Repeatable extraction**
    - Run the existing extraction capability across multiple listings and produce structured extraction artifacts.

- **Source preservation**
    - Maintain a direct connection between each extracted Signal and the source text from which it was derived.

- **Extraction evaluation**
    - Bring the useful evaluation principles from Experiment 0 into the working pipeline so extraction quality can be measured rather than assumed.

- **Uncertainty preservation**
    - Preserve the distinction between what a listing claims and what is actually established.
    - The extraction process must not silently convert uncertain or attributed claims into facts.

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

- directly extractable source evidence;
- interpretations or conclusions derived from source evidence;
- absence-based observations.

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

- Evidence Relationship implementation
- entity resolution or persistent entity modeling
- database implementation
- web UI
- recommendation or ranking systems
- marketplace integrations or automated web scraping
- pricing intelligence
- authentication or deployment infrastructure
- generalized AI orchestration
- graph architecture

These capabilities may become appropriate in later phases, but Phase 2 should not assume that they are required.

### Phase 2 Completion Criterion

Phase 2 is complete when Hedstok can repeatedly process a collection of listings and produce structured, source-grounded evidence with enough evaluation support to determine whether the extraction capability is reliable and useful enough to justify further development.

> **Phase 2 is intended to establish whether the core evidence pipeline works well enough to earn the next capability.**

## Phase 3 — Evidence-Based Discovery

### Goal

Determine whether structured, source-grounded evidence can be used to identify acquisition opportunities that are genuinely worth investigating.

Phase 3 should investigate the missing capability between evidence extraction and acquisition discovery without assuming in advance what mechanism will provide it.

The central question is:

> **Can Hedstok turn structured evidence into useful discoveries that a conventional search would not necessarily surface?**

### Scope

Phase 3 will focus on:

- **Discovery opportunities**
    - Establish what makes a listing or acquisition lead potentially worth investigating.
    - Investigate characteristics such as unusual provenance, contradictions, uncertain identification, unusual configuration, meaningful combinations of evidence, or other patterns that emerge from the experiment.

- **Evidence-based discovery**
    - Determine whether candidate opportunities can be identified from the Signals produced by the Phase 2 evidence pipeline.
    - Investigate whether individual Signals are sufficient or whether useful discoveries require combinations of Signals.

- **Discovery explanation**
    - Each candidate opportunity should explain what made it interesting.
    - Explanations should remain grounded in the underlying Signals and preserve the distinction between source claims, interpretation, and uncertainty.

- **Human evaluation**
    - Evaluate whether surfaced candidates are actually worth investigating rather than merely technically plausible.

    - The primary evaluation question is:

        > **Would I actually investigate this?**

    - Where appropriate, a later evaluation may ask:

        > **Would Dan actually investigate this?**

- **Discovery comparison**
    - Consider whether the discoveries provide information that would be difficult to identify through conventional keyword or attribute-based searching.
    - The experiment should distinguish genuinely useful discoveries from ordinary listings that merely happen to match obvious search criteria.

### Experimental Approach

Phase 3 should begin with the existing Phase 2 listing collection and structured extraction artifacts rather than introducing a larger data-acquisition system.

The initial workflow should remain conceptually simple:

```text
Listings
    ↓
Structured Signals
    ↓
Discovery mechanism
    ↓
Candidate opportunities
    ↓
Human evaluation
    ↓
Useful discovery?
    ↓
Supporting evidence
```

The discovery mechanism should be treated as an experimental component.

It may involve deterministic rules, combinations of Signals, explicit relationships, AI-assisted interpretation, or another approach that emerges from the evidence.

No particular mechanism is required at the beginning of Phase 3.

The experiment should favor approaches that can explain their output through the existing evidence model.

### Evaluation

Phase 3 should evaluate both **discovery usefulness** and **evidence grounding**.

#### Discovery usefulness

For each surfaced candidate, determine:

- Is there something genuinely interesting about this listing?
- Would a human consider it worth investigating?
- Is the discovery more than an obvious match to a conventional search criterion?
- Does the discovery depend on information that would otherwise be easy to overlook?

#### Evidence grounding

For each candidate, determine:

- What Signals support the discovery?
- Can the supporting evidence be traced back to the original listing?
- Are source claims distinguished from interpretation?
- Is uncertainty preserved?
- Does the explanation avoid asserting facts that are not established by the evidence?

#### False positives

The experiment should also record candidates that appear interesting mechanically but are not considered useful by human review.

Understanding why apparently interesting candidates are not useful is part of determining what discovery should mean for Hedstok.

### Evaluation Findings

Phase 3 should document the characteristics of discoveries that are considered useful, including:

- recurring types of opportunities;
- combinations of evidence that produce useful discoveries;
- evidence patterns that consistently produce false positives;
- discoveries that are obvious from conventional search;
- discoveries that appear genuinely non-obvious;
- limitations of the current Signal model.

These findings should determine whether a reusable discovery mechanism is justified.

### Out of Scope

Phase 3 does not currently include:

- automated marketplace scraping or universal marketplace search;
- marketplace API integrations;
- persistent entity resolution;
- cross-marketplace duplicate detection;
- automated purchasing, bidding, or seller contact;
- production recommendation or ranking systems;
- pricing or valuation intelligence;
- continuous background monitoring;
- notification infrastructure;
- production web UI;
- generalized graph architecture;
- persistent Evidence Relationship implementation unless the experiment demonstrates that relationships are necessary or useful for discovery;
- a second AI model acting as an automated semantic judge;
- a trained machine-learning model.

These capabilities may become appropriate later, but Phase 3 should first establish whether evidence-based discovery itself is useful.

### Phase 3 Completion Criterion

Phase 3 is complete when Hedstok has experimentally demonstrated whether structured, source-grounded evidence can produce candidate acquisition opportunities that a human considers worth investigating, and can explain those opportunities through the underlying evidence.

A successful result does not require a sophisticated discovery algorithm.

It requires evidence that Hedstok can move meaningfully from:

> **"Here is what the listing says."**

to:

> **"This is worth looking into, and here's why."**

If the experiment does not demonstrate useful discovery, that result is still a valid Phase 3 finding and should guide the next phase rather than being hidden by implementation complexity.

### Phase 3.1 — Discovery Experiment

#### Input

Phase 3.1 will use the existing artifacts produced during Phase 2:

- `experiment-0/input/listings.json`
    - The original collection of 14 guitar listings and their descriptions.

- `extraction2.json`
    - The structured Signals produced by the Phase 2 batch extraction.

- `experiment-0/evaluation/expected-signals.json`
    - Used as evaluation context rather than as instructions for what the discovery mechanism should find.

The discovery experiment should operate primarily on the structured evidence while retaining access to the original listings so that discoveries can be traced back to their source text.

No new listings or marketplace data will be introduced for the initial experiment.

No new extraction calls are required.

#### Task

The experiment will ask Hedstok to examine the structured evidence and identify **candidate acquisition opportunities**.

A candidate should represent something that appears potentially worth investigating because of the evidence present in the listing.

The experiment should consider possibilities including:

- unusual provenance or personal history;
- contradictions or inconsistencies;
- uncertain or potentially incorrect identification;
- unusual instrument configurations;
- meaningful combinations of otherwise ordinary Signals;
- interesting stories or circumstances;
- evidence that suggests useful follow-up investigation.

These possibilities are not predefined definitions of a discovery. The experiment should remain open to other patterns that emerge from the evidence.

The core task is:

> **Review the available structured evidence and identify candidate acquisition opportunities supported by the available evidence. For each candidate, explain what makes it interesting using the available evidence.**

The discovery process should not:

- determine whether seller claims are true;
- determine monetary value;
- make a purchasing recommendation;
- invent missing information;
- convert uncertainty into certainty.

#### Evaluation

Human evaluation is the primary measure of Phase 3.1 success.

For each surfaced candidate, evaluate:

**Discovery usefulness**

> **Would I actually investigate this listing further?**

**Non-obviousness**

> Does the discovery depend on evidence or a combination of evidence that ordinary keyword or attribute-based searching might miss?

**Explanation usefulness**

> Does the explanation make clear why the listing might be worth investigating?

**Evidence grounding**

> Can the explanation be traced back to the relevant Signals and original listing?

**Uncertainty preservation**

> Does the discovery distinguish source claims from established information and preserve unresolved questions?

The evaluation should also record candidates that initially appear interesting but are ultimately not considered worth investigating.

These false positives are useful experimental evidence because they help establish what discovery should and should not mean for Hedstok.

A technically plausible or unusual observation is not sufficient for success. The goal is to identify opportunities that are genuinely useful for human investigation.

#### Expected Output

Each candidate opportunity should contain, at minimum:

- **listing ID**
- **discovery description** — what Hedstok noticed;
- **reason** — why the observation might make the listing worth investigating;
- **supporting Signals** — the evidence relevant to the discovery;
- **source grounding** — the original source text supporting that evidence;
- **uncertainty** — relevant claims or questions that remain unresolved.

Conceptually:

```text
Candidate opportunity
        ↓
Listing ID
        ↓
What makes it interesting
        ↓
Supporting Signals
        ↓
Source evidence
        ↓
What remains uncertain
```

The output should not include:

- purchasing recommendations;
- monetary valuations;
- confidence or ranking scores;
- verification results;
- invented explanations for why an instrument is valuable.

Phase 3.1 is an experiment to determine whether structured evidence can produce useful discoveries. It is not yet a commitment to a particular discovery algorithm, schema, or implementation architecture.

### Phase 3.1 Initial Discovery Findings

The first discovery experiment was run against the Phase 2 batch extraction artifact without additional extraction calls.

The discovery process surfaced five candidate acquisition opportunities:

- listing-01;
- listing-05;
- listing-06;
- listing-08;
- listing-11.

Human review judged all five surfaced candidates worth investigating. This demonstrates that structured Signals can support discovery of acquisition opportunities that a human considers worth further investigation.

A separate human review of all 14 listings identified 11 listings as worth investigating, one as potentially worth investigating, and two as not worth investigating. The first discovery run therefore did not demonstrate complete discovery coverage.

Several clear discovery misses were identified. Listings 02, 04, 09, and 14 contained evidence that the human reviewer considered worth investigating but were not surfaced by the discovery process. The relevant evidence was already present in the structured Signals, so these cases represent discovery interpretation misses rather than extraction failures.

The misses also revealed several distinct discovery requirements:

- useful opportunities may emerge from combinations of otherwise ordinary Signals;
- unusual configuration or identification evidence may itself warrant investigation;
- seller or inventory context may represent an acquisition opportunity independently of an individual instrument;
- some human discoveries depend on external knowledge that is intentionally unavailable under the current source-grounded discovery rules.

Listings 07 and 12 illustrate the latter boundary. Their human-interest judgments included knowledge not established by the supplied Signals, such as knowledge about a brand's status or the market desirability of an instrument. These cases should not currently be treated as failures of source-grounded discovery.

Listing 13 was treated as a weak or ambiguous opportunity during human review and does not currently provide strong evidence of a discovery capability failure.

The first experiment also demonstrated that discovery can arise from relationships between Signals. Listing 11 was identified because the textual identification and image-description Signals conflict. This supports further investigation of multi-Signal discovery without establishing a general relationship or graph architecture.

These findings are provisional. They do not establish a production discovery taxonomy, ranking system, external-knowledge architecture, or persistent relationship model.

The next experiment revised the discovery prompt to more explicitly test combinations of Signals, unusual configurations, seller/inventory context, and the distinction between source-grounded evidence and external knowledge. The same discovery input was used so that the results could be compared with the first experiment.

### Phase 3.1 Second Discovery Experiment Findings

The second discovery experiment used the same structured evidence input, model, and execution process as the first experiment, with only the discovery prompt revised to more explicitly address combinations of Signals, unusual configurations, seller or inventory context, and external-knowledge boundaries.

The revised discovery process surfaced seven candidate acquisition opportunities:

- listing-01;
- listing-02;
- listing-05;
- listing-06;
- listing-08;
- listing-09;
- listing-11.

Human review judged all seven surfaced candidates worth investigating. Compared with the first experiment, the revised prompt recovered listings 02 and 09, both of which had previously been identified as clear discovery misses. This indicates that prompt guidance about Signal combinations and seller or inventory context can improve discovery coverage without necessarily introducing false positives among the surfaced candidates.

Listings 04 and 14 remained unsurfaced despite containing source-grounded evidence that the human reviewer considered worth investigating. Both were within the revised prompt's stated discovery scope. This provides evidence that prompt expansion alone does not reliably produce complete discovery coverage.

The second experiment also showed continued interpretation drift beyond the supplied evidence. Some explanations introduced significance not established by the Signals, including descriptions such as "vintage," "period-appropriate," and "high-end." These cases demonstrate that source-grounded extraction does not by itself guarantee source-grounded discovery interpretation.

The experiments therefore indicate two distinct discovery challenges:

- useful opportunities can remain undiscovered even when the supporting Signals are present and the prompt explicitly identifies the relevant discovery pattern;
- discovered opportunities can acquire unsupported significance during interpretation.

The first two experiments provide evidence that structured Signals can support useful acquisition discovery, and that prompt guidance can improve discovery coverage. They do not yet establish that free-form AI discovery is sufficiently reliable as a production discovery mechanism.

Further work should determine whether these limitations can be addressed through a more explicit discovery mechanism, deterministic evidence combinations, structured relationships, or another approach before committing to a production discovery architecture.

### Phase 3.1 Third Discovery Experiment Findings

The third discovery experiment analyzed the human evaluation results from the first two discovery experiments to determine whether the human "investigate" decisions could be explained by recurring patterns in the existing Signals.

The analysis did not introduce new extraction calls or new evidence. Instead, the existing structured evidence was reviewed against the 11 listings that the human reviewer considered worth investigating.

Several provisional evidence patterns emerged:

- **Converging Identity Clues** — an uncertain identity is accompanied by multiple additional Signals containing clues that may help narrow or investigate that identity;

- **Dated Configuration/Modification History** — a dated instrument has configuration, modification, retained-original-component, and/or condition evidence that together provide a potentially investigable picture of the instrument's history;

- **Instrument + Transaction Context** — instrument-specific evidence is accompanied by explicit transaction or trade context that may create an acquisition path;

- **Named Provenance** — a Signal describes an identifiable person, recording, performance, ownership history, or other specific provenance associated with the instrument;

- **Seller/Inventory Opportunity** — seller-context evidence indicates a meaningful collection or inventory combined with explicit willingness to sell, trade, make deals, or establish an ongoing acquisition relationship;

- **Cross-Source Contradiction** — Signals from different evidence sources make materially inconsistent claims about the same subject;

- **Explicitly Unusual Configuration** — a Signal directly describes an unusual or nonstandard configuration or combination of characteristics;

- **Dated Instrument + Originality/Period Evidence** — a dated instrument has evidence of original or period-appropriate components or accessories, optionally accompanied by explicit market context such as price.

These patterns are provisional observations from the current evaluation set rather than a proposed production taxonomy.

The patterns also differ in how readily they could be detected deterministically.

Some patterns appear to have relatively direct structural conditions. Named provenance, for example, can currently be treated as a discovery trigger when identifiable provenance is explicitly represented in a Signal. Seller or inventory opportunity can similarly be represented as a combination of collection or inventory evidence and explicit willingness to transact.

Other patterns contain a detectable structural component but require interpretation to determine whether the evidence is meaningful. Converging identity clues require determining whether multiple clues actually converge on a useful investigative possibility. Cross-source contradiction requires determining whether differing claims are semantically incompatible rather than merely different. Instrument and transaction context may require determining whether the instrument evidence is sufficiently relevant for the transaction circumstances to constitute an opportunity. Explicitly unusual configuration can be detected structurally when the source itself describes the configuration as unusual, but recognizing unusualness in less explicit cases may require additional interpretation.

The dated configuration and modification pattern illustrates another limitation. A deterministic detector could identify a dated instrument combined with configuration, modification, retained-original-component, or condition evidence, but this structural combination is broad enough that it may produce false positives. Detecting the pattern and determining whether a particular instance is actually useful for acquisition discovery are therefore separate questions.

The dated instrument and originality/period evidence pattern illustrates the role of external knowledge. The supplied Signals can preserve evidence such as a 1950s instrument, a specific model, original components, period-appropriate accessories, and an explicit price. However, recognizing the resulting opportunity as a potentially rare, desirable, high-quality, or unusually inexpensive instrument depends on knowledge not established by those Signals. However, recognizing the resulting opportunity as a potentially rare, desirable, high-quality, or unusually inexpensive instrument depends on knowledge not established by those Signals. The source-grounded evidence can therefore support the investigation without independently establishing the significance of the opportunity.

Listings 07 and 12 provide examples of this boundary. Listing 07 depended in part on external knowledge about the brand, while listing 12 depended in part on external knowledge about desirability, rarity, quality, and market price. These should not currently be treated as failures of the source-grounded evidence layer. Instead, they demonstrate that some useful acquisition discoveries may require knowledge beyond the listing itself.

The analysis also confirmed that not all human investigation decisions need to be represented by a discovery pattern. Listing 13 remained an ambiguous or weak opportunity, while listings 03 and 10 served as negative examples that did not meaningfully trigger the identified patterns.

The resulting architectural observation is that discovery may be better approached as a combination of evidence-pattern detection and evidence-grounded interpretation rather than as unconstrained AI discovery alone.

Conceptually:

```text
Signals
   ↓
Evidence pattern detection
   ↓
Detected evidence structures
   ↓
Evidence-grounded interpretation
   ↓
Candidate opportunities
   ↓
Human evaluation
```

Under this model, deterministic analysis could identify evidence structures that are reliable enough to detect mechanically, while an interpretation layer could determine what those structures may mean and explain why they might warrant investigation. Free-form AI discovery could remain useful as a secondary exploratory mechanism for identifying patterns that the deterministic layer does not yet recognize.

This separation also provides a way to preserve the existing evidence principle. The detection layer does not need to decide that an instrument is valuable, desirable, rare, or historically significant. It can identify the evidence supporting a possible opportunity and allow later interpretation to determine whether additional knowledge is required.

The third experiment therefore provides preliminary evidence that a hybrid discovery approach may be more appropriate than relying on free-form AI discovery alone. However, the current experiment does not establish a production discovery architecture, a permanent evidence-pattern taxonomy, a deterministic rule engine, an external-knowledge system, or a persistent relationship model.

Further experimentation should determine whether the provisional evidence patterns can be expressed precisely enough for useful deterministic detection, how frequently those detectors produce false positives, and where interpretation or external knowledge is genuinely required.
