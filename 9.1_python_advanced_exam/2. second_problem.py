#  Fishing Competition
def find_pos(fishing_area_, starting_position_):
    for r in range(size):
        for c in range(size):
            if fishing_area_[r][c] == 'S':
                position_ = [r, c]
    return position_


def move(position_, direction_):
    if direction_ == 'up':
        position_[0] -= 1
    elif direction_ == 'down':
        position_[0] += 1
    elif direction_ == 'left':
        position_[1] -= 1
    elif direction_ == 'right':
        position_[1] += 1
    return position_


def opposite_direction(position_, direction_):
    if direction_ == 'up':
        position_[0] = size-1
    elif direction_ == 'down':
        position_[0] = 0
    elif direction_ == 'left':
        position_[1] = size-1
    elif direction_ == 'right':
        position_[1] = 0
    return position_


size = int(input())
fishing_area = [list(input()) for _ in range(size)]
position = None
position = find_pos(fishing_area, position)
fish_count = 0

direction = input()
while direction != "collect the nets":
    fishing_area[position[0]][position[1]] = '-'
    row, col = move(position, direction)
    position = [row, col]

    if row not in range(size) or col not in range(size):
        position = opposite_direction(position, direction)
        row, col = position

    if fishing_area[row][col] == 'W':
        fish_count = 0
        print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught. '
              f'Last coordinates of the ship: [{row},{col}]')
        exit()

    if fishing_area[row][col].isdigit():
        fish_count += int(fishing_area[row][col])
        fishing_area[row][col] = 'S'
    else:
        fishing_area[row][col] = 'S'

    direction = input()

if fish_count >= 20:
    print('Success! You managed to reach the quota!')
else:
    print(f"You didn\'t catch enough fish and didn\'t reach the quota! You need {20-fish_count} tons of fish more.")
if fish_count > 0:
    print(f'Amount of fish caught: {fish_count} tons.')
print('\n'.join([''.join([el for el in x]) for x in fishing_area]))
