def search_for_K():
    for row in range(n_size):
        for col in range(n_size):
            if ches_board[row][col] == 'K':
                knights_positions.append((row, col))


def K_possible_attacks(k_position):
    row, col = k_position
    attack_positions = {
    'up_left': [row-2, col-1],
    'up_right': [row-2, col+1],
    'left_up': [row-1,col-2],
    'left_down': [row+1, col-2],
    'right_up': [row-1, col+2],
    'right_down': [row+1, col+2],
    'down_left': [row+2, col-1],
    'down_right': [row+2, col+1]
    }
    for direction, coordinates in attack_positions.items():
        if coordinates[0] in range(n_size) and coordinates[1] in range(n_size) and \
                ches_board[coordinates[0]][coordinates[1]] == 'K':
            if k_position not in knights_number_of_targets:
                knights_number_of_targets[k_position] = [coordinates]
            else:
                knights_number_of_targets[k_position].append(coordinates)
    max_shots_knight = None
    max_len = 0
    for key, v in knights_number_of_targets.items():
        if len(v) > max_len:
            max_shots_knight = key
            max_len = len(v)
    return max_shots_knight


n_size = int(input())
ches_board = [[el for el in input()] for num in range(n_size)]
knights_positions = []
knights_number_of_targets = {}
knights_removed =0

while True:
    search_for_K() # searching for K's positions on the chess board
    position_max_shot_knight = None
    for position in knights_positions:
        position_max_shot_knight = K_possible_attacks(position) # finding every possible move for every K in the field
    if position_max_shot_knight is None:
        break
    ches_board[position_max_shot_knight[0]][position_max_shot_knight[1]] = '0'
    knights_positions.remove(position_max_shot_knight)
    knights_removed += 1
    knights_number_of_targets.clear()
    knights_positions.clear()

#print('\n'.join([' '.join([str(x) for x in el]) for el in ches_board]))
print(knights_removed)