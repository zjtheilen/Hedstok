import json


with open("experiment-0/output/extraction-baseline.json") as file:
    extractions = json.load(file)

with open("experiment-0/evaluation/expected-signals.json") as file:
    expected = json.load(file)


extractions_by_id = {
    listing["listing_id"]: listing
    for listing in extractions
}

expected_by_id = {
    listing["id"]: listing
    for listing in expected["listings"]
}


for listing_id, expected_listing in expected_by_id.items():
    print(f"\n{'=' * 60}")
    print(listing_id)
    print(f"{'=' * 60}")

    print("\nEXPECTED:")
    for signal in expected_listing["expected_signals"]:
        print(f"  - {signal}")

    print("\nEXTRACTED:")
    for signal in extractions_by_id[listing_id]["signals"]:
        print(f"  - [{signal['type']}] {signal['claim']}")
