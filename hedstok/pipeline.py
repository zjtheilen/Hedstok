import json

from dotenv import load_dotenv
from google import genai
from google.genai import types

from hedstok.models import BatchExtraction

load_dotenv()

client = genai.Client(http_options=types.HttpOptions(timeout=30000))


def process_listings(input_path: str, output_path: str) -> None:
    with open(input_path, encoding="utf-8") as file:
        data = json.load(file)

    listings_text = "\n\n".join(
        f"""LISTING ID: {listing["id"]}
DESCRIPTION:
{listing["description"]}"""
        for listing in data["listings"]
    )

    prompt = f"""
Extract the observable claims from each guitar listing below.

{listings_text}

STRICT RULES:
- Extract only information explicitly stated in each listing.
- Do not use outside knowledge.
- Do not verify or fact-check any claim.
- Do not decide whether a claim is true or false.
- Do not infer missing information.
- Do not evaluate the guitar's value or significance.
- Preserve the distinction between what the source says and what is known.
- Every source_text value must be copied exactly from the listing.
- Keep each claim concise and faithful to the source.
- Do not strengthen the certainty of a claim.
- Process every listing.
- Preserve each listing's ID exactly.

For each signal provide:
- type: exactly one of:
  identity, configuration, story, associated_equipment,
  seller_context, condition, or market_context
- claim: a concise restatement of exactly what the listing claims
- source_text: the exact text from the listing supporting that claim

Use these semantic categories:
- identity: manufacturer, model, instrument type, or other evidence
  about what the instrument is or may be
- configuration: physical, electronic, hardware, construction, or
  unusual configuration characteristics
- story: human history, ownership, personal significance, previous
  players, recordings, use, or other narrative associated with the
  instrument
- associated_equipment: amps, accessories, or other equipment
  connected to the listing or instrument
- seller_context: seller inventory, collection, selling/trading
  motivation, or business context
- condition: physical condition, damage, wear, or originality
- market_context: price, date, trade terms, or other listing/market
  context
"""

    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=prompt,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": BatchExtraction.model_json_schema(),
        },
    )

    result = BatchExtraction.model_validate_json(interaction.output_text)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            [listing.model_dump() for listing in result.listings],
            file,
            indent=2,
        )


if __name__ == "__main__":
    process_listings(
        "experiment-0/input/listings.json",
        "extraction2.json",
    )
