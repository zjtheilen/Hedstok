# Hedstok — Phase 3: Discovery Experiments

## Purpose

Phase 3 investigated how Hedstok could identify potentially interesting acquisition leads from structured evidence extracted from messy listing descriptions.

The central question was:

> Can Hedstok discover reasons to investigate a listing that would not necessarily be apparent from conventional keyword or attribute search?

The goal was not to establish that an instrument was valuable, authentic, rare, or a good purchase. The goal was to identify evidence and relationships that might justify closer human attention.

This document records experimental findings and their limitations. It does not define a complete production discovery architecture.

## Starting Point: Experiment 0

Experiment 0 used a small synthetic dataset of 14 guitar listings and acquisition leads.

The examples deliberately varied across ordinary listings, unusual configurations, provenance claims, personal histories, incomplete descriptions, uncertain identification, conflicting information, and cases that should not warrant attention.

The original listing descriptions were the source material. Evaluation expectations were maintained separately so they would not dictate the discovery process.

The experiment was intended to test the underlying concept before committing to a larger product architecture.

## Phase 3.1 — AI-Assisted Signal Extraction

### Research question

Could an AI model transform unstructured listing descriptions into structured, source-grounded observations suitable for later discovery analysis?

### Inputs

The experiment used the existing Experiment 0 materials:

- `experiment-0/input/listings.json` — the 14 original listing descriptions.
- `extraction2.json` — the batch extraction results.
- `experiment-0/evaluation/expected-signals.json` — separate evaluation context.

Phase 3.1 reused the existing listings and extraction output. It did not introduce new listings or make additional extraction calls.

### Intended extraction boundary

The extraction stage was expected to produce structured observations containing:

- A Signal type
- A concise claim
- The source text supporting the claim

The prompt required claims to remain grounded in the listing. Fact-checking, valuation, unsupported inference, and interpretation were outside the extraction task.

This distinction mattered because an extracted Signal should represent what the source says, not what Hedstok thinks the source might mean.

### Findings

The batch extraction demonstrated that Gemini could convert unstructured listing descriptions into structured observations across all 14 listings in a single request.

The resulting observations were generally source-grounded and preserved important distinctions, including:

- Uncertain instrument identification
- Seller-reported provenance
- Ownership and personal history
- Seller context
- Image-derived observations
- Potentially conflicting information

However, the extraction was not complete or perfectly consistent.

It did not reproduce every Signal represented in the separate evaluation dataset, and some Signal categories were broad or inconsistent.

Early prompt behavior also showed that unconstrained extraction could introduce interpretation beyond the source, including attempts to fact-check claims or characterize claims as unsupported. The extraction boundary was tightened to keep verification and interpretation outside this stage.

### Phase 3.1 conclusion

The experiment supported using AI to establish a structured observation layer, but it did not establish that AI extraction was complete, universally reliable, or ready for production without validation.

The results did not justify expanding the extraction schema simply to accommodate every expected Signal. The purpose of extraction was to preserve evidence faithfully, not to encode discovery logic.

The resulting architectural principle was:

> **AI extracts. Software reasons. Human evaluates.**

## Deterministic Discovery

### Research question

Could software identify potentially interesting relationships among the extracted observations without asking the AI model to act as an opaque judge of what was interesting?

The discovery layer operated on the frozen extraction baseline. It evaluated the presence and relationships of extracted observations rather than determining whether individual seller claims were true.

### First Discovery Experiment

The first discovery experiment was run against the Phase 2 batch extraction artifact without additional extraction calls.

The discovery process surfaced five candidate acquisition opportunities:

- listing-01
- listing-05
- listing-06
- listing-08
- listing-11

Human review judged all five surfaced candidates worth investigating. This demonstrated that structured Signals could support discovery of acquisition opportunities that a human considered worth further investigation.

A separate human review of all 14 listings identified 11 listings as worth investigating, one as potentially worth investigating, and two as not worth investigating. The first discovery run therefore did not demonstrate complete discovery coverage.

