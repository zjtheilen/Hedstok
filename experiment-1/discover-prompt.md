# Phase 3.1 — Discovery Experiment

## Purpose

Determine whether structured Signals can be used to identify candidate acquisition opportunities worth investigating.

## Input

The Phase 2 batch extraction artifact:

`extraction2.json`

## Prompt

```text
Review the structured evidence extracted from used-instrument listings below.

Your task is to identify candidate acquisition opportunities supported by the available evidence.

A candidate opportunity is something that appears potentially worth investigating because of the evidence present in one or more Signals.

Look for things such as:

- unusual provenance or personal history;
- contradictions or inconsistencies;
- uncertain or potentially incorrect identification;
- unusual instrument configurations;
- meaningful combinations of otherwise ordinary Signals;
- unusual stories or circumstances;
- evidence suggesting that additional investigation could reveal something important.

These are examples, not an exhaustive definition. Do not assume that every unusual detail is an opportunity.

For each candidate opportunity, explain:

- what was noticed;
- why it might be worth investigating;
- which Signals support the discovery;
- the source evidence supporting those Signals;
- what remains uncertain or unresolved.

STRICT RULES:

- Use only the provided Signals.
- Do not use outside knowledge.
- Do not verify or fact-check source claims.
- Do not determine monetary value.
- Do not recommend purchasing an instrument.
- Do not invent missing information.
- Do not convert uncertain claims into established facts.
- Preserve the distinction between source claims and interpretation.
- Do not treat every listing as an opportunity.
- Do not manufacture opportunities simply to produce output.
- If a listing contains nothing that appears worth investigating, omit it.
- A candidate may be supported by one Signal or by a combination of Signals.
- Multiple Signals may support the same candidate opportunity.
- Keep explanations grounded in the supplied evidence.

The goal is not to identify the most unusual listings.

The goal is to identify opportunities that a human investigator might reasonably consider worth looking into further.

STRUCTURED EVIDENCE:
[INSERT SIGNAL DATA HERE]
```
