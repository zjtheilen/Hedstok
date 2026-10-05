# Hedstok Concept

## 1. Problem

Used-instrument acquisition often depends on finding things that are not obvious from a conventional search.

Relevant information may be:

* incomplete;
* inconsistent;
* poorly structured;
* qualitative;
* distributed across different sources;
* buried in seller descriptions or personal leads;
* uncertain or contradictory.

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

* extracting structured information from natural-language listings;
* identifying claims and provenance;
* comparing descriptions;
* detecting potentially contradictory information;
* identifying information that warrants further investigation.

AI should not be treated as the final authority.

Deterministic analysis, source evidence, uncertainty, and human judgment remain part of the system.

## 6. Initial Experiment

The first experiment should remain deliberately small.

### Input

Approximately 10–20 guitar listings or acquisition leads containing realistic, imperfect information.

### Output

Hedstok should surface approximately 1–3 candidates it considers worth investigating.

For each candidate, Hedstok should provide:

* what caught its attention;
* the evidence supporting that observation;
* what remains uncertain;
* where the relevant information came from.

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

* autonomous purchasing or bidding;
* universal marketplace scraping;
* a general-purpose chatbot;
* an authoritative guitar valuation system;
* a full image-recognition system;
* a trained machine-learning model;
* a sophisticated entity-resolution platform;
* notifications or continuous monitoring;
* a complete marketplace;
* the eventual production architecture.

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

* **Multiple-listing input**

  * Establish a simple input format for processing a collection of listings rather than a single hard-coded listing.

* **Repeatable extraction**

  * Run the existing extraction capability across multiple listings and produce structured extraction artifacts.

* **Source preservation**

  * Maintain a direct connection between each extracted Signal and the source text from which it was derived.

* **Extraction evaluation**

  * Bring the useful evaluation principles from Experiment 0 into the working pipeline so extraction quality can be measured rather than assumed.

* **Uncertainty preservation**

  * Preserve the distinction between what a listing claims and what is actually established.
  * The extraction process must not silently convert uncertain or attributed claims into facts.

### Out of Scope

Phase 2 does not currently include:

* Evidence Relationship implementation
* entity resolution or persistent entity modeling
* database implementation
* web UI
* recommendation or ranking systems
* marketplace integrations or automated web scraping
* pricing intelligence
* authentication or deployment infrastructure
* generalized AI orchestration
* graph architecture

These capabilities may become appropriate in later phases, but Phase 2 should not assume that they are required.

### Phase 2 Completion Criterion

Phase 2 is complete when Hedstok can repeatedly process a collection of listings and produce structured, source-grounded evidence with enough evaluation support to determine whether the extraction capability is reliable and useful enough to justify further development.

> **Phase 2 is intended to establish whether the core evidence pipeline works well enough to earn the next capability.**
