import json

data = {
    "builds": [
        {"id": 101, "status": "success"},
        {"id": 102, "status": "failed"}
    ]
}

failed = [b["id"] for b in data.get("builds", []) if b.get("status") == "failed"]

print(failed)