import json
from pathlib import Path

EXPERIMENT_DIR = Path(__file__).parent
SOURCE_PATH = EXPERIMENT_DIR / "interpretation-cases.json"
OUTPUT_PATH = EXPERIMENT_DIR / "interpretation-cases-phase-4-8.json"


def main():
    with SOURCE_PATH.open(encoding="utf-8") as file:
        cases = json.load(file)

    derived_cases = []
    seen_ids = set()
    total_signals = 0

    for case in cases:
        listing_id = case["listing_id"]
        derived_signals = []

        for index, signal in enumerate(case["signals"], start=1):
            signal_id = f"{listing_id}-S{index:02d}"

            if signal_id in seen_ids:
                raise ValueError(f"Duplicate Signal ID: {signal_id}")

            seen_ids.add(signal_id)
            derived_signals.append(
                {
                    "signal_id": signal_id,
                    "type": signal["type"],
                    "claim": signal["claim"],
                    "source_text": signal["source_text"],
                }
            )
            total_signals += 1

        derived_cases.append(
            {
                "listing_id": listing_id,
                "signals": derived_signals,
            }
        )

    with OUTPUT_PATH.open("w", encoding="utf-8") as file:
        json.dump(derived_cases, file, indent=2, ensure_ascii=False)
        file.write("\n")

    print(f"Cases: {len(derived_cases)}")
    print(f"Signals: {total_signals}")
    print(f"Unique Signal IDs: {len(seen_ids)}")
    print(f"Output: {OUTPUT_PATH.name}")


if __name__ == "__main__":
    main()
