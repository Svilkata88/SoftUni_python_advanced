from collections import deque

seats = [x for x in input().split(', ')]
first_numbers = deque(list(map(int, input().split(', '))))  # take first number
second_numbers = deque(list(map(int, input().split(', '))))  # take second number
taken_seats = []
rotations = 0

while True:
    if len(taken_seats) == 3 or rotations == 10:
        break

    current_first = first_numbers.popleft()
    current_second = second_numbers.pop()
    sum_nums = current_first + current_second

    current_char = chr(sum_nums)
    current_first_plus_char_result = str(current_first) + current_char
    current_second_plus_char_result = str(current_second) + current_char

    if current_first_plus_char_result in seats and current_first_plus_char_result not in taken_seats:
        taken_seats.append(current_first_plus_char_result)
    elif current_second_plus_char_result in seats and current_second_plus_char_result not in taken_seats:
        taken_seats.append(current_second_plus_char_result)
    else:
        first_numbers.append(current_first)
        second_numbers.appendleft(current_second)
    rotations += 1

print(f'Seat matches: {", ".join(taken_seats)}')
print(f'Rotations count: {rotations}')
