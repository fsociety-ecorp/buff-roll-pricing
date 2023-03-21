# Open the first file and read its contents
with open('64.txt', 'r', encoding='utf-8') as f:
    file1_contents = set(f.read().splitlines())

# Open the second file and read its contents
with open('65.txt', 'r', encoding='utf-8') as f:
    file2_contents = set(f.read().splitlines())

# Find the intersection of the two sets (i.e., the duplicates)
duplicates = file1_contents.intersection(file2_contents)

# Print the duplicates
if duplicates:
    print("Duplicates found:")
    for duplicate in duplicates:
        print(duplicate)
else:
    print("No duplicates found.")