Several clear discovery misses were identified. Listings 02, 04, 09, and 14 contained evidence that the human reviewer considered worth investigating but were not surfaced by the discovery process. The relevant evidence was already present in the structured Signals, so these cases represented discovery interpretation misses rather than extraction failures.

The misses revealed several distinct discovery requirements:

- Useful opportunities may emerge from combinations of otherwise ordinary Signals.
- Unusual configuration or identification evidence may itself warrant investigation.
- Seller or inventory context may represent an acquisition opportunity independently of an individual instrument.
- Some human discoveries depend on external knowledge that is intentionally unavailable under the current source-grounded discovery rules.

Listings 07 and 12 illustrate the latter boundary. Their human-interest judgments included knowledge not established by the supplied Signals, such as knowledge about a brand's status or the market desirability of an instrument. These cases should not be treated as failures of source-grounded discovery under the current rules.

Listing 13 was treated as a weak or ambiguous opportunity during human review and did not provide strong evidence of a discovery capability failure.

Listing 11 was identified because the textual identification and image-description Signals conflicted. This supported further investigation of multi-Signal discovery without establishing a general relationship or graph architecture.

These findings were provisional. They did not establish a production discovery taxonomy, ranking system, external-knowledge architecture, or persistent relationship model.

### Second Discovery Experiment

The second discovery experiment used the same structured evidence input, model, and execution process as the first experiment. Only the discovery prompt was revised to more explicitly address combinations of Signals, unusual configurations, seller or inventory context, and external-knowledge boundaries.

The revised discovery process surfaced seven candidate acquisition opportunities:

- listing-01
- listing-02
- listing-05
- listing-06
- listing-08
- listing-09
- listing-11

Human review judged all seven surfaced candidates worth investigating. Compared with the first experiment, the revised prompt recovered listings 02 and 09, both previously identified as clear discovery misses. This indicated that prompt guidance about Signal combinations and seller or inventory context could improve discovery coverage without introducing false positives among the surfaced candidates.

Listings 04 and 14 remained unsurfaced despite containing source-grounded evidence that the human reviewer considered worth investigating. Both were within the revised prompt's stated discovery scope. This provided evidence that prompt expansion alone did not reliably produce complete discovery coverage.

The second experiment also showed continued interpretation drift beyond the supplied evidence. Some explanations introduced significance not established by the Signals, including descriptions such as "vintage," "period-appropriate," and "high-end." Source-grounded extraction therefore did not, by itself, guarantee source-grounded discovery interpretation.

The first two experiments indicated two distinct challenges:

- Useful opportunities could remain undiscovered even when supporting Signals were present and the prompt explicitly identified the relevant discovery pattern.
- Discovered opportunities could acquire unsupported significance during interpretation.

Together, these experiments provided evidence that structured Signals could support useful acquisition discovery and that prompt guidance could improve coverage. They did not establish that free-form AI discovery was sufficiently reliable for production.

### Third Discovery Experiment — Provisional Evidence Patterns

The third discovery experiment analyzed the human evaluation results from the first two discovery experiments to determine whether the human "investigate" decisions could be explained by recurring patterns in the existing Signals.

The analysis introduced no new extraction calls or evidence. Instead, the existing structured evidence was reviewed against the 11 listings that the human reviewer considered worth investigating.

Several provisional evidence patterns emerged:

- **Converging Identity Clues:** An uncertain identity is accompanied by multiple additional Signals containing clues that may help narrow or investigate that identity.
- **Dated Configuration/Modification History:** A dated instrument has configuration, modification, retained-original-component, and/or condition evidence that together provide a potentially investigable picture of its history.
- **Instrument + Transaction Context:** Instrument-specific evidence is accompanied by explicit transaction or trade context that may create an acquisition path.
- **Provenance:** Evidence explicitly associates an instrument with a specific person, ownership history, recording, performance, or other identifiable historical context.
- **Seller/Inventory Opportunity:** Seller-context evidence indicates a meaningful collection or inventory combined with explicit willingness to sell, trade, make deals, or establish an ongoing acquisition relationship.
- **Cross-Source Contradiction:** Signals from different evidence sources make materially inconsistent claims about the same subject.
- **Explicitly Unusual Configuration:** A Signal directly describes an unusual or nonstandard configuration or combination of characteristics.
- **Dated Instrument + Originality/Period Evidence:** A dated instrument has evidence of original or period-appropriate components or accessories, optionally accompanied by explicit market context such as price.

