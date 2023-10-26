#  01. Offroad Challenge
from collections import deque

initial_fuel = list(map(int, input().split()))  # take last fuel
additional_consumption_index = deque(list(map(int, input().split())))  # take first index
amount_of_fuel_needed = deque(list(map(int, input().split())))
attitudes_count = len(amount_of_fuel_needed)
attitudes = []

while initial_fuel and additional_consumption_index and amount_of_fuel_needed:
    last_fuel = initial_fuel.pop()
    first_index = additional_consumption_index.popleft()

    result = last_fuel - first_index
    if result >= amount_of_fuel_needed[0]:
        attitudes.append(amount_of_fuel_needed.popleft())
        print(f'John has reached: Altitude {len(attitudes)}')
    else:
        print(f'John did not reach: Altitude {len(attitudes)+1}')
        break

if amount_of_fuel_needed and attitudes:
    print('John failed to reach the top.')
    print(f'Reached altitudes: ', end='')
    result = []
    for i in range(1, len(attitudes) + 1):
        result.append(f'Altitude {i}')
    print(*result, sep=', ')
elif amount_of_fuel_needed and not attitudes:
    print("John failed to reach the top.\n John didn't reach any altitude.")
elif not amount_of_fuel_needed:
    print(f'John has reached all the altitudes and managed to reach the top!')
