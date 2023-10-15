from collections import deque

monsters = deque([int(m) for m in input().split(',')])  # each el represent monster armor / take 1st monster - use deque
soldiers = [int(s) for s in input().split(',')]  # each int represent soldier attack / take last soldier
total_monsters_kills = 0

while monsters and soldiers:
    current_monster = monsters.popleft()
    current_soldier = soldiers.pop()
    if current_soldier >= current_monster:
        current_soldier -= current_monster  # current soldier can be 0 after the impact!
        total_monsters_kills += 1
        if soldiers:
            soldiers[-1] += current_soldier
        else:
            soldiers.append(current_soldier) if current_soldier > 0 else ''
    else:
        current_monster -= current_soldier
        monsters.append(current_monster)

if not monsters:
    print('All monsters have been killed!')
if not soldiers:
    print( 'The soldier has been defeated.')
print(f'Total monsters killed: {total_monsters_kills}')
