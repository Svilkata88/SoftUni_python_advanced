matrix = [list(input().split()) for el in range(6)]
position = [int(x) for x in input() if x.isdigit()]
mapper_direction = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

commands = input()
while commands != 'Stop':
    command, *others = commands.split(', ')
    direction = others[0]
    position[0] += mapper_direction[direction][0]
    position[1] += mapper_direction[direction][1]
    row, col = position

    if command == 'Create':
        value = others[1]
        if matrix[row][col] == '.':
            matrix[row][col] = value
    elif command == 'Update':
        value = others[1]
        if matrix[row][col].isalnum():
            matrix[row][col] = value
    elif command == 'Delete':
        if matrix[row][col].isalnum():
            matrix[row][col] = '.'
    elif command == 'Read':
        if matrix[row][col].isalnum():
            print(matrix[row][col])

    commands = input()

print('\n'.join([' '.join([el for el in x]) for x in matrix]))
