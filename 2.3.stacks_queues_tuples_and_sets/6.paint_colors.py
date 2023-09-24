from collections import deque

string = deque(input().split())

main_colours = ["red", "yellow", "blue"]
secondary_colours = {"orange":['red', 'yellow'],
                     "purple":['red', 'blue'],
                     "green":['yellow', 'blue']
                     }
colors_finded = []

while string:
    first_string = string.popleft()
    last_string = string.pop() if string else ''

    if first_string + last_string in main_colours or first_string + last_string in secondary_colours:
        colors_finded.append(first_string + last_string)
    elif last_string + first_string in main_colours or last_string + first_string in secondary_colours:
        colors_finded.append(last_string + first_string)
    else:
        if len(first_string) > 1:
            string.insert(len(string) // 2, first_string[:-1])
        if len(last_string) > 1:
            string.insert(len(string) // 2, last_string[:-1])

for color in colors_finded:
    if color in main_colours:
        continue
    else:
        for el in secondary_colours[color]:
            if el not in colors_finded:
                colors_finded.remove(color)
                break



print(colors_finded)