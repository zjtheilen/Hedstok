import json
from pathlib import Path

EXPERIMENT_DIR = Path(__file__).parent
SOURCE_PATH = EXPERIMENT_DIR / "interpretation-cases.json"
DERIVED_PATH = EXPERIMENT_DIR / "interpretation-cases-phase-4-8.json"


def main():
    with SOURCE_PATH.open(encoding="utf-8") as file:
        source = json.load(file)

    with DERIVED_PATH.open(encoding="utf-8") as file:
        derived = json.load(file)

    same_case_count = len(source) == len(derived)

    same_listings_and_counts = same_case_count and all(
        original["listing_id"] == converted["listing_id"]
        and len(original["signals"]) == len(converted["signals"])
        for original, converted in zip(source, derived)
    )

    fields_preserved = same_listings_and_counts and all(
        all(
            original_signal[field] == derived_signal[field]
            for field in ("type", "claim", "source_text")
        )
        and derived_signal["signal_id"] == f"{original_case['listing_id']}-S{index:02d}"
        for original_case, derived_case in zip(source, derived)
        for index, (original_signal, derived_signal) in enumerate(
            zip(original_case["signals"], derived_case["signals"]),
            start=1,
        )
    )

    print(f"Same case count: {same_case_count}")
    print(f"Same listings and Signal counts: {same_listings_and_counts}")
    print(f"Original Signal fields preserved and IDs deterministic: {fields_preserved}")
    print(f"VALID: {same_case_count and same_listings_and_counts and fields_preserved}")


if __name__ == "__main__":
    main()
