from collections import deque

bullet_price = int(input())
barrel = int(input())
bullets = deque(int(bullet) for bullet in input().split())
locks = deque(int(bullet) for bullet in input().split())
intelligence_value = int(input())

# checking if bullets are less than barrel size
if len(bullets) < barrel:
    barrel = len(bullets)
current_barrel_level = barrel

while locks:
    if current_barrel_level == 0: # if barrel is empty reload (if we have bullets we reload with the Q we have)
        print('Reloading!')
        current_barrel_level = barrel if len(bullets) > barrel else len(bullets)
    if bullets:
        bullet = bullets.pop() # shooting
        intelligence_value -= bullet_price
        current_barrel_level -= 1 # minus one bullet in the barrel
    else:
        break
    if bullet <= locks[0]:
        print('Bang!')
        locks.popleft()
    else:
        print('Ping!')

if not locks:
    print(f'"{len(bullets)} bullets left. Earned ${intelligence_value}')
else:
    print(f'Couldn\'t get through. Locks left: {len(locks)}')