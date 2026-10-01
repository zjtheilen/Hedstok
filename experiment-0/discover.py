import json


def find_uncertain_identification(listing):
    signals = listing["signals"]

    identity_signals = [signal for signal in signals if signal["type"] == "identity"]

    uncertain_identity_signals = [
        signal
        for signal in identity_signals
        if any(
            term in signal["claim"].lower()
            for term in (
                "something",
                "might",
                "maybe",
                "unknown",
                "not sure",
                "unsure",
            )
        )
    ]

    if uncertain_identity_signals:
        return {
            "listing_id": listing["listing_id"],
            "reason": (
                "The listing contains identity evidence with unresolved identification."
            ),
            "signals": uncertain_identity_signals,
            "investigate": ("Determine the instrument's manufacturer and model."),
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


def discover(extractions):
    discoveries = []

    for listing in extractions:
        for rule in (
            find_uncertain_identification,
            find_identity_configuration_convergence,
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
