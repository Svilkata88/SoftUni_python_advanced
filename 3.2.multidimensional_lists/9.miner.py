from collections import deque


def is_position_valid(command, position): # checking if new position is valid!
    row, col = position
    if possible_moves[command][0]+row in range(0, size) and possible_moves[command][1]+col in range(0, size):
        return True
    return False


def move(command, position): # starts to move and execute all the actions
    row, col = position
    if command == 'left':
        if is_position_valid(command, position):
            row += possible_moves[command][0]
            col += possible_moves[command][1]
    elif command == 'right':
        if is_position_valid(command, position):
            row += possible_moves[command][0]
            col += possible_moves[command][1]
    elif command == 'up':
        if is_position_valid(command, position):
            row += possible_moves[command][0]
            col += possible_moves[command][1]
    elif command == 'down':
        if is_position_valid(command, position):
            row += possible_moves[command][0]
            col += possible_moves[command][1]
    element = field[row][col]
    if element == 'c':
        global coals_in_the_field
        coals_in_the_field -= 1
        field[row][col] = '*'
    elif element == 'e':
        print(f'Game over! {(row, col)}')
        exit()
    position[0], position[1] = row, col
    return position


size = int(input())  # reads matrix side size
commands = deque(input().split())  # reading commands and putting it in deque ( to use popleft )
field = [[element for element in input().split()] for rows in range(size)] # reading matrix elements
possible_moves = {'left': [0, -1], # defining values needed for calculation when receive the command
                  'right': [0, 1],
                  'up': [-1, 0],
                  'down': [1, 0]
                  }

coals_in_the_field = 0
position = None

for row in range(size): # finding out position s and number of coils(c) in the field
    for col in range(size):
        element = field[row][col]
        if element == 'c':
            coals_in_the_field += 1
        if element == 's':
            position = [row, col]

while commands:  # starts to move te miner
    command = commands.popleft()
    move(command, position)
    if coals_in_the_field == 0:
        print(f'You collected all coal! {(position[0], position[1])}')

if not commands and coals_in_the_field > 0:  # if commands finishes and still coils in the field we print below text!
    print(f'{coals_in_the_field} pieces of coal left. {(position[0], position[1])}')
