# Future Directions

## Purpose

This document captures possible future capabilities and areas of investigation identified during Hedstok's early development.

These ideas are intentionally exploratory. They are **not committed features, architectural requirements, or a product roadmap**.

Future phases should evaluate these possibilities against experimental findings rather than assuming that every idea should be implemented.

> **Future capabilities should be earned by evidence, not assumed in advance.**

## Data Acquisition

### Automated Listing Discovery

Investigate whether Hedstok should search marketplaces and other sources automatically rather than requiring listings to be supplied manually.

Potential capabilities include:

- automated marketplace search;
- web scraping or supported APIs;
- scheduled searches;
- configurable search criteria.

The appropriate acquisition approach should depend on what Hedstok ultimately needs to discover and what sources can be accessed reliably and appropriately.

### Wanted-Advertisement Discovery

Search wanted ads and similar buyer requests for people who may be looking for instruments or characteristics that Hedstok identifies.

This could eventually allow Hedstok to connect a potentially interesting instrument with a potential buyer or client.

## Evidence and Analysis

### Image Analysis

Investigate whether images can provide useful evidence that is absent, ambiguous, or contradictory in listing text.

Potential uses include:

- identifying visible instrument characteristics;
- detecting apparent contradictions between text and images;
- preserving visual evidence alongside textual evidence;
- identifying information that warrants further investigation.

### Cross-Source Duplicate Detection

Determine whether multiple listings represent the same physical instrument.

For example, the same guitar might appear on multiple marketplaces with different descriptions, prices, or photographs.

Cross-source identification could eventually allow Hedstok to combine evidence rather than treating each listing as an independent opportunity.

### Narrative Generation

Investigate whether Hedstok can construct a **possible narrative** from the evidence in a listing or collection of listings.

A generated narrative should remain explicitly grounded in the available evidence and should distinguish:

- what the source directly claims;
- what multiple pieces of evidence suggest;
- what remains uncertain;
- what should be investigated further.

A narrative should not silently turn speculation into fact.

### Investigation Questions

Explore whether Hedstok can identify the missing information that would be most useful when investigating an opportunity.

For example, a listing containing an unusual identification claim might lead to suggested questions about serial numbers, markings, provenance, or additional photographs.

This could eventually support human-led seller interactions without replacing human judgment.

### Analytics

Potential analytical capabilities include:

- identifying which sources produce the most useful leads;
- tracking useful leads over time;
- measuring discovery rates;
- identifying recurring characteristics among interesting opportunities;
- observing changes in listing activity;
- eventually investigating broader market activity or fluctuations.

Operational analytics and broader market intelligence should be treated as separate questions. Meaningful market analysis may require substantially more historical data than is currently available.

## Interaction and Delivery

### Reports and Summaries

Generate human-readable summaries of opportunities identified by Hedstok.

Possible formats include:

- investigation reports;
- daily or periodic digests;
- email summaries;
- text-message notifications.

The usefulness and appropriate format should depend on what the discovery process ultimately produces.

### Seller Communication Assistance

Investigate whether Hedstok can help prepare messages for contacting sellers.

A possible workflow would be:

```text
Opportunity identified
        ↓
Evidence reviewed
        ↓
Suggested questions generated
        ↓
Human reviews and approves
        ↓
Human contacts seller
        ↓
Human interaction continues
```

The goal would be to assist investigation rather than automatically conduct transactions or replace human judgment.

### User Interface

A dedicated interface may eventually be useful for:

- reviewing discovered opportunities;
- inspecting supporting evidence;
- comparing listings;
- tracking investigations;
- configuring search and discovery preferences;
- reviewing historical activity.

The form of the interface should be determined by the needs of the resulting workflow rather than designed in advance.

### Background Processing

Hedstok may eventually operate as a scheduled or continuously running service.

Possible workflows include:

- daily searches;
- periodic listing updates;
- price-change detection;
- new-opportunity notifications;
- background processing of newly discovered listings.

This should follow, rather than precede, establishing what information is worth processing and notifying about.

### Configurable Settings

Potential user-configurable controls include:

- search strictness;
- geographic distance;
- source selection;
- price ranges;
- price-change-only monitoring;
- notification preferences.

These controls should be based on demonstrated user needs rather than assumed requirements.

## Listing and Source Metadata

Future implementations may need to preserve additional information about each listing, including:

- source or marketplace;
- listing URL;
- seller information or contact information;
- publication or discovery time;
- price history;
- source-specific identifiers;
- associated images.

This information could support later capabilities such as duplicate detection, historical tracking, source analytics, and seller communication.

The exact data model should be established only when a demonstrated capability requires it.

## Personalization

Hedstok may eventually include small presentation details specific to its intended user.

One example is Dan's recurring phrase:

> **"It's a great day to be alive!"**

This is intentionally a presentation/personality consideration rather than a core intelligence requirement.

Personalization should not affect the evidence, analysis, or reasoning produced by the system.

## Testing

### Automated testing

Hedstok should eventually be able to test itself at multiple levels:

- Unit tests for deterministic code.
- Structural tests for things like valid Signal schemas and source-text grounding.
- Fixture-based extraction tests using known listings and expected evidence criteria.
- Pipeline/integration tests to make sure changes don't break the end-to-end workflow.

The Phase 2 structural evaluator and Experiment 0 fixtures provide the beginnings of this capability.

### Regression testing

This is especially valuable for Hedstok because the AI layer can change behavior without the Python code necessarily breaking.

Regression testing could compare new extraction or discovery behavior against previously evaluated fixtures and identify meaningful losses or changes in evidence coverage.

The exact regression strategy should be determined after the extraction and discovery behavior stabilizes enough to make such comparisons useful.

### Relationship to Future Phases

The ideas in this document should not be interpreted as a sequence of implementation phases.

A future phase may:

- investigate one of these ideas;
- combine several related ideas;
- determine that an idea is unnecessary;
- replace an idea with a better approach;
- or discover that a capability is not justified at all.

The purpose of this document is to preserve useful possibilities while keeping future development **evidence-driven and experimentally scoped**.