These patterns were provisional observations from the current evaluation set, not a proposed production taxonomy.

The patterns differed in how readily they could be detected deterministically. Named provenance and seller/inventory opportunity appeared to have relatively direct structural conditions. Other patterns required interpretation to determine whether evidence was meaningful. For example, converging identity clues require determining whether multiple clues converge on a useful investigative possibility; cross-source contradiction requires distinguishing semantic incompatibility from mere difference.

Dated configuration and modification history illustrated a separate limitation: its structural components could be detected, but the broad combination could produce false positives. Detecting a pattern and determining whether a particular instance was useful for acquisition discovery were separate questions.

Dated instrument and originality/period evidence also exposed the external-knowledge boundary. Signals could preserve a date, model, original components, period-appropriate accessories, and price without independently establishing rarity, desirability, quality, or unusual market value. Listings 07 and 12 illustrated this boundary. They should not be treated as failures of the source-grounded evidence layer simply because their potential significance depended partly on external knowledge.

Not every human investigation decision needed to be represented by a discovery pattern. Listing 13 remained ambiguous or weak, while listings 03 and 10 served as negative examples that did not meaningfully trigger the identified patterns.

The resulting architectural observation was that discovery might be better approached through evidence-pattern detection combined with evidence-grounded interpretation, rather than unconstrained AI discovery alone.

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

Under this model, deterministic analysis could identify evidence structures reliable enough to detect mechanically, while interpretation could determine what those structures might mean and explain why they might warrant investigation. Free-form AI discovery could remain useful as a secondary exploratory mechanism for identifying patterns not yet recognized by deterministic detection.

The third experiment provided preliminary evidence for a hybrid approach. It did not establish a production architecture, permanent evidence-pattern taxonomy, deterministic rule engine, external-knowledge system, or persistent relationship model.

Further experimentation needed to determine whether the provisional patterns could be expressed precisely enough for useful deterministic detection, how often detectors produced false positives, and where interpretation or external knowledge was genuinely required.

### Fourth Discovery Experiment — Deterministic Detection

The fourth discovery experiment tested whether provisional evidence patterns could be expressed as deterministic detection conditions.

The experiment initially focused on three patterns:

- **Named Provenance**
- **Seller/Inventory Opportunity**
- **Dated Configuration/Modification History**

The patterns were tested against representative positive, negative, and borderline examples. Where a pattern appeared structurally detectable, a small deterministic detector was implemented and evaluated against the existing extraction artifact. The purpose was to determine which parts of discovery could be detected from observable evidence structures and which parts required interpretation.

**Provenance** showed that deterministic detection was possible to a limited degree. Provenance could appear across different Signal types rather than being limited to `story` Signals. Ownership or recording history might appear as `story` evidence, while physical evidence attributed to a specific person might appear as `condition` evidence. Ordinary ownership history was generally insufficient; associations involving identifiable people, activities, performances, recordings, or other specific historical context were more likely to warrant investigation. Determining whether a provenance association was sufficiently meaningful still required interpretation.

**Seller/Inventory Opportunity** showed the strongest case for deterministic detection. The relevant structure combined evidence of multiple instruments, a meaningful collection or inventory, or ongoing acquisition activity with explicit willingness to transact. Transaction activity could include selling, trading, buying, or establishing an ongoing acquisition relationship. A single instrument being offered for sale did not by itself constitute this pattern. Much of the structure appeared mechanically detectable, although borderline cases still required interpretation.

**Dated Configuration/Modification History** showed that its structural components could also be detected mechanically, but determining whether a particular instance warranted investigation depended more heavily on interpretation. Dated instruments combined with configuration, modification, originality, retained-original-component, or condition evidence produced a range of human judgments. Originality and modification history were particularly useful when they provided evidence about the instrument's configuration or history. The likelihood that a pattern warranted investigation varied with the age and combination of the evidence.

