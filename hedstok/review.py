import json


def load_json(path: str):
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def build_review(
    extraction_path: str,
    comparison_path: str,
    expected_path: str,
) -> None:
    extraction = load_json(extraction_path)
    comparison = load_json(comparison_path)
    expected = load_json(expected_path)

    extraction_by_id = {listing["listing_id"]: listing for listing in extraction}

    comparison_by_id = {
        listing["listing_id"]: listing
        for listing in comparison
    }

    expected_by_id = {listing["id"]: listing for listing in expected["listings"]}

    print("SEMANTIC EXTRACTION REVIEW")
    print("==========================")

    for listing_id in expected_by_id:
        print(f"\n{listing_id}")
        print("-" * len(listing_id))

        print("\n14-call extraction:")

        result = extraction_by_id.get(listing_id)

        if result is None:
            print("  <no extraction>")
        elif not result["signals"]:
            print("  <no signals>")
        else:
            for signal in result["signals"]:
                print(f"  - [{signal['type']}] {signal['claim']}")
                print(f"    source: {signal['source_text']}")

        print("\n1-call batch extraction:")

        result = comparison_by_id.get(listing_id)

        if result is None:
            print("  <no extraction>")
        elif not result["signals"]:
            print("  <no signals>")
        else:
            for signal in result["signals"]:
                print(f"  - [{signal['type']}] {signal['claim']}")
                print(f"    source: {signal['source_text']}")


if __name__ == "__main__":
    build_review(
        "extraction.json",
        "extraction2.json",
        "experiment-0/evaluation/expected-signals.json",
    )
