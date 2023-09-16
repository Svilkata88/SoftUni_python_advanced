from collections import deque

quantity = int(input())
orders = deque([int(order) for order in input().split()])

print(max(orders))
while orders and orders[0] <= quantity:
    quantity -= orders[0]
    orders.popleft()

if orders:
    print(f'Orders left:', end='')
    while orders:
        print(f' {orders.popleft()}', end='')
else:
    print('Orders complete')