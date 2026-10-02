import json

from google import genai
from google.genai import types
from pydantic import BaseModel


class Signal(BaseModel):
    type: str
    claim: str
    source_text: str


class Extraction(BaseModel):
    signals: list[Signal]


with open("experiment-0/input/listings.json") as file:
    data = json.load(file)

listing = next(
    item for item in data["listings"]
    if item["id"] == "listing-04"
)

client = genai.Client(
    http_options=types.HttpOptions(timeout=30000)
)

prompt = """
Extract the observable claims from this guitar listing.

STRICT RULES:
- Extract only information explicitly stated in the listing.
- Do not use outside knowledge.
- Do not verify or fact-check any claim.
- Do not decide whether a claim is true or false.
- Do not infer missing information.
- Do not evaluate the guitar's value or significance.
- Preserve the distinction between what the source says and what is known.
- Every source_text value must be copied exactly from the listing.
- Keep each claim concise and faithful to the source.

For each signal provide:
- type: a short category such as ownership_history, recording_history,
  brand, electronics, or condition
- claim: a concise restatement of exactly what the listing claims
- source_text: the exact text from the listing supporting that claim

LISTING:
""" + listing["description"]

interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Extraction.model_json_schema(),
    },
)

result = Extraction.model_validate_json(interaction.output_text)

print(result.model_dump_json(indent=2))