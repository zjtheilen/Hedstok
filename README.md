```
░  ░░░░  ░░        ░░       ░░░░      ░░░        ░░░      ░░░  ░░░░  ░
▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒▒  ▒▒
▓        ▓▓      ▓▓▓▓  ▓▓▓▓  ▓▓▓      ▓▓▓▓▓▓  ▓▓▓▓▓  ▓▓▓▓  ▓▓     ▓▓▓▓
█  ████  ██  ████████  ████  ████████  █████  █████  ████  ██  ███  ██
█  ████  ██        ██       ████      ██████  ██████      ███  ████  █
                       Hey. Look at this one.
```

# Hedstok

**Acquisition intelligence for used musical instruments.**

> **Find. Filter. Summarize. Cool Guitars with Cool Stories.**

Hedstok explores whether software can help people discover musical instruments and acquisition leads worth a closer look—not necessarily because they are the best, rarest, or most valuable, but because there is **a story worth hearing, a question worth investigating, or something unusual worth noticing.**

A listing might contain a personal history, an uncertain identity, an unusual configuration, a provenance claim, conflicting evidence, or a connection that becomes meaningful only when several details are considered together.

Hedstok's goal is to surface those details and explain why they may matter:

> **"Hey. Look at this one."**

## The Core Idea

Conventional search is good at finding listings that match known attributes. Hedstok investigates a different question:

> **Can software identify meaningful reasons to investigate a listing when those reasons are buried in messy descriptions, incomplete information, or relationships among otherwise ordinary details?**

The answer is not assumed. It is the premise being tested.

Hedstok is interested in public listings as well as manually supplied leads and private acquisition opportunities. It does not assume that every useful lead must come from broad marketplace search.

## What Hedstok Is — and Is Not

Hedstok is an experimental project exploring evidence-grounded discovery and interpretation.

It is intended to help a person notice something potentially interesting and understand why it deserves attention.

It is **not** intended to:

- Decide what a person should buy.
- Estimate market value or identify a bargain.
- Authenticate an instrument or independently verify seller claims.
- Treat an AI-generated interpretation as established fact.
- Replace human investigation with an opaque score or recommendation.

An interesting lead is a reason to look closer, not proof of value, authenticity, rarity, or significance.

## Current Status

**Early R&D — experimental evidence and interpretation work**

The repository contains experiments with structured Signal extraction, deterministic evidence-pattern detectors, and evidence-grounded interpretation.

The initial experiments used a small synthetic dataset of 14 guitar listings and acquisition leads. The examples intentionally include uncertain identification, seller-reported history, unusual configurations, incomplete descriptions, conflicting information, and cases that should not necessarily be surfaced.

The experiments provided preliminary evidence that structured Signals can support useful discovery. They also exposed important limitations:

- Extracted evidence can lose relevant source context.
- Signal categories can be inconsistent with the meaning of a claim.
- Detector rules can infer more than the available evidence supports.
- A faithful extraction does not guarantee a faithful interpretation.
- Source references improve traceability but do not guarantee that a claim is fully supported by its cited text.

The current work is a **Signal Fidelity Audit**: examining source material, extracted Signals, and downstream detector behavior before making broader changes to prompts, schemas, or architecture.

Hedstok remains experimental. The current work does not establish a finished product or a generally reliable acquisition-discovery system.

## Guiding Principles

**Evidence before assumptions.** Preserve what the source says or shows without silently turning a claim into a verified fact.

**Stories before specifications.** Specifications matter, but so can personal history, context, provenance claims, unusual details, and relationships among evidence.

**Evidence before labels.** A judgment should be explainable through the evidence behind it.

**Concepts before implementation.** An experimental result informs design; it does not automatically justify a permanent feature.

**Evolution, not rewrite.** Preserve useful discoveries and working behavior unless there is a demonstrated reason to change them.

The core boundary is:

> **AI can help identify and structure evidence. Software can evaluate explicit relationships. Interpretation must remain grounded in the available evidence. A human decides what deserves further investigation.**

## Research and Documentation

The project keeps durable concepts, current direction, and detailed experimental findings separate.

- [`docs/concept.md`](docs/concept.md) — the project's purpose, conceptual distinctions, and design boundaries.
- [`docs/roadmap.md`](docs/roadmap.md) — phase status, open questions, and next steps.
- [`docs/phase-3-discovery.md`](docs/phase-3-discovery.md) — evidence-pattern discovery experiments and findings.
- [`docs/phase-4-interpretation.md`](docs/phase-4-interpretation.md) — interpretation experiments, evaluations, and retained limitations.
- [`docs/phase-5-signal-fidelity-audit.md`](docs/phase-5-signal-fidelity-audit.md) — the active audit of extraction fidelity, Signal semantics, and detector interpretation.

The experimental record is part of the project. Negative results, false positives, unresolved questions, and limitations are retained rather than hidden behind a claim of success.

## The Standard

Every proposed capability should answer a simple question:

> **Does this help a person notice something meaningful, understand why it matters, and distinguish evidence from assumption?**

If a feature cannot demonstrate that contribution, it has not earned a place in Hedstok's design.
