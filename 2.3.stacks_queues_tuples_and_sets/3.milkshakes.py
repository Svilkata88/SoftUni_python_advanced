from collections import deque
milkshakes = 0

chocolates = deque([int(num) for num in input().split(', ')])
cups_of_milk = deque([int(num) for num in input().split(', ')])

while chocolates and cups_of_milk and milkshakes < 5:
    if chocolates[-1] <=0 and cups_of_milk[0] <= 0:
        chocolates.pop()
        cups_of_milk.popleft()
        continue
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue
    elif cups_of_milk[0] == chocolates[-1]:
        removed_chocolate = chocolates.pop()
        removed_cup_milk = cups_of_milk.popleft()
        milkshakes += 1
    else:
        cups_of_milk.rotate(-1)
        chocolates[-1] -= 5

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if chocolates:
    print(f'Chocolate:', end=' ')
    print(*chocolates, sep=', ')
else:
    print('Chocolate: empty')
if cups_of_milk:
    print(f'Milk:', end=' ')
    print(*cups_of_milk, sep=', ')
else:
    print('Milk: empty')