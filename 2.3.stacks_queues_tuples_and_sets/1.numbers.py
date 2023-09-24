numbers_1 = set(int(num) for num in input().split())
numbers_2 = set(int(num) for num in input().split())
n_commands = int(input())

for _ in range(n_commands):
    command_info = input().split()
    command = command_info[0] + ' ' + command_info[1]
    numbers = [int(num) for num in command_info[2:]]
    if command == 'Add First':
        numbers_1.update(numbers)

    elif command == 'Add Second':
        numbers_2.update(numbers)

    elif command == 'Remove First':
        numbers = [int(num) for num in numbers]
        numbers_1 = numbers_1.difference(numbers)

    elif command == 'Remove Second':
        numbers = [int(num) for num in numbers]
        numbers_2 = numbers_2.difference(numbers)

    elif command == 'Check Subset':
        print(numbers_1.issubset(numbers_2) or numbers_2.issubset(numbers_1))

print(*sorted(numbers_1), sep=', ')
print(*sorted(numbers_2), sep=', ')