from collections import deque

time_needed = deque([int(el) for el in input().split()])  # takes 1st
number_of_tasks = [int(el) for el in input().split()]  # takes last

ducks_given = []
ducky_mapper = {
    range(0, 60+1): 'Darth Vader Ducky',
    range(61, 120+1): 'Thor Ducky',
    range(121, 180+1): 'Big Blue Rubber Ducky',
    range(181, 240+1): 'Small Yellow Rubber Ducky'
}

while time_needed and number_of_tasks:
    current_time = time_needed.popleft()
    current_task = number_of_tasks.pop()
    result = current_task * current_time

    for el, duck_type in ducky_mapper.items():
        if result in el:
            ducks_given.append(duck_type)
        elif result > 240:
            current_task -= 2
            number_of_tasks.append(current_task)
            time_needed.append(current_time)
            break

print('Congratulations, all tasks have been completed! Rubber ducks rewarded:')
print(f"Darth Vader Ducky: {ducks_given.count('Darth Vader Ducky')}")
print(f"Thor Ducky: {ducks_given.count('Thor Ducky')}")
print(f"Big Blue Rubber Ducky: {ducks_given.count('Big Blue Rubber Ducky')}")
print(f"Small Yellow Rubber Ducky: {ducks_given.count('Small Yellow Rubber Ducky')}")
