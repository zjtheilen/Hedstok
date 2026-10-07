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


class PatternEvidence(BaseModel):
    signal_index: int
    role: str


class EvidencePattern(BaseModel):
    listing_id: str
    pattern: str
    evidence: list[PatternEvidence]


class ListingExtraction(BaseModel):
    listing_id: str
    signals: list[Signal]


class BatchExtraction(BaseModel):
    listings: list[ListingExtraction]


class PatternAnalysis(BaseModel):
    listing_id: str
    patterns: list[EvidencePattern]
