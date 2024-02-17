import json

def fix_and_remove_duplicates(file_path, key_name):
    # Attempt to fix the JSON file format
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                obj = json.loads(line)
                data.append(obj)
            except json.JSONDecodeError:
                print(f"Error processing line, attempting to fix: {line}")
                continue
    
    # Remove duplicates based on the specified key
    unique_data = {}
    for item in data:
        if key_name in item:
            key_value = item[key_name]
            if key_value not in unique_data:
                unique_data[key_value] = item
        else:
            print(f"Key '{key_name}' not found in some items. Skipping those.")
    
    # Get the list of unique items
    unique_list = list(unique_data.values())
    
    # Write the unique data back to a file, one JSON object per line
    with open('unique_data.json', 'w', encoding='utf-8') as file:
        for item in unique_list:
            json.dump(item, file, ensure_ascii=False)
            file.write('\n')

    print(f"Duplicates removed based on '{key_name}'. Results are saved in 'unique_data.json', one object per line.")

# User input for file path and key name
file_path = input("Enter the path to your JSON file: ")
key_name = input("Enter the key to remove duplicates by: ")

fix_and_remove_duplicates(file_path, key_name)