The experiment also examined two additional patterns.

**Cross-Source Contradiction** was demonstrated using listing 11. One Signal identified the instrument as a 1958 Les Paul, while another described the image as a kid-size Stratocaster-style guitar. A deterministic detector identified the contradiction and returned the two supporting Signals. It produced no additional matches across the current 14-listing extraction artifact. This demonstrated that explicit contradictory evidence could be surfaced without deciding which claim was correct; it did not establish a general semantic contradiction detector.

**Explicitly Unusual Configuration** was demonstrated using listing 14, where a Signal described the instrument as "Tele and Strat in one guitar." A deterministic detector identified the Signal and returned it as supporting evidence. It produced no additional matches across the current 14-listing artifact, and synthetic negative cases did not trigger on ordinary configuration or modification evidence. This demonstrated detection when the source explicitly characterized the configuration, not a general ability to determine independently whether a configuration was unusual.

The results reinforced the distinction between evidence-pattern detection and discovery interpretation. Deterministic detection could identify evidence structures without deciding that they represented worthwhile acquisition opportunities.

| Pattern                                  | Deterministic detection           | Interpretation required |
| ---------------------------------------- | --------------------------------- | ----------------------- |
| Provenance                               | Partial                           | Significant             |
| Seller/Inventory Opportunity             | Strong                            | Limited                 |
| Dated Configuration/Modification History | Strong                            | Significant             |
| Cross-Source Contradiction               | Demonstrated for an explicit case | Significant             |
| Explicitly Unusual Configuration         | Demonstrated for an explicit case | Context-dependent       |

These results provided preliminary evidence that discovery might benefit from a hybrid approach: deterministic analysis to identify evidence structures, followed by interpretation to evaluate their potential significance.

The detectors remained experimental implementations, not a permanent evidence-pattern schema or generalized rule engine. The results did not establish that every useful discovery pattern could or should be detected deterministically.

### Relationship types surfaced

The initial deterministic discovery layer surfaced several kinds of relationships:

- Ownership history combined with uncertain identification
- Ownership history combined with recording-history claims
- Multiple modification or specialized-configuration Signals
- Conflicting instrument identification and image-based observations

These examples suggested that potentially interesting cases could emerge from combinations of observations rather than from a single keyword or isolated attribute.

The distinction was important: a detail may be unremarkable on its own but become relevant when considered alongside another detail.

### Adversarial testing and false positives

Initial adversarial testing exposed a false-positive path in the modification rule.

The rule initially treated unrelated uses of words such as “pickup” and “setup” as evidence of modification. Those words can appear in ordinary descriptions without indicating a meaningful modification history.

The rule was tightened to require stronger modification-oriented language.

The revised behavior passed six targeted tests covering positive cases and plausible false positives.

This was a focused test result, not evidence that the discovery system was free of false positives generally.

### Discovery conclusion

The experiment established a useful design boundary:

> **Discovery rules must identify relationships between observations, not merely the presence of interesting-sounding words.**

The rules remained intentionally narrow and experiment-specific. Further generalization should be driven by observed failures rather than by trying to anticipate a complete taxonomy of discovery opportunities.

## Final Discovery Comparison

The final Phase 3.1 experiment compared the human investigation decisions against whether the underlying discovery was naturally represented by conventional item-oriented search.

This was a qualitative comparison, not a benchmark of any particular search engine or marketplace. It examined whether useful opportunities depended on relationships, combinations, contradictions, uncertainty, provenance, seller context, or other evidence structures that ordinary keyword or attribute-based searching would not necessarily represent directly.

The comparison used the 11 listings that the human reviewer classified as definite investigation candidates.

**Listing 07 — Conventional search and external knowledge**

The listing described a 3/4-size KAY acoustic guitar. The reason for considering it interesting depended substantially on external knowledge about the brand and instrument. The available Signals did not contain an unusual relationship, contradiction, or combination establishing why the instrument was worth investigating. This illustrates a case where Hedstok can preserve useful information while discovery significance depends on knowledge beyond the source evidence.

