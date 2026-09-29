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

The extraction output is therefore considered sufficient to proceed to deterministic discovery analysis. Further refinement of the extraction stage should be driven by failures discovered during that analysis rather than by attempting to make the AI independently determine what is "interesting."

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

## 11. Non-Goals

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

## 12. Guiding Principle

> **The experiment should earn the right to become a product.**

Implementation choices should follow what is learned from the experiment rather than assuming the architecture of the eventual system in advance.
