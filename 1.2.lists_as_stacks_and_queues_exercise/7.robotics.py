from collections import deque

robots = input().split(';')
starting_time = input().split(':')
starting_time = f'{int(starting_time[0]):02d}:{starting_time[1]}:{starting_time[2]}'


robots_info = {}
products = deque()
end_products = False


def time(current_time):
    hour, min, sec = current_time.split(':')
    sec = int(sec)
    min = int(min)
    hour = int(hour)
    if sec + 1 == 60:
        sec = 0
        min += 1
        if min == 60:
            min = 0
            hour += 1
            if hour == 24:
                sec = 0
                min = 0
                hour = 0
    else:
        sec += 1
    result_time = f'{hour:02d}:{min:02d}:{sec:02d}'
    return result_time


def robot_time_when_free(current_time, processing_time):
    hour, minute, sec = current_time.split(':')
    sec = int(sec)
    minute = int(minute)
    hour = int(hour)
    if sec + processing_time >= 60:
        sec = sec + processing_time - 60
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
            if hour == 24:
                hour = 0
    else:
        sec += processing_time
    result_time = f'{hour:02d}:{minute:02d}:{sec:02d}'
    return result_time


for robot in robots:
    robot_name, processing_time = robot.split('-')
    if starting_time == '23:59:59':
        starting_time = '00:00:00'
    robots_info[robot_name] = [int(processing_time), starting_time]


detail = input()
products.append(detail)
current_time = starting_time

while products:
    current_time = time(current_time)
    # checking if there is free robot to process the detail
    for robot in robots_info:
        if current_time >= robots_info[robot][1]:
            # time when robot is registered for proceeding the detail
            print(f'{robot} - {products[0]} [{current_time}]')
            robots_info[robot][1] = robot_time_when_free(current_time,robots_info[robot][0])
            products.popleft()
            break
    else:
        products.rotate(-1)

    if not end_products:
        detail = input()
    else:
        continue
    if detail == 'End':
        end_products = True
        continue
    products.append(detail)
    products.rotate(1)