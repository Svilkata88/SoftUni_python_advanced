def search_the_matrix(n_targets, shooter_position):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == 'x':
                n_targets += 1
            elif matrix[r][c] == 'A':
                shooter_position = [r, c]
    return n_targets, shooter_position


matrix = [[x for x in input().split()] for el in range(5)]
shooter_position = [0,0]
targets_left = 0
targets_shotted = 0
targets_shotted_positions = []
targets_left, shooter_position = search_the_matrix(targets_left, shooter_position)
n_commands = int(input())
directions = {'right': [0, 1], 'left': [0, -1], 'up': [-1, 0], 'down': [1, 0]}

for _ in range(n_commands):
    command, *others = input().split()
    if command == 'move':
        if matrix[shooter_position[0]][shooter_position[1]] == 'A':
            matrix[shooter_position[0]][shooter_position[1]] = '.'
        direction, steps = others
        steps = int(steps)
        move_directions = {'right': [0, steps], 'left': [0, -steps], 'up': [-steps, 0], 'down': [steps, 0]}
        row, col = shooter_position
        new_row = row + move_directions[direction][0]
        new_col = col + move_directions[direction][1]
        if new_row not in range(5) or new_col not in range(5) or matrix[new_row][new_col] == 'x':
            continue
        shooter_position = [new_row, new_col]
    elif command == 'shoot':
        direction = others[0]
        row, col = shooter_position
        shot_row = row
        shot_col = col
        target_position = [0, 0]
        for _ in range(5):
            shot_row += directions[direction][0]
            shot_col += directions[direction][1]
            if shot_row not in range(5) or shot_col not in range(5):
                break
            elif matrix[shot_row][shot_col] == '.':
                continue
            elif matrix[shot_row][shot_col] == 'x':
                targets_left -= 1
                targets_shotted += 1
                matrix[shot_row][shot_col] = '.'
                targets_shotted_positions.append([shot_row, shot_col])
                break
    if targets_left == 0:
        print(f'Training completed! All {targets_shotted} targets hit.')
        break

if targets_left > 0:
    print(f'Training not completed! {targets_left} targets left.')
print(*targets_shotted_positions, sep='\n')

