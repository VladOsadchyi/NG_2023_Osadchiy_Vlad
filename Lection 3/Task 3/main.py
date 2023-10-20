import json
file_name = input("Enter the name of your JSON file or the way to it: ")
with open(file_name, 'r') as file:
        data = json.load(file)
your_key = input("Enter the name of key: ")
stack = [data]
found=None
while stack:
        current_data = stack.pop()
        if isinstance(current_data, dict):
            for key, val in current_data.items():
                    if key == your_key:
                        found = val
                        break
                    if isinstance(val, dict):
                        stack.append(val)
print(f"The value of key '{your_key}': {found}")
        