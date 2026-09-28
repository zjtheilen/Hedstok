import json

from google import genai
from google.genai import types
from pydantic import BaseModel


class Signal(BaseModel):
    type: str
    claim: str
    source_text: str


class ListingExtraction(BaseModel):
    listing_id: str
    signals: list[Signal]


class Extraction(BaseModel):
    listings: list[ListingExtraction]


client = genai.Client(
    http_options=types.HttpOptions(timeout=30000)
)


def extract_signals(listings):
    listings_text = "\n\n".join(
        f"LISTING ID: {listing['id']}\n"
        f"DESCRIPTION: {listing['description']}"
        for listing in listings
    )

    prompt = """
Extract the observable claims from each guitar listing below.

STRICT RULES:
- Extract only information explicitly stated in each listing.
- Do not use outside knowledge.
- Do not verify or fact-check any claim.
- Do not decide whether a claim is true or false.
- Do not infer missing information.
- Do not evaluate the guitar's value or significance.
- Preserve the distinction between what the source says and what is known.
- Every source_text value must be copied exactly from its listing.
- Keep each claim concise and faithful to the source.
- Do not strengthen the certainty of a claim.
- Keep signals associated with the correct listing ID.
- Include every listing, even if it has no unusual signals.

For each signal provide:
- type: a short category such as ownership_history, recording_history,
  brand, electronics, condition, or other
- claim: a concise restatement of exactly what the listing claims
- source_text: the exact text from the listing supporting that claim

LISTINGS:

""" + listings_text

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": Extraction.model_json_schema(),
        },
    )

    return Extraction.model_validate_json(
        interaction.output_text
    ).listings


with open("experiment-0/input/listings.json") as file:
    data = json.load(file)

results = extract_signals(data["listings"])

for result in results:
    print(json.dumps(
        result.model_dump(),
        indent=2
    ))