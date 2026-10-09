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

> **Can software identify instruments whose available evidence gives a person a meaningful reason to stop and look closer?**

This is the central question of Hedstok.

Stories and story potential are a major source of those reasons, but they are not the only possible source. Provenance, unusual characteristics, distinctive configurations, human circumstances, personal relevance, and combinations of otherwise ordinary evidence may also make an instrument worth noticing.

The project should not assume that the answer is yes. Early development exists to test the premise.

## 3. Core Behavior

Given a collection of guitar listings or acquisition leads, Hedstok should attempt to:

1. understand the available information;
2. identify potentially interesting characteristics, stories, story potential, or relationships;
3. surface candidates worth investigating;
4. explain why each candidate was surfaced;
5. preserve the evidence supporting those explanations;
6. distinguish known information from uncertainty or inference.

The desired outcome is not a definitive purchasing recommendation.

It is:

> **"Hey. Look at this one."**

## 4. Story as a Core Principle

Hedstok is fundamentally interested in **stories and story potential**.

The project is not intended to identify the objectively “best” instruments, the most valuable instruments, or the instruments with the most desirable specifications. Those characteristics may sometimes contribute to an interesting discovery, but they are not the purpose of the system.

A guitar can be worth surfacing because:

- it has a specific personal or ownership history;
- it was reportedly used by someone;
- it has an unusual provenance claim;
- its history raises an interesting question;
- its identity is uncertain but the available evidence provides clues;
- several otherwise ordinary pieces of evidence combine into a compelling story;
- the circumstances surrounding the instrument suggest that there may be more to uncover.

The story does not need to be established as true before Hedstok can surface it. A reported story, unresolved question, contradiction, or other piece of evidence may itself provide a reason to investigate.

This is an important distinction:

> **Hedstok does not need to know that a guitar has a great story. It needs to recognize when there may be a story worth looking into.**

The intended behavior is therefore not:

> “This is the best guitar.”

It is:

> **“Hey. Look at this one.”**

That observation should invite human attention rather than replace human judgment. Hedstok surfaces the evidence and explains why it caught the system's attention; the human decides whether the story is interesting, whether it is worth investigating further, and what to do next.

“Story” is therefore a central touchstone for evaluating future Hedstok experiments. New capabilities should be considered not only in terms of whether they identify useful instrument characteristics, but whether they help Hedstok notice and surface **stories, story potential, or questions worth investigating**.

## 5. Evidence Principle

Hedstok should not treat extracted or inferred information as unquestioned truth.

Where practical, claims should remain traceable to their source.

Uncertainty should be preserved rather than silently converted into certainty.

## 6. AI Principle

AI may be useful for understanding messy, unstructured information.

Potential uses include:

- extracting structured information from natural-language listings;
- identifying claims and provenance;
- comparing descriptions;
- detecting potentially contradictory information;
- identifying information that warrants further investigation.

AI should not be treated as the final authority.

Deterministic analysis, source evidence, uncertainty, and human judgment remain part of the system.

## 7. Initial Experiment

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

## 8. Experiment Success

The experiment should be considered promising if Hedstok surfaces at least one candidate that is interesting specifically because it identified a relationship, anomaly, uncertainty, provenance detail, or combination of information that would not have been obvious from simply searching for a known guitar.

Technical sophistication alone does not constitute success.

## 9. Current Non-Goals

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

## 10. Guiding Principle

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

- **Provenance** — evidence that explicitly associates an instrument with a specific person, ownership history, recording, performance, or other identifiable historical context;

- **Seller/Inventory Opportunity** — seller-context evidence indicates a meaningful collection or inventory combined with explicit willingness to sell, trade, make deals, or establish an ongoing acquisition relationship;

- **Cross-Source Contradiction** — Signals from different evidence sources make materially inconsistent claims about the same subject;

- **Explicitly Unusual Configuration** — a Signal directly describes an unusual or nonstandard configuration or combination of characteristics;

- **Dated Instrument + Originality/Period Evidence** — a dated instrument has evidence of original or period-appropriate components or accessories, optionally accompanied by explicit market context such as price.

These patterns are provisional observations from the current evaluation set rather than a proposed production taxonomy.

The patterns also differ in how readily they could be detected deterministically.

Some patterns appear to have relatively direct structural conditions. Named provenance, for example, can currently be treated as a discovery trigger when identifiable provenance is explicitly represented in a Signal. Seller or inventory opportunity can similarly be represented as a combination of collection or inventory evidence and explicit willingness to transact.

Other patterns contain a detectable structural component but require interpretation to determine whether the evidence is meaningful. Converging identity clues require determining whether multiple clues actually converge on a useful investigative possibility. Cross-source contradiction requires determining whether differing claims are semantically incompatible rather than merely different. Instrument and transaction context may require determining whether the instrument evidence is sufficiently relevant for the transaction circumstances to constitute an opportunity. Explicitly unusual configuration can be detected structurally when the source itself describes the configuration as unusual, but recognizing unusualness in less explicit cases may require additional interpretation.

The dated configuration and modification pattern illustrates another limitation. A deterministic detector could identify a dated instrument combined with configuration, modification, retained-original-component, or condition evidence, but this structural combination is broad enough that it may produce false positives. Detecting the pattern and determining whether a particular instance is actually useful for acquisition discovery are therefore separate questions.

The dated instrument and originality/period evidence pattern illustrates the role of external knowledge. The supplied Signals can preserve evidence such as a 1950s instrument, a specific model, original components, period-appropriate accessories, and an explicit price. However, recognizing the resulting opportunity as a potentially rare, desirable, high-quality, or unusually inexpensive instrument depends on knowledge not established by those Signals. The source-grounded evidence can therefore support the investigation without independently establishing the significance of the opportunity.

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

### Phase 3.1 Fourth Discovery Experiment Findings

The fourth discovery experiment tested whether provisional evidence patterns identified during the third experiment could be expressed as deterministic detection conditions.

The experiment focused on three patterns:

- **Named Provenance**;
- **Seller/Inventory Opportunity**;
- **Dated Configuration/Modification History**.

The patterns were tested against representative positive, negative, and borderline examples. Where a pattern appeared structurally detectable, a small deterministic detector was implemented and evaluated against the existing extraction artifact. The purpose was to determine which parts of discovery could be detected from observable evidence structures and which parts required interpretation.

**Provenance** showed that deterministic detection is possible to a limited degree. Provenance may be represented across different Signal types rather than being limited to `story` Signals. For example, ownership or recording history may appear as `story` evidence, while physical evidence attributed to a specific person may appear as `condition` evidence. Ordinary ownership history was generally insufficient, while associations involving identifiable people, activities, performances, recordings, or other specific historical context were more likely to warrant investigation. Determining whether a provenance association is sufficiently meaningful therefore requires interpretation beyond the structural presence of an individual Signal.

**Seller/Inventory Opportunity** showed the strongest case for deterministic detection. The relevant structure consists of evidence of multiple instruments, a meaningful collection or inventory, or ongoing acquisition activity combined with explicit willingness to transact. Transaction activity may include selling, trading, buying, or establishing an ongoing acquisition relationship. A single instrument being offered for sale does not by itself constitute this pattern. The experiment indicates that much of this structure could potentially be detected mechanically, although interpretation may still be useful for borderline cases such as determining what constitutes meaningful inventory.

**Dated Configuration/Modification History** showed that its structural components can also be detected mechanically, but that determining whether a particular instance warrants investigation is more dependent on interpretation. Dated instruments combined with configuration, modification, originality, retained-original-component, or condition evidence produced a range of human judgments from possible to clearly investigable. Originality and modification history were particularly useful when they provided evidence about the instrument's configuration or history. The experiment also showed that the same structural pattern can be more or less likely to warrant investigation depending on the age and combination of the evidence.

**Cross-Source Contradiction** provided a clear example of a pattern that can be represented deterministically when the contradictory claims are explicit in the Signals. The experiment used listing 11, where one Signal identifies the instrument as a 1958 Les Paul while another Signal describes the image as a kid-size Stratocaster-style guitar. A deterministic detector identified this contradiction and returned the two supporting Signals. The detector produced no additional matches across the current 14-listing extraction artifact. This demonstrates that explicit contradictory evidence can be surfaced without determining which claim is correct. However, the experiment does not establish a general semantic contradiction detector; the current implementation only demonstrates the pattern for this specific form of identity conflict.

