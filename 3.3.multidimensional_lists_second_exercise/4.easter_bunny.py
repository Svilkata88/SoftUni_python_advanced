n_size = int(input())
matrix = [[x for x in input().split()] for el in range(n_size)]

directions = [[-1, 0, 'up'], [+1, 0, 'down'], [0, -1, 'left'], [0, + 1, 'right']] # left, right, up, down

bunny = [0,0]
for row in range(n_size):
    for col in range(n_size):
        if matrix[row][col] == 'B':
            bunny = [row, col]

wining_direction = None
positions_direction = []
max_eggs = float('-inf')
for i in range(4):
    row, col = bunny
    current_eggs = 0
    current_positions = []
    for _ in range(n_size):
        row += directions[i][0]
        col += directions[i][1]
        if row not in range(n_size) or col not in range(n_size):
            break
        if matrix[row][col] != 'X':
            current_eggs += int(matrix[row][col])
            current_positions.append([row, col])
        else:
            break
    if current_eggs >= max_eggs:
        max_eggs = current_eggs
        positions_direction.clear()
        positions_direction.extend(current_positions)
        wining_direction = directions[i][2]

print(wining_direction)
print(*positions_direction, sep='\n')
print(max_eggs)