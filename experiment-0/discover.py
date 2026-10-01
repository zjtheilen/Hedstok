import json


def find_provenance_clusters(listing):
    signals = listing["signals"]
    signal_types = {signal["type"] for signal in signals}

    if {"ownership_history", "recording_history"} <= signal_types:
        return {
            "listing_id": listing["listing_id"],
            "reason": (
                "The listing combines ownership history with a recording-history claim."
            ),
            "signals": [
                signal
                for signal in signals
                if signal["type"]
                in {
                    "ownership_history",
                    "recording_history",
                }
            ],
            "investigate": ("Verify the claimed ownership and recording history."),
        }

    return None


def find_uncertain_identification(listing):
    signals = listing["signals"]
    signal_types = {signal["type"] for signal in signals}

    if "ownership_history" not in signal_types:
        return None

    brand_signals = [signal for signal in signals if signal["type"] == "brand"]

    if any(
        "something" in signal["claim"].lower()
        or "might" in signal["claim"].lower()
        or "unknown" in signal["claim"].lower()
        for signal in brand_signals
    ):
        return {
            "listing_id": listing["listing_id"],
            "reason": (
                "The listing combines ownership history "
                "with an uncertain instrument identification."
            ),
            "signals": [
                signal
                for signal in signals
                if signal["type"]
                in {
                    "ownership_history",
                    "brand",
                }
            ],
            "investigate": ("Determine the instrument's manufacturer and model."),
        }

    return None


def find_modification_cluster(listing):
    signals = listing["signals"]

    modification_terms = (
        "aftermarket",
        "off-brand",
        "locking nut",
        "heavy gauge",
        "modified",
        "modification",
        "setup for",
    )

    modification_signals = [
        signal
        for signal in signals
        if any(term in signal["claim"].lower() for term in modification_terms)
    ]

    if len(modification_signals) >= 2:
        return {
            "listing_id": listing["listing_id"],
            "reason": (
                "The listing contains multiple signals describing "
                "modifications or specialized configuration."
            ),
            "signals": modification_signals,
            "investigate": (
                "Determine which modifications are present and "
                "whether the original configuration is available."
            ),
        }

    return None


def find_identity_configuration_convergence(listing):
    signals = listing["signals"]
    signal_types = {signal["type"] for signal in signals}

    if {"identity", "configuration"} <= signal_types:
        return {
            "listing_id": listing["listing_id"],
            "reason": (
                "The listing combines instrument-identification evidence "
                "with configuration evidence."
            ),
            "signals": [
                signal
                for signal in signals
                if signal["type"] in {"identity", "configuration"}
            ],
            "investigate": (
                "Verify the instrument's identity and determine whether "
                "the configuration is consistent with that identification."
            ),
        }

    return None


def find_contradictions(listing):
    signals = listing["signals"]

    identity_signals = [
        signal
        for signal in signals
        if signal["type"] in {"brand", "other"}
        and any(
            term in signal["claim"].lower()
            for term in {"les paul", "guitar is listed as"}
        )
    ]

    image_signals = [
        signal for signal in signals if "image" in signal["source_text"].lower()
    ]

    if identity_signals and image_signals:
        return {
            "listing_id": listing["listing_id"],
            "reason": (
                "The listing contains an instrument identification "
                "that conflicts with an image-based observation."
            ),
            "signals": identity_signals + image_signals,
            "investigate": (
                "Verify the instrument's identity against the image "
                "and other available evidence."
            ),
        }

    return None


def find_seller_motivation(listing):
    signals = listing["signals"]

    has_original_claim = any(
        "original" in signal["claim"].lower() for signal in signals
    )

    motivation_signals = [
        signal
        for signal in signals
        if any(
            term in signal["claim"].lower()
            for term in (
                "trade",
                "tube amp",
                "high-gain",
                "high gain",
            )
        )
    ]

    if has_original_claim and motivation_signals:
        return {
            "listing_id": listing["listing_id"],
            "reason": (
                "The listing combines an originality claim "
                "with a specific seller trade motivation."
            ),
            "signals": [
                signal
                for signal in signals
                if signal in motivation_signals or "original" in signal["claim"].lower()
            ],
            "investigate": (
                "Determine what the seller wants in trade and "
                "whether the instrument's original configuration "
                "can be verified."
            ),
        }

    return None


def discover(extractions):
    discoveries = []

    for listing in extractions:
        for rule in (
            find_provenance_clusters,
            find_uncertain_identification,
            find_identity_configuration_convergence,
            find_modification_cluster,
            find_seller_motivation,
            find_contradictions,
        ):
            discovery = rule(listing)

            if discovery is not None:
                discoveries.append(discovery)

    return discoveries


if __name__ == "__main__":
    with open("experiment-0/output/extraction-baseline.json") as file:
        extractions = json.load(file)

    results = discover(extractions)

    print(json.dumps(results, indent=2))
