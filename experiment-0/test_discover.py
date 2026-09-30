from discover import (
    find_modification_cluster,
    find_provenance_clusters,
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


def test_provenance_cluster():
    listing = make_listing(
        "test-provenance",
        [
            make_signal(
                "ownership_history",
                "The guitar belonged to the seller's father.",
            ),
            make_signal(
                "recording_history",
                "The guitar was used on a recording.",
            ),
        ],
    )

    result = find_provenance_clusters(listing)

    assert result is not None
    assert result["listing_id"] == "test-provenance"


def test_provenance_requires_both_signal_types():
    listing = make_listing(
        "test-no-provenance",
        [
            make_signal(
                "ownership_history",
                "The guitar belonged to the seller's father.",
            ),
            make_signal(
                "condition",
                "The guitar is in good condition.",
            ),
        ],
    )

    result = find_provenance_clusters(listing)

    assert result is None


def test_modification_cluster():
    listing = make_listing(
        "test-modification",
        [
            make_signal(
                "electronics",
                "Aftermarket pickups are installed.",
            ),
            make_signal(
                "other",
                "The guitar is setup for heavy gauge strings.",
            ),
            make_signal(
                "other",
                "A locking nut is installed.",
            ),
        ],
    )

    result = find_modification_cluster(listing)

    assert result is not None
    assert result["listing_id"] == "test-modification"


def test_single_modification_signal_does_not_trigger():
    listing = make_listing(
        "test-single-modification",
        [
            make_signal(
                "electronics",
                "Aftermarket pickups are installed.",
            ),
        ],
    )

    result = find_modification_cluster(listing)

    assert result is None


def test_original_pickups_alone_does_not_trigger_modification_cluster():
    listing = make_listing(
        "test-original-pickups",
        [
            make_signal(
                "electronics",
                "Original pickups are installed.",
            ),
        ],
    )

    result = find_modification_cluster(listing)

    assert result is None


def run_tests():
    tests = [
        test_provenance_cluster,
        test_provenance_requires_both_signal_types,
        test_modification_cluster,
        test_single_modification_signal_does_not_trigger,
        test_original_pickups_alone_does_not_trigger_modification_cluster,
        test_unrelated_configuration_terms_do_not_trigger_modification_cluster,
    ]

    for test in tests:
        test()
        print(f"PASS: {test.__name__}")

    print(f"\n{len(tests)} tests passed.")


def test_unrelated_configuration_terms_do_not_trigger_modification_cluster():
    listing = make_listing(
        "test-unrelated-configuration",
        [
            make_signal(
                "electronics",
                "Original pickups are included.",
            ),
            make_signal(
                "other",
                "The original setup is documented.",
            ),
        ],
    )

    result = find_modification_cluster(listing)

    assert result is None


if __name__ == "__main__":
    run_tests()
