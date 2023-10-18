def find_start_position(playground_):
    position_ = None
    for row_ in range(rows):
        for col_ in range(cols):
            if playground_[row_][col_] == 'B':
                position_ = [row_, col_]
                return position_


def move(direction_, row_, col_):
    if direction_ == 'up':
        row_ -= 1
    elif direction_ == 'down':
        row_ += 1
    elif direction_ == 'left':
        col_ -= 1
    elif direction_ == 'right':
        col_ += 1
    return row_, col_


rows, cols = [int(el) for el in input().split()]
playground = [list(input().split()) for el in range(rows)]
position = find_start_position(playground)
moves_count = 0
players_touched = 0

direction = input()
while direction != 'Finish':
    row, col = position

    new_row, new_col = move(direction, row, col)
    if new_row in range(rows) and new_col in range(cols) and playground[new_row][new_col] != 'O':
        if playground[new_row][new_col] == '-':
            pass
        elif playground[new_row][new_col] == 'P':
            playground[new_row][new_col] = '-'
            players_touched += 1
            if players_touched == 3:
                moves_count += 1
                break
        moves_count += 1
        position = [new_row, new_col]
    direction = input()

print("Game over!")
print(f"Touched opponents: {players_touched} Moves made: {moves_count}")

#print(*playground, sep='\n')