**Listing 02 — Dated configuration and modification history**

This listing combined a dated instrument with modification history, retained original components, configuration evidence, and condition evidence. Individual facts could appear in conventional search, but the potentially investigable combination was not naturally represented as a single search criterion.

**Listing 05 — Combined provenance**

Multiple provenance-bearing Signals connected the instrument to a specific owner, session-player history, recordings, and an attributed physical characteristic. Individual claims might be searchable if a user already knew which connection to seek, but the combined provenance structure was not naturally represented by ordinary item search.

**Listing 06 — Uncertain identity**

The listing contained uncertain identity alongside additional clues about configuration, history, and transaction context. The uncertainty itself contributed to the reason for investigation. Conventional search generally benefits from a known identity, whereas this discovery depended partly on an unresolved identity.

**Listing 08 — Converging identity clues**

This listing also contained uncertain identity with additional clues that could help narrow it, including configuration, associated equipment, ownership history, and transaction context. The potential discovery depended on the combination rather than a single obvious search attribute.

**Listing 09 — Seller and inventory opportunity**

The opportunity was primarily associated with the seller's collection, inventory, and willingness to establish an ongoing acquisition relationship, rather than a unique characteristic of the individual instrument. Conventional search might surface the listing, but it would not naturally represent the seller as an acquisition opportunity.

**Listing 11 — Cross-source contradiction**

The listing contained a contradiction between an identity claim and an image-derived description. Such a contradiction is unlikely to be represented by conventional search because a user would generally need to know that the conflicting evidence exists before searching for it.

**Listing 14 — Explicitly unusual configuration**

The source described the instrument as "Tele and Strat in one guitar." Conventional product-oriented search could locate the instrument, but the unusual configuration provided an additional discovery characteristic a user might not know to search for in advance.

**Listings 01, 04, and 12 — Intermediate cases**

These listings contained potentially useful combinations of evidence whose significance depended more heavily on interpretation or external knowledge.

- Listing 01 combined uncertain identity, multigenerational ownership, and personal significance.
- Listing 04 combined instrument evidence with explicit trade circumstances.
- Listing 12 combined age, model identity, originality or period evidence, accessories, and explicit price.

These cases demonstrate that evidence-based discovery and conventional search are not mutually exclusive. A listing may be readily searchable while still containing a combination of evidence that becomes useful only after structured analysis.

The comparison did not demonstrate that Hedstok would consistently find instruments conventional search could not find. It supported a narrower conclusion: several useful acquisition opportunities depended on relationships or combinations among pieces of evidence that conventional item-oriented search does not naturally represent.

Hedstok's potential value was therefore not necessarily replacing search or retrieving otherwise inaccessible listings. It could instead transform information in retrieved listings into structured evidence and surface characteristics that a human would otherwise have to notice and synthesize manually.

## Image-Derived Evidence

Listing 11 established an important boundary for the evidence pipeline.

The contradiction identified during the experiment depended on a Signal derived from an associated image. In the experimental artifact, that image-derived observation already existed as structured evidence, allowing discovery to compare it with the textual identity claim.

A real Hedstok workflow cannot assume that a human will manually inspect every associated image and supply those observations. If image-derived evidence is important to discovery, the upstream evidence pipeline will eventually need to support image analysis as another source of Signals.

This does not require a separate image-specific discovery architecture. The experiment suggests a simpler boundary:

```text
Listing text ──────┐
                   │
Listing images ────┼──> Evidence extraction
                   │             ↓
Other sources ─────┘           Signals
                                  ↓
                      Evidence-based discovery
```

The discovery layer can operate on the resulting Signals without needing to know whether a Signal originated from text, an image, or another supported source.

Image analysis was therefore identified as a future evidence-generation capability, not a requirement for completing the current Phase 3 discovery experiment.

## Evaluation Principles

The discovery experiment established several useful evaluation dimensions.

### Discovery quality

Did the system surface candidates that were genuinely worth investigating?

### Relevance

Were the surfaced candidates interesting for reasons supported by the available information?

### Evidence grounding

Could each important observation be traced to source material?

