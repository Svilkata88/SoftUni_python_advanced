from collections import deque

cups = deque([int(ch) for ch in input().split()])
bottles = [int(ch) for ch in input().split()]
wasted_water = 0

while cups:
    if not bottles:
        break
    removed_bottle = bottles.pop()
    filling_cup = cups.popleft()

    while filling_cup > 0:
        if removed_bottle >= filling_cup:
            removed_bottle -= filling_cup
            wasted_water += removed_bottle
            filling_cup = 0
        else:
            filling_cup -= removed_bottle
            removed_bottle = bottles.pop()

if not cups:
    print(f'Bottles: ', end='')
    print(*bottles, sep=' ')
    print(f'Wasted litters of water: {wasted_water}')
elif not bottles:
    print(f'Cups: ', end='')
    print(*cups, sep=' ')
    print(f'Wasted litters of water: {wasted_water}')