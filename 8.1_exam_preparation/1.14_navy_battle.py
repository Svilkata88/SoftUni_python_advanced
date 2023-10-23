
class Submarine:
    cruisers = 3

    def __init__(self):
        self.health = 3
        self.position_ = submarine_start_position(battleground)

    def move(self, direction_):
        # return submarine new position on the battlefield!
        if direction_ == 'up':
            self.position_[0] -= 1
        elif direction_ == 'down':
            self.position_[0] += 1
        elif direction_ == 'left':
            self.position_[1] -= 1
        elif direction_ == 'right':
            self.position_[1] += 1

    def take_dmg(self):
        self.health -= 1

    def last_position(self, direction_):
        # return submarine old position on the battlefield!
        if direction_ == 'up':
            position[0] -= 1
        elif direction_ == 'down':
            position[0] += 1
        elif direction_ == 'left':
            position[1] -= 1
        elif direction_ == 'right':
            position[1] += 1
        return position


def submarine_start_position(battleground_):
    for r in range(size):
        for c in range(size):
            if battleground_[r][c] == 'S':
                return [r, c]


def check_new_position(position_, direction_):
    result = False
    if direction_ == 'up':
        position_[0] -= 1
        if position_[0] in range(size):
            result = True
    elif direction_ == 'down':
        position_[0] += 1
        if position_[0] in range(size):
            result = True
    elif direction_ == 'left':
        position_[1] -= 1
        if position_[1] in range(size):
            result = True
    elif direction_ == 'right':
        position_[1] += 1
        if position_[1] in range(size):
            result = True
    return result  # w  # ne
# not necessary to check but is written anyway.


size = int(input())
battleground = [list(input()) for _ in range(size)]
position = submarine_start_position(battleground)
u_9 = Submarine()


direction = input()
while direction:
    u_9.move(direction)
    new_position = battleground[u_9.position_[0]][u_9.position_[1]]
    if new_position == '-':
        battleground[u_9.position_[0]][u_9.position_[1]] = 'S'
        pass
    elif new_position == '*':
        u_9.take_dmg()
        battleground[u_9.position_[0]][u_9.position_[1]] = 'S'
        if u_9.health == 0:
            print(f'Mission failed, U-9 disappeared! Last known coordinates [{u_9.position_[0]}, {u_9.position_[1]}]!')
            battleground[position[0]][position[1]] = '-'
            break
    elif new_position == 'C':
        Submarine.cruisers -= 1
        battleground[u_9.position_[0]][u_9.position_[1]] = 'S'
        if Submarine.cruisers == 0:
            print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
            battleground[position[0]][position[1]] = '-'
            break
    battleground[position[0]][position[1]] = '-'
    position = u_9.last_position(direction)
    direction = input()

print('\n'.join([''.join([el for el in ch]) for ch in battleground]))