**Explicitly Unusual Configuration** provided another clear example of a pattern that can be detected deterministically when the source itself explicitly characterizes the configuration as unusual. The experiment used listing 14, where a Signal describes the instrument as “Tele and Strat in one guitar.” A deterministic detector identified this Signal and returned it as the supporting evidence. The detector produced no additional matches across the current 14-listing extraction artifact, and synthetic negative cases did not trigger on ordinary configuration or modification evidence. This demonstrates that an explicitly stated unusual configuration can be surfaced without relying on outside knowledge or determining independently whether a configuration is unusual. However, the experiment does not establish a general semantic detector for unusual configurations; the current implementation demonstrates the pattern for this specific explicit configuration.

These results reinforce the distinction between **evidence-pattern detection** and **discovery interpretation**. A deterministic detector can identify evidence structures without deciding that those structures represent a worthwhile acquisition opportunity.

Conceptually:

```text
Signals
   ↓
Evidence pattern detection
   ↓
Detected evidence structures
   ↓
Interpretation
   ↓
Candidate opportunities
   ↓
Human evaluation
```

The experiment also demonstrated that human judgment is not necessarily a component that must be eliminated from the discovery process. Some discovery patterns contain inherently interpretive questions about whether a combination of evidence is meaningful enough to investigate. The role of deterministic detection may therefore be to provide reliable evidence coverage, while interpretation determines whether detected evidence appears potentially worth investigating.

The three patterns produced different architectural characteristics:

| Pattern                                  | Deterministic detection | Interpretation required |
| ---------------------------------------- | ----------------------- | ----------------------- |
| Provenance                               | Partial                 | Significant             |
| Seller/Inventory Opportunity             | Strong                  | Limited                 |
| Dated Configuration/Modification History | Strong                  | Significant             |
| Cross-Source Contradiction               | Demonstrated            | Significant             |

These findings provide preliminary evidence that discovery may benefit from a hybrid approach in which deterministic analysis identifies evidence structures and an interpretation layer evaluates their potential significance.

This remains an experimental finding rather than a production architecture decision. The experiment produced small provisional detectors for selected evidence patterns, but these detectors are experimental implementations rather than a permanent evidence-pattern schema or generalized rule engine. The results show that some discovery patterns can be surfaced from observable evidence structures without external knowledge, while other patterns require semantic interpretation. The experiments do not establish that all useful discovery patterns can or should be detected deterministically.

### Phase 3.1 Final Discovery Comparison

The final Phase 3.1 experiment compared the human investigation decisions against the question of whether the underlying discovery was naturally represented by conventional item-oriented search.

This was a qualitative comparison rather than a benchmark of any particular search engine or marketplace. The purpose was to determine whether the useful opportunities identified during the experiment depended on relationships, combinations, contradictions, uncertainty, provenance, seller context, or other evidence structures that would not necessarily be represented directly by ordinary keyword or attribute-based searching.

The comparison used the 11 listings that the human reviewer classified as definite investigation candidates. The results showed several distinct categories.

**Listing 07** provided a clear conventional-search case. The listing described a 3/4-size KAY acoustic guitar, and the reason for considering it interesting depended substantially on external knowledge about the brand and instrument. The available Signals themselves did not contain an unusual relationship, contradiction, or combination that established why the instrument was worth investigating. This represents a case where Hedstok's source-grounded evidence model can preserve useful information, but discovery significance depends on knowledge beyond the source evidence.

Several listings demonstrated stronger evidence for discovery that would not naturally be represented by conventional item-oriented search.

**Listing 02** combined a dated instrument with modification history, retained original components, configuration evidence, and condition evidence. The individual facts could appear in a conventional listing search, but the potentially investigable combination is not naturally represented as a search criterion.

**Listing 05** contained multiple provenance-bearing Signals connecting the instrument to a specific owner, session-player history, recordings, and an attributed physical characteristic. The individual claims may be searchable if a user already knows what connection to search for, but the combined provenance structure is not naturally represented by ordinary item search.

**Listing 06** contained uncertain identity together with multiple additional clues about configuration, history, and transaction context. The uncertainty itself became part of the reason for investigation. Conventional search generally benefits from a known identity, whereas this discovery is based partly on the fact that the identity is unresolved.

**Listing 08** similarly contained uncertain identity with multiple additional clues that may help narrow the identity, including configuration, associated equipment, ownership history, and transaction context. The useful discovery depends on the combination rather than on any single obvious search attribute.

**Listing 09** demonstrated a different kind of discovery. The opportunity was primarily associated with the seller's collection, inventory, and willingness to establish an ongoing acquisition relationship rather than with a unique characteristic of the individual instrument. Conventional item-oriented search may surface the listing, but it does not naturally represent the seller as an acquisition opportunity.

**Listing 11** demonstrated a cross-source contradiction between an identity claim and an image-derived description. The contradiction itself is unlikely to be represented by conventional search because a user would generally need to know that the conflicting evidence exists before being able to search for it.

**Listing 14** contained an explicitly unusual configuration described by the source as "Tele and Strat in one guitar." The instrument could be found through conventional product-oriented search, but the unusual configuration provides an additional discovery characteristic that a user would not necessarily know to search for in advance.

Listings 01, 04, and 12 provided intermediate cases. Each contained potentially useful combinations of evidence, but the significance of those combinations was more dependent on interpretation or external knowledge. Listing 01 combined uncertain identity, multigenerational ownership, and personal significance. Listing 04 combined instrument evidence with explicit trade circumstances. Listing 12 combined age, model identity, originality or period evidence, accessories, and explicit price. These cases demonstrate that evidence-based discovery and conventional search are not mutually exclusive: a listing may be readily searchable while still containing a combination of evidence that becomes useful only after structured analysis.

The comparison therefore did not show that Hedstok will consistently find instruments that conventional search cannot find. It did show something narrower and more defensible: several useful acquisition opportunities depended on **relationships or combinations among pieces of evidence that conventional item-oriented search does not naturally represent**.

This distinction is important. Hedstok's potential value is not necessarily replacing search or retrieving hidden listings. It may instead be in transforming information contained within retrieved listings into structured evidence and surfacing characteristics that a human would otherwise have to notice and synthesize manually.

### Image-Derived Evidence

Listing 11 also establishes an important boundary for the evidence pipeline.

The contradiction identified during the experiment depended on a Signal derived from an associated image. In the current experimental artifact, that image-derived observation already exists as structured evidence, allowing the discovery mechanism to compare it with the textual identity claim.

A real Hedstok workflow cannot assume that a human will manually inspect every associated image and provide those observations to the application. If image-derived evidence is important to discovery, the upstream evidence pipeline will eventually need to support image analysis as another source of Signals.

This does not require a separate image-specific discovery architecture. The experiment suggests a simpler boundary:

```text
Listing text ──────┐
                   │
Listing images ────┼──→ Evidence extraction
                   │          ↓
Other sources ─────┘       Signals
                              ↓
                    Evidence-based discovery
```

The discovery layer can operate on the resulting Signals without needing to know whether a Signal originated from text, an image, or another supported source.

Image analysis is therefore identified as a future evidence-generation capability rather than a requirement to complete the current Phase 3 discovery experiment.

### Phase 3 Final Findings

Phase 3 demonstrated that structured, source-grounded evidence can support useful acquisition discovery, while also establishing important limits on what can be determined from listing evidence alone.

The experiments showed that:

1. structured Signals can support candidate acquisition opportunities;
2. candidate explanations can be grounded in specific Signals and source evidence;
3. uncertainty can remain explicit rather than being converted into certainty;
4. some discovery patterns can be detected deterministically;
5. other patterns require semantic interpretation or external knowledge;
6. several useful opportunities depend on combinations or relationships among evidence that conventional item-oriented search does not naturally represent.

The experiments also showed that free-form AI discovery alone is not sufficiently reliable to serve as the sole discovery mechanism. A provisional hybrid direction is therefore supported:

```text
Listings and other sources
            ↓
      Evidence extraction
            ↓
          Signals
            ↓
   Evidence-pattern analysis
            ↓
Evidence-grounded interpretation
            ↓
   Candidate opportunities
            ↓
      Human evaluation
```

This remains a provisional direction rather than a production architecture. The experiments do not establish a permanent evidence-pattern taxonomy, generalized rule engine, ranking system, persistent relationship model, or image-analysis implementation.

