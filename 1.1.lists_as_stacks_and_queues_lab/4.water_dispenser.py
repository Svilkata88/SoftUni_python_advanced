from collections import deque
queue = deque()

water_q = int(input())

people_wanting_water = input()

while people_wanting_water != 'Start':
    queue.append(people_wanting_water)
    people_wanting_water = input()

litters_wanted = input()

while litters_wanted != 'End':
    command = litters_wanted.split()
    if command[0] == 'refill':
        litters = int(command[1])
        water_q += litters
    else:
        litters = int(command[0])
        if litters <= water_q:
            print(f'{queue.popleft()} got water')
            water_q -= litters
        else:
            print(f'{queue.popleft()} must wait')

    litters_wanted = input()

print(f'{water_q} liters left')

