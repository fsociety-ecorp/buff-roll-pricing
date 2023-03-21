import json

# Open the original JSON file
with open('buff.json', 'r', encoding='utf-8') as f:
    original_data = json.load(f)

# Transform the data
transformed_data = {}
for key, value in original_data.items():
    transformed_data[key] = {"id": value}

# Write the transformed JSON to a new file
with open('transformed.json', 'w', encoding='utf-8') as f:
    json.dump(transformed_data, f, indent=4)