### Phase 3 Completion Assessment

The Phase 3 completion criterion was:

> **Demonstrate whether structured source-grounded evidence can produce candidate acquisition opportunities that a human considers worth investigating, and can explain those opportunities through the underlying evidence.**

**This criterion has been met experimentally.**

The result does not establish that Hedstok will consistently discover opportunities that conventional search cannot find. Instead, it provides evidence for a narrower and more useful proposition:

> **Hedstok can structure and interpret evidence within listings to surface acquisition-relevant characteristics, combinations, and relationships that a human might otherwise have to discover and synthesize manually.**

Phase 3 therefore provides sufficient experimental evidence to continue beyond evidence extraction into evidence-based discovery.

## Phase 4 — Opportunity Interpretation

### Goal

Phase 4 investigates whether Hedstok can transform structured, source-grounded evidence into explainable candidate acquisition opportunities without overstating what the available evidence establishes.

Phase 3 demonstrated that Signals can support useful discovery patterns, and that some of those patterns can be detected deterministically. It also showed that free-form AI discovery alone can miss useful opportunities and introduce interpretations not established by the evidence.

Phase 4 therefore focuses on the transition between evidence analysis and candidate opportunities.

### Core Question

> **Can Hedstok transform structured evidence and detected evidence patterns into explainable candidate acquisition opportunities while preserving uncertainty and avoiding unsupported claims?**

### Experimental Scope

The experiment will use the existing Phase 3 extraction artifact and evidence-pattern results rather than collecting new listings or making new extraction calls.

The experiment will investigate:

- how Signals and evidence patterns contribute to candidate opportunities;
- whether multiple Signals or patterns can support a single opportunity;
- how candidate opportunities should reference their supporting evidence;
- whether useful opportunities can arise from Signals that do not match an existing evidence pattern;
- how uncertainty can be preserved in the resulting interpretation;
- how deterministic analysis and AI-assisted interpretation might contribute different capabilities;
- whether candidate explanations can remain grounded in the underlying Signals.

A candidate opportunity should represent something that appears potentially worth investigating because of the available evidence. It should not assert that the underlying claims are true, valuable, rare, authentic, or otherwise significant unless that conclusion is independently supported by the available evidence.

### Opportunity and Evidence Boundaries

The experiment will distinguish between evidence, evidence patterns, and candidate opportunities.

```text
Signals
   │
   ├───────────────┐
   │               │
   ▼               ▼
Evidence        Evidence
patterns        not yet patterned
   │               │
   └───────┬───────┘
           ▼
   Candidate opportunity
           │
           ▼
   Evidence-grounded
      explanation
```

An evidence pattern is an observed structure within the available evidence. A candidate opportunity is an interpretation that the evidence may warrant further investigation.

A pattern does not automatically constitute an opportunity, and an opportunity does not necessarily require a previously defined pattern.

This distinction is intentionally experimental. The Phase 4 work should determine whether these concepts provide a useful boundary or whether a different representation is needed.

### Evaluation

Candidate opportunities will be evaluated by human review using criteria including:

- **Usefulness** — does the candidate identify something reasonably worth investigating?
- **Evidence grounding** — can the candidate be explained through specific underlying Signals?
- **Uncertainty preservation** — does the explanation avoid converting uncertain or attributed claims into established facts?
- **Interpretation discipline** — does the candidate avoid introducing significance not established by the available evidence?
- **Coverage** — does the approach identify useful opportunities that deterministic evidence-pattern detection alone would miss?
- **Explanation quality** — does the supporting evidence make it clear why the candidate was surfaced?

False positives are useful experimental results. A candidate that appears interesting but does not withstand human review should help identify where the interpretation process overreaches.

### AI Role

Phase 3 did not support using free-form AI discovery as the sole discovery mechanism. Phase 4 will therefore treat AI-assisted interpretation as an experimental capability rather than an assumed architectural foundation.

AI may be used to propose or explain candidate opportunities, but any resulting interpretation must remain traceable to the available Signals.

The experiment will specifically examine whether AI can provide useful semantic interpretation after evidence has already been structured, without becoming a source of unsupported claims.

### Out of Scope

The following remain outside the Phase 4 experiment:

- marketplace scraping or live APIs;
- automated purchasing or seller contact;
- pricing or valuation;
- ranking or recommendation systems;
- notifications or monitoring;
- persistent database architecture;
- UI implementation;
- generalized graph or relationship architecture;
- image-analysis implementation;
- generalized AI orchestration;
- production discovery architecture.

### Completion Criterion

Phase 4 will be considered complete when the experiment establishes whether structured evidence and evidence-pattern analysis can be transformed into candidate acquisition opportunities that:

1. are considered useful enough to investigate by human review;
2. can be explained through specific underlying evidence;
3. preserve uncertainty and attribution;
4. avoid unsupported significance or factual claims; and
5. provide useful coverage beyond what the current deterministic evidence-pattern detectors identify alone.

Completion does not require establishing a permanent opportunity schema, production discovery architecture, ranking model, or AI orchestration framework.

The purpose of Phase 4 is to determine whether **opportunity interpretation** is a coherent and useful layer in the Hedstok pipeline, and what constraints that layer should have if development continues.

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

## Phase 4.3 — Representing the Reason to Look Closer

### Purpose

Phase 4.2 established that Hedstok is not simply looking for interesting stories, unusual specifications, or objectively desirable instruments. The relevant question is whether the available evidence gives a person a meaningful reason to stop and look closer.

This raises a further architectural question:

> **How, if at all, should this "reason to look closer" be represented and interpreted from the existing Signals?**

This phase explores that question without introducing a permanent production schema.

### Experimental Question

> **Can the reason an instrument is worth bringing to someone's attention be understood as an interpretation of existing evidence rather than as another type of evidence?**

### Observation

The existing evidence pipeline can be understood as:

```text
Source listing
     ↓
   Signals
     ↓
Evidence patterns / relationships
     ↓
  Interpretation
"What is interesting here?"
     ↓
Acquisition context
"Is this relevant to what we're looking for?"
     ↓
Surface observation
"Hey. Look at this one."
```

The important distinction is that the final observation is not itself source evidence.

A Signal represents something the source says. An evidence pattern or relationship represents a structured connection between pieces of evidence. A "reason to look closer" is an interpretation of that evidence in context.

For example, a listing may contain:

- a specific instrument identity;
- multigenerational ownership;
- a historical use claim;
- documentation or other supporting artifacts;
- an unresolved question about the instrument's history.

None of those Signals individually needs to state that the instrument is worth attention. The reason to look closer can emerge from their combination.

### Manual Interpretation Experiment

A small set of previously evaluated cases was used to separate three different questions:

1. **What evidence is present?**
2. **What is interesting about that evidence?**
3. **Does that combination justify "Hey. Look at this one."?**

The experiment showed that people naturally distinguish these layers.

For example, one case was described in terms of generational ownership, a potential recording-studio association, and an unresolved physical detail. The evidence itself remained distinct from the interpretation that those details formed an interesting story worth examining.

Another case contained an interesting story but no personal connection, no meaningful instrument identification, and no clear reason to pursue it. The story was interesting, but the final surface judgment was still "maybe" and then "no."

This reinforces the finding from Phase 4.2 that **interesting evidence and surface-worthy evidence are not identical concepts**.

### Findings

#### 1. The reason to look closer is not another Signal type

The experiment provides no reason to add a new Signal category for "interestingness" or "attention."

Signals should continue to represent source-grounded evidence. The reason to look closer is better understood as an interpretation derived from existing evidence.

This preserves the distinction between:

> **What the listing says**

and:

> **Why that evidence caught Hedstok's attention.**

#### 2. Evidence composition matters

A reason to look closer can emerge from the relationship between multiple Signals rather than from a single exceptional fact.

Generational ownership, dates, personal history, provenance claims, documentation, uncertain identity, and transaction context may each be modest individually while becoming meaningful when considered together.

This does not imply that Hedstok should automatically treat combinations of Signals as opportunities. The combination still requires interpretation.

#### 3. A single Signal can sometimes be sufficient

The experiment also demonstrated the opposite boundary.

A single, sufficiently specific historical claim can provide a reason to look closer. Multiple Signals are therefore not a requirement.

The relevant property is not the number of Signals, but whether the available evidence provides a meaningful reason for attention.

