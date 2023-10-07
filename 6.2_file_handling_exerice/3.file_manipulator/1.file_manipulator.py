import os

while True:
    line = input()
    if line == 'End':
        break

    command, file_name, *args = line.split('-')

    if command == 'Create':
        file = open(file_name, 'w').close
    elif command == 'Add':
        try:
            with open(file_name, 'a') as f:
                f.write(f'{args[0]}\n')
        except FileNotFoundError:
            with open(file_name, 'w') as f:
                f.write(f'{args[0]}\n')
    elif command == 'Replace':
        try:
            with open(file_name, 'r') as file:
                data = file.read()
        except FileNotFoundError:
            print("An error occurred")
        else:
            with open(file_name, 'w') as file:
                data = data.replace(args[0], args[1])
                file.write(data)
    elif command == 'Delete':
        pass
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")