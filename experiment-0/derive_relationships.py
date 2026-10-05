import json
import random
import time
from typing import Literal

from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel

load_dotenv()


class Relationship(BaseModel):
    type: Literal[
        "convergence",
        "association",
        "historical_association",
        "contradiction",
        "distinctiveness",
    ]
    description: str
    supporting_signals: list[str]


class ListingRelationships(BaseModel):
    listing_id: str
    relationships: list[Relationship]


class RelationshipResults(BaseModel):
    listings: list[ListingRelationships]


client = genai.Client(
    http_options=types.HttpOptions(timeout=300000)
)


def create_interaction_with_retry(prompt, schema, max_retries=3):
    for attempt in range(max_retries + 1):
        try:
            return client.interactions.create(
                model="gemini-3.5-flash-lite",
                input=prompt,
                response_format={
                    "type": "text",
                    "mime_type": "application/json",
                    "schema": schema.model_json_schema(),
                },
            )
        except Exception as error:
            error_text = str(error)

            if "requests per day" in error_text:
                print("Daily request limit reached.")
                raise

            if attempt == max_retries:
                raise

            delay = (5 * (2 ** attempt)) + random.uniform(0, 2)
            print(
                f"Request failed: {error_text}\n"
                f"Retrying in {delay:.1f} seconds..."
            )
            time.sleep(delay)


def derive_relationships(extractions):
    listings_text = "\n\n".join(
        f"LISTING ID: {extraction['listing_id']}\n"
        + "\n".join(
            f"- [{signal['type']}] {signal['claim']} "
            f"(source: {signal['source_text']})"
            for signal in extraction["signals"]
        )
        for extraction in extractions
    )

    prompt = f"""
Identify candidate relationships between extracted signals in each
guitar listing below.

{listings_text}

STRICT RULES:
- Derive relationships only from the supplied signals.
- Do not use outside knowledge.
- Do not verify or fact-check any signal.
- Do not decide whether any signal is true or false.
- Preserve uncertainty present in the source evidence.
- Do not introduce new factual premises.
- Do not infer value, rarity, authenticity, desirability, or
  acquisition suitability.
- Do not make recommendations.
- Do not rank relationships.
- Do not treat the existence of multiple signals as sufficient by
  itself to establish a relationship.
- Every relationship must be supported by at least two signals.
- Every supporting_signals value must exactly match a signal claim
  supplied for that listing.
- If the supplied evidence does not support a meaningful relationship,
  return an empty relationships list.
- Include exactly one result for every listing ID provided.

Use only these relationship types:

- convergence: multiple distinct pieces of evidence point toward the
  same underlying possibility or meaning
- association: evidence establishes a meaningful relationship between
  the instrument and another entity
- historical_association: evidence connects the instrument to a person,
  event, work, or historical context beyond ordinary ownership
- contradiction: two or more pieces of evidence make materially
  incompatible claims about the same aspect
- distinctiveness: evidence indicates an unusual or potentially notable
  characteristic relative to an appropriate reference context

Important:
- Relationship types describe the structure of the evidence.
- They do not establish significance, value, rarity, desirability,
  authenticity, or acquisition suitability.
- For distinctiveness, do not claim that a characteristic is actually
  rare or unusual unless that is established by supplied evidence.
  Instead, describe the evidence as potentially distinctive when
  appropriate.
- Do not create a relationship merely by combining unrelated facts.
- A relationship description must explain what connects the supporting
  signals.
- A description must not simply restate one signal.
"""

    print(
        f"Deriving relationships for {len(extractions)} listings..."
    )

    interaction = create_interaction_with_retry(
        prompt,
        RelationshipResults,
    )

    results = RelationshipResults.model_validate_json(
        interaction.output_text
    ).listings

    print("Relationship derivation complete.")

    return results


with open("experiment-0/output/extraction-revised.json") as file:
    extractions = json.load(file)


fixture_ids = {
    "listing-01",
    "listing-02",
    "listing-03",
    "listing-05",
    "listing-06",
    "listing-08",
    "listing-09",
    "listing-11",
    "listing-12",
    "listing-14",
}

fixtures = [
    extraction
    for extraction in extractions
    if extraction["listing_id"] in fixture_ids
]

results = derive_relationships(fixtures)

output = [result.model_dump() for result in results]

with open(
    "experiment-0/output/relationships_fixtures.json",
    "w",
) as file:
    json.dump(output, file, indent=2)

print(json.dumps(output, indent=2))