#### 4. Context affects whether an observation is surface-worthy

The same evidence can be interesting without necessarily being appropriate to surface.

An instrument may have a compelling family history while the listing explicitly states that it is not for sale. The story remains interesting, but the acquisition-oriented context changes whether it should produce the desired:

> **"Hey. Look at this one."**

This suggests that the interpretation cannot be derived from evidence alone. It must also account for the context in which Hedstok is being used.

#### 5. Uncertainty can be part of the reason

A reason to look closer does not require a claim to be established as true.

Uncertain provenance, unresolved identity, contradictory evidence, or a historical claim supported by partial documentation may itself create a meaningful question.

However, uncertainty alone is not sufficient. There must be some additional reason that the unresolved question is worth attention.

#### 6. A rigid taxonomy of reasons is not yet justified

Different people may describe the same evidence using different but compatible reasons for paying attention.

One person may emphasize the instrument's family history. Another may emphasize its connection to a local musician. Another may focus on the documentation or unresolved identity.

The experiment does not currently show that these interpretations need to be forced into a fixed vocabulary.

A useful representation should therefore preserve the explanation of **why the evidence caught attention** without prematurely deciding that every reason belongs to a predefined category.

### Provisional Architectural Finding

The current evidence supports treating the "reason to look closer" as a **derived interpretation of existing evidence in context**, rather than as another evidence type.

Conceptually:

```text
Evidence
   ↓
Interpretation
   ↓
Reason to look closer
   ↓
"Hey. Look at this one."
```

The interpretation should remain traceable to the Signals and evidence patterns that support it, while preserving uncertainty and relevant limitations.

This is a stronger candidate for future representation than adding additional Signal types. However, the experiment does not yet establish what that representation should be called, what fields it should contain, or whether it should become a persistent production object.

Terms such as "attention reason," "surface observation," "candidate," and "opportunity" should therefore remain provisional rather than being formalized at this stage.

### Completion Assessment

**This criterion has been met experimentally.**

The experiment demonstrated that:

- the reason to look closer can be distinguished from the underlying evidence;
- the reason can emerge from one Signal or a combination of Signals;
- evidence composition can create an interpretation not explicitly stated by the source;
- uncertainty can contribute to an attention-worthy interpretation without being resolved;
- acquisition context can affect whether an otherwise interesting instrument should be surfaced;
- different interpretations of the same evidence may be legitimate;
- a rigid taxonomy of attention reasons is not currently justified.

These findings support further investigation into a minimal representation of evidence-grounded surface observations.

They do **not** yet justify a permanent schema, scoring system, ranking mechanism, recommendation model, or new Signal type.

## Phase 4.4 — Surface-Worthiness as Emergent Interpretation

### Purpose

Phase 4.3 established that the "reason to look closer" is better understood as an interpretation of existing evidence rather than as another type of evidence.

Phase 4.4 tests whether that interpretation depends on a particular category of evidence, or whether different evidence configurations can independently or collectively create a reason to surface an instrument.

The experiment uses observations from Dan's existing instrument inventory together with controlled variations of otherwise ordinary instruments.

### Experimental Question

> **Does surface-worthiness emerge from a particular type of evidence, or can different evidence configurations create a meaningful reason to look closer?**

### Dan's Inventory as a Reference Point

Dan's existing inventory provides useful real-world context for understanding the kinds of characteristics, stories, and circumstances that appear to interest him.

Examples include:

- a homemade EVH Frankenstein associated with an artist Dan particularly likes;
- a Mark Tremonti signature model personally signed by Tremonti during a small exclusive event that Dan attended;
- an Epiphone Lucille signed by B.B. King and purchased from the local casino where it was signed;
- a headless eight-string Strandberg purchased from a local artist who needed the money;
- unusual surf-style guitars with distinctive appearances and configurations;
- a Gibson SG Bass with an unusual but recognizable body shape;
- a Mark Hoppus signature bass purchased from a local church;
- a customized Les Paul featured in _Hot Rod_ magazine and produced as a limited run of 150;
- visually distinctive rock and metal instruments;
- familiar instruments such as Strats, Teles, and Les Pauls that may become interesting through their appearance, history, model, or other characteristics.

These examples suggest that Dan's attention is not driven by a single property.

Potential sources of attention include:

- personal or ownership history;
- provenance or association with a person, organization, place, or event;
- unusual construction or configuration;
- distinctive physical appearance;
- recognizable artist or model associations;
- unusual acquisition circumstances;
- personal relevance or connection;
- limited or unusual production history;
- combinations of otherwise ordinary evidence.

Story remains an important source of attention, particularly when it provides provenance, human context, or a meaningful reason to investigate. However, the inventory examples demonstrate that a compelling story is not required in every case.

### Controlled Variation Experiment

A familiar instrument was progressively given additional characteristics to test whether surface-worthiness could emerge through accumulated evidence.

The baseline instrument was an ordinary Fender Stratocaster.

The tested variations included:

- ordinary instrument with no additional distinguishing information;
- unusual custom appearance;
- unusual appearance combined with a local musician association;
- unusual appearance, local musician association, and historical use;
- the same characteristics combined with explicit transaction context;
- a recognizable or particularly relevant model with otherwise ordinary presentation;
- an ordinary instrument accompanied by an unspecified personal story;
- an instrument matching a personal preference.

The results did not produce a single threshold.

An ordinary instrument did not warrant surfacing by default. Adding distinctive appearance produced a possible reason to look closer. Additional human or historical context strengthened that reason. Transaction context could strengthen a borderline observation further.

At the same time, a sufficiently distinctive model or identity could independently justify surfacing without requiring a narrative history.

Personal preference alone was not consistently sufficient.

### Findings

#### 1. Surface-worthiness is not tied to one evidence category

The experiments do not support defining surface-worthiness as:

- a story;
- provenance;
- unusual configuration;
- rarity;
- a particular model;
- personal preference;
- transaction context;
- or any other single category.

Different categories can independently contribute to attention.

#### 2. A single strong characteristic can be sufficient

Some instruments can provide a strong reason to look closer from a relatively small amount of evidence.

A distinctive model, unusual instrument type, recognizable artist association, or other specific characteristic may be sufficient without requiring several additional Signals.

The number of Signals is therefore not itself a useful measure of surface-worthiness.

#### 3. Multiple modest Signals can combine into a stronger observation

Other instruments become interesting through accumulation.

For example:

```text
unusual appearance
        +
specific person
        +
historical use
        +
transaction context
        ↓
stronger reason to look closer
```

The individual Signals do not necessarily become independently compelling. Their combination provides a more compelling explanation for why the instrument deserves attention.

#### 4. Story is important but not mandatory

Dan's inventory suggests that story is a major source of interest, especially when it provides:

- provenance;
- personal history;
- local connection;
- unusual acquisition circumstances;
- association with a musician or organization.

However, unusual physical design, configuration, model identity, or aesthetic characteristics can also produce a legitimate reason to look closer.

This means the project's existing emphasis on **story and story potential** should remain a central touchstone without becoming a complete definition of surface-worthiness.

#### 5. Ordinary instruments should not be automatically excluded

Common instruments such as Strats, Teles, and Les Pauls are not inherently uninteresting.

An otherwise familiar instrument may become surface-worthy because of:

- a distinctive finish or graphic;
- unusual history;
- provenance;
- a particular vintage or model;
- unusual configuration;
- personal relevance;
- or another characteristic that gives it a reason to stand out.

Conversely, familiarity alone does not justify surfacing an instrument.

#### 6. Personal preference is contextual rather than sufficient

Dan's preferences, such as smaller bodies or Teles, can contribute to whether an instrument is interesting to him.

However, a preference match alone does not necessarily create the desired "Hey. Look at this one" observation.

This suggests that personal preference may eventually be useful as context for interpretation rather than as a standalone discovery rule.

#### 7. Surface-worthiness is emergent

The combined experiments provide stronger evidence that surface-worthiness is an **emergent interpretation of available evidence in context**.

Different evidence configurations can produce the same outcome:

> **"Hey. Look at this one."**

There is therefore no current justification for assuming that Hedstok needs a single fixed trigger, threshold, or evidence category.

### Provisional Architectural Finding

The Phase 4 experiments now support the following working interpretation:

> **Hedstok should identify instruments whose available evidence, individually or in combination, gives a person a meaningful reason to stop and look closer.**

