import json


def load_json(path: str):
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def evaluate_structure(
    extraction_path: str,
    listings_path: str,
) -> None:
    extraction = load_json(extraction_path)
    listings = load_json(listings_path)

    source_by_id = {
        listing["id"]: listing["description"]
        for listing in listings["listings"]
    }

    extraction_by_id = {
        listing["listing_id"]: listing
        for listing in extraction
    }

    print("STRUCTURAL EVALUATION")
    print("=====================")

    print(f"Source listings: {len(source_by_id)}")
    print(f"Extracted listings: {len(extraction_by_id)}")

    missing_listings = set(source_by_id) - set(extraction_by_id)
    unexpected_listings = set(extraction_by_id) - set(source_by_id)

    if missing_listings:
        print("\nMissing listings:")
        for listing_id in sorted(missing_listings):
            print(f"  - {listing_id}")
    else:
        print("All source listings were extracted.")

    if unexpected_listings:
        print("\nUnexpected listing IDs:")
        for listing_id in sorted(unexpected_listings):
            print(f"  - {listing_id}")

    invalid_source_text = []

    for listing_id, result in extraction_by_id.items():
        source_text = source_by_id.get(listing_id)

        if source_text is None:
            continue

        for signal in result["signals"]:
            if signal["source_text"] not in source_text:
                invalid_source_text.append(
                    (listing_id, signal["source_text"])
                )

    print()

    if invalid_source_text:
        print("Invalid source_text references:")
        for listing_id, source_text in invalid_source_text:
            print(f"  - {listing_id}: {source_text}")
    else:
        print("All source_text values were found exactly in the source listing.")

    total_signals = sum(
        len(result["signals"])
        for result in extraction_by_id.values()
    )

    print(f"\nTotal extracted signals: {total_signals}")


if __name__ == "__main__":
    evaluate_structure(
        "extraction.json",
        "experiment-0/input/listings.json",
    )
