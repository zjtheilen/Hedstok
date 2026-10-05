from discover import find_identity_configuration_convergence


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


def test_identity_configuration_convergence():
    listing = make_listing(
        "test-identity-configuration",
        [
            make_signal("identity", "The guitar says Fender."),
            make_signal("identity", "The guitar says Precision."),
            make_signal("configuration", "The instrument has four thick strings."),
            make_signal("configuration", "The instrument is kind of long."),
        ],
    )

    result = find_identity_configuration_convergence(listing)

    assert result is not None
    assert result["listing_id"] == "test-identity-configuration"


def test_identity_alone_does_not_trigger_convergence():
    listing = make_listing(
        "test-identity-only",
        [
            make_signal("identity", "The guitar is a Fender Precision."),
            make_signal("market_context", "The guitar is from 1975."),
        ],
    )

    result = find_identity_configuration_convergence(listing)

    assert result is None


def test_configuration_alone_does_not_trigger_convergence():
    listing = make_listing(
        "test-configuration-only",
        [
            make_signal("configuration", "The guitar has four thick strings."),
            make_signal("configuration", "The guitar is kind of long."),
        ],
    )

    result = find_identity_configuration_convergence(listing)

    assert result is None


def test_unrelated_signals_do_not_trigger_convergence():
    listing = make_listing(
        "test-unrelated-signals",
        [
            make_signal("identity", "The guitar is a Fender."),
            make_signal("market_context", "The guitar is from 1992."),
            make_signal("market_context", "The guitar costs $500."),
            make_signal("condition", "The guitar has brand new strings."),
        ],
    )

    result = find_identity_configuration_convergence(listing)

    assert result is None


def run_tests():
    tests = [
        test_identity_configuration_convergence,
        test_identity_alone_does_not_trigger_convergence,
        test_configuration_alone_does_not_trigger_convergence,
        test_unrelated_signals_do_not_trigger_convergence,
    ]

    for test in tests:
        test()
        print(f"PASS: {test.__name__}")

    print(f"\n{len(tests)} tests passed.")


if __name__ == "__main__":
    run_tests()