Stories and story potential are a major source of those reasons, but they are not the only source.

The relevant property is therefore not whether an instrument belongs to a predefined "interesting" category. It is whether the available evidence can support an understandable explanation for why this particular instrument deserves attention in context.

Conceptually:

```text
Source
  ↓
Signals
  ↓
Evidence patterns / relationships
  ↓
Evidence-grounded interpretation
  ↓
Context
  ↓
Surface observation
  ↓
"Hey. Look at this one."
```

This remains an interpretation rather than a recommendation or valuation.

The experiment does not justify a scoring threshold, ranking system, fixed taxonomy of attention triggers, or preference model.

### Completion Assessment

**This criterion has been met experimentally.**

The experiments demonstrated that:

- surface-worthiness is not tied to a single evidence category;
- a single strong characteristic can justify attention;
- multiple modest Signals can combine into a stronger reason to look closer;
- story is an important but non-mandatory source of attention;
- unusual characteristics can independently create interest;
- familiar instruments can become surface-worthy through additional evidence;
- personal preference can contribute without being sufficient by itself;
- no fixed threshold or single trigger has been justified.

These findings strengthen the Phase 4.3 conclusion that the "reason to look closer" should be treated as an evidence-grounded interpretation rather than another Signal type.

They also provide a more general working definition of surface-worthiness for subsequent experiments:

> **Surface-worthiness is the presence of a meaningful, explainable reason for human attention arising from the available evidence and relevant context.**

This definition remains provisional and should continue to be tested before being treated as a production requirement.

## Phase 4.5 — Interpretation Reproducibility

### Purpose

Phase 4.4 established that surface-worthiness can emerge from different evidence configurations rather than from a single evidence category or fixed trigger.

Phase 4.5 tests whether the same structured evidence can be interpreted consistently into a useful, evidence-grounded reason to look closer.

### Experimental Question

> **Given the same Signals, can Hedstok consistently produce a useful, evidence-grounded reason to look closer?**

The experiment uses eight controlled cases containing only existing Signals. Human interpretation was established independently before evaluating how the evidence could be represented computationally.

The experiment separates:

- the available evidence;
- the interpretation of that evidence;
- the uncertainty surrounding the interpretation;
- the resulting surface judgment.

### Interpretation Representation

The experiments suggest that a useful interpretation can be represented as:

```text
Signals
   ↓
Interpretation
   ├── observation
   ├── supporting Signals
   └── uncertainty
   ↓
Surface judgment
```

The **observation** describes what is notable about the particular instrument.

The **supporting Signals** identify the specific evidence that gives rise to that observation.

The **uncertainty** preserves unresolved questions, limitations, contradictions, or claims that are not established by the available evidence.

The **surface judgment** represents whether the available evidence gives a human a reason to look closer. It is an experimental judgment, not a score, recommendation, or valuation.

### Findings

#### 1. Signal presence is not interpretation

The presence of a Signal category does not by itself establish that an instrument is worth surfacing.

For example, an ordinary Stratocaster can contain identity, configuration, condition, seller, and market Signals without providing a meaningful reason to look closer.

Interpretation therefore requires more than detecting which types of Signals exist.

#### 2. Interpretation depends on relationships and combinations

Useful observations can arise from relationships between Signals rather than from individual Signals considered independently.

Examples include:

- a personal history combined with supporting physical evidence;
- an unusual configuration that independently distinguishes an instrument;
- provenance supported by markings or documentation;
- a timeline containing information that may warrant clarification;
- strong seller claims combined with an absence of supporting identification or provenance;
- an unresolved physical clue that creates a potentially interesting question.

This reinforces the Phase 4 finding that existing Signal and relationship concepts provide a useful evidence base for interpretation.

#### 3. Supporting evidence must be selective

An interpretation should identify the Signals that actually support the observation rather than treating every Signal in a listing as supporting evidence.

For example, an asking price may be relevant acquisition context without supporting a claim about an instrument's history.

This distinction improves explainability and preserves the separation between evidence and interpretation.

#### 4. Uncertainty is part of the interpretation

A useful interpretation does not need to resolve every question.

Uncertainty may itself be relevant when the available evidence creates a meaningful question, contradiction, or unresolved clue.

However, the interpretation must preserve the distinction between:

- what the source explicitly claims;
- what the available evidence supports;
- what remains unknown;
- and what the interpreter is suggesting is worth investigating.

The interpreter should not strengthen a source claim into an established fact.

#### 5. Surface judgment remains contextual

The experiments reinforce that an interesting observation does not always produce a surface-worthy candidate.

For example, a strong family history may be interesting while an explicit statement that the instrument is not for sale provides a reason not to surface it for acquisition attention.

Conversely, an instrument may warrant attention from a distinctive configuration without having a particularly compelling personal story.

Surface-worthiness therefore remains a contextual interpretation rather than a property of any individual Signal.

### Provisional Architectural Finding

The Phase 4 experiments support the following working pipeline:

```text
Source listing
     ↓
   Signals
     ↓
Evidence patterns / relationships
     ↓
Evidence-grounded interpretation
     ↓
Context
     ↓
Surface observation
     ↓
"Hey. Look at this one."
```

A useful interpretation can be represented experimentally as:

```text
Interpretation
├── observation
├── supporting Signals
└── uncertainty
```

with surface judgment remaining separate from the evidence and interpretation.

This representation is useful for experimentation, but it is **not yet established as a permanent production schema**.

The experiment does not justify:

- an interestingness score;
- a confidence score;
- a fixed taxonomy of attention triggers;
- a ranking system;
- a recommendation system;
- a valuation model;
- or a new permanent Signal type.

### AI Role

The Phase 4.5 results provide a narrower and more appropriate experimental role for AI than the free-form discovery approach tested during Phase 3.

Rather than asking AI to discover interesting instruments from unstructured listings, Hedstok can provide AI with already structured, source-grounded Signals and ask it to:

1. identify what is notable about the available evidence;
2. select the Signals supporting that interpretation;
3. preserve uncertainty and unresolved questions;
4. produce a concise explanation of why the evidence may justify a closer look.

This keeps evidence extraction and interpretation conceptually separate.

The AI remains an experimental interpreter of structured evidence rather than the sole source of discovery.

### Completion Assessment

**This criterion has been met experimentally.**

The experiments demonstrated that:

- the same evidence can be represented as an observation with supporting evidence and uncertainty;
- Signal presence alone is insufficient for useful interpretation;
- relationships and combinations between Signals are important;
- supporting evidence should be selected rather than indiscriminately repeated;
- uncertainty can be meaningful without being resolved;
- interestingness and surface-worthiness are not identical;
- surface judgment depends on context;
- the resulting representation can remain separate from the existing Signal model.

These findings provided sufficient conceptual basis to conduct a small AI interpretation experiment without changing the production Hedstok architecture.

That experiment was subsequently conducted using the same structured Signals and human interpretation targets documented above.

## Phase 4.5 AI Interpretation Experiment

The reproducibility experiment was extended with a small AI interpretation test using the same eight Signals-only cases used for the human interpretation targets.

The AI was asked to produce, for each case:

- an evidence-grounded observation;
- the Signals supporting that observation;
- relevant uncertainty;
- a contextual surface judgment of `yes`, `maybe`, or `no`.

The AI was explicitly constrained to the supplied Signals. It was not asked to verify claims, use outside knowledge, estimate value, assign a score, or make a purchasing recommendation.

### Experimental Result

The initial AI interpretation successfully produced the intended output structure for all eight cases.

It correctly handled several important boundaries:

- ordinary listings were not automatically surfaced;
- explicit unavailability was respected;
- unusual instrument configurations could provide a reason to look closer without requiring a story;
- physical documentation and provenance details could be recognized as meaningful evidence;
- unexplained physical evidence could contribute to a potentially interesting story.

However, comparison with the human interpretation targets exposed several limitations.

The AI sometimes:

- treated the presence of Signals as sufficient reason for an observation;
- selected more supporting Signals than were actually necessary;
- missed meaningful relationships or timelines between Signals;
- generated uncertainty that was technically relevant but not the uncertainty most important to the interpretation;
- treated strong seller claims combined with an apparent price discrepancy as an acquisition opportunity rather than recognizing the unsupported claim itself as the interesting evidence;
- produced conservative `maybe` judgments where the available evidence supported a stronger human `yes`.

### Findings

