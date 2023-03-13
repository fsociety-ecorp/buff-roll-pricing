import json

# Load the JSON data from file
with open('buff.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('0.64.txt', 'r', encoding='utf-8') as f:
    lines64 = f.read().splitlines()

with open('0.65.txt', 'r', encoding='utf-8') as f:
    lines65 = f.read().splitlines()

# Create a new dictionary with the desired format
new_data = {}
for key, value in data.items():
    if key in lines64:
        new_data[key] = {
            "id": value,
            "rate": "0.64"
        }
    elif key in lines65:
        new_data[key] = {
            "id": value,
            "rate": "0.65"
        }
    else:
        new_data[key] = {
            "id": value,
            "rate": "0.66"
        }

# Write the updated JSON data to file
with open('updated_data.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)
