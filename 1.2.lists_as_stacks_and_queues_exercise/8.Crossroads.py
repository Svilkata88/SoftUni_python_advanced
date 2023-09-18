from collections import deque

green_light_time = int(input())
additional_time = int(input())
total_free_time = green_light_time + additional_time
car_passed_counter = 0
crossroad_entering_time_remaining = 0
waiting_cars = deque()
crash = False

command = input()

while command != 'END' and not crash:
    if command == 'green':
        g_time = green_light_time
        f_time = total_free_time
        t_time = total_free_time
        # car starts to go in the crossroad till time becomes 0
        while g_time > 0:
            if waiting_cars:# avoiding pop from empty deque error
                car_crossing = waiting_cars.popleft()
            else:
                break
            # checking if 1st car can pass!
            if t_time < len(car_crossing):
                hit_char = t_time
                print('A crash happened!')
                print(f"{car_crossing} was hit at {car_crossing[hit_char]}.")
                crash = True
                break
            # checking if car passing can go through the green light window
            elif g_time >= len(car_crossing):
                g_time -= len(car_crossing)
                t_time -= len(car_crossing)
                car_passed_counter += 1
            # checking if the car in the crossroad can pass but no other car can go in the crossroad
            elif g_time < len(car_crossing) <= t_time:
                g_time = 0
                car_passed_counter += 1
    else:
        waiting_cars.append(command)

    command = input()

# if there was no crash we print the output
if not crash:
    print('Everyone is safe.')
    print(f'{car_passed_counter} total cars passed the crossroads.')