The experiment provides evidence that an AI model can transform structured Signals into a useful first-pass interpretation, but the interpretation is not yet reliably equivalent to human judgment.

The most important limitation is not basic extraction or formatting. It is **interpretive discipline**: determining which evidence matters, how multiple Signals relate to one another, what uncertainty is meaningful, and why a particular combination gives a person a reason to look closer.

This reinforces the distinction established earlier in Phase 4.5:

> **Signal presence is not interpretation.**

It also suggests a second distinction:

> **An interesting claim is not necessarily an interesting acquisition implication.**

For example, an unsupported claim that an instrument is extremely rare or highly valuable may itself be worth noticing because of the discrepancy between the claim and the available evidence. Hedstok should not convert that discrepancy into an unsupported conclusion about the instrument's value.

### Provisional AI Finding

The initial AI experiment supports using AI as an **interpretive component after evidence has been structured**, rather than as the sole source of discovery.

The AI appears capable of:

- identifying potentially notable evidence;
- combining multiple Signals into an observation;
- selecting supporting evidence;
- expressing uncertainty;
- producing a concise reason to look closer.

Further work is needed to determine how much of the observed inconsistency can be addressed through prompt design, Signal representation, or additional interpretation structure.

No scoring model, confidence model, ranking system, permanent interpretation schema, valuation system, or recommendation system is justified by this experiment alone.

The current result is therefore **promising but exploratory**. The experiment provides enough evidence to continue investigating AI-assisted interpretation, but not enough evidence to treat the current AI output as a reliable final surface-worthiness judgment.

## Phase 4.6 — Interpretation Discipline

### Purpose

Phase 4.5 demonstrated that an AI model can transform structured Signals into an initial interpretation containing an observation, supporting Signals, uncertainty, and a surface judgment.

The initial experiment also exposed specific limitations involving relationships between Signals, relevant uncertainty, and the distinction between noteworthy evidence and unsupported acquisition implications.

Phase 4.6 investigates whether targeted interpretive guidance can address these limitations without changing the underlying Signals, interpretation structure, or production architecture.

### Experimental Question

> **Can targeted guidance about relationships between Signals, relevant uncertainty, and evidence versus acquisition implications improve AI interpretation beyond the existing general instructions?**

### Experimental Design

The experiment will reuse the eight cases in `experiment-phase-4/interpretation-cases.json` and the human interpretation targets in `experiment-phase-4/interpretation-targets.json`.

The existing Phase 4.5 AI output provides the baseline.

A second interpretation run will use:

- the same eight input cases;
- the same model;
- the same output structure;
- the same general interpretive constraints;
- additional, targeted guidance addressing the observed failure patterns.

The existing baseline script and results will remain unchanged. The second run will produce a separate script and results artifact so the two outputs can be compared directly.

### Targeted Guidance

The additional guidance will investigate three areas.

#### 1. Relationships Between Signals

The interpreter should examine how Signals relate to one another before forming an observation.

Relevant relationships may include:

- timelines that appear unclear or potentially inconsistent;
- personal history supported by physical evidence;
- modifications considered alongside retained original components;
- provenance claims supported by markings or documentation;
- combinations of details that create a meaningful unresolved question.

The interpreter should identify a meaningful relationship when the supplied evidence supports one, without assuming that every apparent tension is a contradiction.

#### 2. Relevant Uncertainty

The interpreter should identify the unresolved question or limitation most relevant to its observation.

Uncertainty should not be included merely because some information is absent. It should explain what remains unknown about the observation or why a claim cannot be established from the available evidence.

The interpreter must preserve the distinction between an unresolved question and evidence that a claim is false.

#### 3. Evidence Versus Acquisition Implications

The interpreter should distinguish noteworthy evidence from conclusions about an instrument's desirability, value, or acquisition potential.

For example, strong seller claims about rarity or value without supporting identification or provenance may themselves provide a reason to look closer.

The interpreter must not convert those claims or an apparent discrepancy between claimed value and asking price into an unsupported conclusion that the instrument is a bargain or worth more than the asking price.

### Evaluation

The second output will be compared with both the Phase 4.5 baseline and the existing human interpretation targets.

Evaluation will consider:

- **Observation quality:** Does the interpretation identify what is actually notable?
- **Supporting evidence:** Does it select the Signals that directly support the observation?
- **Relationships:** Does it recognize meaningful connections, timelines, and tensions between Signals?
- **Uncertainty:** Does it preserve the most relevant unknowns without inventing contradictions?
- **Evidence discipline:** Does it avoid turning source claims into established facts or acquisition conclusions?
- **Surface judgment:** Does its contextual judgment align with the human target without sacrificing the quality of the explanation?

Agreement with the human surface judgment is one evaluation dimension, not the sole measure of success. Matching a label while producing a weak or unsupported explanation does not constitute a successful interpretation.

### Constraints

Phase 4.6 will not:

- change the input Signals or their representation;
- change the output schema;
- introduce scores, confidence values, rankings, or fixed attention thresholds;
- add new evidence categories or permanent interpretation fields;
- change production Hedstok code;
- introduce external market data or claim verification;
- treat human targets as instructions embedded in the AI input.

The comparison will use the existing eight cases in a single grouped request per run, preserving the same model and request structure as the baseline.

### Completion Criteria

Phase 4.6 will be considered complete when:

- the targeted-guidance experiment has been run against the same eight cases;
- the results have been compared with the Phase 4.5 baseline and human targets;
- improvements and regressions have been documented across the evaluation dimensions;
- the findings support a clear decision about whether prompt-level guidance is sufficient to justify further investigation or whether another part of the interpretation process needs examination.

The experiment does not assume that targeted guidance will improve the results. A lack of improvement, or improvement in some areas accompanied by regressions in others, is a valid finding.

No production architecture change is justified by the experiment alone.

### Phase 4.6 Results — Targeted Interpretation Guidance

**Status: EXPERIMENT RUN; RESULTS DOCUMENTED**

#### Experiment

The Phase 4.5 AI interpretation script was copied to `experiment-phase-4/interpret_with_ai_phase_4_6.py`. The Phase 4.6 script retained the same eight input cases, model, output schema, and general constraints while adding targeted guidance concerning:

- Relationships between Signals and preservation of unresolved ambiguity.
- Relevant uncertainty versus merely missing information.
- The distinction between noteworthy evidence and acquisition implications.
- Selection of supporting Signals that directly support the observation.

The Phase 4.5 script and results were preserved. Phase 4.6 wrote its results to `experiment-phase-4/interpretation-results-phase-4-6.json`. The human evaluation targets were not included in the AI input.

#### Surface-judgment comparison

| Case      | Human target | Phase 4.5 | Phase 4.6 | Result                    |
| --------- | ------------ | --------- | --------- | ------------------------- |
| interp-01 | yes          | maybe     | yes       | Improved agreement        |
| interp-02 | no           | no        | no        | Agreement retained        |
| interp-03 | no           | no        | no        | Agreement retained        |
| interp-04 | yes          | maybe     | maybe     | Conservative miss remains |
| interp-05 | yes          | maybe     | yes       | Improved agreement        |
| interp-06 | yes          | yes       | yes       | Agreement retained        |
| interp-07 | maybe        | yes       | maybe     | Improved agreement        |
| interp-08 | yes          | yes       | yes       | Agreement retained        |

Exact agreement with the human surface-judgment targets increased from **4/8 in Phase 4.5 to 6/8 in Phase 4.6**.

This is a descriptive result from one run over eight cases, not evidence of general reliability or a statistically established improvement.

#### Observations

**1. Targeted guidance improved several surface judgments.**

- `interp-01`: The family-history evidence now supports a `yes` judgment rather than a conservative `maybe`.
- `interp-05`: The studio name and inventory tag are treated as meaningful provenance evidence even though the identity of any particular player remains unknown.
- `interp-07`: Unsupported claims of rarity and value, combined with a substantial gap between claimed value and asking price, result in `maybe` rather than an unsupported positive conclusion.

The third case is particularly relevant to the experiment's distinction between noteworthy evidence and acquisition implications. A discrepancy may warrant scrutiny without establishing a bargain, actual value, or acquisition opportunity.

**2. Signal selection remains overinclusive.**

The model frequently includes most or all available Signals, including ordinary specifications, asking prices, and seller motivations that do not directly support the stated observation. The additional instruction to select only directly supporting Signals did not consistently produce selective evidence representation.

