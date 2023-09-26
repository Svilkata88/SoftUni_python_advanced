from collections import deque


def search_for_b(r,c):
    for row in range(r):
        for col in range(c):
            if lair[row][col] == 'P':
                player_position[0], player_position[1] = row, col
            elif lair[row][col] == 'B':
                list_b_pos.append([row, col])


def bunny_spread(b_position):
    row, col = b_position
    if row - 1 in range(r) and col in range(c):  # up cell
        lair[row - 1][col] = 'B'
    if row in range(r) and col - 1 in range(c):  # left cell
        lair[row][col - 1] = 'B'
    if row in range(r) and col + 1 in range(c):  # right cell
        lair[row][col + 1] = 'B'
    if row + 1 in range(r) and col in range(c):  # down cell
        lair[row+1][col] = 'B'


def player_moves(player_position, direction):
    row, col = player_position
    new_row = possible_moves[direction][0]+row
    new_col = possible_moves[direction][1]+col
    if new_row not in range(r) or new_col not in range(c):
        if lair[row][col] != 'B':
            lair[row][col] = '.'
        print('\n'.join([''.join([el for el in x]) for x in lair]))
        print(f'won: {row} {col}')
        exit()
    elif lair[new_row][new_col] == 'B':
        if lair[row][col] != 'B':
            lair[row][col] = '.'
        print('\n'.join([''.join([el for el in x]) for x in lair]))
        print(f'dead: {new_row} {new_col}')
        exit()
    else:
        if lair[row][col] != 'B':
            lair[row][col] = '.'
            lair[new_row][new_col] = 'P'
        else:
            lair[new_row][new_col] = 'P'
    player_position = [new_row, new_col]


r, c = [int(el) for el in input().split()]
lair = [[x for x in input()] for el in range(r)]
moves = deque([ch for ch in input()])
list_b_pos = deque([])
player_position = [0, 0]
possible_moves = {'L': [0, -1], # defining values needed for calculation when receive the command
                  'R': [0, 1],
                  'U': [-1, 0],
                  'D': [1, 0]
                  }

search_for_b(r, c)

counter = 0
while moves:
    for position in list_b_pos:
        bunny_spread(position)
    list_b_pos.clear()
    player_moves(player_position, moves.popleft())
    search_for_b(r,c)

