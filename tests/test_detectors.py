import json
from pathlib import Path

from hedstok.detectors import detect_seller_inventory_opportunity
from hedstok.models import ListingExtraction, Signal


def test_seller_inventory_opportunity_detected():
    extraction = ListingExtraction(
        listing_id="listing-09",
        signals=[
            Signal(
                type="seller_context",
                claim="seller has a large collection",
                source_text="I have a large collection of guitars.",
            ),
            Signal(
                type="seller_context",
                claim="seller is willing to make deals for long-term business potential",
                source_text="I'm willing to make deals if there's long-term business potential.",
            ),
        ],
    )

    result = detect_seller_inventory_opportunity(extraction)

    assert result is not None
    assert result.listing_id == "listing-09"
    assert result.pattern == "seller_inventory_opportunity"

    assert len(result.evidence) == 2

    assert result.evidence[0].signal_index == 0
    assert result.evidence[0].role == "establishes meaningful collection or inventory"

    assert result.evidence[1].signal_index == 1
    assert result.evidence[1].role == "establishes willingness to transact"


def test_single_instrument_sale_is_not_seller_inventory_opportunity():
    extraction = ListingExtraction(
        listing_id="listing-negative-01",
        signals=[
            Signal(
                type="seller_context",
                claim="seller is selling an old guitar",
                source_text="I'm selling my old guitar.",
            ),
        ],
    )

    result = detect_seller_inventory_opportunity(extraction)

    assert result is None

def test_collection_alone_is_not_seller_inventory_opportunity():
    extraction = ListingExtraction(
        listing_id="listing-negative-02",
        signals=[
            Signal(
                type="seller_context",
                claim="seller has a large collection",
                source_text="I have a large collection of guitars.",
            ),
        ],
    )

    result = detect_seller_inventory_opportunity(extraction)

    assert result is None

def test_seller_inventory_opportunity_can_use_multiple_signal_types():
    extraction = ListingExtraction(
        listing_id="listing-03",
        signals=[
            Signal(
                type="seller_context",
                claim="seller has a large collection",
                source_text="I have a large collection of guitars.",
            ),
            Signal(
                type="market_context",
                claim="seller is selling several guitars",
                source_text="I'm selling several guitars from my collection.",
            ),
        ],
    )

    result = detect_seller_inventory_opportunity(extraction)

    assert result is not None

def test_explicitly_not_transacting_is_not_an_opportunity():
    extraction = ListingExtraction(
        listing_id="listing-negative-03",
        signals=[
            Signal(
                type="seller_context",
                claim="seller has a large collection but is not selling or trading",
                source_text="I have a large collection of guitars but I'm not selling or trading anything.",
            ),
        ],
    )

    result = detect_seller_inventory_opportunity(extraction)

    assert result is None

def test_explicitly_not_trading_is_not_an_opportunity():
    extraction = ListingExtraction(
        listing_id="listing-negative-04",
        signals=[
            Signal(
                type="seller_context",
                claim="seller has a large collection and is not open to trades",
                source_text="I have a large collection of guitars and I'm not open to trades.",
            ),
        ],
    )

    result = detect_seller_inventory_opportunity(extraction)

    assert result is None

def test_collection_in_storage_with_offer_is_detected():
    extraction = ListingExtraction(
        listing_id="listing-positive-02",
        signals=[
            Signal(
                type="seller_context",
                claim="seller has a bunch of guitars in storage",
                source_text="I've got a bunch of guitars in storage.",
            ),
            Signal(
                type="seller_context",
                claim="seller wants an offer",
                source_text="Make me an offer.",
            ),
        ],
    )

    result = detect_seller_inventory_opportunity(extraction)

    assert result is not None
    assert result.listing_id == "listing-positive-02"
    assert result.pattern == "seller_inventory_opportunity"
    assert len(result.evidence) == 2

def test_listing_09_from_extraction_artifact():
    extraction_path = (
        Path(__file__).parent.parent / "extraction2.json"
    )

    with open(extraction_path, encoding="utf-8") as file:
        data = json.load(file)

    listing_data = next(
        listing
        for listing in data
        if listing["listing_id"] == "listing-09"
    )

    extraction = ListingExtraction.model_validate(listing_data)

    result = detect_seller_inventory_opportunity(extraction)

    assert result is not None
    assert result.listing_id == "listing-09"
    assert result.pattern == "seller_inventory_opportunity"

    assert len(result.evidence) >= 2

    roles = {evidence.role for evidence in result.evidence}

    assert "establishes meaningful collection or inventory" in roles
    assert "establishes willingness to transact" in roles

def test_seller_inventory_detector_against_extraction_artifact():
    extraction_path = (
        Path(__file__).parent.parent / "extraction2.json"
    )

    with open(extraction_path, encoding="utf-8") as file:
        data = json.load(file)

    extractions = [
        ListingExtraction.model_validate(listing)
        for listing in data
    ]

    results = {
        extraction.listing_id: detect_seller_inventory_opportunity(extraction)
        for extraction in extractions
    }

    assert results["listing-09"] is not None

    assert results["listing-01"] is None
    assert results["listing-02"] is None
    assert results["listing-03"] is None
    assert results["listing-04"] is None
    assert results["listing-05"] is None
    assert results["listing-06"] is None
    assert results["listing-07"] is None
    assert results["listing-08"] is None
    assert results["listing-10"] is None
    assert results["listing-11"] is None
    assert results["listing-12"] is None
    assert results["listing-13"] is None
    assert results["listing-14"] is None
