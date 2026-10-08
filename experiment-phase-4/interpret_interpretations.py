import json
from pathlib import Path

INPUT_PATH = Path(__file__).parent / "interpretation-cases.json"


def load_cases():
    with INPUT_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def interpret(case):
    signals = case["signals"]

    stories = [signal for signal in signals if signal["type"] == "story"]

    configurations = [signal for signal in signals if signal["type"] == "configuration"]

    identity = [signal for signal in signals if signal["type"] == "identity"]

    seller_context = [
        signal for signal in signals if signal["type"] == "seller_context"
    ]

    reasons = []

    if stories:
        reasons.append(
            "The listing contains personal, historical, or provenance-related details."
        )

    if configurations:
        reasons.append(
            "The instrument has configuration or physical characteristics that may make it distinctive."
        )

    if identity:
        reasons.append("The listing provides specific instrument identity information.")

    if seller_context:
        reasons.append("The seller context may add useful acquisition context.")

    if not reasons:
        reasons.append(
            "The available evidence does not provide an obvious reason to look closer."
        )

    return {
        "listing_id": case["listing_id"],
        "reasons": reasons,
        "supporting_signals": [signal["claim"] for signal in signals],
    }


def main():
    cases = load_cases()

    for case in cases:
        result = interpret(case)

        print(f"\n{result['listing_id']}")
        print("-" * len(result["listing_id"]))

        print("Reasons:")
        for reason in result["reasons"]:
            print(f"- {reason}")

        print("Supporting signals:")
        for signal in result["supporting_signals"]:
            print(f"- {signal}")


if __name__ == "__main__":
    main()
