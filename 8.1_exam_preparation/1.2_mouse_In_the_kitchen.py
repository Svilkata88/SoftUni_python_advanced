def mouse_pos_check(cupboard_, cheese_count_, mouse_pos):
    for r in range(rows):
        for c in range(cols):
            if cupboard_[r][c] == 'C':
                cheese_count_ += 1
            elif cupboard_[r][c] == 'M':
                mouse_pos = (r, c)
    return cheese_count_, mouse_pos


rows, cols = [int(n) for n in input().split(',')]
cupboard = [list(input()) for row in range(rows)]
possible_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
cheese_count = 0
mouse_position = (0, 0)
cheese_count, mouse_position = mouse_pos_check(cupboard, cheese_count, mouse_position)

direction = input()
while direction != 'danger':
    row, col = mouse_position
    new_row = row + possible_directions[direction][0]
    new_col = col + possible_directions[direction][1]
    if new_row not in range(rows) or new_col not in range(cols):
        print('No more cheese for tonight!')
        break
    if cupboard[new_row][new_col] == 'C':
        cupboard[row][col] = '*'
        cupboard[new_row][new_col] = 'M'
        cheese_count -= 1
        mouse_position = (new_row, new_col)
        if cheese_count == 0:
            print('Happy mouse! All the cheese is eaten, good night!')
            break
    elif cupboard[new_row][new_col] == 'T':
        cupboard[row][col] = '*'
        cupboard[new_row][new_col] = 'M'
        mouse_position = (new_row, new_col)
        print('Mouse is trapped!')
        break
    elif cupboard[new_row][new_col] == '*':
        cupboard[row][col] = '*'
        cupboard[new_row][new_col] = 'M'
        mouse_position = (new_row, new_col)
    elif cupboard[new_row][new_col] == '@':
        pass
    direction = input()
else:
    print('Mouse will come back later!')

for row in cupboard:
    print(''.join(row))

