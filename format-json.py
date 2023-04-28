import json

with open('transformed.json', 'r', encoding='utf-8') as f:
    original_data = json.load(f)

new_data = {"items": []}

for name, item in original_data.items():
    new_data["items"].append(
        {"name": name, "id": item["id"], "rate": item["rate"]})

with open('new_transformed.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, indent=4)
