from typing import Literal

from pydantic import BaseModel


class Signal(BaseModel):
    type: Literal[
        "identity",
        "configuration",
        "story",
        "associated_equipment",
        "seller_context",
        "condition",
        "market_context",
    ]
    claim: str
    source_text: str


class ListingExtraction(BaseModel):
    listing_id: str
    signals: list[Signal]


class BatchExtraction(BaseModel):
    listings: list[ListingExtraction]
