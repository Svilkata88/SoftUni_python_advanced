def find_position(neighborhood_, position_):
    for row in range(rows):
        for col in range(cols):
            if neighborhood_[row][col] == 'B':
                position_ = (row, col)
    return position_


rows, cols = [int(el) for el in input().split()]
neighborhood = [list(input()) for row in range(rows)]
possible_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
position = (0, 0)
starting_position = find_position(neighborhood, position)
position = starting_position
out_of_the_hood = False

direction = input()
while direction:
    current_row, current_col = position
    new_row = current_row + possible_directions[direction][0]
    new_col = current_col + possible_directions[direction][1]

    if new_row not in range(rows) or new_col not in range(cols):
        neighborhood[current_row][current_col] = '.' if neighborhood[current_row][current_col] != 'R' else 'R'
        print('The delivery is late. Order is canceled.')
        out_of_the_hood = True
        break
    elif neighborhood[new_row][new_col] == 'P':
        neighborhood[current_row][current_col] = '.'
        neighborhood[new_row][new_col] = 'R'
        position = (new_row, new_col)
        print('Pizza is collected. 10 minutes for delivery.')
    elif neighborhood[new_row][new_col] == 'A':
        neighborhood[current_row][current_col] = '.' if neighborhood[current_row][current_col] != 'R' else 'R'
        neighborhood[new_row][new_col] = 'P'
        position = (new_row, new_col)
        print('Pizza is delivered on time! Next order...')
        break
    elif neighborhood[new_row][new_col] == '-' or neighborhood[new_row][new_col] == '.':
        neighborhood[new_row][new_col] = '.'
        neighborhood[current_row][current_col] = '.' if neighborhood[current_row][current_col] != 'R' else 'R'
        position = (new_row, new_col)
    elif neighborhood[new_row][new_col] == '*':
        pass
    direction = input()

neighborhood[starting_position[0]][starting_position[1]] = 'B'
if out_of_the_hood:
    neighborhood[starting_position[0]][starting_position[1]] = ' '


for row in neighborhood:
    print(''.join(row))
