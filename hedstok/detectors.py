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


def detect_dated_configuration_modification_history(
    extraction: ListingExtraction,
) -> EvidencePattern | None:
    dated_evidence = []
    core_evidence = []
    history_evidence = []

    date_terms = (
        "19",
        "20",
    )

    core_terms = (
        "modified",
        "modification",
        "installed",
        "locking nut",
        "heavy gauge",
    )

    supporting_terms = (
        "original",
        "retained",
        "rust",
        "corrosion",
    )

    for index, signal in enumerate(extraction.signals):
        claim = signal.claim.lower()

        if any(term in claim for term in date_terms):
            dated_evidence.append((index, signal))

        if "original" in claim and "installed" in claim:
            role = "establishes modification and retained original components"
            history_evidence.append((index, role))

        elif any(term in claim for term in core_terms):
            if "heavy gauge" in claim:
                role = "establishes configuration"
            else:
                role = "establishes modification"

            history_evidence.append((index, role))
            core_evidence.append(index)

        elif any(term in claim for term in supporting_terms):
            if "original" in claim or "retained" in claim:
                role = "establishes retained original components"
            else:
                role = "establishes condition evidence"

            history_evidence.append((index, role))

    if not dated_evidence or not core_evidence:
        return None

    evidence = [
        PatternEvidence(
            signal_index=index,
            role="establishes dated instrument context",
        )
        for index, signal in dated_evidence
    ]

    evidence.extend(
        PatternEvidence(
            signal_index=index,
            role=role,
        )
        for index, role in history_evidence
    )

    return EvidencePattern(
        listing_id=extraction.listing_id,
        pattern="dated_configuration_modification_history",
        evidence=evidence,
    )


def detect_instrument_transaction_context(
    extraction: ListingExtraction,
) -> EvidencePattern | None:
    instrument_evidence = []
    transaction_evidence = []

    for index, signal in enumerate(extraction.signals):
        if signal.type in ("identity", "configuration"):
            instrument_evidence.append(index)

        if signal.type == "seller_context":
            transaction_evidence.append(index)

    if not instrument_evidence or not transaction_evidence:
        return None

    evidence = [
        PatternEvidence(
            signal_index=index,
            role="establishes instrument-specific evidence",
        )
        for index in instrument_evidence
    ]

    evidence.extend(
        PatternEvidence(
            signal_index=index,
            role="establishes transaction context",
        )
        for index in transaction_evidence
    )

    return EvidencePattern(
        listing_id=extraction.listing_id,
        pattern="instrument_transaction_context",
        evidence=evidence,
    )


def detect_provenance(
    extraction: ListingExtraction,
) -> EvidencePattern | None:
    evidence = []

    for index, signal in enumerate(extraction.signals):
        claim = signal.claim.lower()

        if (
            ("belongs to" in claim and "seller's dad" in claim)
            or "featured on" in claim
            or "from kirk hammett" in claim
        ):
            evidence.append(
                PatternEvidence(
                    signal_index=index,
                    role="establishes provenance",
                )
            )

    if not evidence:
        return None

    return EvidencePattern(
        listing_id=extraction.listing_id,
        pattern="provenance",
        evidence=evidence,
    )