**3. Relational interpretation remains incomplete.**

In `interp-04`, the unusual custom headless eight-string configuration is recognized, but the surface judgment remains `maybe` despite the human target being `yes`. This suggests that the guidance did not consistently prevent uncertainty from suppressing an otherwise meaningful reason to look closer.

In `interp-06`, the observation identifies modifications and retained original parts but does not fully express the relationship between the modification timeline, the uncle's ownership, and the handwritten setup notes. The output also does not establish who performed the modifications.

**4. Uncertainty is not always relevant to the interpretation.**

In `interp-03`, uncertainty about whether the instrument is available for acquisition adds little because the seller explicitly states that they are keeping it. In `interp-08`, the unknown meaning of the handwritten control-cavity notes is identified, but the observation does not fully articulate why the combination of the notes and the bass's reported history is noteworthy.

These examples show that naming uncertainty is not the same as interpreting its relevance.

#### Conclusion

Phase 4.6 provides preliminary evidence that targeted interpretation guidance can improve surface judgments in some cases. Exact agreement increased from 4/8 to 6/8, with three judgments moving into agreement with the human targets and no previously correct surface judgments becoming incorrect.

However, the experiment did not consistently improve selective Signal attribution, relational interpretation, or the relevance of uncertainty. A correct surface label alone does not establish that the reasoning supporting it is sufficiently disciplined.

**Phase 4.6 is complete as an initial experiment.** Its results support retaining the distinction between evidence, interpretation, uncertainty, and acquisition implications as explicit evaluation criteria. They do not justify changing the production architecture, adding permanent schema fields, or treating the new instructions as validated.

Any follow-up experiment should isolate a specific remaining weakness rather than add broad guidance indiscriminately. No further prompt or production changes are made as part of this results record.

### Phase 4.7 — Evidence Selection Discipline

**Status: PLANNED**

#### Research question

Can targeted guidance improve the selection of supporting Signals so that the model identifies the evidence that directly supports its interpretation, omits incidental details, and preserves important evidence without simply repeating the listing?

#### Motivation

Phase 4.6 improved exact agreement with the human surface-judgment targets from 4/8 to 6/8. However, the model continued to include most or all available Signals in several cases, including details that did not directly support the stated observation.

The presence of a Signal does not establish its relevance to an interpretation. Hedstok must make its reasoning inspectable by distinguishing the evidence that supports an observation from details that are merely available.

This experiment isolates evidence selection rather than attempting to improve surface judgments, relational interpretation, and uncertainty handling simultaneously.

#### Experimental design

Use the same eight interpretation cases, model, output schema, and general constraints as Phase 4.6. Introduce targeted guidance focused on selecting supporting Signals.

Preserve the Phase 4.5 and Phase 4.6 scripts and results. Use a separate script and output file for Phase 4.7. Do not include human evaluation targets in the model input.

Do not change the input Signals, production architecture, scoring, surface-judgment categories, or permanent schema.

#### Evaluation criteria

Evaluate supporting evidence separately from surface-judgment agreement.

For each case, assess:

1. **Direct relevance:** Does each selected Signal directly support or qualify the stated observation?
2. **Omission:** Is any important supplied Signal missing from the supporting evidence?
3. **Selectivity:** Does the model exclude incidental details that add no meaningful support?
4. **Evidence sufficiency:** Can a reader understand the basis for the observation from the selected Signals without needing the entire listing repeated?
5. **Evidence fidelity:** Does the model preserve the supplied evidence without inventing facts, relationships, or stronger claims than the source supports?

A smaller supporting-Signal set is not inherently better. Evidence should be selected for relevance and sufficiency, not to satisfy an arbitrary count or length limit.

Surface-judgment agreement will be recorded as a secondary observation. It is not the primary success criterion for this experiment.

#### Constraints

- Do not change the input Signals or output schema.
- Do not impose an arbitrary maximum number of supporting Signals.
- Do not optimize for shorter outputs at the expense of important evidence.
- Do not introduce scores, rankings, thresholds, or permanent fields.
- Do not change the production architecture.
- Do not use external market data or independent verification.
- Do not include human evaluation targets in the model input.
- Do not assume that targeted guidance will improve results.

#### Completion criteria

Phase 4.7 is complete when the experiment has been run, the outputs have been evaluated against the criteria above, and the findings and limitations have been documented.

The conclusion should identify where evidence selection improved, where it did not, and whether any observed problems appear to depend on relational interpretation or uncertainty handling.

No production change is justified by this experiment alone.

## Phase 4.7 — Evidence Selection Discipline

**Status: EXPERIMENT COMPLETE — COMPARATIVE AUDIT PENDING**

### Research question

Can targeted guidance improve selection of supporting Signals so that the model identifies evidence that directly supports an interpretation, excludes incidental details, and preserves important evidence without repeating the listing?

### Experiment

The Phase 4.7 experiment used the same eight cases, model, input, response schema, and general interpretation guidance as Phase 4.6. The prompt added explicit guidance for selecting supporting Signals, including direct relevance, qualifying evidence, exclusion of incidental details, preservation of important evidence, original Signal wording, and no arbitrary limit on Signal count.

The experiment was run once using `gemini-3.5-flash-lite`. It produced eight interpretations in `experiment-phase-4/interpretation-results-phase-4-7.json`.

The first attempt failed with a temporary Gemini `503 UNAVAILABLE` response. A subsequent run succeeded without code or prompt changes.

### Results

Surface-judgment agreement with the human targets was **5/8**, compared with **6/8** in Phase 4.6 and **4/8** in Phase 4.5.

The initial review did not establish a consistent improvement in evidence selection. A direct comparison against Phase 4.6 and the original input Signals remains pending.

- **Direct relevance:** Mixed. Some interpretations selected evidence closely related to their observations, while others included descriptive details that did not materially support the interpretation.
- **Omission:** Potential weaknesses remain. In particular, the studio-origin Stratocaster interpretation retained relevant documentation but treated the provenance as relatively generic. A complete omission assessment requires comparison against the original Signals.
- **Selectivity:** Inconsistent. The ordinary Stratocaster interpretation included several descriptive Signals despite concluding that the listing offered no meaningful reason to look closer.
- **Evidence sufficiency:** Generally adequate. Most interpretations provided enough context to understand their stated observations, although sufficient evidence did not ensure that the observation itself was well founded.
- **Evidence fidelity:** The instruction to preserve original Signal wording did not reliably prevent paraphrasing or combining Signal text. Traceability remains an unresolved concern.

The custom headless eight-string guitar was a notable interpretation weakness: the model selected Signals describing its unusual configuration but still characterized the listing as ordinary and assigned `no`. This illustrates that evidence selection and interpretation quality are related but distinct problems.

### Findings and limitations

The added guidance did not demonstrate a reliable improvement over Phase 4.6. The experiment suggests that explicit selection instructions alone may not consistently distinguish relevant supporting evidence from incidental description or guarantee faithful reproduction of source Signals.

The lower surface-agreement result does not establish that the prompt change caused the decline. This was a single run of eight cases, and the results are too limited to support broad claims about model behavior.

Phase 4.7 does not justify a production change. The existing input, response schema, and interpretation pipeline remain unchanged.

### Next investigation

Compare Phase 4.6 and Phase 4.7 directly against the five evidence-selection criteria, using the original input Signals and both output files. Determine which differences reflect improved or degraded evidence selection, which reflect interpretation quality, and which remain uncertain.

Use that comparison to decide whether a more explicit evidence-selection method warrants a separate experiment. Do not assume that shorter Signal lists are inherently better, and do not introduce arbitrary Signal-count limits.

### Phase 4.7 Comparative Audit

**Status: EXPERIMENT COMPLETE — COMPARATIVE AUDIT COMPLETE**

#### Research question

Did targeted guidance improve the model's selection of supporting Signals compared with Phase 4.6, without sacrificing evidence sufficiency, fidelity, or the quality of its overall interpretation?

#### Comparison summary

Phase 4.6 selected 66 supporting Signals across the eight cases. Phase 4.7 selected 36, a reduction of approximately 45%.

This demonstrates increased selectivity in output, but the reduction alone does not establish better evidence selection. The comparative review considered direct relevance, omission, selectivity, evidence sufficiency, and evidence fidelity.

