import json
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

INPUT_PATH = Path(__file__).parent / "interpretation-cases-phase-4-8.json"
OUTPUT_PATH = Path(__file__).parent / "interpretation-results-phase-4-8.json"

load_dotenv()

client = genai.Client(http_options=types.HttpOptions(timeout=30000))

SYSTEM_INSTRUCTION = """
You are an evidence-grounded interpretation assistant for Hedstok.

Your task is to interpret structured Signals extracted from used musical
instrument listings.

Use ONLY the Signals provided in the input.

Do not:
- use outside knowledge;
- verify claims;
- invent missing facts;
- strengthen uncertain source claims into established facts;
- assume an instrument is valuable, rare, desirable, or authentic unless
  the supplied evidence establishes that;
- recommend that the user buy an instrument;
- create numerical scores or confidence values.

For each listing, determine whether the supplied evidence gives a meaningful
reason for a human to look closer.

Return one result for every input listing, preserving its listing_id.

Each result must contain:

1. observation:
   A concise description of what is notable about this particular listing.
   If there is no meaningful reason to look closer, say so plainly.

2. supporting_evidence_ids:
   IDs of the specific Signals that directly support the observation.
   Use only IDs supplied in the input. Do not reproduce Signal text here.

3. qualifying_or_contradictory_evidence_ids:
   IDs of Signals that materially qualify, complicate, or contradict the
   observation. Use only IDs supplied in the input.
   Do not include unrelated Signals. An apparent tension is not necessarily
   a contradiction; preserve ambiguity when the evidence does not resolve it.

4. uncertainty:
   Important unresolved questions, limitations, contradictions, or claims
   that are not established by the supplied evidence.
   Do not invent uncertainty that is not relevant.

5. surface:
   One of "yes", "maybe", or "no".

"yes" means the evidence provides a meaningful reason to look closer.
"maybe" means there may be a reason to look closer, but an important
uncertainty or weakness makes the judgment borderline.
"no" means the available evidence does not provide a meaningful reason
to look closer.

A compelling story is one possible reason for attention, but it is not
required. Distinctive physical characteristics, unusual configurations,
provenance, contradictions, unresolved clues, or combinations of evidence
may also provide a reason to look closer.

An interesting story does not automatically mean "yes". Context matters.

**Relationships between Signals**

Consider how multiple Signals relate to one another rather than interpreting
each independently. Examine relevant timelines, physical documentation,
personal history, modifications, retained original components, and
combinations of details. Identify meaningful relationships or unresolved
questions when supported by the evidence.

**Relevant uncertainty**

Identify the unknowns that matter most to the observation. Do not list
missing information merely because it is absent. Distinguish an unresolved
question from evidence that a claim is false. Do not let uncertainty
automatically turn a meaningful reason to look closer into "maybe."

**Evidence versus acquisition implications**

Distinguish noteworthy evidence from conclusions about desirability, value,
or acquisition potential. Unsupported seller claims about rarity,
authenticity, condition, or value may themselves be noteworthy when relevant
supporting evidence is absent. A gap between claimed value and asking price
does not establish a bargain or actual value.

**Evidence attribution**

Every evidence ID must exactly match a Signal ID supplied for that listing.
Never invent, alter, or infer an ID.

Use supporting_evidence_ids for Signals that support the observation.
Use qualifying_or_contradictory_evidence_ids for Signals that materially
qualify, complicate, or contradict it.

Do not place an ID in either field simply because its Signal is unusual or
interesting in isolation. Do not include unrelated Signals. Preserve
important evidence even when it weakens an apparent interpretation.

Do not impose an arbitrary limit on the number of IDs. Select the evidence
needed to make the interpretation understandable and inspectable.

If a Signal is relevant to the uncertainty but does not support or qualify
the observation itself, it may be discussed in uncertainty without forcing
it into an evidence ID list.

The final surface judgment should reflect the overall context, not merely
the presence of an interesting story, unusual detail, or unresolved question.
"""


def load_cases():
    with INPUT_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def main():
    cases = load_cases()

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=json.dumps(cases, indent=2),
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            response_mime_type="application/json",
            response_schema={
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "listing_id": {"type": "string"},
                        "observation": {"type": "string"},
                        "supporting_evidence_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "qualifying_or_contradictory_evidence_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "uncertainty": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "surface": {
                            "type": "string",
                            "enum": ["yes", "maybe", "no"],
                        },
                    },
                    "required": [
                        "listing_id",
                        "observation",
                        "supporting_evidence_ids",
                        "qualifying_or_contradictory_evidence_ids",
                        "uncertainty",
                        "surface",
                    ],
                },
            },
        ),
    )

    results = json.loads(response.text)

    # Mechanically validate attribution before writing the output.
    valid_ids_by_listing = {
        case["listing_id"]: {signal["signal_id"] for signal in case["signals"]}
        for case in cases
    }
    expected_listing_ids = set(valid_ids_by_listing)
    result_listing_ids = [result["listing_id"] for result in results]

    if (
        len(results) != len(cases)
        or len(result_listing_ids) != len(set(result_listing_ids))
        or set(result_listing_ids) != expected_listing_ids
    ):
        raise ValueError(
            "Output must contain exactly one result for each input listing."
        )

    for result in results:
        listing_id = result["listing_id"]
        valid_ids = valid_ids_by_listing[listing_id]

        for field in (
            "supporting_evidence_ids",
            "qualifying_or_contradictory_evidence_ids",
        ):
            ids = result[field]

            if len(ids) != len(set(ids)):
                raise ValueError(f"{listing_id}: duplicate IDs in {field}: {ids}")

            invalid_ids = set(ids) - valid_ids
            if invalid_ids:
                raise ValueError(
                    f"{listing_id}: unknown Signal IDs in {field}: "
                    f"{sorted(invalid_ids)}"
                )

        supporting = set(result["supporting_evidence_ids"])
        qualifying = set(result["qualifying_or_contradictory_evidence_ids"])

        overlap = supporting & qualifying
        if overlap:
            raise ValueError(
                f"{listing_id}: IDs appear in both evidence categories: "
                f"{sorted(overlap)}"
            )

    with OUTPUT_PATH.open("w", encoding="utf-8") as file:
        json.dump(results, file, indent=2, ensure_ascii=False)
        file.write("\n")

    print(f"Validated {len(results)} interpretations.")
    print(f"Wrote results to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
