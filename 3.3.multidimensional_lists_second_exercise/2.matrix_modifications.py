n_size = int(input())
matrix = [[int(el) for el in input().split()] for num in range(n_size)]

commands = input()
while commands != 'END':
    command, *others = commands.split()
    row, col, value = others
    row = int(row)
    col = int(col)
    value = int(value)
    if command == 'Add':
        if row in range(0, n_size) and col in range(0, n_size):
            matrix[row][col] += value
        else:
            print('Invalid coordinates')
    elif command == 'Subtract':
        if row in range(0, n_size) and col in range(0, n_size):
            matrix[row][col] -= value
        else:
            print('Invalid coordinates')
    commands = input()

print('\n'.join([' '.join([str(x) for x in el]) for el in matrix]))