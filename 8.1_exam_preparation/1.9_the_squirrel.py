size = int(input())
directions = input().split(', ')
field = [list(input()) for el in range(size)]
s_position = [0, 0]
hazelnuts = 0


for row in range(size):
    for col in range(size):
        if field[row][col] == 's':
            s_position[0], s_position[1] = row, col

for direction in directions:
    if direction == 'up':
        s_position[0] -= 1
    elif direction == 'down':
        s_position[0] += 1
    elif direction == 'right':
        s_position[1] += 1
    elif direction == 'left':
        s_position[1] -= 1

    if not (0 <= s_position[0] < size and 0 <= s_position[1] < size):
        print('The squirrel is out of the field.')
        break
    row = s_position[0]
    col = s_position[1]

    if field[row][col] == 'h':
        hazelnuts += 1
        field[row][col] = '*'
        if hazelnuts == 3:
            print('Good job! You have collected all hazelnuts!')
            break
    elif field[row][col] == 't':
        print('Unfortunately, the squirrel stepped on a trap...')
        field[row][col] = '*'
        break
    elif field[row][col] == '*':
        pass
else:
    print('There are more hazelnuts to collect.')
print(f'Hazelnuts collected: {hazelnuts}')

