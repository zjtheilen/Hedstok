import json
import random
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel


class Interpretation(BaseModel):
    description: str
    supporting_signals: list[str]


class ListingInterpretations(BaseModel):
    listing_id: str
    interpretations: list[Interpretation]


class InterpretationResults(BaseModel):
    listings: list[ListingInterpretations]


load_dotenv()

client = genai.Client(http_options=types.HttpOptions(timeout=300000))


def create_interaction_with_retry(prompt, schema, max_retries=3):
    for attempt in range(max_retries + 1):
        try:
            return client.interactions.create(
                model="gemini-3.5-flash-lite",
                input=prompt,
                response_format={
                    "type": "text",
                    "mime_type": "application/json",
                    "schema": schema,
                },
            )

        except Exception as error:
            error_text = str(error)

            if "requests per day" in error_text:
                print(
                    "Gemini daily request limit reached. Stopping retries.",
                    flush=True,
                )
                raise

            if attempt >= max_retries:
                raise

            delay = (5 * (2**attempt)) + random.uniform(0, 2)

            print(
                f"Gemini request failed: {error}",
                flush=True,
            )
            print(
                f"Retrying in {delay:.1f} seconds "
                f"(attempt {attempt + 1}/{max_retries})...",
                flush=True,
            )

            time.sleep(delay)


def derive_interpretations(extractions):
    listings_text = "\n\n".join(
        f"LISTING ID: {extraction['listing_id']}\n"
        + "\n".join(
            f"- [{signal['type']}] {signal['claim']} (source: {signal['source_text']})"
            for signal in extraction["signals"]
        )
        for extraction in extractions
    )

    prompt = f"""
Identify possible semantic interpretations supported by multiple
signals in each guitar listing below.

A semantic interpretation is a cautious hypothesis about what multiple
signals may mean when considered together. It is not a verified fact.

{listings_text}

STRICT RULES:
- Derive interpretations only from the supplied signals.
- Do not use outside knowledge.
- Do not verify or fact-check the signals.
- Do not introduce facts that are not supported by the signals.
- Do not introduce new factual premises through common knowledge,
  domain knowledge, or typical associations.
- Every substantive element of an interpretation must be traceable
  to one or more supporting signals.
- Combining signals may produce a new possible meaning, but must not
  add assumptions about what is typical, common, valuable, authentic,
  neglected, beginner-oriented, vintage, rare, or desirable unless
  those characteristics are explicitly supported by the signals.
- Do not convert an uncertain claim into a stronger claim.
- Do not infer motive, condition, authenticity, rarity, or market
  significance unless the supplied signals explicitly support it.
- Do not decide whether an interpretation is true.
- Preserve uncertainty when the evidence is incomplete or ambiguous.
- An interpretation may synthesize multiple signals into a more coherent
  possible meaning, provided that the synthesis does not require adding
  unsupported factual assumptions.
- An interpretation may identify a possible identity or configuration
  suggested by multiple signals, but must preserve uncertainty when the
  identity is not explicit.
- An interpretation may identify conflicting claims when multiple signals
  describe the same aspect of the listing inconsistently.
- An interpretation may identify a meaningful association between the
  instrument and another entity when multiple signals support that
  association.
- An interpretation must add semantic meaning beyond simply repeating
  that multiple signals exist.
- Do not create an interpretation merely because several signals exist.
- Do not evaluate whether an interpretation is valuable, rare,
  desirable, or worth purchasing.
- Do not rank interpretations.
- Do not make recommendations.
- Each interpretation must identify the specific signal claims that
  support it.
- If no meaningful interpretation is supported by multiple signals,
  return an empty interpretations list.
- Include exactly one result for every listing ID provided.

Examples of acceptable interpretations:

- Multiple physical and identity clues may together suggest a possible
  instrument type or configuration, while leaving the identification
  uncertain.
- Textual and image evidence may conflict about the identity of an
  instrument.
- Ownership, configuration, and associated-equipment signals may together
  suggest a possible relationship or history that is not explicitly
  stated as a single claim.

For each interpretation provide:
- description: a concise description of the possible interpretation
- supporting_signals: the exact signal claims that support it
"""

    print(
        f"Deriving interpretations for {len(extractions)} listings...",
        flush=True,
    )

    interaction = create_interaction_with_retry(
        prompt,
        InterpretationResults.model_json_schema(),
    )

    results = InterpretationResults.model_validate_json(
        interaction.output_text
    ).listings

    print("Interpretation derivation complete.", flush=True)

    return results


with open("experiment-0/output/extraction-revised.json") as file:
    extractions = json.load(file)


fixture_ids = {
    "listing-03",
    "listing-06",
    "listing-08",
    "listing-11",
}

fixtures = [
    extraction for extraction in extractions if extraction["listing_id"] in fixture_ids
]

results = derive_interpretations(fixtures)

print(
    json.dumps(
        [result.model_dump() for result in results],
        indent=2,
    )
)