| Case                               | Comparative finding                                                                                                                                                                                                             |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 01 — Family provenance             | Phase 4.7 reduced the selection but omitted the mother's ownership and church-band history, losing central provenance context.                                                                                                  |
| 02 — Ordinary listing              | The selection was shorter, but still included incidental finish, neck, condition, and functionality details that did not directly support the observation.                                                                      |
| 03 — Inherited guitar not for sale | The selection retained the identity, family ownership, inheritance, and refusal to sell. Some historical context was omitted, but the core conclusion remained supported.                                                       |
| 04 — Unusual eight-string guitar   | Relevant configuration details were retained, yet the model still characterized the listing as ordinary and assigned a negative surface judgment. Selection alone did not correct the interpretation.                           |
| 05 — Recording-studio history      | The selection retained the studio connection, case inscription, inventory tag, and uncertainty about prior use. The judgment shifted from “yes” to “maybe”; this was more conservative, but not demonstrably more accurate.     |
| 06 — Modified Telecaster           | The modifications, retained original pickup, and handwritten setup notes formed a coherent evidence set. This was one of the stronger examples of selective support.                                                            |
| 07 — Rarity and value claims       | The selection retained the seller's claims, claimed value versus asking price, and absence of documentation. The judgment shifted from “maybe” to “yes”; the significance of this change remains uncertain.                     |
| 08 — Bass with unexplained notes   | The selection retained the identity, local playing history, worn finish, notes, and uncertainty about their authorship. Omitting the estate purchase, willingness to sell, and price was reasonable for the stated observation. |

#### Findings by evaluation criterion

**Direct relevance — Partial improvement.** Cases 03, 06, and 08 showed more focused selections. Case 02 still included incidental details. Case 04 demonstrated that selecting relevant Signals does not guarantee a sound interpretation of them.

**Omission — Unresolved weakness.** Case 01 lost central provenance context. Case 03 also omitted historical details, though these were less critical to its conclusion. A shorter selection can discard evidence that gives an observation its meaning.

**Selectivity — Improvement in several cases.** Cases 06 and 08 were particularly coherent. The overall reduction in selected Signals is encouraging, but selectivity must be evaluated alongside relevance and completeness.

**Evidence sufficiency — Generally maintained, with exceptions.** Most selections retained plausible support for their observations. Case 01 was materially incomplete, while Case 04 showed that a selection can contain relevant evidence without the resulting observation adequately accounting for it.

**Evidence fidelity — Unresolved.** The prompt instructed the model to preserve original Signal wording, but the output still paraphrased, combined, or abbreviated Signals. This weakens traceability between an interpretation and its source evidence.

#### Interpretation

Phase 4.7 produced more selective output, but the experiment did not establish an overall improvement in evidence selection quality.

A central limitation is that the model performs two related but distinct tasks in one response:

1. Interpret the listing's Signals and form an observation.
2. Select Signals that support that observation.

When the initial interpretation is weak, the selected evidence may still appear internally consistent while omitting context that would challenge or qualify the interpretation. Case 04 is the clearest example.

The current `supporting_signals` representation also stores Signal text as strings rather than stable references to source Signals. This allows paraphrasing and combining, making exact attribution harder to verify.

The surface-label agreement results were:

- Phase 4.5: 4/8
- Phase 4.6: 6/8
- Phase 4.7: 5/8

These results are descriptive, not proof that one prompt is superior. Each phase was evaluated on only eight cases, and a single run cannot establish that prompt changes caused the observed differences.

#### Conclusion

Phase 4.7 supports a limited finding: explicit evidence-selection guidance can reduce the number of selected Signals and produce more coherent selections in some cases, but it does not reliably prevent omissions, incidental details, or weak interpretations.

No production architecture change, scoring rule, threshold, or permanent data-model change is justified by this experiment alone.

#### Potential next investigation: Explicit evidence attribution

A separate, disposable experiment could test whether asking the model to reference supplied Signals by stable IDs improves traceability and makes omissions easier to audit.

The investigation should distinguish:

- Whether every selected reference points to an existing source Signal.
- Whether each selected Signal directly supports or materially qualifies the observation.
- Whether important supporting or contradictory context is omitted.
- Whether the observation itself is sound, independently of the quality of its supporting references.

This would test evidence attribution as a distinct problem rather than assuming that better attribution automatically improves interpretation. Define the experiment and success criteria before implementation. Preserve all existing Phase 4.5–4.7 artifacts; no production changes are proposed.

### Phase 4.8 — Explicit Evidence Attribution

**Status: EXPERIMENT DEFINED — NOT YET RUN**

#### Research question

Does requiring the model to reference source Signals by stable IDs improve the traceability and auditability of its evidence selection, while preserving evidence relevance, sufficiency, fidelity, and interpretation quality?

#### Motivation

Phase 4.7 reduced the number of selected supporting Signals from 66 to 36 across eight cases, but the comparative audit identified remaining weaknesses:

- Important contextual Signals were omitted in some cases.
- Some selected Signals were incidental to the observation.
- The model sometimes paraphrased, combined, or abbreviated Signal text despite instructions to preserve original wording.
- Better evidence selection did not consistently produce better interpretations.

The existing `supporting_signals` representation contains Signal text rather than stable references to the original Signals. This makes exact attribution difficult to verify and complicates the distinction between evidence-selection errors and interpretation errors.

Phase 4.8 will investigate explicit evidence attribution as a separate experimental variable.

#### Experimental approach

Create a disposable experiment based on Phase 4.7.

Use the same eight cases, source Signals, model, and general interpretation task. Require the model to reference supplied Signals using their stable IDs rather than reproducing their text as the primary means of attribution.

If the existing input Signals do not already have stable IDs, assign deterministic experiment-only IDs in a separate derived input or mapping. Preserve each Signal's original text and source association, and do not modify the Phase 4.7 input.

The experimental output should distinguish:

- **Observation:** the model's interpretation of the listing.
- **Supporting evidence:** IDs of Signals that directly support the observation.
- **Qualifying or contradictory evidence:** IDs of Signals that materially qualify, complicate, or challenge the observation.
- **Uncertainty:** unresolved questions that affect interpretation.

The response must not invent Signal IDs. Referenced IDs must correspond to Signals supplied in the input. Supporting and qualifying evidence should remain distinguishable rather than treating every relevant Signal as positive support.

The experiment may use a structured response schema and validation to test these requirements. Any schema or prompt changes must remain isolated from production code and existing experimental artifacts.

#### Evaluation criteria

Evaluate the results against the following criteria:

1. **Attribution validity:** Every referenced ID exists in the supplied input, and its original Signal can be retrieved without relying on generated text.
2. **Direct relevance:** Selected Signals materially support, qualify, or challenge the observation for the role assigned to them.
3. **Evidence sufficiency:** Important supporting, qualifying, or contradictory context is not omitted.
4. **Evidence fidelity:** The model's interpretation remains consistent with the source Signals and does not silently strengthen uncertain claims.
5. **Interpretation quality:** The observation adequately accounts for the evidence, including relevant uncertainty and conflicting context.

Attribution validity can be checked mechanically. The remaining criteria require comparative review against the original inputs and the Phase 4.7 output.

#### Comparison and controls

Compare Phase 4.8 with Phase 4.7 using the same eight cases and the criteria above.

Keep the original Phase 4.7 input, script, output, and comparative audit unchanged. Record the Phase 4.8 script, output, and findings as separate artifacts.

Do not provide human interpretation targets to the model. Use them only during evaluation.

A successful attribution check must not be treated as proof of relevance, completeness, or interpretation quality. Likewise, shorter evidence lists must not be assumed superior.

The small case set and single-run design limit the strength of any conclusions. Observed differences will be treated as exploratory findings rather than proof that stable IDs caused an improvement.

#### Scope constraints

- No production-code or production-schema changes.
- No new scoring system, confidence metric, threshold, or ranking mechanism.
- No external market research, fact verification, or valuation.
- No arbitrary limit on the number of referenced Signals.
- No changes to the existing Phase 4.5–4.7 artifacts.
- No assumption that explicit attribution will improve interpretation.

#### Decision after evaluation

Use the results to determine whether explicit attribution makes evidence selection materially easier to audit and whether it reveals meaningful omissions or interpretation errors.

If attribution improves traceability but not interpretation quality, record that distinction rather than expanding the approach into a broader redesign. Any subsequent experiment must be justified by the observed results.
