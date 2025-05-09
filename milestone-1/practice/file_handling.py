import os

print(os.getcwd())

# Get current working directory
wd = os.getcwd()
# Creating file in a specific folder

try:
    with open(f'{wd}/sample_text.txt', 'w') as file:
        file.write('Python is fun. I think am in love with it.\n')
        file.write('Till the end of times.')

    with open(f'{wd}/sample_text.txt', 'r') as file:
        content = file.read() # Read the entire content.
        print(content)
except FileNotFoundError:
    print(f'Error: file {wd} not found.')
except PermissionError:
    print(f'Error: No permissions to access {wd}')
except Exception as e:
    print(f'An unexpected error occurred {e}.')