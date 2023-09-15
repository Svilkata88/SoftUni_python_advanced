from collections import deque

customers_name = input()
queue = deque()

while customers_name != 'End':
    if customers_name == 'Paid':
        while queue:
            print(queue.popleft())
    elif customers_name:
        queue.append(customers_name)

    customers_name = input()

print(f"{len(queue)} people remaining.")