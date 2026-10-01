from discover import (
    find_uncertain_identification,
)


def make_listing(listing_id, signals):
    return {
        "listing_id": listing_id,
        "signals": signals,
    }


def make_signal(signal_type, claim):
    return {
        "type": signal_type,
        "claim": claim,
        "source_text": claim,
    }


def test_uncertain_identity_triggers():
    listing = make_listing(
        "test-uncertain-identity",
        [
            make_signal(
                "identity",
                "The seller says it might be a Gibson or something.",
            ),
        ],
    )

    result = find_uncertain_identification(listing)

    assert result is not None
    assert result["listing_id"] == "test-uncertain-identity"


def test_certain_identity_does_not_trigger():
    listing = make_listing(
        "test-certain-identity",
        [
            make_signal(
                "identity",
                "The guitar is a Fender Stratocaster.",
            ),
        ],
    )

    result = find_uncertain_identification(listing)

    assert result is None


def test_unrelated_evidence_does_not_trigger():
    listing = make_listing(
        "test-unrelated-evidence",
        [
            make_signal(
                "identity",
                "The guitar is a Fender.",
            ),
            make_signal(
                "market_context",
                "The guitar is from 1992.",
            ),
            make_signal(
                "condition",
                "The guitar has some rust.",
            ),
        ],
    )

    result = find_uncertain_identification(listing)

    assert result is None


def test_story_does_not_trigger_uncertain_identity():
    listing = make_listing(
        "test-story-only",
        [
            make_signal(
                "story",
                "The guitar belonged to the seller's father.",
            ),
        ],
    )

    result = find_uncertain_identification(listing)

    assert result is None


def run_tests():
    tests = [
        test_uncertain_identity_triggers,
        test_certain_identity_does_not_trigger,
        test_unrelated_evidence_does_not_trigger,
        test_story_does_not_trigger_uncertain_identity,
    ]

    for test in tests:
        test()
        print(f"PASS: {test.__name__}")

    print(f"\n{len(tests)} tests passed.")


if __name__ == "__main__":
    run_tests()
