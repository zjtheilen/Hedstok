import json
import sys

sys.path.insert(0, "experiment-0")

from discover import discover

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

discoveries = discover(extractions)

discoveries_by_id = {
    listing_id: []
    for listing_id in extractions_by_id
}

for discovery in discoveries:
    discoveries_by_id[discovery["listing_id"]].append(discovery)


for listing_id, expected_listing in expected_by_id.items():
    print(f"\n{'=' * 60}")
    print(listing_id)
    print(f"{'=' * 60}")

    print("\nEXPECTED SIGNALS:")
    for signal in expected_listing["expected_signals"]:
        print(f"  - {signal}")

    print("\nDISCOVERIES:")
    listing_discoveries = discoveries_by_id[listing_id]

    if not listing_discoveries:
        print("  (none)")
        continue

    for discovery in listing_discoveries:
        print(f"  - {discovery['reason']}")
        print(f"    Investigate: {discovery['investigate']}")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

discovered_ids = {
    discovery["listing_id"]
    for discovery in discoveries
}

print(f"\nListings with discoveries: {len(discovered_ids)}")
print(f"Listings without discoveries: {len(expected_by_id) - len(discovered_ids)}")

print("\nDISCOVERED:")
for listing_id in sorted(discovered_ids):
    print(f"  - {listing_id}")

print("\nNOT DISCOVERED:")
for listing_id in sorted(expected_by_id):
    if listing_id not in discovered_ids:
        print(f"  - {listing_id}")
