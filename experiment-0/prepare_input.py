import json
from pathlib import Path

path = Path("experiment-0/input/listings.json")

with path.open() as f:
    data = json.load(f)

data["listings"] = [
    {
        "id": f"listing-{i:02d}",
        "description": description
    }
    for i, description in enumerate(data["listings"], start=1)
]

with path.open("w") as f:
    json.dump(data, f, indent=4)
    f.write("\n")