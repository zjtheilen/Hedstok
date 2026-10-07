from hedstok.models import EvidencePattern, ListingExtraction, PatternEvidence


def detect_seller_inventory_opportunity(
    extraction: ListingExtraction,
) -> EvidencePattern | None:
    collection_evidence = []
    transaction_evidence = []

    collection_terms = (
        "large collection",
        "several guitars",
        "multiple guitars",
        "bunch of guitars",
        "inventory",
        "guitar shop",
        "buy and sell",
    )

    transaction_terms = (
        "selling",
        "open to trades",
        "open to trade",
        "willing to sell",
        "make me an offer",
        "make an offer",
        "make deals",
        "looking to buy",
        "buying",
        "business relationship",
        "wants an offer",
    )

    for index, signal in enumerate(extraction.signals):
        claim = signal.claim.lower()

        if any(
            phrase in claim
            for phrase in (
                "not selling",
                "not open to trade",
                "not open to trades",
                "not trading",
            )
        ):
            continue

        if any(term in claim for term in collection_terms):
            collection_evidence.append((index, signal))

        if any(term in claim for term in transaction_terms):
            transaction_evidence.append((index, signal))

    if not collection_evidence or not transaction_evidence:
        return None

    evidence = [
        PatternEvidence(
            signal_index=index,
            role="establishes meaningful collection or inventory",
        )
        for index, signal in collection_evidence
    ]

    evidence.extend(
        PatternEvidence(
            signal_index=index,
            role="establishes willingness to transact",
        )
        for index, signal in transaction_evidence
    )

    return EvidencePattern(
        listing_id=extraction.listing_id,
        pattern="seller_inventory_opportunity",
        evidence=evidence,
    )
