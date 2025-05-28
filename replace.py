#!/usr/bin/env python3

# Goal: Search for a line in a file and modify it in-place
# Example: Replace "Transition=False" with "Transition=True"

file_path = input("Enter the path to the file: ").strip()
search_line = "Transition=False"
replace_line = "Transition=True"

try:
    # Read all lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Replace matching line
    modified = False
    for i in range(len(lines)):
        if search_line in lines[i]:
            lines[i] = lines[i].replace(search_line, replace_line)
            modified = True

    # Write back if modified
    if modified:
        with open(file_path, 'w') as file:
            file.writelines(lines)
        print(f"Line updated: '{search_line}' → '{replace_line}'")
    else:
        print(f"No line containing '{search_line}' found.")

except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied — try running with sudo if needed.")
