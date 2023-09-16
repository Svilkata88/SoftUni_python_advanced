# read how many pumps we have on the road
petrol_pumps = int(input())

# variables needed
pumps_info = []
petrol_in_the_tank = 0
first_petrol_pump = 0

# read pumps info for every line
for _ in range(petrol_pumps):
    info = [int(x) for x in input().split()]
    pumps_info.append(info)

# logic
for index in range(len(pumps_info)):
    petrol_filled, distance = pumps_info[index]
    petrol_in_the_tank += petrol_filled
    if petrol_in_the_tank >= distance:
        petrol_in_the_tank -= distance
    else:
        first_petrol_pump = index + 1
        petrol_in_the_tank = 0

# output
print(first_petrol_pump)