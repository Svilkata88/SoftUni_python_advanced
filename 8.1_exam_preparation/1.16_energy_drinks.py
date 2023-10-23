from collections import deque

milligrams_of_caffeine = list(map(int, input().split(', ')))  # take last caffeine
energy_drinks = deque(list(map(int, input().split(', '))))  # take first energy
max_caffeine = 300

while milligrams_of_caffeine and energy_drinks:
    current_caffeine = milligrams_of_caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    current_result = current_caffeine * current_energy_drink
    if current_result <= max_caffeine:
        max_caffeine -= current_result
    else:
        energy_drinks.append(current_energy_drink)
        max_caffeine += 30
        if max_caffeine > 300:
            max_caffeine = 300

if energy_drinks:
    print(f'Drinks left: {", ".join([str(x) for x in energy_drinks])}')
else:
    print('At least Stamat wasn\'t exceeding the maximum caffeine.')
print(f'Stamat is going to sleep with {300-max_caffeine} mg caffeine.')