class InvalidColumn(Exception):
    pass


def player_turn(player_):
    player_ = 1 if player_ == 2 else 2
    return player_


def validation_column_input(board_, player_):
    while True:
        try:
            column_ = int(input())
            if column_ < 1 or column_ > 7:
                raise ValueError
            if board_[0][column_-1] != 0:
                raise InvalidColumn
            return column_
        except ValueError:
            print('Please enter valid number [1-7]')
            continue
        except InvalidColumn:
            print('Please choose another column! This one is full.')
            continue


def play(board_, column_, player_):
    for row in range(len(board_)):
        for col in range(column_ - 1, column_):
            if row+1 in range(len(board_)):
                if board_[row + 1][column_ - 1] != 0:
                    board_[row][column_ - 1] = player_
                    position_ = (row, column_-1)
                    return board_, position_
            else:
                board_[row][column_ - 1] = player_
                position_ = (row, column_ - 1)
                return board_, position_


def is_horizontal_win(position_, board_):
    row, col = position_
    counter = 0
    for i in range(col, 7):
        if board_[row][i] == player:
            counter += 1
        else:
            break
    for i in range(col-1, -1, -1):
        if board_[row][i] == player:
            counter += 1
        else:
            break
    if counter >= 4:
        return True
    return False


def is_vertical_win(position_, board_):
    row, col = position_
    counter = 0
    for i in range(row, len(board_)):
        if board_[i][col] == player:
            counter += 1
        else:
            break
    for i in range(row-1, -1, -1):
        if board_[i][col] == player:
            counter += 1
        else:
            break
    if counter >= 4:
        return True
    return False


def is_diagonal_1_win(position_, board_):
    row, col = position_
    counter = 0
    i = 0
    while row-i in range(len(board_)) and col+i in range(7):
        if board_[row - i][col + i] == player:
            counter += 1
            i += 1
        else:
            break
    i = 1
    while row+i in range(len(board_)) and col-i in range(7):
        if board_[row+i][col-i] == player:
            counter += 1
            i += 1
        else:
            break
    if counter >= 4:
        return True
    return False


def is_diagonal_2_win(position_, board_):
    row, col = position_
    counter = 0
    i = 0
    while row - i in range(len(board_)) and col - i in range(7):
        if board_[row - i][col - i] == player:
            counter += 1
            i += 1
        else:
            break
    i = 1
    while row + i in range(len(board_)) and col + i in range(7):
        if board_[row + i][col + i] == player:
            counter += 1
            i += 1
        else:
            break
    if counter >= 4:
        return True
    return False


def is_win():
    if is_horizontal_win(position, board) or \
            is_vertical_win(position, board) or \
            is_diagonal_1_win(position, board) or \
            is_diagonal_2_win(position, board):
        return True
    return False


board = [[0] * 7 for el in range(6)]
player = 1

while True:
    print(f'Player {player} please chose a column')
    column = validation_column_input(board, player)  # read the input for the column and validate it!
    board, position = play(board, column, player)
    if is_win():
        print(*board, sep='\n')  # print the board
        print(f'Player {player} WON!')
        break
    player = player_turn(player)  # change player

    print(*board, sep='\n')  # print the board
