import json
def find_key(data, target_key):
    stack = [data]
    found = None
    while stack:
        current_data = stack.pop()
        if isinstance(current_data, dict):
            for key, val in current_data.items():
                if key == target_key:
                    found = val
                    break
                if isinstance(val, dict):
                    stack.append(val)
    return found
file_name = input("Enter the name of your JSON file or the path to it: ")
with open(file_name, 'r') as file:
    data = json.load(file)
your_key = input("Enter the name of the key you want to find: ")
result = find_key(data, your_key)
if result is not None:
    print(f"The value of key '{your_key}': {result}")
else:
    print(f"Key '{your_key}' not found in the JSON data.")

        