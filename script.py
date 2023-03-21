import json

# Open the original JSON file
with open('buff-all-items.json', 'r', encoding='utf-8') as f:
    original_data = json.load(f)

# Transform the data
transformed_data = {}
for key, value in original_data.items():
    transformed_data[key] = {"id": value}

# Open the file with rates
with open('62.txt', 'r', encoding='utf-8') as f:
    file_62 = set(f.read().splitlines())

with open('64.txt', 'r', encoding='utf-8') as f:
    file_64 = set(f.read().splitlines())

with open('65.txt', 'r', encoding='utf-8') as f:
    file_65 = set(f.read().splitlines())

# Update the transformed data with rates
for key, value in transformed_data.items():
    if key in file_65:
        value["rate"] = 0.65
    elif key in file_64:
        value["rate"] = 0.64
    elif key in file_62:
        value["rate"] = 0.62
    else:
        value["rate"] = 0.66

# Write the updated JSON to the same file
with open('transformed.json', 'w', encoding='utf-8') as f:
    json.dump(transformed_data, f, indent=4)