### Uncertainty preservation

Did the system distinguish source claims from verified facts and preserve unresolved ambiguity?

### False positives

Did the system surface ordinary or weak cases merely because they contained interesting-sounding words?

### False negatives

Did it overlook cases containing meaningful evidence or relationships?

### Explanation quality

Did the explanation establish why the listing was surfaced rather than merely restating the description?

### Hallucination

Did the system introduce information that was absent from the source?

These criteria remain useful for evaluating subsequent discovery and interpretation experiments.

## Architectural Implications

The Phase 3 findings support a separation of responsibilities:

1. **Source material** provides the original listing information.
2. **AI extraction** produces structured observations grounded in the source.
3. **Deterministic discovery** identifies candidate relationships among observations.
4. **Interpretation** explains why a candidate may warrant closer attention.
5. **Human evaluation** determines whether the explanation is useful and whether further investigation is justified.

This is a conceptual separation of responsibilities. It does not require every stage to become a separate service or establish a final production schema.

In particular, the findings do not justify moving discovery judgments into the extraction prompt. Doing so would make it harder to distinguish source-grounded observations from interpretive conclusions and harder to test discovery behavior independently.

## Limitations

The experiments were small and used a synthetic dataset of 14 listings.

The results therefore do not establish:

- General discovery accuracy across real marketplaces
- Completeness of Signal extraction
- Reliability across different listing formats or instruments
- Generalization beyond the tested discovery rules
- The absence of false positives or false negatives
- Production readiness

The six targeted tests validate a narrow rule change; they do not constitute comprehensive discovery evaluation.

The findings should be treated as evidence for architectural direction, not as proof of overall system performance.

## Phase 3 Final Findings and Completion Assessment

Phase 3 demonstrated that structured, source-grounded evidence can support useful acquisition discovery, while also establishing important limits on what can be determined from listing evidence alone.

The experiments showed that:

1. Structured Signals can support candidate acquisition opportunities.
2. Candidate explanations can be grounded in specific Signals and source evidence.
3. Uncertainty can remain explicit rather than being converted into certainty.
4. Some discovery patterns can be detected deterministically.
5. Other patterns require semantic interpretation or external knowledge.
6. Some useful opportunities depend on combinations or relationships among evidence that conventional item-oriented search does not naturally represent.

The experiments also showed that free-form AI discovery alone is not sufficiently reliable to serve as the sole discovery mechanism. The results support a **provisional hybrid direction** in which evidence-pattern analysis and evidence-grounded interpretation operate on structured Signals.

This remains a provisional direction rather than a production architecture. The experiments do not establish a permanent evidence-pattern taxonomy, generalized rule engine, ranking system, persistent relationship model, or image-analysis implementation.

### Completion Assessment

The Phase 3 completion criterion was:

> **Demonstrate whether structured source-grounded evidence can produce candidate acquisition opportunities that a human considers worth investigating, and can explain those opportunities through the underlying evidence.**

**This criterion has been met experimentally.**

The result does not establish that Hedstok will consistently discover opportunities that conventional search cannot find. Instead, it provides evidence for a narrower and more useful proposition:

> **Hedstok can structure and interpret evidence within listings to surface acquisition-relevant characteristics, combinations, and relationships that a human might otherwise have to discover and synthesize manually.**

Phase 3 therefore provides sufficient experimental evidence to continue beyond evidence extraction into evidence-based discovery. Phase 4 investigates the next question: how to interpret evidence in context and explain why a listing deserves human attention.

## Resulting Design Position

Phase 3 supported proceeding from structured evidence to deterministic discovery analysis.

The key lessons were:

- Preserve source-grounded observations.
- Keep extraction separate from interpretation.
- Evaluate relationships among observations rather than isolated keywords.
- Use adversarial tests to expose plausible false-positive paths.
- Refine the system in response to observed failures.
- Avoid expanding schemas or rules without a demonstrated need.

The next research question was no longer simply whether evidence could be extracted or related. It was how to interpret evidence in context and explain why a listing deserved human attention.

That investigation is documented in `docs/phase-4-interpretation.md`.
