import os

# Specify the directory you want to list
directory = 'C:/Users/Anike/Documents'  # Replace with your actual path

# List the contents of the directory
try:
    contents = os.listdir(directory)  # No extra indentation here
    print(f"Contents of '{directory}':")
    for item in contents:  # This is indented correctly
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory}' does not exist.")
except PermissionError:
    print(f"You do not have permission to access '{directory}'.")
